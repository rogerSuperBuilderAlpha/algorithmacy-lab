"""Analysis for the phi_measure_fragmentation review: reliability + the three hypothesis tests.

    python -m org_frontier.reviews.phi_measure_fragmentation.run

Reads coding/ (independent coder JSONL), literature/corpus.jsonl, and edges/ (harvested graph),
writes results/frozen.json, results/summary.json, and clusters.json, and prints the per-hypothesis
verdicts. Standard library only; uses the arm's reusable tooling. If edges/ is sparse (harvest
rate-limited), H3 is reported as partial.
"""

import json
import os
from collections import Counter

from org_frontier.reviews.lib import bibliometrics, reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["measure_family", "validation", "substrate"]


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
    n = len(frozen)

    print("\n" + "=" * 70)
    # --- H1: many distinct measure families ---
    fam = Counter(r["measure_family"] for r in frozen)
    families_ge3 = {k: v for k, v in fam.items() if k != "na" and v >= 3}
    top_share = max(v for k, v in fam.items() if k != "na") / n
    print("H1 (many distinct measure families):")
    for k, v in fam.most_common():
        print(f"    {k:22} {v:3}  ({100*v/n:.0f}%)")
    print(f"   families with >=3 sources: {len(families_ge3)}; "
          f"largest family share {top_share:.0%} (majority = >50%)")

    # --- H2: asserted, not validated against a ground truth ---
    val = Counter(r["validation"] for r in frozen)
    gt = val.get("ground_truth", 0)
    print(f"\nH2 (asserted, not validated): validation {dict(val)}")
    print(f"   ground_truth {gt}/{n} ({100*gt/n:.0f}%); "
          f"none-or-internal {val.get('none/conceptual',0)+val.get('internal',0)}/{n} "
          f"({100*(val.get('none/conceptual',0)+val.get('internal',0))/n:.0f}%)")

    # --- H3: fragmentation on the citation graph ---
    cluster_of = {s: r["measure_family"] for s, r in fro.items()}
    json.dump(cluster_of, open(os.path.join(HERE, "clusters.json"), "w"), indent=1)
    edges = bibliometrics.load_edges(os.path.join(HERE, "edges"))
    resolved = sum(1 for e in edges.values() if "error" not in e)
    seeds = {r["slug"]: r for r in json.load(open(os.path.join(HERE, "seeds.json")))} \
        if os.path.exists(os.path.join(HERE, "seeds.json")) else None
    clusters = sorted(set(cluster_of.values()))
    links = bibliometrics.cluster_matrix(edges, cluster_of, seeds)
    within = sum(v for k, v in links.items() if k[0] == k[1])
    cross = sum(v for k, v in links.items() if k[0] != k[1])
    print(f"\nH3 (fragmentation): edges harvested {len(edges)}/{n} seeds, resolved {resolved}")
    if links:
        bibliometrics.print_matrix(links, clusters)
        print(f"   within-family {within} vs cross-family {cross} "
              f"-> {'within > cross (fragmented)' if within > cross else 'cross >= within (connected)'}")
    else:
        print("   no intra-corpus citation links resolved yet — H3 PARTIAL")

    summary = {"n": n, "measure_family": dict(fam), "families_ge3": len(families_ge3),
               "largest_family_share": round(top_share, 3), "validation": dict(val),
               "ground_truth_rate": round(gt / n, 3),
               "kappa_note": "measure_family 0.963, validation 0.905, substrate 0.985",
               "h3_within": within, "h3_cross": cross, "edges_resolved": resolved}
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print(f"\nwrote results/frozen.json, results/summary.json, clusters.json")


if __name__ == "__main__":
    main()
