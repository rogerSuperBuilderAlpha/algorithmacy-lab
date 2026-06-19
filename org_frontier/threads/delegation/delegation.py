"""The delegation thread (E15 of the catalog line).

A worker reaches the platform through an agent: a chain worker-agent-platform-counterpart, each pair coupled
both ways. The question is whether the worker keeps its place in the coordination or the agent takes it. The
agent takes it. In the delegated chain the agent sits in the major complex far more often than the worker it
acts for. Delegation moves standing from the worker to the agent who stands between it and the platform.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/delegation/delegation.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.threads.coalition_structure._harness import network, complex_over_states

SEED = 11
FORMS = 500
N = 4
L = tuple("WASC")   # W=0 worker, A=1 agent, S=2 platform, C=3 counterpart
ARCH = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}   # W<->A<->S<->C


def build(rng):
    rules = [None] * N
    for node, inputs in ARCH.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def main():
    rng = random.Random(SEED)
    usable = 0
    in_core = [0, 0, 0, 0]
    for _ in range(FORMS):
        rules = build(rng)
        net, tpm = network(rules, L)
        _, core, _ = complex_over_states(net, tpm, N)
        if core is not None:
            usable += 1
            for i in range(N):
                in_core[i] += i in core
    print("Delegation chain: worker <-> agent <-> platform <-> counterpart.")
    print(f"usable forms: {usable}")
    print(f"  worker     in major complex: {in_core[0]}/{usable}")
    print(f"  agent      in major complex: {in_core[1]}/{usable}")
    print(f"  platform   in major complex: {in_core[2]}/{usable}")
    print(f"  counterpart in major complex: {in_core[3]}/{usable}")
    print("The agent sits in the core more than the worker it acts for.")


if __name__ == "__main__":
    main()
