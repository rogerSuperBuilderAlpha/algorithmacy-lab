#!/usr/bin/env python3
"""Build the atlas index of the six research programs' reference cards."""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from org_frontier.research.build_cards_index import PROGRAMS, frontmatter  # noqa: E402

OUTPUT = ROOT / "research-atlas" / "cards.json"


def summary(path):
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## Summary\s*\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
    if not match:
        return ""
    paragraph = match.group(1).strip().split("\n\n", 1)[0]
    return re.sub(r"\s+", " ", paragraph)[:500]


def build():
    rows = []
    for program in PROGRAMS:
        for path in sorted((ROOT / "org_frontier" / "research" / program / "literature" / "cards").glob("*.md")):
            meta = frontmatter(path)
            rows.append({
                "kind": "reference",
                "id": meta.get("citekey") or path.stem,
                "title": meta.get("title") or path.stem,
                "authors": meta.get("authors", ""),
                "year": meta.get("year", ""),
                "program": program,
                "source_basis": meta.get("source_basis", ""),
                "verified": meta.get("verified", ""),
                "doi": meta.get("doi", ""),
                "summary": summary(path),
                "path": path.relative_to(ROOT).as_posix(),
            })
    return {"rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if cards.json is stale")
    args = parser.parse_args()
    content = json.dumps(build(), ensure_ascii=False, indent=1) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            print("research-atlas/cards.json is stale — run research-atlas/build_cards.py")
            return 1
        print("research-atlas/cards.json is up to date.")
    else:
        OUTPUT.write_text(content, encoding="utf-8")
        print(f"Wrote {OUTPUT.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
