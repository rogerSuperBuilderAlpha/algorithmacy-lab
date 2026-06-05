#!/usr/bin/env python
"""Q52 / H2 — C-centric commits plateau at the mid rung.

Run:  python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_ccentric_plateau
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q52_phi_ladder_mechanism.ladder_utils import (  # noqa: E402
    C_CENTRIC, LABELS, MID_PHI, PHI_TOL, implication_forms, instrument_control,
    ladder_rung, matched_live_reads, s_index, worker_backchannel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 161 (H2) — C-centric commits plateau at the mid rung")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    at_mid = 0
    for label, rules in implication_forms(matched_live_reads):
        if s_index(label) not in C_CENTRIC:
            continue
        bc = worker_backchannel(rules)
        v = verdict(bc, LABELS)
        mid_ok = v.structure == "triadic" and abs(v.max_phi - MID_PHI) < PHI_TOL
        at_mid += int(mid_ok)
        rows.append({
            "label": label, "s_index": s_index(label), "structure": v.structure,
            "max_phi": f"{v.max_phi:.6f}", "rung": ladder_rung(label, v.structure, v.max_phi),
            "at_mid": mid_ok,
        })
        print(f"  {label}: {v.structure}, max_phi={v.max_phi:.6f}")

    print(f"\n  C-centric matched at mid rung (0.415037): {at_mid}/4")
    if at_mid == 4:
        decision = "confirmed"
    elif at_mid >= 1:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all four at mid?  {at_mid == 4}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "ccentric_plateau.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
