"""Q97: can a coalition of non-core agents flip the verdict that a single one cannot?

Q84 showed one read-only agent cannot flip the triad's verdict, and influence requires membership. Q97
adds two external agents to the read-recipient triad (E, M, R) and asks whether they can jointly destroy
the triad, manufacture one in a broadcast, or gain influence by coordinating with each other while each
stays unidirectional with respect to the core.

Nodes E=0, M=1, R=2, X1=3, X2=4.

- two_read_only : both X1 and X2 read M and are read by none (a coalition of observers).
- two_emit_only : a broadcast base (M'=E), with X1 and X2 as constant sources the core does not read.
- external_loop : X1 reads M, M reads X2, X2 reads X1 — the coalition bridges the core on both sides
                  (M→X1→X2→M), so the pair is collectively bidirectional while each is unidirectional w.r.t.
                  the core directly.
- single_bidir  : one bidirectional-pivotal agent (M'=E∧R∧X, X'=M); the Q84 control that flips the verdict.

Imported by `probe_coordinated_adversary.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


def two_read_only():
    rules = [
        lambda x: x[1],            # E' = M
        lambda x: x[0] & x[2],     # M' = E & R
        lambda x: x[1],            # R' = M
        lambda x: x[1],            # X1' = M
        lambda x: x[1],            # X2' = M
    ]
    return rules, ("E", "M", "R", "X1", "X2")


def two_emit_only():
    rules = [
        lambda x: x[1],            # E' = M
        lambda x: x[0],            # M' = E  (broadcast, ignores R and the agents)
        lambda x: x[1],            # R' = M
        lambda x: x[3],            # X1' = X1 (constant source)
        lambda x: x[4],            # X2' = X2 (constant source)
    ]
    return rules, ("E", "M", "R", "X1", "X2")


def external_loop():
    rules = [
        lambda x: x[1],                  # E' = M
        lambda x: x[0] & x[2] & x[4],    # M' = E & R & X2  (the core reads X2)
        lambda x: x[1],                  # R' = M
        lambda x: x[1],                  # X1' = M          (X1 reads the core)
        lambda x: x[3],                  # X2' = X1         (X2 reads X1, not the core directly)
    ]
    return rules, ("E", "M", "R", "X1", "X2")


def single_bidir():
    rules = [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]
    return rules, ("E", "M", "R", "X")
