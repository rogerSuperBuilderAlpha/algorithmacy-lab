"""The mediator-memory thread (E3 of the catalog line).

The gate-logic thread varied what the mediator computes. This one varies whether it remembers: a self-loop
gives the mediator its own intrinsic activity. Memory does not change whether the triad commits, but it
changes who is credited. A mediator that remembers takes a far larger share of the credit than a memoryless
one, and the parties recover some of it only when they remember too.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/memory/memory.py

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
L = tuple("WSC")
EPS = 1e-6


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    tri = integ = veto = 0
    shares = []
    for _ in range(FORMS):
        rules = build(arch, rng)
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
    print(f"{name}: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) "
          f"S-veto|integrating={veto}/{integ}={100 * veto / max(integ, 1):.0f}% S-share|triadic={s}")


def main():
    print("Mediator memory: a self-loop gives intrinsic activity. Does it concentrate credit?")
    run("memoryless S (reads W,C)    ", {0: [1], 1: [0, 2], 2: [1]})
    run("S remembers (reads W,S,C)   ", {0: [1], 1: [0, 1, 2], 2: [1]})
    run("everyone remembers          ", {0: [0, 1], 1: [0, 1, 2], 2: [1, 2]})


if __name__ == "__main__":
    main()
