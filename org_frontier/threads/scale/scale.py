"""The scale thread (E24 of the catalog line).

How large a coordination can one mediator hold together? Not large. A single-hub star — every party reading
the hub, the hub reading all — binds three parties about a tenth of the time, four parties about a fiftieth, and five parties essentially never. Commitment collapses as the
coordination grows, while the hub's share of the credit where it does commit stays near constant. One
mediator has a size limit; past it, the parties cannot be bound into a single irreducible whole.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/scale/scale.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 300
EPS = 1e-6


def run(n):
    rng = random.Random(SEED)
    L = tuple("ABCDE"[:n])
    hub = n - 1
    tri = 0
    shares = []
    for _ in range(FORMS):
        rules = [None] * n
        for i in range(n - 1):
            rules[i] = _rule_of_one(rng.randint(0, 3), hub)
        rules[hub] = _rule_of_set([rng.randint(0, 1) for _ in range(2 ** (n - 1))], list(range(n - 1)))
        if classify_rules(rules, L).structure != "triadic":
            continue
        tri += 1
        v = value_function(network(rules, L)[0], network(rules, L)[1], n)
        sh = shapley(v, n)
        total = sum(sh)
        if total > EPS:
            shares.append(sh[hub] / total)
    s = f"{np.mean(shares):.3f}" if shares else "n/a"
    print(f"  {n} parties (1 hub + {n - 1}): commit={tri}/{FORMS} ({100 * tri / FORMS:.0f}%)  hub-share={s}")


def main():
    print("A single-hub star at growing size. How large a coordination can one mediator bind?")
    for n in (3, 4, 5):
        run(n)
    print("Commitment collapses with scale (10% -> 2% -> 0%); the hub's share stays near constant.")


if __name__ == "__main__":
    main()
