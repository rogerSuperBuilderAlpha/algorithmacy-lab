"""Random coupling ensemble at n=5 (extends agenda #18).

Reuses generators from analyze_ensemble.py. Hypotheses in hypotheses_n5.md.

Run:  python org_frontier/studies/random_coupling_ensemble/analyze_ensemble_n5.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from collections import Counter

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import pool
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import (
    BASE_SEED,
    ba_ins,
    er_ins,
    fixed_k_ins,
    run_ensemble,
    ws_ins,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

# L5 from hypotheses_n5.md / interior_ring_pool n=5 landmarks
LANDMARKS_N5 = {2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 20.0}
BETWEEN_ATOMS = {6.0, 8.0, 12.0}


def main():
    print("RANDOM COUPLING ENSEMBLE n=5 — extends agenda #18")
    print("=" * 80)
    print("  cited: n=4 DISCRETE_LANDMARKS; interior_ring_pool n=5 landmarks")
    print("  hypotheses fixed in hypotheses_n5.md before computing")
    print("  N≈92 total (~5–10s/sample; candid runtime)")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("POLE LANDMARKS n=5")
    print("-" * 80)
    labels5 = tuple(f"N{i}" for i in range(5))
    _, ring_phi = major_complex(ring(5), labels5)
    _, pool_phi = major_complex(pool(5), labels5)
    print(f"  ring5 coreΦ={float(ring_phi):.3f}  pool5 coreΦ={float(pool_phi):.3f}")
    print()

    # Patch landmark set used inside run_ensemble for n=5
    import org_frontier.studies.random_coupling_ensemble.analyze_ensemble as ae
    ae.LANDMARKS_N5 = LANDMARKS_N5

    all_rows = []
    summaries = []
    by_ens = {}

    print("ENSEMBLES n=5")
    print("-" * 80)
    specs = [
        ("ER_p0.4", lambda rng: er_ins(5, 0.4, rng), 20, 1100),
        ("fixed_k2", lambda rng: fixed_k_ins(5, 2, rng), 20, 1200),
        ("fixed_k3", lambda rng: fixed_k_ins(5, 3, rng), 16, 1300),
        ("WS_p0.3", lambda rng: ws_ins(5, 0.3, rng), 20, 1400),
        ("BA_m2", lambda rng: ba_ins(5, 2, rng), 16, 1500),
    ]
    for name, builder, N, off in specs:
        rows, summ = run_ensemble(name, builder, 5, N, off)
        all_rows.extend(rows)
        summaries.append(summ)
        by_ens[name] = (rows, summ)
    print()

    phis = [r["core_phi"] for r in all_rows]
    n_tot = len(phis)
    on_land = sum(1 for p in phis if round(float(p), 6) in LANDMARKS_N5)
    on_land_frac = on_land / n_tot
    off = [round(float(p), 6) for p in phis if round(float(p), 6) not in LANDMARKS_N5]
    hist = Counter(round(float(p), 3) for p in phis)

    h1_ctrl = (
        ctrl
        and abs(float(ring_phi) - 4.0) < PHI_EPS
        and abs(float(pool_phi) - 20.0) < PHI_EPS
    )
    h1 = h1_ctrl and on_land_frac >= 0.90 - 1e-12
    h2 = len(off) >= 1  # new values appear

    er_tri = by_ens["ER_p0.4"][1]["triadic_rate"]
    k2_tri = by_ens["fixed_k2"][1]["triadic_rate"]
    h3 = er_tri + 0.05 < k2_tri

    between = [
        round(float(r["core_phi"]), 6)
        for r in all_rows
        if 4.0 + PHI_EPS < r["core_phi"] < 20.0 - PHI_EPS
    ]
    h4 = all(p in BETWEEN_ATOMS for p in between)

    if h1 and not h2 and h4:
        reading = (
            "DISCRETE_LANDMARKS_N5 — all Φ in L5={2,3,4,6,8,12,20}; "
            f"on_landmark={on_land_frac:.2f}; echoes n=4"
        )
        verdict_word = "DISCRETE_LANDMARKS_N5"
    elif h2 and not h1:
        reading = (
            "NEW_VALUES_N5 — off-landmark Φ appeared; discrete set incomplete at n=5"
        )
        verdict_word = "NEW_VALUES_N5"
    elif h1 and h2:
        reading = (
            "PARTIAL_N5 — ≥90% on landmarks but some new atoms; mostly discrete"
        )
        verdict_word = "PARTIAL_N5"
    else:
        reading = "PARTIAL — anchors or rate pattern incomplete"
        verdict_word = "PARTIAL"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  n=5 samples: {n_tot}  on_landmark={on_land_frac:.3f}  "
          f"off_count={len(off)}")
    print(f"  Φ histogram n=5: {hist.most_common()}")
    print(f"  off-landmark values: {Counter(off).most_common() if off else 'none'}")
    print(f"  between (4,20) values: {Counter(between).most_common()}")
    print(f"  triadic rates: ER0.4={er_tri:.3f}  fixed_k2={k2_tri:.3f}  "
          f"fixed_k3={by_ens['fixed_k3'][1]['triadic_rate']:.3f}  "
          f"WS0.3={by_ens['WS_p0.3'][1]['triadic_rate']:.3f}  "
          f"BA={by_ens['BA_m2'][1]['triadic_rate']:.3f}")
    print(f"  H1 (≥90% on L5 + poles):            "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (new Φ values appear):           "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (triadic ER < fixed_k2):         "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (between-band in {{6,8,12}}):      "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  discrete landmarks hold at n=5? "
          f"{'YES' if h1 and not h2 else 'NO' if h2 and not h1 else 'PARTIAL'}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "samples_n5.csv"), "w", newline="") as fh:
        fields = [
            "ensemble", "n", "seed", "structure", "whole_phi_mip", "core",
            "core_phi", "n_core", "mean_degree", "clustering",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "ensemble": r["ensemble"],
                "n": r["n"],
                "seed": r["seed"],
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "mean_degree": f"{r['mean_degree']:.6f}",
                "clustering": f"{r['clustering']:.6f}",
            })
    with open(os.path.join(RESULTS, "summary_n5.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summaries[0].keys()))
        w.writeheader()
        for s in summaries:
            w.writerow(s)
    with open(os.path.join(RESULTS, "verdict_n5.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "h1", "h2", "h3", "h4", "verdict", "on_landmark",
                "n_samples", "off_count", "reading",
            ],
        )
        w.writeheader()
        w.writerow({
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "verdict": verdict_word,
            "on_landmark": f"{on_land_frac:.6f}",
            "n_samples": n_tot,
            "off_count": len(off),
            "reading": reading,
        })


if __name__ == "__main__":
    main()
