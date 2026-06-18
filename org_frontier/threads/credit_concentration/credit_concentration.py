"""The credit-concentration thread, run end to end and deterministically.

The Shapley value pays each party its average marginal contribution to v(S) = φ_s(S). In a triadic form,
how is that credit spread? It concentrates on one party, and how much depends on who the exclusion postulate
keeps: when every party is in the major complex the credit is shared, and when exclusion drops a party the
credit goes winner-take-all and the excluded party's share turns negative.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/credit_concentration/credit_concentration.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.credit_concentration._harness import shapley, gini, EPS
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 300
N = 3
L = tuple("ABC"[:N])


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    tri = gt5 = gt9 = 0
    top_shares, ginis = [], []
    full_shares, sub_shares = [], []
    sub_forms = sub_excluded_negative = 0

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        whole = v[frozenset(range(N))]
        if classify_rules(list(rules), L).structure != "triadic" or whole <= EPS:
            continue

        sh = shapley(v, N)
        total = sum(sh)
        if total <= EPS:
            continue
        tri += 1
        share = max(sh) / total
        top_shares.append(share)
        gt5 += share > 0.5
        gt9 += share > 0.9
        ginis.append(gini(sh))

        _, core, _ = complex_over_states(net, tpm, N)
        if core is None:
            continue
        if len(core) == N:
            full_shares.append(share)
        else:
            sub_shares.append(share)
            sub_forms += 1
            if any(sh[i] < -EPS for i in range(N) if i not in core):
                sub_excluded_negative += 1

    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    print(f"triadic forms with v(N) > 0: {tri}")
    print()
    print("The integration credit concentrates on one party:")
    print(f"    mean top-party Shapley share: {np.mean(top_shares):.3f}")
    print(f"    top party holds a majority (> 50%): {pct(gt5, len(top_shares))}")
    print(f"    top party holds almost all (> 90%): {pct(gt9, len(top_shares))}")
    print(f"    mean Gini of the credit (0 equal, 1 concentrated): {np.mean(ginis):.3f}")
    print()
    print("Concentration tracks exclusion:")
    print(f"    full triads (|core| = 3), mean top share: {np.mean(full_shares):.3f}  (n={len(full_shares)})")
    print(f"    sub  triads (|core| < 3), mean top share: {np.mean(sub_shares):.3f}  (n={len(sub_shares)})")
    print(f"    sub triads where an excluded party has negative Shapley: {pct(sub_excluded_negative, sub_forms)}")


if __name__ == "__main__":
    main()
