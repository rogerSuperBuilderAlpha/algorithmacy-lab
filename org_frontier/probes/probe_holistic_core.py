"""Probe 131 (P2) — what are the forms no cheap feature reaches?

Question: the full cheap panel tops out near 95% (#126), so ~5% of wirings stay misclassified. Are these
a coherent missed structure, or a scattered, near-boundary set the classifier is simply unsure about?
Hypothesis: they are scattered and near the decision boundary — not a single overlooked feature but the
genuinely holistic tail. Method: from the cached panel, find the forms a full-feature random forest
misclassifies under cross-validation; report their coupling and dynamics profile and how close their
predicted probability sits to the 0.5 boundary.

Reads: org_frontier/probes/results/residual_panel.csv (run Probe 125 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_holistic_core
"""

import csv
import os

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict

PANEL = os.path.join(os.path.dirname(__file__), "results", "residual_panel.csv")
FEATURES = ("n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
            "n_fixed", "n_reachable", "invertible", "max_period")


def main():
    print("PROBE 131 (P2) — the irreducibly-holistic forms")
    print("=" * 64)
    with open(PANEL) as fh:
        rows = list(csv.DictReader(fh))
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    miss = pred != y
    nb3 = np.array([int(r["n_bidir"]) == 3 for r in rows])
    per = np.array([int(r["max_period"]) for r in rows])
    print(f"  {len(y)} wirings; {int(miss.sum())} misclassified by the full-feature forest ({100*miss.mean():.1f}%)")
    print(f"  of the misses: {int((miss & nb3).sum())} are three-way-coupled, {int((miss & ~nb3).sum())} are not")
    print(f"  predicted probability of the misses: mean |p-0.5| = {np.mean(np.abs(proba[miss]-0.5)):.3f}")
    print(f"  predicted probability of the hits:   mean |p-0.5| = {np.mean(np.abs(proba[~miss]-0.5)):.3f}")
    near = np.mean(np.abs(proba[miss] - 0.5) < 0.25)
    print(f"  fraction of misses within 0.25 of the boundary: {near:.2f}")
    print(f"  misses' attractor period: mean {per[miss].mean():.2f} vs hits {per[~miss].mean():.2f}")
    print("=" * 64)
    if near > 0.6:
        print("  Reading: the misclassified forms sit near the decision boundary, where the classifier is")
        print("  unsure — a scattered holistic tail, not a coherent structure a single missing feature")
        print("  would resolve. The last few percent are genuinely irreducible to cheap features.")
    else:
        print("  Reading: many misses sit far from the boundary, where the classifier is confidently wrong —")
        print("  a sign of a coherent structure the cheap features systematically misread, worth isolating.")
    print("=" * 64)


if __name__ == "__main__":
    main()
