"""Probe 85 (#21) — can a feature-combining model recover the binary verdict?

Question: single cheap proxies (Φ_R, Φ_WMS, Φ_AR, O-information) each miss the exact verdict. Does a
model that combines many cheap time-series features recover it? Hypothesis: a random forest over a panel
of features (per-node entropy, pairwise mutual information, transfer entropy, O-information) recovers the
dyadic/triadic verdict well above chance — the verdict is implicit in the joint statistics even though no
single proxy captures it. Method: build a feature panel from noisy trajectories of the 256-form corpus,
label each by the exact verdict, and report 5-fold cross-validated accuracy and ROC-AUC for a random
forest, against the majority-class baseline.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_learned_surrogate
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
from sklearn.metrics import accuracy_score, roc_auc_score

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from proxy_audit import exact_phi
from ._info import entropy, mutual_information, transfer_entropy, o_information

LABELS = ("W", "S", "C")
NOISE = 0.08
T = 8000


def features(traj):
    f = [entropy(traj, [i]) for i in range(3)]
    pairs = [(0, 1), (0, 2), (1, 2)]
    f += [mutual_information(traj, [a], [b]) for a, b in pairs]
    f += [transfer_entropy(traj, a, b) for a in range(3) for b in range(3) if a != b]
    f.append(o_information(traj, [0, 1, 2]))
    return f


def main():
    print("PROBE 85 (#21) — random-forest surrogate over cheap features vs the exact verdict")
    print("=" * 78)
    rng = np.random.default_rng(3)
    X, y = [], []
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), 3, T, rng)
        X.append(features(traj))
        y.append(1 if v.structure == "triadic" else 0)
    X = np.array(X)
    y = np.array(y)
    base = max(y.mean(), 1 - y.mean())
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    print(f"  {len(y)} forms ({int(y.sum())} triadic, {int((1-y).sum()) if y.sum()==0 else len(y)-int(y.sum())} dyadic), {X.shape[1]} features, 5-fold CV")
    print(f"  majority-class baseline accuracy = {base:.3f}")
    print(f"  random-forest CV accuracy        = {accuracy_score(y, pred):.3f}")
    print(f"  random-forest CV ROC-AUC         = {roc_auc_score(y, proba):.3f}")
    print("=" * 78)
    print("  Reading: an AUC well above 0.5 and accuracy above the baseline say the verdict is")
    print("  recoverable from a combination of cheap features, even though no single proxy recovers")
    print("  it — the structural distinction leaves a statistical fingerprint a learner can read.")
    print("=" * 78)


if __name__ == "__main__":
    main()
