#!/usr/bin/env python
"""Q55 / H5 — XNOR inverts one-sided alignment polarity relative to XOR.

Run:  python -m org_frontier.questions.q55_bijective_discriminator.probe_xnor_alignment_flip
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
    xnor_aligned_at_ceiling,
    xor_aligned_at_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 179 (H5) — XNOR inverts one-sided alignment polarity relative to XOR")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = bijective_parity_panel()
    one_sided = [r for r in rows if r["topology"] in (
        "worker_xor", "counterpart_xor", "worker_xnor", "counterpart_xnor"
    )]

    xnor_ceiling = [r for r in one_sided if "xnor" in r["topology"] and r["at_ceiling"]]
    xnor_misaligned = sum(
        1 for r in xnor_ceiling
        if not xnor_aligned_at_ceiling(r["label"], r["topology"])
    )

    xor_aligned_rows = [
        r for r in one_sided
        if "xor" in r["topology"] and "xnor" not in r["topology"]
        and xor_aligned_at_ceiling(r["label"], r["topology"])
    ]
    xor_aligned_at_phi2 = sum(1 for r in xor_aligned_rows if r["at_ceiling"])
    xor_aligned_miss = len(xor_aligned_rows) - xor_aligned_at_phi2

    worker_xnor_wcentric = sum(
        1 for r in xnor_ceiling
        if r["topology"] == "worker_xnor" and r["s_index"] in {2, 13}
    )
    counterpart_xnor_ccentric = sum(
        1 for r in xnor_ceiling
        if r["topology"] == "counterpart_xnor" and r["s_index"] in {4, 11}
    )

    print(f"\n  one-sided parity pairs: {len(one_sided)}")
    print(f"  XNOR ceiling hits: {len(xnor_ceiling)}")
    print(f"  XNOR ceiling misalignments: {xnor_misaligned}")
    print(f"  worker_xnor at ceiling (W-centric): {worker_xnor_wcentric}/4")
    print(f"  counterpart_xnor at ceiling (C-centric): {counterpart_xnor_ccentric}/4")
    print(f"  XOR aligned one-sided at ceiling: {xor_aligned_at_phi2}/{len(xor_aligned_rows)}")
    print(f"  XOR aligned misses: {xor_aligned_miss}")

    if (
        xnor_misaligned == 0
        and xor_aligned_miss == 0
        and worker_xnor_wcentric == len(xnor_ceiling) // 2
        and counterpart_xnor_ccentric == len(xnor_ceiling) // 2
    ):
        decision = "confirmed"
    elif xnor_misaligned == 0 and xor_aligned_miss == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero XNOR ceiling misalignments?  {xnor_misaligned == 0}")
    print(f"    all XOR aligned at ceiling?  {xor_aligned_miss == 0}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "xnor_alignment_flip.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "max_phi", "at_ceiling",
                        "xor_aligned", "xnor_aligned"],
        )
        w.writeheader()
        for r in one_sided:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "max_phi": f"{r['max_phi']:.6f}",
                "at_ceiling": r["at_ceiling"],
                "xor_aligned": xor_aligned_at_ceiling(r["label"], r["topology"]),
                "xnor_aligned": xnor_aligned_at_ceiling(r["label"], r["topology"]),
            })
    return decision


if __name__ == "__main__":
    main()
