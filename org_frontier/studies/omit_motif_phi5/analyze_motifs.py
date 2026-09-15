"""Omit-motif census: Φ=5 vs Φ=6 at n=5 fixed_k=3 (extends fixed_k_atoms_n5).

Partitions non-derangement omit functions by (indeg_sig, cycles, recip);
evaluates orbit representatives + motif-M uniformity sample.
Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/omit_motif_phi5/analyze_motifs.py
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
from org_frontier.probes.probe_topology_map import pool
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import eval_one

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

MOTIF_M = ((0, 1, 1, 1, 2), (3,), 0)
N_UNIFORM = 12
BASE_SEED = 20260915


def omit_feats(om):
    vals = [om[i] for i in range(5)]
    indeg = Counter(vals)
    indeg_sig = tuple(sorted(indeg[i] for i in range(5)))
    seen = set()
    cyc_lens = []
    for start in range(5):
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
    recip = sum(1 for i in range(5) if om[om[i]] == i) // 2
    return indeg_sig, tuple(sorted(cyc_lens)), recip


def ins_from_omit(om):
    return {i: [j for j in range(5) if j != i and j != om[i]] for i in range(5)}


def is_derangement(om):
    vals = [om[i] for i in range(5)]
    return sorted(vals) == list(range(5))


def all_omit_functions():
    out = []
    for choices in itertools.product(
        *[[j for j in range(5) if j != i] for i in range(5)]
    ):
        out.append({i: choices[i] for i in range(5)})
    return out


def fmt_key(key):
    indeg, cyc, recip = key
    return f"indeg={indeg}|cyc={cyc}|recip={recip}"


def main():
    print("OMIT-MOTIF CENSUS Φ=5 vs Φ=6 — n=5 fixed_k=3")
    print("=" * 80)
    print("  cited: fixed_k_atoms_n5 NEW_RUNGS; random_coupling PARTIAL_N5")
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

    print("PARTITION omit functions")
    print("-" * 80)
    all_oms = all_omit_functions()
    ders = [om for om in all_oms if is_derangement(om)]
    by_class = defaultdict(list)
    for om in all_oms:
        if is_derangement(om):
            continue
        by_class[omit_feats(om)].append(om)
    print(f"  total omits={len(all_oms)}  derangements={len(ders)}  "
          f"nonder={sum(len(v) for v in by_class.values())}  "
          f"classes={len(by_class)}")
    print(f"  motif M {MOTIF_M} size={len(by_class[MOTIF_M])}")
    print()

    rows = []
    t0 = time.time()

    print("ORBIT REPRESENTATIVES (one per nonder class)")
    print("-" * 80)
    class_results = {}
    for key in sorted(by_class, key=lambda k: (-len(by_class[k]), k)):
        om = by_class[key][0]
        r = eval_one(ins_from_omit(om), 5, labels)
        r.update({
            "family": "orbit_rep",
            "class_key": fmt_key(key),
            "class_size": len(by_class[key]),
            "is_motif_M": key == MOTIF_M,
            "omit": "|".join(str(om[i]) for i in range(5)),
        })
        rows.append(r)
        class_results[key] = r
        tag = "MOTIF_M" if key == MOTIF_M else ""
        print(
            f"  {fmt_key(key):<48} n={len(by_class[key]):3d}  "
            f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}  {tag}"
        )
    print()

    print(f"MOTIF M UNIFORMITY SAMPLE N={N_UNIFORM}")
    print("-" * 80)
    rng = np.random.default_rng(BASE_SEED + 77)
    M_list = by_class[MOTIF_M]
    # include designed witness (index 0) + random distinct others
    idxs = [0] + list(
        rng.choice(range(1, len(M_list)), size=min(N_UNIFORM - 1, len(M_list) - 1), replace=False)
    )
    m_phis = []
    m_cores = []
    for i, idx in enumerate(idxs):
        om = M_list[int(idx)]
        r = eval_one(ins_from_omit(om), 5, labels)
        r.update({
            "family": "motif_M_sample",
            "class_key": fmt_key(MOTIF_M),
            "class_size": len(M_list),
            "is_motif_M": True,
            "omit": "|".join(str(om[i]) for i in range(5)),
            "sample_i": i,
        })
        rows.append(r)
        m_phis.append(r["core_phi"])
        m_cores.append(r["n_core"])
    m_all5 = all(abs(p - 5.0) < PHI_EPS for p in m_phis)
    m_all4 = all(c == 4 for c in m_cores)
    print(f"  Φ hist={Counter(round(p, 3) for p in m_phis)}  "
          f"n_cores={Counter(m_cores)}  all_Φ5={m_all5} all_ncore4={m_all4}")
    print()

    # derangement control (1 sample)
    print("DERANGEMENT CONTROL")
    print("-" * 80)
    om_d = ders[0]
    rd = eval_one(ins_from_omit(om_d), 5, labels)
    print(f"  derangement[0] Φ={rd['core_phi']:.1f} n_core={rd['n_core']}  "
          f"(expect 9 / 5)")
    print(f"  elapsed_eval={round(time.time() - t0, 2)}s")
    print()

    # ---- Hypotheses ----
    m_rep = class_results[MOTIF_M]
    h1 = (
        ctrl and poles_ok
        and abs(m_rep["core_phi"] - 5.0) < PHI_EPS
        and m_rep["n_core"] == 4
        and m_all5 and m_all4
        and len(M_list) == 120
    )
    other_keys = [k for k in class_results if k != MOTIF_M]
    h2 = all(abs(class_results[k]["core_phi"] - 5.0) >= PHI_EPS for k in other_keys)
    siblings = [
        k for k in class_results
        if k[0] == (0, 1, 1, 1, 2) and k != MOTIF_M
    ]
    h3 = all(abs(class_results[k]["core_phi"] - 6.0) < PHI_EPS for k in siblings)
    h4 = h1 and h2
    h5 = len(M_list) == 120 and h1

    if h4 and h3 and h5:
        reading = (
            "MOTIF_DISCRIMINANT — Φ=5 iff omit motif M "
            "(indeg (0,1,1,1,2) + 3-cycle + recip=0); same-indeg siblings → Φ=6; "
            "designed witness class size 120"
        )
        verdict_word = "MOTIF_DISCRIMINANT"
    elif h1 and not h2:
        reading = "MULTI_MOTIF — Φ=5 arises from more than motif M"
        verdict_word = "MULTI_MOTIF"
    else:
        reading = "PARTIAL — discriminant incomplete"
        verdict_word = "PARTIAL"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  motif M rep: Φ={m_rep['core_phi']:.1f} n_core={m_rep['n_core']}  "
          f"class_size={len(M_list)}")
    print(f"  M sample: all_Φ5={m_all5} all_ncore4={m_all4} N={len(m_phis)}")
    print(f"  other classes Φ≠5: {h2}  "
          f"(phis={[round(class_results[k]['core_phi'], 1) for k in other_keys]})")
    print(f"  same-indeg siblings Φ=6: {h3}  keys={len(siblings)}")
    print(f"  H1 (motif M → Φ=5, n_core=4):           "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (no other nonder class → Φ=5):       "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (same-indeg siblings → Φ=6):         "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (Φ=5 exactly motif M):               "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (designed witness, |M|=120):         "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  discriminant: motif M = indeg(0,1,1,1,2) + 3-cycle + recip=0")
    print(f"  Φ=5 vs Φ=6: 3-cycle vs other cycles (within same indeg type)")
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
            "family", "class_key", "class_size", "is_motif_M", "omit",
            "structure", "whole_phi_mip", "core", "core_phi", "n_core",
            "mean_degree", "clustering",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "class_key": r["class_key"],
                "class_size": r["class_size"],
                "is_motif_M": str(r["is_motif_M"]),
                "omit": r["omit"],
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
            "motif_M_size": len(M_list),
            "n_nonder_classes": len(by_class),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
