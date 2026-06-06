#!/usr/bin/env python
"""Q45 / H4 — OR commits do not bind triadically in strict mediation.

Run:  python -m org_frontier.questions.q45_edge_floor_uniqueness.probe_or_strict
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.questions.q45_edge_floor_uniqueness.floor_utils import (  # noqa: E402
    LABELS, OR_INDEX, instrument_control, s_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 148 (H4) — OR commits do not bind triadically in strict mediation")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    triadic_or = []
    for label, rules in enumerate_family():
        si = s_index(label)
        if si != OR_INDEX:
            continue
        v = verdict(rules, LABELS)
        rows.append({"label": label, "structure": v.structure,
                     "max_phi": f"{v.max_phi:.6f}"})
        if v.structure == "triadic":
            triadic_or.append(label)

    print(f"\n  OR-commit forms (S-index {OR_INDEX}): {len(rows)}  (expect 16)")
    print(f"  triadic OR forms: {len(triadic_or)}")
    for lab in triadic_or[:5]:
        print(f"      {lab}")

    decision = "confirmed" if not triadic_or else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero triadic OR forms?  {not triadic_or}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "or_strict.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/or_strict.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
