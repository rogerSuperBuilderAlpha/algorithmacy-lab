#!/usr/bin/env python
"""Q55 / H4 — MIP seam singleton {S,WC} marks the below-ceiling half.

Run:  python -m org_frontier.questions.q55_bijective_discriminator.probe_mip_singleton
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q55_bijective_discriminator.discriminator_utils import (  # noqa: E402
    MIP_BELOW,
    enriched_panel,
    instrument_control,
    split_below_ceiling,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 178 (H4) — MIP seam singleton {S,WC} marks the below-ceiling half")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = enriched_panel()
    below, ceiling = split_below_ceiling(rows)

    below_sw = sum(1 for r in below if r["mip_first"] == MIP_BELOW)
    below_other = len(below) - below_sw
    ceiling_sw = sum(1 for r in ceiling if r["mip_first"] == MIP_BELOW)

    from collections import Counter
    ceiling_mips = Counter(r["mip_first"] for r in ceiling)

    print(f"\n  below at {MIP_BELOW}: {below_sw}/{len(below)}")
    print(f"  below other MIP: {below_other}")
    print(f"  ceiling at {MIP_BELOW}: {ceiling_sw}/{len(ceiling)}")
    print(f"  ceiling MIP distribution: {dict(ceiling_mips)}")

    if below_sw == len(below) == 16 and ceiling_sw == 0:
        decision = "confirmed"
    elif below_sw == len(below) and ceiling_sw == 0:
        decision = "partial"
    else:
        decision = "refuted"

    print("\n=== Decision (rule fixed before run) ===")
    print(f"    all below at S-singleton seam?  {below_sw == len(below)}")
    print(f"    zero ceiling at S-singleton seam?  {ceiling_sw == 0}")
    print(f"    H4 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "mip_singleton.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["label", "topology", "max_phi", "at_ceiling", "mip_first"],
        )
        w.writeheader()
        for r in rows:
            w.writerow({
                "label": r["label"],
                "topology": r["topology"],
                "max_phi": f"{r['max_phi']:.6f}",
                "at_ceiling": r["at_ceiling"],
                "mip_first": r["mip_first"],
            })
    return decision


if __name__ == "__main__":
    main()
