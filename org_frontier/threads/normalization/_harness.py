"""Harness for the normalization thread.

A standing objection to integrated information is that Φ grows with system size, so it should be normalized
— divided by the number of elements — before systems are compared. IIT does not normalize: the major
complex is the subset of absolutely largest φ_s, not largest φ_s per element. This harness measures what
the per-element version would select instead.

Density of a coalition is d(S) = φ_s(S) / |S|. The density-maximal subset is what a normalized exclusion
postulate would keep.
"""

import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


def all_subsets(n):
    return [frozenset(S) for r in range(1, n + 1) for S in itertools.combinations(range(n), r)]


def density_argmax(v, n, min_size=1):
    """The subset maximizing φ_s(S) / |S|, ties broken toward the smaller set. min_size restricts the
    candidate subsets (use 2 for the coordination-only reading)."""
    cands = [S for S in all_subsets(n) if len(S) >= min_size]
    return max(cands, key=lambda S: (v[S] / len(S), -len(S)))
