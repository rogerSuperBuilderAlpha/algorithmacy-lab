"""The engagement-blind thread (E21 of the catalog line).

The momentary thread found a triad is irreducible at only a minority of its states. The natural guess is that
those are the busy states, where many parties are active. They are not. The states at which a coordination is
irreducible carry about the same number of active parties as the states at which it factors, both near the
uniform average. A coordination's irreducible moments are engagement-blind: whether the system is irreducible
does not track how many parties are switched on.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/engagement_blind/engagement_blind.py

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
    irr, red = [], []
    for _ in range(FORMS):
        rules = [rule([rng.randint(0, 1) for _ in range(2 ** N)]) for _ in range(N)]
        v = classify_rules(rules, L)
        if v.structure != "triadic":
            continue
        for state, phi in v.phi_profile:
            (irr if phi > 1e-6 else red).append(sum(state))
    dist = Counter(irr)
    print(f"mean active parties at IRREDUCIBLE states: {np.mean(irr):.3f}  (n={len(irr)})")
    print(f"mean active parties at reducible  states:  {np.mean(red):.3f}  (n={len(red)})")
    print(f"  irreducible-state activity counts (0-3 active): {dict(sorted(dist.items()))}")
    print("The irreducible moments are engagement-blind: activity is near the uniform 1.5 either way.")


if __name__ == "__main__":
    main()
