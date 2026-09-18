"""Omit cycle-type morph at n=7 (RESEARCH_AGENDA_V3 #8).

Does the omit cycle-type discriminant morph again at n=7, or does the
n=5→n=6 singleton→band shift (V2 #42 SCALE_MORPHS) stabilize into a
fixed band grammar? Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Reuses committed n=5/n=6 purity tables; new compute is n=7 indeg
(0,1,1,1,1,1,2) cycle-type catalog + light uniformity.

Run:  python org_frontier/studies/omit_cycle_morph_n7/analyze_morph_n7.py
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
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import eval_one

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
STUDIES = os.path.join(HERE, "..")

N = 7
K = 5  # fixed_k = n-2
TARGET_INDEG = (0, 1, 1, 1, 1, 1, 2)
BASE_SEED = 20260918
N_U = 2  # uniformity on selected classes
# classes to double-sample for purity (filled after catalog discovery if present)
PURITY_KEYS = None  # set in main after catalog

# Reused priors (committed)
N5_SINGLETON = {((3,), 0)}  # → Φ=5
N5_SIBLING = {((2,), 1), ((2, 2), 2), ((4,), 0)}  # → Φ=6
N6_BAND9 = {(5,), (2, 3)}
N6_BAND8 = {(3,), (2,), (2, 2), (4,)}


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def omit_feats(om, n=N):
    indeg = Counter(om[i] for i in range(n))
    indeg_sig = tuple(sorted(indeg[i] for i in range(n)))
    seen = set()
    cyc_lens = []
    for start in range(n):
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
    recip = sum(1 for i in range(n) if om[om[i]] == i) // 2
    return indeg_sig, tuple(sorted(cyc_lens)), recip


def is_derangement(om, n=N):
    vals = [om[i] for i in range(n)]
    return sorted(vals) == list(range(n)) and all(om[i] != i for i in range(n))


def ins_from_omit(om, n=N):
    return {i: [j for j in range(n) if j != i and j != om[i]] for i in range(n)}


def fmt_omit(om, n=N):
    return "|".join(str(om[i]) for i in range(n))


def om_key(om, n=N):
    return tuple(om[i] for i in range(n))


def sample_target_classes(n_target=250000, seed=BASE_SEED):
    """Monte-Carlo catalog of (cyc, recip) under TARGET_INDEG."""
    rng = np.random.default_rng(seed)
    by = defaultdict(list)
    hits = 0
    for _ in range(n_target):
        om = {}
        for i in range(N):
            choices = [j for j in range(N) if j != i]
            om[i] = int(choices[rng.integers(0, len(choices))])
        if is_derangement(om):
            continue
        sig, cyc, recip = omit_feats(om)
        if sig != TARGET_INDEG:
            continue
        hits += 1
        key = (cyc, recip)
        if len(by[key]) < 8:
            by[key].append(om)
    return by, hits


def load_csv(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def purity(phis):
    hist = Counter(round(float(p), 6) for p in phis)
    return len(hist) == 1, hist


def run_omit(om, tag, family):
    labels = tuple(f"N{i}" for i in range(N))
    ins = ins_from_omit(om)
    t0 = time.time()
    r = eval_one(ins, N, labels)
    sig, cyc, recip = omit_feats(om)
    return {
        "family": family,
        "name": tag,
        "n": N,
        "omit": fmt_omit(om),
        "indeg": str(sig),
        "cycles": str(cyc),
        "recip": recip,
        "class_key": f"cyc={cyc}|recip={recip}",
        "structure": r["structure"],
        "whole_phi_mip": r["whole_phi_mip"],
        "core": "|".join(r["core"]) if r["core"] else "",
        "core_phi": r["core_phi"],
        "n_core": r["n_core"],
        "seconds": round(time.time() - t0, 2),
    }


def main():
    os.makedirs(RESULTS, exist_ok=True)
    print("OMIT CYCLE-TYPE MORPH n=7 — V3 #8")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 80)

    print("INSTRUMENT CONTROL")
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")

    # ---- reuse n=5 / n=6 priors from committed CSVs ----
    print("\nREUSED PRIORS (n=5 singleton / n=6 band)")
    blur = load_csv(os.path.join(STUDIES, "discriminant_scale_blur", "results", "census.csv"))
    n5 = [r for r in blur if r.get("n") == "5" or str(r.get("n")) == "5"]
    band6 = load_csv(os.path.join(STUDIES, "same_indeg_band_n6", "results", "census.csv"))
    print(f"  discriminant_scale_blur rows n=5-ish: {len(n5)} (file has {len(blur)} total)")
    print(f"  same_indeg_band_n6 rows: {len(band6)}")
    # summarize n=6 purity from census
    by6 = defaultdict(list)
    for r in band6:
        by6[r.get("cycles", "") + "|r" + str(r.get("recip", ""))].append(float(r["core_phi"]))
    n6_pure = all(purity(v)[0] for v in by6.values() if v)
    n6_phis = sorted({round(float(r["core_phi"]), 3) for r in band6})
    print(f"  n=6 class purity (all classes): {n6_pure}; Φ set={n6_phis}")

    # ---- n=7 catalog ----
    print("\nN=7 CLASS CATALOG (MC sample under indeg (0,1,1,1,1,1,2))")
    by_class, hits = sample_target_classes()
    print(f"  MC hits={hits} classes={len(by_class)}")
    for key in sorted(by_class.keys(), key=lambda k: (k[0], k[1])):
        print(f"    cyc={key[0]} recip={key[1]}  pool={len(by_class[key])}")

    rows = []
    # designed: one per class
    print("\nN=7 DESIGNED WITNESSES (1 per class)")
    for key in sorted(by_class.keys(), key=lambda k: (k[0], k[1])):
        om = by_class[key][0]
        tag = f"des_cyc{key[0]}_r{key[1]}"
        print(f"  computing {tag} ...", flush=True)
        row = run_omit(om, tag, "designed")
        rows.append(row)
        print(
            f"    → struct={row['structure']} coreΦ={row['core_phi']:.3f} "
            f"n_core={row['n_core']} t={row['seconds']}s"
        )

    # purity: pick two classes with distinct designed Φ if possible
    des_by_key = {}
    for r in rows:
        key = (eval(r["cycles"]) if isinstance(r["cycles"], str) else r["cycles"], int(r["recip"]))
        # cycles stored as str of tuple
        cyc = eval(r["cycles"]) if r["cycles"].startswith("(") else r["cycles"]
        des_by_key[(cyc, int(r["recip"]))] = r

    # group designed by phi
    phi_to_keys = defaultdict(list)
    for key, r in des_by_key.items():
        phi_to_keys[round(float(r["core_phi"]), 6)].append(key)

    # choose purity keys: one from each of two largest distinct-phi bands
    bands_sorted = sorted(phi_to_keys.items(), key=lambda kv: -len(kv[1]))
    purity_keys = []
    for phi, keys in bands_sorted:
        if keys:
            purity_keys.append(keys[0])
        if len(purity_keys) >= 2:
            break
    # if only one band, still purity-test two classes in it
    if len(purity_keys) < 2:
        all_keys = list(des_by_key.keys())
        for k in all_keys:
            if k not in purity_keys:
                purity_keys.append(k)
            if len(purity_keys) >= 2:
                break

    print(f"\nN=7 PURITY UNIFORMITY (N_U={N_U}) on {purity_keys}")
    rng = np.random.default_rng(BASE_SEED + 7)
    for key in purity_keys:
        pool = by_class[key]
        # ensure designed first
        forced = [des_by_key[key]["omit"]]
        # convert omit string back? use om objects from pool
        designed_om = by_class[key][0]
        chosen = [designed_om]
        seen = {om_key(designed_om)}
        rest = [om for om in pool if om_key(om) not in seen]
        need = N_U - 1
        if need > 0 and rest:
            idxs = rng.choice(len(rest), size=min(need, len(rest)), replace=False)
            for i in np.atleast_1d(idxs):
                chosen.append(rest[int(i)])
        for j, om in enumerate(chosen):
            if j == 0:
                continue  # already have designed
            tag = f"u_cyc{key[0]}_r{key[1]}_{j}"
            print(f"  computing {tag} ...", flush=True)
            row = run_omit(om, tag, "uniformity")
            rows.append(row)
            print(
                f"    → struct={row['structure']} coreΦ={row['core_phi']:.3f} "
                f"n_core={row['n_core']} t={row['seconds']}s"
            )

    # write census
    path = os.path.join(RESULTS, "census.csv")
    fields = [
        "family", "name", "n", "omit", "indeg", "cycles", "recip", "class_key",
        "structure", "whole_phi_mip", "core", "core_phi", "n_core", "seconds",
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # ---- hypothesis tests ----
    print("\nHYPOTHESIS TESTS")
    designed = [r for r in rows if r["family"] == "designed"]
    des_phis = [round(float(r["core_phi"]), 6) for r in designed]
    unique_phi = sorted(set(des_phis))
    print(f"  designed Φ set: {unique_phi}  (n_classes={len(designed)})")

    # H1 purity
    pure_ok = True
    purity_detail = []
    for key in purity_keys:
        cyc, recip = key
        class_rows = [
            r for r in rows
            if eval(r["cycles"]) == cyc and int(r["recip"]) == recip
        ]
        phis = [float(r["core_phi"]) for r in class_rows]
        ok, hist = purity(phis)
        pure_ok = pure_ok and ok and len(phis) >= N_U
        purity_detail.append((key, ok, hist, len(phis)))
        print(f"  purity {key}: ok={ok} n={len(phis)} hist={dict(hist)}")
    h1 = pure_ok and len(purity_keys) >= 2
    print(f"H1 (class purity at n=7):                    {'SUPPORTED' if h1 else 'REFUTED'}")

    # H2 discrete bands
    n_phi = len(unique_phi)
    n_cls = len(designed)
    # band grammar: at least 2 distinct Φ, and not all classes unique Φ (some multi-class band)
    phi_counts = Counter(des_phis)
    multi_class_bands = sum(1 for c in phi_counts.values() if c >= 2)
    continuum_like = n_phi >= 6 and multi_class_bands == 0
    h2 = n_phi >= 2 and not continuum_like and (multi_class_bands >= 1 or n_phi <= n_cls // 2 + 1)
    # stronger: prefer multi_class_bands >= 1 (true band)
    h2 = n_phi >= 2 and multi_class_bands >= 1 and not continuum_like
    print(
        f"H2 (discrete cycle-type bands):              {'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(f"  n_phi={n_phi} multi_class_bands={multi_class_bands} continuum_like={continuum_like}")

    # H3 not singleton
    # singleton would be: exactly one class has the minority/special Φ alone, all others share one
    # or exactly one cycle type unique at lower incomplete band
    singleton_like = (
        (n_phi == 2 and sorted(phi_counts.values()) == [1, n_cls - 1])
        or (n_phi == 1)
    )
    h3 = not singleton_like and multi_class_bands >= 1
    print(f"H3 (not n=5-style singleton):                {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  singleton_like={singleton_like}")

    if not ctrl:
        token = "CONTROLS_FAIL"
    elif not h1:
        token = "PURITY_BREAKS_N7"
    elif h1 and h2 and h3:
        token = "BAND_GRAMMAR_HOLDS"
    else:
        token = "MORPHS_AGAIN"

    h4 = token == "BAND_GRAMMAR_HOLDS"
    print(f"H4 (panel closed):                           {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")
    if token == "BAND_GRAMMAR_HOLDS":
        print(
            "reading: BAND_GRAMMAR_HOLDS — at n=7 the omit cycle-type discriminant "
            "keeps class-pure discrete Φ bands (no singleton return, no continuum, "
            "no purity break); n=5→n=6 singleton→band shift stabilizes (V2 #42)"
        )
    elif token == "MORPHS_AGAIN":
        print(
            "reading: MORPHS_AGAIN — n=7 changes the omit cycle-type grammar again "
            "beyond the n=6 band form (singleton return / continuum / other)"
        )
    elif token == "PURITY_BREAKS_N7":
        print(
            "reading: PURITY_BREAKS_N7 — within-class Φ mixing appears at n=7 "
            "(scale blur that #42 ruled out at n=5/6)"
        )
    else:
        print(f"reading: {token}")

    # summary csv
    summary = {
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "verdict": token,
        "n7_phi_set": ";".join(str(p) for p in unique_phi),
        "n7_n_classes": n_cls,
        "n7_multi_class_bands": multi_class_bands,
        "n6_phi_set": ";".join(str(p) for p in n6_phis),
        "n6_pure": str(n6_pure),
    }
    sp = os.path.join(RESULTS, "summary.csv")
    with open(sp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)
    print(f"wrote {path}")
    print(f"wrote {sp}")


if __name__ == "__main__":
    main()
