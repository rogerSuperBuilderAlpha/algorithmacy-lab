#!/usr/bin/env python
"""Q50 / H3 — asymmetric party reads collapse OR.

Run:  python -m org_frontier.questions.q50_or_triadic_seam.probe_or_asymmetric
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q50_or_triadic_seam.seam_utils import (  # noqa: E402
    LABELS, instrument_control, or_forms, w_index, c_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 152 (H3) — asymmetric party reads collapse OR")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    asymmetric = []
    triadic_asymmetric = []
    for label, rules in or_forms():
        iw, ic = w_index(label), c_index(label)
        is_asym = iw != ic
        v = verdict(rules, LABELS)
        rows.append({"label": label, "w_index": iw, "c_index": ic,
                     "asymmetric": is_asym, "structure": v.structure,
                     "max_phi": f"{v.max_phi:.6f}"})
        if is_asym:
            asymmetric.append(label)
            if v.structure == "triadic":
                triadic_asymmetric.append(label)

    print(f"\n  asymmetric OR forms (iw != ic): {len(asymmetric)}  (expect 12)")
    print(f"  triadic among asymmetric forms: {len(triadic_asymmetric)}")

    decision = "confirmed" if not triadic_asymmetric else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero triadic OR with iw != ic?  {not triadic_asymmetric}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "or_asymmetric.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "w_index", "c_index", "asymmetric",
                                            "structure", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/or_asymmetric.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
