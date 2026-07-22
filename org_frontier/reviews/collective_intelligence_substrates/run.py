"""Analysis for the collective_intelligence_substrates review: reliability + the three hypothesis tests.

    python3 -m org_frontier.reviews.collective_intelligence_substrates.run

Reads coding/ (independent coder JSONL), literature/corpus.jsonl, and edges/ (harvested graph),
writes results/frozen.json, clusters.json, and results/summary.json, and prints the per-hypothesis
verdicts. Standard library only; uses the arm's reusable tooling.
"""

import json
import os
from collections import Counter

from org_frontier.reviews.lib import bibliometrics, reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["substrate", "method", "spans_multiple"]


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def main():
    corpus = _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))
    n = len(corpus)

    # --- reliability + adjudicated dataset ---
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))
    fro = {r["slug"]: r for r in frozen}

    # clusters.json: slug -> adjudicated substrate (the H1 cluster key)
    cluster_of = {s: r["substrate"] for s, r in fro.items()}
    json.dump(cluster_of, open(os.path.join(HERE, "clusters.json"), "w"), indent=1)

    print("\n" + "=" * 70)
    # --- H2: substrate frequency ---
    sub = Counter(r["substrate"] for r in frozen)
    human = sub.get("human_team", 0) + sub.get("crowd", 0)
    print("H2 (human teams + crowds dominate):")
    for k, v in sub.most_common():
        print(f"   {k:16}{v:>3}  ({100*v/len(frozen):.0f}%)")
    print(f"   human_team+crowd = {human}/{len(frozen)} ({100*human/len(frozen):.0f}%); "
          f"swarm = {sub.get('swarm',0)}; ai_multiagent = {sub.get('ai_multiagent',0)}")

    # --- H3: cross-substrate synthesis ---
    spans = sum(1 for r in frozen if r["spans_multiple"] == "yes")
    print(f"H3 (cross-substrate synthesis rare): spans_multiple=yes "
          f"{spans}/{len(frozen)} ({100*spans/len(frozen):.0f}%)")

    # --- method context ---
    meth = Counter(r["method"] for r in frozen)
    print(f"method mix: {dict(meth)}")

    # --- H1: substrate citation matrix ---
    edges = bibliometrics.load_edges(os.path.join(HERE, "edges"))
    seeds = {r["slug"]: r for r in json.load(open(os.path.join(HERE, "seeds.json")))} \
        if os.path.exists(os.path.join(HERE, "seeds.json")) else None
    resolved = sum(1 for e in edges.values() if "error" not in e)
    clusters = sorted(set(cluster_of.values()))
    links = bibliometrics.cluster_matrix(edges, cluster_of, seeds)
    within = sum(v for k, v in links.items() if k[0] == k[1])
    cross = sum(v for k, v in links.items() if k[0] != k[1])
    print(f"\nH1 (fragmented by substrate): edges harvested {len(edges)}, resolved {resolved}")
    bibliometrics.print_matrix(links, clusters)
    print("\nassembly-spanning citers:")
    for k, v in sorted(bibliometrics.spanning(edges, cluster_of, seeds).items(), reverse=True):
        print(f"   spans {k}: {v} external papers")

    summary = {"n": n, "substrate": dict(sub), "method": dict(meth),
               "spans_yes": spans, "edges_resolved": resolved,
               "within_substrate_links": within, "cross_substrate_links": cross,
               "cluster_links": {f"{a}|{b}": v for (a, b), v in links.items()}}
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print(f"\nwrote results/frozen.json, results/summary.json, clusters.json")


if __name__ == "__main__":
    main()
