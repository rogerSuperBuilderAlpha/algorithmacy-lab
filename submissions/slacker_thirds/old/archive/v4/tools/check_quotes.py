#!/usr/bin/env python3
"""Check every quoted span in the chapter against the film's transcript.

The chapter quotes dialogue from a subtitle-derived transcript. A quotation that does
not appear in that transcript is either drawn from a scholarly source -- fine, and
expected -- or it is a line nobody can source, which is how a fabricated quotation
enters a draft. This project has already caught three: a half-invented Stark and Pais
sentence, a Moretti phrase appearing in no source, and a Berg sentence Berg never wrote.

So the script reports every quoted span and whether the transcript contains it. It does
not decide which ones matter; a quotation absent from the transcript and attributed to a
book is correct, and only a human reading the note can tell the two cases apart.

Matching normalizes curly quotes, dashes, ellipses and whitespace, and ignores case. A
quotation broken by an ellipsis is checked in fragments, since the film's line may be
interrupted in the chapter but continuous on screen.

Usage:
    python3 v4/tools/check_quotes.py chapter/chapter_v4.md
    python3 v4/tools/check_quotes.py chapter/chapter_v4.md --min-words 3
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRANSCRIPT = ROOT / "research" / "slacker_transcript.md"

QUOTE = re.compile(r"[“\"]([^”\"]{4,400})[”\"]")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", " ").replace("–", " ").replace("--", " ")
    s = s.replace("…", " ... ")
    s = re.sub(r"[^\w' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def fragments(q):
    """Split a quotation on ellipses; each side must be found independently."""
    parts = re.split(r"\.\.\.|…", q)
    return [p for p in (f.strip() for f in parts) if len(p.split()) >= 2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--min-words", type=int, default=3)
    args = ap.parse_args()

    chap = Path(args.chapter)
    if not chap.is_absolute():
        chap = ROOT / chap
    raw = chap.read_text(encoding="utf-8")
    body = re.split(r"(?m)^##\s*Notes\s*$", raw)[0]
    notes = raw[len(body):]
    tx = norm(TRANSCRIPT.read_text(encoding="utf-8"))

    found, missing = [], []
    seen = set()
    for region, label in ((body, "body"), (notes, "notes")):
        for m in QUOTE.finditer(region):
            q = m.group(1).strip()
            if len(q.split()) < args.min_words:
                continue
            key = norm(q)
            if not key or key in seen:
                continue
            seen.add(key)
            line = region.count("\n", 0, m.start()) + 1 + (0 if label == "body" else body.count("\n"))
            frs = fragments(q) or [q]
            hits = [norm(f) in tx for f in frs]
            (found if all(hits) else missing).append((label, line, q, sum(hits), len(frs)))

    print("quotation check: %s" % chap.name)
    print("  transcript: %s" % TRANSCRIPT.name)
    print("  %d distinct quoted spans of %d+ words" % (len(found) + len(missing), args.min_words))
    print()

    print("IN THE TRANSCRIPT  (%d)" % len(found))
    for label, line, q, _, _ in found:
        print("  %-5s L%-4d %s" % (label, line, q[:88]))
    print()

    print("NOT IN THE TRANSCRIPT  (%d)" % len(missing))
    print("  Expected for anything quoted from a book, an article, or a web page.")
    print("  Read the attached note for each: a line of dialogue that lands here is a")
    print("  quotation nobody can source.")
    for label, line, q, h, n in missing:
        part = "" if n == 1 else "   [%d/%d fragments found]" % (h, n)
        print("  %-5s L%-4d %s%s" % (label, line, q[:88], part))
    return 0


if __name__ == "__main__":
    sys.exit(main())
