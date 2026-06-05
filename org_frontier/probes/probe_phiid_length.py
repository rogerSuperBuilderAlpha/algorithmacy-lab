"""Probe 86 (#22) — does a longer trajectory recover the verdict Φ_R misses?

Question: Φ_R estimated from a finite trajectory failed to recover the exact verdict. Is that a
finite-sample problem that more data fixes? Hypothesis: no — Φ_R converges to a value that still does
not separate the groups, so length does not rescue it. Method: across a sample of triadic and dyadic
corpus forms, estimate Φ_R from trajectories of increasing length and track the triadic−dyadic group
separation as length grows.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phiid_length
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
from foundations.phiid_vs_phi.phiid_measure import phi_r_integration

LABELS = ("W", "S", "C")
NOISE = 0.08
PER_GROUP = 10
LENGTHS = (1000, 4000, 16000, 64000)


def main():
    print("PROBE 86 (#22) — Φ_R group separation vs trajectory length")
    print("=" * 60)
    tri, dya = [], []
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        (tri if v.structure == "triadic" else dya).append(rules)
    rng = np.random.default_rng(9)
    sel = lambda p: [p[i] for i in rng.choice(len(p), min(PER_GROUP, len(p)), replace=False)]
    tri_s, dya_s = sel(tri), sel(dya)
    print(f"  {len(tri_s)} triadic, {len(dya_s)} dyadic forms (noise={NOISE})")
    print(f"  {'length':<10}{'triadic Φ_R':<14}{'dyadic Φ_R':<14}{'|gap|'}")
    for T in LENGTHS:
        def mean_phi(forms):
            return np.mean([phi_r_integration(add_noise(tpm_from_rules(r), NOISE), 3, rng, traj_len=T)[0]
                            for r in forms])
        tm, dm = mean_phi(tri_s), mean_phi(dya_s)
        print(f"  {T:<10}{tm:<14.4f}{dm:<14.4f}{abs(tm-dm):.4f}")
    print("=" * 60)
    print("  Reading: if the gap does not grow toward the exact verdict's gap as length increases, the")
    print("  proxy's failure is structural, not a finite-sample artifact — more data does not recover it.")
    print("=" * 60)


if __name__ == "__main__":
    main()
