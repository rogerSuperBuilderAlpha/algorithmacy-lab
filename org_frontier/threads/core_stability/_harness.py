"""Harness for the core-stability thread.

The cooperative game v(S) = φ_s(S) assigns a worth to every coalition of parties. The *core* is the set of
ways to split the whole's worth v(N) among the parties so that no coalition can do better on its own:
allocations x with sum(x) = v(N) and sum_{i in S} x_i >= v(S) for every S. A non-empty core means a stable
division of the credit for the coordination's integration exists; an empty core means every division leaves
some coalition wanting to walk.

The subadditivity thread showed φ_s is subadditive — a tight pair often out-values the whole. This harness
asks what that does to stability: whether a stable allocation exists, and whether the Shapley value is one.
"""

import itertools
import os
import sys

import numpy as np
from scipy.optimize import linprog

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

EPS = 1e-6


def g(v, S):
    return v.get(frozenset(S), 0.0)


def core_nonempty(v, n):
    """True if some efficient allocation meets every coalition's demand — the core is non-empty."""
    A_ub, b_ub = [], []
    for r in range(1, n):
        for S in itertools.combinations(range(n), r):
            A_ub.append([-1.0 if i in S else 0.0 for i in range(n)])
            b_ub.append(-g(v, S))
    res = linprog(
        c=[0.0] * n,
        A_ub=np.array(A_ub), b_ub=np.array(b_ub),
        A_eq=np.array([[1.0] * n]), b_eq=np.array([g(v, tuple(range(n)))]),
        bounds=[(None, None)] * n, method="highs",
    )
    return bool(res.success)


def shapley_in_core(x, v, n):
    """True if the Shapley allocation x meets every coalition's demand."""
    for r in range(1, n):
        for S in itertools.combinations(range(n), r):
            if sum(x[i] for i in S) < g(v, S) - EPS:
                return False
    return True
