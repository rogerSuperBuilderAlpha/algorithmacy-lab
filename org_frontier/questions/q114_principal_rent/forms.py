"""Q114: the principal's value capture — rent at the parties' expense, or added value?

Finding 8 found a principal joins the irreducible core only when bidirectionally coupled to the mediator.
This asks what joining the core is worth: does the principal capture value, and does its value come at the
parties' expense (rent) or add to the total? An owner who only monitors the mediator, without being read by
it, should capture nothing.

Forms (worker E, mediator M, recipient R, principal P), from the principal study:
- bidirectional : M' = E ∧ R ∧ P, P' = M — P is in the core (Finding 8).
- monitor_only  : M' = E ∧ R, P' = M — P reads the mediator but is not read; P is outside the core.

`shapley_for` reuses Q111's Shapley value of subsystem-Φ.

Imported by `probe_principal_rent.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q111_shapley_value import forms as q111

LABELS = ("E", "M", "R", "P")
BIDIRECTIONAL = [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]
MONITOR_ONLY = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]


def base_triad_shapley():
    return q111.shapley(*q111.read_recipient())[0]      # {E: .333, M: 1.333, R: .333}


def shapley_for(rules):
    return q111.shapley(rules, LABELS)
