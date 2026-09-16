"""Same-indeg Φ=8 vs 9 band at n=6 fixed_k=4.

Dense uniformity over the six (cycles, recip) classes with indeg
(0,1,1,1,1,2). Hypotheses fixed in hypotheses.md.
Extends omit_lift_n6 LAWS_MORPH; compares to omit_motif_phi5.

Run:  python org_frontier/studies/same_indeg_band_n6/analyze_band.py
"""

from __future__ import annotations

import csv
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
from org_frontier.studies.omit_lift_n6.analyze_lift import (
    MOTIF_M3,
    enumerate_same_indeg_classes,
    fmt_omit,
    ins_from_omit,
    omit_feats,
)
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import eval_one

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N = 6
BASE_SEED = 20260915
N_U = 3  # uniformity per class (designed + random)
EXPECT_SIZES = {
    ((2,), 1): 720,
    ((2, 2), 2): 360,
    ((2, 3), 1): 600,
    ((3,), 0): 720,
    ((4,), 0): 720,
    ((5,), 0): 720,
}
BAND8_CYCLES = {(3,), (2,), (2, 2), (4,)}
BAND9_CYCLES = {(2, 3), (5,)}

# Designed witnesses from omit_lift_n6 census (omit string → dict)
DESIGNED = {
    ((3,), 0): [{0: 1, 1: 2, 2: 0, 3: 0, 4: 3, 5: 4}],  # M3
    ((2,), 1): [{0: 1, 1: 0, 2: 0, 3: 2, 4: 3, 5: 4}],
    ((2, 2), 2): [{0: 1, 1: 0, 2: 0, 3: 2, 4: 5, 5: 4}],
    ((2, 3), 1): [{0: 1, 1: 0, 2: 0, 3: 4, 4: 5, 5: 3}],
    ((4,), 0): [{0: 1, 1: 2, 2: 3, 3: 0, 4: 0, 5: 4}],
    ((5,), 0): [{0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 0}],
}


def om_key(om):
    return tuple(om[i] for i in range(N))


def sample_class(oms, n_want, rng, forced_oms):
    out = []
    forced_keys = set()
    for om in forced_oms:
        k = om_key(om)
        if k not in forced_keys:
            out.append(om)
            forced_keys.add(k)
    rest = [om for om in oms if om_key(om) not in forced_keys]
    need = max(0, n_want - len(out))
    if need > 0 and rest:
        idxs = rng.choice(len(rest), size=min(need, len(rest)), replace=False)
        for i in idxs:
            out.append(rest[int(i)])
    return out[:n_want]


def main():
    print("SAME-INDEG Φ=8 vs 9 BAND — n=6 fixed_k=4")
    print("=" * 80)
    print("  cited: omit_lift_n6 LAWS_MORPH; omit_motif_phi5 MOTIF_DISCRIMINANT")
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

    print("H5 CLASS CATALOG")
    print("-" * 80)
    by_class = enumerate_same_indeg_classes()
    sizes = {k: len(v) for k, v in sorted(by_class.items())}
    print(f"  indeg=(0,1,1,1,1,2) classes={sizes}")
    print(f"  total={sum(sizes.values())}")
    h5 = sizes == EXPECT_SIZES
    print(f"  match omit_lift catalog: {'PASS' if h5 else 'FAIL'}")
    # verify designed witnesses land in claimed classes
    for key, oms in DESIGNED.items():
        feats = omit_feats(oms[0])
        assert feats[0] == (0, 1, 1, 1, 1, 2), feats
        assert (feats[1], feats[2]) == key, (feats, key)
    print(f"  designed witnesses: {len(DESIGNED)} keys OK")
    print()

    labels = tuple(f"N{i}" for i in range(N))
    rows = []
    t_all = time.time()
    rng = np.random.default_rng(BASE_SEED + 89)

    print(f"UNIFORMITY SAMPLE N_U={N_U} per class")
    print("-" * 80)
    class_phis = {}
    class_cores = {}
    for key in sorted(by_class.keys()):
        cyc, recip = key
        forced = DESIGNED.get(key, [])
        samp = sample_class(by_class[key], N_U, rng, forced)
        phis = []
        cores = []
        for i, om in enumerate(samp):
            feats = omit_feats(om)
            assert (feats[1], feats[2]) == key
            r = eval_one(ins_from_omit(om), N, labels)
            tag = "designed" if i < len(forced) and om_key(om) == om_key(forced[0]) else "sample"
            # mark designed if matches any forced
            if any(om_key(om) == om_key(f) for f in forced):
                tag = "designed"
            r.update({
                "family": "same_indeg",
                "name": f"cyc{cyc}_r{recip}_{i}_{tag}",
                "omit": fmt_omit(om),
                "cycles": str(cyc),
                "recip": recip,
                "band": "BAND9" if cyc in BAND9_CYCLES else "BAND8",
            })
            rows.append(r)
            phis.append(r["core_phi"])
            cores.append(r["n_core"])
            print(
                f"  cyc={cyc} r={recip} [{i}_{tag}]  "
                f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}"
            )
        class_phis[key] = phis
        class_cores[key] = cores
        hist = Counter(round(p, 3) for p in phis)
        pure = len(hist) == 1
        print(f"    → hist={dict(hist)}  pure={pure}  n_cores={Counter(cores)}")
    print()

    # ---- contingency ----
    print("CONTINGENCY (cycles, recip) × Φ")
    print("-" * 80)
    for key in sorted(class_phis.keys()):
        cyc, recip = key
        hist = Counter(round(p, 3) for p in class_phis[key])
        expect = 9.0 if cyc in BAND9_CYCLES else 8.0
        ok = all(abs(p - expect) < PHI_EPS for p in class_phis[key])
        print(f"  cyc={cyc} recip={recip} n={sizes[key]}  "
              f"Φ={dict(hist)}  band_expect={expect:.0f}  match={ok}")
    print()

    # ---- hypotheses ----
    # H2: any class mixes 8 and 9
    h2 = False
    for phis in class_phis.values():
        has8 = any(abs(p - 8.0) < PHI_EPS for p in phis)
        has9 = any(abs(p - 9.0) < PHI_EPS for p in phis)
        if has8 and has9:
            h2 = True
            break

    # H1: band law holds for all tested
    h1_ok = True
    for key, phis in class_phis.items():
        cyc, _ = key
        expect = 9.0 if cyc in BAND9_CYCLES else 8.0
        if not all(abs(p - expect) < PHI_EPS for p in phis):
            h1_ok = False
            break
    all_pure = all(len(Counter(round(p, 3) for p in phis)) == 1
                   for phis in class_phis.values())
    h1 = ctrl and h1_ok and all_pure and not h2

    # H3: recip alone or n_core alone
    recip_to_phis = defaultdict(set)
    for key, phis in class_phis.items():
        _, recip = key
        for p in phis:
            recip_to_phis[recip].add(round(p, 1))
    recip_alone = all(len(v) == 1 for v in recip_to_phis.values()) and len(recip_to_phis) >= 2
    # stronger: does a single recip value map to only one Φ across classes?
    # "recip alone separates" means there exists a function recip→Φ that works
    # for all classes. Check if each recip maps to exactly one Φ.
    all_cores = [c for cores in class_cores.values() for c in cores]
    ncore_alone = len(set(all_cores)) >= 2 and (
        # Φ tracks n_core: all Φ=8 share one n_core distinct from Φ=9
        False  # will compute below
    )
    phi8_cores = set()
    phi9_cores = set()
    for key, phis in class_phis.items():
        for p, c in zip(phis, class_cores[key]):
            if abs(p - 8.0) < PHI_EPS:
                phi8_cores.add(c)
            elif abs(p - 9.0) < PHI_EPS:
                phi9_cores.add(c)
    ncore_separates = (
        len(phi8_cores) == 1 and len(phi9_cores) == 1
        and phi8_cores != phi9_cores
    )
    all_ncore5 = all(c == 5 for c in all_cores)
    h3 = recip_alone or ncore_separates

    # H4: Φ=8 not unique to M3
    phi8_keys = [
        key for key, phis in class_phis.items()
        if any(abs(p - 8.0) < PHI_EPS for p in phis)
    ]
    h4 = len(phi8_keys) >= 2 and ((3,), 0) in phi8_keys

    if h1 and not h2 and not h3 and h4 and h5:
        verdict_word = "BAND_DISCRIMINANT"
        reading = (
            "BAND_DISCRIMINANT — within indeg (0,1,1,1,1,2), Φ=9 iff "
            "cycles∈{(5,),(2,3)}; else Φ=8; classes pure; not n=5 3-cycle singleton; "
            "not recip/n_core alone"
        )
    elif h2:
        verdict_word = "COLLAPSE"
        reading = "COLLAPSE — same (cycles, recip) class mixes Φ=8 and Φ=9"
    elif h1 and not h4:
        verdict_word = "SINGLETON_ANALOGUE"
        reading = "SINGLETON_ANALOGUE — Φ=8 unique to 3-cycle motif (n=5 style)"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — band law incomplete or alternate separator"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  band law match all classes: {h1_ok}  all_pure={all_pure}")
    print(f"  recip→Φ maps: { {k: sorted(v) for k, v in recip_to_phis.items()} }  "
          f"recip_alone={recip_alone}")
    print(f"  n_cores all5={all_ncore5}  phi8_cores={phi8_cores}  "
          f"phi9_cores={phi9_cores}  ncore_sep={ncore_separates}")
    print(f"  Φ=8 classes: {phi8_keys}")
    print(f"  H1 (cycle-type band 8 vs 9):        "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (within-class mix collapse):     "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (recip or n_core alone):         "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (no 3-cycle singleton analogue): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (class catalog stable):          "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  discriminant: Φ=9 iff cycles∈{{(5,),(2,3)}}; else Φ=8 "
          f"(indeg (0,1,1,1,1,2))")
    print(f"  vs n=5: MOTIF_DISCRIMINANT was 3-cycle singleton; "
          f"n=6 is multi-class band")
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
            "family", "name", "omit", "cycles", "recip", "band",
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
                "recip": r["recip"],
                "band": r["band"],
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
            "n_per_class": N_U,
            "n_classes": len(by_class),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
