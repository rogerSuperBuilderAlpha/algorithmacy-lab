"""Probe 34 — graded contestability.

Probe 21 found contestability collapses the triad (binary). Make it graded: the worker ignores the
determination (acts on her own prior) with probability q, else tracks it. Trace exact Φ as q rises.

H34: Φ falls smoothly with contestability q and the verdict flips to dyadic at a threshold — there is
a tolerance band of contestability the triad survives.

Nodes: 0=W, 1=S, 2=C. W' = S with prob (1−q), persists (=W) with prob q; S'=W∧C; C'=S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_graded_contestability
"""

import csv
import os

import numpy as np

from .lib import max_phi_float

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
PHI_EPS = 1e-6


def build(q):
    tpm = np.zeros((8, 3))
    for s in range(8):
        w, S, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        tpm[s, 0] = (1 - q) * S + q * w     # tracks S, or persists (ignores S) w.p. q
        tpm[s, 1] = float(w & c)
        tpm[s, 2] = float(S)
    return tpm


def main():
    rows = []
    print("PROBE 34 — graded contestability")
    print("=" * 56)
    print("  contestability q   Φ_max    verdict")
    for q in [0.0, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0]:
        phi, _ = max_phi_float(build(q))
        verdict = "triadic" if phi > PHI_EPS else "dyadic"
        rows.append({"q": q, "phi_max": round(phi, 4), "verdict": verdict})
        print(f"   {q:.2f}              {phi:.4f}   {verdict}")
    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "graded_contestability.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    flip = next((r["q"] for r in rows if r["verdict"] == "dyadic"), None)
    print("=" * 56)
    print(f"  verdict flips to dyadic at q = {flip}")
    print("=" * 56)


if __name__ == "__main__":
    main()
