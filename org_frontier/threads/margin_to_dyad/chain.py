"""The twenty-step deep dive on Q4: distance to the dyad, the Φ margin.

Q4 from the mediation_boundary thread's QUESTIONS.md. The binary commit/convey verdict becomes a
continuous quantity by making the mediator's determination probabilistic: a commit probability p (the
gate fires its determination with probability p, else a coin flip) and a read fidelity q (a party copies
the mediator with probability q, else a coin flip) are two knobs on how far a mediated triad sits from
factoring. Each step's question is drawn from the previous step's result; the narrative is in
DEEP_DIVE.md, and every number reproduces here.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/threads/margin_to_dyad/chain.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from org_frontier.threads.margin_to_dyad._sphi import sphi, triad, quad_allrequired, AND, XOR, OR

L4 = ("W", "S", "C", "D")


def backchannel(b):
    """Strict mediation with a symmetric W<->C back-channel of strength b (b=0 strict)."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = (1 - b) * S + b * C
        T[s, 2] = (1 - b) * S + b * W
        T[s, 1] = float(W & C)
    return T


def substit(r):
    """n=4, interpolate all-required (r=0) toward substitutable (r=1)."""
    T = np.zeros((16, 4))
    for s in range(16):
        W, S, C, D = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
        for k in (0, 2, 3):
            T[s, k] = S
        T[s, 1] = (1 - r) * float(W & C & D) + r * float(W & (C | D))
    return T


def veto(p):
    """A mixed/veto gate S = W AND NOT C, committed with probability p."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = S
        T[s, 2] = S
        T[s, 1] = p * float(W & (1 - C)) + (1 - p) * 0.5
    return T


def globaltemp(t):
    """Noise of magnitude t on every node, not only the commit."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = (1 - t) * S + t * 0.5
        T[s, 2] = (1 - t) * S + t * 0.5
        T[s, 1] = (1 - t) * float(W & C) + t * 0.5
    return T


def half_knob(fn, full):
    """Knob value (1.0 = intact) at which Φ falls to half the full margin."""
    lo, hi = 0.0, 1.0
    for _ in range(18):
        m = (lo + hi) / 2
        if fn(m) > full / 2:
            hi = m
        else:
            lo = m
    return round((lo + hi) / 2, 3)


def run():
    print("STEP 1-4 the margin curve Φ(p): convex, no threshold, between linear and quadratic")
    for p in (1.0, 0.75, 0.5, 0.25, 0.1, 0.02):
        print(f"  p={p:<5} Φ={sphi(triad(p=p))}   (2p={2*p:.2f}, 2p^2={2*p*p:.2f})")
    print("STEP 3 gate type near the boundary (parity vanishes proportionally):")
    for p in (1.0, 0.5, 0.1):
        print(f"  p={p}: AND Φ={sphi(triad(p=p, gate=AND))}  XOR Φ={sphi(triad(p=p, gate=XOR))}  OR Φ={sphi(triad(p=p, gate=OR))}")

    print("\nSTEP 5-6 read fidelity q, and the non-separable two-knob surface:")
    print("        q=1.0   q=0.75  q=0.5")
    for p in (1.0, 0.75, 0.5):
        print(f"  p={p}: " + "  ".join(f"{sphi(triad(p=p, qW=q, qC=q)):.3f}" for q in (1.0, 0.75, 0.5)))

    print("\nSTEP 7-8 weakest-link liveness and the steeper n=4 decay:")
    print(f"  asymmetric (qW=1, qC=0.5): Φ={sphi(triad(p=1, qW=1, qC=0.5))}; one party decoupled (qC=0): Φ={sphi(triad(p=1, qW=1, qC=0.0))}")
    for p in (1.0, 0.75, 0.5):
        print(f"  n=4 all-required p={p}: Φ={sphi(quad_allrequired(p=p), labels=L4)}")

    print("\nSTEP 9-11 the perturbation knobs: back-channel (resilient), substitutability (brittle), commit vs read:")
    print("  back-channel b: " + ", ".join(f"{b}->{sphi(backchannel(b))}" for b in (0.1, 0.25, 0.5, 0.75)))
    print("  substitutability r: " + ", ".join(f"{r}->{sphi(substit(r), labels=L4)}" for r in (0.1, 0.25, 0.5)))
    print(f"  commit-noise Φ(p=.5)={sphi(triad(p=0.5))} vs read-noise Φ(q=.5)={sphi(triad(p=1, qW=0.5, qC=0.5))}")

    print("\nSTEP 12 the fragility ranking (half-margin knob value; smaller intact-range = more brittle):")
    print(f"  back-channel  half at strength {round(1-half_knob(lambda b: sphi(backchannel(1-b)), 2.0),3)} (most resilient)")
    print(f"  read fidelity half at q={half_knob(lambda q: sphi(triad(p=1, qW=q, qC=q)), 2.0)}")
    print(f"  commit prob   half at p={half_knob(lambda p: sphi(triad(p=p)), 2.0)}")
    print(f"  substitutability half at r={round(1-half_knob(lambda x: sphi(substit(1-x), labels=L4), 3.0),3)} (most brittle)")

    print("\nSTEP 13-15 the veto stays zero; global ~ targeted; the commit component dominates:")
    print(f"  veto W&(not C): " + ", ".join(f"p={p}->{sphi(veto(p))}" for p in (1.0, 0.75, 0.5)))
    for t in (0.25, 0.5):
        print(f"  noise {t}: global Φ={sphi(globaltemp(t))} vs targeted commit Φ={sphi(triad(p=1-t))}")


if __name__ == "__main__":
    run()
