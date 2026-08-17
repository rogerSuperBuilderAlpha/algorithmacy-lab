#!/usr/bin/env python3
"""Render references.bib into Intellect Harvard for Hospitality & Society.

House rules (JOURNAL_SPEC.md, from HOSP_NFC_May_26.pdf):
  - year of publication in brackets
  - commas, not full stops, between parts of each reference
  - no 'no.' for the journal number; a colon between volume and number
  - 'pp.' before page extents
  - article titles in single quotes, journal and book titles italic
  - 'Anon.' where there is no author
  - the list is titled 'References' and holds only works cited in the text

Entries marked DO-NOT-CITE in their note field are refused, loudly.

Usage: python3 render_refs.py --cited cited_keys.txt
"""
import argparse
import re
import sys
from pathlib import Path

BIB = Path(__file__).resolve().parent.parent / "literature" / "references.bib"


def parse_bib(text):
    entries = {}
    for block in re.split(r"\n@", text)[1:]:
        m = re.match(r"(\w+)\s*\{\s*([^,]+),", block)
        if not m:
            continue
        kind, key = m.group(1).lower(), m.group(2).strip()
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", block):
            name, i, depth, buf = fm.group(1).lower(), fm.end(), 1, []
            while i < len(block) and depth:
                c = block[i]
                depth += (c == "{") - (c == "}")
                if depth:
                    buf.append(c)
                i += 1
            fields[name] = re.sub(r"\s+", " ", "".join(buf)).strip()
        entries[key] = (kind, fields)
    return entries


ACCENTS = {"k": "\u0328", "r": "\u030a", '"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303",
           "c": "\u0327", "v": "\u030c", "=": "\u0304", ".": "\u0307", "u": "\u0306"}


def clean(s):
    """Unescape LaTeX into Unicode. Accents are handled generically, not by table:
    a hardcoded list silently passed \\"a and \\'o straight through to the rendered
    reference list, which is how 'Sch\\"anzel' reached a draft. Braced or bare."""
    import unicodedata
    for a, b in [("\\&", "&"), ("\\#", "#"), ("\\%", "%"), ("\\_", "_"), ("--", "\u2013"), ("``", "\u2018"), ("''", "\u2019"),
                 ("{\\dh}", "\u00f0"), ("{\\TH}", "\u00de"), ("{\\o}", "\u00f8"),
                 ("{\\ss}", "\u00df"), ("{\\aa}", "\u00e5"),
                 ("{\\i}", "\u0131"), ("\\i ", "\u0131"), ("{\\j}", "\u0237"),
                 ("{\\l}", "\u0142"), ("{\\L}", "\u0141"), ("{\\O}", "\u00d8"),
                 ("{\\AA}", "\u00c5"), ("{\\ae}", "\u00e6"), ("{\\AE}", "\u00c6")]:
        s = s.replace(a, b)

    def sub(m):
        mark = ACCENTS.get(m.group(1))
        return unicodedata.normalize("NFC", m.group(2) + mark) if mark else m.group(2)

    s = re.sub(r'\{\\(["\'`^~cvkr=.u])\s*\{?([A-Za-z])\}?\}', sub, s)   # {\"a} {\"{a}} {\k{a}} {\k a}
    s = re.sub(r'\\(["\'`^~cvkr=.u])\s*\{([A-Za-z])\}', sub, s)      # \k{a}  \c{c}  \v{s}
    s = re.sub(r'\\(["\'`^~])\{?([A-Za-z])\}?', sub, s)              # bare \"a
    # single-backtick / straight-apostrophe quotes inside titles, left after `` and '' pass
    s = re.sub(r"`([^`']+)'", "\u2018\\1\u2019", s)
    return s.replace("{", "").replace("}", "").strip()


def authors(raw):
    """Intellect gives full forenames: 'Surname, Firstname and Surname, Firstname'."""
    people = [clean(a).strip() for a in raw.split(" and ")]
    out = []
    for person in people:
        if "," in person:
            surname, given = [p.strip() for p in person.split(",", 1)]
            out.append(f"{surname}, {given}")
        else:
            out.append(person)
    if len(out) == 1:
        return out[0]
    return ", ".join(out[:-1]) + " and " + out[-1]


def render(kind, f, suffix=""):
    who = authors(f["author"]) if "author" in f else "Anon."
    year = f.get("year", "n.d.") + suffix
    title = clean(f.get("title", ""))
    head = f"{who} ({year}), "

    if kind == "article":
        vol = f.get("volume", "")
        num = f.get("number", "")
        vn = f"{vol}:{num}" if vol and num else vol
        pages = clean(f.get("pages", ""))
        bits = [f"'{title}'", f"*{clean(f.get('journal',''))}*"]
        if vn:
            bits.append(vn)
        if pages:
            bits.append(f"pp. {pages}")
        return head + ", ".join(bits) + "."

    if kind == "book":
        addr = clean(f.get("address", ""))
        pub = clean(f.get("publisher", ""))
        return head + f"*{title}*, {addr}: {pub}."

    if kind == "incollection":
        eds = authors(f["editor"]) if f.get("editor") else ""
        pages = clean(f.get("pages", ""))
        lead = f"in {eds} (ed.), " if eds else "in "
        tail = f", pp. {pages}" if pages else ""
        return (head + f"'{title}', {lead}*{clean(f.get('booktitle',''))}*, "
                f"{clean(f.get('address',''))}: {clean(f.get('publisher',''))}{tail}.")

    if kind == "inproceedings":
        pages = clean(f.get("pages", ""))
        tail = f", pp. {pages}" if pages else ""
        return head + f"'{title}', *{clean(f.get('booktitle',''))}*{tail}."

    return head + f"*{title}*."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cited", required=True, help="file of bib keys, one per line")
    args = ap.parse_args()

    entries = parse_bib(BIB.read_text(encoding="utf-8"))
    keys = [l.strip() for l in Path(args.cited).read_text().splitlines()
            if l.strip() and not l.lstrip().startswith("#")]

    missing = [k for k in keys if k not in entries]
    if missing:
        print("ABORT: keys not in references.bib: " + ", ".join(missing), file=sys.stderr)
        return 1

    seen_doi = {}
    for k in keys:
        doi = entries[k][1].get("doi", "").lower().strip()
        if doi and doi in seen_doi:
            print(f"ABORT: {k} and {seen_doi[doi]} are the same work (DOI {doi}). "
                  f"Merge the bib entries before rendering.", file=sys.stderr)
            return 1
        if doi:
            seen_doi[doi] = k

    refused = [k for k in keys if "DO-NOT-CITE" in entries[k][1].get("note", "")]
    if refused:
        print("ABORT: refused DO-NOT-CITE entries: " + ", ".join(refused), file=sys.stderr)
        return 1

    unverified = [k for k in keys
                  if "verified" not in entries[k][1].get("note", "")
                  and "crossref-verified" not in entries[k][1].get("note", "")]
    if unverified:
        print("WARNING: cited but not marked verified: " + ", ".join(unverified), file=sys.stderr)

    # Harvard requires a/b suffixes when the same authors publish twice in one year,
    # and the manuscript already cites them that way ("Lynch et al. 2021a, 2021b").
    # Without this the rendered list printed two bare 2021 entries and the citation
    # check reported a disagreement that was the renderer's, not the author's.
    # The signature is FIRST AUTHOR + year, not the whole author list: two works can
    # share a first author and a year while differing further down the list, and in
    # text they both read "Lynch et al. 2021". That is the collision a reader hits.
    def first_surname(f):
        if "author" not in f:
            return "Anon."
        first = clean(f["author"].split(" and ")[0]).strip()
        return first.split(",")[0].strip() if "," in first else first.split()[-1]

    by_author_year = {}
    for k in keys:
        kind, f = entries[k]
        by_author_year.setdefault((first_surname(f), f.get("year", "n.d.")), []).append(k)
    suffix = {}
    for sig, ks in by_author_year.items():
        if len(ks) > 1 and sig[1] != "n.d.":
            # order by title so the letters are stable across runs
            for i, k in enumerate(sorted(ks, key=lambda k: clean(entries[k][1].get("title", "")).lower())):
                suffix[k] = chr(ord("a") + i)

    rendered = sorted((render(*entries[k], suffix=suffix.get(k, "")) for k in keys),
                      key=lambda s: s.lower())
    print("## References\n")
    for r in rendered:
        print(r + "\n")
    print(f"<!-- {len(rendered)} entries -->", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
