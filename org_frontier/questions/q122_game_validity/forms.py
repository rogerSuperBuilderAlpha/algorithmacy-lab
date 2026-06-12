"""Q122: is the value function a valid cooperative game? An audit answering critical-review T2/T3/T5.

The critical review charged that the Shapley machinery of the value wave (Q111-Q116) reads welfare off an
ill-formed game: subsystem-Φ is not monotone or superadditive in general, so the "value distribution"
language is unlicensed; the negative Shapley values are clamp artifacts; and the whole game depends on the
arbitrary frozen background. This study audits those three claims directly on the forms the wave used.

The value function v(S) is the subsystem-Φ of the node-set S, with the complement frozen at a background
state (Q111). The audit recomputes it with the clamp on and off, and at the all-ones (integrating) and
all-zeros backgrounds, and checks monotonicity and superadditivity over the full subset lattice.

Imported by `probe_game_validity.py`.
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
from org_frontier.questions.q111_shapley_value import forms as q111
from org_frontier.questions.q114_principal_rent import forms as q114
from org_frontier.questions.q85_agent_market import forms as q85


def value_fn(rules, labels, background=1, clamp=True):
    """v(S) = subsystem-Φ of S with the complement frozen at the background state. Cached."""
    n = len(rules)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
    state = tuple(background for _ in range(n))
    cache = {}

    def v(S):
        S = tuple(sorted(S))
        if S in cache:
            return cache[S]
        if not S:
            return 0.0
        try:
            phi = float(nbp.sia(pyphi.Subsystem(net, state, nodes=S)).phi)
        except Exception:
            phi = 0.0
        cache[S] = max(0.0, phi) if clamp else phi
        return cache[S]

    return v, n


def shapley(rules, labels, background=1, clamp=True):
    v, n = value_fn(rules, labels, background, clamp)
    players = list(range(n))
    vals = {i: 0.0 for i in players}
    for i in players:
        others = [p for p in players if p != i]
        for r in range(len(others) + 1):
            for S in combinations(others, r):
                w = factorial(len(S)) * factorial(n - len(S) - 1) / factorial(n)
                vals[i] += w * (v(tuple(S) + (i,)) - v(S))
    return {labels[i]: round(vals[i], 3) for i in players}


def monotone_superadditive(rules, labels):
    """(monotonicity violations, superadditivity violations) over the full subset lattice, clamp on, bg=1."""
    v, n = value_fn(rules, labels)
    players = list(range(n))
    subs = [S for r in range(n + 1) for S in combinations(players, r)]
    mono = sum(1 for S in subs for i in players
               if i not in S and v(tuple(sorted(S + (i,)))) < v(S) - 1e-9)
    nonempty = [S for S in subs if S]
    sup = 0
    for a in range(len(nonempty)):
        for b in range(a, len(nonempty)):
            S, T = nonempty[a], nonempty[b]
            if set(S) & set(T):
                continue
            if v(tuple(sorted(set(S) | set(T)))) < v(S) + v(T) - 1e-9:
                sup += 1
    return mono, sup


def productive_forms():
    """The forms whose value distribution the wave actually reported as surplus."""
    return [
        ("read_recipient", *q111.read_recipient()),
        ("bidirectional_principal", q114.BIDIRECTIONAL, q114.LABELS),
        ("market_N2", q85.all_required(2), q85.labels(2)),
        ("market_N3", q85.all_required(3), q85.labels(3)),
    ]


def degenerate_form():
    """The monitor-only principal: a read-only owner that factors the system (the -0.833 case)."""
    return ("monitor_only_principal", q114.MONITOR_ONLY, q114.LABELS)
