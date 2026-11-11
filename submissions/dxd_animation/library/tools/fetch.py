#!/usr/bin/env python3
"""Stage S5 of the Peircean triad library: resolve DOIs, save their records, fetch an open copy.

Run from the library folder:
    python3 -I tools/fetch.py DOI [DOI ...]
    python3 -I tools/fetch.py --list dois.txt
    python3 -I tools/fetch.py --skip-host HOST [--skip-host HOST ...] DOI [DOI ...]
    python3 -I tools/fetch.py --records-only --key KEY DOI
    python3 -I tools/fetch.py --key KEY --url URL [--url URL2 ...] DOI
    python3 -I tools/fetch.py --key KEY --openalex-id W_ID [--search-openlibrary "title" "author"]
    python3 -I tools/fetch.py --key KEY --openlibrary ISBN

Per DOI: the Crossref record (doi.org CSL JSON when Crossref answers 404) is saved to PDF_ROOT/<key>/.
The OpenAlex record is used only when Crossref has none, and then only with --key. Then one copy is
sought: the --url copies in the order given, then the OpenAlex open-access candidates. Only a PDF
counts. --records-only skips the copy search. The keyed lookups take no DOI and save openalex.json,
openlibrary.json or openlibrary_search.json in the key folder. Each run appends one row to
FETCH_LOG.tsv. Standard library only. pdftotext and pdfinfo (poppler) must be on PATH.
"""

import argparse
import hashlib
import html
import html.parser
import json
import os
import re
import shutil
import socket
import string
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import namedtuple

LIB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(LIB_DIR, "FETCH_LOG.tsv")
PDF_ROOT = "/Users/ludwitt/iit-playground/dxd_animation_local/pdfs"

LOG_COLUMNS = ["key", "doi", "oa_route", "url", "http", "bytes", "sha256", "txt_bytes", "pages", "status"]
API_UA = "algorithmacy-dxd-animation-library/1.0 (stdlib urllib)"
BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
              "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")
API_HEADERS = {"User-Agent": API_UA, "Accept": "application/json"}
CSL_HEADERS = {"User-Agent": API_UA, "Accept": "application/vnd.citationstyles.csl+json"}
PAGE_HEADERS = {"User-Agent": BROWSER_UA,
                "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9"}

TIMEOUT = 90           # seconds per request
PAUSE = 2.0            # minimum seconds between request starts
RATE_WAIT = 30         # seconds to wait after HTTP 429, then one retry
OPENLIBRARY = "https://openlibrary.org"
TEXT_MIN = 2000        # text bytes for status open
HTML_TEXT_MIN = 40000  # text bytes a landing page needs, with the title, to count as full text
ARTICLES = ("a", "an", "the")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([a-z\-]+/\d{7}|\d{4}\.\d{4,5})", re.I)
TRANSLIT = str.maketrans({
    "ø": "o", "Ø": "O", "ł": "l", "Ł": "L", "đ": "d", "Đ": "D", "ð": "d", "Ð": "D",
    "ħ": "h", "Ħ": "H", "ı": "i", "þ": "th", "Þ": "Th", "ß": "ss", "æ": "ae", "Æ": "AE",
    "œ": "oe", "Œ": "OE",
})

SKIP_HOSTS = []        # set by --skip-host
_last_start = [0.0]
Resp = namedtuple("Resp", "status body url ctype error")


def say(msg=""):
    print(msg, flush=True)


# ---- network ------------------------------------------------------------------

def pace():
    """Keep at least PAUSE seconds between request starts."""
    gap = time.time() - _last_start[0]
    if gap < PAUSE:
        time.sleep(PAUSE - gap)
    _last_start[0] = time.time()


def is_timeout(err):
    reason = getattr(err, "reason", err)
    return isinstance(reason, (socket.timeout, TimeoutError))


def http_get(url, headers):
    """GET url. A timeout is retried once; HTTP 429 waits RATE_WAIT seconds and is retried once.

    status is None when no HTTP status arrived.
    """
    url = urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~-._")
    retried = set()
    while True:
        pace()
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return Resp(resp.status, resp.read(), resp.geturl(),
                            resp.headers.get("Content-Type", ""), None)
        except urllib.error.HTTPError as err:
            if err.code == 429 and "429" not in retried:
                retried.add("429")
                say(f"          HTTP 429; waiting {RATE_WAIT} s, then one retry")
                time.sleep(RATE_WAIT)
                continue
            return Resp(err.code, b"", url, "", f"HTTP Error {err.code}: {err.reason}")
        except Exception as err:
            if is_timeout(err):
                if "timeout" not in retried:
                    retried.add("timeout")
                    say("          timeout; retrying once")
                    continue
                return Resp(None, b"", url, "", "timeout")
            return Resp(None, b"", url, "", f"{type(err).__name__}: {err}"[:200])


def note(resp):
    return resp.error or f"HTTP {resp.status}"


def parse_json(body):
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None


def quoted_doi(doi):
    return urllib.parse.quote(doi, safe="/:;()")


def fetch_record(doi):
    """Crossref works record, or doi.org CSL JSON when Crossref answers 404.

    Returns (file name, body, message dict, note). The message is None when the DOI did not resolve.
    """
    q = quoted_doi(doi)
    cr = http_get(f"https://api.crossref.org/works/{q}", API_HEADERS)
    if cr.status == 200:
        data = parse_json(cr.body)
        if isinstance(data, dict) and isinstance(data.get("message"), dict):
            return "crossref.json", cr.body, data["message"], "Crossref 200"
        return None, b"", None, "Crossref 200 but not a works record"
    if cr.status != 404:
        return None, b"", None, f"Crossref {note(cr)}"
    csl = http_get(f"https://doi.org/{q}", CSL_HEADERS)
    if csl.status == 200:
        data = parse_json(csl.body)
        if isinstance(data, dict):
            return "csl.json", csl.body, data, "Crossref 404; doi.org CSL 200"
        return None, b"", None, "Crossref 404; doi.org 200 but not CSL JSON"
    return None, b"", None, f"Crossref 404; doi.org {note(csl)}"


def fetch_openalex(doi):
    """OpenAlex work record. Returns (body or None, dict or None, note)."""
    r = http_get(f"https://api.openalex.org/works/https://doi.org/{quoted_doi(doi)}", API_HEADERS)
    if r.status == 200:
        data = parse_json(r.body)
        if isinstance(data, dict):
            return r.body, data, "200"
        return None, None, "200 but not JSON"
    return None, None, note(r)


def fetch_openalex_id(wid):
    """OpenAlex work by ID, such as W2071014039. Returns (body or None, dict or None, note)."""
    wid = wid.strip()
    if not re.fullmatch(r"W\d+", wid):
        return None, None, f"not an OpenAlex work ID: {wid!r}"
    r = http_get(f"https://api.openalex.org/works/{wid}", API_HEADERS)
    if r.status == 200:
        data = parse_json(r.body)
        if isinstance(data, dict):
            return r.body, data, "200"
        return None, None, "200 but not JSON"
    return None, None, note(r)


# ---- Open Library (no DOI; used for books) ------------------------------------

def openlibrary_isbn(isbn):
    """Edition for an ISBN, and its work when the edition names one.

    Returns (document or None, note). The document is {"isbn", "edition", "work"}.
    """
    clean = re.sub(r"[\s-]", "", isbn)
    ed = http_get(f"{OPENLIBRARY}/isbn/{clean}.json", API_HEADERS)
    edition = parse_json(ed.body) if ed.status == 200 else None
    if not isinstance(edition, dict):
        return None, f"isbn {clean}: {note(ed)}"
    work, notes = None, [f"isbn {clean} 200"]
    works = edition.get("works")
    if isinstance(works, list) and works and isinstance(works[0], dict) and works[0].get("key"):
        wkey = works[0]["key"]
        wr = http_get(f"{OPENLIBRARY}{wkey}.json", API_HEADERS)
        work = parse_json(wr.body) if wr.status == 200 else None
        notes.append(f"work {wkey} {'200' if work is not None else note(wr)}")
    return {"isbn": clean, "edition": edition, "work": work}, "; ".join(notes)


def openlibrary_search(title, author):
    """Open Library search by title and author. Returns (document or None, note, top hits)."""
    query = urllib.parse.urlencode({"title": title, "author": author, "limit": 5,
                                    "fields": "key,title,author_name,first_publish_year,publisher,isbn,edition_count"})
    r = http_get(f"{OPENLIBRARY}/search.json?{query}", API_HEADERS)
    data = parse_json(r.body) if r.status == 200 else None
    if not isinstance(data, dict):
        return None, note(r), []
    docs = [d for d in (data.get("docs") or [])[:5] if isinstance(d, dict)]
    return data, f"200, {len(docs)} top hits of {data.get('numFound', '?')}", docs


def print_edition(doc):
    ed = doc.get("edition") or {}
    work = doc.get("work") or {}
    say(f"  edition: {ed.get('title') or '-'} | publish_date {ed.get('publish_date') or '-'} | "
        f"publishers {'; '.join(ed.get('publishers') or []) or '-'} | "
        f"isbn_13 {', '.join(ed.get('isbn_13') or []) or '-'} | pages {ed.get('number_of_pages') or '-'}")
    if work:
        say(f"  work:    {work.get('title') or '-'} | first_publish_date {work.get('first_publish_date') or '-'} "
            f"| key {work.get('key') or '-'}")


def print_hits(docs):
    for i, d in enumerate(docs, 1):
        say(f"  hit {i}: {d.get('title') or '-'} | {'; '.join(d.get('author_name') or []) or '-'} | "
            f"first_publish_year {d.get('first_publish_year') or '-'} | key {d.get('key') or '-'}")
        say(f"          publishers: {'; '.join((d.get('publisher') or [])[:6]) or '-'}")
        say(f"          ISBNs: {', '.join(d.get('isbn') or []) or '-'}")


# ---- key ----------------------------------------------------------------------

def letters(text):
    """Lowercase a-z only. Diacritics fold to ASCII; every other character is dropped."""
    folded = unicodedata.normalize("NFKD", str(text).translate(TRANSLIT))
    folded = folded.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z]", "", folded.lower())


def clean_title(raw):
    if isinstance(raw, list):
        raw = raw[0] if raw else ""
    text = re.sub(r"<[^>]+>", " ", str(raw or ""))
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def first_author(msg):
    for role in ("author", "editor"):
        people = msg.get(role)
        if isinstance(people, list) and people and isinstance(people[0], dict):
            return people[0], role
    return None, ""


def surname(person):
    if not person:
        return ""
    for field in ("family", "literal", "name"):
        if person.get(field):
            return str(person[field])
    return ""


def year_of(msg):
    for field in ("issued", "published-print", "created"):
        date = msg.get(field)
        parts = date.get("date-parts") if isinstance(date, dict) else None
        if isinstance(parts, list) and parts and isinstance(parts[0], list) and parts[0] and parts[0][0]:
            return str(parts[0][0]), field
    return "", ""


def derive(msg):
    """Key parts from a Crossref-shaped record. Flags name anything a human should check."""
    title = clean_title(msg.get("title"))
    person, role = first_author(msg)
    raw = surname(person)
    sur = letters(raw)
    year, year_src = year_of(msg)
    first = ""
    for word in title.split():
        w = letters(word)
        if w and w not in ARTICLES:
            first = w
            break
    flags = []
    if person is None:
        flags.append("no author or editor on the record")
    elif role == "editor":
        flags.append("no author; surname taken from the editor")
    if not sur:
        flags.append("no surname letters")
    if not year:
        flags.append("no year on the record")
    if not first:
        flags.append("no title word")
    if raw and (re.search(r"[\s'\-.]", raw) or re.search(r"[^\x00-\x7f]", raw)):
        flags.append(f"surname {raw!r} folded to {sur!r}")
    return {"base": f"{sur or 'anon'}{year or 'nd'}{first}", "title": title, "year": year,
            "year_src": year_src, "person": person, "flags": flags}


def folder_owner(folder):
    """DOI in a key folder's records, lowercased. None when the folder or a readable record is absent."""
    if not os.path.isdir(folder):
        return None
    for name in ("crossref.json", "csl.json", "openalex.json"):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        with open(path, "rb") as f:
            data = parse_json(f.read())
        if not isinstance(data, dict):
            continue
        if name == "openalex.json":
            doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", str(data.get("doi") or ""), flags=re.I)
        else:
            msg = data["message"] if isinstance(data.get("message"), dict) else data
            doi = str(msg.get("DOI") or "")
        if doi:
            return doi.lower()
    return None


def claim_key(base, doi):
    """The base key, or base + a, b, ... while another DOI's records hold the folder (library README)."""
    for suffix in [""] + list(string.ascii_lowercase):
        key = base + suffix
        folder = os.path.join(PDF_ROOT, key)
        if folder_owner(folder) in (None, doi.lower()):
            return key, folder
    raise RuntimeError(f"no free key for {base}")


# ---- open copies --------------------------------------------------------------

def host_of(url):
    return (urllib.parse.urlsplit(url).hostname or "").lower()


def excluded(host):
    return any(host == h or host.endswith("." + h) for h in SKIP_HOSTS)


def arxiv_ids(doi, oa):
    ids = []
    m = re.match(r"10\.48550/arxiv\.(.+)$", doi, re.I)
    if m:
        ids.append(m.group(1))
    if oa:
        blob = json.dumps({k: oa.get(k) for k in ("ids", "primary_location", "best_oa_location",
                                                    "locations", "open_access")}, ensure_ascii=False)
        ids += ARXIV_RE.findall(blob)
    return list(dict.fromkeys(ids))


BITSTREAM_RE = re.compile(
    r"/bitstreams/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/download", re.I)


def dspace_content_url(url):
    """DSpace REST content URL for a /bitstreams/<uuid>/download URL, on the same host; else None."""
    parts = urllib.parse.urlsplit(url)
    m = BITSTREAM_RE.search(parts.path)
    if not m:
        return None
    return f"{parts.scheme}://{parts.netloc}/server/api/core/bitstreams/{m.group(1)}/content"


def with_dspace(items):
    """Each (route, url, kind), then its DSpace REST content URL when the URL is a DSpace bitstream."""
    out = []
    for route, url, kind in items:
        out.append((route, url, kind))
        rest = dspace_content_url(url) if isinstance(url, str) and url else None
        if rest:
            out.append(("dspace_rest", rest, "pdf"))
    return out


def admit(items):
    """Keep (route, url, kind) items in order; drop repeated URLs and excluded hosts."""
    out, seen = [], set()
    for route, url, kind in items:
        if not isinstance(url, str) or not url or url in seen:
            continue
        seen.add(url)
        if excluded(host_of(url)):
            say(f"  skip:   {route} {url} (host excluded)")
            continue
        out.append((route, url, kind))
    return out


def explicit_route(url):
    """Route name for a copy given with --url. arXiv and PMC keep their own names."""
    host = host_of(url)
    if host == "arxiv.org" or host.endswith(".arxiv.org"):
        return "arxiv_preprint"
    if host.endswith("ncbi.nlm.nih.gov"):
        return "pmc"
    return "explicit_url"


def explicit_candidates(urls):
    """Copies given with --url, in the order given, as (route, url, 'pdf')."""
    return admit(with_dspace([(explicit_route(url), url, "pdf") for url in urls]))


def candidates(doi, oa):
    """Copies to try, in the plan's order, as (route, url, kind).

    kind 'pdf' accepts only a PDF; kind 'landing' also accepts full-text HTML.
    """
    oa = oa or {}
    best = oa.get("best_oa_location") or {}
    locations = [loc for loc in (oa.get("locations") or []) if isinstance(loc, dict)]
    oa_locs = [loc for loc in locations if loc.get("is_oa")]
    plan = [("openalex_best_oa_pdf", best.get("pdf_url"), "pdf")]
    plan += [("openalex_location_pdf", loc.get("pdf_url"), "pdf") for loc in oa_locs]
    plan += [("openalex_oa_url", (oa.get("open_access") or {}).get("oa_url"), "pdf")]
    plan += [("openalex_landing", best.get("landing_page_url"), "landing")]
    plan += [("openalex_landing", loc.get("landing_page_url"), "landing") for loc in oa_locs]
    plan += [("arxiv_pdf", f"https://arxiv.org/pdf/{ident}", "pdf") for ident in arxiv_ids(doi, oa)]
    return admit(with_dspace(plan))


class _PageText(html.parser.HTMLParser):
    SKIP = ("script", "style", "noscript", "template")
    BLOCK = ("p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section",
             "article", "table", "blockquote", "figure", "figcaption")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.hidden += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.hidden = max(0, self.hidden - 1)
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def html_text(raw):
    parser = _PageText()
    parser.feed(raw.decode("utf-8", "replace"))
    parser.close()
    text = "".join(parser.parts)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip() + "\n"


def looks_html(resp):
    if "html" in (resp.ctype or "").lower():
        return True
    return re.search(rb"<(!doctype\s+html|html|head|body)\b", resp.body[:8192], re.I) is not None


def full_text_check(text, title):
    size = len(text.encode("utf-8"))
    if size <= HTML_TEXT_MIN:
        return False, f"{size} text bytes, not more than {HTML_TEXT_MIN}"
    want = letters(clean_title(title))
    if not want:
        return False, "no title to match"
    if want not in letters(text):
        return False, f"title not found in {size} text bytes"
    return True, f"full text: {size} text bytes, title found"


def write_bytes(path, data):
    with open(path, "wb") as f:
        f.write(data)


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_pages(pdf):
    try:
        res = subprocess.run(["pdfinfo", pdf], capture_output=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired):
        return ""
    match = re.search(rb"^Pages:\s+(\d+)", res.stdout, re.M)
    return match.group(1).decode("ascii") if match else ""


def save_pdf(folder, key, route, url, body, status):
    pdf = os.path.join(folder, key + ".pdf")
    txt = os.path.join(folder, key + ".txt")
    write_bytes(pdf, body)
    sha = hashlib.sha256(body).hexdigest()
    write_text(os.path.join(folder, "sha256.txt"), f"{sha}  {key}.pdf\n")
    if os.path.exists(txt):
        os.remove(txt)
    try:
        res = subprocess.run(["pdftotext", "-layout", pdf, txt], capture_output=True, timeout=300)
        ok = res.returncode == 0
        if not ok:
            say(f"          pdftotext exit {res.returncode}")
    except (OSError, subprocess.TimeoutExpired) as err:
        ok = False
        say(f"          pdftotext: {err}")
    txt_bytes = 0
    if ok and os.path.exists(txt):
        txt_bytes = os.path.getsize(txt)
    elif os.path.exists(txt):
        os.remove(txt)
    return {"oa_route": route, "url": url, "http": str(status), "bytes": len(body), "sha256": sha,
            "txt_bytes": txt_bytes, "pages": pdf_pages(pdf),
            "status": "open" if txt_bytes >= TEXT_MIN else "no_text_layer"}


def save_html(folder, key, url, body, text, status):
    raw = text.encode("utf-8")
    sha = hashlib.sha256(body).hexdigest()
    write_bytes(os.path.join(folder, key + ".html"), body)
    write_bytes(os.path.join(folder, key + ".txt"), raw)
    write_text(os.path.join(folder, "sha256.txt"), f"{sha}  {key}.html\n")
    return {"oa_route": "html", "url": url, "http": str(status), "bytes": len(body), "sha256": sha,
            "txt_bytes": len(raw), "pages": "",
            "status": "open" if len(raw) >= TEXT_MIN else "no_text_layer"}


def existing_copy(folder, key):
    pdf = os.path.join(folder, key + ".pdf")
    txt = os.path.join(folder, key + ".txt")
    return {"oa_route": "", "url": "", "http": "", "bytes": os.path.getsize(pdf),
            "sha256": sha256_file(pdf),
            "txt_bytes": os.path.getsize(txt) if os.path.exists(txt) else 0,
            "pages": pdf_pages(pdf), "status": "exists"}


def search_copy(folder, key, cands, title):
    """Try candidates in order. Returns (row fields or None, last URL, last HTTP note)."""
    last_url = ""
    last_http = "" if cands else "no candidates"
    for route, url, kind in cands:
        resp = http_get(url, PAGE_HEADERS)
        last_url = resp.url or url
        say(f"  try:    {route} {url}")
        if resp.error:
            last_http = resp.error
            say(f"          {resp.error}")
            continue
        if excluded(host_of(last_url)):
            last_http = f"{resp.status} redirected to an excluded host"
            say(f"          redirected to an excluded host ({host_of(last_url)}); not accepted")
            continue
        if resp.body[:5] == b"%PDF-":
            say(f"          PDF, {len(resp.body)} bytes")
            return save_pdf(folder, key, route, last_url, resp.body, resp.status), last_url, ""
        last_http = f"{resp.status} non-pdf ({len(resp.body)} bytes)"
        if kind == "landing" and looks_html(resp):
            text = html_text(resp.body)
            ok, why = full_text_check(text, title)
            say(f"          HTML: {why}")
            if ok:
                return save_html(folder, key, last_url, resp.body, text, resp.status), last_url, ""
        else:
            say(f"          not a PDF ({resp.ctype or 'no content type'})")
    return None, last_url, last_http


# ---- one DOI, and the batch ---------------------------------------------------

def append_log(row):
    cells = [re.sub(r"[\t\r\n]+", " ", str(row.get(c, ""))) for c in LOG_COLUMNS]
    fresh = not os.path.exists(LOG_PATH) or os.path.getsize(LOG_PATH) == 0
    lacks_newline = False
    if not fresh:
        with open(LOG_PATH, "rb") as f:
            f.seek(-1, os.SEEK_END)
            lacks_newline = f.read(1) != b"\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        if fresh:
            f.write("\t".join(LOG_COLUMNS) + "\n")
        elif lacks_newline:
            f.write("\n")
        f.write("\t".join(cells) + "\n")


def copy_result(doi, key, folder, title, opts):
    """Try the --url copies in order, then the OpenAlex candidates. Returns the log fields."""
    last_url, last_http = "", ""
    explicit = explicit_candidates(opts.url)
    if explicit:
        result, last_url, last_http = search_copy(folder, key, explicit, title)
        if result is not None:
            return result
    oa_body, oa, oa_note = fetch_openalex(doi)
    say(f"  openalex: {oa_note}")
    if oa_body is not None:
        write_bytes(os.path.join(folder, "openalex.json"), oa_body)
    result, url, http = search_copy(folder, key, candidates(doi, oa), title)
    if result is not None:
        return result
    notes = [n for n in (last_http, http) if n and n != "no candidates"]
    return {"oa_route": "", "url": url or last_url, "http": "; ".join(notes) or "no candidates", "bytes": 0,
            "sha256": "", "txt_bytes": 0, "pages": "", "status": "closed"}


def process_doi(doi, index, total, opts):
    say(f"\n[{index}/{total}] {doi}")
    name, body, msg, rec_note = fetch_record(doi)
    if msg is None:
        say(f"  UNRESOLVED: {rec_note}")
        oa_body, oa, oa_note = fetch_openalex(doi)
        say(f"  openalex: {oa_note}")
        if oa_body is not None and opts.key:
            folder = os.path.join(PDF_ROOT, opts.key)
            os.makedirs(folder, exist_ok=True)
            write_bytes(os.path.join(folder, "openalex.json"), oa_body)
            append_log({"key": opts.key, "doi": doi, "oa_route": "", "url": "",
                        "http": f"{rec_note}; openalex {oa_note} (no Crossref record, so the OpenAlex record was saved)",
                        "bytes": 0, "sha256": "", "txt_bytes": 0, "pages": "", "status": "records-only"})
            say("  RESULT: records-only (OpenAlex record)")
            return {"doi": doi, "key": opts.key, "title": "", "year": "", "status": "records-only",
                    "oa_route": "", "pages": "", "txt_bytes": 0}
        why = "; OpenAlex has a record, so rerun with --key KEY" if oa_body is not None else ""
        append_log({"key": opts.key or "", "doi": doi, "oa_route": "", "url": "", "http": rec_note + why,
                    "bytes": 0, "sha256": "", "txt_bytes": 0, "pages": "", "status": "unresolved"})
        return {"doi": doi, "key": "", "title": "", "year": "", "status": "unresolved",
                "oa_route": "", "pages": "", "txt_bytes": 0}
    info = derive(msg)
    say(f"  record: {name} ({rec_note})")
    say(f"  key:    {info['base']}   year {info['year'] or '-'} [{info['year_src'] or '-'}]")
    say(f"  title:  {info['title']}")
    say(f"  author: {json.dumps(info['person'], ensure_ascii=False) if info['person'] else 'none'}")
    for flag in info["flags"]:
        say(f"  CHECK:  {flag}")
    if opts.key:
        key, folder = opts.key, os.path.join(PDF_ROOT, opts.key)
        owner = folder_owner(folder)
        if owner not in (None, doi.lower()):
            raise RuntimeError(f"{key} is held by {owner}; this DOI is {doi}")
        if key != info["base"]:
            say(f"  CHECK:  --key {key} differs from the derived key {info['base']}")
    else:
        key, folder = claim_key(info["base"], doi)
        if key != info["base"]:
            owner = folder_owner(os.path.join(PDF_ROOT, info["base"]))
            say(f"  CHECK:  {info['base']} is held by {owner}; this DOI takes {key}")
    os.makedirs(folder, exist_ok=True)
    write_bytes(os.path.join(folder, name), body)
    if opts.records_only:
        row = {"oa_route": "", "url": "", "http": f"{rec_note}; records only", "bytes": 0, "sha256": "",
               "txt_bytes": 0, "pages": "", "status": "records-only"}
    elif os.path.exists(os.path.join(folder, key + ".pdf")):
        row = existing_copy(folder, key)
        say("  PDF already in the key folder; download skipped")
    else:
        row = copy_result(doi, key, folder, info["title"], opts)
    row = dict(row, key=key, doi=doi)
    append_log(row)
    say(f"  RESULT: {row['status']}  route={row['oa_route'] or '-'}  pages={row['pages'] or '-'}  "
        f"txt_bytes={row['txt_bytes']}")
    return {"doi": doi, "key": key, "title": info["title"], "year": info["year"],
            "status": row["status"], "oa_route": row["oa_route"], "pages": row["pages"],
            "txt_bytes": row["txt_bytes"]}


def process_keyed(opts, index, total):
    """OpenAlex by ID and Open Library by ISBN or search, for a work with no DOI. One log row per run."""
    key = opts.key
    say(f"\n[{index}/{total}] {key} (no DOI)")
    folder = os.path.join(PDF_ROOT, key)
    os.makedirs(folder, exist_ok=True)
    notes = []
    if opts.openalex_id:
        body, oa, oa_note = fetch_openalex_id(opts.openalex_id)
        say(f"  openalex {opts.openalex_id}: {oa_note}")
        notes.append(f"openalex {opts.openalex_id} {oa_note}")
        if body is not None:
            write_bytes(os.path.join(folder, "openalex.json"), body)
            say(f"  title:  {clean_title(oa.get('display_name') or oa.get('title'))} | "
                f"publication_year {oa.get('publication_year') or '-'} | type {oa.get('type') or '-'}")
    if opts.openlibrary:
        doc, ol_note = openlibrary_isbn(opts.openlibrary)
        say(f"  openlibrary: {ol_note}")
        notes.append(f"openlibrary {ol_note}")
        if doc is not None:
            write_text(os.path.join(folder, "openlibrary.json"),
                       json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
            print_edition(doc)
    if opts.search_openlibrary:
        title, author = opts.search_openlibrary
        data, s_note, docs = openlibrary_search(title, author)
        say(f"  openlibrary search: {s_note}")
        notes.append(f"openlibrary search {s_note}")
        if data is not None:
            write_text(os.path.join(folder, "openlibrary_search.json"),
                       json.dumps(data, ensure_ascii=False, indent=1) + "\n")
            print_hits(docs)
    append_log({"key": key, "doi": "", "oa_route": "", "url": "", "http": "; ".join(notes), "bytes": 0,
                "sha256": "", "txt_bytes": 0, "pages": "", "status": "records-only"})
    say("  RESULT: records-only")
    return {"doi": "", "key": key, "title": "", "year": "", "status": "records-only", "oa_route": "",
            "pages": "", "txt_bytes": 0}


def normalize_doi(raw):
    return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", raw.strip(), flags=re.I).strip()


def read_list(path):
    dois = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                dois.append(line.split(" #", 1)[0].strip())
    return dois


def main(argv=None):
    global SKIP_HOSTS
    parser = argparse.ArgumentParser(description="Stage S5: resolve DOIs and fetch an open copy.")
    parser.add_argument("dois", nargs="*", help="DOIs to process")
    parser.add_argument("--list", dest="list_file", help="file with one DOI per line; # starts a comment")
    parser.add_argument("--skip-host", action="append", default=[], metavar="HOST",
                        help="never accept a copy from this host, even after a redirect (repeatable)")
    parser.add_argument("--key", help="folder name under PDF_ROOT for one work")
    parser.add_argument("--url", action="append", default=[], metavar="URL",
                        help="copy URL to try first, in the order given; only a PDF counts "
                             "(repeatable; needs --key and one DOI)")
    parser.add_argument("--records-only", action="store_true",
                        help="save the registry records and log records-only; search no copy")
    parser.add_argument("--openalex-id", metavar="W_ID",
                        help="save this OpenAlex work as openalex.json (needs --key; no DOI)")
    parser.add_argument("--openlibrary", metavar="ISBN",
                        help="save this Open Library edition and work as openlibrary.json "
                             "(needs --key; no DOI)")
    parser.add_argument("--search-openlibrary", nargs=2, metavar=("TITLE", "AUTHOR"),
                        help="search Open Library, save openlibrary_search.json and print the top hits "
                             "(needs --key; no DOI)")
    args = parser.parse_args(argv)
    keyed = bool(args.openalex_id or args.openlibrary or args.search_openlibrary)
    raw = (read_list(args.list_file) if args.list_file else []) + args.dois
    dois = []
    for item in raw:
        doi = normalize_doi(item)
        if not re.match(r"^10\.\d{4,9}/\S+$", doi):
            say(f"skipped, not a DOI: {item!r}")
        elif doi.lower() not in (d.lower() for d in dois):
            dois.append(doi)
    if keyed:
        if dois:
            parser.error("the OpenAlex and Open Library lookups take no DOI")
        if not args.key:
            parser.error("the OpenAlex and Open Library lookups need --key")
        if args.url:
            parser.error("--url needs a DOI")
    else:
        if not dois:
            parser.error("no DOIs given")
        if args.key and len(dois) != 1:
            parser.error("--key names one work, so give exactly one DOI")
        if args.url and not args.key:
            parser.error("--url needs --key")
    for tool in ("pdftotext", "pdfinfo"):
        if shutil.which(tool) is None:
            sys.exit(f"{tool} not found on PATH")
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    SKIP_HOSTS = [h.strip().lower() for h in args.skip_host if h.strip()]
    jobs = [None] if keyed else dois
    results = []
    for index, doi in enumerate(jobs, 1):
        try:
            if keyed:
                results.append(process_keyed(args, index, len(jobs)))
            else:
                results.append(process_doi(doi, index, len(jobs), args))
        except Exception as err:  # one bad item must not stop the batch; its log row says so
            text = f"{type(err).__name__}: {err}"
            say(f"  ERROR: {text}")
            append_log({"key": args.key or "", "doi": doi or "", "http": text[:200], "status": "error",
                        "bytes": 0, "txt_bytes": 0})
            results.append({"doi": doi or "", "key": args.key or "", "title": "", "year": "",
                            "status": "error", "oa_route": "", "pages": "", "txt_bytes": 0})
    say("\nSUMMARY")
    say("\t".join(["doi", "key", "title", "year", "status", "oa_route", "pages", "txt_bytes"]))
    for r in results:
        say("\t".join([r["doi"], r["key"], r["title"][:60], r["year"], r["status"], r["oa_route"],
                       r["pages"], str(r["txt_bytes"])]))
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    say("counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    main()
