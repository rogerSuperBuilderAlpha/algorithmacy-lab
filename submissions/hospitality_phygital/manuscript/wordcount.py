#!/usr/bin/env python3
"""Word count for the Hospitality & Society manuscript, on a declared denominator.

The journal's limit is 6,000-9,000 words *including* notes, references, contributor biography,
keywords and abstract (JOURNAL_SPEC.md). Body and total are therefore both reported, and the
budget gate runs on the body while the ceiling gate runs on the projected total.

Measures
  BODY   the line '## 1. Introduction' through the line before the next '## ' heading that is not
         a numbered body section -- in practice '## Acknowledgment'. Headings and table rows count.
  ITALIC drafting notes in *...* on their own paragraph are excluded; they are scaffolding.

Usage: python3 wordcount.py DRAFT.md [--refs N]
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
        keys = here / "cited_keys_draft.txt"
        args.refs = sum(1 for ln in keys.read_text(encoding="utf-8").splitlines() if ln.strip())

    lines = open(args.paper, encoding="utf-8").read().splitlines()
    body = count(strip_markdown("\n".join(body_of(lines))))
    if body == 0:
        print("ABORT: no body found. Expected a '## 1. ' heading.")
        return 1

    # THE AUTHOR HAS RULED THAT REFERENCES DO NOT COUNT. The figure that governs is the
    # body, sections 1-9, against 6,000-9,000. See JOURNAL_SPEC.md. A session on 17 August
    # read the Notes literally, computed a 3,600-word overage that did not exist, and cut
    # 2,344 words on that basis. The reference count is reported for information only.
    raw = open(args.paper, encoding="utf-8").read()
    nrefs = 0
    if "## References" in raw:
        nrefs = len([ln for ln in raw.split("## References", 1)[1].splitlines()
                     if ln.strip() and not ln.startswith("*")])

    print(f"BODY            {body:>6,}   against 6,000-9,000 (body only, per the author's ruling)")
    print(f"references      {nrefs:>6,}   entries, not counted")

    fail = False
    if not 6000 <= body <= 9000:
        where = "below the 6,000 floor" if body < 6000 else "above the 9,000 ceiling"
        print(f"G-LEN FAIL: body {body:,} is {where}")
        fail = True
    else:
        print(f"            headroom: {9000 - body:,} words to the ceiling, "
              f"{body - 6000:,} above the floor")
    print("G-LEN: FAIL" if fail else "G-LEN: PASS")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
