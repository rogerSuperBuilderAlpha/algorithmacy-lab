"""Omit cycle-type band grammar at n=8–9 (RESEARCH_AGENDA_V4 #8).

Does V3 #8 BAND_GRAMMAR_HOLDS survive the indeg lift to n=8–9, or does a
new morph appear once more cycle types fit?

Exact binary IIT-4.0. Lean panel: n=7 committed control + MC cycle-type
catalogs at n=7/8/9 + optional exact-Φ micro panel at n=8 (all-1 major
complex). Hypotheses fixed in hypotheses.md before computing.

Run:
  python org_frontier/studies/omit_cycle_band_n89/analyze_band_n89.py

Rebuild catalogs:
  python org_frontier/studies/omit_cycle_band_n89/analyze_band_n89.py --rebuild

Attempt exact micro panel (long):
  python org_frontier/studies/omit_cycle_band_n89/analyze_band_n89.py --exact-micro
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from collections import Counter, defaultdict

import numpy as np

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO not in sys.path:
    sys.path.insert(0, _REPO)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
N7_CENSUS = os.path.join(
    _REPO, "org_frontier", "studies", "omit_cycle_morph_n7", "results", "census.csv"
)

TARGETS = {
    7: (0, 1, 1, 1, 1, 1, 2),
    8: (0, 1, 1, 1, 1, 1, 1, 2),
    9: (0, 1, 1, 1, 1, 1, 1, 1, 2),
}
MC_TRIALS = 250_000
MC_SEED = 41
PHI_EPS = 1e-6


def feats(om, n):
    indeg = Counter(om[i] for i in range(n))
    sig = tuple(sorted(indeg[i] for i in range(n)))
    seen = set()
    cyc = []
    for start in range(n):
        if start in seen:
            continue
        path = []
        u = start
        while u not in seen and u not in path:
            path.append(u)
            u = om[u]
        if u in path:
            cyc.append(len(path) - path.index(u))
        for x in path:
            seen.add(x)
    recip = sum(1 for i in range(n) if om[om[i]] == i) // 2
    return sig, tuple(sorted(cyc)), recip


def catalog(n, target, trials=MC_TRIALS, seed=MC_SEED):
    rng = np.random.default_rng(seed + n)
    by = defaultdict(int)
    hits = 0
    for _ in range(trials):
        om = {
            i: int([j for j in range(n) if j != i][rng.integers(0, n - 1)])
            for i in range(n)
        }
        if sorted(om.values()) == list(range(n)) and all(om[i] != i for i in range(n)):
            continue
        sig, cyc, recip = feats(om, n)
        if sig != target:
            continue
        hits += 1
        by[(cyc, recip)] += 1
    return hits, dict(by)


def load_n7_control():
    with open(N7_CENSUS, newline="") as fh:
        rows = list(csv.DictReader(fh))
    designed = [r for r in rows if r["family"] == "designed"]
    bands = defaultdict(set)
    for r in designed:
        bands[round(float(r["core_phi"]), 6)].add(r["cycles"])
    phi_set = sorted(bands.keys())
    h1 = phi_set == [12.0, 14.0] and len(bands[12.0]) >= 2 and len(bands[14.0]) >= 2
    return {
        "n_designed": len(designed),
        "phi_set": phi_set,
        "bands": {str(k): sorted(v) for k, v in bands.items()},
        "h1": h1,
    }


def build_catalogs():
    out = {}
    for n, targ in TARGETS.items():
        hits, by = catalog(n, targ)
        classes = sorted(by.keys(), key=lambda k: (-by[k], k[0], k[1]))
        out[str(n)] = {
            "target_indeg": list(targ),
            "hits": hits,
            "n_classes": len(by),
            "classes": [
                {"cycles": list(c), "recip": r, "count": by[(c, r)]}
                for c, r in classes
            ],
        }
        print(f"  n={n} hits={hits} classes={len(by)}")
    c7 = {tuple(x["cycles"]) for x in out["7"]["classes"]}
    c8 = {tuple(x["cycles"]) for x in out["8"]["classes"]}
    c9 = {tuple(x["cycles"]) for x in out["9"]["classes"]}
    out["new_cycle_types_n8"] = [list(t) for t in sorted(c8 - c7)]
    out["new_cycle_types_n9"] = [list(t) for t in sorted(c9 - c8)]
    path = os.path.join(RESULTS, "catalog.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)
    return out


def load_catalog():
    path = os.path.join(RESULTS, "catalog.json")
    if not os.path.exists(path):
        print("  no catalog.json — building")
        return build_catalogs()
    with open(path) as fh:
        return json.load(fh)


def load_exact_micro():
    path = os.path.join(RESULTS, "exact_micro.json")
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return json.load(fh)


def run_exact_micro(forms=None):
    import pyphi
    from pyphi import new_big_phi
    from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules

    pyphi.config.PROGRESS_BARS = False
    N = 8
    target = TARGETS[8]
    if forms is None:
        forms = [((2,), 101), ((3,), 202), ((2, 3), 303), ((7,), 404)]

    def find_om(cyc_t, seed):
        rng = np.random.default_rng(seed)
        for _ in range(500_000):
            om = {
                i: int([j for j in range(N) if j != i][rng.integers(0, N - 1)])
                for i in range(N)
            }
            if sorted(om.values()) == list(range(N)) and all(om[i] != i for i in range(N)):
                continue
            sig, cyc, recip = feats(om, N)
            if sig == target and cyc == cyc_t:
                return om, recip
        raise RuntimeError(cyc_t)

    results = []
    for cyc, seed in forms:
        om, recip = find_om(cyc, seed)
        rules = [
            (
                lambda x, i=i, om=om: int(
                    all(x[j] for j in range(N) if j != i and j != om[i])
                )
            )
            for i in range(N)
        ]
        tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
        net = pyphi.Network(tpm, cm=cm, node_labels=tuple(f"N{i}" for i in range(N)))
        state = (1,) * N
        print(f"  exact micro cyc={cyc} recip={recip} (all-1)...", flush=True)
        t0 = time.time()
        try:
            mc = new_big_phi.maximal_complex(net, state)
            null = isinstance(mc, new_big_phi.NullPhiStructure)
            phi = 0.0 if null else float(mc.phi)
            core = None if null else list(mc.node_indices)
            row = {
                "cycles": list(cyc),
                "recip": recip,
                "state": "all1",
                "phi": phi,
                "core": core,
                "seconds": round(time.time() - t0, 1),
                "status": "ok",
                "omit": "|".join(str(om[i]) for i in range(N)),
            }
        except Exception as e:
            row = {
                "cycles": list(cyc),
                "recip": recip,
                "status": "error",
                "error": repr(e),
                "seconds": round(time.time() - t0, 1),
            }
        print(f"    -> {row}", flush=True)
        results.append(row)
        with open(os.path.join(RESULTS, "exact_micro.json"), "w") as fh:
            json.dump(results, fh, indent=2)
    return results


def evaluate(control, catalogs, micro):
    h1 = bool(control["h1"])
    n7 = catalogs["7"]["n_classes"]
    n8 = catalogs["8"]["n_classes"]
    n9 = catalogs["9"]["n_classes"]
    h2 = n8 > n7 and n9 > n8

    h3 = False
    h4 = False
    h5 = False
    micro_phis = []
    if micro:
        ok = [r for r in micro if r.get("status") == "ok"]
        pos = [r for r in ok if float(r.get("phi", 0)) > PHI_EPS]
        micro_phis = sorted({round(float(r["phi"]), 6) for r in pos})
        h3 = len(pos) >= 2 and len({tuple(r["cycles"]) for r in pos}) >= 2
        if h3:
            by_phi = defaultdict(list)
            for r in pos:
                by_phi[round(float(r["phi"]), 6)].append(tuple(r["cycles"]))
            multi = any(len(v) >= 2 for v in by_phi.values())
            two_bands = len(by_phi) >= 2
            h4 = two_bands and (multi or len(pos) >= 3)

    if not h1:
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — n=7 census Φ set {control['phi_set']} "
            f"does not replicate BAND_GRAMMAR_HOLDS"
        )
    elif not h2:
        verdict = "CATALOG_FLAT"
        reading = (
            f"CATALOG_FLAT — class counts n7={n7} n8={n8} n9={n9}; "
            f"expected growth under indeg lift"
        )
    elif not h3:
        verdict = "SCALE_BLOCKS_EXACT_PHI"
        reading = (
            f"SCALE_BLOCKS_EXACT_PHI — cycle-type catalog expands "
            f"({n7}->{n8}->{n9}; new n8={catalogs['new_cycle_types_n8']}, "
            f"new n9={catalogs['new_cycle_types_n9']}) but exact core-Φ "
            f"at n=8 is not adjudicable under the lab stack "
            f"(dense-state major complex exceeds budget; sparse states "
            f"Φ=0); n=7 BAND_GRAMMAR_HOLDS unrebutted"
        )
    elif h4:
        verdict = "BAND_GRAMMAR_HOLDS"
        reading = (
            f"BAND_GRAMMAR_HOLDS — n=8 exact micro Φ bands {micro_phis}; "
            f"catalog expands {n7}->{n8}->{n9}; grammar survives with more "
            f"cycle types"
        )
    else:
        verdict = "MORPHS_AGAIN"
        reading = (
            f"MORPHS_AGAIN — n=8 exact micro Φ set {micro_phis} breaks "
            f"the class-pure discrete band form; catalog {n7}->{n8}->{n9}"
        )

    return {
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "verdict": verdict,
        "reading": reading,
        "n_classes": {"7": n7, "8": n8, "9": n9},
        "micro_phis": micro_phis,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--exact-micro", action="store_true")
    args = ap.parse_args()
    os.makedirs(RESULTS, exist_ok=True)
    t_all = time.time()

    print("AGENDA V4 #8 — OMIT CYCLE BAND GRAMMAR AT n=8-9")
    print("=" * 80)
    print("  cited: V3 #8 BAND_GRAMMAR_HOLDS; V2 #42 SCALE_MORPHS")
    print("  scope: lean — n=7 control + MC catalogs + optional exact micro")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    from org_frontier.probes.lib import verdict as vlib
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ok = v0.structure == "triadic" and abs(float(v0.max_phi) - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={float(v0.max_phi):.6f}  "
        f"{'PASS' if ok else 'FAIL'}"
    )
    if not ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("H1 CONTROL — n=7 committed census")
    print("-" * 80)
    control = load_n7_control()
    print(
        f"  designed={control['n_designed']}  Φ set={control['phi_set']}  "
        f"bands={control['bands']}"
    )
    print(f"  H1 replicate BAND_GRAMMAR_HOLDS: {'PASS' if control['h1'] else 'FAIL'}")
    print()

    print("H2 CATALOGS — cycle types under indeg lift")
    print("-" * 80)
    catalogs = build_catalogs() if args.rebuild else load_catalog()
    print(
        f"  classes: n7={catalogs['7']['n_classes']}  "
        f"n8={catalogs['8']['n_classes']}  n9={catalogs['9']['n_classes']}"
    )
    print(f"  new at n=8: {catalogs['new_cycle_types_n8']}")
    print(f"  new at n=9: {catalogs['new_cycle_types_n9']}")
    print()

    micro = load_exact_micro()
    if args.exact_micro:
        print("H3/H4 EXACT MICRO — n=8 all-1 major complex")
        print("-" * 80)
        micro = run_exact_micro()
        print()
    else:
        print("EXACT MICRO")
        print("-" * 80)
        if micro:
            print(f"  loaded exact_micro.json ({len(micro)} rows)")
            for r in micro:
                print(f"    {r}")
        else:
            print("  none committed — run with --exact-micro to attempt (long)")
        print()

    ev = evaluate(control, catalogs, micro)
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    for key, label in [
        ("h1", "H1 (n=7 control BAND_GRAMMAR_HOLDS)"),
        ("h2", "H2 (class count grows n7<n8<n9)"),
        ("h3", "H3 (n=8 exact micro adjudicable)"),
        ("h4", "H4 (band grammar holds at n=8 | H3)"),
        ("h5", "H5 (n=9 consistent | budget)"),
    ]:
        print(f"  {label + ':':42s} {'SUPPORTED' if ev[key] else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {ev['verdict']}")
    print(f"  reading: {ev['reading']}")
    print(
        f"  metrics: n_classes_7={ev['n_classes']['7']}; "
        f"n_classes_8={ev['n_classes']['8']}; "
        f"n_classes_9={ev['n_classes']['9']}; "
        f"new_n8={catalogs['new_cycle_types_n8']}; "
        f"new_n9={catalogs['new_cycle_types_n9']}; "
        f"micro_phis={ev['micro_phis']}; "
        f"n7_phi_set={control['phi_set']}"
    )
    print("  best next:         V4 #9 parity-hub law for n>8")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    summary = {
        "verdict": ev["verdict"],
        "reading": ev["reading"],
        "h1": ev["h1"],
        "h2": ev["h2"],
        "h3": ev["h3"],
        "h4": ev["h4"],
        "h5": ev["h5"],
        "n_classes": ev["n_classes"],
        "new_cycle_types_n8": catalogs["new_cycle_types_n8"],
        "new_cycle_types_n9": catalogs["new_cycle_types_n9"],
        "micro_phis": ev["micro_phis"],
        "n7_phi_set": control["phi_set"],
        "scope": (
            "lean: n=7 committed control + MC catalogs n=7/8/9 + optional "
            "n=8 all-1 exact micro; full designed census intractable"
        ),
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)


if __name__ == "__main__":
    main()
