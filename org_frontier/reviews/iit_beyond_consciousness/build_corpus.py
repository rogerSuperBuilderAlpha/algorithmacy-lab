"""Build the corpus for the iit_beyond_consciousness review from Semantic Scholar search.

Runs a fixed set of keyword queries (integrated information / IIT / phi crossed with
non-individual-brain substrates), collects candidates, deduplicates, and applies the boundary rule
(mentions IIT/Phi AND a non-brain-system term; not pure brain-only consciousness work). Writes:

  literature/corpus.jsonl        — one screened in-boundary source per line
  seeds.json                     — [{slug, doi|title}] for lib/harvest.py
  literature/screened_out.jsonl  — candidates dropped by the boundary rule (auditable)

    python -m org_frontier.reviews.iit_beyond_consciousness.build_corpus

Deterministic given the API's responses; standard library only. No model tokens.
"""

import json
import os
import re
import time
import urllib.parse
import urllib.request

API = "https://api.semanticscholar.org/graph/v1/paper/search"
HERE = os.path.dirname(__file__)

QUERIES = [
    "integrated information theory organization",
    "integrated information theory collective",
    "integrated information phi social system",
    "integrated information phi economy market",
    "integrated information swarm collective behavior",
    "integrated information ant colony superorganism",
    "integrated information multi-agent system",
    "integrated information theory group cognition",
    "phi integrated information firm team coordination",
    "integrated information society social network",
    "integrated information collective intelligence",
    "integrated information theory beyond brain",
    "IIT phi non-neural systems",
    "integrated information distributed cognition organization",
]

IIT_TERMS = re.compile(r"integrated information|\biit\b|\bphi\b|Φ", re.I)
SUBSTRATE = re.compile(
    r"organization|organisation|\bfirm\b|\bteam\b|collective|social|societ|econom|\bmarket|"
    r"swarm|ant colon|superorganism|multi-?agent|\bgroup\b|institution|coordinat|distributed cognition|"
    r"collective intelligence|beyond (the )?brain|non-neural|ecosystem|\bcolony\b", re.I)
COLLECTIVE = re.compile(r"organization|organisation|collective|swarm|econom|social network|"
                        r"superorganism|multi-?agent|ant colon|society|institution|\bmarket", re.I)
BRAIN_ONLY = re.compile(r"anesthe|anaesthe|\beeg\b|\bfmri\b|\bcoma\b|vegetative state|\bsleep\b|"
                        r"cortic|disorders of consciousness|\bpatients\b|clinical", re.I)


def _get(url, tries=6):
    wait, key = 3.0, os.environ.get("S2_API_KEY")
    headers = {"x-api-key": key} if key else {}
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                return json.load(r)
        except Exception:
            time.sleep(wait)
            wait *= 2
    return None


def slugify(title, year, taken):
    base = re.sub(r"[^a-z0-9]+", "", (title or "").lower())[:24] or "src"
    slug = f"{base}{year or ''}"
    n, out = 1, slug
    while out in taken:
        n += 1
        out = f"{slug}_{n}"
    taken.add(out)
    return out


def in_boundary(text):
    t = text or ""
    if not IIT_TERMS.search(t) or not SUBSTRATE.search(t):
        return False
    if BRAIN_ONLY.search(t) and not COLLECTIVE.search(t):
        return False
    return True


def main():
    seen, taken, kept, dropped = set(), set(), [], []
    for q in QUERIES:
        url = (f"{API}?query={urllib.parse.quote(q)}"
               f"&fields=paperId,title,abstract,year,venue,externalIds,citationCount&limit=100")
        data = _get(url)
        hits = (data or {}).get("data", []) or []
        for p in hits:
            pid = p.get("paperId")
            if not pid or pid in seen:
                continue
            seen.add(pid)
            title, ab = p.get("title") or "", p.get("abstract") or ""
            rec = {"paperId": pid, "title": title, "abstract": ab, "year": p.get("year"),
                   "venue": p.get("venue"), "doi": (p.get("externalIds") or {}).get("DOI"),
                   "citationCount": p.get("citationCount")}
            (kept if in_boundary(title + " " + ab) else dropped).append(rec)
        print(f"query {q!r}: {len(hits)} hits")
        time.sleep(1.5)

    for r in kept:
        r["slug"] = slugify(r["title"], r["year"], taken)
    os.makedirs(os.path.join(HERE, "literature"), exist_ok=True)
    with open(os.path.join(HERE, "literature", "corpus.jsonl"), "w") as fh:
        for r in kept:
            fh.write(json.dumps(r) + "\n")
    with open(os.path.join(HERE, "literature", "screened_out.jsonl"), "w") as fh:
        for r in dropped:
            fh.write(json.dumps(r) + "\n")
    seeds = [{"slug": r["slug"], "doi": r["doi"]} if r["doi"]
             else {"slug": r["slug"], "title": r["title"]} for r in kept]
    json.dump(seeds, open(os.path.join(HERE, "seeds.json"), "w"), indent=1)
    print(f"\nkept (in-boundary): {len(kept)}  |  screened out: {len(dropped)}  |  "
          f"unique candidates: {len(seen)}")
    print(f"wrote literature/corpus.jsonl, seeds.json ({len(seeds)}), literature/screened_out.jsonl")


if __name__ == "__main__":
    main()
