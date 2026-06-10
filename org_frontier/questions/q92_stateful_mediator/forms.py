"""Q92: a mediator with memory, and whether stored state substitutes for a live read.

Every determination in the corpus is memoryless: the next state is a function of the current state alone.
Q92 gives the mediator memory and asks whether a remembered value of the recipient can substitute for a
live read of it. Finding 3 made liveness — the mediator reading the parties as they currently are —
necessary for the triad. This tests whether liveness is about the current read or about the recipient
being bound through any path, including a memory.

Forms (worker E, mediator M, recipient R, memory Mem):
- live            : M'=E∧R (the read-recipient triad; Φ=2, baseline).
- tracking_memory : M'=E∧Mem, Mem'=R — M reads a memory that holds the recipient's previous value, not
                    the recipient directly.
- frozen_memory   : M'=E∧Mem, Mem'=Mem — the memory does not track the recipient.
- self_memory     : M'=E∧M (M reads the worker and its own previous state); the recipient feeds nothing.

Imported by `probe_stateful_mediator.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


def live():
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    return rules, ("E", "M", "R")


def tracking_memory():
    # E=0, M=1, R=2, Mem=3. M reads E and Mem; Mem tracks R.
    rules = [
        lambda x: x[1],            # E' = M
        lambda x: x[0] & x[3],     # M' = E & Mem
        lambda x: x[1],            # R' = M
        lambda x: x[2],            # Mem' = R
    ]
    return rules, ("E", "M", "R", "Mem")


def frozen_memory():
    rules = [
        lambda x: x[1],            # E' = M
        lambda x: x[0] & x[3],     # M' = E & Mem
        lambda x: x[1],            # R' = M
        lambda x: x[3],            # Mem' = Mem  (does not track R)
    ]
    return rules, ("E", "M", "R", "Mem")


def self_memory():
    # M reads the worker and its own previous state; the recipient feeds nothing into M.
    rules = [lambda x: x[1], lambda x: x[0] & x[1], lambda x: x[1]]
    return rules, ("E", "M", "R")
