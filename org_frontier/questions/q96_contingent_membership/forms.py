"""Q96: a recipient bound into the determination only in some states.

Finding 5 collapses the triad when a party is substitutable or optional, but participation in the corpus
is always unconditional: a bound party is read in every state. Q96 makes the recipient's participation
state-contingent. A gate T tracks the worker (T'=E), and the mediator reads the recipient only when the
gate is on:
    M' = E ∧ (R ∨ ¬T)
so when T=1 the mediator reads the recipient (M'=E∧R) and when T=0 it ignores it (M'=E). Across reachable
states T takes both values, so the recipient is in the determination contingently. The question is whether
contingent participation integrates (triadic) or the conditionality factors it out (dyadic).

Forms (worker E, mediator M, recipient R, gate T):
- contingent : M'=E∧(R∨¬T), T'=E — the recipient is read only when the gate is on.
- always     : M'=E∧R — the read-recipient triad (gate always on); control.
- never      : M'=E — broadcast (gate always off); control.

Imported by `probe_contingent_membership.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


def contingent():
    # E=0, M=1, R=2, T=3. M reads R only when T=1; T tracks E.
    rules = [
        lambda x: x[1],                          # E' = M
        lambda x: x[0] & (x[2] | (1 - x[3])),    # M' = E AND (R OR NOT T)
        lambda x: x[1],                          # R' = M
        lambda x: x[0],                          # T' = E
    ]
    return rules, ("E", "M", "R", "T")


def always():
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    return rules, ("E", "M", "R")


def never():
    rules = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]
    return rules, ("E", "M", "R")
