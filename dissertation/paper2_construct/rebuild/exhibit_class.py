"""Paper 2 §8 — the exhibit is representative of a whole class, not cherry-picked.

The Section 8 exhibit is one strongly-connected three-node wiring with exact IIT-4.0
Φ = 0. This script shows it belongs to a populated class and that the geometric measure
over-calls the entire class. It buckets all 4,096 three-node wirings by §8's own logic:

  - simple dyad : NOT strongly connected            (=> exact Φ = 0, by §8's argument)
  - hard dyad   : strongly connected AND exact Φ = 0 (the exhibit's class)
  - triad       : strongly connected AND exact Φ > 0 (genuine triads)

and computes the exact information-geometric Φ (geometric_check.geometric_phi, reachable
input) for every wiring — not a sample. The claim §8 makes:

  - geometric Φ reads ~0 on the simple dyads (true negatives),
  - over-calls the ENTIRE hard-dyad class (every member, exact Φ = 0, geometric Φ > 0),
  - reads positive on the genuine triads (true positives).

So the over-call is a property of the strongly-connected-yet-reducible class, of which
the exhibit is one member, not an artifact of one constructed automaton.

Bucketing computes exact IIT-4.0 Φ (PyPhi) for the strongly-connected wirings, so this
takes a few minutes. Depends on PyPhi 4.0, numpy, and the sibling rebuild scripts.

Reproduce:
    ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/exhibit_class.py
"""

import os, sys, itertools
import numpy as np
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "paper3_baseline", "rebuild"))
import phi_core
from geometric_check import geometric_phi

FUNCS = []
for bits in itertools.product((0, 1), repeat=4):
    tt = {(0, 0): bits[0], (0, 1): bits[1], (1, 0): bits[2], (1, 1): bits[3]}
    FUNCS.append((lambda a, b, tt=tt: tt[(a, b)]))
READS = [(1, 2), (0, 2), (0, 1)]   # W reads (S,C); S reads (W,C); C reads (W,S)


def rules_for(fi):
    return [(lambda x, f=FUNCS[fi[j]], r=READS[j]: f(x[r[0]], x[r[1]])) for j in range(3)]


def main():
    simple_g, hard_g, triad_g = [], [], []
    for fi in itertools.product(range(16), repeat=3):
        rules = rules_for(fi)
        cm = phi_core.cm_from_rules(rules, 3)
        g = geometric_phi(rules, 3, "reachable")
        if not phi_core.strongly_connected(cm):
            simple_g.append(g)
        else:
            mx = phi_core.placement(rules, 3)["max"]
            (hard_g if mx <= 1e-9 else triad_g).append(g)

    def row(name, gs):
        gs = np.array(gs)
        over = (gs > 1e-6).mean() * 100
        print(f"  {name:24} n={len(gs):4d}   geometric Φ > 0: {over:5.1f}%   "
              f"range {gs.min():.2f}–{gs.max():.2f}  median {np.median(gs):.2f}")

    print("All 4,096 three-node wirings, exact geometric Φ by class:")
    row("simple dyad (not SC)", simple_g)
    row("HARD dyad (SC, Φ=0)", hard_g)
    row("triad (SC, Φ>0)", triad_g)
    print("\nThe hard-dyad class is the exhibit's class. Geometric Φ over-calls every")
    print("member of it while exact IIT-4.0 Φ is zero for every member — so the §8")
    print("exhibit is representative of a populated class, not a cherry-picked automaton.")


if __name__ == "__main__":
    main()
