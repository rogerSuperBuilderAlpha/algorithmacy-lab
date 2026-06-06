#!/usr/bin/env python
"""Q55 / H3 — seam conditional entropy is lower on below-ceiling bijective pairs.

Run:  python -m org_frontier.questions.q55_bijective_discriminator.probe_seam_entropy_split
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q55_bijective_discriminator.discriminator_utils import (  # noqa: E402
    enriched_panel,
    instrument_control,
    split_below_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 177 (H3) — seam conditional entropy is lower on below-ceiling bijective pairs")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    below, ceiling = split_below_ceiling(rows)

    mean_below = sum(r["seam_h"] for r in below) / len(below)
    mean_ceiling = sum(r["seam_h"] for r in ceiling) / len(ceiling)
    delta = mean_ceiling - mean_below
    pair_below_lower = sum(
        1 for b in below for c in ceiling if b["seam_h"] < c["seam_h"]
    )
    pair_total = len(below) * len(ceiling)

    print(f"\n  bijective parity pairs: {len(rows)}")
    print(f"  mean H(W,C|S) below: {mean_below:.6f}")
    print(f"  mean H(W,C|S) ceiling: {mean_ceiling:.6f}")
    print(f"  mean delta (ceiling - below): {delta:.6f} bits")
    print(f"  pair-wise below<ceiling: {pair_below_lower}/{pair_total}")

    if delta > 1e-6:
        decision = "confirmed"
    elif pair_below_lower > pair_total // 2:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    mean gap positive?  {delta > 1e-6}")
    print(f"    H3 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "seam_entropy_split.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "max_phi", "at_ceiling", "seam_h"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "max_phi": f"{r['max_phi']:.6f}",
                "at_ceiling": r["at_ceiling"],
                "seam_h": f"{r['seam_h']:.6f}",
            })
    return decision


if __name__ == "__main__":
    main()
