"""Paper 2 rebuild — why Φ, not a cheaper test (from scratch).

The strongest objection: a connectivity / conditional-independence / factorization test catches
the reducible dyad for free (not-strongly-connected => Φ=0). The answer is an EXHIBIT, not an
aggregate: a STRONGLY-CONNECTED structure (all six edges, no constant nodes) that nonetheless
REDUCES — exact Φ=0 at every reachable state — which every cheap structural test over-calls as
triadic and only the MIP machinery reduces.

    Exhibit:  W' = NOR(S, C),  S' = ¬W ∧ C,  C' = NAND(W, S)

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/why_phi.py
"""

import os, sys
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from instrument import (tpm_from_rules, cm_from_rules, reachable_states,
                        strongly_connected, system_phi)

LABELS = ("W", "S", "C")

# The exhibit: all six off-diagonal edges, no self-loops, no constant nodes.
EXHIBIT = [
    lambda s: not (s[1] or s[2]),     # W' = NOR(S, C)
    lambda s: (not s[0]) and s[2],    # S' = ¬W ∧ C
    lambda s: not (s[0] and s[1]),    # C' = NAND(W, S)
]


# ----- the two cheap structural tests a reviewer proposes -----------------------------

def connectivity_says_triadic(cm):
    """Cheap test 1: strongly connected => 'irreducible/triadic'. (Over-calls: strong
    connectivity is necessary but NOT sufficient for Φ>0.)"""
    return strongly_connected(cm)


def factorization_says_triadic(cm):
    """Cheap test 2: a structural factorization test. 'Dyadic' iff the party graph splits
    into two blocks with no edges crossing between them (block-diagonal under some party
    partition); else 'triadic'. Over-calls any all-edges structure."""
    n = cm.shape[0]
    A = cm.astype(bool) | cm.T.astype(bool)        # undirected coupling
    for mask in range(1, 2 ** n - 1):              # non-trivial party bipartitions
        block = [bool((mask >> i) & 1) for i in range(n)]
        crosses = any(A[i, j] for i in range(n) for j in range(n) if block[i] != block[j])
        if not crosses:
            return False                            # found a clean split -> dyadic
    return True                                     # no clean split -> 'triadic'


def phi_says_triadic(rules):
    """The instrument: Φ>0 at any reachable state => mediated triad."""
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    phis = []
    for s in reachable_states(tpm):
        st = tuple((s >> i) & 1 for i in range(3))
        phi, _ = system_phi(tpm, cm, st)
        if phi is not None:
            phis.append(phi)
    return (max(phis) > 1e-9 if phis else False), (max(phis) if phis else 0.0)


def main():
    tpm, cm = tpm_from_rules(EXHIBIT), cm_from_rules(EXHIBIT)
    n_edges = int(cm.sum() - np.trace(cm))         # off-diagonal edges
    has_constant = any((cm[:, j].sum() == 0) for j in range(3))

    print("THE EXHIBIT —  W'=NOR(S,C),  S'=¬W∧C,  C'=NAND(W,S)")
    print(f"  connectivity matrix (cm[i,j]=1 iff j reads i):\n{cm}")
    print(f"  off-diagonal edges present : {n_edges} / 6")
    print(f"  any constant (unread) node : {has_constant}")
    print(f"  strongly connected         : {strongly_connected(cm)}")

    # Per-state exact Φ.
    print("  per reachable state, exact IIT-4.0 Φ:")
    allzero = True
    for s in reachable_states(tpm):
        st = tuple((s >> i) & 1 for i in range(3))
        phi, mip = system_phi(tpm, cm, st)
        if phi is None:
            continue
        allzero = allzero and (phi <= 1e-9)
        print(f"    state {st}:  Φ = {phi:.4f}")
    print(f"  Φ=0 at EVERY reachable state: {allzero}")

    print("\nVERDICTS ON THE EXHIBIT")
    print(f"  cheap connectivity test     -> {'TRIAD' if connectivity_says_triadic(cm) else 'dyad'}  (over-calls)")
    print(f"  cheap factorization test    -> {'TRIAD' if factorization_says_triadic(cm) else 'dyad'}  (over-calls)")
    triad, maxphi = phi_says_triadic(EXHIBIT)
    print(f"  Φ over the MIP (instrument) -> {'TRIAD' if triad else 'DYAD'}   (maxΦ={maxphi:.4f}) — correct: it REDUCES")
    print("\n  The exhibit is strongly connected with all six edges, so every cheap structural")
    print("  test calls it triadic. Only Φ's minimum-information partition finds that the")
    print("  cause-effect structure factors. That residual zone is where Φ earns its weight.")
    print("  (../results.md §5; corroborated by IIT's Rule 110 'magic cut'.)")


if __name__ == "__main__":
    main()
