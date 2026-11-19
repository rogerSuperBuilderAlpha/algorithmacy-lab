#!/usr/bin/env python3
"""Run one facet's search queries against OpenAlex, Crossref, Semantic Scholar and arXiv; tag hits already
carded in the three existing libraries; append hits to search/<facet>.jsonl and rows to SEARCH_LOG.md.

Measurement only: it finds records; it writes no card prose and decides nothing.

    python3 -I tools/search.py F1 "query one" "query two" ...
    python3 -I tools/search.py F1 --from FACETS.md      # reads the **Queries:** bullets under "## F1"

Each hit carries: facet, source, query, rank, id, doi, title, year, first_author, venue, type, oa_url,
cited_by, in_registry (the existing key, or null). Registry match: DOI first; else first author surname +
year + normalised-title similarity >= 0.85.
"""
import difflib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.expanduser("~/iit-playground/dxd_animation_local/registry.tsv")
UA = {"User-Agent": "algorithmacy-dxd-animation-library/1.0 (stdlib urllib; research use)"}
TODAY = date.today().isoformat()


def fold(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s)).strip()


def get(url, timeout=60):
    waits = (12, 30, 0)  # three attempts; Semantic Scholar's unauthenticated pool answers 429 freely
    for attempt, wait in enumerate(waits, 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < len(waits):
                time.sleep(wait)
                continue
            raise
        except Exception:
            if attempt < len(waits):
                time.sleep(3)
                continue
            raise


def load_registry():
    by_doi, by_ay = {}, {}
    with open(REG, encoding="utf-8") as f:
        cols = f.readline().rstrip("\n").split("\t")
        for line in f:
            r = dict(zip(cols, line.rstrip("\n").split("\t")))
            if r.get("doi"):
                by_doi[r["doi"].lower()] = r["key"]
            by_ay.setdefault((r.get("first_author", ""), r.get("year", "")), []).append(r)
    return by_doi, by_ay


def in_registry(hit, by_doi, by_ay):
    doi = (hit.get("doi") or "").lower()
    if doi and doi in by_doi:
        return by_doi[doi]
    fa = re.sub(r"[^a-z]", "", fold(hit.get("first_author") or ""))
    yr = str(hit.get("year") or "")[:4]
    nt = fold(hit.get("title") or "")
    for r in by_ay.get((fa, yr), []):
        if nt and r.get("norm_title") and difflib.SequenceMatcher(None, nt, r["norm_title"]).ratio() >= 0.85:
            return r["key"]
    return None


def openalex(q):
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": q, "per-page": 25,
        "select": "id,doi,title,publication_year,type,authorships,primary_location,open_access,cited_by_count"})
    d = json.loads(get(url))
    out = []
    for i, w in enumerate(d.get("results", []), 1):
        au = (w.get("authorships") or [{}])[0].get("author", {}).get("display_name", "")
        out.append({"source": "openalex", "rank": i, "id": w.get("id"),
                    "doi": (w.get("doi") or "").replace("https://doi.org/", "") or None,
                    "title": w.get("title"), "year": w.get("publication_year"),
                    "first_author": au.split()[-1] if au else "", "type": w.get("type"),
                    "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
                    "oa_url": (w.get("open_access") or {}).get("oa_url"), "cited_by": w.get("cited_by_count")})
    return out


def crossref(q):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
        "query.bibliographic": q, "rows": 20,
        "select": "DOI,title,author,issued,container-title,type,is-referenced-by-count"})
    d = json.loads(get(url))
    out = []
    for i, w in enumerate(d.get("message", {}).get("items", []), 1):
        au = (w.get("author") or [{}])[0]
        yr = ((w.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        out.append({"source": "crossref", "rank": i, "id": "doi:" + w.get("DOI", ""), "doi": w.get("DOI"),
                    "title": (w.get("title") or [None])[0], "year": yr,
                    "first_author": au.get("family") or au.get("name", ""), "type": w.get("type"),
                    "venue": (w.get("container-title") or [None])[0], "oa_url": None,
                    "cited_by": w.get("is-referenced-by-count")})
    return out


def semantic(q):
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode({
        "query": q, "limit": 20, "fields": "title,year,authors,externalIds,openAccessPdf,citationCount,venue,publicationTypes"})
    d = json.loads(get(url))
    out = []
    for i, w in enumerate(d.get("data", []), 1):
        au = (w.get("authors") or [{}])[0].get("name", "")
        out.append({"source": "semanticscholar", "rank": i, "id": "s2:" + w.get("paperId", ""),
                    "doi": (w.get("externalIds") or {}).get("DOI"), "title": w.get("title"), "year": w.get("year"),
                    "first_author": au.split()[-1] if au else "", "type": ",".join(w.get("publicationTypes") or []),
                    "venue": w.get("venue"), "oa_url": (w.get("openAccessPdf") or {}).get("url"),
                    "cited_by": w.get("citationCount")})
    return out


def arxiv(q):
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": "all:" + q, "max_results": 10})
    root = ET.fromstring(get(url))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for i, e in enumerate(root.findall("a:entry", ns), 1):
        aid = (e.findtext("a:id", default="", namespaces=ns) or "").rsplit("/", 1)[-1]
        au = e.find("a:author/a:name", ns)
        out.append({"source": "arxiv", "rank": i, "id": "arxiv:" + aid, "doi": None,
                    "title": re.sub(r"\s+", " ", e.findtext("a:title", default="", namespaces=ns)),
                    "year": (e.findtext("a:published", default="", namespaces=ns) or "")[:4],
                    "first_author": (au.text.split()[-1] if au is not None and au.text else ""), "type": "preprint",
                    "venue": "arXiv", "oa_url": f"https://arxiv.org/pdf/{aid}", "cited_by": None})
    return out


SOURCES = [("openalex", openalex), ("crossref", crossref), ("semanticscholar", semantic), ("arxiv", arxiv)]


def queries_from_facets(facet, path):
    text = open(path, encoding="utf-8").read()
    m = re.search(rf"^##\s+{facet}\b.*?(?=^##\s+F\d|\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"no section for {facet} in {path}")
    block = m.group(0)
    qm = re.search(r"\*\*Queries[.:]?\*\*(.*?)(?=\n\*\*[A-Z][a-z]+[.:]?\*\*|\n## |\Z)", block, re.S)
    if not qm:
        sys.exit(f"no **Queries** block under {facet}")
    qs = re.findall(r"`([^`]+)`", qm.group(1))          # inline backticked queries (FACETS.md style)
    if not qs:                                          # or one query per bullet line
        qs = [re.sub(r"^[-*\d.)\s]+", "", l).strip().strip('`"') for l in qm.group(1).splitlines()]
    return [q.replace('"', '').strip() for q in qs if len(q.strip()) > 3]  # APIs need no phrase quotes


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    facet = args[0]
    qs = queries_from_facets(facet, args[2] if len(args) > 2 and args[1] == "--from" else os.path.join(LIB, "FACETS.md")) \
        if "--from" in args else args[1:]
    by_doi, by_ay = load_registry()
    os.makedirs(os.path.join(LIB, "search"), exist_ok=True)
    outp = os.path.join(LIB, "search", f"{facet}.jsonl")
    seen = set()
    if os.path.exists(outp):
        for line in open(outp, encoding="utf-8"):
            try:
                seen.add(json.loads(line).get("id"))
            except Exception:
                pass
    log_rows, n_new = [], 0
    with open(outp, "a", encoding="utf-8") as out:
        for q in qs:
            for name, fn in SOURCES:
                try:
                    hits = fn(q)
                    err = ""
                except Exception as e:
                    hits, err = [], f"{type(e).__name__}: {str(e)[:60]}"
                tops = []
                for h in hits:
                    h.update({"facet": facet, "query": q, "in_registry": in_registry(h, by_doi, by_ay), "date": TODAY})
                    tops.append(h.get("doi") or h.get("id"))
                    if h.get("id") in seen:
                        continue
                    seen.add(h.get("id"))
                    out.write(json.dumps(h, ensure_ascii=False) + "\n")
                    n_new += 1
                note = err or ("; ".join(t for t in tops[:3] if t))
                log_rows.append(f"| {TODAY} | {facet} | {name} | {q.replace('|', '/')} | {len(hits)} | {note.replace('|', '/')} |")
                print(f"{facet} {name:16s} n={len(hits):2d} {q[:60]!r} {err}")
                time.sleep(1.2 if name != "semanticscholar" else 3.5)
    with open(os.path.join(LIB, "SEARCH_LOG.md"), "a", encoding="utf-8") as f:
        f.write(f"\n### {facet} — API searches, {TODAY} (tools/search.py)\n\n| date | facet | source | query | n | top ids / note |\n|---|---|---|---|---|---|\n")
        f.write("\n".join(log_rows) + "\n")
    print(f"{facet}: {len(qs)} queries x {len(SOURCES)} sources; {n_new} new hits appended to search/{facet}.jsonl")


if __name__ == "__main__":
    main()
