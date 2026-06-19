"""The designed-mediator thread, run end to end and deterministically.

A committee objection to the cooperative-game program: every form was a random truth table, so "the mediator"
was a node labelled after the fact because it came out indispensable, not a designed architecture. This
thread answers it. It wires a mediator into the architecture and asks whether the cooperative-game structure
lands on it, and what wiring alone does and does not buy.

Three findings: the wired bottleneck is the cooperative-game veto player and major-complex member, by
construction; wiring a mediator is far from sufficient for the form to commit (be triadic); and when the
designed mediator does commit, it shares the credit rather than seizing it, because committing binds all the
parties. A symmetric control shows the membership recovery is the wiring, not an artifact.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/designed_mediator/designed_mediator.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import designed_mediator_rules, symmetric_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 1200
N = 3
M = 1  # the designed mediator is node index 1 (B)
L = tuple("ABC"[:N])
EPS = 1e-6


def main():
    rng = random.Random(SEED)
    tri = dya = integ = 0
    m_veto = 0
    m_complex_tri = m_complex_dya = 0
    m_shares = []

    for _ in range(FORMS):
        rules = designed_mediator_rules(rng, M, N)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)

        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if M in veto_set(W):
                m_veto += 1

        triadic = classify_rules(list(rules), L).structure == "triadic"
        _, core, _ = complex_over_states(net, tpm, N)
        in_core = core is not None and M in core
        if triadic:
            tri += 1
            m_complex_tri += in_core
            total = sum(shapley(v, N))
            if total > EPS:
                m_shares.append(shapley(v, N)[M] / total)
        else:
            dya += 1
            m_complex_dya += in_core

    # symmetric control: in-major-complex rate by position, to show no node is privileged
    rng2 = random.Random(SEED + 1)
    pos_in_core = [0, 0, 0]
    sym_tri = 0
    for _ in range(FORMS):
        rules = symmetric_rules(rng2, N)
        net, tpm = network(rules, L)
        if classify_rules(list(rules), L).structure == "triadic":
            sym_tri += 1
        _, core, _ = complex_over_states(net, tpm, N)
        if core is not None:
            for i in range(N):
                pos_in_core[i] += i in core

    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    print("=== designed mediator (B wired as the bottleneck) ===")
    print(f"wiring a mediator does not force commitment: triadic in {pct(tri, FORMS)}")
    print()
    print("position is recovered by construction:")
    print(f"    B is the veto player when anything integrates: {pct(m_veto, integ)}")
    print(f"    B is in the major complex when triadic: {pct(m_complex_tri, tri)}")
    print(f"    B is in the major complex when dyadic:  {pct(m_complex_dya, dya)}")
    print()
    print("a committing mediator shares the credit, it does not seize it:")
    print(f"    B's mean Shapley share when triadic: {np.mean(m_shares):.3f}  (equal split = {1/N:.3f})")
    print()
    print("=== symmetric control (no wired mediator) ===")
    print(f"    in-major-complex rate by position: "
          f"A={100*pos_in_core[0]/FORMS:.0f}% B={100*pos_in_core[1]/FORMS:.0f}% C={100*pos_in_core[2]/FORMS:.0f}%"
          f"  (no position privileged)")


if __name__ == "__main__":
    main()
