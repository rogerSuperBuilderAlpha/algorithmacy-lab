#!/usr/bin/env python3
"""Regenerate INDEX.md from literature/cards/*.md.

Run from this directory after adding or rewriting any card:
    python3 _build_index.py
"""
from __future__ import annotations

import glob
import os
import re
from collections import Counter, defaultdict

CARDS_DIR = "cards"
OUT = "INDEX.md"
GENERATED = {OUT, "README.md", "REFERENCES.md", "COVERAGE.md", "TRAPS.md",
             "ZHOU_2025_INSTRUMENT.md"}

FULL = {"full_text", "author_manuscript", "full_text_passages", "full",
        "full_text_via_authors_revisited", "argument",
        "canonical_summary_plus_scholarship"}
DEPTH_ORDER = ["full_text", "author_manuscript", "extended_preview",
               "abstract_plus_reviews", "abstract_only", "citing_reconstruction",
               "publisher_record", "metadata_only"]
DLABEL = {
    "full_text": "Full text",
    "author_manuscript": "Author manuscript",
    "extended_preview": "Extended preview",
    "abstract_plus_reviews": "Abstract + reviews",
    "abstract_only": "Abstract only",
    "citing_reconstruction": "Citing reconstruction",
    "publisher_record": "Publisher record",
    "metadata_only": "Metadata only",
}

# Dual filenames from the 18 August sweep. Junior slugs stay on disk;
# the index lists them under the canonical slug.
CANONICAL = {
    "klawitterhargittai2018": "klawitter2018",
    "cotterreisdorf2020": "cotter2020",
    "long2020": "longmagerko2020",
}


def _first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    if not text:
        return ""
    m = re.match(r"(.+?[.!?])(?:\s|$)", text)
    s = m.group(1) if m else text
    if len(s) > 260:
        s = s[:257].rsplit(" ", 1)[0] + "…"
    return s


def parse(path: str) -> dict:
    t = open(path, encoding="utf-8").read()
    lines = t.splitlines()
    slug = os.path.splitext(os.path.basename(path))[0]
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), slug)
    meta = next((l for l in lines if "Read depth:" in l or "Identifier:" in l), "")
    md = re.search(r"Read depth:\*\*?\s*([a-z_]+)", meta) or re.search(
        r"(full_text|author_manuscript|extended_preview|abstract_plus_reviews|"
        r"abstract_only|citing_reconstruction|publisher_record|metadata_only)", t)
    depth = md.group(1) if md else "abstract_only"
    cm = re.search(r"\*\*Cluster:\*\*\s*(\S+)", t)
    cluster = cm.group(1).rstrip(";").split(";")[0] if cm else ""
    rel = ""
    for i, l in enumerate(lines):
        if l.strip().lower().startswith("## relation"):
            for l2 in lines[i + 1:]:
                if l2.strip() and not l2.startswith("#"):
                    rel = _first_sentence(l2)
                    break
            break
    junior = slug in CANONICAL or any(
        l.startswith("> **Junior slug.**") for l in lines[:4])
    return {
        "slug": slug,
        "title": title,
        "depth": depth,
        "cluster": cluster,
        "rel": rel,
        "junior": junior,
        "canonical": CANONICAL.get(slug),
    }


def _dl(d: str) -> str:
    return DLABEL.get(d, d.replace("_", " ").capitalize())


def _depth_key(d: str) -> tuple:
    return (d not in FULL, DEPTH_ORDER.index(d) if d in DEPTH_ORDER else 99, d)


def main() -> None:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    paths = sorted(glob.glob(os.path.join(CARDS_DIR, "*.md")))
    entries = [parse(p) for p in paths]
    c = Counter(e["depth"] for e in entries)
    depths_present = sorted(c, key=_depth_key)
    by_cluster: dict[str, list] = defaultdict(list)
    for e in entries:
        by_cluster[e["cluster"]].append(e)
    clusters = sorted(k for k in by_cluster if k)
    if "" in by_cluster:
        clusters.append("")

    o = [
        "# Lima PDW — literature index\n",
        f"{len(entries)} cards in [`cards/`](cards/). Grouped by cluster, then by "
        "read depth. Blurb is the first sentence of **Relation to the argument**. "
        "Regenerate with `_build_index.py`.\n",
        "This is the working library for the Lima support arm. Paper 2's 44 cited "
        "works are mapped in [`COVERAGE.md`](COVERAGE.md). Citation hazards are in "
        "[`TRAPS.md`](TRAPS.md). How to add a card is in [`README.md`](README.md).\n",
        "## Dual filenames\n",
        "Three works were carded twice in the 18 August sweep. Both files stay. "
        "The junior slug points at the canonical one.\n",
        "- `klawitter2018` ← `klawitterhargittai2018`",
        "- `cotter2020` ← `cotterreisdorf2020`",
        "- `longmagerko2020` (Paper 2 / dissertation slug) ← `long2020` (fuller, `full_text`)\n",
        "## Read-depth summary\n",
        "| Depth | Count |",
        "|---|---|",
    ]
    for d in depths_present:
        o.append(f"| {_dl(d)} | {c[d]} |")
    o.append("\n## Clusters\n")
    o.append("| Cluster | Count |")
    o.append("|---|---|")
    for cl in clusters:
        label = cl if cl else "(unclustered)"
        o.append(f"| {label} | {len(by_cluster[cl])} |")
    o.append("\n---\n")

    for cl in clusters:
        grp = by_cluster[cl]
        heading = cl if cl else "Unclustered"
        o.append(f"## {heading} ({len(grp)})\n")
        by_d: dict[str, list] = defaultdict(list)
        for e in grp:
            by_d[e["depth"]].append(e)
        for d in sorted(by_d, key=_depth_key):
            o.append(f"### {_dl(d)}\n")
            for e in sorted(by_d[d], key=lambda x: x["title"].lower()):
                note = ""
                if e["junior"] and e["canonical"]:
                    note = f"  \n  Junior slug of [`{e['canonical']}`](cards/{e['canonical']}.md)."
                blurb = e["rel"] or ""
                o.append(f"- **[{e['title']}](cards/{e['slug']}.md)**  \n  {blurb}{note}")
            o.append("")

    open(OUT, "w", encoding="utf-8").write("\n".join(o) + "\n")
    print(f"entries: {len(entries)} | depth: {dict(c)} | clusters: {len(clusters)}")


if __name__ == "__main__":
    main()
