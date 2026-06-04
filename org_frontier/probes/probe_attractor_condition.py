"""Probe 130 (P1) — is a collapsing attractor the dyadic condition among coupled wirings?

Question: the residual is all false positives — three-way-coupled wirings that are dyadic anyway (#125),
and those forms collapse to a fixed point fast. Among the three-way-coupled wirings, does attractor type
separate the verdict — are the dyadic ones exactly the ones whose dynamics collapses to a single fixed
point? Hypothesis: yes within coupling; a coupled wiring is dyadic when its map runs down to one
globally attracting fixed point and triadic when it sustains a cycle. Method: from the cached residual
panel, restrict to n_bidir==3; test attractor-type predicates (max period, fixed-point count,
reachability) against the verdict and report the best.

Reads: org_frontier/probes/results/residual_panel.csv (run Probe 125 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_attractor_condition
"""

import csv
import os

import numpy as np

PANEL = os.path.join(os.path.dirname(__file__), "results", "residual_panel.csv")


def main():
    print("PROBE 130 (P1) — attractor type vs the verdict among three-way-coupled wirings")
    print("=" * 70)
    with open(PANEL) as fh:
        rows = [r for r in csv.DictReader(fh) if int(r["n_bidir"]) == 3]
    y = np.array([int(r["triadic"]) for r in rows])
    per = np.array([int(r["max_period"]) for r in rows])
    nfix = np.array([int(r["n_fixed"]) for r in rows])
    reach = np.array([int(r["n_reachable"]) for r in rows])
    n = len(rows)
    print(f"  {n} three-way-coupled wirings, {int(y.sum())} triadic, {n - int(y.sum())} dyadic (the residual)")

    def report(name, pred):
        pred = np.array(pred, int)
        acc = (pred == y).mean()
        fp = int(((pred == 1) & (y == 0)).sum())
        fn = int(((pred == 0) & (y == 1)).sum())
        print(f"  {name:<34}acc={acc:.4f}  (fp={fp}, fn={fn})")
        return acc

    print(f"  {'predicate -> triadic':<34}result")
    report("max_period > 1", per > 1)
    report("max_period > 1 AND n_fixed <= 1", (per > 1) & (nfix <= 1))
    report("n_reachable > 2", reach > 2)
    report("max_period > 1 OR n_reachable > 4", (per > 1) | (reach > 4))
    print("=" * 70)
    print("  Reading: a predicate that perfectly separates the coupled wirings would make the verdict, given")
    print("  coupling, an attractor property — dyadic exactly when the dynamics collapses. A high but")
    print("  imperfect accuracy says attractor type carries most of the residual, with a holistic remainder.")
    print("=" * 70)


if __name__ == "__main__":
    main()
