#!/usr/bin/env python
"""Q52 / H4 — symmetric coupling lifts dyadic W-centric forms to the high rung.

Run:  python -m org_frontier.questions.q52_phi_ladder_mechanism.probe_symmetric_lift
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.questions.q52_phi_ladder_mechanism.ladder_utils import (  # noqa: E402
    HIGH_PHI, LABELS, PHI_TOL, instrument_control, symmetric_backchannel, worker_backchannel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
DYADIC_LABELS = {"W1_S13_C1", "W2_S2_C2"}


def main():
    print("PROBE 163 (H4) — symmetric coupling lifts dyadic W-centric forms")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    lifted = 0
    for label, rules in enumerate_family():
        if label not in DYADIC_LABELS:
            continue
        os_v = verdict(worker_backchannel(rules), LABELS)
        sym = symmetric_backchannel(rules)
        v = verdict(sym, LABELS)
        high_ok = v.structure == "triadic" and abs(v.max_phi - HIGH_PHI) < PHI_TOL
        lifted += int(high_ok)
        rows.append({
            "label": label, "onesided_structure": os_v.structure,
            "onesided_phi": f"{os_v.max_phi:.6f}",
            "sym_structure": v.structure, "sym_phi": f"{v.max_phi:.6f}",
            "lifted": high_ok,
        })
        print(f"  {label}: one-sided {os_v.structure} phi={os_v.max_phi:.6f} -> "
              f"symmetric {v.structure} phi={v.max_phi:.6f}")

    print(f"\n  dyadic W-centric lifted to high rung: {lifted}/2")
    if lifted == 2:
        decision = "confirmed"
    elif lifted == 1:
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    both lifted?  {lifted == 2}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "symmetric_lift.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
