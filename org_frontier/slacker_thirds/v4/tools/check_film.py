#!/usr/bin/env python3
"""Measure how long the chapter goes without the film in it.

Every editor lens in every round raised the same complaint. July 3: sections 2 and 5
are "the strain the prompt predicted, and it is real." August 2: "§2 and §5 together
are 1,630 words -- thirty per cent of the chapter -- in which Slacker appears in about
forty," and "compression took words out of the film and left the sociology whole."
The complaint was raised four times and fixed by revision each time, which is why it
came back four times.

The v4 answer is a budget rather than a resolution. Scenes are assigned in the outline
and this script measures whether the draft kept them:

  1. how many of the film's dialogue segments the chapter engages
  2. whether each section reaches the film inside its first 120 words
  3. the longest run of words anywhere with no film referent in it

A film referent is a scene name, a character description the project uses, a line of
quoted dialogue, a proper noun from the production, or the film's title. The lexicon
lives in v4/factbase/film_lexicon.txt, one term per line, '#' for comments -- so the
list is editable evidence rather than something buried in code.

Usage:
    python3 v4/tools/check_film.py chapter/chapter_v4.md
    python3 v4/tools/check_film.py chapter/chapter_v4.md --max-gap 250 --min-scenes 12
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_LEXICON = "v4/factbase/film_lexicon.txt"


def body_of(text):
    return re.split(r"(?m)^##\s*Notes\s*$", text)[0]


def load_lexicon(path):
    terms = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if line:
            terms.append(line)
    if not terms:
        sys.exit("lexicon is empty: %s" % path)
    return terms


def sections(body):
    """[(heading, text)] split on '## n. Title' headings."""
    parts = re.split(r"(?m)^(##\s+.*)$", body)
    out, i = [], 1
    if parts[0].strip():
        out.append(("(front matter)", parts[0]))
    while i + 1 < len(parts) + 1 and i < len(parts):
        head = parts[i].strip("# ").strip()
        text = parts[i + 1] if i + 1 < len(parts) else ""
        out.append((head, text))
        i += 2
    return out


def words_with_offsets(text):
    return [(m.group(), m.start()) for m in re.finditer(r"[A-Za-z][A-Za-z'’-]*", text)]


def film_word_indices(text, terms, quoted_counts=True):
    """Indices (into the word list) of words that sit inside a film referent."""
    marks = set()
    words = words_with_offsets(text)
    starts = [w[1] for w in words]

    spans = []
    for term in terms:
        pat = r"\b%s\b" % re.escape(term).replace(r"\ ", r"\s+")
        for m in re.finditer(pat, text, re.I):
            spans.append((m.start(), m.end()))
    if quoted_counts:
        for m in re.finditer(r"[“\"][^”\"]{8,400}[”\"]", text, re.S):
            spans.append((m.start(), m.end()))

    for lo, hi in spans:
        for idx, off in enumerate(starts):
            if lo <= off < hi:
                marks.add(idx)
    return marks, words


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--lexicon", default=None)
    ap.add_argument("--max-gap", type=int, default=250,
                    help="longest permitted run of words with no film referent")
    ap.add_argument("--open-within", type=int, default=120,
                    help="each section must reach the film inside this many words")
    ap.add_argument("--min-scenes", type=int, default=12,
                    help="minimum distinct dialogue segments engaged")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[2]
    draft = Path(args.draft)
    if not draft.is_absolute():
        draft = root / draft
    lex_path = Path(args.lexicon) if args.lexicon else root / DEFAULT_LEXICON

    terms = load_lexicon(lex_path)
    scene_terms = [t for t in terms if not t.startswith("~")]
    terms = [t.lstrip("~") for t in terms]

    body = body_of(draft.read_text(encoding="utf-8"))
    problems = []

    print("film-forwardness: %s" % draft.name)
    print("  lexicon: %s (%d terms)" % (lex_path.name, len(terms)))
    print()

    # --- per section
    print("PER SECTION")
    print("  %-44s %6s %8s %9s" % ("section", "words", "opens@", "max gap"))
    for head, text in sections(body):
        marks, words = film_word_indices(text, terms)
        n = len(words)
        if n < 30:
            continue
        first = min(marks) if marks else None
        gaps, prev = [], -1
        for idx in sorted(marks):
            gaps.append(idx - prev - 1)
            prev = idx
        gaps.append(n - prev - 1)
        maxgap = max(gaps) if gaps else n

        opens = "%d" % first if first is not None else "never"
        flags = ""
        if first is None or first > args.open_within:
            flags += " OPEN"
            problems.append("%s: reaches the film at word %s (limit %d)"
                            % (head[:40], opens, args.open_within))
        if maxgap > args.max_gap:
            flags += " GAP"
            problems.append("%s: %d words with no film referent (limit %d)"
                            % (head[:40], maxgap, args.max_gap))
        print("  %-44s %6d %8s %9d%s" % (head[:44], n, opens, maxgap, flags))
    print()

    # --- scene coverage
    engaged = sorted({t for t in scene_terms
                      if re.search(r"\b%s\b" % re.escape(t).replace(r"\ ", r"\s+"), body, re.I)})
    print("SCENE COVERAGE")
    print("  %d of %d lexicon scene terms present   minimum %d   %s"
          % (len(engaged), len(scene_terms), args.min_scenes,
             "ok" if len(engaged) >= args.min_scenes else "UNDER"))
    if len(engaged) < args.min_scenes:
        problems.append("only %d scene terms present, minimum %d" % (len(engaged), args.min_scenes))
    missing = [t for t in scene_terms if t not in engaged]
    if missing:
        print("  absent: %s" % ", ".join(missing[:18]))
        if len(missing) > 18:
            print("           ... and %d more" % (len(missing) - 18))
    print()

    # --- whole body
    marks, words = film_word_indices(body, terms)
    n = len(words)
    gaps, prev = [], -1
    worst = (0, 0)
    for idx in sorted(marks):
        if idx - prev - 1 > worst[0]:
            worst = (idx - prev - 1, prev + 1)
        prev = idx
    if n - prev - 1 > worst[0]:
        worst = (n - prev - 1, prev + 1)
    print("WHOLE BODY")
    print("  %d words, %d inside a film referent (%.0f%%)" % (n, len(marks), 100 * len(marks) / n))
    print("  longest filmless run: %d words, starting at word %d" % worst)
    if worst[0] and worst[1] < len(words):
        start = words[worst[1]][1]
        print("    \"%s...\"" % " ".join(w[0] for w in words[worst[1]:worst[1] + 12]))
    print()

    if problems:
        print("RESULT: FAIL")
        for p in problems:
            print("  %s" % p)
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
