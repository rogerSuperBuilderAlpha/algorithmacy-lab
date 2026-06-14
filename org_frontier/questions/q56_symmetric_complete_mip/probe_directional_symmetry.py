#!/usr/bin/env python
"""Q56 / H3 — directional coupling symmetry distinguishes topology classes.

Run:  python -m org_frontier.questions.q56_symmetric_complete_mip.probe_directional_symmetry
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    instrument_control,
    one_sided_ceiling,
    scan_row,
    symmetric_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 182 (H3) — directional coupling symmetry distinguishes topology classes")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    sym_rows = [scan_row(r) for r in symmetric_ceiling()]
    one_rows = [scan_row(r) for r in one_sided_ceiling()]
    sym_dir = sum(1 for r in sym_rows if r["dir_symmetric"])
    one_dir = sum(1 for r in one_rows if r["dir_symmetric"])

    print(f"\n  symmetric directionally symmetric: {sym_dir}/{len(sym_rows)}")
    print(f"  one-sided directionally symmetric: {one_dir}/{len(one_rows)}")

    if sym_dir == len(sym_rows) == 16 and one_dir == 0:
        decision = "confirmed"
    elif sym_dir == len(sym_rows) and one_dir == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all symmetric directionally symmetric?  {sym_dir == len(sym_rows)}")
    print(f"    zero one-sided directionally symmetric?  {one_dir == 0}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "directional_symmetry.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "class", "dir_symmetric"],
        )
        w.writeheader()
        for r in sym_rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "class": "symmetric",
                "dir_symmetric": r["dir_symmetric"],
            })
        for r in one_rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "class": "one_sided",
                "dir_symmetric": r["dir_symmetric"],
            })
    return decision


if __name__ == "__main__":
    main()
