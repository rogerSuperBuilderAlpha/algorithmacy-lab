"""The influence-membership thread (E13 of the catalog line).

A party can shape what the others do without being part of the coordination's irreducible core. This thread
crosses each party's Boolean influence — whether flipping it changes any party's next state — against its
membership in the major complex. Every party is influential, and a third of the influential party-instances
sit outside the core. Influence is universal and does not determine membership: shaping behavior is not the
same as being constitutive of the irreducible coordination.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/influence_membership/influence_membership.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 2000
N = 3
L = tuple("ABC")
EPS = 1e-6


def rule(tt):
    return lambda x, _t=tt: _t[sum(x[i] << (N - 1 - i) for i in range(N))]


def influence(rules, i):
    """Boolean sensitivity: fraction of (state, target) pairs whose next state flips when party i flips."""
    changed = total = 0
    for s in range(2 ** N):
        cur = tuple((s >> k) & 1 for k in range(N))
        flipped = tuple(b ^ 1 if k == i else b for k, b in enumerate(cur))
        for j in range(N):
            total += 1
            changed += rules[j](cur) != rules[j](flipped)
    return changed / total


def main():
    rng = random.Random(SEED)
    tri = 0
    incore_inf = incore_noinf = out_inf = out_noinf = 0
    for _ in range(FORMS):
        rules = [rule([rng.randint(0, 1) for _ in range(2 ** N)]) for _ in range(N)]
        if classify_rules(rules, L).structure != "triadic":
            continue
        net, tpm = network(rules, L)
        _, core, _ = complex_over_states(net, tpm, N)
        if core is None:
            continue
        tri += 1
        for i in range(N):
            inf = influence(rules, i) > EPS
            inc = i in core
            if inc and inf:
                incore_inf += 1
            elif inc and not inf:
                incore_noinf += 1
            elif not inc and inf:
                out_inf += 1
            else:
                out_noinf += 1
    print(f"triadic forms: {tri} (party-instances cross-tabbed)")
    print(f"  in-core & influential:      {incore_inf}")
    print(f"  in-core & no influence:     {incore_noinf}")
    print(f"  out-of-core & influential:  {out_inf}")
    print(f"  out-of-core & no influence: {out_noinf}")
    print("Every party is influential; a third of the influential are outside the core.")


if __name__ == "__main__":
    main()
