#!/usr/bin/env python
"""Q59 / H3 — cross-edge subtraction equalizes severed counts.

Run:  python -m org_frontier.questions.q59_directed_cut_edges.probe_cross_subtract_equal
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
    print("PROBE 197 (H3) — cross-edge subtraction equalizes counts")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = edge_detail_rows()
    equal = sum(1 for r in rows if r["adj_equal"])
    adj_tied_vals = [r["adj_tied"] for r in rows]
    adj_excl_vals = [r["adj_excl"] for r in rows]

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  adj_tied == adj_excl: {equal}/{len(rows)}")
    print(f"  adj_tied values: {sorted(set(adj_tied_vals))}")
    print(f"  adj_excl values: {sorted(set(adj_excl_vals))}")

    if equal == len(rows) == 16:
        decision = "confirmed"
    elif equal == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    adjusted counts equal on all pairs?  {equal == len(rows)}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "cross_subtract_equal.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "cut_ones_tied", "cut_ones_excl",
                        "adj_tied", "adj_excl", "adj_equal"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "cut_ones_tied": int(r["tied_cm"].sum()),
                "cut_ones_excl": int(r["excl_cm"].sum()),
                "adj_tied": r["adj_tied"],
                "adj_excl": r["adj_excl"],
                "adj_equal": r["adj_equal"],
            })
    return decision


if __name__ == "__main__":
    main()
