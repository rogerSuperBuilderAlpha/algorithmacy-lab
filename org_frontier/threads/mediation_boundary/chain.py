"""The twenty-step deep dive on Q3: the structure of the irreducibility boundary.

Each step's question is drawn from the previous step's result; the narrative is in DEEP_DIVE.md. This
script reproduces every computation. Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/threads/mediation_boundary/chain.py

Node order is little-endian. The canonical strict-mediated triad is W(0) reads S, C(2) reads S, and
S(1) reads W and C; the steps vary S's determination and the surrounding structure.
"""

import itertools
import os
import random
import sys
from collections import Counter

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from org_frontier.classifier.classifier import classify_rules
from org_frontier.threads.mediation_boundary._probe import show, probe

L = ("W", "S", "C")
L4 = ("W", "S", "C", "D")


def steps_1_to_4():
    print("STEP 1-2 baseline and weakened gates (W<-S, C<-S, S=f(W,C)):")
    show("S=W&C", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)
    show("S=W|C", [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]], L)
    show("S=W^C parity", [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]], L)
    print("STEP 3-4 the co-monotonicity test (same-direction binds, mixed factors, parity weak):")
    show("S=NAND", [lambda x: x[1], lambda x: 1 - (x[0] & x[2]), lambda x: x[1]], L)
    show("S=NOR", [lambda x: x[1], lambda x: 1 - (x[0] | x[2]), lambda x: x[1]], L)
    show("S=W&(not C) mixed", [lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]], L)
    show("S=(not W)&C mixed", [lambda x: x[1], lambda x: (1 - x[0]) & x[2], lambda x: x[1]], L)


def step_6_mip():
    print("STEP 6 the MIP cut (bipartition-irreducible vs only-tripartition-irreducible):")
    for tag, r in [("S=W&C", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),
                   ("S=W^C", [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]])]:
        p = probe(r, L)
        print(f"  {tag:<10} Φ={p['phi']:<5} MIP={p['mip']}")


def steps_7_to_13():
    print("STEP 7-8 robust to downstream negation (W=not S, C=not S):")
    show("S=W&C, downstream negated", [lambda x: 1 - x[1], lambda x: x[0] & x[2], lambda x: 1 - x[1]], L)
    show("S=W^C, downstream negated", [lambda x: 1 - x[1], lambda x: x[0] ^ x[2], lambda x: 1 - x[1]], L)
    print("STEP 9 a back-channel erodes Φ and migrates the core:")
    show("W also reads C (W=S&C)", [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1]], L)
    show("symmetric W<->C", [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]], L)
    print("STEP 10-11 four parties: one mixed input collapses; substitutability overrides co-monotonicity:")
    show("S=W&C&D all-required", [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], L4)
    show("S=W&C&(not D) one mixed", [lambda x: x[1], lambda x: x[0] & x[2] & (1 - x[3]), lambda x: x[1], lambda x: x[1]], L4)
    show("S=W&(C|D) substitutable", [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]], L4)
    print("STEP 12-13 parity weakens with parties; one mixed gate breaks a chain:")
    show("S=W^C^D 3-way parity", [lambda x: x[1], lambda x: x[0] ^ x[2] ^ x[3], lambda x: x[1], lambda x: x[1]], L4)
    show("chain all-AND", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]], L4)
    show("chain, one mixed gate", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & (1 - x[3]), lambda x: x[2]], L4)


def step_14_robustness():
    print("STEP 14 verdict robustness (single-bit TPM flips; parity stays triadic, co-monotone is fragile):")
    for tag, r in [("S=W&C", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),
                   ("S=W^C", [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]])]:
        tpm = np.array([[r[j]((s & 1, (s >> 1) & 1, (s >> 2) & 1)) for j in range(3)] for s in range(8)], dtype=int)
        flips = changed = 0
        for s in range(8):
            for j in range(3):
                t2 = tpm.copy(); t2[s, j] ^= 1
                nr = [(lambda x, col=col, t=t2: int(t[x[0] | (x[1] << 1) | (x[2] << 2), col])) for col in range(3)]
                flips += 1; changed += classify_rules(nr, L).structure != "triadic"
        print(f"  {tag:<8} {changed}/{flips} flips change the verdict = {100*changed/flips:.0f}%")


def _dtype(tt):
    dep_w = tt[0] != tt[1] or tt[2] != tt[3]
    dep_c = tt[0] != tt[2] or tt[1] != tt[3]
    if not (dep_w and dep_c):
        return "degenerate"
    if tt in [(0, 1, 1, 0), (1, 0, 0, 1)]:
        return "parity"
    incW = tt[1] >= tt[0] and tt[3] >= tt[2]; decW = tt[1] <= tt[0] and tt[3] <= tt[2]
    incC = tt[2] >= tt[0] and tt[3] >= tt[1]; decC = tt[2] <= tt[0] and tt[3] <= tt[1]
    return "co-monotone" if (incW and incC) or (decW and decC) else "mixed"


def steps_15_to_19():
    print("STEP 15-17 mixedness not negation; majority is substitutable; the governance prediction:")
    show("S=NOR (both negated, co-monotone-down)", [lambda x: x[1], lambda x: (1 - x[0]) & (1 - x[2]), lambda x: x[1]], L)
    show("S=majority(W,C,D)", [lambda x: x[1], lambda x: int(x[0] + x[2] + x[3] >= 2), lambda x: x[1], lambda x: x[1]], L4)
    show("merge=opened&approved (positive)", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)
    show("merge=opened&not-blocked (veto)", [lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]], L)
    print("STEP 18 population test over all 16 two-input mediators (canonical config):")
    tot = Counter(); tri = Counter(); phi = Counter()
    for tt in itertools.product([0, 1], repeat=4):
        r = [lambda x: x[1], (lambda x, tt=tt: tt[x[0] + 2 * x[2]]), lambda x: x[1]]
        v = classify_rules(r, L); c = _dtype(tt); tot[c] += 1; tri[c] += v.structure == "triadic"; phi[c] += v.max_phi
    for c in ["co-monotone", "mixed", "parity", "degenerate"]:
        if tot[c]:
            print(f"  {c:<12} triadic {tri[c]}/{tot[c]}, mean Φ {phi[c]/tot[c]:.2f}")
    print("STEP 19 the against-the-grain party is the one excluded from the core:")
    show("S=(not W)&C -> core excludes W", [lambda x: x[1], lambda x: (1 - x[0]) & x[2], lambda x: x[1]], L)
    show("S=W&(not C) -> core excludes C", [lambda x: x[1], lambda x: x[0] & (1 - x[2]), lambda x: x[1]], L)


def step_20_general(n=600, seed=0):
    print("STEP 20 random downstream reads: the co-monotonicity advantage collapses, parity survives:")
    rng = random.Random(seed)

    def randfun1():
        tt = [rng.randint(0, 1) for _ in range(2)]
        return lambda x, tt=tt: tt[x[1]]
    tot = Counter(); tri = Counter()
    for _ in range(n):
        Stt = tuple(rng.randint(0, 1) for _ in range(4))
        c = _dtype(Stt)
        if c == "degenerate":
            continue
        rules = [randfun1(), (lambda x, tt=Stt: tt[x[0] + 2 * x[2]]), randfun1()]
        tot[c] += 1; tri[c] += classify_rules(rules, L).structure == "triadic"
    for c in ["co-monotone", "mixed", "parity"]:
        if tot[c]:
            print(f"  mediator {c:<12} triadic in {tri[c]}/{tot[c]} = {100*tri[c]/tot[c]:.0f}% of random downstream reads")


if __name__ == "__main__":
    steps_1_to_4()
    step_6_mip()
    steps_7_to_13()
    step_14_robustness()
    steps_15_to_19()
    step_20_general()
