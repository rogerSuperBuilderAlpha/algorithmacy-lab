#!/usr/bin/env python
"""Q50 / H4 — binding OR forms share the canonical seam tie.

Run:  python -m org_frontier.questions.q50_or_triadic_seam.probe_or_seam
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q50_or_triadic_seam.seam_utils import (  # noqa: E402
    CANON, LABELS, MAX_PHI, OR_INDEX, instrument_control, seam_set, s_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
BINDING = ("W1_S7_C1", "W2_S7_C2")


def main():
    print("PROBE 153 (H4) — binding OR forms share the canonical seam tie")
    print("=" * 64)
    ctrl = instrument_control()
    ctrl_seam = seam_set(CANON, LABELS)
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}, seam={sorted(ctrl_seam)!r}  -> PASS")

    lookup = {label: rules for label, rules in enumerate_family()}
    rows = []
    violations = []
    for label in BINDING:
        rules = lookup[label]
        v = verdict(rules, LABELS)
        seam = seam_set(rules, LABELS)
        ok = (v.structure == "triadic" and abs(v.max_phi - MAX_PHI) < 1e-6
              and seam == ctrl_seam)
        rows.append({"label": label, "structure": v.structure,
                     "max_phi": f"{v.max_phi:.6f}",
                     "seam_set": "|".join(sorted(seam)),
                     "matches_control_seam": ok})
        print(f"\n  {label}: {v.structure}, max_phi={v.max_phi:.3f}, seam={sorted(seam)!r}")
        if not ok:
            violations.append(label)

    decision = "confirmed" if not violations else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    both binding OR forms triadic Phi=2.0 with control seam?  {not violations}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "or_seam.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "structure", "max_phi", "seam_set",
                                            "matches_control_seam"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/or_seam.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
