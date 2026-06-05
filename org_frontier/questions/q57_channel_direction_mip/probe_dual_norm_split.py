#!/usr/bin/env python
"""Q57 / H2 — dual at-system Phi with fixed normalized_phi split.

Run:  python -m org_frontier.questions.q57_channel_direction_mip.probe_dual_norm_split
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    EXCLUDED_NORM,
    PHI_TOL,
    TIED_NORM,
    enriched_rows,
    instrument_control,
    norm_fields,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 186 (H2) — dual at-system Phi with fixed normalized_phi split")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_rows()
    dual = norm_split = 0
    for r in rows:
        nf = norm_fields(r)
        tied_ok = nf["tied_norm"] is not None and abs(nf["tied_norm"] - TIED_NORM) < PHI_TOL
        excl_ok = nf["excl_norm"] is not None and abs(nf["excl_norm"] - EXCLUDED_NORM) < PHI_TOL
        if nf["dual_at_sys"]:
            dual += 1
        if nf["dual_at_sys"] and tied_ok and excl_ok:
            norm_split += 1

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  both outer cuts at system Phi: {dual}/{len(rows)}")
    print(f"  tied norm {TIED_NORM}, excluded norm {EXCLUDED_NORM}: {norm_split}/{len(rows)}")

    if norm_split == len(rows) == 16:
        decision = "confirmed"
    elif norm_split == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all dual at-system with 0.5/1.0 split?  {norm_split == len(rows)}")
    print(f"    H2 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "dual_norm_split.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "topology", "dual_at_sys", "tied_norm", "excl_norm",
            ],
        )
        w.writeheader()
        for r in rows:
            nf = norm_fields(r)
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "dual_at_sys": nf["dual_at_sys"],
                "tied_norm": nf["tied_norm"],
                "excl_norm": nf["excl_norm"],
            })
    return decision


if __name__ == "__main__":
    main()
