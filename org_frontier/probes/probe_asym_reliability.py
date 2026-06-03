"""Probe 38 — asymmetric reliability (the system perceives one party better than the other).

Probe 27 degraded the determination's overall reliability. Here the asymmetry is which party the
system reads reliably: it reads the worker cleanly but perceives the counterpart with reliability
r_c (else as noise). Trace exact Φ as the system's perception of the counterpart degrades.

H38: as the system's read of the counterpart degrades, the determination drifts toward depending on
the worker alone — the counterpart effectively drops, Φ falls, and the form heads to dyadic.

Nodes: 0=W, 1=S, 2=C. S' = W ∧ (C perceived at reliability r_c); W'=S; C'=S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_asym_reliability
"""

import csv
import os

import numpy as np

from .lib import max_phi_float

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
PHI_EPS = 1e-6


def build(rc):
    """S sees C as C with prob rc, else as a coin flip (0.5)."""
    tpm = np.zeros((8, 3))
    for s in range(8):
        w, S, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        c_perceived = rc * c + (1 - rc) * 0.5
        tpm[s, 0] = float(S)
        tpm[s, 1] = w * c_perceived           # S = W AND (perceived C)
        tpm[s, 2] = float(S)
    return tpm


def main():
    rows = []
    print("PROBE 38 — asymmetric reliability (system's read of the counterpart)")
    print("=" * 64)
    print("  r_c (counterpart read)   Φ_max    verdict")
    for rc in [1.0, 0.9, 0.75, 0.5, 0.25, 0.0]:
        phi, _ = max_phi_float(build(rc))
        verdict = "triadic" if phi > PHI_EPS else "dyadic"
        rows.append({"r_counterpart": rc, "phi_max": round(phi, 4), "verdict": verdict})
        print(f"   {rc:.2f}                    {phi:.4f}   {verdict}")
    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "asym_reliability.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("=" * 64)


if __name__ == "__main__":
    main()
