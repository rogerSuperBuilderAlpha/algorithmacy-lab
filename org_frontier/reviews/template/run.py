"""Run the analysis for this review: reliability + adjudication, then the hypothesis tests.

Copy alongside your review's data. Fill in the variable names and the per-hypothesis tests, then:

    python -m org_frontier.reviews.<slug>.run

Assumes coder files in coding/, harvested edges in edges/, and clusters.json + seeds.json present.
Standard library only; imports the arm's reusable tooling.
"""

import json
import os

from org_frontier.reviews.lib import bibliometrics, reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["<var1>", "<var2>"]   # fill in
SET_VALUED = ["<setvar>"]            # fill in


def main():
    # 1. reliability + adjudicated dataset
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, SET_VALUED,
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))

    # 2. bibliometrics
    edges = bibliometrics.load_edges(os.path.join(HERE, "edges"))
    cluster_of = json.load(open(os.path.join(HERE, "clusters.json")))
    seeds_path = os.path.join(HERE, "seeds.json")
    seeds = {s["slug"]: s for s in json.load(open(seeds_path))} if os.path.exists(seeds_path) else None
    clusters = sorted(set(cluster_of.values()))
    bibliometrics.print_matrix(bibliometrics.cluster_matrix(edges, cluster_of, seeds), clusters)

    # 3. per-hypothesis tests on `frozen` — fill in
    # e.g. Counter(r["<var1>"] for r in frozen), cross-tabs, proportions...
    print(f"\ncoded sources: {len(frozen)}")


if __name__ == "__main__":
    main()
