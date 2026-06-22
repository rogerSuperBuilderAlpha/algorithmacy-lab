"""The twenty-step deep dive on Q8: who sits in the irreducible core, and who drops out.

Q8 from the mediation_boundary thread's QUESTIONS.md. The first three dives asked whether a coordination
is irreducible; this one asks which parties are in the irreducible whole when it is. The major complex
is the lab's reading of membership, and the dive maps the rules that put a party in it or push it out.
Each step's question is drawn from the previous step's result; the narrative is in DEEP_DIVE.md, and
every number reproduces here.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/threads/core_membership/chain.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from org_frontier.threads.mediation_boundary._probe import show, probe
from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set

L = ("W", "S", "C")
L4 = ("W", "S", "C", "D")


def rand3(rng):
    rules = []
    for _ in range(3):
        ins = [i for i in range(3) if rng.random() < 0.5] or [rng.randrange(3)]
        if len(ins) == 1:
            rules.append(_rule_of_one(rng.randint(0, 3), ins[0]))
        else:
            rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules


def auc(scores, labels):
    p = [s for s, l in zip(scores, labels) if l]
    n = [s for s, l in zip(scores, labels) if not l]
    return sum((a > b) + 0.5 * (a == b) for a in p for b in n) / (len(p) * len(n)) if p and n else float("nan")


def run():
    print("STEP 1-3 the exclusions: a party leaves the core when it is decoupled, half-coupled,")
    print("read against the grain, or substitutable:")
    show("full triad S=W&C", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)
    show("against-the-grain S=W&(not C)", [lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]], L)
    show("observer X (in-only)", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]], L4)
    show("emitter X (out-only)", [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]], L4)
    show("substitutable S=W&(C|D)", [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]], L4)

    print("\nSTEP 4-7 directional and competitive exclusions:")
    show("chain core localizes to a link", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]], ("W", "S1", "S2", "C"))
    show("v10 review: author excluded", [lambda x: x[3], lambda x: x[0] & x[3], lambda x: x[1] & x[0], lambda x: x[2]], ("W", "R", "S", "C"))
    show("pure relay: mediator excluded", [lambda x: x[0], lambda x: x[0], lambda x: x[1]], L)
    show("coupled principal seizes core", [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[0] & x[2] & x[1]], ("W", "S", "C", "P"))

    print("\nSTEP 8 mutual (2-cycle) coupling predicts membership (per-node, n=3):")
    rng = random.Random(0)
    sc, lb = [], []
    for _ in range(150):
        r = rand3(rng)
        cm = cm_from_rules(r)
        net, tpm = network(r, L)
        _, core, _ = complex_over_states(net, tpm, 3)
        if core is None:
            continue
        for i in range(3):
            sc.append(sum(1 for j in range(3) if j != i and cm[i, j] and cm[j, i]))
            lb.append(i in core)
    print(f"  AUC of mutual-coupling degree for core membership = {auc(sc, lb):.2f}")

    print("\nSTEP 10,12,15 the negatively-read party leaves; the core is one connected cycle; the governance reading:")
    print(f"  S=W&(not C): core {probe([lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]], L)['core']} (C, negatively read, out)")
    print(f"  S=(not W)&C: core {probe([lambda x: x[1], lambda x: (1 - x[0]) & x[2], lambda x: x[1]], L)['core']} (W, negatively read, out)")
    print(f"  W<->S 2-cycle, C self-loop: core {probe([lambda x: x[1], lambda x: x[0], lambda x: x[2]], L)['core']} (one connected cycle, not disconnected)")
    print(f"  v9 light merge S=W&C: core {probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)['core']} (everyone bound)")
    print(f"  v10 heavy review: core {probe([lambda x: x[3], lambda x: x[0] & x[3], lambda x: x[1] & x[0], lambda x: x[2]], ('W','R','S','C'))['core']} (author excluded)")

    print("\nSTEP 14 the whole verdict needs the full core (core size vs whole-system Φ):")
    rng = random.Random(1)
    bysize = {}
    for _ in range(200):
        r = rand3(rng)
        v = classify_rules(r, L)
        net, tpm = network(r, L)
        _, core, _ = complex_over_states(net, tpm, 3)
        sz = len(core) if core else 0
        bysize.setdefault(sz, []).append(v.max_phi)
    for sz in sorted(bysize):
        print(f"  core size {sz}: n={len(bysize[sz]):<3} mean whole-Φ={np.mean(bysize[sz]):.2f}")


if __name__ == "__main__":
    run()
