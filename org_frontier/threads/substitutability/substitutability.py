"""The substitutability thread (E8 of the catalog line).

A platform connects two workers to a counterpart. Whether the workers are a team or a pool decides whether
the coordination binds. When the platform needs both workers jointly — a team — the whole commits and both
workers enter the core. When either worker suffices — a pool — the whole never commits: the redundant worker
makes the system factor, and substitutability is the enemy of integration. The platform is the bottleneck
either way.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/substitutability/substitutability.py

Deterministic: fixed seed, fixed form count.
"""

import itertools
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 400
N = 4
L = tuple("ABSC")   # A=0, B=1 workers; S=2 platform; C=3 counterpart
EPS = 1e-6
GATES = {
    "team (platform needs both: S=A&B&C)": lambda x: x[0] & x[1] & x[3],
    "pool (either suffices:    S=(A|B)&C)": lambda x: (x[0] | x[1]) & x[3],
}


def interchangeable(v, a, b):
    others = [x for x in range(N) if x not in (a, b)]
    for r in range(len(others) + 1):
        for combo in itertools.combinations(others, r):
            if abs(v.get(frozenset(combo + (a,)), 0) - v.get(frozenset(combo + (b,)), 0)) > 1e-6:
                return False
    return True


def run(name, gate):
    rng = random.Random(SEED)
    tri = integ = s_veto = both_in_core = inter = 0
    for _ in range(FORMS):
        rules = [_rule_of_one(rng.randint(0, 3), 2), _rule_of_one(rng.randint(0, 3), 2),
                 gate, _rule_of_one(rng.randint(0, 3), 2)]
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if 2 in veto_set(W):
                s_veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
            _, core, _ = complex_over_states(net, tpm, N)
            if core is not None and {0, 1} <= core:
                both_in_core += 1
            inter += interchangeable(v, 0, 1)
    print(f"{name}: triadic={tri}/{FORMS} S-veto|integrating={s_veto}/{integ} "
          f"both-workers-in-core={both_in_core}/{tri} workers-interchangeable={inter}/{tri}")


def main():
    print("Team vs pool: two workers, one platform, one counterpart.")
    for name, gate in GATES.items():
        run(name, gate)


if __name__ == "__main__":
    main()
