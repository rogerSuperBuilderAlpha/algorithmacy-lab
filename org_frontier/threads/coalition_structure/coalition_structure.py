"""The coalition-structure thread, run end to end and deterministically.

Question. The Shapley thread predicts major-complex membership at AUC ~0.87, not 1.0. Why the ceiling?
Reading the exclusion postulate as cooperative game theory answers it.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/coalition_structure/coalition_structure.py

Deterministic: fixed seed, fixed form count. The printed headline numbers are the ones the CI gate and
the writeup quote.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.coalition_structure._harness import (
    network, complex_over_states, argmax_subsets_at, node_marginal_auc_at,
    optimal_structure, condensation, auc,
)

SEED = 11
FORMS = 150
N = 3


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    marginal_pairs = []
    unique_match = tie_match = setlevel_correct = setlevel_total = 0
    cond_eq_opt = 0
    usable = 0

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, tuple("ABC"[:N]))

        s_star, core, _ = complex_over_states(net, tpm, N)
        if core is None:
            continue
        usable += 1

        vals, _, argmaxes = argmax_subsets_at(net, s_star, N)
        unique_argmax = max(vals, key=lambda S: (vals[S], -len(S)))  # deterministic tie-break
        unique_match += (unique_argmax == core)
        tie_match += (core in argmaxes)

        # Set-level membership predictor: a node is in the core iff it is in the (tie-broken) argmax
        # coalition. Contrast its per-node accuracy with the node-level marginal AUC below.
        for i in range(N):
            setlevel_correct += ((i in unique_argmax) == (i in core))
            setlevel_total += 1

        node_marginal_auc_at(net, s_star, N, core, marginal_pairs)

        cond_eq_opt += (condensation(net, tpm, N) == optimal_structure(net, tpm, N))

    print(f"forms with a defined major complex: {usable}/{FORMS}")
    print()
    print("Q8  node-level marginal predictor (best-with-i minus best-without-i at s*):")
    print(f"    AUC(score -> in major complex) = {auc(marginal_pairs):.3f}   (Shapley reached 0.87)")
    print()
    print("Q10 the major complex IS the maximally integrated coalition argmax_S phi_s(S) at s*:")
    print(f"    complex == unique argmax (deterministic tie-break): {unique_match}/{usable} "
          f"= {100 * unique_match / usable:.1f}%")
    print(f"    complex in argmax set (tie-tolerant):               {tie_match}/{usable} "
          f"= {100 * tie_match / usable:.1f}%")
    print()
    print("    set-level membership predictor (node in core iff in argmax coalition):")
    print(f"    per-node accuracy = {setlevel_correct}/{setlevel_total} "
          f"= {100 * setlevel_correct / setlevel_total:.1f}%")
    print()
    print("Q9  IIT condensation (greedy peel of maximal complex) == optimal coalition structure:")
    print(f"    {cond_eq_opt}/{usable} = {100 * cond_eq_opt / usable:.1f}%")


if __name__ == "__main__":
    main()
