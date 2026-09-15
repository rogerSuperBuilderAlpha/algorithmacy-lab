"""Finer grain on MIX indeg (0,0,1,1,2,2): t_targets discriminant.

Hypotheses fixed in hypotheses.md. Extends indeg_002122_n6 MIX.

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
# (cycles, recip, t_targets) -> N_U
SAMPLE_PLAN = [
    (((2, 2), 2), (1, 1), 3),   # expect Φ=12
    (((2, 2), 2), (2, 2), 2),   # expect Φ=6
    (((4,), 0), (1, 1), 3),     # expect Φ=12
    (((4,), 0), (1, 2), 2),     # expect Φ=6
    (((2,), 1), (1, 1), 3),     # H2: extend?
    (((2,), 1), (2, 2), 1),     # control Φ=6
    (((3,), 0), (1, 2), 2),     # H3 flat
]


def is_derangement(om):
    vals = [om[i] for i in range(N)]
    return sorted(vals) == list(range(N))


def t_targets_of(om):
    vals = [om[i] for i in range(N)]
    indeg = Counter(vals)
    t = sorted(i for i in range(N) if indeg[i] == 2)
    return tuple(sorted(indeg[om[i]] for i in t))


def enumerate_pool():
    """Map (cyc, recip, t_targets) -> list of omit dicts."""
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
        key = (feats[1], feats[2], t_targets_of(om))
        by[key].append(om)
    return by


def om_key(om):
    return tuple(om[i] for i in range(N))


def sample(oms, n_want, rng):
    if len(oms) <= n_want:
        return list(oms)
    idxs = rng.choice(len(oms), size=n_want, replace=False)
    return [oms[int(i)] for i in idxs]


def main():
    print("INDEG (0,0,1,1,2,2) FINER GRAIN — t_targets")
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

    print("SUBTYPE CATALOG (t_targets)")
    print("-" * 80)
    pool = enumerate_pool()
    for key in sorted(pool):
        print(f"  cyc={key[0]} recip={key[1]} t_targets={key[2]}  n={len(pool[key])}")
    print()

    labels = tuple(f"N{i}" for i in range(N))
    rows = []
    t_all = time.time()
    rng = np.random.default_rng(BASE_SEED + 221)
    subtype_phis = {}

    print("UNIFORMITY BY SUBTYPE")
    print("-" * 80)
    for (cyc_recip, tt, n_want) in SAMPLE_PLAN:
        cyc, recip = cyc_recip
        key = (cyc, recip, tt)
        oms = pool[key]
        samp = sample(oms, n_want, rng)
        phis = []
        cores = []
        for i, om in enumerate(samp):
            assert t_targets_of(om) == tt
            r = eval_one(ins_from_omit(om), N, labels)
            r.update({
                "family": "grain",
                "name": f"cyc{cyc}_r{recip}_tt{tt}_{i}",
                "omit": fmt_omit(om),
                "cycles": str(cyc),
                "recip": recip,
                "t_targets": str(tt),
            })
            rows.append(r)
            phis.append(r["core_phi"])
            cores.append(r["n_core"])
            print(
                f"  cyc={cyc} r={recip} tt={tt} [{i}]  "
                f"Φ={r['core_phi']:.1f}  n_core={r['n_core']}"
            )
        subtype_phis[key] = (phis, cores)
        hist = Counter(round(p, 3) for p in phis)
        print(f"    → hist={dict(hist)} pure={len(hist)==1}  "
              f"n_cores={Counter(cores)}")
    print()

    # ---- Hypotheses ----
    def all_phi(key, expect, ncore_expect):
        phis, cores = subtype_phis[key]
        return (
            all(abs(p - expect) < PHI_EPS for p in phis)
            and all(c == ncore_expect for c in cores)
        )

    # H1
    h1_keys_12 = [(((2, 2), 2), (1, 1)), (((4,), 0), (1, 1))]
    h1_keys_6 = [(((2, 2), 2), (2, 2)), (((4,), 0), (1, 2))]
    h1 = all(
        all_phi((cyc, recip, tt), 12.0, 4)
        for (cyc, recip), tt in h1_keys_12
    ) and all(
        all_phi((cyc, recip, tt), 6.0, 6)
        for (cyc, recip), tt in h1_keys_6
    )

    # H2
    h2 = all_phi(((2,), 1, (1, 1)), 12.0, 4)

    # H3
    h3 = all_phi(((3,), 0, (1, 2)), 6.0, 6)

    # H4: all tested subtypes pure
    h4 = h1 and all(
        len(Counter(round(p, 3) for p in subtype_phis[k][0])) == 1
        for k in subtype_phis
    )

    if h1 and h4 and h3:
        if h2:
            verdict_word = "T_TARGETS_LAW"
            reading = (
                "T_TARGETS_LAW — within indeg (0,0,1,1,2,2), Φ=12 iff "
                "t_targets=(1,1) (hubs omit only singles); else Φ=6; "
                "extends to cycle (2,); MIX dissolved"
            )
        else:
            verdict_word = "T_TARGETS_RESTRICTED"
            reading = (
                "T_TARGETS_RESTRICTED — t_targets=(1,1)⇒Φ=12 on mixed classes "
                "(2,2)/(4,); does not extend to (2,); MIX dissolved there"
            )
    elif not h1:
        verdict_word = "IRREDUCIBLE_MIX"
        reading = (
            "IRREDUCIBLE_MIX — t_targets does not purify; mix remains"
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
    print(f"  H3 ((3,) stays Φ=6):                    "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (pure discriminant / MIX dissolved): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  discriminant: t_targets=(1,1) → Φ=12 n_core=4; else Φ=6 full-core "
          f"(within indeg (0,0,1,1,2,2))")
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
            "family", "name", "omit", "cycles", "recip", "t_targets",
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
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
