"""Finer grain on MIX indeg (0,0,1,1,2,2): role-target discriminants.

t_targets=(1,1) → Φ=12; within (3,), z_targets splits Φ=8 vs 6.
Hypotheses fixed in hypotheses.md (H5 fixed after H3 fail, before confirm).

Run:  python org_frontier/studies/indeg_002122_grain/analyze_grain.py
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
TARGET = (0, 0, 1, 1, 2, 2)
BASE_SEED = 20260915

# (cycles, recip, t_targets, z_targets|None, n_want, expect_phi, expect_ncore)
SAMPLE_PLAN = [
    (((2, 2), 2), (1, 1), None, 3, 12.0, 4),
    (((2, 2), 2), (2, 2), None, 2, 6.0, 6),
    (((4,), 0), (1, 1), None, 3, 12.0, 4),
    (((4,), 0), (1, 2), None, 2, 6.0, 6),
    (((2,), 1), (1, 1), None, 3, 12.0, 4),
    (((2,), 1), (2, 2), None, 1, 6.0, 6),
    (((3,), 0), (1, 2), (2, 2), 3, 8.0, 5),  # H5
    (((3,), 0), (1, 2), (1, 2), 3, 6.0, 6),  # H5
]


def is_derangement(om):
    vals = [om[i] for i in range(N)]
    return sorted(vals) == list(range(N))


def indeg_of(om):
    return Counter(om[i] for i in range(N))


def t_targets_of(om):
    indeg = indeg_of(om)
    t = sorted(i for i in range(N) if indeg[i] == 2)
    return tuple(sorted(indeg[om[i]] for i in t))


def z_targets_of(om):
    indeg = indeg_of(om)
    z = sorted(i for i in range(N) if indeg[i] == 0)
    return tuple(sorted(indeg[om[i]] for i in z))


def enumerate_pool():
    by = defaultdict(list)
    for choices in itertools.product(
        *[[j for j in range(N) if j != i] for i in range(N)]
    ):
        om = {i: choices[i] for i in range(N)}
        if is_derangement(om):
            continue
        feats = omit_feats(om)
        if feats[0] != TARGET:
            continue
        key = (feats[1], feats[2], t_targets_of(om), z_targets_of(om))
        by[key].append(om)
    return by


def sample(oms, n_want, rng):
    if len(oms) <= n_want:
        return list(oms)
    idxs = rng.choice(len(oms), size=n_want, replace=False)
    return [oms[int(i)] for i in idxs]


def main():
    print("INDEG (0,0,1,1,2,2) FINER GRAIN — role targets")
    print("=" * 80)
    print("  cited: indeg_002122_n6 MIX; OMIT_ATOM_ARC")
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

    pool = enumerate_pool()
    print("SUBTYPE CATALOG")
    print("-" * 80)
    # aggregate by (cyc,recip,tt) and by (cyc,recip,tt,zt)
    agg = defaultdict(int)
    for (cyc, recip, tt, zt), oms in pool.items():
        agg[(cyc, recip, tt)] += len(oms)
    for key in sorted(agg):
        print(f"  cyc={key[0]} recip={key[1]} t_targets={key[2]}  n={agg[key]}")
    print()

    labels = tuple(f"N{i}" for i in range(N))
    rows = []
    t_all = time.time()
    rng = np.random.default_rng(BASE_SEED + 221)
    results = {}

    print("UNIFORMITY BY SUBTYPE")
    print("-" * 80)
    for (cyc_recip, tt, zt, n_want, exp_phi, exp_nc) in SAMPLE_PLAN:
        cyc, recip = cyc_recip
        if zt is None:
            oms = []
            for (c, r, t, z), v in pool.items():
                if (c, r, t) == (cyc, recip, tt):
                    oms.extend(v)
        else:
            oms = pool[(cyc, recip, tt, zt)]
        samp = sample(oms, n_want, rng)
        phis = []
        cores = []
        for i, om in enumerate(samp):
            assert t_targets_of(om) == tt
            if zt is not None:
                assert z_targets_of(om) == zt
            r = eval_one(ins_from_omit(om), N, labels)
            r.update({
                "family": "grain",
                "name": f"cyc{cyc}_r{recip}_tt{tt}_zt{zt}_{i}",
                "omit": fmt_omit(om),
                "cycles": str(cyc),
                "recip": recip,
                "t_targets": str(tt),
                "z_targets": str(zt) if zt else "",
            })
            rows.append(r)
            phis.append(r["core_phi"])
            cores.append(r["n_core"])
            print(
                f"  cyc={cyc} r={recip} tt={tt} zt={zt} [{i}]  "
                f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}"
            )
        key = (cyc, recip, tt, zt)
        results[key] = (phis, cores, exp_phi, exp_nc)
        hist = Counter(round(p, 3) for p in phis)
        match = (
            all(abs(p - exp_phi) < PHI_EPS for p in phis)
            and all(c == exp_nc for c in cores)
        )
        print(f"    → hist={dict(hist)} pure={len(hist)==1}  "
              f"expect Φ={exp_phi} n_core={exp_nc} match={match}")
    print()

    def ok(key):
        phis, cores, exp_phi, exp_nc = results[key]
        return (
            all(abs(p - exp_phi) < PHI_EPS for p in phis)
            and all(c == exp_nc for c in cores)
            and len(Counter(round(p, 3) for p in phis)) == 1
        )

    h1 = (
        ok(((2, 2), 2, (1, 1), None))
        and ok(((2, 2), 2, (2, 2), None))
        and ok(((4,), 0, (1, 1), None))
        and ok(((4,), 0, (1, 2), None))
    )
    h2 = ok(((2,), 1, (1, 1), None))
    # H3 original: (3,) flat Φ=6 — expect REFUTED; check both zt subtypes not both 6
    h3 = (
        ok(((3,), 0, (1, 2), (1, 2)))
        and ok(((3,), 0, (1, 2), (2, 2)))
        and abs(results[((3,), 0, (1, 2), (2, 2))][2] - 6.0) < PHI_EPS
    )
    # Actually H3 was "all Φ=6" — with zt=(2,2) expecting 8, h3 should be False
    h3 = False  # structural: we now know (3,) is not flat; H5 replaces
    # Recompute H3 as originally stated: both (3,) samples Φ=6
    phis_3 = (
        results[((3,), 0, (1, 2), (2, 2))][0]
        + results[((3,), 0, (1, 2), (1, 2))][0]
    )
    h3 = all(abs(p - 6.0) < PHI_EPS for p in phis_3)

    h5 = (
        ok(((3,), 0, (1, 2), (2, 2)))
        and ok(((3,), 0, (1, 2), (1, 2)))
    )
    h4 = h1 and h2 and h5 and all(ok(k) for k in results)

    if h1 and h2 and h5 and h4 and not h3:
        verdict_word = "ROLE_TARGETS_LAW"
        reading = (
            "ROLE_TARGETS_LAW — MIX dissolved: t_targets=(1,1)⇒Φ=12; "
            "within (3,), z_targets=(2,2)⇒Φ=8 else Φ=6; all subtypes pure"
        )
    elif h1 and h2 and not h5:
        verdict_word = "T_TARGETS_PARTIAL"
        reading = (
            "T_TARGETS_PARTIAL — t_targets=(1,1)⇒Φ=12 holds; (3,) residual unpurified"
        )
    else:
        verdict_word = "PARTIAL"
        reading = "PARTIAL — grain incomplete"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (tt=(1,1)⇒12 on (2,2)/(4,); else 6): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (law extends to cycle (2,)):         "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 ((3,) stays Φ=6 flat):               "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (all subtypes pure / MIX dissolved): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 ((3,) z_targets 8 vs 6):             "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  discriminant: t_targets=(1,1)→Φ=12; (3,)+z_targets=(2,2)→Φ=8; else Φ=6")
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
            "family", "name", "omit", "cycles", "recip", "t_targets", "z_targets",
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
                "t_targets": r["t_targets"],
                "z_targets": r.get("z_targets", ""),
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
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
