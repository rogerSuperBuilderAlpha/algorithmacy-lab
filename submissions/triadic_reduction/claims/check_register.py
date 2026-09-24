#!/usr/bin/env python3
"""Check the claims register against the sources it quotes.

Every row in ``register.json`` carries an ``anchor``: a short span copied from
one source file. The anchor is the row's proof that the claim is really in
the source and not an extractor's invention. This check fails if an anchor is
not found in its file, if an id repeats, or if a field holds a value outside
the allowed set. It also rewrites ``REGISTER.md`` from the JSON with
``--write``; with ``--check`` it fails when ``REGISTER.md`` is stale.

Stdlib only:

    python3 claims/check_register.py --check
    python3 claims/check_register.py --write
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARM = HERE.parent
SOURCES = ARM / "sources"
REGISTER = HERE / "register.json"
TABLE = HERE / "REGISTER.md"

KINDS = {"quotation", "citation", "historical", "logical", "number", "lab_result",
         "definition", "argument_step", "rhetorical"}
SECTIONS = {"S1", "S2", "S3", "S4", "S5", "S6", "X"}
STATUSES = {"pending", "needs_primary", "lab_supported", "lab_contradicted",
            "stipulation", "out_of_scope", "verified", "corrected", "refuted",
            "unverifiable"}
SECTION_TITLES = {
    "S1": "Peirce's logical argument",
    "S2": "Simmel",
    "S3": "Quine and Löwenheim",
    "S4": "The modern logic and philosophy debate",
    "S5": "The lab's IIT move",
    "S6": "Algorithmacy",
    "X": "Out of scope (parked)",
}


def norm(text: str) -> str:
    """Compare text the way a reader would: ignore Markdown and spacing."""
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|~<>$])", r"\1", text)  # Markdown escapes
    text = re.sub(r"[*_`>#|~]", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def load_sources() -> dict[str, str]:
    out = {}
    for path in sorted(SOURCES.glob("*.md")):
        if path.name == "MANIFEST.md":
            continue
        out[path.name.split("_", 1)[0]] = norm(path.read_text(encoding="utf-8"))
    return out


def check(rows: list[dict]) -> list[str]:
    errors = []
    sources = load_sources()
    seen = set()
    for i, row in enumerate(rows):
        rid = row.get("id", f"<row {i}>")
        if rid in seen:
            errors.append(f"{rid}: duplicate id")
        seen.add(rid)
        if row.get("kind") not in KINDS:
            errors.append(f"{rid}: kind {row.get('kind')!r} not allowed")
        if row.get("section") not in SECTIONS:
            errors.append(f"{rid}: section {row.get('section')!r} not allowed")
        if row.get("status") not in STATUSES:
            errors.append(f"{rid}: status {row.get('status')!r} not allowed")
        src = row.get("source")
        if src not in sources:
            errors.append(f"{rid}: source {src!r} has no file in sources/")
            continue
        anchor = norm(row.get("anchor", ""))
        if len(anchor) < 12:
            errors.append(f"{rid}: anchor too short to prove anything")
        elif anchor not in sources[src]:
            errors.append(f"{rid}: anchor not found verbatim in {src}")
    return errors


def render(rows: list[dict]) -> str:
    lines = [
        "# Claims register",
        "",
        "Generated from [`register.json`](register.json) by "
        "[`check_register.py`](check_register.py); edit the JSON, not this file.",
        "",
        "Every row is one claim a preliminary source makes, with a short verbatim "
        "anchor proving the source makes it. *Status* records what the lab has "
        "done with the claim; nothing reaches the talk with a status other than "
        "`verified`, `corrected`, `lab_supported` or `stipulation`.",
        "",
    ]
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    lines.append("Status counts: " + ", ".join(
        f"{k} {v}" for k, v in sorted(counts.items())) + f" — {len(rows)} rows.")
    for sec in ["S1", "S2", "S3", "S4", "S5", "S6", "X"]:
        sec_rows = [r for r in rows if r["section"] == sec]
        if not sec_rows:
            continue
        lines += ["", f"## {sec} — {SECTION_TITLES[sec]} ({len(sec_rows)})", "",
                  "| id | source | kind | claim | cited work | status | note |",
                  "| --- | --- | --- | --- | --- | --- | --- |"]
        for r in sec_rows:
            cells = [r["id"], r["source"] + (f" t{r['turn']}" if r.get("turn") else ""),
                     r["kind"], r["claim"], r.get("cited_work") or "",
                     r["status"], r.get("note") or ""]
            cells = [str(c).replace("|", "\\|").replace("\n", " ") for c in cells]
            lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rows = json.loads(REGISTER.read_text(encoding="utf-8"))
    errors = check(rows)
    for e in errors:
        print("FAIL", e)
    table = render(rows)
    if a.write:
        TABLE.write_text(table, encoding="utf-8")
    elif TABLE.read_text(encoding="utf-8") != table:
        errors.append("REGISTER.md is stale; run with --write")
        print("FAIL REGISTER.md is stale; run with --write")
    print(f"{len(rows)} rows, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
