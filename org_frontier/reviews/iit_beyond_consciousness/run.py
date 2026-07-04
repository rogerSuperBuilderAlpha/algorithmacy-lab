"""Analysis for the iit_beyond_consciousness review: reliability + the four hypothesis tests.

    python -m org_frontier.reviews.iit_beyond_consciousness.run

Reads coding/ (independent coder JSONL), literature/corpus.jsonl, and edges/ (harvested graph),
writes results/frozen.json and results/summary.json, and prints the per-hypothesis verdicts.
Standard library only; uses the arm's reusable tooling.
"""

import json
import os
from collections import Counter

from org_frontier.reviews.lib import bibliometrics, reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["substrate", "evidence", "claim_type", "cites_org_theory"]


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def main():
    corpus = _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))
    by_slug = {r["slug"]: r for r in corpus}

    # --- reliability + adjudicated dataset ---
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))
    fro = {r["slug"]: r for r in frozen}

    print("\n" + "=" * 70)
    # --- H1: size and recency ---
    years = [by_slug[s].get("year") for s in fro if by_slug.get(s, {}).get("year")]
    years = [y for y in years if y]
    n = len(frozen)
    post2015 = sum(1 for y in years if y >= 2015)
    print(f"H1 (small & recent): corpus n = {n}; with year = {len(years)}; "
          f">=2015: {post2015} ({100*post2015/len(years):.0f}% of dated)" if years else
          f"H1: corpus n = {n}")
    if years:
        print(f"   year range {min(years)}-{max(years)}; median {sorted(years)[len(years)//2]}")

    # --- H3: asserted vs measured ---
    ev = Counter(r["evidence"] for r in frozen)
    emp = ev.get("empirical", 0)
    print(f"H3 (asserted not measured): evidence {dict(ev)}; "
          f"empirical {emp}/{n} ({100*emp/n:.0f}%)")

    # --- H2 (coded cross-check): engagement with org theory ---
    cot = Counter(r["cites_org_theory"] for r in frozen)
    print(f"H2 (disconnected, coded): cites_org_theory {dict(cot)}; "
          f"engages org theory {cot.get('yes',0)}/{n} ({100*cot.get('yes',0)/n:.0f}%)")

    # --- H4 + H2 (bibliometric): substrate clusters + coordination-canon cross-citation ---
    edges = bibliometrics.load_edges(os.path.join(HERE, "edges"))
    seeds = {r["slug"]: r for r in json.load(open(os.path.join(HERE, "seeds.json")))} \
        if os.path.exists(os.path.join(HERE, "seeds.json")) else None
    # clusters: IIT sources -> coded substrate; canon seeds -> coordination_canon
    cluster_of = {s: r["substrate"] for s, r in fro.items()}
    canon = json.load(open(os.path.join(HERE, "canon_seeds.json")))
    for c in canon:
        cluster_of[c["slug"]] = "coordination_canon"
    json.dump(cluster_of, open(os.path.join(HERE, "clusters.json"), "w"), indent=1)
    clusters = sorted(set(cluster_of.values()))
    links = bibliometrics.cluster_matrix(edges, cluster_of, seeds)
    print("\nH4 (substrate clustering) + H2 (canon cross-citation):")
    bibliometrics.print_matrix(links, clusters)
    canon_links = sum(v for k, v in links.items()
                      if "coordination_canon" in k and k[0] != k[1])
    print(f"   IIT-corpus <-> coordination_canon citation links: {canon_links}")

    summary = {"n": n, "years": {"post2015": post2015, "dated": len(years)},
               "evidence": dict(ev), "cites_org_theory": dict(cot),
               "cluster_links": {f"{a}|{b}": v for (a, b), v in links.items()},
               "canon_cross_links": canon_links}
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print(f"\nwrote results/frozen.json, results/summary.json, clusters.json")


if __name__ == "__main__":
    main()
