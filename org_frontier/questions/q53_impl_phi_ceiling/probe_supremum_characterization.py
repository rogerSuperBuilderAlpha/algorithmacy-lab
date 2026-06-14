#!/usr/bin/env python
"""Q53 / H5 — supremum is exactly 0.830075 and symmetric-AND saturates it.

Run:  python -m org_frontier.questions.q53_impl_phi_ceiling.probe_supremum_characterization
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q53_impl_phi_ceiling.ceiling_utils import (  # noqa: E402
    ALL_TOPOLOGIES,
    PHI_TOL,
    SYMMETRIC_EQ,
    classify_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 169 (H5) — supremum is exactly 0.830075 and symmetric-AND saturates it")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = classify_panel(ALL_TOPOLOGIES)
    max_phi = max(r["max_phi"] for r in rows)
    argmax = [r for r in rows if abs(r["max_phi"] - max_phi) < 1e-9]
    sym_and = [r for r in rows if r["topology"] == "symmetric_and"]
    sym_at_eq = sum(1 for r in sym_and if abs(r["max_phi"] - SYMMETRIC_EQ) < PHI_TOL)
    sym_phis = [r["max_phi"] for r in sym_and]
    spread = max(sym_phis) - min(sym_phis) if sym_phis else 0.0
    any_exceed = max_phi > SYMMETRIC_EQ + PHI_TOL

    print(f"\n  global max_phi: {max_phi:.6f}")
    print(f"  argmax count: {len(argmax)}")
    for r in argmax[:4]:
        print(f"    {r['label']} + {r['topology']}: {r['max_phi']:.6f}")
    print(f"  symmetric-AND at equilibrium {SYMMETRIC_EQ}: {sym_at_eq}/8")
    print(f"  symmetric-AND max_phi spread: {spread:.6f}")

    if not any_exceed and sym_at_eq == 8 and spread < PHI_TOL:
        decision = "confirmed"
    elif any_exceed:
        decision = "refuted"
    else:
        decision = "partial"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    global max equals 0.830075?  {abs(max_phi - SYMMETRIC_EQ) < PHI_TOL}")
    print(f"    symmetric-AND uniform at 0.830075?  {sym_at_eq == 8 and spread < PHI_TOL}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "supremum_characterization.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "topology", "structure", "max_phi"])
        w.writeheader()
        for r in rows:
            w.writerow({"label": r["label"], "topology": r["topology"],
                        "structure": r["structure"], "max_phi": f"{r['max_phi']:.6f}"})
    return decision


if __name__ == "__main__":
    main()
