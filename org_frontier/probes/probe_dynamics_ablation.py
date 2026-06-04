"""Probe 127 (M3) — do global dynamics features help beyond connectivity and synergy?

Question: per-function synergy did not lift accuracy beyond connectivity (#106). Do global-dynamics
features (fixed points, reachability, invertibility, attractor period) help where synergy did not?
Hypothesis: they do not — the residual is not a coarse-dynamics property either. Method: from the cached
panel, fit a decision tree on three nested feature sets — connectivity, connectivity+synergy,
connectivity+synergy+dynamics — and compare accuracy at each step.

Reads: org_frontier/probes/results/residual_panel.csv (run Probe 125 first).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_dynamics_ablation
"""

import csv
import os

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score

PANEL = os.path.join(os.path.dirname(__file__), "results", "residual_panel.csv")
CONN = ["n_edges", "n_bidir", "strongly_connected"]
SYN = ["syn_sum", "syn_min", "syn_max"]
DYN = ["n_fixed", "n_reachable", "invertible", "max_period"]


def main():
    print("PROBE 127 (M3) — ablation: connectivity, + synergy, + global dynamics")
    print("=" * 64)
    with open(PANEL) as fh:
        rows = list(csv.DictReader(fh))
    y = np.array([int(r["triadic"]) for r in rows])

    def acc(cols):
        X = np.array([[float(r[c] if not isinstance(r[c], float) else r[c]) for c in cols] for r in rows])
        clf = DecisionTreeClassifier(max_depth=6, random_state=0)
        pred = cross_val_predict(clf, X, y, cv=5)
        return accuracy_score(y, pred)

    a_conn = acc(CONN)
    a_syn = acc(CONN + SYN)
    a_dyn = acc(CONN + SYN + DYN)
    print(f"  {len(y)} wirings, {int(y.sum())} triadic (5-fold CV decision tree)")
    print(f"  connectivity only              = {a_conn:.4f}")
    print(f"  connectivity + synergy         = {a_syn:.4f}")
    print(f"  connectivity + synergy + dynamics = {a_dyn:.4f}")
    print("=" * 64)
    lift_syn = a_syn - a_conn
    lift_dyn = a_dyn - a_syn
    print(f"  synergy lift = {lift_syn:+.4f}; dynamics lift = {lift_dyn:+.4f}")
    if lift_dyn < 0.01:
        print("  Reading: global dynamics adds essentially nothing beyond connectivity and synergy. The")
        print("  residual is not a coarse-dynamics property; it sits in the full cause-effect structure")
        print("  that none of these summaries reach.")
    else:
        print("  Reading: global dynamics lifts the accuracy, so attractor structure carries part of the")
        print("  residual the graph and the function tables miss.")
    print("=" * 64)


if __name__ == "__main__":
    main()
