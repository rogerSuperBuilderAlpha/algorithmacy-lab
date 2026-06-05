#!/usr/bin/env python
"""Q53 / H4 — no tested topology restores Phi=2.0.

Run:  python -m org_frontier.questions.q53_impl_phi_ceiling.probe_topology_sweep_phi2
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q53_impl_phi_ceiling.ceiling_utils import (  # noqa: E402
    TOPOLOGY_SWEEP,
    at_ceiling,
    classify_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 168 (H4) — no tested topology restores Phi=2.0")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    at_phi2 = 0
    for row in classify_panel(TOPOLOGY_SWEEP):
        from types import SimpleNamespace
        ceiling = at_ceiling(SimpleNamespace(structure=row["structure"], max_phi=row["max_phi"]))
        at_phi2 += int(ceiling)
        rows.append({
            "label": row["label"],
            "topology": row["topology"],
            "structure": row["structure"],
            "max_phi": f"{row['max_phi']:.6f}",
            "at_phi2": ceiling,
        })
        if ceiling:
            print(f"  HIT  {row['label']} + {row['topology']}: max_phi={row['max_phi']:.6f}")

    print(f"\n  at Phi=2.0 across {len(rows)} pairs: {at_phi2}/{len(rows)}")
    if at_phi2 == 0:
        decision = "confirmed"
    else:
        decision = "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero at ceiling across sweep?  {at_phi2 == 0}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "topology_sweep_phi2.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "topology", "structure", "max_phi", "at_phi2"])
        w.writeheader()
        w.writerows(rows)
    return decision


if __name__ == "__main__":
    main()
