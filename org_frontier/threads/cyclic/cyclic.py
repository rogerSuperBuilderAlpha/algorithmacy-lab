"""The cyclic-coordination thread (E1 of the catalog line).

The engagement thread found that closing a feedback cycle raises commitment. This one takes the cycle to its
limit: a directed ring of three parties, each reading the one before it, with no designated mediator. The
question for the catalog is whether cyclic coordination has a bottleneck at all, and how its commitment and
credit compare to the mediated star. A ring is symmetric, so the prior is that no single party is the veto
player and the credit spreads evenly, with commitment higher than the star's because every party closes a
loop.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/cyclic/cyclic.py

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
FORMS = 600
N = 3
L = tuple("ABC")
EPS = 1e-6


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    tri = integ = empty_veto = single_veto = 0
    top_shares = []
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            vs = veto_set(W)
            if not vs:
                empty_veto += 1
            elif len(vs) == 1:
                single_veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            sh = shapley(v, N)
            total = sum(sh)
            if total > EPS:
                top_shares.append(max(sh) / total)
    ts = f"{np.mean(top_shares):.3f}" if top_shares else "n/a  "
    print(f"{name}: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) "
          f"empty-veto|integrating={empty_veto}/{integ}={100 * empty_veto / max(integ, 1):.0f}% "
          f"single-veto|integrating={single_veto}/{integ}={100 * single_veto / max(integ, 1):.0f}% "
          f"top-credit-share|triadic={ts}")


def main():
    print("Cyclic coordination vs the mediated star. A ring has no designated mediator.")
    run("mediated star (S=node 1)   ", {0: [1], 1: [0, 2], 2: [1]})
    run("directed ring (A->B->C->A) ", {0: [2], 1: [0], 2: [1]})
    run("fully connected (all<->all)", {0: [1, 2], 1: [0, 2], 2: [0, 1]})


if __name__ == "__main__":
    main()
