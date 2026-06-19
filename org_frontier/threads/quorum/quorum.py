"""The quorum thread (E12 of the catalog line).

A quorum mediator fires when at least k of its parties are active. This thread asks which thresholds can bind
an irreducible coordination. Only the extremes can. A mediator that needs any one party (k=1) or all of them
(k=3) commits in a few percent of forms; a mediator that needs a majority (k=2) never commits at all. The
interior threshold factors. The mediator is the bottleneck at every threshold.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/quorum/quorum.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.designed_mediator._harness import _rule_of_one
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.classifier.classifier import classify_rules

SEED = 11
FORMS = 400
N = 4
L = tuple("ABCS")   # A,B,C parties (0,1,2) read S=3; S = threshold-k of A,B,C


def threshold(k):
    return lambda x, _k=k: 1 if (x[0] + x[1] + x[2]) >= _k else 0


def run(k):
    rng = random.Random(SEED)
    tri = integ = s_veto = 0
    for _ in range(FORMS):
        rules = [_rule_of_one(rng.randint(0, 3), 3), _rule_of_one(rng.randint(0, 3), 3),
                 _rule_of_one(rng.randint(0, 3), 3), threshold(k)]
        net, tpm = network(rules, L)
        W = integrating_coalitions(net, tpm, N)
        if W:
            integ += 1
            if 3 in veto_set(W):
                s_veto += 1
        if classify_rules(list(rules), L).structure == "triadic":
            tri += 1
    label = {1: "any", 2: "majority", 3: "all"}[k]
    print(f"quorum k={k} ({label:8s}): triadic={tri}/{FORMS} ({100 * tri / FORMS:.0f}%) "
          f"S-veto|integrating={s_veto}/{integ}")


def main():
    print("Quorum mediator: S fires if at least k of three parties are active; parties heed S.")
    for k in [1, 2, 3]:
        run(k)


if __name__ == "__main__":
    main()
