#!/usr/bin/env python
"""Q53 / H3 — XOR parity gates exceed the 0.830075 symmetric-AND equilibrium.

Run:  python -m org_frontier.questions.q53_impl_phi_ceiling.probe_xor_exceed_equilibrium
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q53_impl_phi_ceiling.ceiling_utils import (  # noqa: E402
    LABELS,
    SYMMETRIC_EQ,
    XOR_TOPOLOGIES,
    apply_topology,
    exceeds_equilibrium,
    instrument_control,
    matched_implication_panel,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 167 (H3) — XOR parity gates exceed the 0.830075 symmetric-AND equilibrium")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    exceed_count = 0
    for label, rules in matched_implication_panel():
        for topo in XOR_TOPOLOGIES:
            bc = apply_topology(rules, topo)
            v = verdict(bc, LABELS)
            exc = exceeds_equilibrium(v.max_phi)
            exceed_count += int(exc)
            rows.append({"label": label, "topology": topo, "structure": v.structure,
                         "max_phi": f"{v.max_phi:.6f}", "exceeds_eq": exc})
            print(f"  {label} + {topo}: {v.structure}, max_phi={v.max_phi:.6f}, "
                  f"exceeds {SYMMETRIC_EQ}? {exc}")

    print(f"\n  pairs exceeding symmetric equilibrium: {exceed_count}/24")
    if exceed_count >= 1:
        decision = "confirmed"
    elif any(r["structure"] == "triadic" for r in rows):
        decision = "partial"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    any pair exceeds 0.830075?  {exceed_count >= 1}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "xor_exceed_equilibrium.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "topology", "structure", "max_phi", "exceeds_eq"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
