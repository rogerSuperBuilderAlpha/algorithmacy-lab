"""Probe Q124 (H1-H4) — is the verdict robust to the state-aggregation rule? (critical-review F1/T4)

For each triadic form, recomputes the verdict under max / mean / stationary / min aggregation of the per-state
Φ_MIP profile, and confirms no dyadic form turns triadic under any aggregation.

Run:  ~/iit-playground/venv-4.0/bin/python -m \
      org_frontier.questions.q124_aggregation_robustness.probe_aggregation_robustness
"""

import csv
import os

from org_frontier.questions.q124_aggregation_robustness import forms as F


def main():
    print("PROBE Q124 (H1-H4) — robustness of the verdict to the state-aggregation rule")
    print("=" * 78)
    triadic, dyadic = F.classify_family()
    print(f"  {len(triadic)} triadic, {len(dyadic)} dyadic forms")

    survives = {"max": 0, "mean": 0, "stationary": 0, "min": 0}
    for _, rules in triadic:
        agg = F.aggregations(rules)
        for rule, val in agg.items():
            if val > F.EPS:
                survives[rule] += 1
    nt = len(triadic)
    print(f"  triadic forms still triadic under each aggregation (of {nt}):")
    for rule in ("max", "mean", "stationary", "min"):
        print(f"     {rule:11s}: {survives[rule]}/{nt}")

    # no dyadic form becomes triadic under any aggregation (a dyadic form has Φ_MIP=0 at every state)
    dyadic_flips = 0
    for _, rules in dyadic:
        agg = F.aggregations(rules)
        if max(agg.values()) > F.EPS:
            dyadic_flips += 1

    h1 = survives["mean"] == nt                       # survives the uniform-mean aggregation
    h2 = survives["stationary"] == nt                 # survives the long-run stationary weighting
    h3 = survives["min"] < nt                         # the strict every-state rule flips some
    h4 = dyadic_flips == 0                            # no dyadic form gains a triadic verdict
    print("=" * 78)
    print(f"  H1 every triadic form survives mean aggregation:           {h1} ({survives['mean']}/{nt})")
    print(f"  H2 every triadic form survives stationary aggregation:     {h2} ({survives['stationary']}/{nt})")
    print(f"  H3 the strict min (every-state) rule flips some:           {h3} ({survives['min']}/{nt})")
    print(f"  H4 no dyadic form turns triadic under any aggregation:     {h4} ({dyadic_flips} flips)")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "aggregation_robustness.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["aggregation", "triadic_forms_surviving", "of_total"])
        for rule in ("max", "mean", "stationary", "min"):
            w.writerow([rule, survives[rule], nt])
        w.writerow(["dyadic_forms_flipping_to_triadic", dyadic_flips, len(dyadic)])


if __name__ == "__main__":
    main()
