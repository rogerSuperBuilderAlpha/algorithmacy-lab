"""The disintermediation thread, run end to end and deterministically.

A prior for the catalog. The designed-mediator and back-edge threads built a mediator and asked what makes it
commit. This one asks what unmakes its bottleneck: a direct channel between the parties, the structural form
of an outside option. The naive expectation is that any direct contact between the parties bypasses the
mediator. It does not. A one-way channel — one party reading the other — entrenches the mediator instead,
raising commitment and concentrating more credit on it. Only a symmetric two-way channel disintermediates,
stripping the mediator of its veto and its credit.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/disintermediation/disintermediation.py

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
M = 1  # the mediator S = node 1; parties W = 0, C = 2
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
            if M in veto_set(W):
                veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            total = sum(shapley(v, N))
            if total > EPS:
                shares.append(shapley(v, N)[M] / total)
    print(f"{name}: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) "
          f"S-veto|integrating={veto}/{integ}={100 * veto / max(integ, 1):.0f}% "
          f"S-share|triadic={np.mean(shares):.3f}")


def main():
    print("A direct W<->C channel is the structural outside option. One-way entrenches; two-way disintermediates.")
    run("no back-channel (strict mediator)", {0: [1], 1: [0, 2], 2: [1]})
    run("one-way back-channel (C reads W) ", {0: [1], 1: [0, 2], 2: [1, 0]})
    run("two-way back-channel (W<->C)     ", {0: [1, 2], 1: [0, 2], 2: [1, 0]})


if __name__ == "__main__":
    main()
