"""Harness for the subadditivity thread.

Treat a coordination form as a cooperative game whose value on a coalition S is v(S) = φ_s(S), the system
integrated information of S (max over reachable states, true value for singletons). The dissertation's
slogan, "the whole is more than the sum of its parts," is the cooperative-game property of
superadditivity: v(S ∪ T) ≥ v(S) + v(T) for disjoint S, T. This harness measures whether the integration
game has it.

Two regimes matter at the edges of the lattice:
  - synergy at the bottom: two parties that integrate with no one alone (v = 0 each) form an integrating
    dyad (v > 0). Coordination creates irreducibility from nothing.
  - dilution at the top: the whole integrates less than its tightest pair, v(N) < max-pair. A third party
    lowers integration. This is the exclusion postulate selecting a proper subset.
"""

import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.threads.coalition_structure._harness import phi_s_maxstate

EPS = 1e-6


def value_function(net, tpm, n):
    """v(S) = φ_s(S) for every non-empty subset, singletons at their true intrinsic value."""
    return {frozenset(S): phi_s_maxstate(net, tpm, n, S)
            for r in range(1, n + 1) for S in itertools.combinations(range(n), r)}


def disjoint_splits(n):
    """Each unordered pair of disjoint non-empty coalitions (S, T) over n nodes."""
    seen = set()
    nodes = range(n)
    for r in range(1, n):
        for S in itertools.combinations(nodes, r):
            rest = [x for x in nodes if x not in S]
            for t in range(1, len(rest) + 1):
                for T in itertools.combinations(rest, t):
                    key = frozenset([frozenset(S), frozenset(T)])
                    if key not in seen:
                        seen.add(key)
                        yield frozenset(S), frozenset(T)


def has_subadditive_split(v, n):
    """True if some disjoint split has v(S∪T) < v(S) + v(T): the whole is worth less than its parts."""
    return any(v[S | T] < v[S] + v[T] - EPS for S, T in disjoint_splits(n))


def is_superadditive(v, n):
    """True if every disjoint split has v(S∪T) ≥ v(S) + v(T)."""
    return all(v[S | T] >= v[S] + v[T] - EPS for S, T in disjoint_splits(n))


def is_non_monotone(v, n):
    """True if adding a party to some coalition lowers its integration: v(S ∪ {i}) < v(S)."""
    for r in range(1, n):
        for S in itertools.combinations(range(n), r):
            fs = frozenset(S)
            for i in range(n):
                if i not in fs and v[fs | {i}] < v[fs] - EPS:
                    return True
    return False
