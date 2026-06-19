"""The structured-forms thread, run end to end and deterministically.

The committee that reviewed the cooperative-game synthesis pressed one objection above the rest: every
headline rate — the core empty in 96% of forms, φ_s subadditive in 99% — was a frequency over random Boolean
truth tables, not coordinations. A prior study, q122, found the value function well-behaved on the
structured forms the dissertation actually uses. This thread tests the two pathology rates — the empty core
and the dilution that empties it — on structured coordination forms, and they reverse. On the strict-
mediation mediated-triad family the core is non-empty in every triadic form and no pair out-values the
whole. The empty core is a property of the random sample, not of coordination.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/structured_forms/structured_forms.py

Deterministic: fixed seed, fixed form count, plus a fixed curated library.
"""

import itertools
import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.corpus import forms_library as lib
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.core_stability._harness import core_nonempty
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.threads.designed_mediator._harness import designed_mediator_rules
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 1200
N = 3
L = tuple("WSC")
EPS = 1e-6


def dilution(v):
    """True if some pair out-values the whole — the condition that empties the core."""
    whole = v[frozenset(range(N))]
    best_pair = max(v[frozenset(S)] for S in itertools.combinations(range(N), 2))
    return whole < best_pair - EPS


def measure(rules):
    net, tpm = network(rules, L)
    v = value_function(net, tpm, N)
    triadic = classify_rules(list(rules), L).structure == "triadic"
    sh = shapley(v, N)
    total = sum(sh)
    share = sh[1] / total if total > EPS else float("nan")  # node 1 = the mediator S
    return triadic, core_nonempty(v, N), dilution(v), share


def main():
    print("Random-form baselines (from the cluster): core empty in 96%, a pair out-values the whole in 66%.")
    print()
    print("=== structured mediated-triad family (strict mediation), triadic forms ===")
    rng = random.Random(SEED)
    tri = core_ne = dil = 0
    shares = []
    for _ in range(FORMS):
        triadic, cne, d, share = measure(designed_mediator_rules(rng, 1, N))
        if triadic:
            tri += 1
            core_ne += cne
            dil += d
            if not np.isnan(share):
                shares.append(share)
    print(f"    triadic forms: {tri}/{FORMS}")
    print(f"    core non-empty (a stable split exists): {core_ne}/{tri} = {100 * core_ne / tri:.1f}%")
    print(f"    a pair out-values the whole (dilution): {dil}/{tri} = {100 * dil / tri:.1f}%")
    print(f"    mediator mean credit share: {np.mean(shares):.3f}")
    print()
    print("=== curated, named coordination forms ===")
    tri_forms = [f for f in lib.FORMS if measure(f.rules)[0]]
    tri_core = sum(1 for f in tri_forms if measure(f.rules)[1])
    for f in tri_forms:
        _, cne, d, share = measure(f.rules)
        print(f"    {f.key:24s} core_nonempty={str(cne):5s} dilution={str(d):5s} S-share={share:.2f}")
    print(f"    curated triadic forms with a non-empty core: {tri_core}/{len(tri_forms)}")


if __name__ == "__main__":
    main()
