"""The fragility thread (E6 of the catalog line).

The gate-logic thread found that a parity mediator binds all three parties equally while a monotone one
concentrates the credit. This thread reads the same split as resilience: which party is the coordination's
single point of failure. Remove a node and measure the integration left. Under a monotone mediator only the
mediator is indispensable — a party can be dropped with no loss — while under a parity mediator every party
is a single point of failure, and removing any node destroys all the integration.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/fragility/fragility.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one
from org_frontier.threads.coalition_structure._harness import network, phi_s_maxstate
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 400
N = 3
L = tuple("WSC")
EPS = 1e-6
GATES = {"AND ": lambda x: x[0] & x[2], "XOR ": lambda x: x[0] ^ x[2]}


def run(name, gate):
    rng = random.Random(SEED)
    tri = 0
    loss_mediator, loss_party = [], []
    for _ in range(FORMS):
        rules = [_rule_of_one(rng.randint(0, 3), 1), gate, _rule_of_one(rng.randint(0, 3), 1)]
        net, tpm = network(rules, L)
        if classify_rules(list(rules), L).structure != "triadic":
            continue
        tri += 1
        whole = phi_s_maxstate(net, tpm, N, (0, 1, 2))
        if whole <= EPS:
            continue
        no_mediator = phi_s_maxstate(net, tpm, N, (0, 2))   # remove S -> {W,C}
        no_party = phi_s_maxstate(net, tpm, N, (1, 2))       # remove W -> {S,C}
        loss_mediator.append((whole - no_mediator) / whole)
        loss_party.append((whole - no_party) / whole)
    print(f"{name} mediator: triadic={tri} fraction-of-Phi-lost removing the MEDIATOR={np.mean(loss_mediator):.3f} "
          f"a PARTY={np.mean(loss_party):.3f}")


def main():
    print("Single point of failure: fraction of integration lost when a node is removed.")
    for name in ["AND ", "XOR "]:
        run(name, GATES[name])


if __name__ == "__main__":
    main()
