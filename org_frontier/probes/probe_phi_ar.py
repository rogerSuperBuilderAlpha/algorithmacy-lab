"""Probe 84 (#20) — does the Barrett–Seth Φ_AR proxy recover the verdict?

Question: the proxy bridge found Φ_R and Φ_WMS fail to recover the exact dyadic/triadic verdict. Does
the Barrett–Seth autoregressive Φ_AR (stochastic interaction across the minimum-information bipartition)
do better? Hypothesis: it does not — a Gaussian AR model of a discrete coordination form misses the same
structure the other proxies miss. Method: fit an AR(1) model to noisy trajectories of the 256-form
corpus, compute Φ_AR as the minimum over bipartitions of (sum of parts' residual entropies − whole
residual entropy), and test how well Φ_AR separates exact-triadic from exact-dyadic forms (group means
and rank-AUC).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phi_ar
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from proxy_audit import exact_phi

LABELS = ("W", "S", "C")
NOISE = 0.08
T = 20000
PER_GROUP = 24


def _gent(S):
    _, ld = np.linalg.slogdet(2 * np.pi * np.e * np.atleast_2d(S))
    return 0.5 * ld


def _resid_cov(past, fut):
    ridge = 1e-6 * np.eye(past.shape[1])
    A = np.linalg.solve(past.T @ past + ridge, past.T @ fut)
    E = fut - past @ A
    return np.cov(E, rowvar=False) + 1e-9 * np.eye(fut.shape[1])


def phi_ar(traj):
    X = traj[:-1].astype(float).copy()
    Y = traj[1:].astype(float).copy()
    X -= X.mean(0)
    Y -= Y.mean(0)
    n = traj.shape[1]
    hw = _gent(_resid_cov(X, Y))
    best = np.inf
    for mask in range(1, 2 ** (n - 1)):
        a = [i for i in range(n) if (mask >> i) & 1]
        b = [i for i in range(n) if not (mask >> i) & 1]
        if not a or not b:
            continue
        ha = _gent(_resid_cov(X[:, a], Y[:, a]))
        hb = _gent(_resid_cov(X[:, b], Y[:, b]))
        best = min(best, ha + hb - hw)
    return float(best)


def _auc(scores, labels):
    pos = [s for s, l in zip(scores, labels) if l]
    neg = [s for s, l in zip(scores, labels) if not l]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n_) + 0.5 * (p == n_) for p in pos for n_ in neg)
    return wins / (len(pos) * len(neg))


def main():
    print("PROBE 84 (#20) — Barrett–Seth Φ_AR vs the exact verdict")
    print("=" * 64)
    tri, dya = [], []
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        (tri if v.structure == "triadic" else dya).append(rules)
    rng = np.random.default_rng(7)
    sel = lambda pool: [pool[i] for i in rng.choice(len(pool), min(PER_GROUP, len(pool)), replace=False)]
    tri_s, dya_s = sel(tri), sel(dya)

    def scores(forms):
        out = []
        for r in forms:
            traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(r), NOISE), 3, T, rng)
            out.append(phi_ar(traj))
        return np.array(out)

    ts, ds = scores(tri_s), scores(dya_s)
    s = np.concatenate([ts, ds])
    y = [1] * len(ts) + [0] * len(ds)
    print(f"  groups: {len(tri_s)} triadic, {len(dya_s)} dyadic   (noise={NOISE}, T={T})")
    print(f"  Φ_AR triadic mean = {ts.mean():+.4f}   dyadic mean = {ds.mean():+.4f}")
    print(f"  rank-AUC (Φ_AR separates triadic from dyadic) = {_auc(s, y):.3f}")
    print("=" * 64)
    print("  Reading: an AUC near 0.5 means Φ_AR carries little of the exact verdict, joining Φ_R and")
    print("  Φ_WMS as proxies that miss the structural distinction. A higher AUC would say the")
    print("  autoregressive model recovers part of what the others miss.")
    print("=" * 64)


if __name__ == "__main__":
    main()
