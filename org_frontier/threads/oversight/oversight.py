"""The oversight thread (E7 of the catalog line).

Add a principal over the mediator — a regulator, an owner, a board — coupled to it both ways, and ask what
oversight does to the coordination. It does not break the mediator's bottleneck. The mediator stays the veto
player in every integrating form. The principal joins the core, becomes a co-bottleneck in some forms, and
takes a substantial share of the credit, while the mediator's own share rises and the two parties are
squeezed toward nothing. Oversight joins the top of the arrangement; it does not redistribute to the parties.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/oversight/oversight.py

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

SEED = 11
FORMS = 400
N = 4
L = tuple("WSCP")   # W=0, S=1 (mediator), C=2, P=3 (principal)
EPS = 1e-6


def build(arch, rng):
    rules = [None] * N
    for node, inputs in arch.items():
        rules[node] = (_rule_of_one(rng.randint(0, 3), inputs[0]) if len(inputs) == 1
                       else _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(inputs))], inputs))
    return rules


def run(name, arch):
    rng = random.Random(SEED)
    usable = integ = s_veto = p_veto = p_in_core = 0
    s_share, p_share = [], []
    for _ in range(FORMS):
        rules = build(arch, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            vs = veto_set(W)
            s_veto += 1 in vs
            p_veto += 3 in vs
        _, core, _ = complex_over_states(net, tpm, N)
        if core is not None:
            usable += 1
            p_in_core += 3 in core
            sh = shapley(v, N)
            total = sum(sh)
            if total > EPS:
                s_share.append(sh[1] / total)
                p_share.append(sh[3] / total)
    ss = f"{np.mean(s_share):.3f}" if s_share else "n/a"
    ps = f"{np.mean(p_share):.3f}" if p_share else "n/a"
    print(f"{name}: S-veto={s_veto}/{integ} P-veto={p_veto}/{integ} "
          f"P-in-core={p_in_core}/{usable} S-share={ss} P-share={ps}")


def main():
    print("A principal P over the mediator S. Does oversight break the bottleneck or join the top?")
    run("no oversight (P only observes S)     ", {0: [1], 1: [0, 2], 2: [1], 3: [1]})
    run("oversight (S heeds P; P<->S coupled) ", {0: [1], 1: [0, 2, 3], 2: [1], 3: [1, 3]})


if __name__ == "__main__":
    main()
