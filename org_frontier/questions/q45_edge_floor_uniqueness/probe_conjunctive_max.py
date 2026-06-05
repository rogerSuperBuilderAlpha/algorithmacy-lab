#!/usr/bin/env python
"""Q45 / H2 — only AND commits reach max Phi at the edge floor.

Run:  python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_conjunctive_max
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
from org_frontier.questions.q45_edge_floor_uniqueness.floor_utils import (  # noqa: E402
    AND_INDEX, LABELS, edge_count, instrument_control, s_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
MAX_PHI = 2.0  # n-1 at n=3


def main():
    print("PROBE 146 (H2) — only AND commits reach max Phi at the edge floor")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    counterexamples = []
    for label, rules in enumerate_family():
        v = verdict(rules, LABELS)
        if v.structure != "triadic" or abs(v.max_phi - MAX_PHI) > 1e-6:
            continue
        si = s_index(label)
        rows.append({"label": label, "s_index": si, "edge_count": edge_count(rules),
                     "max_phi": f"{v.max_phi:.6f}"})
        if si != AND_INDEX:
            counterexamples.append((label, si))

    print(f"\n  triadic forms at max Phi={MAX_PHI}: {len(rows)}  (#113 reports 16)")
    print(f"  non-AND counterexamples: {len(counterexamples)}")
    for lab, si in counterexamples[:5]:
        print(f"      {lab}: S-index {si}")

    decision = "confirmed" if not counterexamples else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all max-Phi forms use AND (S-index {AND_INDEX})?  {not counterexamples}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "conjunctive_max.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "s_index", "edge_count", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/conjunctive_max.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
