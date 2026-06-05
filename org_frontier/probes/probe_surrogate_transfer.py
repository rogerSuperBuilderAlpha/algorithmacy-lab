"""Probe 99 (A1) — does the learned surrogate transfer across scale?

Question: Probe 85 recovered the verdict perfectly from cheap features at n=3. If a model trained on n=3
also predicts the verdict at n=4 and n=5 — where exact Φ is costly — the surrogate becomes a usable
instrument at scales the exact computation cannot reach. Hypothesis: size-invariant aggregate features
transfer; a random forest trained on the n=3 corpus ranks the verdict on larger forms above chance.
Method: compute fixed-length aggregate features (mean/min/max over nodes and pairs of entropy, mutual
information, transfer entropy, plus the full-joint O-information) on noisy trajectories; train on the 256
n=3 forms; test on n=4 and n=5 strict-mediation samples.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_surrogate_transfer
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
from org_frontier.multiparty.scaling import sample_form
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from ._info import entropy, mutual_information, transfer_entropy, o_information
from .probe_phi_ar import _auc

NOISE = 0.08
T = 4000


def feats(traj, n):
    ent = [entropy(traj, [i]) for i in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    mi = [mutual_information(traj, [a], [b]) for a, b in pairs]
    te = [transfer_entropy(traj, a, b) for a in range(n) for b in range(n) if a != b]
    oi = o_information(traj, list(range(n)))
    return [np.mean(ent), np.min(ent), np.max(ent),
            np.mean(mi), np.max(mi), np.mean(te), np.max(te), oi]


def dataset(forms_n, rng):
    X, y = [], []
    for n, rules in forms_n:
        labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)]) if n > 3 else ("W", "S", "C")
        v = classify_rules(rules, labels=labels)
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), n, T, rng)
        X.append(feats(traj, n))
        y.append(int(v.structure == "triadic"))
    return np.array(X), np.array(y)


def main():
    print("PROBE 99 (A1) — surrogate transfer across scale")
    print("=" * 60)
    rng = np.random.default_rng(99)
    Xtr, ytr = dataset([(3, r) for _, r in enumerate_family()], rng)
    X4, y4 = dataset([(4, sample_form(4, rng)) for _ in range(400)], rng)
    X5, y5 = dataset([(5, sample_form(5, rng)) for _ in range(400)], rng)
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    cv = cross_val_predict(clf, Xtr, ytr, cv=5, method="predict_proba")[:, 1]
    clf.fit(Xtr, ytr)
    print(f"  trained on {len(ytr)} n=3 forms ({int(ytr.sum())} triadic), 8 aggregate features")
    print(f"  in-sample (n=3) 5-fold CV-AUC = {roc_auc_score(ytr, cv):.3f}")
    for n, X, y in ((4, X4, y4), (5, X5, y5)):
        p = clf.predict_proba(X)[:, 1]
        auc = _auc(p, y) if 0 < y.sum() < len(y) else float("nan")
        print(f"  transfer to n={n}: {len(y)} forms, {int(y.sum())} triadic, AUC = {auc:.3f}")
    print("=" * 60)
    print("  Reading: a transfer AUC well above 0.5 says a model trained on the cheap n=3 forms ranks the")
    print("  verdict on larger forms, so the surrogate is usable where exact Φ is too costly to run.")
    print("=" * 60)


if __name__ == "__main__":
    main()
