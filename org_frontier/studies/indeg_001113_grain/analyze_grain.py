"""Role-target grain on indeg (0,0,1,1,1,3).

z_targets dissolves (2,) mix; t_targets constant. Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/indeg_001113_grain/analyze_grain.py
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
from org_frontier.studies.omit_lift_n6.analyze_lift import fmt_omit, ins_from_omit, omit_feats
from org_frontier.studies.random_coupling_ensemble.analyze_ensemble import eval_one

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

N = 6
TARGET = (0, 0, 1, 1, 1, 3)
BASE_SEED = 20260916

# (cycles, recip, z_targets, n_want, expect_phi, expect_ncore)
SAMPLE_PLAN = [
    (((2,), 1), (1, 1), 3, 6.0, 3),
    (((2,), 1), (1, 3), 3, 12.0, 4),
    (((3,), 0), (1, 3), 3, 6.0, 3),
    (((2, 2), 2), (3, 3), 2, 12.0, 4),
    (((4,), 0), (3, 3), 2, 12.0, 4),
]


def is_derangement(om):
    return sorted(om[i] for i in range(N)) == list(range(N))


def indeg_of(om):
    return Counter(om[i] for i in range(N))


def t_targets_of(om):
    indeg = indeg_of(om)
    t = sorted(i for i in range(N) if indeg[i] == 3)
    return tuple(sorted(indeg[om[i]] for i in t))


def z_targets_of(om):
    indeg = indeg_of(om)
    z = sorted(i for i in range(N) if indeg[i] == 0)
    return tuple(sorted(indeg[om[i]] for i in z))


def enumerate_pool():
    by = defaultdict(list)
    tt_set = set()
    for choices in itertools.product(
        *[[j for j in range(N) if j != i] for i in range(N)]
    ):
        om = {i: choices[i] for i in range(N)}
        if is_derangement(om):
            continue
        feats = omit_feats(om)
        if feats[0] != TARGET:
            continue
        tt = t_targets_of(om)
        zt = z_targets_of(om)
        tt_set.add(tt)
        key = (feats[1], feats[2], zt)
        by[key].append(om)
    return by, tt_set


def sample(oms, n_want, rng):
    if len(oms) <= n_want:
        return list(oms)
    idxs = rng.choice(len(oms), size=n_want, replace=False)
    return [oms[int(i)] for i in idxs]


def main():
    print("INDEG (0,0,1,1,1,3) ROLE-TARGET GRAIN — z_targets")
    print("=" * 80)
    print("  cited: indeg_002122_grain ROLE_TARGETS_LAW; same_indeg_band_n6")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  target indeg: {TARGET}")
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

    pool, tt_set = enumerate_pool()
    print("SUBTYPE CATALOG")
    print("-" * 80)
    print(f"  t_targets values observed: {sorted(tt_set)}")
    for key in sorted(pool):
        print(f"  cyc={key[0]} recip={key[1]} z_targets={key[2]}  n={len(pool[key])}")
    print()

    labels = tuple(f"N{i}" for i in range(N))
    rows = []
    t_all = time.time()
    rng = np.random.default_rng(BASE_SEED + 113)
    results = {}

    print("UNIFORMITY BY SUBTYPE")
    print("-" * 80)
    for (cyc_recip, zt, n_want, exp_phi, exp_nc) in SAMPLE_PLAN:
        cyc, recip = cyc_recip
        key = (cyc, recip, zt)
        oms = pool[key]
        samp = sample(oms, n_want, rng)
        phis = []
        cores = []
        for i, om in enumerate(samp):
            assert z_targets_of(om) == zt
            assert t_targets_of(om) == (1,)
            r = eval_one(ins_from_omit(om), N, labels)
            r.update({
                "family": "grain",
                "name": f"cyc{cyc}_r{recip}_zt{zt}_{i}",
                "omit": fmt_omit(om),
                "cycles": str(cyc),
                "recip": recip,
                "t_targets": str(t_targets_of(om)),
                "z_targets": str(zt),
            })
            rows.append(r)
            phis.append(r["core_phi"])
            cores.append(r["n_core"])
            print(
                f"  cyc={cyc} r={recip} zt={zt} [{i}]  "
                f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}"
            )
        results[key] = (phis, cores, exp_phi, exp_nc)
        hist = Counter(round(p, 3) for p in phis)
        match = (
            all(abs(p - exp_phi) < PHI_EPS for p in phis)
            and all(c == exp_nc for c in cores)
        )
        print(
            f"    → hist={dict(hist)} pure={len(hist) == 1}  "
            f"expect Φ={exp_phi} n_core={exp_nc} match={match}"
        )
    print()

    def ok(key):
        phis, cores, exp_phi, exp_nc = results[key]
        return (
            all(abs(p - exp_phi) < PHI_EPS for p in phis)
            and all(c == exp_nc for c in cores)
            and len(Counter(round(p, 3) for p in phis)) == 1
        )

    h1 = ok(((2,), 1, (1, 1))) and ok(((2,), 1, (1, 3)))
    h2 = ok(((3,), 0, (1, 3)))
    h3 = ok(((2, 2), 2, (3, 3))) and ok(((4,), 0, (3, 3)))
    h4 = h1 and h2 and h3
    # H5: t_targets constant; z_targets is the grain
    h5 = ctrl and tt_set == {(1,)} and h1

    if h1 and h2 and h3 and h4 and h5:
        verdict_word = "Z_TARGETS_LAW"
        reading = (
            "Z_TARGETS_LAW — on indeg (0,0,1,1,1,3): z_targets=(1,1)→Φ=6 "
            "(n_core=3); cycles=(3,)→Φ=6; else Φ=12 (n_core=4); "
            "t_targets constant; ROLE_TARGETS grain generalizes via zeros"
        )
    elif h1 and h4:
        verdict_word = "PARTIAL_GRAIN"
        reading = "PARTIAL_GRAIN — (2,) split works; other classes incomplete"
    else:
        verdict_word = "MIX_PERSISTS"
        reading = "MIX_PERSISTS — role-target grain does not purify this indeg"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  t_targets values: {sorted(tt_set)}")
    print(f"  H1 (z_targets dissolves (2,) mix):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 ((3,) stays Φ=6):                   "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 ((2,2)/(4,) stay Φ=12):             "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (all subtypes pure / MIX dissolved): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (grain generalizes via z_targets):  "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
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
            "family", "name", "omit", "cycles", "recip", "t_targets",
            "z_targets", "structure", "whole_phi_mip", "core", "core_phi",
            "n_core",
        ]
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            core = r.get("core", ())
            if isinstance(core, tuple):
                core_s = "|".join(core)
            else:
                core_s = str(core)
            w.writerow({
                "family": r.get("family", ""),
                "name": r.get("name", ""),
                "omit": r.get("omit", ""),
                "cycles": r.get("cycles", ""),
                "recip": r.get("recip", ""),
                "t_targets": r.get("t_targets", ""),
                "z_targets": r.get("z_targets", ""),
                "structure": r.get("structure", ""),
                "whole_phi_mip": f"{r.get('whole_phi_mip', float('nan')):.6f}",
                "core": core_s,
                "core_phi": f"{r.get('core_phi', float('nan')):.6f}",
                "n_core": r.get("n_core", ""),
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "verdict": verdict_word,
            "t_targets_values": "|".join(str(t) for t in sorted(tt_set)),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
