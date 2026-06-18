"""The normalization thread, run end to end and deterministically.

Critics of integrated information say Φ should be normalized by system size before systems are compared.
IIT keeps absolute φ_s: the major complex is the subset of largest φ_s, not largest φ_s per element. This
thread measures what normalizing would do to the major complex. It collapses it to a single party in almost
every form — so absolute φ_s is what gives IIT a multi-party core at all.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/normalization/normalization.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.normalization._harness import density_argmax
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
    usable = 0
    density_singleton = 0
    complex_sizes, density_sizes = [], []
    triadic = triadic_density_singleton = 0
    multiparty_complex = density_shrinks = 0

    for _ in range(FORMS):
        rules = random_rules(N, rng)
        net, tpm = network(rules, L)
        v = value_function(net, tpm, N)
        _, core, _ = complex_over_states(net, tpm, N)
        if core is None:
            continue
        usable += 1

        d_all = density_argmax(v, N, min_size=1)
        complex_sizes.append(len(core))
        density_sizes.append(len(d_all))
        if len(d_all) == 1:
            density_singleton += 1

        is_tri = classify_rules(list(rules), L).structure == "triadic"
        if is_tri:
            triadic += 1
            if len(d_all) == 1:
                triadic_density_singleton += 1

        if len(core) >= 2:
            multiparty_complex += 1
            d_coord = density_argmax(v, N, min_size=2)
            if len(d_coord) < len(core):
                density_shrinks += 1

    pct = lambda a, b: f"{a}/{b} = {100 * a / b:.1f}%"
    mean = lambda xs: sum(xs) / len(xs)
    print(f"usable forms: {usable}/{FORMS}")
    print()
    print("Normalizing exclusion (max phi_s per element) collapses the core to one party:")
    print(f"    density-maximal subset is a single party: {pct(density_singleton, usable)}")
    print(f"    mean size — absolute major complex: {mean(complex_sizes):.2f} | density-maximal: {mean(density_sizes):.2f}")
    print()
    print("It also mis-reads multi-party coordinations:")
    print(f"    triadic forms whose density-maximal subset is a lone party: {pct(triadic_density_singleton, triadic)}")
    print(f"    multi-party complexes that density shrinks (over size>=2): {pct(density_shrinks, multiparty_complex)}")


if __name__ == "__main__":
    main()
