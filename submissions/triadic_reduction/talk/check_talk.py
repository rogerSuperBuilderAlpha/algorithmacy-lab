#!/usr/bin/env python3
"""Check the talk against its own rules before anyone rehearses it.

1. deck.pptx is black on white and text only: text boxes and nothing else,
   every run explicitly black, every background explicitly white, one sans
   and one mono face, 16:9, no transitions or animation timing.
2. Each slide's speaker notes equal its section of script.md.
3. The spoken script fits the slot at 130 words a minute, with a buffer.
4. Every number in deck.md and script.md is declared in NUMBERS.md; a number
   declared as a lab result must name a check whose expect string in
   ci/reproduce.json contains the declared substring.
5. Every quotation of four or more words matches, after normalising
   whitespace and quote marks, a quotation in the Loci of a library card
   whose `verified` field is `verified` or `corrected`.
6. No phrase listed in BANNED.txt appears in deck.md or script.md.

Run with a Python that has python-pptx:

    /usr/bin/python3 talk/check_talk.py
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches

HERE = Path(__file__).resolve().parent
ARM = HERE.parent
REPO = ARM.parent.parent
CARDS = ARM / "library" / "cards"
SLOT_MINUTES = 20
BUFFER_MINUTES = 1.5
WPM = 130
FONTS = {"Arial", "Courier New"}

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
            if shape.shape_type != MSO_SHAPE_TYPE.TEXT_BOX:
                problems.append(f"slide {i}: non-text shape {shape.shape_type}")
                continue
            for p in shape.text_frame.paragraphs:
                for r in p.runs:
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
        if norm(notes) != norm(script.get(i, "")):
            problems.append(f"slide {i}: speaker notes differ from script.md")


def check_timing(script: dict[int, str], problems: list[str], report: list[str]) -> None:
    words = {n: len(spoken(t).split()) for n, t in script.items()}
    total = sum(words.values())
    budget = int((SLOT_MINUTES - BUFFER_MINUTES) * WPM)
    report.append(f"script: {total} spoken words = {total / WPM:.1f} min at {WPM} wpm "
                  f"(budget {budget} words)")
    report.append("per slide: " + ", ".join(f"{n}:{w}" for n, w in sorted(words.items())))
    if total > budget:
        problems.append(f"script is {total} words; budget is {budget}")


def load_numbers() -> tuple[set[str], list[str]]:
    path = HERE / "NUMBERS.md"
    declared, problems = set(), []
    if not path.exists():
        return declared, ["NUMBERS.md is missing"]
    ci = (REPO / "ci" / "reproduce.json").read_text(encoding="utf-8")
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] in ("number", "---") or set(cells[0]) <= {"-"}:
            continue
        number, kind, check, expect = cells[:4]
        declared.add(number.strip("`"))
        if kind == "lab result":
            expect = expect.strip("`")
            if check.strip("`") not in ci or expect not in ci:
                problems.append(f"NUMBERS.md: {number} — check {check} / expect {expect!r} "
                                "not found in ci/reproduce.json")
    return declared, problems


NUM_RE = re.compile(r"(?<![\w.])(?:\d+(?:[.,]\d+)*(?:[–-]\d+(?:\.\d+)*)?)(?![\w])")


def check_numbers(texts: dict[str, str], problems: list[str]) -> None:
    declared, errs = load_numbers()
    problems.extend(errs)
    for name, text in texts.items():
        text = re.sub(r"^## Slide \d+.*$", "", text, flags=re.M)
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


def check_quotes(texts: dict[str, str], problems: list[str]) -> None:
    pool = card_quotes()
    for name, text in texts.items():
        for q in re.findall(r"[\"“]([^\"”\n]+)[\"”]", text):
            if len(q.split()) < 4:
                continue
            nq = norm(q).strip(" .,;:")
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
