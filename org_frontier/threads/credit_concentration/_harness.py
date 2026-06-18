"""Harness for the credit-concentration thread.

In the game v(S) = φ_s(S), the Shapley value pays each party its average marginal contribution to the
coordination's integration. This harness measures how that credit is spread across the parties of a triadic
form: whether one party takes most of it, and whether an excluded party's share goes negative.

Shares are taken against the whole's worth v(N) = φ_s of the full system, which is positive exactly when
the form is triadic.
"""

import itertools
import math
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

EPS = 1e-6


def g(v, S):
    return v.get(frozenset(S), 0.0)


def shapley(v, n):
    out = []
    for i in range(n):
        others = [j for j in range(n) if j != i]
        tot = 0.0
        for r in range(len(others) + 1):
            for S in itertools.combinations(others, r):
                w = math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)
                tot += w * (g(v, S + (i,)) - g(v, S))
        out.append(tot)
    return out


def gini(values):
    """Gini coefficient of non-negative shares (0 = equal, toward 1 = concentrated)."""
    xs = sorted(max(x, 0.0) for x in values)
    n = len(xs)
    s = sum(xs)
    if s <= 0:
        return float("nan")
    return 2 * sum((i + 1) * x for i, x in enumerate(xs)) / (n * s) - (n + 1) / n
