#!/usr/bin/env python3
"""Prove that a draft shares no sentences with its predecessors.

The v4 rebuild carries a rule -- discard every v3 sentence -- and a rule nobody can
check is a wish. This script checks it. It shingles the candidate body into overlapping
8-word sequences and looks for each one in the prior drafts.

Quotations are exempt. They are the sources' words, not the previous draft's, and two
drafts quoting the same passage of Simmel is not carryover. So are the notes and
bibliography blocks, which carry forward by policy: they are the most expensive verified
artifact in the repo and re-typing them would only invite new errors.

Usage:
    python3 v4/tools/check_carryover.py chapter/chapter_v4.md
    python3 v4/tools/check_carryover.py chapter/chapter_v4.md --n 6 --show 40
"""
import argparse
import re
import sys
from pathlib import Path

PRIOR_DRAFTS = [
    "chapter/chapter_v3.md",
    "chapter/chapter_v3_long.md",
    "chapter/archive/chapter_v2.md",
    "chapter/archive/chapter_v1.md",
]

# straight and curly pairs, plus block quotes
QUOTED = re.compile(r"[“\"][^”\"]{0,600}[”\"]", re.S)
BLOCKQUOTE = re.compile(r"(?m)^>.*$")
NOTE_MARKER = re.compile(r"\[\^[^\]]+\]")
CODE = re.compile(r"`[^`]*`")
HEADING = re.compile(r"(?m)^#+.*$")
ITALIC_TITLE = re.compile(r"\*[^*]{1,120}\*")


def body_of(text):
    """Everything before the Notes block. Notes and bibliography carry forward by policy."""
    return re.split(r"(?m)^##\s*Notes\s*$", text)[0]


def strip_exempt(text):
    """Blank out spans that are allowed to match, preserving offsets."""
    for pattern in (BLOCKQUOTE, QUOTED, CODE, HEADING, NOTE_MARKER, ITALIC_TITLE):
        text = pattern.sub(lambda m: " " * len(m.group()), text)
    return text


def words_with_offsets(text):
    return [(m.group().lower(), m.start()) for m in re.finditer(r"[A-Za-z][A-Za-z'’-]*", text)]


def shingles(text, n):
    """Yield (shingle, char_offset). Offsets index the ORIGINAL text."""
    toks = words_with_offsets(text)
    for i in range(len(toks) - n + 1):
        yield " ".join(t[0] for t in toks[i:i + n]), toks[i][1]


def shingle_set(text, n):
    return {s for s, _ in shingles(text, n)}


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("--n", type=int, default=8, help="shingle length in words (default 8)")
    ap.add_argument("--show", type=int, default=25, help="max matches to print")
    ap.add_argument("--root", default=None, help="project root (default: two levels up)")
    args = ap.parse_args()

    root = Path(args.root) if args.root else Path(__file__).resolve().parents[2]
    cand_path = Path(args.candidate)
    if not cand_path.is_absolute():
        cand_path = root / cand_path
    if not cand_path.exists():
        sys.exit("candidate not found: %s" % cand_path)

    raw = cand_path.read_text(encoding="utf-8")
    cand_body = body_of(raw)
    cand_clean = strip_exempt(cand_body)

    prior = set()
    found_priors = []
    for rel in PRIOR_DRAFTS:
        p = root / rel
        if not p.exists():
            continue
        found_priors.append(rel)
        prior |= shingle_set(strip_exempt(body_of(p.read_text(encoding="utf-8"))), args.n)

    if not found_priors:
        sys.exit("no prior drafts found under %s -- nothing to check against" % root)

    hits = []
    seen = set()
    for sh, off in shingles(cand_clean, args.n):
        if sh in prior and sh not in seen:
            seen.add(sh)
            hits.append((line_of(cand_body, off), sh))

    print("carryover check: %s" % cand_path.name)
    print("  %d-word shingles, checked against %d prior drafts:" % (args.n, len(found_priors)))
    for rel in found_priors:
        print("    %s" % rel)
    print("  quotations, block quotes, headings, italic titles, note markers, and the")
    print("  Notes/Bibliography blocks are exempt")
    print()

    if not hits:
        print("PASS -- no shared %d-word sequence outside the exempt spans" % args.n)
        return 0

    print("FAIL -- %d shared sequences" % len(hits))
    for line, sh in hits[:args.show]:
        print("  line %-5d %s" % (line, sh))
    if len(hits) > args.show:
        print("  ... and %d more" % (len(hits) - args.show))
    return 1


if __name__ == "__main__":
    sys.exit(main())
