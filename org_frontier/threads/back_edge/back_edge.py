"""The back-edge thread, run end to end and deterministically.

The designed-mediator thread wired one architecture — a bidirectional star, where the mediator reads the
outer parties and they read it back — and found that wiring buys the mediator its position but not its
power. It left three wirings open: a chain, a mediator without back-edges, and four parties. This thread
runs them. The answer isolates what earns the power: the back-edge. Forward-only mediators — a broadcast
with no return, a feedforward chain — produce no integration at all, so they only convey. The bidirectional
star generalizes to four parties: the hub recovers its position, commitment stays rare, and the credit is
shared among the parties it binds.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/back_edge/back_edge.py

Deterministic: fixed seed, fixed form count. Slow.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
M = 1  # the wired mediator is node index 1 (B)
EPS = 1e-6


def build(arch, rng, n):
    rules = [None] * n
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch, n, forms):
    rng = random.Random(SEED)
    L = tuple("ABCD"[:n])
    tri = integ = veto = complex_tri = 0
    shares = []
    for _ in range(forms):
        rules = build(arch, rng, n)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, n)
        W = integrating_coalitions(net, tpm, n)
        if W:
            integ += 1
            if M in veto_set(W):
                veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            _, core, _ = complex_over_states(net, tpm, n)
            if core is not None and M in core:
                complex_tri += 1
            total = sum(shapley(v, n))
            if total > EPS:
                shares.append(shapley(v, n)[M] / total)
    share = f"{np.mean(shares):.3f}" if shares else "n/a"
    print(f"{name}: forms={forms} integrating={integ} triadic={tri} "
          f"veto|integrating={veto}/{integ} complex|triadic={complex_tri}/{tri} "
          f"B-share|triadic={share} (equal={1/n:.3f})")


def main():
    print("Mediator B = node 1. Forward-only wirings convey; the back-edge commits.")
    run("bidirectional star (back-edge)", {0: [1], 1: [0, 2], 2: [1]}, 3, 400)
    run("broadcast (no back-edge)       ", {0: [1], 1: [1], 2: [1]}, 3, 400)
    run("chain A->B->C                  ", {0: [0], 1: [0], 2: [1]}, 3, 400)
    run("four-party star (back-edge)    ", {0: [1], 1: [0, 2, 3], 2: [1], 3: [1]}, 4, 250)


if __name__ == "__main__":
    main()
