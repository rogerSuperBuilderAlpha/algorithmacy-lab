#!/usr/bin/env python
"""Q50 / H5 — commit symmetry splits the party-read rule.

Run:  python -m org_frontier.questions.q50_or_triadic_seam.probe_commit_symmetry
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
    IMPLICATION_INDICES, LABELS, MAX_PHI, SYMMETRIC_INDICES, complementary_reads,
    instrument_control, matched_live_reads, s_index, w_index, c_index,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def main():
    print("PROBE 154 (H5) — commit symmetry splits the party-read rule")
    print("=" * 64)
    ctrl = instrument_control()
    print(f"[instrument control] canonical triad: triadic, max_phi={ctrl.max_phi:.3f}, "
          f"MIP={ctrl.mip_partition!r}  -> PASS")

    rows = []
    violations = []
    sym_matched = 0
    impl_comp = 0
    for label, rules in enumerate_family():
        v = verdict(rules, LABELS)
        if v.structure != "triadic" or abs(v.max_phi - MAX_PHI) > 1e-6:
            continue
        si = s_index(label)
        iw, ic = w_index(label), c_index(label)
        is_sym = si in SYMMETRIC_INDICES
        is_impl = si in IMPLICATION_INDICES
        matched = matched_live_reads(iw, ic)
        comp = complementary_reads(iw, ic)
        if is_sym:
            ok = matched
            sym_matched += 1 if matched else 0
        elif is_impl:
            ok = comp
            impl_comp += 1 if comp else 0
        else:
            ok = False
        rows.append({"label": label, "s_index": si, "w_index": iw, "c_index": ic,
                     "commit_class": "symmetric" if is_sym else ("implication" if is_impl else "other"),
                     "matched_live": matched, "complementary": comp, "rule_ok": ok})
        if not ok:
            violations.append(label)

    print(f"\n  monotone Phi=2.0 triadic forms: {len(rows)}  (expect 16)")
    print(f"  symmetric-commit with matched reads: {sym_matched}/8")
    print(f"  implication-commit with complementary reads: {impl_comp}/8")
    print(f"  cross-rule violations: {len(violations)}")
    for lab in violations:
        print(f"      {lab}")

    decision = "confirmed" if not violations else "refuted"
    print("\n=== Decision (rule fixed before run) ===")
    print(f"    zero cross-rule violations?  {not violations}")
    print(f"    H5 VERDICT: {decision.upper()}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "commit_symmetry.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["label", "s_index", "w_index", "c_index",
                                            "commit_class", "matched_live", "complementary",
                                            "rule_ok"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n  wrote results/commit_symmetry.csv ({len(rows)} rows)")
    return decision


if __name__ == "__main__":
    main()
