#!/usr/bin/env python
"""Q62 / H3 — excluded determined by tied singleton.

Run:  python -m org_frontier.questions.q62_excluded_cut_signal.probe_tied_determines_excluded
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q62_excluded_cut_signal.excluded_cut_utils import (  # noqa: E402
    PANEL_SIZE,
    enriched_panel,
    instrument_control,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 212 (H3) — excluded determined by tied singleton")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    w_tied_excl_w = sum(
        1 for r in rows if r["tied_singleton"] == "W" and r["excluded_singleton"] == "W"
    )
    c_tied_excl_c = sum(
        1 for r in rows if r["tied_singleton"] == "C" and r["excluded_singleton"] == "C"
    )
    heterogeneity = w_tied_excl_w + c_tied_excl_c

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  W-tied with excluded W: {w_tied_excl_w}/8")
    print(f"  C-tied with excluded C: {c_tied_excl_c}/8")
    print(f"  within-tied excluded heterogeneity: {heterogeneity}/{len(rows)}")

    if heterogeneity == 0:
        decision = "confirmed"
    elif heterogeneity == 1:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    heterogeneity count 0?  {heterogeneity == 0}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "tied_determines_excluded.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_singleton", "excluded_singleton"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_singleton": r["tied_singleton"],
                "excluded_singleton": r["excluded_singleton"],
            })
    return decision


if __name__ == "__main__":
    main()
