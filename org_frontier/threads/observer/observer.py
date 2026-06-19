"""The observer thread (E4 of the catalog line).

A coordination often has an audience: a party that watches but is not watched, reads the others but is read
by none. This thread asks whether an observer is part of the coordination's core. It is not. A party with
inputs and no outputs has no causal effect, so it cannot enter the major complex however much it reads. A
party joins the core only when it is read as well as reads — when it acts, not only watches.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/observer/observer.py

Deterministic: fixed seed, fixed form count.
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
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 400
N = 4
L = tuple("WSCP")   # P = node 3, the fourth party


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    usable = s_veto = integ = p_in_core = 0
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if 1 in veto_set(W):
                s_veto += 1
        _, core, _ = complex_over_states(net, tpm, N)
        if core is not None:
            usable += 1
            if 3 in core:
                p_in_core += 1
    print(f"{name}: usable={usable} S-veto|integrating={s_veto}/{integ} "
          f"P-in-major-complex={p_in_core}/{usable}")


def main():
    print("The fourth party P, around the W-S-C triad. Does it join the core?")
    run("P observes S (reads S, read by none) ", {0: [1], 1: [0, 2], 2: [1], 3: [1]})
    run("P acts on C (reads S, and C reads P) ", {0: [1], 1: [0, 2], 2: [1, 3], 3: [1]})


if __name__ == "__main__":
    main()
