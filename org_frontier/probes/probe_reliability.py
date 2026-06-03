"""Probe 27 — mediator reliability.

Is the triad robust to an unreliable system? Model the mediator's commit S' = W ∧ C realized only
with reliability r; with probability (1 − r) it lands on the wrong value (the repo's output-noise
model). Trace exact Φ over states as reliability falls.

H27: the triad is robust to moderate unreliability — Φ degrades gracefully and the verdict holds
until the mediator is near-random, where it collapses to dyadic.

Nodes: 0=W, 1=S, 2=C. S' = W∧C with reliability r; W'=S, C'=S (deterministic).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_reliability
"""

import csv
import os

import numpy as np

from .lib import max_phi_float

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
PHI_EPS = 1e-6


def build(r):
    noise = 1.0 - r
    tpm = np.zeros((8, 3))
    for s in range(8):
        w, S, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        out = float(w & c)
        tpm[s, 0] = float(S)                       # W' = S
        tpm[s, 1] = out * r + (1 - out) * noise    # S' = W∧C with reliability r
        tpm[s, 2] = float(S)                       # C' = S
    return tpm


def main():
    rows = []
    print("PROBE 27 — mediator reliability")
    print("=" * 60)
    print("  reliability r   Φ_max     verdict")
    for r in [1.0, 0.95, 0.9, 0.8, 0.7, 0.6, 0.5]:
        phi, _ = max_phi_float(build(r))
        verdict = "triadic" if phi > PHI_EPS else "dyadic"
        rows.append({"reliability": r, "phi_max": round(phi, 4), "verdict": verdict})
        print(f"   {r:.2f}           {phi:.4f}    {verdict}")
    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "reliability.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print("=" * 60)


if __name__ == "__main__":
    main()
