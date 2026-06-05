"""Probe 134 (R2) — is there a coupling feature that separates the verdict across topologies?

Question: mean pairwise MI ranks the verdict within a family (#122) but the surrogate built on it fails
across topology (#129) — high-Φ pools get called dyadic. Why, and does a normalized coupling feature do
better across topologies? Hypothesis: all-to-all pools spread their coupling thin, so raw mean pairwise MI
is low there despite high Φ; a feature normalized by system spread (total correlation per node) separates
the verdict across topologies where raw MI does not. Method: over the archetype families, compute raw mean
pairwise MI, total correlation per node, and O-information on noisy trajectories; report each feature's
cross-topology AUC against the verdict and the pools' raw-MI value.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_invariant_feature
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from .probe_ood_surrogate import ood_forms
from ._info import entropy, mutual_information, o_information
from .probe_phi_ar import _auc

NOISE = 0.08
T = 6000


def coupling_features(traj, n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    mean_mi = float(np.mean([mutual_information(traj, [a], [b]) for a, b in pairs]))
    tc = sum(entropy(traj, [i]) for i in range(n)) - entropy(traj, list(range(n)))
    tc_per_node = float(tc) / n
    oi = o_information(traj, list(range(n)))
    return mean_mi, tc_per_node, oi


def main():
    print("PROBE 134 (R2) — a cross-topology coupling feature")
    print("=" * 64)
    rng = np.random.default_rng(134)
    mi, tc, oi, y, pool_mi = [], [], [], [], []
    for name, rules, n in ood_forms():
        labels = tuple(f"x{i}" for i in range(n))
        traj = exact_phi.simulate_trajectory(add_noise(tpm_from_rules(rules), NOISE), n, T, rng)
        m, t, o = coupling_features(traj, n)
        mi.append(m)
        tc.append(t)
        oi.append(o)
        y.append(int(classify_rules(rules, labels=labels).structure == "triadic"))
        if name.startswith("pool"):
            pool_mi.append(m)
    mi, tc, oi, y = np.array(mi), np.array(tc), np.array(oi), np.array(y)
    print(f"  {len(y)} archetype forms ({int(y.sum())} triadic) across topologies")
    print(f"  mean pairwise MI of pools (triadic, high-Φ): {np.mean(pool_mi):.4f}")
    print(f"  mean pairwise MI of all triadic: {mi[y==1].mean():.4f}; of dyadic: {mi[y==0].mean():.4f}")
    print(f"  {'feature':<26}{'cross-topology AUC'}")
    print(f"  {'raw mean pairwise MI':<26}{_auc(mi, y):.3f}")
    print(f"  {'total correlation / node':<26}{_auc(tc, y):.3f}")
    print(f"  {'O-information':<26}{_auc(np.abs(oi), y):.3f}")
    print("=" * 64)
    best = max([("raw mean MI", _auc(mi, y)), ("TC/node", _auc(tc, y)), ("|O-info|", _auc(np.abs(oi), y))],
               key=lambda z: z[1])
    print(f"  best cross-topology feature: {best[0]} (AUC {best[1]:.3f})")
    print("  Reading: if pools carry low raw MI while a normalized feature still ranks them triadic, the")
    print("  cross-topology failure is a normalization problem and the normalized coupling is the fix. If")
    print("  no feature separates the families, the verdict has no topology-invariant cheap proxy.")
    print("=" * 64)


if __name__ == "__main__":
    main()
