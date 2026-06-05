"""Probe 87 (#23) — does the redundancy function or the noise level change ΦID separation?

Question: Φ_R uses the CCS redundancy at a fixed noise. Would a different redundancy lattice (MMI) or a
different noise level make ΦID separate the verdict? Hypothesis: no — neither choice turns ΦID into a
verdict recoverer; the separation stays small across MMI/CCS and across noise. Method: across a sample of
triadic and dyadic corpus forms, compute the minimum-over-bipartitions Φ_R with both the MMI and CCS
redundancy lattices, at two noise levels, and report the triadic−dyadic group separation in each cell.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phiid_sweep
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
from foundations.proxy_audit import exact_phi
from foundations.phiid_vs_phi.phiid_measure import _bipartitions, _part_int_series, phi_r_bipartition

LABELS = ("W", "S", "C")
PER_GROUP = 8
T = 8000


def phi_r_min(tpm, rng, redundancy):
    traj = exact_phi.simulate_trajectory(tpm, 3, T, rng)
    best = np.inf
    for a, b in _bipartitions(3):
        A = _part_int_series(traj, a)
        B = _part_int_series(traj, b)
        best = min(best, phi_r_bipartition(A, B, redundancy=redundancy))
    return best if np.isfinite(best) else 0.0


def main():
    print("PROBE 87 (#23) — ΦID separation across redundancy lattice (MMI/CCS) and noise")
    print("=" * 72)
    tri, dya = [], []
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        (tri if v.structure == "triadic" else dya).append(rules)
    rng = np.random.default_rng(13)
    sel = lambda p: [p[i] for i in rng.choice(len(p), min(PER_GROUP, len(p)), replace=False)]
    tri_s, dya_s = sel(tri), sel(dya)
    print(f"  {len(tri_s)} triadic, {len(dya_s)} dyadic forms")
    print(f"  {'redundancy':<12}{'noise':<8}{'triadic':<12}{'dyadic':<12}{'|gap|'}")
    for red in ("CCS", "MMI"):
        for noise in (0.05, 0.15):
            def mean_phi(forms):
                return np.mean([phi_r_min(add_noise(tpm_from_rules(r), noise), rng, red) for r in forms])
            tm, dm = mean_phi(tri_s), mean_phi(dya_s)
            print(f"  {red:<12}{noise:<8}{tm:<12.4f}{dm:<12.4f}{abs(tm-dm):.4f}")
    print("=" * 72)
    print("  Reading: if no cell opens a large gap, neither the redundancy lattice nor the noise level")
    print("  is the reason ΦID misses the verdict — the limitation is the measure, not the settings.")
    print("=" * 72)


if __name__ == "__main__":
    main()
