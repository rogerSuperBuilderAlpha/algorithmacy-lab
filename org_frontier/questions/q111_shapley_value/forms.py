"""Q111: the Shapley value of integration — how a coordination's value is distributed among its parties.

The program reads which parties are bound into the core. This asks what each party is worth. The value of
a coalition S is the integrated information of the subsystem on S — how much irreducible coordination that
set of parties can sustain — and a party's Shapley value is its average marginal contribution to that value
across all orderings. The Shapley values distribute the system's Φ among the parties.

For the read-recipient triad, the mediator is in every productive coalition (the two outer parties produce
nothing without it), so it should capture a disproportionate share. A spectator, contributing nothing,
should have value zero.

Imported by `probe_shapley_value.py`.
"""

import os
import sys
from itertools import combinations
from math import factorial

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules


def read_recipient():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("E", "M", "R")


def with_spectator():
    """The triad plus a read-only spectator X that reads the mediator and is read by no one."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]
    return rules, ("E", "M", "R", "X")


def _value_fn(rules, labels):
    n = len(rules)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
    state = tuple(1 for _ in range(n))
    cache = {}

    def v(S):
        S = tuple(sorted(S))
        if S in cache:
            return cache[S]
        if not S:
            cache[S] = 0.0
            return 0.0
        try:
            phi = float(nbp.sia(pyphi.Subsystem(net, state, nodes=S)).phi)
        except Exception:
            phi = 0.0
        cache[S] = max(0.0, phi)
        return cache[S]

    return v


def shapley(rules, labels):
    """Return {party: Shapley value of integration}."""
    n = len(rules)
    v = _value_fn(rules, labels)
    players = list(range(n))
    vals = {i: 0.0 for i in players}
    for i in players:
        others = [p for p in players if p != i]
        for r in range(len(others) + 1):
            for S in combinations(others, r):
                w = factorial(len(S)) * factorial(n - len(S) - 1) / factorial(n)
                vals[i] += w * (v(tuple(S) + (i,)) - v(S))
    return {labels[i]: round(vals[i], 3) for i in players}, round(v(tuple(players)), 3)
