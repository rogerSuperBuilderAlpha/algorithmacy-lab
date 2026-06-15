"""Harness for the veto-player thread.

A coalition of parties is *integrating* when its system integrated information φ_s exceeds zero. Among the
multi-party coalitions (two or more parties), a party is a *veto player* when it belongs to every
integrating coalition — no two other parties can integrate without it. In a three-party form this reads
off the complement: party m is a veto player exactly when the opposite pair does not integrate alone.

The veto player is the cooperative-game name for a structural bottleneck. This harness finds it and relates
it to the Shapley value (the platform thread's outside-option party, the Shapley thread's pivotal party)
and to the triadic verdict (the dissertation's commit-versus-convey line).
"""

import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.threads.coalition_structure._harness import network, phi_s_maxstate

EPS = 1e-6


def integrating_coalitions(net, tpm, n):
    """Multi-party coalitions (size >= 2) whose φ_s exceeds zero, as a dict frozenset(S) -> φ_s."""
    out = {}
    for r in range(2, n + 1):
        for S in itertools.combinations(range(n), r):
            val = phi_s_maxstate(net, tpm, n, S)
            if val > EPS:
                out[frozenset(S)] = val
    return out


def veto_set(winners):
    """Intersection of all integrating coalitions — the parties in every one. Empty if no winners."""
    if not winners:
        return frozenset()
    inter = None
    for w in winners:
        inter = set(w) if inter is None else (inter & set(w))
    return frozenset(inter)


def is_hub(winners, m, n):
    """A dyadic bottleneck signature: the integrating coalitions are exactly the pairs that contain m,
    each a two-party dyad, with no larger coalition integrating. m bridges two dyads without binding the
    whole into one irreducible determination."""
    if not winners:
        return False
    for w in winners:
        if len(w) != 2 or m not in w:
            return False
    return True
