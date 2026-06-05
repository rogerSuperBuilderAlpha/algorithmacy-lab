#!/usr/bin/env python
"""Q45 / H3 — parity commits saturate their ceiling at the same edge floor.

Run:  python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_parity_floor
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
    LABELS, PARITY_INDICES, edge_count, instrument_control, s_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
FLOOR = 4
PARITY_CEILING = 0.5  # 2^(2-3)


def main():
    print("PROBE 147 (H3) — parity commits saturate their ceiling at the edge floor")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    bad = []
    for label, rules in enumerate_family():
        v = verdict(rules, LABELS)
        si = s_index(label)
        if v.structure != "triadic" or si not in PARITY_INDICES:
            continue
        ec = edge_count(rules)
        rows.append({"label": label, "s_index": si, "edge_count": ec,
                     "max_phi": f"{v.max_phi:.6f}"})
        if ec != FLOOR or abs(v.max_phi - PARITY_CEILING) > 1e-6:
            bad.append((label, ec, v.max_phi))

    print(f"\n  parity triadic forms: {len(rows)}  (#113 reports 8)")
    print(f"  off-ceiling or off-floor: {len(bad)}")
    for lab, ec, phi in bad[:5]:
        print(f"      {lab}: edges={ec}, Phi={phi:.3f}")

    decision = "confirmed" if not bad else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all parity at {FLOOR} edges and Phi={PARITY_CEILING}?  {not bad}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "parity_floor.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "s_index", "edge_count", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/parity_floor.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
