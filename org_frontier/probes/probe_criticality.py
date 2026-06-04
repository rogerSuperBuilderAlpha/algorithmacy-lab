"""Probe 81 (#19) — is there a coordination form whose Φ peaks at intermediate coupling?

Question: earlier sweeps (Probes 27, 38) found Φ monotone in reliability. Is there an axis on which Φ
peaks at an interior point, the way order parameters peak near a critical regime? Hypothesis: as the
parties' tracking shifts from anti-phase through random to in-phase, Φ peaks where tracking is coherent
and falls off on both sides. Method: a three-node form with S' = W∧C fixed; the parties track S with
phase parameter p (P(track correct) = p, so p=1 in-phase, p=0.5 random, p=0 anti-phase). Sweep p and
read exact Φ, looking for an interior maximum.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_criticality
"""

import numpy as np

from .lib import max_phi_float


def build(p):
    tpm = np.zeros((8, 3))
    for s in range(8):
        w, S, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        # parties track S with phase p: P(track=1) = p if S==1 else (1-p)
        tpm[s, 0] = p if S == 1 else (1 - p)
        tpm[s, 1] = float(w & c)
        tpm[s, 2] = p if S == 1 else (1 - p)
    return tpm


def main():
    print("PROBE 81 (#19) — criticality: Φ across the tracking-phase axis")
    print("=" * 60)
    print(f"  {'p (tracking phase)':<22}{'Φ'}")
    curve = []
    for p in [0.0, 0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1.0]:
        phi, _ = max_phi_float(build(p))
        curve.append((p, phi))
        print(f"  {p:<22.2f}{phi:.4f}")
    print("=" * 60)
    ps = [c[0] for c in curve]
    phis = [c[1] for c in curve]
    imax = int(np.argmax(phis))
    interior = 0 < imax < len(phis) - 1
    print(f"  peak at p={ps[imax]:.2f} (Φ={phis[imax]:.4f}); interior peak: {interior}")
    if interior:
        print("  Reading: Φ peaks at an intermediate tracking phase and falls on both sides — a")
        print("  coordination form can have a critical coupling where integration is maximal.")
    else:
        print("  Reading: Φ is symmetric in phase, maximal at both deterministic extremes (in-phase and")
        print("  anti-phase) and zero at random tracking (p=0.5). It tracks coupling determinism, not")
        print("  phase sign. The interior point is a trough, not a peak — no critical Φ maximum here.")
    print("=" * 60)


if __name__ == "__main__":
    main()
