#!/usr/bin/env python
"""Q50 / H1 — matched non-constant party reads bind OR.

Run:  python -m org_frontier.questions.q50_or_triadic_seam.probe_or_matched
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
    LABELS, instrument_control, matched_live_reads, or_forms, w_index, c_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
EXPECTED_TRIADIC = {"W1_S7_C1", "W2_S7_C2"}


def main():
    print("PROBE 150 (H1) — matched non-constant party reads bind OR")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    triadic = set()
    false_pos = []
    false_neg = []
    for label, rules in or_forms():
        iw, ic = w_index(label), c_index(label)
        v = verdict(rules, LABELS)
        pred = matched_live_reads(iw, ic)
        rows.append({"label": label, "w_index": iw, "c_index": ic,
                     "matched_live": pred, "structure": v.structure,
                     "max_phi": f"{v.max_phi:.6f}"})
        if v.structure == "triadic":
            triadic.add(label)
        if pred and v.structure != "triadic":
            false_pos.append(label)
        if not pred and v.structure == "triadic":
            false_neg.append(label)

    print(f"\n  OR-commit forms: {len(rows)}  (expect 16)")
    print(f"  triadic OR forms: {len(triadic)}")
    print(f"  matched-live predicate matches triadic set: {triadic == EXPECTED_TRIADIC}")
    print(f"  false positives (matched-live but dyadic): {len(false_pos)}")
    print(f"  false negatives (triadic but not matched-live): {len(false_neg)}")

    ok = triadic == EXPECTED_TRIADIC and not false_pos and not false_neg
    decision = "confirmed" if ok else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    triadic set equals {{W1_S7_C1, W2_S7_C2}}?  {triadic == EXPECTED_TRIADIC}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "or_matched.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "w_index", "c_index", "matched_live",
                                            "structure", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/or_matched.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
