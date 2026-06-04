"""Probe 126 (M2) — can any cheap feature panel close the residual?

Question: connectivity and synergy leave ~7% of the n=3 verdict undecided (#94, #106). Does a richer
panel — adding global-dynamics features — reach 100%, or is the residual irreducibly holistic?
Hypothesis: no cheap panel reaches 100%; the verdict is a property of the whole cause-effect structure
that no per-node, per-function, or coarse-dynamics feature captures. Method: from the cached residual
panel, fit a random forest on the full feature set with cross-validation and report the ceiling accuracy
and the feature importances.

Reads: org_frontier/probes/results/residual_panel.csv (run Probe 125 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_residual_ceiling
"""

import csv
import os

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score

PANEL = os.path.join(os.path.dirname(__file__), "results", "residual_panel.csv")
FEATURES = ("n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
            "n_fixed", "n_reachable", "invertible", "max_period")


def main():
    print("PROBE 126 (M2) — the cheap-feature ceiling on the verdict (4096 wirings)")
    print("=" * 64)
    with open(PANEL) as fh:
        rows = list(csv.DictReader(fh))
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    pred = cross_val_predict(clf, X, y, cv=5)
    cv_acc = accuracy_score(y, pred)
    clf.fit(X, y)
    full_acc = clf.score(X, y)
    imp = sorted(zip(FEATURES, clf.feature_importances_), key=lambda t: -t[1])
    print(f"  {len(y)} wirings, {int(y.sum())} triadic, {len(FEATURES)} features")
    print(f"  random-forest 5-fold CV accuracy = {cv_acc:.4f}")
    print(f"  random-forest in-sample accuracy = {full_acc:.4f}")
    print("  top feature importances:")
    for nm, v in imp[:5]:
        print(f"    {nm:<20}{v:.3f}")
    print("=" * 64)
    if cv_acc < 0.999:
        print(f"  Reading: the ceiling sits at {cv_acc:.3f}, short of perfect. No cheap feature panel — even")
        print("  with global dynamics added — defines the verdict. The residual is irreducibly holistic, a")
        print("  property of the whole cause-effect structure (confirms #13, #106).")
    else:
        print("  Reading: the panel reaches perfect accuracy; the verdict is captured by cheap features after")
        print("  all, and the top importances name what closed the residual.")
    print("=" * 64)


if __name__ == "__main__":
    main()
