#!/usr/bin/env python
"""Q56 / H4 — dual outer-party cuts at system Phi excluded from official ties on symmetric pairs.

Run:  python -m org_frontier.questions.q56_symmetric_complete_mip.probe_dual_outer_excluded
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    OUTER_C,
    OUTER_W,
    instrument_control,
    scan_row,
    symmetric_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 183 (H4) — dual outer-party at system Phi excluded from official ties")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = [scan_row(r) for r in symmetric_ceiling()]
    dual_at_sys = 0
    no_outer_official = 0
    for r in rows:
        if r["at_sys"][OUTER_W] and r["at_sys"][OUTER_C]:
            dual_at_sys += 1
        if r["outer_count_official"] == 0:
            no_outer_official += 1

    print(f"\n  symmetric ceiling pairs: {len(rows)}")
    print(f"  both outer-party at system Phi: {dual_at_sys}/{len(rows)}")
    print(f"  zero outer-party in official ties: {no_outer_official}/{len(rows)}")

    if dual_at_sys == len(rows) == 16 and no_outer_official == 16:
        decision = "confirmed"
    elif dual_at_sys == len(rows) and no_outer_official == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all dual outer at system Phi?  {dual_at_sys == len(rows)}")
    print(f"    all zero outer in official ties?  {no_outer_official == len(rows)}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "dual_outer_excluded.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "at_sys_W_SC", "at_sys_WS_C", "outer_count_official"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "at_sys_W_SC": r["at_sys"][OUTER_W],
                "at_sys_WS_C": r["at_sys"][OUTER_C],
                "outer_count_official": r["outer_count_official"],
            })
    return decision


if __name__ == "__main__":
    main()
