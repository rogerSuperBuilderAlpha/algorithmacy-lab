"""Indeg (0,0,1,1,2,2) band test at n=6 fixed_k=4.

Different fingerprint from closed (0,1,1,1,1,2). Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/indeg_002122_n6/analyze_indeg.py
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
from org_frontier.studies.omit_lift_n6.analyze_lift import omit_feats, fmt_omit, ins_from_omit
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import eval_one

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N = 6
TARGET_INDEG = (0, 0, 1, 1, 2, 2)
BASE_SEED = 20260915
N_U = 3
EXPECT_SIZES = {
    ((2,), 1): 2160,
    ((2, 2), 2): 540,
    ((3,), 0): 1800,
    ((4,), 0): 1080,
}
DESIGNED = {
    ((2,), 1): {0: 1, 1: 0, 2: 0, 3: 1, 4: 2, 5: 3},
    ((2, 2), 2): {0: 1, 1: 0, 2: 0, 3: 1, 4: 5, 5: 4},
    ((3,), 0): {0: 1, 1: 2, 2: 0, 3: 0, 4: 1, 5: 3},
    ((4,), 0): {0: 1, 1: 2, 2: 3, 3: 0, 4: 0, 5: 1},
}


def is_derangement(om):
    vals = [om[i] for i in range(N)]
    return sorted(vals) == list(range(N))


def enumerate_classes():
    by = defaultdict(list)
    for choices in itertools.product(
        *[[j for j in range(N) if j != i] for i in range(N)]
    ):
        om = {i: choices[i] for i in range(N)}
        if is_derangement(om):
            continue
        feats = omit_feats(om)
        if feats[0] != TARGET_INDEG:
            continue
        by[(feats[1], feats[2])].append(om)
    return by


def om_key(om):
    return tuple(om[i] for i in range(N))


def sample_class(oms, n_want, rng, forced):
    out = []
    seen = set()
    if forced is not None:
        out.append(forced)
        seen.add(om_key(forced))
    rest = [om for om in oms if om_key(om) not in seen]
    need = max(0, n_want - len(out))
    if need and rest:
        idxs = rng.choice(len(rest), size=min(need, len(rest)), replace=False)
        for i in idxs:
            out.append(rest[int(i)])
    return out[:n_want]


def main():
    print("INDEG (0,0,1,1,2,2) BAND — n=6 fixed_k=4")
    print("=" * 80)
    print("  cited: same_indeg_band_n6 BAND_DISCRIMINANT; omit_motif_phi5; OMIT_ATOM_ARC")
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

    print("CLASS CATALOG")
    print("-" * 80)
    by_class = enumerate_classes()
    sizes = {k: len(v) for k, v in sorted(by_class.items())}
    print(f"  indeg={TARGET_INDEG} classes={sizes}")
    print(f"  total={sum(sizes.values())}")
    catalog_ok = sizes == EXPECT_SIZES
    print(f"  catalog match: {'PASS' if catalog_ok else 'FAIL'}")
    for key, om in DESIGNED.items():
        assert omit_feats(om)[0] == TARGET_INDEG
        assert (omit_feats(om)[1], omit_feats(om)[2]) == key
    print()

    labels = tuple(f"N{i}" for i in range(N))
    rows = []
    t_all = time.time()
    rng = np.random.default_rng(BASE_SEED + 122)
    class_phis = {}

    print(f"UNIFORMITY N_U={N_U} per class")
    print("-" * 80)
    for key in sorted(by_class.keys()):
        cyc, recip = key
        samp = sample_class(by_class[key], N_U, rng, DESIGNED[key])
        phis = []
        for i, om in enumerate(samp):
            r = eval_one(ins_from_omit(om), N, labels)
            tag = "designed" if i == 0 else "sample"
            r.update({
                "family": "indeg_002122",
                "name": f"cyc{cyc}_r{recip}_{i}_{tag}",
                "omit": fmt_omit(om),
                "cycles": str(cyc),
                "recip": recip,
            })
            rows.append(r)
            phis.append(r["core_phi"])
            print(f"  cyc={cyc} r={recip} [{i}_{tag}]  "
                  f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}")
        class_phis[key] = phis
        hist = Counter(round(p, 3) for p in phis)
        print(f"    → hist={dict(hist)} pure={len(hist)==1}")
    print()

    print("CONTINGENCY")
    print("-" * 80)
    all_phis = []
    for key in sorted(class_phis):
        cyc, recip = key
        hist = Counter(round(p, 3) for p in class_phis[key])
        all_phis.extend(class_phis[key])
        print(f"  cyc={cyc} recip={recip} n={sizes[key]}  Φ={dict(hist)}")
    distinct = sorted({round(p, 6) for p in all_phis})
    print(f"  distinct Φ={distinct}")
    print()

    all_pure = all(len(Counter(round(p, 3) for p in phis)) == 1
                   for phis in class_phis.values())
    h3 = not all_pure  # mix
    distinct_all = sorted({round(p, 6) for p in all_phis})
    # modal Φ per class (for flat/band claims when pure)
    class_modal = {
        k: Counter(round(p, 6) for p in phis).most_common(1)[0][0]
        for k, phis in class_phis.items()
    }
    distinct_modals = sorted(set(class_modal.values()))
    h2 = all_pure and len(distinct_all) == 1
    h1 = all_pure and len(distinct_all) >= 2 and ctrl and catalog_ok

    recip_to_phis = defaultdict(set)
    for (cyc, recip), phis in class_phis.items():
        for p in phis:
            recip_to_phis[recip].add(round(p, 1))
    recip_alone = (
        len(distinct_all) >= 2
        and all(len(v) == 1 for v in recip_to_phis.values())
        and len({next(iter(v)) for v in recip_to_phis.values()})
        == len(distinct_all)
    )
    # H4: recip alone does NOT separate — when ≥2 Φ appear
    h4 = len(distinct_all) >= 2 and not recip_alone

    if h1 and not h3:
        verdict_word = "BAND_OR_SPLIT"
        reading = (
            f"BAND_OR_SPLIT — indeg {TARGET_INDEG}: cycle classes pure with "
            f"distinct Φ={distinct_all}; cycle-type discriminant survives"
        )
    elif h2 and not h3:
        verdict_word = "FLAT"
        reading = (
            f"FLAT — indeg {TARGET_INDEG}: all cycle classes share Φ="
            f"{distinct_all[0]}; no cycle-type discriminant"
        )
    elif h3:
        verdict_word = "MIX"
        reading = (
            f"MIX — within-class Φ mixing under indeg {TARGET_INDEG} "
            f"(seen Φ={distinct_all})"
        )
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  all_pure={all_pure}  distinct_Φ={distinct_all}  "
          f"modals={distinct_modals}")
    print(f"  recip→Φ={ {k: sorted(v) for k,v in recip_to_phis.items()} }  "
          f"recip_alone={recip_alone}")
    print(f"  H1 (cycle-type band/discriminant):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (flat — one Φ all classes):      "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (within-class mix):              "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (recip alone does not separate): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  indeg: {TARGET_INDEG}")
    print(f"  distinct Φ: {distinct_all}")
    print(f"  vs closed band (0,1,1,1,1,2): "
          f"{'also cycle-split' if h1 else 'flat or mix — fingerprint-dependent'}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "family", "name", "omit", "cycles", "recip", "structure",
            "whole_phi_mip", "core", "core_phi", "n_core", "mean_degree", "clustering",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "name": r["name"],
                "omit": r["omit"],
                "cycles": r["cycles"],
                "recip": r["recip"],
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
            "verdict": verdict_word,
            "distinct_phi": ";".join(str(p) for p in distinct_all),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
