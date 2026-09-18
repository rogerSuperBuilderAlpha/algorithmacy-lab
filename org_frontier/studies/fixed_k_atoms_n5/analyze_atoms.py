"""Fixed-k atoms 5/9 at n=5 — denser map (extends random_coupling_ensemble).

Enumerates all derangement-omit fixed_k=3 forms; denser non-derangement
fixed_k=3 sample; fixed_k=2 contrast. Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/fixed_k_atoms_n5/analyze_atoms.py
"""

from __future__ import annotations

import csv
import itertools
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
    eval_one,
    fixed_k_ins,
    rules_from_ins,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N_NONDER = 48
N_K2 = 24
BASE_SEED = 20260915
L5_PLUS = {2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 9.0, 12.0, 20.0}


def omit_of(ins):
    n = 5
    om = {}
    for i in range(n):
        others = set(range(n)) - {i}
        omitted = list(others - set(ins[i]))
        om[i] = omitted[0] if len(omitted) == 1 else None
    return om


def is_derangement_omit(om):
    if any(v is None for v in om.values()):
        return False
    vals = [om[i] for i in range(5)]
    if sorted(vals) != list(range(5)):
        return False
    return all(om[i] != i for i in range(5))


def ins_from_omit(omit_tuple):
    """omit_tuple[i] = node omitted by i."""
    ins = {}
    for i in range(5):
        ins[i] = [j for j in range(5) if j != i and j != omit_tuple[i]]
    return ins


def all_derangements():
    out = []
    for p in itertools.permutations(range(5)):
        if all(p[i] != i for i in range(5)):
            out.append(p)
    return out


def main():
    print("FIXED-K ATOMS 5/9 AT n=5 — denser map")
    print("=" * 80)
    print("  cited: random_coupling_ensemble PARTIAL_N5; interior_ring_pool L5")
    print("  hypotheses fixed in hypotheses.md before computing")
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
    labels = tuple(f"N{i}" for i in range(5))
    _, ring_phi = major_complex(ring(5), labels)
    _, pool_phi = major_complex(pool(5), labels)
    poles_ok = abs(float(ring_phi) - 4.0) < PHI_EPS and abs(float(pool_phi) - 20.0) < PHI_EPS
    print(f"  ring5 Φ={float(ring_phi):.3f}  pool5 Φ={float(pool_phi):.3f}  "
          f"{'PASS' if poles_ok else 'FAIL'}")
    print()

    rows = []

    # ---- H1 arm: all derangements ----
    print("DERANGEMENT OMITS (fixed_k=3) — full enumeration")
    print("-" * 80)
    ders = all_derangements()
    print(f"  n_derangements (!5) = {len(ders)}")
    t0 = time.time()
    der_phis = []
    for idx, omit in enumerate(ders):
        ins = ins_from_omit(omit)
        r = eval_one(ins, 5, labels)
        r.update({
            "family": "derangement_k3",
            "seed": idx,
            "omit": "|".join(str(omit[i]) for i in range(5)),
            "is_derangement": True,
        })
        rows.append(r)
        der_phis.append(r["core_phi"])
    der_secs = round(time.time() - t0, 2)
    der_hist = Counter(round(p, 3) for p in der_phis)
    all_nine = all(abs(p - 9.0) < PHI_EPS for p in der_phis)
    all_full = all(r["n_core"] == 5 and r["structure"] == "triadic" for r in rows)
    print(f"  Φ hist: {der_hist.most_common()}  ({der_secs}s)")
    print(f"  all Φ=9.0 full-core triadic: {all_nine and all_full}")
    print()

    # ---- Non-derangement dense sample ----
    print(f"NON-DERANGEMENT fixed_k=3 SAMPLE N={N_NONDER}")
    print("-" * 80)
    t0 = time.time()
    non_rows = []
    s = 0
    attempts = 0
    rng_gate = np.random.default_rng(BASE_SEED + 9000)
    while len(non_rows) < N_NONDER and attempts < N_NONDER * 20:
        attempts += 1
        rng = np.random.default_rng(BASE_SEED + 9100 + s * 19)
        s += 1
        ins = fixed_k_ins(5, 3, rng)
        om = omit_of(ins)
        if is_derangement_omit(om):
            continue
        r = eval_one(ins, 5, labels)
        r.update({
            "family": "nonder_k3",
            "seed": s - 1,
            "omit": "|".join(str(om[i]) for i in range(5)),
            "is_derangement": False,
        })
        non_rows.append(r)
        rows.append(r)
    non_secs = round(time.time() - t0, 2)
    non_phis = [r["core_phi"] for r in non_rows]
    non_hist = Counter(round(p, 3) for p in non_phis)
    n_phi5 = sum(1 for p in non_phis if abs(p - 5.0) < PHI_EPS)
    n_phi9 = sum(1 for p in non_phis if abs(p - 9.0) < PHI_EPS)
    phi5_rows = [r for r in non_rows if abs(r["core_phi"] - 5.0) < PHI_EPS]
    phi5_incomplete = all(r["n_core"] < 5 for r in phi5_rows) if phi5_rows else True
    print(f"  kept={len(non_rows)} attempts={attempts}  ({non_secs}s)")
    print(f"  Φ hist: {non_hist.most_common()}")
    print(f"  count Φ=5: {n_phi5}  Φ=9: {n_phi9}")
    if phi5_rows:
        print(f"  Φ=5 n_cores: {sorted({r['n_core'] for r in phi5_rows})}  "
              f"all_incomplete={phi5_incomplete}")
    print()

    # ---- fixed_k=2 contrast ----
    print(f"fixed_k=2 CONTRAST N={N_K2}")
    print("-" * 80)
    t0 = time.time()
    k2_rows = []
    for s in range(N_K2):
        rng = np.random.default_rng(BASE_SEED + 9200 + s * 23)
        ins = fixed_k_ins(5, 2, rng)
        r = eval_one(ins, 5, labels)
        r.update({
            "family": "fixed_k2",
            "seed": s,
            "omit": "",
            "is_derangement": False,
        })
        k2_rows.append(r)
        rows.append(r)
    k2_secs = round(time.time() - t0, 2)
    k2_phis = [r["core_phi"] for r in k2_rows]
    k2_hist = Counter(round(p, 3) for p in k2_phis)
    k2_on = sum(1 for p in k2_phis if round(p, 6) in L5_PLUS) / len(k2_phis)
    k2_has9 = any(abs(p - 9.0) < PHI_EPS for p in k2_phis)
    print(f"  Φ hist: {k2_hist.most_common()}  on_L5∪{{5,9}}={k2_on:.3f}  "
          f"has_Φ9={k2_has9}  ({k2_secs}s)")
    print()

    # ---- Hypothesis tests ----
    h1 = ctrl and poles_ok and all_nine and all_full and len(ders) == 44
    h2 = n_phi9 == 0
    h3 = n_phi5 >= 2 and phi5_incomplete
    k3_phis = der_phis + non_phis
    distinct = sorted({round(p, 6) for p in k3_phis})
    outside = [p for p in distinct if p not in L5_PLUS]
    h4 = len(distinct) <= 8 and len(outside) == 0
    h5 = k2_on >= 0.90 - 1e-12 and not k2_has9

    if h1 and h2 and h3 and h4:
        reading = (
            "NEW_RUNGS — Φ=9 = all derangement omits (rung); Φ=5 recurs on "
            "non-derangement incomplete cores; no continuum under denser k=3"
        )
        verdict_word = "NEW_RUNGS"
    elif h1 and h2 and not h3:
        reading = (
            "RUNG_9_ONLY — derangement Φ=9 holds; atom 5 rare/absent in denser sample"
        )
        verdict_word = "RUNG_9_ONLY"
    elif not h4:
        reading = "CONTINUUM — denser fixed_k=3 sprays many distinct Φ values"
        verdict_word = "CONTINUUM"
    else:
        reading = "PARTIAL — mixed support across H1–H5"
        verdict_word = "PARTIAL"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  derangement Φ: all_9={all_nine}  n={len(ders)}  hist={dict(der_hist)}")
    print(f"  nonder Φ=5 count={n_phi5}  Φ=9 count={n_phi9}  "
          f"phi5_incomplete={phi5_incomplete}")
    print(f"  k3 distinct Φ: {distinct}  outside_L5∪{{5,9}}={outside}")
    print(f"  k2 on_landmark={k2_on:.3f}  has_Φ9={k2_has9}")
    print(f"  H1 (all derangements Φ=9 full-core):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (no Φ=9 in non-derangement):       "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (Φ=5 recurs, incomplete core):     "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (no continuum; atoms ⊆ L5∪{{5,9}}): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (k=2 on known atoms, no Φ=9):      "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  atom 9: {'DERANGEMENT RUNG (44/44)' if h1 else 'NOT CLEAN RUNG'}")
    print(f"  atom 5: {'RECURRING NON-DERANG INCOMPLETE' if h3 else 'NOT ESTABLISHED'}")
    print(f"  continuum? {'NO' if h4 else 'YES/UNCLEAR'}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "family", "seed", "structure", "whole_phi_mip", "core", "core_phi",
            "n_core", "omit", "is_derangement", "mean_degree", "clustering",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "seed": r["seed"],
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "omit": r.get("omit", ""),
                "is_derangement": str(r.get("is_derangement", "")),
                "mean_degree": f"{r['mean_degree']:.6f}",
                "clustering": f"{r['clustering']:.6f}",
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "verdict": verdict_word,
            "n_derangements": len(ders),
            "n_nonder": len(non_rows),
            "n_phi5_nonder": n_phi5,
            "n_phi9_nonder": n_phi9,
            "k3_distinct_phi": ";".join(str(p) for p in distinct),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
