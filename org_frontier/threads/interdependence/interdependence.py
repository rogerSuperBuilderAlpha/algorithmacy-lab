"""The interdependence thread (E14 of the catalog line).

Thompson's typology of interdependence — pooled, sequential, reciprocal — read through exact Φ. Only
reciprocal interdependence binds. Parties that contribute independently to a shared mediator, or that pass
work one way down a line, produce no integration at all. Only when the parties and the mediator read one
another both ways does the coordination commit. The classic ordinal typology comes out binary here: pooled
and sequential are zero, reciprocal is the only one that can be irreducible.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/interdependence/interdependence.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.veto_player._harness import integrating_coalitions
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 600
N = 3
L = tuple("WSC")


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    tri = integ = 0
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        if integrating_coalitions(net, tpm, N):
            integ += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
    print(f"{name}: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) integrating-forms={integ}")


def main():
    print("Thompson's interdependence types, read through exact Phi.")
    run("pooled     (parties autonomous, S reads both)", {0: [0], 1: [0, 2], 2: [2]})
    run("sequential (W->S->C feedforward)             ", {0: [0], 1: [0], 2: [1]})
    run("reciprocal (W<->S<->C bidirectional)         ", {0: [1], 1: [0, 2], 2: [1]})


if __name__ == "__main__":
    main()
