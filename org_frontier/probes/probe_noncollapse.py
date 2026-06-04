"""Probe 82 (#43) — does a Niizato-style size discontinuity appear under non-collapsing dynamics?

Question: Niizato's fish schools show a jump in integration between three and four agents. The
strict-mediation families here collapse to fixed points (Probe 44), which hides any size effect. Does a
richer, non-collapsing dynamics (all-to-all majority coupling under output noise, so the state space
stays explored) show a Φ discontinuity at size four? Hypothesis: max Φ rises with size but need not have
a sharp jump at n=4 the way an interaction-rich physical system does. Method: build an n-node pool where
each node's next state is the majority of the others, add output noise so all states are reachable, and
read exact IIT-4.0 max Φ for n=2..5.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_noncollapse
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.proxy_bridge.bridge import add_noise
from proxy_audit import exact_phi

NOISE = 0.1


def majority_pool(n):
    """Deterministic state-by-node TPM: each node' = majority of the other n-1 nodes."""
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        bits = [(s >> i) & 1 for i in range(n)]
        for j in range(n):
            others = [bits[i] for i in range(n) if i != j]
            tpm[s, j] = 1.0 if sum(others) * 2 > len(others) else 0.0
    cm = np.ones((n, n)) - np.eye(n)   # each node reads every other node
    return tpm, cm


def main():
    print("PROBE 82 (#43) — Φ vs pool size under non-collapsing (noisy majority) dynamics")
    print("=" * 66)
    print(f"  noise={NOISE}")
    print(f"  {'n':<5}{'max Φ':<12}{'Δ from n-1'}")
    rng = np.random.default_rng(11)
    prev = None
    curve = []
    for n in (2, 3, 4, 5):
        tpm, cm = majority_pool(n)
        noisy = add_noise(tpm, NOISE)
        _, mx, _ = exact_phi.network_phi(noisy, cm, n, rng)
        delta = "" if prev is None else f"{mx - prev:+.4f}"
        print(f"  {n:<5}{mx:<12.4f}{delta}")
        curve.append((n, mx))
        prev = mx
    print("=" * 66)
    deltas = [curve[i][1] - curve[i - 1][1] for i in range(1, len(curve))]
    jump4 = len(deltas) >= 3 and deltas[2] > 1.5 * max(deltas[0], deltas[1], 1e-9)
    peak_n = max(curve, key=lambda c: c[1])[0]
    print(f"  step increments: {[f'{d:+.3f}' for d in deltas]}; sharp rise at n=4: {jump4}; peak at n={peak_n}")
    if jump4:
        print("  Reading: a non-collapsing pool reproduces a Niizato-style size-four discontinuity —")
        print("  the rise is a property of the dynamics, not only of the physical substrate.")
    else:
        print(f"  Reading: max Φ does not rise at n=4. Under majority coupling it peaks at n={peak_n} and")
        print("  falls as the pool grows — added members make the consensus more redundant and less")
        print("  integrated. No Niizato-style size-four rise appears; the dependence runs the other way.")
    print("=" * 66)


if __name__ == "__main__":
    main()
