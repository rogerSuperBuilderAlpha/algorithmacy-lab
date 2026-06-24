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


# ---------------------------------------------------------------------------
# Interested-mediator extension (q168). PP1 and PP2 above fix the output to the
# faithful AND gate, where C is hidden and uniform and the worker faces a 0.50-bit
# residual she cannot reduce. These functions reuse the same surprise accounting
# with the output drawn from Q126's mediator(agenda, k): the worker still sees only
# W, C is still hidden and uniform, but the mediator imposes an agenda on the k
# states where the parties least warrant it. A study can then ask whether interest
# raises the residual floor above the 0.50 bits a merely hidden counterpart sets.
# ---------------------------------------------------------------------------


def residual_surprise_under_mediator(gate):
    """H(out | W) with C hidden and uniform, for an arbitrary mediator gate(w, c).

    The worker's best model from W alone predicts P(out=1 | W=w); the residual is the
    mean binary entropy of that prediction over W ~ uniform. For the faithful AND gate
    this returns the 0.50-bit floor that pp1_irreducible_surprise reports. Used by q168
    with gate = Q126's mediator(agenda, k)."""
    res = 0.0
    for w in (0, 1):
        p1 = 0.5 * sum(gate(w, c) for c in (0, 1))   # P(out=1 | W=w), C ~ Bernoulli(0.5)
        res += 0.5 * _H(p1)
    return res


def probed_w_limit_under_mediator(gate):
    """The residual surprise that remains after the worker probes W (PP2), for gate(w, c).

    Probing W lets the worker learn P(out | W) exactly, removing the epistemic uncertainty
    about her own channel. It cannot set or see C, so the C-aliased part of the output
    survives. That surviving part is exactly H(out | W). The function returns it, so a
    study can check whether probing W drives the interested residual toward 0 (the agenda's
    surprise is self-resolvable) or leaves it at H(out | W) (the agenda joins the opacity
    floor)."""
    return residual_surprise_under_mediator(gate)


# ---------------------------------------------------------------------------
# Active-inference probing bridge (empirical line, q170 study 1). The functions
# above work in closed form on the gate's exact marginals. The empirical arm
# instead samples: the worker runs a finite probing budget against the gate and
# fits a recovered generative model from counts, so the line can study how a
# recovered model degrades under a finite budget rather than in the limit. These
# helpers are shared across the empirical studies; results from them are on
# synthetic probing data, not a measured worker.
# ---------------------------------------------------------------------------


def probe_recover_marginal(gate, budget, rng):
    """Run the pp2 active-inference loop against gate(W, C) for a finite budget.

    The worker sets W uniformly and observes the output with the counterpart C hidden and uniform.
    After ``budget`` probes she fits her recovered generative model P̂(out=1 | W) from Laplace-smoothed
    counts. Returns {W: P̂(out=1|W)}. She cannot set C, so the C-dependence stays outside the recovered
    model — the opacity floor pp1/pp2 names. ``rng`` is a numpy Generator; seed it for determinism."""
    cnt = {0: [0, 0], 1: [0, 0]}
    for _ in range(budget):
        w = int(rng.integers(0, 2))
        c = int(rng.integers(0, 2))
        cnt[w][int(gate(w, c))] += 1
    return {w: (cnt[w][1] + 1) / (cnt[w][0] + cnt[w][1] + 2) for w in (0, 1)}


def recovered_model_kl(gate, phat, states=((0, 0), (0, 1), (1, 0), (1, 1))):
    """KL of the recovered model P̂(out|W) from the true gate, averaged over the (W,C) states.

    Each true output is deterministic, so the per-state divergence is the surprise the recovered model
    assigns to the realized output. The average over the four states is the bits of the true rule the
    W-only model fails to carry — the model-fidelity loss."""
    eps = 1e-9
    kl = 0.0
    for (w, c) in states:
        q = int(gate(w, c))
        p = phat[w]
        kl += -math.log2(max(p, eps)) if q == 1 else -math.log2(max(1 - p, eps))
    return kl / len(states)


def recoverable_fraction(gate, phat, states=((0, 0), (0, 1), (1, 0), (1, 1))):
    """Fraction of (W,C) states where the MAP read of the recovered model matches the true output."""
    hit = 0
    for (w, c) in states:
        pred = 1 if phat[w] >= 0.5 else 0
        hit += int(pred == int(gate(w, c)))
    return hit / len(states)


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
