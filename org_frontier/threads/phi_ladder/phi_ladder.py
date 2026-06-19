"""The phi-ladder thread (E11 of the catalog line).

Integration does not take a continuum of values. Across random three-party coordinations the integrated
information of the committing forms clusters on a short ladder of recurring values, with gaps between the
rungs. Ninety percent of triadic forms sit on one of four values — 0.415, 0.830, 1.000, 2.000 — and only a
tenth fall off the ladder. The amount of coordination a triad carries is quantized.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/phi_ladder/phi_ladder.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 3000
N = 3
L = tuple("ABC")
LADDER = {"0.415": 0.415037, "0.830": 0.830075, "1.000": 1.0, "2.000": 2.0}


def rule(tt):
    return lambda x, _t=tt: _t[sum(x[i] << (N - 1 - i) for i in range(N))]


def main():
    rng = random.Random(SEED)
    on = {k: 0 for k in LADDER}
    off = tri = 0
    for _ in range(FORMS):
        rules = [rule([rng.randint(0, 1) for _ in range(2 ** N)]) for _ in range(N)]
        v = classify_rules(rules, L)
        if v.structure != "triadic":
            continue
        tri += 1
        for k, val in LADDER.items():
            if abs(v.max_phi - val) < 1e-3:
                on[k] += 1
                break
        else:
            off += 1
    print(f"triadic forms: {tri}")
    for k in LADDER:
        print(f"  Phi={k}: {on[k]} ({100 * on[k] / tri:.0f}%)")
    print(f"  off-ladder: {off} ({100 * off / tri:.0f}%)")
    print(f"  on a ladder rung: {sum(on.values())}/{tri} = {100 * sum(on.values()) / tri:.0f}%")


if __name__ == "__main__":
    main()
