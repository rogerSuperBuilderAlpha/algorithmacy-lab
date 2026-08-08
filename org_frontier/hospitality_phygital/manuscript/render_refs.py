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


def clean(s):
    for a, b in [("\\&", "&"), ("--", "–"), ("``", "‘"), ("''", "’"),
                 ('{\\"o}', "ö"), ('{\\"u}', "ü"), ("{\\'e}", "é"),
                 ("{\\'a}", "á"), ("{\\'i}", "í"), ("{\\`e}", "è"),
                 ("{\\dh}", "ð"), ("{\\TH}", "Þ")]:
        s = s.replace(a, b)
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


def render(kind, f):
    who = authors(f["author"]) if "author" in f else "Anon."
    year = f.get("year", "n.d.")
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
        eds = authors(f["editor"]) if "editor" in f else ""
        pages = clean(f.get("pages", ""))
        return (head + f"'{title}', in {eds} (ed.), *{clean(f.get('booktitle',''))}*, "
                f"{clean(f.get('address',''))}: {clean(f.get('publisher',''))}, pp. {pages}.")

    if kind == "inproceedings":
        pages = clean(f.get("pages", ""))
        return head + f"'{title}', *{clean(f.get('booktitle',''))}*, pp. {pages}."

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

    refused = [k for k in keys if "DO-NOT-CITE" in entries[k][1].get("note", "")]
    if refused:
        print("ABORT: refused DO-NOT-CITE entries: " + ", ".join(refused), file=sys.stderr)
        return 1

    unverified = [k for k in keys
                  if "verified" not in entries[k][1].get("note", "")
                  and "crossref-verified" not in entries[k][1].get("note", "")]
    if unverified:
        print("WARNING: cited but not marked verified: " + ", ".join(unverified), file=sys.stderr)

    rendered = sorted((render(*entries[k]) for k in keys), key=lambda s: s.lower())
    print("## References\n")
    for r in rendered:
        print(r + "\n")
    print(f"<!-- {len(rendered)} entries -->", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
