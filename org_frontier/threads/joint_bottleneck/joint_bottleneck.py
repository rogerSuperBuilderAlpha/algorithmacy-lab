"""The joint-bottleneck thread, run end to end and deterministically.

The four-party thread found a structure three parties cannot show: a bottleneck that is a set of parties,
all of them in every integrating coalition. This thread studies how the credit is structured inside such a
set. At three parties a single bottleneck took almost all the Shapley credit, winner-take-all. A joint
bottleneck instead shares the credit roughly evenly among its members while still shutting outsiders out.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/joint_bottleneck/joint_bottleneck.py

Deterministic: fixed seed, fixed form count. Slow — joint bottlenecks are rare, so many four-node forms are
scanned to collect them.
"""

import itertools
import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.credit_concentration._harness import shapley

SEED = 11
FORMS = 400
N = 4
L = tuple("ABCD"[:N])
EPS = 1e-6


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    joint = []  # (members, shapley) for forms whose veto set has >= 2 parties

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        winners = [frozenset(S) for r in range(2, N + 1) for S in itertools.combinations(range(N), r)
                   if v[frozenset(S)] > EPS]
        if not winners:
            continue
        vs = set(winners[0])
        for w in winners[1:]:
            vs &= set(w)
        if len(vs) >= 2:
            joint.append((sorted(vs), shapley(v, N)))

    J = len(joint)
    members_top = members_positive = outsiders_nonpositive = 0
    share_ratios = []
    for members, sh in joint:
        order = sorted(range(N), key=lambda i: -sh[i])
        if set(order[:len(members)]) == set(members):
            members_top += 1
        mvals = [sh[i] for i in members]
        if all(m > 0 for m in mvals):
            members_positive += 1
        if all(sh[i] <= EPS for i in range(N) if i not in members):
            outsiders_nonpositive += 1
        a = sorted(abs(m) for m in mvals)
        if a[-1] > EPS:
            share_ratios.append(a[0] / a[-1])  # min/max within set: 1 = perfectly shared

    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    print(f"four-party forms scanned: {FORMS}")
    print(f"forms with a joint bottleneck (veto set >= 2 parties): {J}")
    print()
    print("The credit concentrates on the bottleneck set:")
    print(f"    bottleneck members are the top Shapley parties: {pct(members_top, J)}")
    print(f"    every bottleneck member has positive Shapley:   {pct(members_positive, J)}")
    print(f"    every outsider has non-positive Shapley:        {pct(outsiders_nonpositive, J)}")
    print()
    print("Inside the set the credit is shared, not winner-take-all:")
    print(f"    mean within-set Shapley ratio (min/max, 1 = equal): {np.mean(share_ratios):.3f}")
    print(f"    lowest within-set ratio seen (most unequal):        {min(share_ratios):.3f}")


if __name__ == "__main__":
    main()
