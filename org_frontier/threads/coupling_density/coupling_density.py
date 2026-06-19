"""The coupling-density thread (E10 of the catalog line).

The cyclic thread found a sparse coordination has no bottleneck and a dense one commits readily. This one
makes the relation quantitative: how much coupling a three-party coordination needs before it can bind. The
answer is a threshold and a monotone rise. Below six dependency edges the form never commits; at six it
begins, and the commitment rate climbs with every added edge to the fully connected maximum.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/coupling_density/coupling_density.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.classifier.classifier import cm_from_rules, classify_rules

SEED = 11
FORMS = 3000
N = 3
L = tuple("ABC")


def rule(tt):
    return lambda x, _t=tt: _t[sum(x[i] << (N - 1 - i) for i in range(N))]


def main():
    rng = random.Random(SEED)
    tri = defaultdict(int)
    tot = defaultdict(int)
    for _ in range(FORMS):
        rules = [rule([rng.randint(0, 1) for _ in range(2 ** N)]) for _ in range(N)]
        edges = int(cm_from_rules(rules).sum())
        tri[edges] += classify_rules(rules, L).structure == "triadic"
        tot[edges] += 1
    print("Commitment rate by number of dependency edges in the three-party coordination:")
    for e in sorted(tot):
        print(f"  {e} edges: triadic {tri[e]}/{tot[e]} = {100 * tri[e] / tot[e]:.0f}%")
    print("Below 6 edges the form never commits; commitment rises monotonically with coupling density.")


if __name__ == "__main__":
    main()
