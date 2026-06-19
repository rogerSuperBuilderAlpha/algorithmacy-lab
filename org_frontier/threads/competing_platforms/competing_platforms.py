"""The competing-platforms thread (E17 of the catalog line).

Two platforms connect the same two parties. When the platforms are identical — genuine substitutes — no
single one holds the bottleneck most of the time, and the two split the credit fairly evenly. When they
differ, one becomes the sole bottleneck far more often and the split is less even. A genuine substitute
reduces a platform's hold on the coordination.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/competing_platforms/competing_platforms.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_set
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 400
N = 4
L = tuple("WXYC")   # W=0, S1=1, S2=2, C=3
EPS = 1e-6
AND = lambda x: x[0] & x[3]
OR = lambda x: x[0] | x[3]


def run(name, gate1, gate2):
    rng = random.Random(SEED)
    tri = integ = sole_veto = 0
    ratios = []
    for _ in range(FORMS):
        rW = _rule_of_set([rng.randint(0, 1) for _ in range(4)], [1, 2])
        rC = _rule_of_set([rng.randint(0, 1) for _ in range(4)], [1, 2])
        rules = [rW, gate1, gate2, rC]
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if veto_set(W) & {1, 2}:
                sole_veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            sh = shapley(v, N)
            hi = max(abs(sh[1]), abs(sh[2]))
            if hi > EPS:
                ratios.append(min(abs(sh[1]), abs(sh[2])) / hi)
    r = f"{np.mean(ratios):.3f}" if ratios else "n/a"
    print(f"{name}: triadic={tri}/{FORMS} a-platform-is-veto|integrating={sole_veto}/{integ} "
          f"S1<->S2-credit-ratio={r}")


def main():
    print("Two platforms connect W and C; the parties read both.")
    run("identical platforms (both AND)", AND, AND)
    run("different platforms (AND, OR) ", AND, OR)


if __name__ == "__main__":
    main()
