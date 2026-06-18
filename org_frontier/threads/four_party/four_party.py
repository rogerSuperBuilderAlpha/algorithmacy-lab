"""The four-party thread, run end to end and deterministically.

Every cooperative-game thread so far ran on three-party forms, where a bottleneck reads off a single
complement pair and the lattice of coalitions is small. This thread re-runs the load-bearing results on
four-party forms to see what generalizes and what is new. The structural laws hold; the new thing is a
bottleneck that is a set of parties rather than one.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/four_party/four_party.py

Deterministic: fixed seed, fixed form count. Slower than the three-party threads (four-node exact Φ).
"""

import itertools
import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.coalition_structure._harness import network, complex_over_states, phi_s_at
from org_frontier.threads.subadditivity._harness import value_function, has_subadditive_split
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.core_stability._harness import core_nonempty
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 50
N = 4
L = tuple("ABCD"[:N])


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    usable = 0
    argmax_tie = subadditive = core_ne = 0
    veto_sizes = {}
    single_veto = single_veto_shapley = 0
    top_shares = []

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)

        s_star, core, _ = complex_over_states(net, tpm, N)
        if core is None:
            continue
        usable += 1

        vals = {frozenset(S): phi_s_at(net, s_star, S)
                for r in range(1, N + 1) for S in itertools.combinations(range(N), r)}
        mx = max(vals.values())
        argmax_tie += core in {S for S, val in vals.items() if abs(val - mx) < 1e-6}

        subadditive += has_subadditive_split(v, N)
        core_ne += core_nonempty(v, N)

        vs = veto_set(integrating_coalitions(net, tpm, N))
        veto_sizes[len(vs)] = veto_sizes.get(len(vs), 0) + 1
        sh = shapley(v, N)
        if len(vs) == 1:
            single_veto += 1
            single_veto_shapley += max(range(N), key=lambda i: sh[i]) == next(iter(vs))

        whole = v[frozenset(range(N))]
        if classify_rules(list(rules), L).structure == "triadic" and whole > 1e-6:
            total = sum(sh)
            if total > 1e-6:
                top_shares.append(max(sh) / total)

    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    print(f"four-party forms with a defined major complex: {usable}/{FORMS}")
    print()
    print("The three-party structural laws hold at four parties:")
    print(f"    major complex in argmax set (tie-tolerant): {pct(argmax_tie, usable)}")
    print(f"    subadditive split exists:                   {pct(subadditive, usable)}")
    print(f"    core empty (no stable split):               {pct(usable - core_ne, usable)}")
    print(f"    single bottleneck is the Shapley-argmax party: {pct(single_veto_shapley, single_veto)}")
    print(f"    mean top-party Shapley share (irreducible forms): {np.mean(top_shares):.3f}")
    print()
    print("New at four parties — the bottleneck can be a set of parties:")
    print(f"    veto-set sizes (parties in every integrating coalition): {dict(sorted(veto_sizes.items()))}")
    joint = sum(c for k, c in veto_sizes.items() if k >= 2)
    print(f"    forms with a joint bottleneck (>=2 parties): {pct(joint, usable)}")


if __name__ == "__main__":
    main()
