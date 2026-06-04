"""Probe 113 (G1) — what are the parity forms that every cheap measure misses?

Question: the 8 pure-higher-order triadic forms (#56) are the universal cheap-measure blind spot — Φ_AR
under-ranks them (#101) and every cheap CES predicate misses exactly them (#102). What are they?
Hypothesis: they are exactly the forms whose commit is a parity (XOR-family) function — the only 2-input
functions that are non-monotone and depend irreducibly on both parties. Method: over the 24 triadic
corpus forms, recover each commit's truth table, label it conjunctive (monotone) vs parity (XOR/XNOR),
and cross-tab with the exact Φ (2.0 vs 0.5).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_parity_characterization
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family
from .probe_abm_difficulty import commit_table

PARITY = {(0, 1, 1, 0), (1, 0, 0, 1)}   # XOR, XNOR


def main():
    print("PROBE 113 (G1) — the parity forms behind the cheap-measure blind spot")
    print("=" * 64)
    n_parity_tri = n_conj_tri = 0
    phi_by_type = {"parity": set(), "conjunctive": set()}
    for _, rules in enumerate_family():
        v = classify_rules(rules, labels=("W", "S", "C"))
        if v.structure != "triadic":
            continue
        ts = commit_table(rules)
        kind = "parity" if ts in PARITY else "conjunctive"
        phi_by_type[kind].add(round(v.max_phi, 3))
        if kind == "parity":
            n_parity_tri += 1
        else:
            n_conj_tri += 1
    print(f"  triadic forms: {n_parity_tri} parity-commit, {n_conj_tri} conjunctive-commit")
    print(f"  Φ values among parity-commit triadic forms      : {sorted(phi_by_type['parity'])}")
    print(f"  Φ values among conjunctive-commit triadic forms : {sorted(phi_by_type['conjunctive'])}")
    print("=" * 64)
    parity_is_low = phi_by_type["parity"] and max(phi_by_type["parity"]) < 1.0
    conj_is_high = phi_by_type["conjunctive"] and min(phi_by_type["conjunctive"]) >= 1.0
    if parity_is_low and conj_is_high:
        print("  Reading: the parity-commit forms are exactly the Φ=0.5 pure-higher-order forms (#56), and")
        print("  the conjunctive-commit forms are the Φ=2.0 ones. The cheap-measure blind spot is the XOR")
        print("  family — the only commits that bind both parties with no monotone, lower-order shadow a")
        print("  linear proxy or a distinction count could pick up.")
    else:
        print("  Reading: the parity/conjunctive split does not line up with the Φ=0.5/2.0 split as expected.")
    print("=" * 64)


if __name__ == "__main__":
    main()
