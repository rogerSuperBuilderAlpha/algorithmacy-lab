#!/usr/bin/env python
"""Q59 / H2 — symmetric-difference size fixed at four directed edges.

Run:  python -m org_frontier.questions.q59_directed_cut_edges.probe_symdiff_size
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q59_directed_cut_edges.cut_edge_utils import (  # noqa: E402
    ONLY_EXCL_SIZE,
    ONLY_TIED_SIZE,
    SYMDIFF_SIZE,
    edge_detail_rows,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 196 (H2) — symmetric-difference size")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = edge_detail_rows()
    at_template = 0
    for r in rows:
        if len(r["only_tied"]) == ONLY_TIED_SIZE and len(r["only_excl"]) == ONLY_EXCL_SIZE:
            at_template += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  |only_tied|={ONLY_TIED_SIZE}, |only_excl|={ONLY_EXCL_SIZE}: {at_template}/{len(rows)}")
    print(f"  symdiff total {SYMDIFF_SIZE}: {at_template}/{len(rows)}")

    if at_template == len(rows) == 16:
        decision = "confirmed"
    elif at_template == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all pairs at symdiff template?  {at_template == len(rows)}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "symdiff_size.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "only_tied_n", "only_excl_n", "symdiff_n"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "only_tied_n": len(r["only_tied"]),
                "only_excl_n": len(r["only_excl"]),
                "symdiff_n": len(r["only_tied"]) + len(r["only_excl"]),
            })
    return decision


if __name__ == "__main__":
    main()
