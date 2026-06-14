#!/usr/bin/env python
"""Q61 / H2 — seam and return-path type partitions are co-extensive.

Run:  python -m org_frontier.questions.q61_seam_return_typing.probe_coextensive_partitions
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q61_seam_return_typing.seam_return_utils import (  # noqa: E402
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 206 (H2) — seam and type partitions co-extensive")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    seq_count = sum(1 for r in rows if r["thompson_type"] == "sequential")
    rec_count = sum(1 for r in rows if r["thompson_type"] == "reciprocal")
    w_count = sum(1 for r in rows if r["singleton"] == "W")
    c_count = sum(1 for r in rows if r["singleton"] == "C")
    equal = sum(1 for r in rows if r["seam_match"])

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  sequential cells: {seq_count}/8")
    print(f"  reciprocal cells: {rec_count}/8")
    print(f"  W singleton cells: {w_count}/8")
    print(f"  C singleton cells: {c_count}/8")
    print(f"  partition equality: {equal}/{len(rows)}")

    counts_ok = seq_count == 8 and rec_count == 8 and w_count == 8 and c_count == 8
    if equal == PANEL_SIZE and counts_ok:
        decision = "confirmed"
    elif equal == len(rows) - 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    8+8 split with 16/16 equality?  {equal == PANEL_SIZE and counts_ok}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "coextensive_partitions.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "singleton", "thompson_type", "partition_equal"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "singleton": r["singleton"],
                "thompson_type": r["thompson_type"],
                "partition_equal": r["seam_match"],
            })
    return decision


if __name__ == "__main__":
    main()
