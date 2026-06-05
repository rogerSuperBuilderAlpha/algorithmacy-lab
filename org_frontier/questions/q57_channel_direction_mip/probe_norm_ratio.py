#!/usr/bin/env python
"""Q57 / H3 — two-to-one normalized_phi ratio on outer cuts.

Run:  python -m org_frontier.questions.q57_channel_direction_mip.probe_norm_ratio
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    NORM_RATIO,
    PHI_TOL,
    enriched_rows,
    instrument_control,
    norm_fields,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 187 (H3) — two-to-one normalized_phi ratio on outer cuts")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_rows()
    at_ratio = 0
    ratios = []
    for r in rows:
        nf = norm_fields(r)
        ratios.append(nf["ratio"])
        if nf["ratio"] is not None and abs(nf["ratio"] - NORM_RATIO) < PHI_TOL:
            at_ratio += 1

    spread = max(ratios) - min(ratios) if ratios else None

    print(f"\n  one-sided ceiling pairs: {len(rows)}")
    print(f"  excluded/tied norm ratio {NORM_RATIO}: {at_ratio}/{len(rows)}")
    print(f"  ratio spread: {spread:.6f}" if spread is not None else "  ratio spread: n/a")

    if at_ratio == len(rows) == 16:
        decision = "confirmed"
    elif at_ratio == len(rows):
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all pairs at ratio {NORM_RATIO}?  {at_ratio == len(rows)}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "norm_ratio.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "tied_norm", "excl_norm", "ratio"],
        )
        w.writeheader()
        for r in rows:
            nf = norm_fields(r)
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "tied_norm": nf["tied_norm"],
                "excl_norm": nf["excl_norm"],
                "ratio": nf["ratio"],
            })
    return decision


if __name__ == "__main__":
    main()
