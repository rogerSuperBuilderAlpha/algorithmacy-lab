#!/usr/bin/env python3
"""Regenerate the derived export files from chapter.md.

chapter.md is the source of truth (hard-wrapped for git diffs). Two files derive from it
and must never be hand-edited:

  chapter_grammarly.md      soft-wrapped paste target for Grammarly; the section 7 table is
                            flattened to a list, because Grammarly does not read pipe tables.
  Full Paper - Alg & Sov.docx   pandoc render of chapter.md, to be reflowed into the IGI template.

Run from the chapter directory:  python3 regen_exports.py
Add --check to verify the exports are current without rewriting them (exit 1 if stale).
"""

import hashlib
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "chapter.md"
GRAMMARLY = HERE / "chapter_grammarly.md"
DOCX = HERE / "Full Paper - Alg & Sov.docx"
# Word styling for the .docx: Times New Roman 12pt, double-spaced, APA 7 heading placement,
# page numbers. Rebuild it with build_reference_docx.py; its hash is part of the stamp below,
# so restyling marks the .docx stale the same way editing chapter.md does.
REFERENCE = HERE / "reference.docx"
# Records the chapter.md hash the .docx was built from. A .docx is a zip whose bytes differ
# on every run, so it cannot be compared against a fresh render; and mtimes are reordered by
# any git checkout, so they cannot be trusted either. This sidecar is committed with them.
STAMP = HERE / ".exports.sha256"

HEADER = """<!-- Paste-ready for Grammarly: soft-wrapped paragraphs, one blank line between them.
     Full chapter including References, Cases, Additional Reading, and Key Terms.
     Source of truth remains chapter.md (hard-wrapped for git diffs).
     Regenerate with regen_exports.py after substantive edits. -->
"""


def flatten_table(rows):
    """Turn a pipe table into 'Instrument: X; <col2 header>: Y; <col3 header>: Z.' lines."""
    header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    out = ["Instrument crosswalk:"]
    for row in rows[2:]:  # skip the |---|---| separator
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        parts = [f"{h}: {c}" for h, c in zip(header, cells)]
        out.append("- " + "; ".join(parts) + ".")
    return out


def build_grammarly(text):
    blocks, buf, table = [], [], []
    for line in text.split("\n"):
        if line.startswith("|"):
            if buf:
                blocks.append(" ".join(buf))
                buf = []
            table.append(line)
            continue
        if table:
            blocks.extend(flatten_table(table))
            table = []
        if not line.strip():
            if buf:
                blocks.append(" ".join(buf))
                buf = []
            continue
        if line.startswith("#"):
            if buf:
                blocks.append(" ".join(buf))
                buf = []
            blocks.append(line)
            continue
        buf.append(line.strip())
    if table:
        blocks.extend(flatten_table(table))
    if buf:
        blocks.append(" ".join(buf))

    out = [HEADER]
    prev_list = False
    for b in blocks:
        is_list = b.startswith("- ")
        if prev_list and is_list:
            out[-1] += "\n" + b
        else:
            out.append(b)
        prev_list = is_list
    return "\n\n".join(out).rstrip() + "\n"


def lint(text):
    """Structural checks that have bitten this manuscript before."""
    problems = []
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].startswith("#") and lines[i - 1].strip() != "":
            problems.append(
                f"line {i + 1}: heading {lines[i]!r} has no blank line before it; "
                "pandoc will swallow it into the previous paragraph"
            )
    for i, line in enumerate(lines):
        if line.startswith("|") and i and lines[i - 1].strip() and not lines[i - 1].startswith("|"):
            problems.append(f"line {i + 1}: table has no blank line before it")
    for name in ("## Abstract", "## References", "## Additional Reading", "## Key Terms and Definitions"):
        if name not in text:
            problems.append(f"missing required IGI section: {name}")
    return problems


def main():
    check_only = "--check" in sys.argv
    text = SOURCE.read_text()

    problems = lint(text)
    if problems:
        print("chapter.md structural problems:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1

    grammarly = build_grammarly(text)

    h = hashlib.sha256(text.encode())
    if REFERENCE.exists():
        h.update(hashlib.sha256(REFERENCE.read_bytes()).digest())
    digest = h.hexdigest()

    if check_only:
        stale = []
        if not GRAMMARLY.exists() or GRAMMARLY.read_text() != grammarly:
            stale.append(GRAMMARLY.name)
        recorded = STAMP.read_text().split()[0] if STAMP.exists() else None
        if not DOCX.exists() or recorded != digest:
            stale.append(DOCX.name)
        if stale:
            print("STALE (rerun regen_exports.py): " + ", ".join(stale), file=sys.stderr)
            return 1
        print("exports are current")
        return 0

    GRAMMARLY.write_text(grammarly)
    cmd = ["pandoc", "-f", "markdown", "-t", "docx", str(SOURCE), "-o", str(DOCX)]
    if REFERENCE.exists():
        cmd.insert(-2, f"--reference-doc={REFERENCE}")
    else:
        print(f"warning: {REFERENCE.name} missing; run build_reference_docx.py", file=sys.stderr)
    subprocess.run(cmd, check=True)
    STAMP.write_text(f"{digest}  {SOURCE.name}\n")
    print(f"wrote {GRAMMARLY.name} ({len(grammarly.split())} words)")
    print(f"wrote {DOCX.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
