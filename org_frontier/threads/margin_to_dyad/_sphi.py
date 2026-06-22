"""Exact Φ on stochastic coordination TPMs, for the distance-to-dyad margin dive.

The margin dive turns the binary commit/convey verdict into a continuous quantity by making the
mediator's determination probabilistic. A commit probability p (the gate fires its determination with
probability p, else outputs a coin flip) and a read fidelity q (a party copies the mediator with
probability q, else a coin flip) are two continuous knobs on how far a mediated triad sits from
factoring. `sphi` returns the maximum big-Φ over states of a stochastic state-by-node TPM.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

AND = lambda *v: float(all(v))
OR = lambda *v: float(any(v))
XOR = lambda W, C: float(W ^ C)


def sphi(T, labels=("W", "S", "C")):
    """Max big-Φ over all states of a stochastic state-by-node TPM."""
    n = len(labels)
    net = pyphi.Network(T, node_labels=labels)
    best = 0.0
    for s in range(2 ** n):
        st = tuple((s >> i) & 1 for i in range(n))
        try:
            best = max(best, float(new_big_phi.sia(pyphi.Subsystem(net, st)).phi))
        except Exception:
            pass
    return round(best, 4)


def triad(p=1.0, qW=1.0, qC=1.0, gate=AND):
    """Three-node commit triad: S commits gate(W,C) w.p. p; W,C read S w.p. qW,qC (else a coin flip)."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = qW * S + (1 - qW) * 0.5
        T[s, 2] = qC * S + (1 - qC) * 0.5
        T[s, 1] = p * gate(W, C) + (1 - p) * 0.5
    return T


def quad_allrequired(p=1.0, q=1.0):
    """Four-node all-required commit: S = W&C&D w.p. p; the three parties read S w.p. q."""
    T = np.zeros((16, 4))
    for s in range(16):
        W, S, C, D = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
        T[s, 0] = q * S + (1 - q) * 0.5
        T[s, 2] = q * S + (1 - q) * 0.5
        T[s, 3] = q * S + (1 - q) * 0.5
        T[s, 1] = p * float(W & C & D) + (1 - p) * 0.5
    return T
