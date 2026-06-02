"""Paper 3 — how much does each typology placement depend on the analyst's coding choice?

Each organization in typology_phi.py is assigned a determination function (AND, XOR, ...) and a
mediation regime by the analyst, "derived from how it actually coordinates." That coding is a
researcher degree of freedom: the same verbal description of, say, rideshare can be read as a
conjunctive match (AND) or a disjunctive one (OR), and Φ moves a lot between them. This script
holds each organization's REGIME and party count fixed (the structural facts we are most sure of)
and recomputes Φ under every determination function in the model's vocabulary, reporting the
range. A placement that barely moves is robust to the coding; one that swings across bands is not.

It also makes explicit what the "court = platform" result is: the court and the rideshare
platform are assigned the SAME (strict, AND) structure, so their equal Φ is true BY CONSTRUCTION
under that coding — a statement about the model, not an empirical discovery about technology vs
structure. The sensitivity table is the honest way to report it.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/typology_sensitivity.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_P2 = os.path.abspath(os.path.join(_HERE, "..", "paper2_construct"))
for p in (_HERE, _P2):
    if p not in sys.path:
        sys.path.insert(0, p)

import numpy as np
import pyphi

from phi_instrument import tpm_from_rules, cm_from_rules, system_phi_over_states
from simulated_orgs import build_rules, DETS

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

# Each organization mapped to the structural facts we hold fixed (regime, n) + its assigned
# determination. Sensitivity = Φ as the determination ranges over the model's vocabulary.
# (Dyadic baselines have no determination to vary, so they are reported as the Φ=0 floor.)
TYPOLOGY = [
    ("Rideshare, solo (Uber/Lyft)",        "strict",  "AND", 3),
    ("Food delivery",                       "strict",  "AND", 3),
    ("Hiring / applicant-tracking system",  "strict",  "AND", 3),
    ("Content moderation",                  "strict",  "AND", 3),
    ("Court (judge between parties)",       "strict",  "AND", 3),
    ("Complementary skill matching",        "strict",  "XOR", 3),
    ("Freelance marketplace (Upwork)",      "partial", "AND", 3),
    ("Healthcare staffing agency",          "partial", "AND", 3),
    ("Real-estate broker",                  "partial", "AND", 3),
]

DET_ORDER = ["AND", "OR", "MAJ", "XOR", "THRESH2"]


def _dense_bc(n):
    import itertools
    parties = [0] + list(range(2, n))
    return frozenset(frozenset(pr) for pr in itertools.combinations(parties, 2))


def phi_for(regime, det, n):
    bc = _dense_bc(n) if regime == "partial" else frozenset()
    rules = build_rules(n, regime, det, bc)
    tpm, cm = tpm_from_rules(rules, n), cm_from_rules(rules, n)
    res = system_phi_over_states(tpm, cm, n)
    phis = [p for _, p in res] or [0.0]
    return float(np.max(phis))


def band(phi):
    if phi == 0:
        return "0 (dyadic)"
    if phi < 1:
        return "low"
    if phi < 2:
        return "moderate"
    if phi < 4:
        return "high"
    return "extreme(Cerullo)"


def main():
    print("=" * 100)
    print("PAPER 3 — typology placement sensitivity to the determination coding (regime fixed)")
    print("=" * 100)
    header = f"{'organization':<34}{'assigned':>9}{'Φ@assigned':>12}   " + \
        "".join(f"{d:>8}" for d in DET_ORDER) + f"{'range':>9}"
    print(header)
    print("-" * 100)
    for name, regime, assigned, n in TYPOLOGY:
        phis = {d: phi_for(regime, d, n) for d in DET_ORDER}
        assigned_phi = phis[assigned]
        lo, hi = min(phis.values()), max(phis.values())
        cells = "".join(f"{phis[d]:>8.2f}" for d in DET_ORDER)
        print(f"{name:<34}{assigned:>9}{assigned_phi:>12.2f}   {cells}{hi-lo:>9.2f}")
    print("-" * 100)
    print("READING: where the row swings across bands as the determination changes, the placement")
    print("is an artifact of the coding, not a robust fact about the organization. The strict forms")
    print("(rideshare, ATS, court) all share one row BY CONSTRUCTION — their equal Φ reflects an")
    print("identical assigned structure, which is why 'court = platform' is a modeling statement,")
    print("not a discovery. Paper 3 §4.4 now reports these placements with this sensitivity band.")
    print("=" * 100)


if __name__ == "__main__":
    main()
