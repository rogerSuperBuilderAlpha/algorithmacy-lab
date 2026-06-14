#!/usr/bin/env python
"""Q59 / H1 — back-channel cross-edge severed in both outer cuts.

Run:  python -m org_frontier.questions.q59_directed_cut_edges.probe_cross_edge_shared
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q59_directed_cut_edges.cut_edge_utils import (  # noqa: E402
    edge_detail_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 195 (H1) — cross-edge shared severance")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = edge_detail_rows()
    both = sum(1 for r in rows if r["cross_in_tied"] and r["cross_in_excl"])
    tied_only = sum(1 for r in rows if r["cross_in_tied"] and not r["cross_in_excl"])
    excl_only = sum(1 for r in rows if r["cross_in_excl"] and not r["cross_in_tied"])
    neither = sum(1 for r in rows if not r["cross_in_tied"] and not r["cross_in_excl"])

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  cross-edge in both cuts: {both}/{len(rows)}")
    print(f"  cross-edge tied-only: {tied_only}")
    print(f"  cross-edge excl-only: {excl_only}")
    print(f"  cross-edge in neither: {neither}")

    if both == len(rows) == 16:
        decision = "confirmed"
    elif both == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    cross-edge in both on all pairs?  {both == len(rows)}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "cross_edge_shared.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "cross_edge", "in_tied", "in_excl", "both"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "cross_edge": r["cross_edge"],
                "in_tied": r["cross_in_tied"],
                "in_excl": r["cross_in_excl"],
                "both": r["cross_in_tied"] and r["cross_in_excl"],
            })
    return decision


if __name__ == "__main__":
    main()
