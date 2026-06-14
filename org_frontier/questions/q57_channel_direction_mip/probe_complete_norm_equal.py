#!/usr/bin/env python
"""Q57 / H4 — complete partition shares tied outer minimum normalized_phi.

Run:  python -m org_frontier.questions.q57_channel_direction_mip.probe_complete_norm_equal
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    PHI_TOL,
    enriched_rows,
    instrument_control,
    norm_fields,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 188 (H4) — complete partition shares tied outer minimum normalized_phi")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_rows()
    equal = 0
    for r in rows:
        nf = norm_fields(r)
        if (
            nf["complete_norm"] is not None
            and nf["tied_norm"] is not None
            and abs(nf["complete_norm"] - nf["tied_norm"]) < PHI_TOL
        ):
            equal += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  complete norm equals tied outer: {equal}/{len(rows)}")

    if equal == len(rows) == 16:
        decision = "confirmed"
    elif equal == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all complete-tied norm equal?  {equal == len(rows)}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "complete_norm_equal.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_norm", "complete_norm", "equal"],
        )
        w.writeheader()
        for r in rows:
            nf = norm_fields(r)
            eq = (
                nf["complete_norm"] is not None
                and nf["tied_norm"] is not None
                and abs(nf["complete_norm"] - nf["tied_norm"]) < PHI_TOL
            )
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_norm": nf["tied_norm"],
                "complete_norm": nf["complete_norm"],
                "equal": eq,
            })
    return decision


if __name__ == "__main__":
    main()
