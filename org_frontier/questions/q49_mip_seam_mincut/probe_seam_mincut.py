#!/usr/bin/env python
"""Q49 / H5 — the seam is not the connectivity min-cut.

Ensemble: the H4 asymmetric panel (worker-side and counterpart-side back-channels) plus the 8 parity
(XOR/XNOR commit) triadic forms from the strict-mediation family (S-function index 6=XOR, 9=XNOR).
Measure: the Φ-seam set vs the connectivity min-cut singleton set (the parties minimizing total
crossing-edge degree, from cm_from_rules). Agreement per form.

Instrument control (run first): canonical triad triadic, Φ=2.0; seam {W,C} and min-cut {W,C} agree
(positive control for the comparison).

Decision rule (fixed before run): H5 confirmed (H0 refuted) if the Φ-seam and the min-cut disagree on at
least one form; refuted if they agree on every form.

Run:  python -m org_frontier.questions.q49_mip_seam_mincut.probe_seam_mincut
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.questions.q49_mip_seam_mincut.seam import seam_set, mincut_set, LABELS  # noqa: E402

CANON = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
ASYM = {
    "worker_side  (C->W)": [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1]],
    "counterpart  (W->C)": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[0]],
}
PARITY_S = {6, 9}  # XOR=6, XNOR=9 (two-input function index, little-endian table)
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def instrument_control():
    v = verdict(CANON, LABELS)
    assert v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6, "control failed"
    assert seam_set(CANON, LABELS) == {"W", "C"} == mincut_set(CANON, LABELS), "control comparison failed"
    return v


def _row(name, rules, kind):
    v = verdict(rules, LABELS)
    seam = seam_set(rules, LABELS) if v.structure == "triadic" else set()
    cut = mincut_set(rules, LABELS)
    agree = seam == cut
    return {"form": name, "kind": kind, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
            "phi_seam": "|".join(sorted(seam)) or "(none)", "graph_mincut": "|".join(sorted(cut)),
            "agree": agree}


def main():
    print("PROBE 144 (H5) — the seam is not the connectivity min-cut")
    print("=" * 64)
    instrument_control()
    print("[instrument control] canonical triad: seam {C, W} == min-cut {C, W}  -> PASS (agreement)")

    rows = [_row("canonical_triad", CANON, "conjunctive")]
    for name, rules in ASYM.items():
        rows.append(_row(name.strip(), rules, "asymmetric"))
    # the 8 parity triadic forms
    n_parity = 0
    for label, rules in enumerate_family():
        s_idx = int(label.split("_S")[1].split("_")[0])
        if s_idx not in PARITY_S:
            continue
        v = verdict(rules, LABELS)
        if v.structure != "triadic":
            continue
        n_parity += 1
        rows.append(_row(label, rules, "parity"))

    print(f"\n  {'form':<26}{'kind':<12}{'Φ-seam':<10}{'min-cut':<10}agree")
    for r in rows:
        print(f"  {r['form']:<26}{r['kind']:<12}{r['phi_seam']:<10}{r['graph_mincut']:<10}{r['agree']}")
    print(f"\n  parity triadic forms found: {n_parity}  (corpus #56/#113 report 8)")

    disagreements = [r for r in rows if not r["agree"]]
    decision = "confirmed" if disagreements else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    forms where Φ-seam != graph min-cut: {len(disagreements)}/{len(rows)}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_mincut.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["form", "kind", "structure", "max_phi", "phi_seam",
                                           "graph_mincut", "agree"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
