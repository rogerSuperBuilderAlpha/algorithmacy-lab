#!/usr/bin/env python
"""Q54 / H5 — parity-class gates are necessary for Phi=2.0 restoration.

Run:  python -m org_frontier.questions.q54_xor_parity_mechanism.probe_parity_necessity
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q54_xor_parity_mechanism.mechanism_utils import (  # noqa: E402
    LABELS,
    TOPOLOGY_SWEEP,
    apply_any_topology,
    at_ceiling,
    instrument_control,
    matched_implication_panel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 174 (H5) — parity-class gates are necessary for Phi=2.0 restoration")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    monotone_at_ceiling = 0
    xnor_at_ceiling = 0
    for label, rules in matched_implication_panel():
        for topo in TOPOLOGY_SWEEP:
            bc = apply_any_topology(rules, topo)
            v = verdict(bc, LABELS)
            hit = at_ceiling(v)
            if hit:
                monotone_at_ceiling += 1
            rows.append({
                "label": label, "topology": topo, "gate_class": "monotone",
                "structure": v.structure, "max_phi": v.max_phi, "at_ceiling": hit,
            })
        bc_xnor = apply_any_topology(rules, "symmetric_xnor")
        v_xnor = verdict(bc_xnor, LABELS)
        hit_xnor = at_ceiling(v_xnor)
        if hit_xnor:
            xnor_at_ceiling += 1
        rows.append({
            "label": label, "topology": "symmetric_xnor", "gate_class": "parity",
            "structure": v_xnor.structure, "max_phi": v_xnor.max_phi, "at_ceiling": hit_xnor,
        })
        print(f"  {label}: symmetric_xnor max_phi={v_xnor.max_phi:.6f} ceiling={hit_xnor}")

    print(f"\n  monotone pairs at Phi=2.0: {monotone_at_ceiling}/64")
    print(f"  symmetric_xnor at Phi=2.0: {xnor_at_ceiling}/8")

    if monotone_at_ceiling == 0 and xnor_at_ceiling == 8:
        decision = "confirmed"
    elif monotone_at_ceiling == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    monotone at ceiling:  {monotone_at_ceiling}/64")
    print(f"    symmetric_xnor at ceiling:  {xnor_at_ceiling}/8")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "parity_necessity.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "gate_class", "structure", "max_phi", "at_ceiling"],
        )
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["max_phi"] = f"{out['max_phi']:.6f}"
            w.writerow(out)
    return decision


if __name__ == "__main__":
    main()
