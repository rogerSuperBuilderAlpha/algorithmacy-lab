"""The engagement thread, run end to end and deterministically.

A prior for the catalog. The back-edge thread showed a mediator commits only when the parties feed back to it.
This one asks the dual question about a party: what binds a party into a mediated coordination. The answer is
coupling, not the direction of a particular edge. A party is bound when it is coupled to the rest — when it
heeds the mediator, or when it reads the other party — and a party coupled to neither cannot be bound, which
collapses the triad to the engaged dyad. A party that does not heed the mediator can still be a member, as
long as it is coupled to the coordination some other way.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/engagement/engagement.py

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
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 600
N = 3
S = 1   # the mediator
C = 2   # the party whose coupling is varied (W = 0 always heeds S)
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
    tri = integ = veto = c_in_core = 0
    shares = []
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if S in veto_set(W):
                veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            total = sum(shapley(v, N))
            if total > EPS:
                shares.append(shapley(v, N)[S] / total)
            _, core, _ = complex_over_states(net, tpm, N)
            if core is not None and C in core:
                c_in_core += 1
    share = f"{np.mean(shares):.3f}" if shares else "n/a  "
    print(f"{name}: triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) "
          f"S-veto|integrating={veto}/{integ}={100 * veto / max(integ, 1):.0f}% "
          f"S-share|triadic={share} C-in-core|triadic={c_in_core}/{tri}")


def main():
    print("What binds party C into the triad: S always reads both parties and W always heeds S; vary C.")
    run("C heeds S (bidirectional)        ", {0: [1], 1: [0, 2], 2: [1]})
    run("C autonomous (reads only itself) ", {0: [1], 1: [0, 2], 2: [2]})
    run("C reads W, not S (coupled to W)  ", {0: [1], 1: [0, 2], 2: [0]})


if __name__ == "__main__":
    main()
