"""The core-stability thread, run end to end and deterministically.

The subadditivity thread showed integration does not aggregate: a tight pair often out-values the whole.
This thread reads that on the allocation side. If a coalition is worth more than the whole that contains
it, no division of the whole's worth can keep that coalition in, and the core is empty — there is no stable
way to share the credit for a coordination's integration.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/core_stability/core_stability.py

Deterministic: fixed seed, fixed form count.
"""

import itertools
import math
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.core_stability._harness import core_nonempty, shapley_in_core, g, EPS
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.coalition_structure._harness import network

SEED = 11
FORMS = 300
N = 3
L = tuple("ABC"[:N])


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def shapley(v, n):
    out = []
    for i in range(n):
        others = [j for j in range(n) if j != i]
        tot = 0.0
        for r in range(len(others) + 1):
            for S in itertools.combinations(others, r):
                w = math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)
                tot += w * (g(v, S + (i,)) - g(v, S))
        out.append(tot)
    return out


def main():
    rng = random.Random(SEED)
    core_ne = shap_in = 0
    dil = dil_core = nodil = nodil_core = 0
    veto = veto_core = 0

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)

        cne = core_nonempty(v, N)
        core_ne += cne
        shap_in += shapley_in_core(shapley(v, N), v, N)

        whole = v[frozenset(range(N))]
        best_pair = max(v[frozenset(S)] for S in itertools.combinations(range(N), 2))
        if whole < best_pair - EPS:
            dil += 1
            dil_core += cne
        else:
            nodil += 1
            nodil_core += cne

        if len(veto_set(integrating_coalitions(net, tpm, N))) >= 1:
            veto += 1
            veto_core += cne

    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    print(f"forms: {FORMS}")
    print()
    print("A stable division of the integration credit rarely exists:")
    print(f"    core non-empty (a stable allocation exists): {pct(core_ne, FORMS)}")
    print(f"    Shapley value lies in the core:              {pct(shap_in, FORMS)}")
    print()
    print("Subadditive dilution is what empties the core:")
    print(f"    dilution forms (v(N) < best pair), core non-empty:    {pct(dil_core, dil)}")
    print(f"    no-dilution forms (v(N) >= best pair), core non-empty: {pct(nodil_core, nodil)}")
    print()
    print("A bottleneck confers power, not stability:")
    print(f"    veto-player forms with a non-empty core: {pct(veto_core, veto)}")


if __name__ == "__main__":
    main()
