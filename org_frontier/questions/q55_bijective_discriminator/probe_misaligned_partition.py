#!/usr/bin/env python
"""Q55 / H1 — misaligned one-sided parity exhausts the below-ceiling set.

Run:  python -m org_frontier.questions.q55_bijective_discriminator.probe_misaligned_partition
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q55_bijective_discriminator.discriminator_utils import (  # noqa: E402
    bijective_parity_panel,
    instrument_control,
    is_one_sided,
    split_below_ceiling,
    xor_misaligned,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 175 (H1) — misaligned one-sided parity exhausts the below-ceiling set")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = bijective_parity_panel()
    below, ceiling = split_below_ceiling(rows)

    below_misaligned = sum(
        1 for r in below if is_one_sided(r["topology"]) and xor_misaligned(r["label"], r["topology"])
    )
    below_symmetric = sum(1 for r in below if not is_one_sided(r["topology"]))
    below_aligned = sum(
        1 for r in below
        if is_one_sided(r["topology"]) and not xor_misaligned(r["label"], r["topology"])
    )
    ceiling_one_sided = sum(1 for r in ceiling if is_one_sided(r["topology"]))
    ceiling_symmetric = sum(1 for r in ceiling if not is_one_sided(r["topology"]))

    print(f"\n  bijective parity pairs: {len(rows)}")
    print(f"  below ceiling: {len(below)}")
    print(f"  at ceiling: {len(ceiling)}")
    print(f"  below misaligned one-sided: {below_misaligned}/{len(below)}")
    print(f"  below symmetric: {below_symmetric}")
    print(f"  below aligned one-sided: {below_aligned}")
    print(f"  ceiling one-sided: {ceiling_one_sided}")
    print(f"  ceiling symmetric: {ceiling_symmetric}")

    if (
        below_misaligned == len(below) == 16
        and below_symmetric == 0
        and below_aligned == 0
        and len(ceiling) == 32
    ):
        decision = "confirmed"
    elif below_misaligned == len(below) and below_symmetric == 0 and below_aligned == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all below misaligned one-sided?  {below_misaligned == len(below)}")
    print(f"    zero below symmetric?  {below_symmetric == 0}")
    print(f"    zero below aligned one-sided?  {below_aligned == 0}")
    print(f"    H1 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "misaligned_partition.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "s_index", "topology", "max_phi", "at_ceiling",
                        "one_sided", "misaligned"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "s_index": r["s_index"],
                "topology": r["topology"],
                "max_phi": f"{r['max_phi']:.6f}",
                "at_ceiling": r["at_ceiling"],
                "one_sided": is_one_sided(r["topology"]),
                "misaligned": xor_misaligned(r["label"], r["topology"]),
            })
    return decision


if __name__ == "__main__":
    main()
