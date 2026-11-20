#!/usr/bin/env python3
"""Mechanical precheck of staged cards (PLAN.md §7.1). Judges nothing.

Usage (from run_2026_11/):  python3 -I tools/precheck.py A   -> verify/PRECHECK_A.tsv
                            python3 -I tools/precheck.py B   -> verify/PRECHECK_B.tsv
                            add --no-net to skip the Crossref lookups.
"""
import hashlib, json, os, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
BASIS = {"full-text", "partial-text", "abstract", "secondary"}
SECTIONS = set("Intro 1.1 1.2 1.3 2.1 2.2 2.3 3.1 3.2 3.3 3.4 3.5 3.6 3.7 4.1 4.2 4.3 4.4-medium 4.4-record "
               "4.4-stop 4.4-contest 4.4-loss 5 6-automation 6-paternalism 6-authority 6-smartreader 6-scale "
               "6-cost 6-gaming 6-responsibilization 7-D02 7-D03 7-D04 7-D05 7-D06 7-D07 7-D08 Concl "
               "new-category counter".split())
QUOTE_PAIR = re.compile('["“]([^"“”]*)["”]')  # consumes pairs left to right


def quotes_in(text):
    """Quoted strings of 25+ characters, pairing quote marks in order so gaps between quotes are never taken."""
    # a segment spanning a newline or a locator tag is the gap between two quotes after an odd mark; skip it
    return [m.group(1) for m in QUOTE_PAIR.finditer(text) if len(m.group(1)) >= 25
            and "\n" not in m.group(1) and "[quote" not in m.group(1) and "[paraphrase" not in m.group(1)]
TEXT_EXT = {".txt", ".md", ".html", ".htm"}


def front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip()
    return out, text[m.end():] if m else text


def norm(s):
    s = re.sub(r"-\s*\n\s*", "", s)
    s = s.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                                   "–": "-", "—": "-", "­": ""}))
    return re.sub(r"\s+", " ", s).strip().lower()


def texts_for(path):
    if not path.exists():
        return []
    cands = [path] if path.suffix.lower() in TEXT_EXT else []
    cands += [p for p in sorted(path.parent.glob("*")) if p.suffix.lower() in TEXT_EXT and p != path
              and p.name != "SOURCE_URL.txt"]
    return cands


def locate(quote, files):
    q = norm(quote)
    for f in files:
        raw = f.read_text(errors="replace")
        lines = raw.split("\n")
        # normalise line by line, keeping a char->line map
        buf, owner = [], []
        for i, ln in enumerate(lines, 1):
            piece = ln + "\n"
            buf.append(piece)
            owner.extend([i] * len(piece))
        joined = "".join(buf)
        # normalise while tracking positions approximately: search in normalised text, then map by ratio
        nj = norm(joined)
        idx = nj.find(q)
        if idx >= 0:
            # the quote is present; find its line: first line whose normalised text holds the quote's opening
            # words, else estimate by position ratio (per-line normalising does not sum to the joined length)
            head = q[:30]
            line_no = next((i for i, ln in enumerate(lines, 1) if head[:20] in norm(ln)), None)
            if line_no is None:
                line_no = max(1, round(idx / max(1, len(nj)) * len(lines)))
                where = f"{f.name}:~{line_no}"
            else:
                where = f"{f.name}:{line_no}"
            lo, hi = max(0, line_no - 3), min(len(lines), line_no + 2)
            ctx = " / ".join(x.strip() for x in lines[lo:hi])[:300]
            return where, ctx
    return "NOT FOUND", ""


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": "research-fetch/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                msg = json.load(r)["message"]
            title = (msg.get("title") or [""])[0]
            year = ""
            for k in ("published-print", "published-online", "issued"):
                parts = (msg.get(k) or {}).get("date-parts") or [[None]]
                if parts[0] and parts[0][0]:
                    year = str(parts[0][0]); break
            return title, year
        except Exception as e:  # noqa: BLE001
            if attempt == 2:
                return f"ERROR {type(e).__name__}", ""
            time.sleep(2)
    return "", ""


def main():
    phase = sys.argv[1] if len(sys.argv) > 1 else "A"
    net = "--no-net" not in sys.argv
    rows = [["citekey", "facet", "field_issues", "sha256", "quote_no", "located", "context", "doi_title", "doi_year"]]
    for card in sorted((HERE / "cards").glob("*.md")):
        fm, body = front(card.read_text(errors="replace"))
        if not fm.get("facet", "").startswith(phase):
            continue
        issues = []
        if fm.get("source_basis") not in BASIS:
            issues.append("source_basis")
        if not fm.get("pages_read"):
            issues.append("pages_read")
        secs = [s.strip() for s in fm.get("structure_sections", "").split(";") if s.strip()]
        if not secs or any(s not in SECTIONS for s in secs):
            issues.append("structure_sections")
        lp = Path(os.path.expanduser(fm.get("local_path", "") or "/nonexistent"))
        if lp.is_file():
            got = hashlib.sha256(lp.read_bytes()).hexdigest()
            sha = "match" if got == fm.get("sha256") else f"MISMATCH {got[:12]}"
        else:
            sha = "NO FILE"
        doi = fm.get("doi", "null")
        t, y = (crossref(doi) if net and doi not in ("", "null") else ("", ""))
        km = re.search(r"## Key facts it relies on\n(.*?)(\n## |\Z)", body, re.S)
        quotes = quotes_in(km.group(1)) if km else []
        files = texts_for(lp)
        base = [fm.get("citekey", card.stem), fm.get("facet", ""), ",".join(issues) or "ok", sha]
        if not quotes:
            rows.append(base + ["0", "-", "", t, y])
        for n, q in enumerate(quotes, 1):
            loc, ctx = locate(q, files) if files else ("NO TEXT FILE", "")
            rows.append(base + [str(n), loc, ctx.replace("\t", " "), t if n == 1 else "", y if n == 1 else ""])
    out = HERE / "verify" / f"PRECHECK_{phase}.tsv"
    out.write_text("\n".join("\t".join(r) for r in rows) + "\n")
    print(f"{out}: {len(rows) - 1} rows")


if __name__ == "__main__":
    main()
