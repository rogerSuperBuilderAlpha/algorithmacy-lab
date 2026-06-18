"""The bottleneck-symmetry thread, run end to end and deterministically.

The joint-bottleneck thread reported that the two members of a veto pair share the credit roughly evenly,
a within-set Shapley ratio averaging 0.78. That average hid two regimes. Cooperative game theory says two
players get equal Shapley exactly when they are interchangeable — the symmetry axiom. This thread tests the
veto pairs against that axiom and finds the sharing is bimodal: exactly equal when the pair is
interchangeable, and sharply unequal when it is not.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/bottleneck_symmetry/bottleneck_symmetry.py

Deterministic: fixed seed, fixed form count. Slow — veto pairs are rare, so many four-node forms are scanned.
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
FORMS = 600
N = 4
L = tuple("ABCD"[:N])
EPS = 1e-6


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def interchangeable(v, a, b, n):
    """True if swapping a and b never changes a coalition's worth: v(S+a) = v(S+b) for all S without
    a or b. The symmetry-axiom condition for equal Shapley value."""
    others = [x for x in range(n) if x not in (a, b)]
    for r in range(len(others) + 1):
        for S in itertools.combinations(others, r):
            if abs(v[frozenset(S + (a,))] - v[frozenset(S + (b,))]) > 1e-6:
                return False
    return True


def main():
    rng = random.Random(SEED)
    inter_ratios, non_ratios = [], []

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
        if len(vs) != 2:
            continue
        a, b = sorted(vs)
        sh = shapley(v, N)
        hi = max(abs(sh[a]), abs(sh[b]))
        if hi <= EPS:
            continue
        ratio = min(abs(sh[a]), abs(sh[b])) / hi
        (inter_ratios if interchangeable(v, a, b, N) else non_ratios).append(ratio)

    J = len(inter_ratios) + len(non_ratios)
    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    print(f"four-party forms scanned: {FORMS}")
    print(f"veto-pair forms (bottleneck of exactly two parties): {J}")
    print()
    print("The within-set sharing is the symmetry axiom, and it is bimodal:")
    print(f"    interchangeable pairs: {pct(len(inter_ratios), J)}")
    print(f"    mean within-set Shapley ratio when interchangeable:     {np.mean(inter_ratios):.3f}")
    print(f"    mean within-set Shapley ratio when not interchangeable: {np.mean(non_ratios):.3f}")
    print()
    print(f"    (the joint-bottleneck thread's 0.78 average was a blend of these two regimes)")


if __name__ == "__main__":
    main()
