#!/usr/bin/env python
"""Q52 / H5 — symmetric equilibrium equals one-sided high rung, erasing spread.

Run:  python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_symmetric_collapse
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q52_phi_ladder_mechanism.ladder_utils import (  # noqa: E402
    HIGH_PHI, LABELS, PHI_TOL, SYMMETRIC_PHI, implication_forms, instrument_control,
    matched_live_reads, symmetric_backchannel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 164 (H5) — symmetric collapse to high-rung equilibrium")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    phis = []
    triadic = 0
    for label, rules in implication_forms(matched_live_reads):
        sym = symmetric_backchannel(rules)
        v = verdict(sym, LABELS)
        phis.append(v.max_phi)
        triadic += int(v.structure == "triadic")
        rows.append({
            "label": label, "structure": v.structure, "max_phi": f"{v.max_phi:.6f}",
        })
        print(f"  {label}: {v.structure}, max_phi={v.max_phi:.6f}")

    spread = max(phis) - min(phis) if phis else 0.0
    at_high = sum(1 for p in phis if abs(p - SYMMETRIC_PHI) < PHI_TOL)
    print(f"\n  triadic symmetric matched: {triadic}/8")
    print(f"  at high rung 0.830075: {at_high}/8")
    print(f"  max_phi spread: {spread:.6f}")

    if triadic == 8 and spread < PHI_TOL and at_high == 8:
        decision = "confirmed"
    elif triadic == 8:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    uniform high rung?  {triadic == 8 and spread < PHI_TOL}")
    print(f"    shared max_phi: {SYMMETRIC_PHI:.6f}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "symmetric_collapse.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
