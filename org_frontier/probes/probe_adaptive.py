"""Probe 79 (#17) — an adaptive mediator's verdict trajectory.

Question: does a mediator that adapts over time trace a different verdict path than a fixed one?
Hypothesis: a mediator that learns to weight a party less drifts the form from triadic toward dyadic.
Method: model the mediator's reliance on the counterpart degrading over epochs (the system perceives
C with reliability r_e falling from 1 to 0, a stand-in for a learning drift), and read exact Φ at each
epoch.

Nodes: 0=W, 1=S, 2=C. S' = W ∧ (C perceived at reliability r_e); W'=S; C'=S.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_adaptive
"""

import numpy as np

from .lib import max_phi_float

PHI_EPS = 1e-6


def build(rc):
    tpm = np.zeros((8, 3))
    for s in range(8):
        w, S, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        c_perceived = rc * c + (1 - rc) * 0.5
        tpm[s, 0] = float(S)
        tpm[s, 1] = w * c_perceived
        tpm[s, 2] = float(S)
    return tpm


def main():
    print("PROBE 79 (#17) — adaptive mediator (drift in reliance on the counterpart)")
    print("=" * 64)
    print("  epoch  r_counterpart   Φ        verdict")
    for e, rc in enumerate([1.0, 0.75, 0.5, 0.25, 0.0]):
        phi, _ = max_phi_float(build(rc))
        verdict = "triadic" if phi > PHI_EPS else "dyadic"
        print(f"   {e}      {rc:.2f}            {phi:.4f}   {verdict}")
    print("=" * 64)
    print("  Reading: an adaptive mediator that learns to weight a party less traces a verdict path")
    print("  from triadic to dyadic — the form's kind is not fixed but moves as the mediator adapts.")
    print("=" * 64)


if __name__ == "__main__":
    main()
