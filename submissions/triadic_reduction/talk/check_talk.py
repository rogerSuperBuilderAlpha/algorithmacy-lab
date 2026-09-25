#!/usr/bin/env python3
"""Check the talk against its own rules before anyone rehearses it.

1. deck.pptx is black on white: text boxes, plus the author's pictures and
   one plain table, and nothing else (no autoshapes, lines or groups); every
   run explicitly black, table cells unfilled, every background explicitly white, one sans
   and one mono face, 16:9, no transitions or animation timing.
2. Each slide's speaker notes equal its section of script.md.
3. The spoken script fits the slot at 130 words a minute, with a buffer and time held back for the
   live demo.
4. Every number in deck.md and script.md is declared in NUMBERS.md; a number
   declared as a lab result must name a check whose expect string in
   ci/reproduce.json contains the declared substring.
5. Every quotation of four or more words, other than the speaker's own
   asides listed in ASIDES.txt, matches, after normalising
   whitespace and quote marks, a quotation in the Loci of a library card
   whose `verified` field is `verified` or `corrected`.
6. No phrase listed in BANNED.txt appears in deck.md or script.md.

Run with a Python that has python-pptx:

    /usr/bin/python3 talk/check_talk.py
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches

from build_deck import notes_text

HERE = Path(__file__).resolve().parent
ARM = HERE.parent
REPO = ARM.parent.parent
CARDS = ARM / "library" / "cards"
SLOT_MINUTES = 30  # requested from the organizers 2026-09-25; the confirmed slot is still 20 — set back to 20 if they decline
DEMO_MINUTES = 3
BUFFER_MINUTES = 1.5
WPM = 130
FONTS = {"Arial", "Courier New", "Cambria Math"}
FONT_FILES = {"Arial": "/System/Library/Fonts/Supplemental/Arial.ttf",
              "Courier New": "/System/Library/Fonts/Supplemental/Courier New.ttf",
              # Cambria Math is not on the build machine; STIX Two Math covers the
              # same symbols and stands in for the glyph check.
              "Cambria Math": "/System/Library/Fonts/Supplemental/STIXTwoMath.otf"}

SLIDE_RE = re.compile(r"^## Slide (\d+)\b.*$", re.M)


def split_slides(text: str) -> dict[int, str]:
    parts = {}
    marks = list(SLIDE_RE.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        parts[int(m.group(1))] = text[m.end():end].strip("\n")
    return parts


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), (" ", " ")):
        text = text.replace(a, b)
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def spoken(text: str) -> str:
    """Script text a speaker reads aloud: drop comments and stage directions."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\[[^\]]*\]", " ", text)
    return text


def missing_glyphs(text: str, face: str) -> str:
    """Characters the face cannot draw (a venue without font fallback shows boxes)."""
    try:
        from PIL import ImageFont
        font = ImageFont.truetype(FONT_FILES[face], 24)
    except (ImportError, KeyError, OSError):
        return ""
    notdef = bytes(font.getmask("\U0010fffd"))  # a private-use code point no face draws

    def absent(c):
        mask = font.getmask(c)
        return mask.getbbox() is None or bytes(mask) == notdef

    return "".join(sorted({c for c in text if not c.isspace() and absent(c)}))


def check_pptx(problems: list[str]) -> Presentation:
    prs = Presentation(HERE / "deck.pptx")
    if abs(prs.slide_width - Inches(13.333)) > Inches(0.01) or \
            abs(prs.slide_height - Inches(7.5)) > Inches(0.01):
        problems.append("deck is not 16:9 at 13.333 x 7.5 in")
    for i, slide in enumerate(prs.slides, 1):
        fill = slide.background.fill
        try:
            if str(fill.fore_color.rgb) != "FFFFFF":
                problems.append(f"slide {i}: background is not white")
        except (AttributeError, TypeError):
            problems.append(f"slide {i}: background is not an explicit white fill")
        xml = slide._element.xml
        if "<p:transition" in xml or "<p:timing" in xml:
            problems.append(f"slide {i}: has a transition or animation timing")
        for shape in slide.shapes:
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                continue
            if shape.has_table:
                frames = []
                for cell in (c for row in shape.table.rows for c in row.cells):
                    if cell.fill.type is not None and cell.fill.type != 5:  # 5 = background
                        problems.append(f"slide {i}: table cell has a fill")
                    frames.append(cell.text_frame)
            elif shape.shape_type == MSO_SHAPE_TYPE.TEXT_BOX:
                frames = [shape.text_frame]
            else:
                problems.append(f"slide {i}: non-text shape {shape.shape_type}")
                continue
            for p in (p for tf in frames for p in tf.paragraphs):
                for r in p.runs:
                    missing = missing_glyphs(r.text, r.font.name)
                    if missing:
                        problems.append(f"slide {i}: {r.font.name} has no glyph for {missing!r}")
                    if r.font.name not in FONTS:
                        problems.append(f"slide {i}: font {r.font.name!r}")
                    try:
                        if str(r.font.color.rgb) != "000000":
                            problems.append(f"slide {i}: run colour {r.font.color.rgb}")
                    except AttributeError:
                        problems.append(f"slide {i}: run without explicit black colour")
    return prs


def check_notes(prs, script: dict[int, str], problems: list[str]) -> None:
    for i, slide in enumerate(prs.slides, 1):
        notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
        if norm(notes) != norm(notes_text(script.get(i, ""))):
            problems.append(f"slide {i}: speaker notes differ from script.md")


def check_timing(script: dict[int, str], problems: list[str], report: list[str]) -> None:
    words = {n: len(spoken(t).split()) for n, t in script.items()}
    total = sum(words.values())
    budget = int((SLOT_MINUTES - BUFFER_MINUTES - DEMO_MINUTES) * WPM)
    report.append(f"script: {total} spoken words = {total / WPM:.1f} min at {WPM} wpm "
                  f"(slot {SLOT_MINUTES} min, demo {DEMO_MINUTES} min, budget {budget} words)")
    report.append("per slide: " + ", ".join(f"{n}:{w}" for n, w in sorted(words.items())))
    if total > budget:
        problems.append(f"script is {total} words; budget is {budget}")


def load_numbers() -> tuple[set[str], list[str]]:
    path = HERE / "NUMBERS.md"
    declared, problems = set(), []
    if not path.exists():
        return declared, ["NUMBERS.md is missing"]
    manifest = json.loads((REPO / "ci" / "reproduce.json").read_text(encoding="utf-8"))
    checks = manifest["checks"] if isinstance(manifest, dict) else manifest
    expects = {c["name"]: "\n".join(c.get("expect", [])) for c in checks}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] in ("number", "---") or set(cells[0]) <= {"-"}:
            continue
        number, kind, check, expect = cells[:4]
        declared.add(number.strip("`"))
        if kind == "lab result":
            check, expect = check.strip("`"), expect.strip("`")
            if expect not in expects.get(check, ""):
                problems.append(f"NUMBERS.md: {number} — check {check} / expect {expect!r} "
                                "not found in ci/reproduce.json")
    return declared, problems


NUM_RE = re.compile(r"(?<![\w.])(?:\d+(?:[.,]\d+)*(?:[–-]\d+(?:\.\d+)*)?)(?![\w])")


def check_numbers(texts: dict[str, str], problems: list[str]) -> None:
    declared, errs = load_numbers()
    problems.extend(errs)
    for name, text in texts.items():
        text = re.sub(r"^## Slide \d+.*$", "", text, flags=re.M)
        text = re.sub(r"https?://\S+", "", text)  # image-credit URLs carry no claims
        for m in NUM_RE.finditer(spoken(text)):
            if m.group(0) not in declared:
                problems.append(f"{name}: number {m.group(0)!r} is not declared in NUMBERS.md")


def card_quotes() -> list[str]:
    quotes = []
    for path in CARDS.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        fm = re.search(r"^verified:\s*(\S+)", text, re.M)
        if not fm or fm.group(1) not in ("verified", "corrected"):
            continue
        loci = re.search(r"## Loci\n(.*?)(\n## |\Z)", text, re.S)
        if loci:
            quotes += [norm(q) for q in re.findall(r"[\"“]([^\"”\n]+)[\"”]", loci.group(1))]
    return quotes


def spoken_asides() -> set[str]:
    """Quoted words that are the speaker's own (imagined speech, file names), not sources."""
    path = HERE / "ASIDES.txt"
    if not path.exists():
        return set()
    return {norm(l).strip(" .,;:") for l in path.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")}


def check_quotes(texts: dict[str, str], problems: list[str]) -> None:
    pool = card_quotes()
    asides = spoken_asides()
    for name, text in texts.items():
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)  # a quotation may wrap across lines
        for q in re.findall(r"[\"“]([^\"”\n]+)[\"”]", text):
            if len(q.split()) < 4:
                continue
            nq = norm(q).strip(" .,;:")
            if nq in asides:
                continue
            if not any(nq in c for c in pool):
                problems.append(f"{name}: quotation not found in a verified card: {q[:70]!r}")


def check_banned(texts: dict[str, str], problems: list[str]) -> None:
    path = HERE / "BANNED.txt"
    if not path.exists():
        return
    for phrase in path.read_text(encoding="utf-8").splitlines():
        phrase = phrase.strip()
        if not phrase or phrase.startswith("#"):
            continue
        for name, text in texts.items():
            if norm(phrase) in norm(text):
                problems.append(f"{name}: banned phrase {phrase!r}")


def main() -> int:
    problems: list[str] = []
    report: list[str] = []
    deck_text = (HERE / "deck.md").read_text(encoding="utf-8")
    script_text = (HERE / "script.md").read_text(encoding="utf-8")
    script = split_slides(script_text)
    prs = check_pptx(problems)
    check_notes(prs, script, problems)
    check_timing(script, problems, report)
    texts = {"deck.md": deck_text, "script.md": script_text}
    check_numbers(texts, problems)
    check_quotes(texts, problems)
    check_banned(texts, problems)
    for line in report:
        print(line)
    for p in problems:
        print("FAIL", p)
    print(f"{len(prs.slides)} slides, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
