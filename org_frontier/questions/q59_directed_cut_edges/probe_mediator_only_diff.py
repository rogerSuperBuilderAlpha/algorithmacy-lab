#!/usr/bin/env python
"""Q59 / H4 — mediator edges in recipient-only symmetric difference.

Run:  python -m org_frontier.questions.q59_directed_cut_edges.probe_mediator_only_diff
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import PHI_TOL  # noqa: E402
from org_frontier.questions.q59_directed_cut_edges.cut_edge_utils import (  # noqa: E402
    ADJ_RATIO,
    MEDIATOR_COUNT,
    edge_detail_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 198 (H4) — mediator edges in recipient-only difference")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = edge_detail_rows()
    med_two = sum(1 for r in rows if r["mediator_only_tied"] == MEDIATOR_COUNT)
    ratios = [r["adj_ratio"] for r in rows if r["adj_ratio"] is not None]
    at_ratio = sum(1 for x in ratios if abs(x - ADJ_RATIO) < PHI_TOL)
    spread = max(ratios) - min(ratios) if ratios else None

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  mediator edges in only_tied == {MEDIATOR_COUNT}: {med_two}/{len(rows)}")
    print(f"  adj ratio {ADJ_RATIO}: {at_ratio}/{len(rows)}")
    print(f"  adj ratio spread: {spread:.6f}" if spread is not None else "  adj ratio spread: n/a")

    if med_two == len(rows) == 16 and at_ratio == len(rows) and spread is not None and spread < PHI_TOL:
        decision = "confirmed"
    elif med_two == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    mediator count 2 on all pairs?  {med_two == len(rows)}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "mediator_only_diff.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "mediator_only_tied", "adj_tied", "adj_excl", "adj_ratio"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "mediator_only_tied": r["mediator_only_tied"],
                "adj_tied": r["adj_tied"],
                "adj_excl": r["adj_excl"],
                "adj_ratio": r["adj_ratio"],
            })
    return decision


if __name__ == "__main__":
    main()
