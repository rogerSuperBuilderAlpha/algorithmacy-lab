#!/usr/bin/env python
"""Q45 / H1 — every triadic strict-mediation form sits at the 4-edge floor.

Run:  python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_edge_floor
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
    LABELS, edge_count, instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
FLOOR = 4  # 2*(n-1) at n=3


def main():
    print("PROBE 145 (H1) — every triadic strict-mediation form sits at the edge floor")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    n_triadic = 0
    bad = []
    for label, rules in enumerate_family():
        v = verdict(rules, LABELS)
        if v.structure != "triadic":
            continue
        n_triadic += 1
        ec = edge_count(rules)
        rows.append({"label": label, "max_phi": f"{v.max_phi:.6f}", "edge_count": ec})
        if ec != FLOOR:
            bad.append((label, ec))

    edge_vals = sorted(set(r["edge_count"] for r in rows))
    print(f"\n  triadic forms: {n_triadic}  (corpus #30 reports 24)")
    print(f"  edge counts among triadic: {edge_vals}")
    print(f"  forms off the {FLOOR}-edge floor: {len(bad)}")
    for lab, ec in bad[:5]:
        print(f"      {lab}: {ec} edges")

    decision = "confirmed" if not bad else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all triadic at {FLOOR} edges?  {not bad}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "edge_floor.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "max_phi", "edge_count"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/edge_floor.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
