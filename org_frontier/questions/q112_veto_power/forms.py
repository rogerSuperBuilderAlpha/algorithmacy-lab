"""Q112: veto power — which parties can unilaterally collapse the coordination?

Q104 found every edge of the minimal triad load-bearing and Q108 the parties knife-edge. This asks the
game-theoretic version: which parties hold a veto, able to collapse the coordination by withdrawing? A
party defects by going constant — it stops participating. The verdict after each defection says whether
that party held a veto.

Veto power is then set against the value capture of Q111: every core party may veto while the value still
concentrates at the mediator, because veto is the power to destroy and value is the productive contribution,
which differ. The sub-coalition values (the recipient pair against a mediator pair) show why.

Imported by `probe_veto_power.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q111_shapley_value import forms as q111

L3 = ("E", "M", "R")
READ_RECIPIENT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def _defect(rules, i):
    """Replace party i's rule with a constant (it stops participating)."""
    out = list(rules)
    out[i] = lambda x: 0
    return out


def core_vetoes():
    """For each party of the triad, whether its defection collapses the verdict to dyadic."""
    out = {}
    for i, name in enumerate(L3):
        v = verdict(_defect(READ_RECIPIENT, i), L3)
        out[name] = v.structure == "dyadic"
    return out


def spectator_veto():
    """Does a read-only spectator's defection collapse the major complex {E, M, R}?"""
    rules, labels = q111.with_spectator()      # E, M, R, X with X reading M
    defected = list(rules)
    defected[3] = lambda x: 0                   # X stops participating
    core, _phi = major_complex(defected, labels)
    return set(core or ()) != {"E", "M", "R"}   # True if the core changed (a veto)


def subcoalition_values():
    """v({E,R}) and v({M,R}) from the Q111 value function."""
    v = q111._value_fn(*q111.read_recipient())
    return {"E,R": round(v((0, 2)), 3), "M,R": round(v((1, 2)), 3), "E,M": round(v((0, 1)), 3)}
