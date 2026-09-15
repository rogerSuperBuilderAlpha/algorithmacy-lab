"""Φ=14 = 3+3 derangement law among !6 at n=6 fixed_k=4.

Dense cycle-type census + thin non-derangement contamination check.
Hypotheses fixed in hypotheses.md. Extends omit_lift_n6 LAWS_MORPH.

Run:  python org_frontier/studies/derangement_33_phi14/analyze_33.py
"""

from __future__ import annotations

import csv
import itertools
import os
import sys
import time
from collections import Counter, defaultdict

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import verdict
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import (
    eval_one,
    fixed_k_ins,
)
from org_frontier.studies.omit_lift_n6.analyze_lift import omit_feats

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N = 6
K = 4
BASE_SEED = 20260915
# Dense sample sizes (candid: not full !6=265 enum; ~45s/cell)
N_33 = 6
N_PER_OTHER = { (6,): 3, (2, 4): 3, (2, 2, 2): 3 }
N_NONDER = 3

# Designed 3+3 witnesses from omit_lift_n6 (must appear in sample)
DESIGNED_33 = [
    (1, 2, 0, 4, 5, 3),  # cyc3_3
    (1, 2, 0, 5, 3, 4),  # cyc3_3_alt
]


def cycle_type_perm(p):
    seen = set()
    lens = []
    for s in range(N):
        if s in seen:
            continue
        L = 0
        u = s
        while u not in seen:
            seen.add(u)
            u = p[u]
            L += 1
        lens.append(L)
    return tuple(sorted(lens))


def om_from_tuple(p):
    return {i: p[i] for i in range(N)}


def fmt_omit(om):
    return "|".join(str(om[i]) for i in range(N))


def ins_from_omit(om):
    return {i: [j for j in range(N) if j != i and j != om[i]] for i in range(N)}


def is_derangement_om(om):
    vals = [om[i] for i in range(N)]
    return sorted(vals) == list(range(N)) and all(om[i] != i for i in range(N))


def omit_of(ins):
    om = {}
    for i in range(N):
        others = set(range(N)) - {i}
        omitted = list(others - set(ins[i]))
        om[i] = omitted[0] if len(omitted) == 1 else None
    return om


def all_derangements_by_type():
    by = defaultdict(list)
    for p in itertools.permutations(range(N)):
        if all(p[i] != i for i in range(N)):
            by[cycle_type_perm(p)].append(p)
    return by


def sample_type(pool, n_want, rng, forced=()):
    """forced tuples first (if in pool), then random without replacement."""
    forced_set = set(forced)
    out = []
    for f in forced:
        if f in pool and f not in out:
            out.append(f)
    rest = [p for p in pool if p not in forced_set]
    need = max(0, n_want - len(out))
    if need > 0 and rest:
        idxs = rng.choice(len(rest), size=min(need, len(rest)), replace=False)
        for i in idxs:
            out.append(rest[int(i)])
    return out[:n_want]


def main():
    print("DERANGEMENT 3+3 Φ=14 LAW — n=6 fixed_k=4")
    print("=" * 80)
    print("  cited: omit_lift_n6 LAWS_MORPH (3+3→14; others→12)")
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
    print()

    print("H4 STRUCTURAL — !6 class sizes")
    print("-" * 80)
    by_type = all_derangements_by_type()
    sizes = {k: len(v) for k, v in sorted(by_type.items(), key=lambda kv: -len(kv[1]))}
    print(f"  !6 total={sum(sizes.values())}  by_type={sizes}")
    expect_sizes = {(6,): 120, (2, 4): 90, (3, 3): 40, (2, 2, 2): 15}
    h4 = sizes == expect_sizes and sum(sizes.values()) == 265
    print(f"  expected={expect_sizes}  H4_sizes={'PASS' if h4 else 'FAIL'}")
    print()

    labels = tuple(f"N{i}" for i in range(N))
    rows = []
    t_all = time.time()
    rng = np.random.default_rng(BASE_SEED + 33)

    # ---- 3+3 sample ----
    print(f"CYCLE TYPE (3,3) SAMPLE N={N_33} (class size={sizes[(3, 3)]})")
    print("-" * 80)
    pool_33 = by_type[(3, 3)]
    samp_33 = sample_type(pool_33, N_33, rng, forced=DESIGNED_33)
    rows_33 = []
    for i, p in enumerate(samp_33):
        om = om_from_tuple(p)
        r = eval_one(ins_from_omit(om), N, labels)
        tag = "designed" if p in DESIGNED_33 else "sample"
        r.update({
            "family": "der_33",
            "name": f"33_{i}_{tag}",
            "omit": fmt_omit(om),
            "cycles": str((3, 3)),
            "is_derangement": True,
        })
        rows.append(r)
        rows_33.append(r)
        print(f"  33_{i}_{tag}  omit={fmt_omit(om)}  "
              f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}")
    phis_33 = [r["core_phi"] for r in rows_33]
    all_14 = all(abs(p - 14.0) < PHI_EPS for p in phis_33)
    all_full_33 = all(r["n_core"] == N for r in rows_33)
    print(f"  Φ hist={dict(Counter(round(p, 3) for p in phis_33))}  "
          f"all_Φ14={all_14} all_full={all_full_33}")
    print()

    # ---- other cycle types ----
    print("OTHER !6 CYCLE TYPES (non-3+3)")
    print("-" * 80)
    rows_other = []
    for ctype, n_want in N_PER_OTHER.items():
        pool = by_type[ctype]
        samp = sample_type(pool, n_want, rng)
        for i, p in enumerate(samp):
            om = om_from_tuple(p)
            r = eval_one(ins_from_omit(om), N, labels)
            r.update({
                "family": f"der_{ctype}",
                "name": f"ctype{ctype}_{i}",
                "omit": fmt_omit(om),
                "cycles": str(ctype),
                "is_derangement": True,
            })
            rows.append(r)
            rows_other.append(r)
            print(f"  {ctype}[{i}]  Φ={r['core_phi']:.1f}  n_core={r['n_core']}")
    phis_other = [r["core_phi"] for r in rows_other]
    other_has_14 = any(abs(p - 14.0) < PHI_EPS for p in phis_other)
    other_hist = Counter(round(p, 3) for p in phis_other)
    print(f"  other Φ hist={dict(other_hist)}  any_Φ14={other_has_14}")
    print()

    # ---- non-derangement contamination ----
    print(f"NON-DERANGEMENT fixed_k=4 SAMPLE N={N_NONDER}")
    print("-" * 80)
    rows_non = []
    s = 0
    attempts = 0
    while len(rows_non) < N_NONDER and attempts < N_NONDER * 40:
        attempts += 1
        rng_i = np.random.default_rng(BASE_SEED + 3300 + s * 17)
        s += 1
        ins = fixed_k_ins(N, K, rng_i)
        om = omit_of(ins)
        if any(v is None for v in om.values()) or is_derangement_om(om):
            continue
        r = eval_one(ins, N, labels)
        feats = omit_feats(om)
        r.update({
            "family": "nonder",
            "name": f"nonder_{len(rows_non)}",
            "omit": fmt_omit(om),
            "cycles": str(feats[1]),
            "is_derangement": False,
        })
        rows_non.append(r)
        rows.append(r)
        print(f"  nonder_{len(rows_non)-1}  cyc={feats[1]}  "
              f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}")
    phis_non = [r["core_phi"] for r in rows_non]
    non_has_14 = any(abs(p - 14.0) < PHI_EPS for p in phis_non)
    print(f"  nonder Φ hist={dict(Counter(round(p, 3) for p in phis_non))}  "
          f"any_Φ14={non_has_14}")
    print()

    # ---- contingency ----
    print("CONTINGENCY cycle-type × Φ (tested)")
    print("-" * 80)
    by_ct_phi = defaultdict(Counter)
    for r in rows:
        if r["is_derangement"]:
            by_ct_phi[r["cycles"]][round(r["core_phi"], 1)] += 1
    for ct in sorted(by_ct_phi.keys()):
        print(f"  {ct}: {dict(by_ct_phi[ct])}")
    print()

    # ---- hypotheses ----
    h5 = ctrl and all_14 and all_full_33 and len(rows_33) == N_33
    h2 = other_has_14
    h3 = non_has_14
    other_all_not_14 = all(abs(p - 14.0) >= PHI_EPS for p in phis_other)
    h1 = h5 and other_all_not_14 and not h2

    if h1 and not h3 and h4:
        verdict_word = "PHI14_IS_33"
        reading = (
            "PHI14_IS_33 — among !6, Φ=14 iff cycle type 3+3 "
            f"(N_33={N_33} all 14; other types no 14); non-ders no 14 in thin sample"
        )
    elif h1 and h3:
        verdict_word = "PHI14_33_AMONG_DERS"
        reading = (
            "PHI14_33_AMONG_DERS — Φ=14 iff 3+3 among derangements, "
            "but non-derangements also hit 14"
        )
    elif h2:
        verdict_word = "CONTAMINATED"
        reading = "CONTAMINATED — non-3+3 derangements also hit Φ=14"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — uniformity or exclusivity incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  3+3: all_Φ14={all_14} all_full={all_full_33} N={len(rows_33)}")
    print(f"  other types any_Φ14={other_has_14}  hist={dict(other_hist)}")
    print(f"  nonder any_Φ14={non_has_14}")
    print(f"  H1 (Φ=14 ⟺ 3+3 among ders):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (other !6 types hit 14):      "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (non-ders hit 14):            "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (!6 sizes 120/90/40/15):       "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (3+3 uniformity Φ=14 full):   "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  !6 class sizes: {sizes}")
    print(f"  3+3 → Φ=14: {all_14} (N={len(rows_33)}/{sizes[(3, 3)]})")
    print(f"  other !6 → Φ=14: {other_has_14}")
    print(f"  nonder → Φ=14: {non_has_14}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "family", "name", "omit", "cycles", "is_derangement",
            "structure", "whole_phi_mip", "core", "core_phi", "n_core",
            "mean_degree", "clustering",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "name": r["name"],
                "omit": r["omit"],
                "cycles": r["cycles"],
                "is_derangement": str(r["is_derangement"]),
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
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
            "n_33": len(rows_33),
            "n_other": len(rows_other),
            "n_nonder": len(rows_non),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
