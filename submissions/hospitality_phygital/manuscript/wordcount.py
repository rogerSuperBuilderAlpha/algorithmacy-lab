#!/usr/bin/env python3
"""Word count for the Hospitality & Society manuscript, on a declared denominator.

The journal's limit is 6,000-9,000 words *including* notes, references, contributor biography,
keywords and abstract (JOURNAL_SPEC.md). Body and total are therefore both reported, and the
budget gate runs on the body while the ceiling gate runs on the projected total.

Measures
  BODY   the line '## 1. Introduction' through the line before the next '## ' heading that is not
         a numbered body section -- in practice '## Acknowledgment'. Headings and table rows count.
  ITALIC drafting notes in *...* on their own paragraph are excluded; they are scaffolding.

Usage: python3 wordcount.py manuscript.md [--refs N]
"""
import argparse
import re
import sys
from pathlib import Path

BODY_START = re.compile(r"^##\s+1\.\s")
BODY_END = re.compile(r"^##\s+(?!\d+\.)")
NOTE_LINE = re.compile(r"^\*[^*].*\*$")


def strip_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # links: keep label, drop target
    text = re.sub(r"`[^`]*`", " ", text)                    # inline code
    text = re.sub(r"[*_#>|]", " ", text)                    # emphasis, headings, quotes, table pipes
    text = re.sub(r"^-{2,}$", " ", text, flags=re.M)        # table rules
    return text


def count(tokens: str) -> int:
    return len([t for t in re.split(r"\s+", tokens) if re.search(r"\w", t)])


def body_of(lines):
    out, inside, in_note = [], False, False
    for line in lines:
        if BODY_START.match(line):
            inside = True
        elif inside and BODY_END.match(line):
            break
        if not inside:
            continue
        stripped = line.strip()
        if stripped.startswith("*") and not stripped.startswith("**"):
            in_note = NOTE_LINE.match(stripped) is None
            continue
        if in_note:
            if stripped.endswith("*"):
                in_note = False
            continue
        out.append(line)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paper")
    ap.add_argument("--refs", type=int, default=None,
                    help="cited references; Intellect Harvard renders at ~26 words each. Measure the\n                         rendered list directly before any lock decision.")
    args = ap.parse_args()

    if args.refs is None:
        # A hard-coded 77 understated the projected total by ~1,200 words while the
        # cited list stood at 124. Read the list the paper actually renders from.
        here = Path(__file__).resolve().parent
        keys = here / ("cited_keys_draft.txt" if Path(args.paper).name == "DRAFT.md"
                       else "cited_keys.txt")
        args.refs = sum(1 for ln in keys.read_text(encoding="utf-8").splitlines() if ln.strip())

    lines = open(args.paper, encoding="utf-8").read().splitlines()
    body = count(strip_markdown("\n".join(body_of(lines))))
    if body == 0:
        print("ABORT: no body found. Expected a '## 1. ' heading.")
        return 1

    refs = args.refs * 26
    other = 180 + 12 + 200 + 50 + 50   # abstract, keywords, two biographies, AI statement, notes
    total = body + refs + other

    ceiling_budget = 9000 - refs - other   # what the all-inclusive ceiling leaves the body
    print(f"BODY            {body:>6,}   budget 6,850; the 9,000 ceiling leaves it {ceiling_budget:,}")
    print(f"references (x{args.refs})  {refs:>6,}   measured at ~26 words each")
    print(f"other required  {other:>6,}   abstract, keywords, biographies, AI statement, notes")
    print(f"TOTAL           {total:>6,}   limit 6,000-9,000 inclusive")

    fail = False
    if not 6000 <= total <= 9000:
        print(f"G-LEN FAIL: projected total {total:,} outside 6,000-9,000")
        fail = True
    if body > 6850:
        print(f"G-BUDGET over: body {body:,} exceeds the 6,850 budget by {body - 6850:,}")
    print("G-LEN: FAIL" if fail else "G-LEN: PASS")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
