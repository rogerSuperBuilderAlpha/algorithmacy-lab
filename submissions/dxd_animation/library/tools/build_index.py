#!/usr/bin/env python3
"""Generate the dxd_animation library's index files from the card frontmatter.

Deterministic: output depends only on the card files on disk (sorted). Adapted from
D/current/monograph/library/tools/build_index.py; the only changes are the facet/claim tags in place of
chapter/section tags and the body heading "What the paper uses it for". It formats the records; it
writes no card prose.

    python3 -I tools/build_index.py           # rewrite INDEX.md, TRACKER.tsv, references.bib, REFERENCES_APA.md
    python3 -I tools/build_index.py --check   # exit 1 if any output is stale or a card is malformed
"""
import glob
import os
import re
import sys

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(LIB, "cards")
OUTS = {k: os.path.join(LIB, k) for k in ("INDEX.md", "TRACKER.tsv", "references.bib", "REFERENCES_APA.md")}

VOCAB = {
    "type": {"article", "book", "chapter", "proceedings", "report", "thesis", "preprint", "web", "legal",
             "dataset", "software"},
    "role": {"anchor", "support", "contrast", "method", "data"},
    "load": {"load-bearing", "exists"},
    "read_depth": {"full_text", "partial", "abstract", "metadata"},
    "verified": {"pending", "verified", "corrected", "unverifiable"},
    "status": {"cited", "candidate", "dropped"},
}
REQUIRED = ["key", "apa", "authors", "year", "title", "type", "facets", "claims", "role", "load",
            "read_depth", "object_read", "verified", "status", "added", "run"]
LISTS = {"facets", "claims", "prior_cards"}
BODY = ["## What it argues", "## What the paper uses it for", "## Loci", "## Caution"]
FACETS = {
    "F1": "Animation theory and the animator's craft",
    "F2": "Apparent motion and film perception",
    "F3": "Anthropomorphism, the ELIZA effect, the media equation",
    "F4": "Stream timing: typing delays, token pacing, latency",
    "F5": "Deciding with a moving goal: goal formation, constructed preference, NDM",
    "F6": "Choice architecture, digital nudging, dark patterns",
    "F7": "Platform opacity, co-optation, transparency critique",
    "F8": "The HF automation dyad versus a triad",
    "F9": "Interface animation in HCI",
    "F10": "Agent-mediated shopping and agentic commerce",
    "G": "Gap check: prior work framing LLM interfaces as animation",
}
CLAIMS = {
    "c1": "a moving goal breaks conversion-era design",
    "c2": "the user is human: biological, cognitive, emotional",
    "c3": "the platform environment is opaque, co-optive and triadic",
    "c4": "an LLM interface is an animation",
    "c5": "animation is opaque: the missing frames",
    "c6": "animation is co-optive: the viewer locks in; the user also animates",
    "c7": "animation is triadic: viewer, character, animator",
    "c8": "DXD must apply the animator's methods",
    "c9": "gap: no prior work frames LLM interfaces as animation for decision design",
}


def frontmatter(text):
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    for line in m.group(1).splitlines():
        mm = re.match(r"([A-Za-z_]+):\s*(.*)$", line)
        if not mm:
            continue
        k, v = mm.group(1), mm.group(2).strip()
        if k in LISTS:
            v = [x.strip().strip('"') for x in v.strip("[]").split(",") if x.strip()]
        else:
            v = v.strip('"')
        fm[k] = v
    return fm


def load():
    cards, malformed = [], []
    for p in sorted(glob.glob(os.path.join(CARDS, "*.md"))):
        name = os.path.basename(p)[:-3]
        text = open(p, encoding="utf-8").read()
        fm = frontmatter(text)
        problems = []
        if fm is None:
            malformed.append(f"{name}: no frontmatter")
            continue
        problems += [f"missing {k}" for k in REQUIRED if not fm.get(k)]
        if fm.get("key") and fm["key"] != name:
            problems.append(f"key {fm['key']} != filename")
        for k, allowed in VOCAB.items():
            if fm.get(k) and fm[k] not in allowed:
                problems.append(f"{k}={fm[k]}")
        bad = [c for c in fm.get("facets", []) if c not in FACETS]
        if bad:
            problems.append(f"facets {bad}")
        bad = [c for c in fm.get("claims", []) if c not in CLAIMS]
        if bad:
            problems.append(f"claims {bad}")
        problems += [f"no section '{h}'" for h in BODY if h not in text]
        if problems:
            malformed.append(f"{name}: " + "; ".join(problems))
        fm["_path"] = f"cards/{name}.md"
        cards.append(fm)
    return cards, malformed


def cell(s, n=None):
    s = (s or "").replace("|", "\\|")
    return s if n is None or len(s) <= n else s[: n - 1] + "…"


def table(rows):
    L = ["| key | work | role | load | read | verified |", "|---|---|---|---|---|---|"]
    L += [f"| [{c['key']}]({c['_path']}) | {cell(c.get('authors'), 40)} ({c.get('year')}). "
          f"{cell(c.get('title'), 70)} | {c.get('role')} | {c.get('load')} | {c.get('read_depth')} | "
          f"{c.get('verified')} |" for c in rows]
    return L


def index_md(cards):
    live = [c for c in cards if c.get("status") != "dropped"]
    n = len(live)
    count = lambda k, v: sum(1 for c in live if c.get(k) == v)
    L = ["# Option C library — index", "",
         "*Generated by `tools/build_index.py`. Do not edit by hand — edits are overwritten.*", "",
         f"**{n} live cards** ({len(cards) - n} dropped). "
         f"Read depth — full_text {count('read_depth', 'full_text')}, partial {count('read_depth', 'partial')}, "
         f"abstract {count('read_depth', 'abstract')}, metadata {count('read_depth', 'metadata')}. "
         f"Verification — verified {count('verified', 'verified')}, corrected {count('verified', 'corrected')}, "
         f"unverifiable {count('verified', 'unverifiable')}, pending {count('verified', 'pending')}.", "",
         "Vocabularies and the card format are in `README.md`. `TRACKER.tsv` holds the same records for "
         "sorting and filtering.", ""]
    L += ["## Load-bearing cards not read in full", ""]
    weak = [c for c in live if c.get("load") == "load-bearing" and c.get("read_depth") in ("abstract", "metadata")]
    L += [f"- [{c['key']}]({c['_path']}) — {c.get('read_depth')}; claims {', '.join(c.get('claims', []))}"
          for c in weak] or ["*None.*"]
    L.append("")
    L += ["## By facet", ""]
    for f, name in FACETS.items():
        here = sorted((c for c in live if f in c.get("facets", [])), key=lambda c: c["key"])
        L += [f"### {f} — {name} ({len(here)})", ""]
        L += table(here) if here else ["*No cards yet.*"]
        L.append("")
    L += ["## By claim", ""]
    for cl, name in CLAIMS.items():
        here = sorted((c for c in live if cl in c.get("claims", [])), key=lambda c: c["key"])
        L += [f"### {cl} — {name} ({len(here)})", ""]
        L += table(here) if here else ["*No cards yet.*"]
        L.append("")
    L += ["## All cards, A–Z", "", "| key | year | title | facets | claims | status |", "|---|---|---|---|---|---|"]
    L += [f"| [{c['key']}]({c['_path']}) | {c.get('year')} | {cell(c.get('title'), 80)} | "
          f"{', '.join(c.get('facets', []))} | {', '.join(c.get('claims', []))} | {c.get('status')} |" for c in cards]
    return "\n".join(L).rstrip() + "\n"


def tracker(cards):
    cols = ["key", "year", "authors", "title", "type", "doi", "facets", "claims", "role", "load",
            "read_depth", "verified", "status", "object_read", "prior_cards", "added", "run"]
    rows = ["\t".join(cols)]
    for c in cards:
        rows.append("\t".join((", ".join(c.get(k, [])) if k in LISTS else str(c.get(k, ""))).replace("\t", " ")
                              for k in cols))
    return "\n".join(rows) + "\n"


BIBTYPE = {"article": "article", "book": "book", "chapter": "incollection", "proceedings": "inproceedings",
           "report": "techreport", "thesis": "phdthesis", "preprint": "misc", "web": "misc", "legal": "misc",
           "dataset": "misc", "software": "misc"}


def bib(cards):
    out = []
    for c in cards:
        if c.get("status") == "dropped":
            continue
        f = [("author", c.get("authors", "").replace(";", " and")), ("title", c.get("title")),
             ("year", c.get("year")), ("journal" if c.get("type") == "article" else "booktitle", c.get("venue")),
             ("volume", c.get("volume")), ("number", c.get("issue")), ("pages", c.get("pages")),
             ("doi", c.get("doi")), ("url", c.get("url"))]
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in f if v)
        out.append(f"@{BIBTYPE.get(c.get('type'), 'misc')}{{{c['key']},\n{body}\n}}")
    return "% Generated by tools/build_index.py from card frontmatter. Do not edit by hand.\n\n" + \
        "\n\n".join(out) + "\n"


def apa(cards):
    live = sorted((c for c in cards if c.get("status") == "cited"), key=lambda c: c.get("apa", "").lower())
    return "# References (APA 7) — cards with status `cited`\n\n" \
           "*Generated by `tools/build_index.py` from each card's `apa` field. Do not edit by hand.*\n\n" + \
           "\n\n".join(c["apa"] for c in live) + "\n"


def main():
    cards, malformed = load()
    outs = {"INDEX.md": index_md(cards), "TRACKER.tsv": tracker(cards), "references.bib": bib(cards),
            "REFERENCES_APA.md": apa(cards)}
    if "--check" in sys.argv:
        stale = [k for k, v in outs.items()
                 if not os.path.exists(OUTS[k]) or open(OUTS[k], encoding="utf-8").read() != v]
        for m in malformed:
            print("MALFORMED", m)
        if stale:
            print("STALE:", ", ".join(stale), "— run tools/build_index.py")
        print(f"{len(cards)} cards; {len(malformed)} malformed; {len(stale)} stale outputs")
        sys.exit(1 if (stale or malformed) else 0)
    for k, v in outs.items():
        open(OUTS[k], "w", encoding="utf-8").write(v)
    print(f"{len(cards)} cards; wrote {', '.join(outs)}")
    for m in malformed:
        print("WARNING malformed", m)


if __name__ == "__main__":
    main()
