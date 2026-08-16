#!/usr/bin/env python3
"""Regenerate the Grammarly paste file and the Word manuscript from chapter.md.

chapter.md is the source of truth and is hard-wrapped for readable git diffs. Neither
artifact should ever be edited by hand; run this after any substantive edit.

    python3 build_artifacts.py            # both artifacts
    python3 build_artifacts.py --check    # verify they are in sync, write nothing

The Grammarly file unwraps every paragraph to one long line, because Grammarly treats a
hard line break as a sentence boundary and reports false fragments otherwise. Markdown
tables get linearized for the same reason: Grammarly cannot parse a pipe table and
scores its cells as sentence fragments.

The Word file goes through pandoc. Reflow it into the IGI template at submission.
"""

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "chapter.md"
GRAMMARLY = HERE / "chapter_grammarly.md"
DOCX = HERE / "Full Paper - Alg & Sov.docx"

BANNER = """<!-- Paste-ready for Grammarly: soft-wrapped paragraphs, one blank line between them.
     Full chapter including References, Cases, Additional Reading, and Key Terms.
     Source of truth remains chapter.md (hard-wrapped for git diffs).
     Regenerate with build_artifacts.py after substantive edits.
     chapter.md sha256: {digest} -->"""


def source_digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def linearize_table(block):
    """Turn a pipe table into labelled bullets Grammarly can read as prose."""
    rows = [r.strip() for r in block.split("\n") if r.strip().startswith("|")]
    cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
    header, body = cells[0], [r for r in cells[1:] if not set("".join(r)) <= set("-: ")]
    lines = ["Instrument crosswalk:"]
    for row in body:
        pairs = [f"{h}: {v}" for h, v in zip(header, row) if v]
        lines.append("- " + "; ".join(pairs))
    return "\n".join(lines)


def build_grammarly(source_text):
    out = [BANNER.format(digest=source_digest(source_text))]
    for block in source_text.split("\n\n"):
        if not block.strip():
            continue
        lines = block.split("\n")
        if any(l.lstrip().startswith("|") for l in lines):
            out.append(linearize_table(block))
        elif lines[0].startswith("#"):
            out.append(block)
        else:
            out.append(" ".join(l.strip() for l in lines))
    return "\n\n".join(out) + "\n"


def prose_words(text):
    """Word sequence of the prose, skipping HTML comments and tables in either form.

    A table is excluded as a pipe table in chapter.md and as the linearized crosswalk in
    the Grammarly file, so the two sides stay comparable; the table's own content is
    checked separately by linearize_table's zip over the header.
    """
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    kept = [
        b for b in text.split("\n\n")
        if not any(l.lstrip().startswith("|") for l in b.split("\n"))
        and not b.lstrip().startswith("Instrument crosswalk:")
    ]
    return " ".join(kept).split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify sync, write nothing")
    args = ap.parse_args()

    source_text = SOURCE.read_text(encoding="utf-8")
    grammarly = build_grammarly(source_text)

    # The unwrap must be whitespace-only: every prose word survives in order.
    if prose_words(source_text) != prose_words(grammarly):
        sys.exit("ABORT: the Grammarly build changed the prose. Nothing written.")

    if args.check:
        # Staleness is decided by the source hash stamped into the Grammarly banner at
        # build time, not by mtimes: git checkout and git pull rewrite mtimes, so an
        # mtime test cries wolf after every branch switch and gets ignored. pandoc
        # output is not byte-reproducible, so the docx is judged by the same stamp.
        if not GRAMMARLY.exists() or not DOCX.exists():
            sys.exit("missing artifact, regenerate: run build_artifacts.py")
        stamped = re.search(r"chapter\.md sha256: ([0-9a-f]{64})", GRAMMARLY.read_text(encoding="utf-8"))
        if not stamped:
            sys.exit("no build stamp in the Grammarly file, regenerate: run build_artifacts.py")
        if stamped.group(1) != source_digest(source_text):
            sys.exit("stale: chapter.md has changed since the last build. Run build_artifacts.py")
        if GRAMMARLY.read_text(encoding="utf-8") != grammarly:
            sys.exit("stale: the Grammarly file does not match a fresh build. Run build_artifacts.py")
        print("both artifacts are in sync with chapter.md")
        return

    GRAMMARLY.write_text(grammarly, encoding="utf-8")
    print(f"wrote {GRAMMARLY.name} ({len(grammarly.split())} words)")

    # No --toc: the manuscript reflows into the IGI template, which supplies its own
    # front matter, and the prior artifact carried none.
    subprocess.run(
        ["pandoc", str(SOURCE), "--from", "markdown", "--to", "docx",
         "--standalone", "-o", str(DOCX)],
        check=True,
    )
    print(f"wrote {DOCX.name} ({DOCX.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
