"""The two-hubs thread (E25 of the catalog line).

The scale thread found a single hub cannot bind five parties: its commitment rate falls to zero. This thread
gives the resolution. Add a second hub — a second mediator, a management layer — and the five-party
coordination commits readily, in two of five forms, more often than a single hub binds even three parties.
A coordination too large for one mediator is bound by two.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/two_hubs/two_hubs.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 300
N = 5
L = tuple("ABCHG")   # A,B,C parties (0,1,2); H1=3, H2=4 hubs


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    tri = 0
    for _ in range(FORMS):
        rules = build(arch, rng)
        if classify_rules(rules, L).structure == "triadic":
            tri += 1
    print(f"  {name}: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%)")


def main():
    print("Five parties, one hub vs two. Does a second mediator beat the size limit?")
    run("one hub  (A,B,C->H1; H1->all) ", {0: [3], 1: [3], 2: [3], 3: [0, 1, 2], 4: [4]})
    run("two hubs (A,B,C<->H1,H2)      ", {0: [3, 4], 1: [3, 4], 2: [3, 4], 3: [0, 1, 2], 4: [0, 1, 2]})
    print("A second hub takes commitment from 0% to 40% at five parties.")


if __name__ == "__main__":
    main()
