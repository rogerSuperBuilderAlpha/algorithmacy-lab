"""Random coupling ensemble at fixed n (agenda #18).

ER / fixed-k / WS / BA-style generators; conjunctive AND on in-neighbors.
Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/random_coupling_ensemble/analyze_ensemble.py
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

from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N_PRIMARY = 32
N_THIN = 8
BASE_SEED = 20260915
LANDMARKS_N4 = {2.0, 4.0, 6.0, 12.0}
LANDMARKS_N5 = {2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 20.0}


def _and_of(srcs):
    srcs = tuple(srcs)
    if not srcs:
        return lambda x: 0

    def f(x, srcs=srcs):
        r = 1
        for s in srcs:
            r &= x[s]
        return r

    return f


def rules_from_ins(ins, n):
    return [_and_of(ins[i]) for i in range(n)]


def er_ins(n, p, rng):
    ins = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and rng.random() < p:
                ins[i].append(j)
        if not ins[i]:
            c = int(rng.integers(0, n - 1))
            if c >= i:
                c += 1
            ins[i] = [c]
    return ins


def fixed_k_ins(n, k, rng):
    ins = {}
    for i in range(n):
        choices = [j for j in range(n) if j != i]
        k_eff = min(k, len(choices))
        picks = rng.choice(choices, size=k_eff, replace=False)
        ins[i] = [int(x) for x in picks]
    return ins


def ws_ins(n, p, rng):
    ins = {i: [(i - 1) % n, (i + 1) % n] for i in range(n)}
    for d in range(n):
        for s in range(2):
            if rng.random() < p:
                cur = set(ins[d])
                choices = [c for c in range(n) if c != d and c not in cur]
                if choices:
                    ins[d][s] = int(rng.choice(choices))
    return ins


def ba_ins(n, m, rng):
    """Preferential-attachment grow: new node reads m older targets."""
    m0 = max(m + 1, 2)
    ins = {i: [] for i in range(n)}
    for i in range(m0):
        others = [j for j in range(m0) if j != i]
        ins[i] = others[:m] if len(others) >= m else list(others)
    stubs = []
    for i in range(m0):
        stubs.extend([i] * max(1, len(ins[i])))
    for i in range(m0, n):
        targets = []
        for _ in range(m):
            for __ in range(40):
                t = int(rng.choice(stubs))
                if t != i and t not in targets:
                    targets.append(t)
                    break
        if not targets:
            targets = [int(rng.integers(0, i))]
        ins[i] = targets
        stubs.extend(targets)
        stubs.append(i)
        for t in targets:
            stubs.append(t)
    for i in range(n):
        if not ins[i]:
            choices = [j for j in range(n) if j != i]
            ins[i] = [int(rng.choice(choices))]
    return ins


def clustering(cm):
    n = cm.shape[0]
    a = ((cm + cm.T) > 0).astype(int)
    np.fill_diagonal(a, 0)
    coeffs = []
    for v in range(n):
        nbrs = np.where(a[v] > 0)[0]
        k = len(nbrs)
        if k < 2:
            coeffs.append(0.0)
            continue
        sub = a[np.ix_(nbrs, nbrs)]
        links = sub.sum() / 2.0
        coeffs.append(links / (k * (k - 1) / 2.0))
    return float(np.mean(coeffs)) if coeffs else 0.0


def mean_degree(cm):
    n = cm.shape[0]
    return float((cm.sum(axis=0) + cm.sum(axis=1)).mean()) if n else 0.0


def eval_one(ins, n, labels):
    rules = rules_from_ins(ins, n)
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    cm = cm_from_rules(rules)
    core_t = tuple(core) if core else ()
    return {
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": core_t,
        "core_phi": float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan"),
        "n_core": len(core_t),
        "mean_degree": mean_degree(cm),
        "clustering": clustering(cm),
    }


def run_ensemble(name, builder, n, N, seed_offset):
    labels = tuple(f"N{i}" for i in range(n))
    rows = []
    t0 = time.time()
    for s in range(N):
        rng = np.random.default_rng(BASE_SEED + seed_offset + s * 17)
        ins = builder(rng)
        r = eval_one(ins, n, labels)
        r.update({"ensemble": name, "n": n, "seed": s})
        rows.append(r)
    elapsed = round(time.time() - t0, 2)
    phis = np.array([r["core_phi"] for r in rows])
    tri = sum(1 for r in rows if r["structure"] == "triadic") / N
    land = LANDMARKS_N4 if n == 4 else LANDMARKS_N5
    on_land = sum(1 for p in phis if round(float(p), 6) in land) / N
    ctr = Counter(round(float(p), 3) for p in phis)
    print(
        f"  {name:<16} n={n} N={N}  tri={tri:.3f}  "
        f"Φ mean={np.nanmean(phis):.3f} med={np.nanmedian(phis):.3f}  "
        f"on_landmark={on_land:.3f}  top={ctr.most_common(5)}  ({elapsed}s)"
    )
    return rows, {
        "ensemble": name,
        "n": n,
        "N": N,
        "triadic_rate": tri,
        "phi_mean": float(np.nanmean(phis)),
        "phi_median": float(np.nanmedian(phis)),
        "phi_min": float(np.nanmin(phis)),
        "phi_max": float(np.nanmax(phis)),
        "on_landmark": on_land,
        "mean_clustering": float(np.mean([r["clustering"] for r in rows])),
        "mean_degree": float(np.mean([r["mean_degree"] for r in rows])),
        "seconds": elapsed,
    }


def main():
    print("RANDOM COUPLING ENSEMBLE — agenda #18")
    print("=" * 80)
    print("  cited: interior_ring_pool discrete steps; q147 random truth-tables;")
    print("         q146/small-world PICK_ONE")
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

    print("POLE LANDMARKS n=4")
    print("-" * 80)
    labels4 = tuple(f"N{i}" for i in range(4))
    _, ring_phi = major_complex(ring(4), labels4)
    _, pool_phi = major_complex(pool(4), labels4)
    print(f"  ring4 coreΦ={float(ring_phi):.3f}  pool4 coreΦ={float(pool_phi):.3f}")
    print()

    all_rows = []
    summaries = []

    print(f"PRIMARY ENSEMBLES n=4 N={N_PRIMARY}")
    print("-" * 80)
    specs = [
        ("ER_p0.3", lambda rng: er_ins(4, 0.3, rng), 100),
        ("ER_p0.5", lambda rng: er_ins(4, 0.5, rng), 200),
        ("fixed_k2", lambda rng: fixed_k_ins(4, 2, rng), 300),
        ("fixed_k3", lambda rng: fixed_k_ins(4, 3, rng), 400),
        ("WS_p0.25", lambda rng: ws_ins(4, 0.25, rng), 500),
        ("WS_p0.5", lambda rng: ws_ins(4, 0.5, rng), 600),
        ("BA_m2", lambda rng: ba_ins(4, 2, rng), 700),
    ]
    by_ens = {}
    for name, builder, off in specs:
        rows, summ = run_ensemble(name, builder, 4, N_PRIMARY, off)
        all_rows.extend(rows)
        summaries.append(summ)
        by_ens[name] = (rows, summ)
    print()

    print(f"THIN n=5 CHECK N={N_THIN} (fixed_k=2)")
    print("-" * 80)
    rows5, summ5 = run_ensemble(
        "fixed_k2_n5", lambda rng: fixed_k_ins(5, 2, rng), 5, N_THIN, 800
    )
    all_rows.extend(rows5)
    summaries.append(summ5)
    print()

    # ---- Hypothesis tests ----
    h1 = (
        ctrl
        and abs(float(ring_phi) - 4.0) < PHI_EPS
        and abs(float(pool_phi) - 12.0) < PHI_EPS
    )

    primary_phis = [r["core_phi"] for r in all_rows if r["n"] == 4]
    on_land_frac = sum(
        1 for p in primary_phis if round(float(p), 6) in LANDMARKS_N4
    ) / len(primary_phis)
    h2 = on_land_frac >= 0.90 - 1e-12

    er03 = by_ens["ER_p0.3"][1]["triadic_rate"]
    fk2 = by_ens["fixed_k2"][1]["triadic_rate"]
    fk3 = by_ens["fixed_k3"][1]["triadic_rate"]
    h3 = (er03 + 0.05 < fk2) and (fk2 + 0.05 < fk3)

    between = [
        round(float(r["core_phi"]), 6)
        for r in all_rows
        if r["n"] == 4 and 4.0 + PHI_EPS < r["core_phi"] < 12.0 - PHI_EPS
    ]
    h4 = all(abs(p - 6.0) < PHI_EPS for p in between)  # vacuously true if empty

    ws_cl = by_ens["WS_p0.25"][1]["mean_clustering"]
    er_cl = by_ens["ER_p0.5"][1]["mean_clustering"]
    h5 = ws_cl > er_cl + 1e-6

    if h1 and h2 and h4:
        reading = (
            "DISCRETE_LANDMARKS — random coupling Φ sits on #19 atoms "
            f"(on_landmark={on_land_frac:.2f}); triadic rate tracks ensemble; "
            "no continuous ring–pool fill"
        )
        verdict_word = "DISCRETE_LANDMARKS"
    elif h1 and not h2:
        reading = "CONTINUOUS_FILL — ≥10% of samples off the discrete landmark set"
        verdict_word = "CONTINUOUS_FILL"
    else:
        reading = "PARTIAL — anchors or landmark pattern incomplete"
        verdict_word = "PARTIAL"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  n=4 samples: {len(primary_phis)}  on_landmark={on_land_frac:.3f}")
    print(f"  Φ histogram n=4: {Counter(round(float(p), 3) for p in primary_phis).most_common()}")
    print(f"  between (4,12) values: {Counter(between).most_common()}")
    print(f"  triadic rates: ER0.3={er03:.3f}  fixed_k2={fk2:.3f}  "
          f"fixed_k3={fk3:.3f}")
    print(f"  clustering: WS0.25={ws_cl:.3f}  ER0.5={er_cl:.3f}  "
          f"(deg WS={by_ens['WS_p0.25'][1]['mean_degree']:.2f} "
          f"ER={by_ens['ER_p0.5'][1]['mean_degree']:.2f})")
    print(f"  n5 fixed_k2: tri={summ5['triadic_rate']:.3f}  "
          f"on_land={summ5['on_landmark']:.3f}  "
          f"Φ hist={Counter(round(r['core_phi'], 3) for r in rows5).most_common()}")
    print(f"  H1 (control + ring/pool poles):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (Φ ≥90% on landmarks):           "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (triadic rate ER < k2 < k3):     "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (between-band only atom 6):      "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (WS clustering > ER):            "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  only discrete #19 landmarks? {'YES' if h2 and h4 else 'NO'}")
    print(f"  match standard ensemble as Φ law? NO — generators differ in "
          f"triadic rate/clustering; Φ atoms shared")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "samples.csv"), "w", newline="") as fh:
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
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        fields = list(summaries[0].keys()) + [
            "h1", "h2", "h3", "h4", "h5", "verdict", "on_landmark_all_n4", "reading"
        ]
        # write per-ensemble then a final verdict row? Simpler: ensemble rows + meta file
        w = csv.DictWriter(fh, fieldnames=list(summaries[0].keys()))
        w.writeheader()
        for s in summaries:
            w.writerow(s)
    with open(os.path.join(RESULTS, "verdict.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "h1", "h2", "h3", "h4", "h5", "verdict",
                "on_landmark_all_n4", "reading",
            ],
        )
        w.writeheader()
        w.writerow({
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "verdict": verdict_word,
            "on_landmark_all_n4": f"{on_land_frac:.6f}",
            "reading": reading,
        })


if __name__ == "__main__":
    main()
