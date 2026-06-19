"""The gate-sensitivity thread (E22 of the catalog line).

The gate-logic thread found a parity mediator binds more readily than a monotone one. This thread gives the
variable behind that: how sensitive the mediator's gate is, how often flipping a party changes its output.
Across all sixteen two-input gates, commitment rises with sensitivity. A constant mediator, insensitive to
its parties, never binds them; a half-sensitive gate binds a few percent of forms; a fully sensitive parity
gate binds a quarter. A coordination's commitment scales with how much information its mediator transmits
about its parties.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/gate_sensitivity/gate_sensitivity.py

Deterministic: fixed seed, all sixteen gates.
"""

import itertools
import os
import random
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 300
N = 3
L = tuple("WSC")


def gate(tt):
    return lambda x, _t=tt: _t[(x[0] << 1) | x[2]]   # function of W (node 0) and C (node 2)


def sensitivity(tt):
    """Fraction of single-input flips that change the two-input gate's output."""
    changed = total = 0
    for a in range(2):
        for b in range(2):
            for bit in range(2):
                na, nb = (1 - a, b) if bit == 0 else (a, 1 - b)
                total += 1
                changed += tt[(a << 1) | b] != tt[(na << 1) | nb]
    return changed / total


def commit_rate(tt):
    rng = random.Random(SEED)
    g = gate(tt)
    tri = 0
    for _ in range(FORMS):
        rules = [_rule_of_one(rng.randint(0, 3), 1), g, _rule_of_one(rng.randint(0, 3), 1)]
        net, tpm = network(rules, L)
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
    return tri / FORMS


def main():
    rows = []
    for bits in itertools.product([0, 1], repeat=4):
        rows.append((sensitivity(list(bits)), commit_rate(list(bits))))
    grouped = defaultdict(list)
    for s, c in rows:
        grouped[round(s, 2)].append(c)
    print("Mediator gate sensitivity vs commitment rate (all sixteen two-input gates):")
    for s in sorted(grouped):
        print(f"  sensitivity={s:.2f}: mean commit={np.mean(grouped[s]):.3f}  (n_gates={len(grouped[s])})")
    ss = [r[0] for r in rows]
    cc = [r[1] for r in rows]
    print(f"  correlation(sensitivity, commit) = {np.corrcoef(ss, cc)[0, 1]:.3f}")


if __name__ == "__main__":
    main()
