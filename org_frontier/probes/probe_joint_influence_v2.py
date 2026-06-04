"""Probe 92 (#1) — does a synergy (joint-influence) term lift the family AUC?

Question: Probe 12 predicted core membership on the full 3-node family from each node's marginal
influence (AUC ~0.70). Probe 13's context-sensitive total-influence did not close the gap to the
controlled 0.89. Does an explicit pairwise/synergy term — how much a node's effect on another depends on
a co-input — lift the prediction? Hypothesis: yes; some core members earn their place through
interaction effects a marginal-sensitivity feature misses, so a model with the synergy term ranks core
membership better than marginal influence alone. Method: sample arbitrary 3-node wirings; for each node
compute marginal out-influence and a joint-influence (interaction) term; among bidirectionally coupled
nodes, compare rank-AUC of marginal influence alone to the cross-validated AUC of a two-feature logistic
model for in-core.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_joint_influence_v2 [N] [seed]
"""

import sys

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_auc_score

from .lib import major_complex
from .probe_phi_ar import _auc

LABELS = ("A", "B", "C")


def _f(table):
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def _sens(table, bit):
    return sum(table[c] != table[c ^ (1 << bit)] for c in range(4)) / 4.0


def _interaction(table, pos):
    """Interaction sensitivity of input `pos`: how its marginal effect changes with the co-input."""
    if pos == 0:
        s0 = float(table[0] != table[1])   # co (bit1) = 0
        s1 = float(table[2] != table[3])   # co = 1
    else:
        s0 = float(table[0] != table[2])   # co (bit0) = 0
        s1 = float(table[1] != table[3])   # co = 1
    return abs(s0 - s1)


def main(N=1500, seed=11):
    rng = np.random.default_rng(seed)
    feats, marg, y = [], [], []
    for _ in range(N):
        t = [tuple(int(b) for b in rng.integers(0, 2, 4)) for _ in range(3)]
        f0, f1, f2 = _f(t[0]), _f(t[1]), _f(t[2])
        rules = [lambda x: f0(x[1], x[2]), lambda x: f1(x[0], x[2]), lambda x: f2(x[0], x[1])]
        core, _ = major_complex(rules, LABELS)
        core = core or ()
        out_infl = {"A": np.mean([_sens(t[1], 0), _sens(t[2], 0)]),
                    "B": np.mean([_sens(t[0], 0), _sens(t[2], 1)]),
                    "C": np.mean([_sens(t[0], 1), _sens(t[1], 1)])}
        joint = {"A": np.mean([_interaction(t[1], 0), _interaction(t[2], 0)]),
                 "B": np.mean([_interaction(t[0], 0), _interaction(t[2], 1)]),
                 "C": np.mean([_interaction(t[0], 1), _interaction(t[1], 1)])}
        reads = {"A": any(_sens(t[0], b) for b in (0, 1)),
                 "B": any(_sens(t[1], b) for b in (0, 1)),
                 "C": any(_sens(t[2], b) for b in (0, 1))}
        for X in ("A", "B", "C"):
            if not (reads[X] and out_infl[X] > 0):     # bidirectional only
                continue
            feats.append([out_infl[X], joint[X]])
            marg.append(out_infl[X])
            y.append(int(X in core))
    feats = np.array(feats)
    y = np.array(y)
    auc_marg = _auc(marg, y)
    clf = LogisticRegression(max_iter=1000)
    p1 = cross_val_predict(clf, feats[:, :1], y, cv=5, method="predict_proba")[:, 1]
    p2 = cross_val_predict(clf, feats, y, cv=5, method="predict_proba")[:, 1]
    print("PROBE 92 (#1) — joint-influence (synergy) term and the family AUC")
    print("=" * 64)
    print(f"  {len(y)} bidirectional node-observations, {int(y.sum())} in core")
    print(f"  rank-AUC, marginal influence alone        = {auc_marg:.3f}")
    print(f"  CV-AUC, logistic on marginal alone        = {roc_auc_score(y, p1):.3f}")
    print(f"  CV-AUC, logistic on marginal + synergy    = {roc_auc_score(y, p2):.3f}")
    print("=" * 64)
    lift = roc_auc_score(y, p2) - roc_auc_score(y, p1)
    print(f"  synergy lift = {lift:+.3f}")
    print("  Reading: a positive lift says some core members earn their place through interaction")
    print("  effects, not marginal influence alone — the joint-influence term carries signal the")
    print("  per-node sensitivity misses. A near-zero lift says marginal influence already suffices.")
    print("=" * 64)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    main(N, seed)
