#!/usr/bin/env python
"""Q54 / H3 — seam conditional entropy peaks at Phi=2.0 XOR pairs.

Run:  python -m org_frontier.questions.q54_xor_parity_mechanism.probe_seam_entropy
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
    apply_any_topology,
    instrument_control,
    matched_implication_panel,
    seam_cond_entropy_wc_given_s,
)
from org_frontier.probes.lib import verdict  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 172 (H3) — seam conditional entropy peaks at Phi=2.0 XOR pairs")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    xor_vals = []
    and_vals = []
    for label, rules in matched_implication_panel():
        bc_xor = apply_any_topology(rules, "symmetric_xor")
        bc_and = apply_any_topology(rules, "symmetric_and")
        v_xor = verdict(bc_xor, LABELS)
        v_and = verdict(bc_and, LABELS)
        h_xor = seam_cond_entropy_wc_given_s(bc_xor)
        h_and = seam_cond_entropy_wc_given_s(bc_and)
        xor_vals.append(h_xor)
        and_vals.append(h_and)
        rows.append({
            "label": label,
            "h_wc_given_s_xor": h_xor,
            "h_wc_given_s_and": h_and,
            "delta": h_xor - h_and,
            "max_phi_xor": v_xor.max_phi,
            "max_phi_and": v_and.max_phi,
        })
        print(f"  {label}: H(W,C|S) xor={h_xor:.6f} and={h_and:.6f} delta={h_xor - h_and:.6f}")

    mean_xor = sum(xor_vals) / len(xor_vals)
    mean_and = sum(and_vals) / len(and_vals)
    mean_delta = mean_xor - mean_and
    xor_higher_count = sum(1 for r in rows if r["delta"] > 0)

    print(f"\n  mean H(W,C|S) symmetric_xor: {mean_xor:.6f}")
    print(f"  mean H(W,C|S) symmetric_and: {mean_and:.6f}")
    print(f"  mean delta (xor - and): {mean_delta:.6f}")
    print(f"  forms with xor > and: {xor_higher_count}/8")

    if mean_delta > 1e-6:
        decision = "confirmed"
    elif xor_higher_count >= 5:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    mean delta > 0?  {mean_delta > 1e-6}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_entropy.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "h_wc_given_s_xor", "h_wc_given_s_and", "delta",
                        "max_phi_xor", "max_phi_and"],
        )
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["h_wc_given_s_xor"] = f"{out['h_wc_given_s_xor']:.6f}"
            out["h_wc_given_s_and"] = f"{out['h_wc_given_s_and']:.6f}"
            out["delta"] = f"{out['delta']:.6f}"
            out["max_phi_xor"] = f"{out['max_phi_xor']:.6f}"
            out["max_phi_and"] = f"{out['max_phi_and']:.6f}"
            w.writerow(out)
    return decision


if __name__ == "__main__":
    main()
