"""Paper 2 rebuild — the honesty sweeps (from scratch), cross-checked against ../results.md §3–4.

1. Eliminate-the-dyad: hold S'=W∧C fixed, sweep encodings of an added direct W–C channel.
   Endpoints robust (no channel -> triad; full bypass -> dyad); the middle is encoding-dependent
   (0.83 vs 6.00), so the result is stated at the BINARY level only — no magnitude gradient.
2. Read structure: hold S'=W∧C fixed, sweep the strict-mediation read space (W'=g(W,S),
   C'=h(C,S), no W–C edge); count the fraction that keep Φ>0. The verdict turns on the reads,
   not only the determination.

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/sweeps.py
"""

import os, sys
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
sys.path.insert(0, os.path.dirname(__file__))

from itertools import product
from instrument import tpm_from_rules, cm_from_rules, reachable_states, system_phi

S_AND = lambda s: s[0] and s[2]   # S' = W ∧ C, held fixed throughout


def max_phi(rules):
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    phis = []
    for s in reachable_states(tpm):
        st = tuple((s >> i) & 1 for i in range(3))
        phi, _ = system_phi(tpm, cm, st)
        if phi is not None:
            phis.append(phi)
    return max(phis) if phis else 0.0


def eliminate_dyad():
    print("1. ELIMINATE-THE-DYAD  (S'=W∧C fixed; vary the direct W–C channel)")
    encodings = {
        "none (only through S): W'=S,   C'=S":   ([lambda s: s[1], S_AND, lambda s: s[1]]),
        "disjunctive:           W'=S∨C, C'=S∨W": ([lambda s: s[1] or s[2], S_AND, lambda s: s[1] or s[0]]),
        "conjunctive:           W'=S∧C, C'=S∧W": ([lambda s: s[1] and s[2], S_AND, lambda s: s[1] and s[0]]),
        "parity:                W'=S⊕C, C'=S⊕W": ([lambda s: bool(s[1] ^ s[2]), S_AND, lambda s: bool(s[1] ^ s[0])]),
        "full bypass:           W'=C,   C'=W":   ([lambda s: s[2], S_AND, lambda s: s[0]]),
    }
    for label, rules in encodings.items():
        print(f"   {label:<42} maxΦ = {max_phi(rules):.2f}")
    print("   expect: 2.00 / 0.83 / 6.00 / 2.00 / 0.00  (../results.md §3)")
    print("   endpoints robust; middle non-monotone -> binary claim only, no magnitude gradient.")


def read_structure():
    print("\n2. READ STRUCTURE  (S'=W∧C fixed; sweep strict-mediation reads W'=g(W,S), C'=h(C,S))")
    # All 16 Boolean functions of 2 inputs, as truth tables over (own, S).
    def make(fn_bits, own_idx):
        # fn_bits: 4-bit truth table over (own, S) in order (0,0),(0,1),(1,0),(1,1)
        def g(s):
            own, sm = s[own_idx], s[1]
            return bool((fn_bits >> ((own << 1) | sm)) & 1)
        return g
    n_pos = 0
    n_total = 0
    anchors = {}
    for gw, hc in product(range(16), range(16)):
        rules = [make(gw, 0), S_AND, make(hc, 2)]   # W'=g(W,S), S'=W∧C, C'=h(C,S)
        mp = max_phi(rules)
        n_total += 1
        if mp > 1e-9:
            n_pos += 1
    print(f"   strict-mediation read pairs with Φ>0:  {n_pos}/{n_total}  ({100*n_pos/n_total:.1f}%)")
    # The two anchors named in the paper.
    bottleneck = [lambda s: s[1], S_AND, lambda s: s[1]]          # W'=S, C'=S
    feedback   = [lambda s: not s[1], S_AND, lambda s: s[1] or s[2]]  # W'=¬S, C'=S∨C
    print(f"   pure bottleneck  W'=S,  C'=S    -> maxΦ = {max_phi(bottleneck):.2f}  (expect 2.0)")
    print(f"   realistic feedbk W'=¬S, C'=S∨C  -> maxΦ = {max_phi(feedback):.2f}  (expect 0.0)")
    print("   expect 12.5% (32/256) keep Φ>0 under the all-functions read space (../results.md §5;")
    print("   read-space-dependent — a narrower admissible set raises it) — the reads decide the verdict.")


if __name__ == "__main__":
    eliminate_dyad()
    read_structure()
