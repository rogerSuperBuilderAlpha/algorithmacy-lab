"""Probe 100 (A2) — what is the minimal feature set that recovers the verdict?

Question: Probe 85 reached AUC 1.0 with thirteen cheap features. How few features carry that? A minimal
set is more interpretable and cheaper to estimate on real logs. Hypothesis: two or three features suffice.
Method: over the 256-form corpus, compute the same thirteen features; rank each by single-feature AUC,
then greedily add features to a random forest until 5-fold CV-AUC reaches ≈ 1.0.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_minimal_features
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_auc_score

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from ._info import entropy, mutual_information, transfer_entropy, o_information
from .probe_phi_ar import _auc

NOISE = 0.08
T = 8000
NAMES = (["H[W]", "H[S]", "H[C]"]
         + ["MI[W;S]", "MI[W;C]", "MI[S;C]"]
         + [f"TE[{a}->{b}]" for a in "WSC" for b in "WSC" if a != b]
         + ["O_info"])


def features(traj):
    f = [entropy(traj, [i]) for i in range(3)]
    f += [mutual_information(traj, [a], [b]) for a, b in [(0, 1), (0, 2), (1, 2)]]
    f += [transfer_entropy(traj, a, b) for a in range(3) for b in range(3) if a != b]
    f.append(o_information(traj, [0, 1, 2]))
    return f


def main():
    print("PROBE 100 (A2) — minimal feature set for the verdict")
    print("=" * 60)
    rng = np.random.default_rng(100)
    X, y = [], []
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=("W", "S", "C"))
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), 3, T, rng)
        X.append(features(traj))
        y.append(int(v.structure == "triadic"))
    X = np.array(X)
    y = np.array(y)
    singles = sorted(((NAMES[j], _auc(X[:, j], y)) for j in range(X.shape[1])),
                     key=lambda t: -abs(t[1] - 0.5))
    print("  single-feature rank-AUC (top 6):")
    for nm, a in singles[:6]:
        print(f"    {nm:<12}{a:.3f}")
    # greedy forward selection on CV-AUC
    clf = RandomForestClassifier(n_estimators=300, random_state=0, n_jobs=-1)
    chosen, remaining = [], list(range(X.shape[1]))
    print("  greedy forward selection (CV-AUC):")
    while remaining:
        best = None
        for j in remaining:
            cols = chosen + [j]
            p = cross_val_predict(clf, X[:, cols], y, cv=5, method="predict_proba")[:, 1]
            auc = roc_auc_score(y, p)
            if best is None or auc > best[1]:
                best = (j, auc)
        chosen.append(best[0])
        remaining.remove(best[0])
        print(f"    + {NAMES[best[0]]:<12} -> CV-AUC {best[1]:.4f}  ({len(chosen)} features)")
        if best[1] >= 0.999 or len(chosen) >= 5:
            break
    print("=" * 60)
    print(f"  minimal set: {[NAMES[j] for j in chosen]}")
    print("  Reading: if a two- or three-feature model reaches AUC near 1.0, the verdict's cheap")
    print("  fingerprint is small and nameable, not a property of the whole thirteen-feature panel.")
    print("=" * 60)


if __name__ == "__main__":
    main()
