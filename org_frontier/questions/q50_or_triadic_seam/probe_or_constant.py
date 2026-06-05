#!/usr/bin/env python
"""Q50 / H2 — constant party reads exclude OR binding.

Run:  python -m org_frontier.questions.q50_or_triadic_seam.probe_or_constant
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
    CONSTANT_INDICES, LABELS, instrument_control, or_forms, w_index, c_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 151 (H2) — constant party reads exclude OR binding")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    constant_forms = []
    triadic_constant = []
    for label, rules in or_forms():
        iw, ic = w_index(label), c_index(label)
        has_constant = iw in CONSTANT_INDICES or ic in CONSTANT_INDICES
        v = verdict(rules, LABELS)
        rows.append({"label": label, "w_index": iw, "c_index": ic,
                     "has_constant_read": has_constant, "structure": v.structure,
                     "max_phi": f"{v.max_phi:.6f}"})
        if has_constant:
            constant_forms.append(label)
            if v.structure == "triadic":
                triadic_constant.append(label)

    print(f"\n  OR forms with any constant party read: {len(constant_forms)}")
    print(f"  triadic among constant-read forms: {len(triadic_constant)}")

    decision = "confirmed" if not triadic_constant else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero triadic OR with constant read?  {not triadic_constant}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "or_constant.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "w_index", "c_index", "has_constant_read",
                                            "structure", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/or_constant.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
