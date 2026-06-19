"""The conflict thread (E23 of the catalog line).

Does it matter whether the two parties agree or conflict in how they respond to the mediator? It does not.
A party that responds to the mediator by agreeing and one that responds by doing the opposite bind into the
coordination identically — same commitment rate, same credit split. Only a party that does not respond at
all, that ignores the mediator, fails to bind. Conflict is integrated exactly like cooperation; what binds a
party is that it heeds the mediator, not that it agrees with it.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/conflict/conflict.py

Deterministic: all sixteen mediator gates per party configuration.
"""

import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

N = 3
L = tuple("WSC")
EPS = 1e-6
ID = lambda x: x[1]          # copy the mediator
NOT = lambda x: 1 - x[1]     # do the opposite of the mediator
CONST = lambda x: 0          # ignore the mediator


def run(name, rW, rC):
    tri = 0
    shares = []
    for bits in itertools.product([0, 1], repeat=4):
        gate = lambda x, _t=bits: _t[(x[0] << 1) | x[2]]   # mediator = function of W, C
        rules = [rW, gate, rC]
        net, tpm = network(rules, L)
        if classify_rules(list(rules), L).structure != "triadic":
            continue
        tri += 1
        v = value_function(net, tpm, N)
        sh = shapley(v, N)
        total = sum(sh)
        if total > EPS:
            shares.append(sh[1] / total)
    s = f"{np.mean(shares):.3f}" if shares else "n/a  "
    print(f"  {name}: triadic-S-gates={tri:2d}/16  mediator-share={s}")


def main():
    print("Worker copies the mediator; vary how the counterpart C responds. S ranges over all gates.")
    run("C agrees    (C = S)    ", ID, ID)
    run("C conflicts (C = not S)", ID, NOT)
    run("C ignores   (C = const)", ID, CONST)


if __name__ == "__main__":
    main()
