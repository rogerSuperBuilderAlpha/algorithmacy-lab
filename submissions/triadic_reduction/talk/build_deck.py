#!/usr/bin/env python3
"""Build the talk deck (deck.pptx) from deck.md, with script.md in the notes.

The deck is black text on a white ground, one typeface, text boxes only: no
colour, pictures, charts, tables, shapes or transitions. Every run is given
an explicit black colour and every slide an explicit white background, so a
venue template cannot tint anything.

deck.md holds one block per slide:

    ## Slide 3 — Peirce's two clauses
    ### A relative term cannot be reduced to absolute terms
    Plain body line.
    > A quotation line, set in italics.
    — attribution line, set small
    ```
    2 + 2 − 2 = 2      (monospace block for typographic diagrams)
    ```

The ``###`` line is the slide's headline; everything after it is body.
script.md uses the same ``## Slide k`` headings; each section becomes that
slide's speaker notes. Run with a Python that has python-pptx:

    /usr/bin/python3 talk/build_deck.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = Path(__file__).resolve().parent
DECK_MD = HERE / "deck.md"
SCRIPT_MD = HERE / "script.md"
OUT = HERE / "deck.pptx"

BLACK = RGBColor(0, 0, 0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SANS = "Arial"
MONO = "Courier New"
WIDTH, HEIGHT = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.9)

SIZES = {"headline": 36, "body": 24, "quote": 24, "attrib": 18, "mono": 22,
         "title": 44, "subtitle": 22}

SLIDE_RE = re.compile(r"^## Slide (\d+)\b.*$", re.M)


def split_slides(text: str) -> dict[int, str]:
    parts = {}
    marks = list(SLIDE_RE.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        parts[int(m.group(1))] = text[m.end():end].strip("\n")
    return parts


def parse_slide(block: str) -> tuple[str, list[tuple[str, str]]]:
    """Return (headline, [(style, text), ...]) for one deck.md block."""
    headline = ""
    items: list[tuple[str, str]] = []
    in_mono = False
    mono: list[str] = []
    for line in block.splitlines():
        if line.strip().startswith("```"):
            if in_mono:
                items.append(("mono", "\n".join(mono)))
                mono = []
            in_mono = not in_mono
            continue
        if in_mono:
            mono.append(line)
            continue
        if not line.strip() or line.startswith("<!--"):
            continue
        if line.startswith("### ") and not headline:
            headline = line[4:].strip()
        elif line.startswith("> "):
            items.append(("quote", line[2:].strip()))
        elif line.startswith("— "):
            items.append(("attrib", line.strip()))
        else:
            items.append(("body", line.strip()))
    return headline, items


def white_background(slide) -> None:
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE


def style_run(run, style: str) -> None:
    font = run.font
    font.name = MONO if style == "mono" else SANS
    font.size = Pt(SIZES[style])
    font.bold = style in ("headline", "title")
    font.italic = style == "quote"
    font.color.rgb = BLACK


def add_box(slide, left, top, width, height, paragraphs, align=PP_ALIGN.LEFT,
            anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Emu(0))
    count = 0
    for style, text in paragraphs:
        for k, piece in enumerate(text.split("\n") if style == "mono" else [text]):
            p = tf.paragraphs[0] if count == 0 else tf.add_paragraph()
            p.alignment = align
            # Space between items; a monospace block's own lines sit tight.
            p.space_before = Pt(0 if count == 0 or (style == "mono" and k > 0) else 14)
            count += 1
            run = p.add_run()
            run.text = piece
            style_run(run, style)
    return box


def build() -> Presentation:
    deck = split_slides(DECK_MD.read_text(encoding="utf-8"))
    script = split_slides(SCRIPT_MD.read_text(encoding="utf-8")) if SCRIPT_MD.exists() else {}
    prs = Presentation()
    prs.slide_width, prs.slide_height = WIDTH, HEIGHT
    blank = prs.slide_layouts[6]
    for n in sorted(deck):
        headline, items = parse_slide(deck[n])
        slide = prs.slides.add_slide(blank)
        white_background(slide)
        inner_w = WIDTH - 2 * MARGIN
        if n == 1:
            add_box(slide, MARGIN, Inches(2.2), inner_w, Inches(1.6),
                    [("title", headline)], anchor=MSO_ANCHOR.BOTTOM)
            add_box(slide, MARGIN, Inches(4.1), inner_w, Inches(2.4),
                    [("subtitle", t) for _, t in items])
        else:
            add_box(slide, MARGIN, Inches(0.7), inner_w, Inches(1.3),
                    [("headline", headline)], anchor=MSO_ANCHOR.BOTTOM)
            add_box(slide, MARGIN, Inches(2.3), inner_w, HEIGHT - Inches(2.3) - MARGIN,
                    items)
        notes = script.get(n, "")
        slide.notes_slide.notes_text_frame.text = notes
    return prs


def main() -> int:
    prs = build()
    prs.save(OUT)
    print(f"wrote {OUT} ({len(prs.slides)} slides)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
