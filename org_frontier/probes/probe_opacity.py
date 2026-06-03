"""Probe 24 — opaque mediation as a gradient.

Scope condition: opaque mediation. Earlier probes flipped the direct worker–counterpart channel on
and off (binary). This makes it a gradient: the worker observes the counterpart directly with
probability p (transparency), otherwise only through the system. p = 0 is fully opaque (the triad);
p = 1 is full transparency. Stochastic TPM, exact Φ over all states.

H24: Φ falls as transparency p rises, and the verdict flips from triadic to dyadic at a threshold —
opacity is necessary, and partial opacity may still sustain the triad.

Nodes: 0=W, 1=S, 2=C. W' blends S (opaque) and C (transparent); S'=W∧C; C'=S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_opacity
"""

import csv
import os

import numpy as np

from .lib import max_phi_float

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
PHI_EPS = 1e-6


def build(p):
    tpm = np.zeros((8, 3))
    for s in range(8):
        w, S, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        tpm[s, 0] = (1 - p) * S + p * c     # W' = S (opaque) blended with C (transparent)
        tpm[s, 1] = float(w & c)            # S' = W AND C
        tpm[s, 2] = float(S)                # C' = S
    return tpm


def main():
    rows = []
    print("PROBE 24 — opaque mediation as a gradient")
    print("=" * 64)
    print("  transparency p   Φ_max     verdict")
    for p in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
        phi, _ = max_phi_float(build(p))
        verdict = "triadic" if phi > PHI_EPS else "dyadic"
        rows.append({"transparency": p, "phi_max": round(phi, 4), "verdict": verdict})
        print(f"   {p:.2f}            {phi:.4f}    {verdict}")
    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "opacity.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    flip = next((r["transparency"] for r in rows if r["verdict"] == "dyadic"), None)
    print("=" * 64)
    print(f"  verdict flips to dyadic at transparency p = {flip}")
    print("=" * 64)


if __name__ == "__main__":
    main()
