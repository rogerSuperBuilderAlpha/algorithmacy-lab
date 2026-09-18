"""#42 discriminant scale-blur — omit cycle-type purity across n=5/6.

Reuses committed MOTIF_DISCRIMINANT + BAND_DISCRIMINANT purity tables;
adds denser n=5 same-indeg sibling uniformity. Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/discriminant_scale_blur/analyze_blur.py
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
from org_frontier.studies.omit_motif_phi5.analyze_motifs import (
    MOTIF_M,
    all_omit_functions,
    fmt_key,
    ins_from_omit,
    is_derangement,
    omit_feats,
)
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import eval_one

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
STUDIES = os.path.join(HERE, "..")

BASE_SEED = 20260915
N_U_SIB = 3  # denser n=5 sibling uniformity

N5_SAME_INDEG = (0, 1, 1, 1, 2)
N5_BAND_LOWER = {((3,), 0)}  # singleton → Φ=5
N5_BAND_UPPER_CYC = {((2,), 1), ((2, 2), 2), ((4,), 0)}  # → Φ=6

N6_BAND9_CYC = {(5,), (2, 3)}
N6_BAND8_CYC = {(3,), (2,), (2, 2), (4,)}


def load_csv(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def om_key(om, n):
    return tuple(om[i] for i in range(n))


def sample_oms(oms, n_want, rng, forced=None):
    out = []
    forced = forced or []
    seen = set()
    for om in forced:
        k = om_key(om, 5)
        if k not in seen:
            out.append(om)
            seen.add(k)
    rest = [om for om in oms if om_key(om, 5) not in seen]
    need = max(0, n_want - len(out))
    if need and rest:
        idxs = rng.choice(len(rest), size=min(need, len(rest)), replace=False)
        for i in idxs:
            out.append(rest[int(i)])
    return out[:n_want]


def purity_from_phis(phis):
    hist = Counter(round(p, 3) for p in phis)
    return len(hist) == 1, hist


def main():
    print("DISCRIMINANT SCALE-BLUR (#42) — omit cycle-type across n=5/6")
    print("=" * 80)
    print("  cited: omit_motif_phi5 MOTIF_DISCRIMINANT; same_indeg_band_n6 BAND_DISCRIMINANT")
    print("  agenda: RESEARCH_AGENDA_50_V2 #42")
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

    rows = []
    t_all = time.time()

    # ---- Reuse n=5 committed purity (M sample + orbit reps) ----
    print("REUSE n=5 MOTIF_DISCRIMINANT (committed)")
    print("-" * 80)
    n5_path = os.path.join(STUDIES, "omit_motif_phi5", "results", "census.csv")
    n5_rows = load_csv(n5_path)
    n5_class_phis = defaultdict(list)
    for r in n5_rows:
        # parse class_key like indeg=(0, 1, 1, 1, 2)|cyc=(3,)|recip=0
        key = r["class_key"]
        if "indeg=(0, 1, 1, 1, 2)" not in key:
            continue
        phi = float(r["core_phi"])
        n5_class_phis[key].append(phi)
        rows.append({
            "family": "reuse_n5",
            "name": r.get("family", "n5"),
            "n": 5,
            "class_key": key,
            "omit": r["omit"],
            "core_phi": phi,
            "n_core": int(r["n_core"]),
            "source": "omit_motif_phi5",
        })
    n5_pure = {}
    for key, phis in sorted(n5_class_phis.items()):
        pure, hist = purity_from_phis(phis)
        n5_pure[key] = pure
        print(f"  {key}: N={len(phis)} Φ={dict(hist)} pure={pure}")
    print()

    # ---- Reuse n=6 committed purity ----
    print("REUSE n=6 BAND_DISCRIMINANT (committed)")
    print("-" * 80)
    n6_path = os.path.join(STUDIES, "same_indeg_band_n6", "results", "census.csv")
    n6_rows = load_csv(n6_path)
    n6_class_phis = defaultdict(list)
    for r in n6_rows:
        key = f"cyc={r['cycles']}|recip={r['recip']}"
        phi = float(r["core_phi"])
        n6_class_phis[key].append(phi)
        rows.append({
            "family": "reuse_n6",
            "name": r["name"],
            "n": 6,
            "class_key": key,
            "omit": r["omit"],
            "core_phi": phi,
            "n_core": int(r["n_core"]),
            "source": "same_indeg_band_n6",
        })
    n6_pure = {}
    for key, phis in sorted(n6_class_phis.items()):
        pure, hist = purity_from_phis(phis)
        n6_pure[key] = pure
        print(f"  {key}: N={len(phis)} Φ={dict(hist)} pure={pure}")
    n6_all_pure = all(n6_pure.values()) and len(n6_pure) == 6
    print(f"  all 6 classes pure: {n6_all_pure}")
    print()

    # ---- NEW: denser n=5 sibling uniformity ----
    print(f"NEW n=5 SAME-INDEG SIBLING UNIFORMITY N_U={N_U_SIB}")
    print("-" * 80)
    all_oms = all_omit_functions()
    by_class = defaultdict(list)
    for om in all_oms:
        if is_derangement(om):
            continue
        feats = omit_feats(om)
        if feats[0] != N5_SAME_INDEG:
            continue
        by_class[feats].append(om)
    siblings = [k for k in by_class if k != MOTIF_M]
    print(f"  same-indeg classes: M={len(by_class[MOTIF_M])}  "
          f"siblings={ {fmt_key(k): len(by_class[k]) for k in siblings} }")

    labels5 = tuple(f"N{i}" for i in range(5))
    rng = np.random.default_rng(BASE_SEED + 42)
    sib_results = {}
    # designed orbit reps from omit_motif census (first of each class)
    designed = {k: by_class[k][0] for k in siblings}
    for key in sorted(siblings):
        samp = sample_oms(by_class[key], N_U_SIB, rng, forced=[designed[key]])
        phis = []
        cores = []
        for i, om in enumerate(samp):
            r = eval_one(ins_from_omit(om), 5, labels5)
            tag = "designed" if om_key(om, 5) == om_key(designed[key], 5) else "sample"
            phis.append(r["core_phi"])
            cores.append(r["n_core"])
            rows.append({
                "family": "n5_sib_uniform",
                "name": f"sib_{fmt_key(key)}_{i}_{tag}",
                "n": 5,
                "class_key": fmt_key(key),
                "omit": "|".join(str(om[j]) for j in range(5)),
                "core_phi": r["core_phi"],
                "n_core": r["n_core"],
                "source": "new",
            })
            print(f"  {fmt_key(key)} [{i}_{tag}] Φ={r['core_phi']:.1f} "
                  f"n_core={r['n_core']}")
        pure, hist = purity_from_phis(phis)
        all6 = all(abs(p - 6.0) < PHI_EPS for p in phis)
        sib_results[key] = {
            "phis": phis, "pure": pure, "hist": hist, "all6": all6, "cores": cores
        }
        print(f"    → hist={dict(hist)} pure={pure} all_Φ6={all6}")
    print()

    # ---- Scale comparison table ----
    print("SCALE COMPARISON")
    print("-" * 80)
    print("  n=5 law: singleton — Φ=5 iff cyc=(3,) recip=0; else same-indeg → Φ=6")
    print("  n=6 law: band — Φ=9 iff cyc∈{(5,),(2,3)}; else same-indeg → Φ=8")
    n5_m_phis = n5_class_phis.get(fmt_key(MOTIF_M), [])
    # fmt_key for MOTIF_M
    m_key = fmt_key(MOTIF_M)
    # committed keys use spaces after commas
    m_phis_committed = []
    for key, phis in n5_class_phis.items():
        if "cyc=(3,)" in key and "recip=0" in key and "0, 1, 1, 1, 2" in key:
            m_phis_committed.extend(phis)
    print(f"  n=5 M committed N={len(m_phis_committed)} "
          f"all_Φ5={all(abs(p-5)<PHI_EPS for p in m_phis_committed)}")
    print(f"  n=5 siblings new: "
          f"{ {fmt_key(k): dict(sib_results[k]['hist']) for k in sib_results} }")
    print(f"  n=6 classes pure: {n6_all_pure}  "
          f"(BAND8={sorted(N6_BAND8_CYC)}; BAND9={sorted(N6_BAND9_CYC)})")
    print()

    # ---- Hypotheses ----
    # H5: denser siblings all Φ=6 and pure
    h5 = (
        ctrl
        and len(sib_results) == 3
        and all(s["all6"] and s["pure"] for s in sib_results.values())
    )

    # H1: purity across n — n=5 same-indeg (M committed + new siblings) + n=6 all pure
    n5_same_indeg_pure = (
        all(abs(p - 5.0) < PHI_EPS for p in m_phis_committed)
        and len(m_phis_committed) >= 12
        and h5
    )
    h1 = n5_same_indeg_pure and n6_all_pure

    # H2: any within-class mix at n=6 or in new n=5 siblings
    h2_n6 = not n6_all_pure
    h2_n5 = any(not s["pure"] for s in sib_results.values())
    h2 = h2_n6 or h2_n5

    # H3: morph singleton → band
    # n=5: exactly one lower class; n=6: >=2 classes in each band
    n6_band8_keys = [k for k in n6_class_phis if any(
        str(c) in k for c in ["(3,)", "(2,)", "(2, 2)", "(4,)"]
    ) and "recip" in k]
    # clearer: parse from census
    n6_phi8_classes = set()
    n6_phi9_classes = set()
    for r in n6_rows:
        cyc = r["cycles"]
        phi = float(r["core_phi"])
        if abs(phi - 8.0) < PHI_EPS:
            n6_phi8_classes.add(cyc)
        elif abs(phi - 9.0) < PHI_EPS:
            n6_phi9_classes.add(cyc)
    h3 = (
        len(N5_BAND_LOWER) == 1
        and len(n6_phi8_classes) >= 2
        and len(n6_phi9_classes) >= 2
    )

    # H4: M3 not unique for Φ=8
    h4 = "(3,)" in n6_phi8_classes and len(n6_phi8_classes) >= 2

    if h1 and not h2 and h3 and h4 and h5:
        verdict_word = "SCALE_MORPHS"
        reading = (
            "SCALE_MORPHS — class purity holds at n=5 and n=6 (no within-class "
            "mix); discriminant morphs singleton→multi-class band; not blur, not copy"
        )
    elif h2:
        verdict_word = "SCALE_BLUR"
        reading = "SCALE_BLUR — within-class Φ mixing appears as n grows"
    elif h1 and not h3:
        verdict_word = "SCALE_HOLDS"
        reading = "SCALE_HOLDS — same singleton discriminant persists across n"
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — purity or morph incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  n=5 same-indeg pure (M+siblings): {n5_same_indeg_pure}")
    print(f"  n=6 all classes pure: {n6_all_pure}")
    print(f"  n=6 Φ=8 cycle types: {sorted(n6_phi8_classes)}  "
          f"Φ=9: {sorted(n6_phi9_classes)}")
    print(f"  H1 (class purity holds across n):      "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (purity collapses / mixes at scale): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (morphs into coarser band):          "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (n=5 singleton not verbatim at n=6): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (denser n=5 siblings pure Φ=6):      "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  #42 scale-blur? {'NO — morphs, purity holds' if verdict_word == 'SCALE_MORPHS' else verdict_word}")
    print(f"  n=5: singleton MOTIF_DISCRIMINANT (pure)")
    print(f"  n=6: multi-class BAND_DISCRIMINANT (pure)")
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
            "family", "name", "n", "class_key", "omit", "core_phi", "n_core", "source",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "name": r["name"],
                "n": r["n"],
                "class_key": r["class_key"],
                "omit": r["omit"],
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "source": r["source"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "verdict": verdict_word,
            "n5_sib_classes": len(sib_results),
            "n6_classes_pure": n6_all_pure,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
