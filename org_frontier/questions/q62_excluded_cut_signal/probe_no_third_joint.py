#!/usr/bin/env python
"""Q62 / H4 — no third independent joint label.

Run:  python -m org_frontier.questions.q62_excluded_cut_signal.probe_no_third_joint
"""

import csv
import os
import sys
from collections import Counter

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q62_excluded_cut_signal.excluded_cut_utils import (  # noqa: E402
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

EXPECTED_JOINTS = {
    ("W", "sequential", "C"): 8,
    ("C", "reciprocal", "W"): 8,
}


def main():
    print("PROBE 213 (H4) — no third independent joint label")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    counts = Counter(r["joint"] for r in rows)
    distinct = len(counts)

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  distinct joint labels: {distinct}")
    for joint, cnt in sorted(counts.items()):
        print(f"    {joint}: {cnt}/16")

    expected_ok = all(counts.get(j, 0) == c for j, c in EXPECTED_JOINTS.items())
    split_ok = distinct == 2 and expected_ok

    if split_ok and distinct == 2:
        decision = "confirmed"
    elif distinct == 2 and not expected_ok:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    exactly 2 joints with 8+8?  {split_ok}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "no_third_joint.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology", "tied_singleton", "thompson_type",
                "excluded_singleton", "joint",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_singleton": r["tied_singleton"],
                "thompson_type": r["thompson_type"],
                "excluded_singleton": r["excluded_singleton"],
                "joint": str(r["joint"]),
            })
    return decision


if __name__ == "__main__":
    main()
