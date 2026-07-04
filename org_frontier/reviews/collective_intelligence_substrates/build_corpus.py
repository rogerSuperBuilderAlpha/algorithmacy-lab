"""Build the corpus for the collective_intelligence_substrates review.

Reads the saved Scholar Gateway semanticSearch result files (each a scholar_gateway.response_payload
JSON), extracts title/abstract/year/doi for each returned article, deduplicates by DOI then by
normalized title, slugifies, and writes:

  literature/corpus.jsonl   — one in-boundary source per line {slug,title,abstract,year,doi}
  seeds.json                — [{slug, doi|title}] for lib/harvest.py

Boundary rule: the title+abstract must mention a collective-intelligence / collective-behavior term
AND name a substrate cue (group/team/crowd/swarm/agent/market/colony/flock). Pure single-topic hits
with no collective framing are screened out to literature/screened_out.jsonl.

    python3 -m org_frontier.reviews.collective_intelligence_substrates.build_corpus

Deterministic given the saved search files; standard library only. No model tokens.
"""

import glob
import json
import os
import re

HERE = os.path.dirname(__file__)
RESULTS_DIR = ("/Users/ludwitt/.claude/projects/"
               "-Users-ludwitt-iit-playground-pyphi-experiments-dissertation/"
               "b841b09d-f057-4d42-a757-2878fe2fee4c/tool-results")

# The eight Scholar Gateway searches run for THIS review (by result-file timestamp), so the corpus
# is not polluted by unrelated searches sharing the scratchpad results directory.
SEARCH_TS = ["1783181168526", "1783181170602", "1783181171345", "1783181196510",
             "1783181197525", "1783181198459", "1783181219481", "1783181219420",
             "1783181316105", "1783181316469", "1783181316620",
             "1783181323852", "1783181325488", "1783181326467"]

CI_TERMS = re.compile(
    r"collective intelligence|collective behavior|collective behaviour|wisdom of crowd|"
    r"swarm intelligence|collective decision|group performance|collective cognition|"
    r"crowdsourc|self-organi|stigmerg|superorganism|collective computation|hive mind|"
    r"emergent|collective wisdom|group intelligence|distributed cognition", re.I)
SUBSTRATE = re.compile(
    r"\bgroup\b|\bteam\b|crowd|swarm|\bagent|market|colony|colonies|flock|school|ant\b|"
    r"\bbee\b|human|robot|multi-?agent|\bllm\b|prediction market|insect|organis|society|"
    r"social|collective", re.I)


def _year(rec):
    md = (rec.get("metadata") or {}).get("additionalMetadata") or {}
    for field in ("publicationDate", "citationLine"):
        m = re.search(r"(19|20)\d{2}", md.get(field) or "")
        if m:
            return int(m.group(0))
    return None


def _norm(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:50]


def slugify(title, year, taken):
    base = re.sub(r"[^a-z0-9]+", "", (title or "").lower())[:24] or "src"
    slug = f"{base}{year or ''}"
    n, out = 1, slug
    while out in taken:
        n += 1
        out = f"{slug}_{n}"
    taken.add(out)
    return out


def main():
    files = [os.path.join(RESULTS_DIR, f"mcp-claude_ai_Scholar_Gateway-semanticSearch-{ts}.txt")
             for ts in SEARCH_TS]
    files = [f for f in files if os.path.exists(f)]
    by_doi, by_title = {}, {}
    candidates = []
    for f in files:
        try:
            payload = json.load(open(f))
        except (OSError, json.JSONDecodeError):
            continue
        for r in payload.get("results", []):
            md = (r.get("metadata") or {}).get("additionalMetadata") or {}
            title = md.get("title") or ""
            doi = (r.get("doi") or "").strip().lower()
            abstract = md.get("abstract") or r.get("text") or ""
            if not title:
                continue
            # dedup: a chunked article appears multiple times (same doi/title)
            key_doi = doi or None
            key_title = _norm(title)
            if key_doi and key_doi in by_doi:
                continue
            if key_title in by_title:
                continue
            rec = {"title": title.strip(), "abstract": re.sub(r"\s+", " ", abstract).strip(),
                   "year": _year(r), "doi": doi or None}
            candidates.append(rec)
            if key_doi:
                by_doi[key_doi] = rec
            by_title[key_title] = rec

    # Front-matter / clearly off-topic hits that the semantic search returns but that are not
    # collective-intelligence articles (news digests, section headers, unrelated humanities pieces).
    DROP = {"complexityatlarge", "cubanamericansandtheautobiography"}
    taken, kept, dropped = set(), [], []
    for rec in candidates:
        text = rec["title"] + " " + rec["abstract"]
        if _norm(rec["title"]) in DROP:
            dropped.append(rec)
        elif CI_TERMS.search(text) and SUBSTRATE.search(text):
            kept.append(rec)
        else:
            dropped.append(rec)

    for rec in kept:
        rec["slug"] = slugify(rec["title"], rec["year"], taken)

    os.makedirs(os.path.join(HERE, "literature"), exist_ok=True)
    with open(os.path.join(HERE, "literature", "corpus.jsonl"), "w") as fh:
        for rec in kept:
            fh.write(json.dumps({"slug": rec["slug"], "title": rec["title"],
                                 "abstract": rec["abstract"], "year": rec["year"],
                                 "doi": rec["doi"]}) + "\n")
    with open(os.path.join(HERE, "literature", "screened_out.jsonl"), "w") as fh:
        for rec in dropped:
            fh.write(json.dumps(rec) + "\n")
    seeds = [{"slug": r["slug"], "doi": r["doi"]} if r["doi"]
             else {"slug": r["slug"], "title": r["title"]} for r in kept]
    json.dump(seeds, open(os.path.join(HERE, "seeds.json"), "w"), indent=1)
    print(f"source files: {len(files)}  unique candidates: {len(candidates)}")
    print(f"kept (in-boundary): {len(kept)}  |  screened out: {len(dropped)}")
    print(f"with DOI: {sum(1 for r in kept if r['doi'])}  |  wrote corpus.jsonl, seeds.json")


if __name__ == "__main__":
    main()
