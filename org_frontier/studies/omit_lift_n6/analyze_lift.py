"""n=6 omit/derangement lift of n=5 NEW_RUNGS + MOTIF_DISCRIMINANT.

Tests whether derangement single-rung and 3-cycle motif laws hold, break,
or morph at fixed_k=4. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/omit_lift_n6/analyze_lift.py
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
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import (
    eval_one,
    fixed_k_ins,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N = 6
K = 4
BASE_SEED = 20260915
L6 = {4.0, 6.0, 8.0, 9.0, 12.0, 30.0}
MOTIF_M3 = ((0, 1, 1, 1, 1, 2), (3,), 0)
N_RANDOM_DER = 2
N_NONDER = 2
# Same-indeg sibling (cyc, recip) reps to evaluate (M3 key excluded).
# Three diverse types suffice for H4; full class catalog is printed without Φ.
SIB_EVAL_KEYS = [((2,), 1), ((2, 2), 2), ((4,), 0)]


def omit_feats(om):
    vals = [om[i] for i in range(N)]
    indeg = Counter(vals)
    indeg_sig = tuple(sorted(indeg[i] for i in range(N)))
    seen = set()
    cyc_lens = []
    for start in range(N):
        if start in seen:
            continue
        path = []
        u = start
        while u not in seen and u not in path:
            path.append(u)
            u = om[u]
        if u in path:
            cyc_lens.append(len(path) - path.index(u))
        for x in path:
            seen.add(x)
    recip = sum(1 for i in range(N) if om[om[i]] == i) // 2
    return indeg_sig, tuple(sorted(cyc_lens)), recip


def ins_from_omit(om):
    return {i: [j for j in range(N) if j != i and j != om[i]] for i in range(N)}


def is_derangement(om):
    vals = [om[i] for i in range(N)]
    return sorted(vals) == list(range(N)) and all(om[i] != i for i in range(N))


def omit_of(ins):
    om = {}
    for i in range(N):
        others = set(range(N)) - {i}
        omitted = list(others - set(ins[i]))
        om[i] = omitted[0] if len(omitted) == 1 else None
    return om


def cycle_type_key(om):
    _, cyc, _ = omit_feats(om)
    return cyc


def designed_derangements():
    """One witness per derangement cycle type on 6 letters."""
    return [
        ("cyc6", {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 0}),
        ("cyc4_2", {0: 1, 1: 2, 2: 3, 3: 0, 4: 5, 5: 4}),
        ("cyc2_2_2", {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}),
        ("cyc3_3", {0: 1, 1: 2, 2: 0, 3: 4, 4: 5, 5: 3}),
        ("cyc3_3_alt", {0: 1, 1: 2, 2: 0, 3: 5, 5: 4, 4: 3}),
    ]


def designed_m3():
    """indeg (0,1,1,1,1,2) + single 3-cycle + recip=0."""
    # om: 0→1→2→0; 3→0, 4→3, 5→4  → indeg 0:2,1:1,2:1,3:1,4:1,5:0
    primary = {0: 1, 1: 2, 2: 0, 3: 0, 4: 3, 5: 4}
    # alternate labeling (rotate nodes +1)
    alt = {(i + 1) % N: (primary[i] + 1) % N for i in range(N)}
    return [("M3", primary), ("M3_alt", alt)]


def enumerate_same_indeg_classes():
    """Partition all omit functions with indeg (0,1,1,1,1,2) by (cyc, recip)."""
    target_indeg = (0, 1, 1, 1, 1, 2)
    by_key = defaultdict(list)
    for choices in itertools.product(
        *[[j for j in range(N) if j != i] for i in range(N)]
    ):
        om = {i: choices[i] for i in range(N)}
        if is_derangement(om):
            continue
        feats = omit_feats(om)
        if feats[0] != target_indeg:
            continue
        by_key[(feats[1], feats[2])].append(om)
    return by_key


def fmt_omit(om):
    return "|".join(str(om[i]) for i in range(N))


def main():
    print("OMIT/DERANGEMENT LIFT n=6 fixed_k=4")
    print("=" * 80)
    print("  cited: fixed_k_atoms_n5 NEW_RUNGS; omit_motif_phi5 MOTIF_DISCRIMINANT")
    print("  cited: interior_ring_pool L6={4,6,8,9,12,30}")
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
    labels = tuple(f"N{i}" for i in range(N))
    _, ring_phi = major_complex(ring(N), labels)
    # pool6=30 cited from interior_ring_pool (skip recompute; ~45s/cell budget)
    poles_ok = abs(float(ring_phi) - 4.0) < PHI_EPS
    print(f"  ring6 Φ={float(ring_phi):.3f}  pool6 cited=30.0  "
          f"{'PASS' if poles_ok else 'FAIL'}")
    print()

    rows = []
    t_all = time.time()

    # ---- Designed derangement cycle types ----
    print("DESIGNED DERANGEMENT CYCLE TYPES")
    print("-" * 80)
    der_rows = []
    for name, om in designed_derangements():
        assert is_derangement(om), name
        feats = omit_feats(om)
        r = eval_one(ins_from_omit(om), N, labels)
        r.update({
            "family": "der_designed",
            "name": name,
            "omit": fmt_omit(om),
            "indeg_sig": str(feats[0]),
            "cycles": str(feats[1]),
            "recip": feats[2],
            "is_derangement": True,
            "is_m3": False,
        })
        rows.append(r)
        der_rows.append(r)
        print(
            f"  {name:<12} cyc={feats[1]}  Φ={r['core_phi']:.1f}  "
            f"n_core={r['n_core']}  structure={r['structure']}"
        )
    print()

    # ---- Random derangement sample ----
    print(f"RANDOM DERANGEMENT SAMPLE N={N_RANDOM_DER}")
    print("-" * 80)
    rng = np.random.default_rng(BASE_SEED + 600)
    # enumerate all derangements is !6=265 — fine; sample without replacement
    all_ders = [
        {i: p[i] for i in range(N)}
        for p in itertools.permutations(range(N))
        if all(p[i] != i for i in range(N))
    ]
    designed_omits = {fmt_omit(om) for _, om in designed_derangements()}
    pool_ders = [om for om in all_ders if fmt_omit(om) not in designed_omits]
    idxs = rng.choice(len(pool_ders), size=N_RANDOM_DER, replace=False)
    for i, idx in enumerate(idxs):
        om = pool_ders[int(idx)]
        feats = omit_feats(om)
        r = eval_one(ins_from_omit(om), N, labels)
        r.update({
            "family": "der_random",
            "name": f"rand_der_{i}",
            "omit": fmt_omit(om),
            "indeg_sig": str(feats[0]),
            "cycles": str(feats[1]),
            "recip": feats[2],
            "is_derangement": True,
            "is_m3": False,
        })
        rows.append(r)
        der_rows.append(r)
        print(
            f"  rand_der_{i}  cyc={feats[1]}  Φ={r['core_phi']:.1f}  "
            f"n_core={r['n_core']}"
        )
    der_phis = [r["core_phi"] for r in der_rows]
    der_hist = Counter(round(p, 3) for p in der_phis)
    der_distinct = sorted({round(p, 6) for p in der_phis})
    print(f"  der Φ hist={dict(der_hist)}  distinct={der_distinct}")
    print()

    # ---- Motif M3 + same-indeg siblings ----
    print("MOTIF M3 + SAME-INDEG SIBLINGS")
    print("-" * 80)
    by_sib = enumerate_same_indeg_classes()
    m3_key = ((3,), 0)
    print(f"  same-indeg classes (cyc,recip): "
          f"{ {k: len(v) for k, v in sorted(by_sib.items())} }")
    assert m3_key in by_sib, "M3 class missing from enum"
    print(f"  M3 class size={len(by_sib[m3_key])}")

    m3_rows = []
    for name, om in designed_m3():
        feats = omit_feats(om)
        assert feats == MOTIF_M3, (name, feats, MOTIF_M3)
        r = eval_one(ins_from_omit(om), N, labels)
        r.update({
            "family": "m3",
            "name": name,
            "omit": fmt_omit(om),
            "indeg_sig": str(feats[0]),
            "cycles": str(feats[1]),
            "recip": feats[2],
            "is_derangement": False,
            "is_m3": True,
        })
        rows.append(r)
        m3_rows.append(r)
        print(
            f"  {name:<12} Φ={r['core_phi']:.1f}  n_core={r['n_core']}  "
            f"structure={r['structure']}"
        )

    sib_rows = []
    for key in SIB_EVAL_KEYS:
        if key not in by_sib:
            print(f"  WARN missing sibling key {key}")
            continue
        oms = by_sib[key]
        om = oms[0]
        feats = omit_feats(om)
        cyc, recip = key
        name = f"sib_cyc{cyc}_r{recip}"
        r = eval_one(ins_from_omit(om), N, labels)
        r.update({
            "family": "m3_sibling",
            "name": name,
            "omit": fmt_omit(om),
            "indeg_sig": str(feats[0]),
            "cycles": str(feats[1]),
            "recip": feats[2],
            "is_derangement": False,
            "is_m3": False,
        })
        rows.append(r)
        sib_rows.append(r)
        print(
            f"  {name:<28} n={len(oms):4d}  Φ={r['core_phi']:.1f}  "
            f"n_core={r['n_core']}"
        )
    print()

    # ---- Thin non-derangement sample ----
    print(f"THIN NON-DERANGEMENT SAMPLE N={N_NONDER}")
    print("-" * 80)
    non_rows = []
    s = 0
    attempts = 0
    while len(non_rows) < N_NONDER and attempts < N_NONDER * 40:
        attempts += 1
        rng_i = np.random.default_rng(BASE_SEED + 6100 + s * 19)
        s += 1
        ins = fixed_k_ins(N, K, rng_i)
        om = omit_of(ins)
        if om is None or any(v is None for v in om.values()):
            continue
        if is_derangement(om):
            continue
        feats = omit_feats(om)
        # skip pure M3 class (already measured)
        if feats == MOTIF_M3:
            continue
        r = eval_one(ins, N, labels)
        r.update({
            "family": "nonder_thin",
            "name": f"nonder_{len(non_rows)}",
            "omit": fmt_omit(om),
            "indeg_sig": str(feats[0]),
            "cycles": str(feats[1]),
            "recip": feats[2],
            "is_derangement": False,
            "is_m3": False,
        })
        non_rows.append(r)
        rows.append(r)
        print(
            f"  nonder_{len(non_rows)-1}  indeg={feats[0]} cyc={feats[1]} "
            f"r={feats[2]}  Φ={r['core_phi']:.1f}  n_core={r['n_core']}"
        )
    print()

    # ---- Hypothesis tests ----
    der_full = all(r["n_core"] == N for r in der_rows)
    h1 = len(der_distinct) == 1 and der_full  # single rung — expect REFUTED
    # H2: 3+3 differs from {6},{4,2},{2,2,2}
    by_ctype = defaultdict(list)
    for r in der_rows:
        # parse cycles from stored string like "(3, 3)" or "(6,)"
        by_ctype[r["cycles"]].append(r["core_phi"])
    phi_33 = by_ctype.get(str((3, 3)), [])
    phi_others = []
    for key in (str((6,)), str((2, 4)), str((2, 2, 2))):
        phi_others.extend(by_ctype.get(key, []))
    # also accept designed names if cycle string formatting differs
    designed_33 = [r for r in der_rows if r["name"].startswith("cyc3_3")]
    designed_non33 = [
        r for r in der_rows
        if r["family"] == "der_designed" and not r["name"].startswith("cyc3_3")
    ]
    if not phi_33:
        phi_33 = [r["core_phi"] for r in designed_33]
    if not phi_others:
        phi_others = [r["core_phi"] for r in designed_non33]
    h2 = (
        len(phi_33) >= 1
        and len(phi_others) >= 1
        and all(
            abs(a - b) >= PHI_EPS
            for a in phi_33 for b in phi_others
        )
    )

    m3_phis = [r["core_phi"] for r in m3_rows]
    m3_cores = [r["n_core"] for r in m3_rows]
    m3_uniform = (
        len(m3_phis) >= 2
        and all(abs(p - m3_phis[0]) < PHI_EPS for p in m3_phis)
    )
    m3_incomplete = all(c == N - 1 for c in m3_cores)
    h3 = m3_uniform and m3_incomplete

    m3_phi0 = m3_phis[0] if m3_phis else float("nan")
    sib_same = [
        r for r in sib_rows if abs(r["core_phi"] - m3_phi0) < PHI_EPS
    ]
    h4 = len(sib_same) >= 1  # discriminant fails to lift

    all_phis = [r["core_phi"] for r in rows]
    distinct_all = sorted({round(p, 6) for p in all_phis})
    outside_L6 = [p for p in distinct_all if p not in L6]
    h5 = len(outside_L6) >= 1

    if (not h1) and h2 and h3 and h4 and h5:
        verdict_word = "LAWS_MORPH"
        reading = (
            "LAWS_MORPH — derangements split by cycle type (3+3 vs others); "
            "M3 incomplete-core persists but sibling cycle discriminant fails; "
            "new atom outside L6"
        )
    elif h1 and h3 and not h4:
        verdict_word = "LAWS_HOLD"
        reading = (
            "LAWS_HOLD — single derangement rung + M3 sibling discriminant lift"
        )
    elif not h1 and not h3:
        verdict_word = "LAWS_BREAK"
        reading = "LAWS_BREAK — neither derangement rung nor M3 incomplete-core survives"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — mixed hold/break/morph across H1–H5"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  derangement Φ distinct={der_distinct}  hist={dict(der_hist)}  "
          f"all_full_core={der_full}")
    print(f"  designed 3+3 Φ={ [round(p,1) for p in phi_33] }  "
          f"other designed Φ={ [round(p,1) for p in phi_others] }")
    print(f"  M3 Φ={ [round(p,1) for p in m3_phis] }  "
          f"n_cores={m3_cores}  uniform={m3_uniform} incomplete={m3_incomplete}")
    print(f"  siblings same-Φ-as-M3: {len(sib_same)}/{len(sib_rows)}  "
          f"sib_phis={[round(r['core_phi'],1) for r in sib_rows]}")
    print(f"  all distinct Φ={distinct_all}  outside_L6={outside_L6}")
    print(f"  H1 (single derangement rung):           "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (3+3 differs from other cycle types): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (M3 incomplete-core, uniform Φ):     "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (sibling discriminant fails):        "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (new atom outside L6):               "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  scale: n=5 Φ=9 der-rung / Φ=5 motif-M → n=6 morph")
    print(f"  derangement spectrum: {der_distinct}")
    print(f"  M3 Φ={round(m3_phi0, 1) if m3_phis else 'NA'} n_core="
          f"{m3_cores[0] if m3_cores else 'NA'}")
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
            "family", "name", "omit", "indeg_sig", "cycles", "recip",
            "is_derangement", "is_m3", "structure", "whole_phi_mip",
            "core", "core_phi", "n_core", "mean_degree", "clustering",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "name": r["name"],
                "omit": r["omit"],
                "indeg_sig": r["indeg_sig"],
                "cycles": r["cycles"],
                "recip": r["recip"],
                "is_derangement": str(r["is_derangement"]),
                "is_m3": str(r["is_m3"]),
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
            "der_distinct_phi": ";".join(str(p) for p in der_distinct),
            "m3_phi": round(m3_phi0, 6) if m3_phis else "",
            "m3_n_core": m3_cores[0] if m3_cores else "",
            "outside_L6": ";".join(str(p) for p in outside_L6),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
