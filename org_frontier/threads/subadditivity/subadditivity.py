"""The subadditivity thread, run end to end and deterministically.

Question. "The whole is more than the sum of its parts" is the slogan integrated information is supposed
to make precise. As a cooperative game v(S) = φ_s(S), that slogan is superadditivity. Does the integration
game have it? It does not, and saying what holds instead sharpens the slogan.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/subadditivity/subadditivity.py

Deterministic: fixed seed, fixed form count.
"""

import itertools
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.subadditivity._harness import (
    value_function, has_subadditive_split, is_superadditive, is_non_monotone, EPS,
)
from org_frontier.threads.coalition_structure._harness import network, complex_over_states

SEED = 11
FORMS = 300
N = 3
L = tuple("ABC"[:N])


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    subadditive = superadditive = non_monotone = 0
    synergy_bottom = dilution_top = 0
    dilution_and_proper = 0
    gaps = []

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)

        subadditive += has_subadditive_split(v, N)
        superadditive += is_superadditive(v, N)
        non_monotone += is_non_monotone(v, N)

        pairs = [v[frozenset(S)] for S in itertools.combinations(range(N), 2)]
        whole = v[frozenset(range(N))]
        best_pair = max(pairs)

        if best_pair > EPS:
            synergy_bottom += 1
        if whole < best_pair - EPS:
            dilution_top += 1
            gaps.append(best_pair - whole)
            _, core, _ = complex_over_states(net, tpm, N)
            if core is not None and len(core) < N:
                dilution_and_proper += 1

    pct = lambda a: f"{a}/{FORMS} = {100 * a / FORMS:.1f}%"
    print(f"forms: {FORMS}")
    print()
    print("Integration does not aggregate — the game v(S) = phi_s(S) is not superadditive:")
    print(f"    forms with a subadditive split (whole < parts): {pct(subadditive)}")
    print(f"    forms that are superadditive everywhere:        {pct(superadditive)}")
    print(f"    non-monotone forms (a party lowers phi_s):      {pct(non_monotone)}")
    print()
    print("What holds instead is a dual edge structure:")
    print(f"    synergy at the bottom (two non-integrating parties make an integrating dyad): {pct(synergy_bottom)}")
    print(f"    dilution at the top (phi_s(whole) < best pair):                               {pct(dilution_top)}")
    if gaps:
        print(f"    mean dilution gap (best_pair - whole) when it bites: {sum(gaps) / len(gaps):.3f}")
    print(f"    dilution coincides with a proper-subset major complex (exclusion): "
          f"{dilution_and_proper}/{dilution_top} = {100 * dilution_and_proper / dilution_top:.1f}%")


if __name__ == "__main__":
    main()
