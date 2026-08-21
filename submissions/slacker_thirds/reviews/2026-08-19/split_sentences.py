#!/usr/bin/env python3
"""Split the chapter body into numbered sentences, one index per sentence.

Same output shape as the v16 file the previous audit worked from
(old/archive/reviews/2026-08-18-v17/v16_sentences.txt): a SECTION line per heading,
a "-- para N" line per paragraph, and "[n] " before each sentence, numbered
continuously across the whole body. Footnote markers are stripped so a reviewer
quoting a sentence quotes what the reader sees.

Usage: python3 split_sentences.py ../../chapter.md > v17_sentences.txt
"""
import re
import sys

ABBREV = r"(?<!\bno)(?<!\bed)(?<!\bvol)(?<!\bpp)(?<!\bp)(?<!\bch)(?<!\bSt)(?<!\bMr)(?<!\bMs)(?<!\btrans)(?<!\be\.g)(?<!\bi\.e)(?<!\betc)(?<!\bcf)(?<!\bart)(?<!\bsec)(?<!\bnos)"
SPLIT = re.compile(ABBREV + r'(?<=[.?!])(["”’\']?)\s+(?=[A-Z"“*‘\'])')


def sentences(text):
    marked = SPLIT.sub(lambda m: m.group(1) + "\x00", text)
    return [s.strip() for s in marked.split("\x00") if s.strip()]


def main():
    raw = open(sys.argv[1], encoding="utf-8").read()
    body = raw.split("\n## Notes")[0]
    body = re.sub(r"\[\^[^\]]+\]", "", body)          # footnote markers
    n = 0
    out = []
    para_in_section = 0
    for block in body.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("#"):
            out.append("")
            out.append("=== SECTION: " + block.lstrip("# ").strip())
            para_in_section = 0
            continue
        if block.startswith(">"):                      # block quote: one unit
            para_in_section += 1
            n += 1
            out.append("")
            out.append(f"-- para {para_in_section} (block quote)")
            out.append(f"[{n}] " + re.sub(r"\s+", " ", block.lstrip("> ")))
            continue
        para_in_section += 1
        out.append("")
        out.append(f"-- para {para_in_section}")
        for s in sentences(re.sub(r"\s+", " ", block)):
            n += 1
            out.append(f"[{n}] {s}")
    print("\n".join(out).strip())
    print(f"\n\n[total: {n} sentences]", file=sys.stderr)


main()
