"""The gate-logic thread (E2 of the catalog line).

E1 found that topology decides whether a coordination has a bottleneck. This one holds the topology fixed —
the mediated star — and varies the mediator's gate, its coordination logic. The logic decides two things the
topology does not: how readily the form commits, and how the credit splits. A monotone mediator (AND, OR)
commits half as often as a parity one and takes two thirds of the credit; a parity mediator (XOR, XNOR)
commits twice as often and splits the credit into equal thirds. The mediator is the veto player throughout.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/gate_logic/gate_logic.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 600
N = 3
L = tuple("WSC")
EPS = 1e-6

GATES = {
    "AND ": lambda x: x[0] & x[2],
    "OR  ": lambda x: x[0] | x[2],
    "XOR ": lambda x: x[0] ^ x[2],
    "XNOR": lambda x: 1 - (x[0] ^ x[2]),
}


def run(name, gate):
    rng = random.Random(SEED)
    tri = integ = veto = 0
    shares = []
    for _ in range(FORMS):
        rules = [_rule_of_one(rng.randint(0, 3), 1), gate, _rule_of_one(rng.randint(0, 3), 1)]
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if 1 in veto_set(W):
                veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            total = sum(shapley(v, N))
            if total > EPS:
                shares.append(shapley(v, N)[1] / total)
    s = f"{np.mean(shares):.3f}" if shares else "n/a"
    print(f"{name} mediator: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) "
          f"S-veto|integrating={veto}/{integ}={100 * veto / max(integ, 1):.0f}% S-share|triadic={s}")


def main():
    print("Coordination logic in the mediated star: S = gate(W,C); parties heed S with random rules.")
    for name in ["AND ", "OR  ", "XOR ", "XNOR"]:
        run(name, GATES[name])


if __name__ == "__main__":
    main()
