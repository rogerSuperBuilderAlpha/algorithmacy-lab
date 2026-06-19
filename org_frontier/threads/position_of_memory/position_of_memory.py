"""The position-of-memory thread (E9 of the catalog line).

The memory thread found that giving the mediator a self-loop raised its credit share sharply. This one asks
whether the same is true of a party. It is not. Memory pays at the center and not at the periphery. Giving
the mediator memory raises its share by about a third; giving a party memory leaves that party's share where
it was, even a touch lower. What accumulating state is worth depends on the position that holds it.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/position_of_memory/position_of_memory.py

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
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 600
N = 3
L = tuple("WSC")
EPS = 1e-6


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def share(arch, node):
    rng = random.Random(SEED)
    vals = []
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        if classify_rules(list(rules), L).structure != "triadic":
            continue
        v = value_function(net, tpm, N)
        sh = shapley(v, N)
        total = sum(sh)
        if total > EPS:
            vals.append(sh[node] / total)
    return np.mean(vals)


def main():
    print("Does memory pay at the center (mediator) or the periphery (a party)?")
    base = {0: [1], 1: [0, 2], 2: [1]}
    s_base = share(base, 1)
    w_base = share(base, 0)
    s_mem = share({0: [1], 1: [0, 1, 2], 2: [1]}, 1)        # mediator gets a self-loop
    w_mem = share({0: [0, 1], 1: [0, 2], 2: [1]}, 0)        # a party gets a self-loop
    print(f"mediator credit share: no memory={s_base:.3f}  with memory={s_mem:.3f}  gain={s_mem - s_base:+.3f}")
    print(f"party    credit share: no memory={w_base:.3f}  with memory={w_mem:.3f}  gain={w_mem - w_base:+.3f}")
    print("Memory pays at the center; at the periphery it does not.")


if __name__ == "__main__":
    main()
