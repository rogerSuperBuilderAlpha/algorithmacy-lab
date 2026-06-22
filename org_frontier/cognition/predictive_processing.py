"""A sixth theory, beyond the paper's five: predictive processing and the moving target.

Hunt's paper engages five accounts of mind. Predictive processing is a sixth the arm adds: the worker
maintains a generative model of the system and acts to reduce its prediction error. The opaque,
interested third party is a generative process she cannot fully invert, because part of what it computes
turns on a counterpart she cannot see, and a moving one, because it retrains on what she feeds it. This
battery formalizes both: an irreducible floor on the surprise she can reduce, set by the hidden
counterpart, and a binding that decays as the system's rule drifts underneath her.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/cognition/predictive_processing.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import math
import numpy as np
from org_frontier.threads.margin_to_dyad._sphi import sphi


def _H(p):
    """Binary entropy in bits."""
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def pp1_irreducible_surprise():
    """The worker predicts the output; the surprise she cannot reduce is the hidden counterpart's."""
    print("PP1 the irreducible surprise — what the worker cannot predict away (gate S = W AND C):")
    # output = W & C, C hidden and uniform. Best model from W alone: P(out=1 | W).
    # H(out | W) is the residual surprise; H(out | W, C) = 0 is the full model.
    res = 0.0
    for w in (0, 1):
        # given W, out = w & C, C ~ Bernoulli(0.5); P(out=1|W=w) = w * 0.5
        res += 0.5 * _H(w * 0.5)
    print(f"  residual surprise with the counterpart hidden: H(out|W) = {res:.2f} bits")
    print(f"  surprise with the counterpart observable:       H(out|W,C) = 0.00 bits")
    print(f"  -> {res:.2f} bits of surprise no amount of modeling removes, set by what she cannot see")


def pp2_active_inference():
    """She acts to test her model; probing closes the channel she controls, not the hidden one."""
    print("\nPP2 active inference — probing reduces the uncertainty she controls, not the hidden part:")
    # she sets W (acts) and observes out; she can learn P(out | W) exactly, never the C-dependence
    print("  by probing her own input she learns P(out|W) exactly (epistemic uncertainty about her channel -> 0)")
    print("  she cannot set the counterpart, so the 0.50 bits from the hidden counterpart stay")
    print("  active inference closes the gap she can act on and leaves the opacity floor intact")


def pp3_moving_target(window=40):
    """The system retrains: the rule drifts, and the worker's window-fit model lags it."""
    print("\nPP3 the moving target — the system retrains, and her model lags as the rule drifts:")
    rng = random.Random(0)
    for period in (1000, 200, 60, 20):   # steps between rule changes; smaller = faster drift
        acc = 0.0
        trials = 30
        for _ in range(trials):
            gate = [rng.randint(0, 1) for _ in range(4)]
            hist = []
            correct = total = 0
            for t in range(400):
                if t % period == 0 and t > 0:
                    j = rng.randrange(4); gate[j] ^= 1   # the system retrains: one entry flips
                w, c = rng.randint(0, 1), rng.randint(0, 1)
                out = gate[w + 2 * c]
                # her model: majority over the last `window` observations at this (w,c)
                recent = [o for (ww, cc, o) in hist[-window * 4:] if ww == w and cc == c]
                pred = (1 if sum(recent) * 2 >= len(recent) else 0) if recent else rng.randint(0, 1)
                correct += pred == out; total += 1
                hist.append((w, c, out))
            acc += correct / total
        print(f"  rule changes every {period:>4} steps: her prediction accuracy {acc/trials:.2f}")


def pp4_drift_binding():
    """A drifting commit binds less: the moving target degrades the coordination's irreducibility."""
    print("\nPP4 the moving target also weakens the binding — a drifting commit is a noisy commit:")
    # a system committing rule A with prob (1-d) and a flipped rule B with prob d (mid-retrain)
    for d in (0.0, 0.1, 0.25, 0.5):
        T = np.zeros((8, 3))
        for s in range(8):
            W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
            T[s, 0] = S; T[s, 2] = S
            A = float(W & C); B = float(W | C)   # two rules it is drifting between
            T[s, 1] = (1 - d) * A + d * B
        print(f"  drift d={d}: Φ={sphi(T)}")


if __name__ == "__main__":
    pp1_irreducible_surprise()
    pp2_active_inference()
    pp3_moving_target()
    pp4_drift_binding()
