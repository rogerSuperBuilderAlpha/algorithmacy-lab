"""Q64 forms: multi-recipient outreach campaigns, parameterized by recipient count k.

Parties: sender intent (E, index 0), agent/mediator (M, index 1), recipients (R1..Rk, indices 2..k+1).
The agent's commit is M's rule. Each recipient reads the agent (Ri'=M) so it stays live; the sender
reads the agent (E'=M).
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]            # R decoupled -> dyadic
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]  # triadic


def labels(k):
    return ("E", "M") + tuple(f"R{i}" for i in range(1, k + 1))


def _downstream(n):
    """E'=M and each Ri'=M (all read the agent)."""
    return [lambda x: x[1]] + [lambda x: x[1] for _ in range(n - 2)]


def all_required(k):
    """M' = E AND R1 AND ... AND Rk."""
    n = k + 2

    def m(x):
        v = x[0]
        for i in range(2, n):
            v &= x[i]
        return v

    rules = [lambda x: x[1], m] + [lambda x: x[1] for _ in range(2, n)]
    return rules


def substitutable(k):
    """M' = E AND (R1 OR ... OR Rk)."""
    n = k + 2

    def m(x):
        o = 0
        for i in range(2, n):
            o |= x[i]
        return x[0] & o

    return [lambda x: x[1], m] + [lambda x: x[1] for _ in range(2, n)]


def pooled(k):
    """M' = E (the agent reads no recipient); recipients are readouts."""
    n = k + 2
    return [lambda x: x[1], lambda x: x[0]] + [lambda x: x[1] for _ in range(2, n)]


def mixed_k3():
    """k=3, n=5: M' = E AND R1 AND (R2 OR R3) — one substitutable pair."""
    return [lambda x: x[1], lambda x: x[0] & x[2] & (x[3] | x[4]),
            lambda x: x[1], lambda x: x[1], lambda x: x[1]]


def check_controls(verdict_fn):
    d = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    t = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = d.structure == "dyadic" and t.structure == "triadic"
    line = (f"[control] dyadic relay: {d.structure} Φ={d.max_phi:.3f} | "
            f"triadic full-coupling: {t.structure} Φ={t.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
