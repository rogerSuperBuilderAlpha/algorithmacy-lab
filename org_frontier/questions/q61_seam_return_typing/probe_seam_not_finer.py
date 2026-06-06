#!/usr/bin/env python
"""Q61 / H3 — seam is not a strict refinement of return-path type.

Run:  python -m org_frontier.questions.q61_seam_return_typing.probe_seam_not_finer
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q61_seam_return_typing.seam_return_utils import (  # noqa: E402
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 207 (H3) — seam not finer than return-path type")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    seq_c_seam = sum(
        1 for r in rows if r["thompson_type"] == "sequential" and r["singleton"] == "C"
    )
    rec_w_seam = sum(
        1 for r in rows if r["thompson_type"] == "reciprocal" and r["singleton"] == "W"
    )
    heterogeneity = seq_c_seam + rec_w_seam

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  sequential with C seam: {seq_c_seam}/8")
    print(f"  reciprocal with W seam: {rec_w_seam}/8")
    print(f"  within-type seam heterogeneity: {heterogeneity}/{len(rows)}")

    if heterogeneity == 0:
        decision = "confirmed"
    elif heterogeneity == 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    heterogeneity count zero?  {heterogeneity == 0}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_not_finer.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "singleton", "thompson_type", "heterogeneous"],
        )
        w.writeheader()
        for r in rows:
            het = (
                (r["thompson_type"] == "sequential" and r["singleton"] == "C")
                or (r["thompson_type"] == "reciprocal" and r["singleton"] == "W")
            )
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "singleton": r["singleton"],
                "thompson_type": r["thompson_type"],
                "heterogeneous": het,
            })
    return decision


if __name__ == "__main__":
    main()
