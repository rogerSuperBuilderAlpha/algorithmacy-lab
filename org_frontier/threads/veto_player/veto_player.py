"""The veto-player thread, run end to end and deterministically.

The Shapley thread found that the mediator carries the largest Shapley value but did not say why. A
classical fact about cooperative games answers it: a veto player — a party in every winning coalition —
carries the maximal Shapley value. This thread shows the mediator is that veto player, and that being one
is necessary but not sufficient for committing an irreducible determination.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/veto_player/veto_player.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set, is_hub
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.shapley_membership._harness import coalition_values, shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 400
N = 3
L = tuple("ABC"[:N])


def random_rules(n, rng):
    return [(lambda x, t=[rng.randint(0, 1) for _ in range(2 ** n)]:
             t[sum(x[i] << (n - 1 - i) for i in range(n))]) for _ in range(n)]


def main():
    rng = random.Random(SEED)
    n_bottleneck = 0
    veto_is_shapley_argmax = 0
    veto_shapley_positive = 0
    triadic = dyadic = 0
    dyadic_is_hub = 0
    in_major_complex = 0

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        winners = integrating_coalitions(net, tpm, N)
        vset = veto_set(winners)
        if len(vset) != 1:
            continue  # single-bottleneck forms only

        n_bottleneck += 1
        m = next(iter(vset))

        v, _, _ = coalition_values(list(rules), L)
        sh = shapley(v, N)
        veto_is_shapley_argmax += (max(range(N), key=lambda i: sh[i]) == m)
        veto_shapley_positive += (sh[m] > 0)

        if classify_rules(list(rules), L).structure == "triadic":
            triadic += 1
        else:
            dyadic += 1
            dyadic_is_hub += is_hub(winners, m, N)

        _, core, _ = complex_over_states(net, tpm, N)
        in_major_complex += (core is not None and m in core)

    print(f"single-bottleneck forms (one veto player): {n_bottleneck}/{FORMS}")
    print()
    print("The veto player is the Shapley-dominant party:")
    print(f"    veto player == argmax-Shapley party: {veto_is_shapley_argmax}/{n_bottleneck} "
          f"= {100 * veto_is_shapley_argmax / n_bottleneck:.1f}%")
    print(f"    veto player has positive Shapley:    {veto_shapley_positive}/{n_bottleneck} "
          f"= {100 * veto_shapley_positive / n_bottleneck:.1f}%")
    print()
    print("A veto player is necessary but not sufficient for an irreducible determination:")
    print(f"    triadic (commits a determination): {triadic}/{n_bottleneck} "
          f"= {100 * triadic / n_bottleneck:.1f}%")
    print(f"    dyadic  (a hub that conveys):       {dyadic}/{n_bottleneck} "
          f"= {100 * dyadic / n_bottleneck:.1f}%")
    print(f"    every dyadic bottleneck is a two-dyad hub: {dyadic_is_hub}/{dyadic}")
    print()
    print(f"veto player sits in the major complex: {in_major_complex}/{n_bottleneck} "
          f"= {100 * in_major_complex / n_bottleneck:.1f}%")


if __name__ == "__main__":
    main()
