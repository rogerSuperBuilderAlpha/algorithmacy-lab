"""The momentary thread (E20 of the catalog line).

Being a triadic coordination does not mean being irreducible all the time. The verdict is read at the one
state where Φ is largest, but a coordination passes through many states, and at most of them it is not
irreducible. On average a triad is irreducible at only about a third of its reachable states, and half of all
triads are irreducible at just one configuration. Coordination is momentary: the irreducible determination is
committed at some moments and not others. This qualifies every other prior in the catalog — the bottleneck
and credit findings describe the states where the coordination is irreducible, which are a minority.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/momentary/momentary.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 3000
N = 3
L = tuple("ABC")


def rule(tt):
    return lambda x, _t=tt: _t[sum(x[i] << (N - 1 - i) for i in range(N))]


def main():
    rng = random.Random(SEED)
    tri = one_only = 0
    fracs = []
    dist = Counter()
    for _ in range(FORMS):
        rules = [rule([rng.randint(0, 1) for _ in range(2 ** N)]) for _ in range(N)]
        v = classify_rules(rules, L)
        if v.structure != "triadic":
            continue
        tri += 1
        fracs.append(v.n_states_irreducible / v.n_states_evaluated)
        dist[v.n_states_irreducible] += 1
        if v.n_states_irreducible == 1:
            one_only += 1
    print(f"triadic forms: {tri}")
    print(f"  mean fraction of reachable states that are irreducible: {np.mean(fracs):.3f}")
    print(f"  irreducible at only ONE state: {one_only}/{tri} = {100 * one_only / tri:.0f}%")
    print(f"  states-irreducible distribution: {dict(sorted(dist.items()))}")
    print("Coordination is momentary: a triad is irreducible at a minority of its states.")


if __name__ == "__main__":
    main()
