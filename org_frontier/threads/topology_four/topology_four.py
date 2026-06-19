"""The topology-four thread (E16 of the catalog line).

The cyclic thread found, at three parties, that a symmetric ring shares the credit while a star concentrates
it. This one carries the finding to four parties. A four-party ring splits the credit into exact quarters,
with no bottleneck; a star concentrates it on the hub; a line falls between, the middle positions holding
more than the ends. Topology sets the credit distribution at four parties as it did at three.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/topology_four/topology_four.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 250
N = 4
L = tuple("ABCD")
EPS = 1e-6


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    tri = integ = empty = 0
    tops = []
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if not veto_set(W):
                empty += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            sh = shapley(v, N)
            total = sum(sh)
            if total > EPS:
                tops.append(max(sh) / total)
    ts = f"{np.mean(tops):.3f}" if tops else "n/a"
    print(f"{name}: triadic={tri}/{FORMS} empty-veto|integrating={empty}/{integ} top-credit-share={ts}")


def main():
    print("Four-party topologies: ring vs star vs line (equal share = 0.25).")
    run("ring (A->B->C->D->A)", {0: [3], 1: [0], 2: [1], 3: [2]})
    run("star (hub=B)        ", {0: [1], 1: [0, 2, 3], 2: [1], 3: [1]})
    run("line (A-B-C-D)      ", {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]})


if __name__ == "__main__":
    main()
