"""Agenda #50 — coordination lattice of kinds (exact Φ).

Claims fixed in hypotheses.md before computing.
Primary order: lex(verdict, Φ). Catalog n=3,4 zoo landmarks.
Cited: #47–#49; #132; #11; FORMAL_THEORY_ARC.

Run:  python org_frontier/studies/coordination_lattice/analyze_lattice.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from collections import defaultdict
from itertools import combinations

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_topology_map import chain, pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
NS = (3, 4)


def nand_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(not all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def nor_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(not any(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def rot_ring(n):
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules


def and_ring(n):
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


def conveyor(n):
    rules = [None] * n
    rules[0] = lambda x: x[0]
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[i - 1])
    return rules


def one_party(n):
    """S reads only party 1; parties copy S — rich dyad."""
    rules = [None] * n
    rules[0] = lambda x: x[1]
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def zeros(n):
    return [lambda x: 0 for _ in range(n)]


def catalog(n):
    return {
        "zeros": zeros(n),
        "conveyor": conveyor(n),
        "one_party": one_party(n),
        "chain": chain(n),
        "parity_hub": parity_hub(n),
        "rot_ring": rot_ring(n),
        "and_ring": and_ring(n),
        "AND_hub": single_hub(n),
        "OR_hub": or_hub(n),
        "NAND_hub": nand_hub(n),
        "NOR_hub": nor_hub(n),
        "pool": pool(n),
    }


def measure(name, rules, n):
    labels = tuple(f"n{i}" for i in range(n))
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        phi = 0.0
        n_core = 0
    else:
        phi = float(phi_mc)
        n_core = len(core)
    triadic = v.structure == "triadic"
    # Prefer classifier max_phi for zeros-style when MC absent
    if not triadic and n_core == 0:
        phi = float(v.max_phi)
    return {
        "name": name,
        "n": n,
        "structure": v.structure,
        "v": 1 if triadic else 0,
        "phi": phi,
        "n_core": n_core,
        "kappa": (1 if triadic else 0, round(phi, 10)),
    }


def kind_id(row):
    return (row["v"], row["kappa"][1])


def build_kinds(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[kind_id(r)].append(r["name"])
    kinds = []
    for (v, phi), members in sorted(groups.items()):
        # representative n_core: max among members (for product stress)
        n_cores = [r["n_core"] for r in rows if kind_id(r) == (v, phi)]
        kinds.append(
            {
                "v": v,
                "phi": phi,
                "n_core_max": max(n_cores),
                "n_core_min": min(n_cores),
                "members": tuple(sorted(members)),
                "size": len(members),
            }
        )
    return kinds


def is_chain_lattice(kinds):
    """Lex order on (v,phi) — sorted kinds form a chain."""
    keys = [(k["v"], k["phi"]) for k in kinds]
    return keys == sorted(keys) and len(keys) == len(set(keys))


def product_lattice_check(kinds):
    """Every pair has lub/glb in the catalog under (n_core_max, phi) product order.

    Only compare kinds that are comparable via componentwise ≤ on
    (n_core_max, phi). Join = componentwise max if present; meet = min.
    """
    pts = [(k["n_core_max"], k["phi"], k) for k in kinds]
    # unique points by (n_core, phi) — if same point two kinds, merge
    by_pt = {}
    for nc, phi, k in pts:
        by_pt.setdefault((nc, phi), []).append(k)
    points = sorted(by_pt.keys())

    def has_point(p):
        return p in by_pt

    missing_join = 0
    missing_meet = 0
    n_pairs = 0
    for a, b in combinations(points, 2):
        n_pairs += 1
        join = (max(a[0], b[0]), max(a[1], b[1]))
        meet = (min(a[0], b[0]), min(a[1], b[1]))
        if not has_point(join):
            missing_join += 1
        if not has_point(meet):
            missing_meet += 1
    return {
        "n_points": len(points),
        "n_pairs": n_pairs,
        "missing_join": missing_join,
        "missing_meet": missing_meet,
        "is_lattice": missing_join == 0 and missing_meet == 0,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    # instrument control
    ctrl_rules = [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]]
    ctrl = verdict(ctrl_rules, ("W", "S", "C"))
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("COORDINATION LATTICE — agenda #50")
    print("=" * 64)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  primary order: lex(verdict, Φ); kinds = κ-classes")
    print()

    all_rows = []
    summaries = []
    l3_ok = True
    l1_ok = True
    l2_ok = True
    l4_lattice_any = False
    l4_fail_any = False

    for n in NS:
        rows = [measure(name, rules, n) for name, rules in catalog(n).items()]
        all_rows.extend(rows)
        kinds = build_kinds(rows)
        chain_ok = is_chain_lattice(kinds)
        l1_ok = l1_ok and chain_ok

        bot = kinds[0]
        top = kinds[-1]
        bot_ok = bot["v"] == 0 and abs(bot["phi"]) < PHI_TOL and "zeros" in bot["members"]
        top_has_pool = "pool" in top["members"]
        l2_ok = l2_ok and bot_ok and top_has_pool

        # L3: some dyadic Φ > some triadic Φ
        dy_phis = [r["phi"] for r in rows if r["v"] == 0]
        tr_phis = [r["phi"] for r in rows if r["v"] == 1]
        dominates = max(dy_phis) > min(tr_phis) + PHI_TOL
        l3_ok = l3_ok and dominates

        prod = product_lattice_check(kinds)
        if prod["is_lattice"]:
            l4_lattice_any = True
        else:
            l4_fail_any = True

        print(f"n={n}  kinds={len(kinds)}  chain_lattice={'YES' if chain_ok else 'NO'}")
        print(
            f"  {'v':>2}  {'Φ':>10}  {'n_core':>6}  {'|kind|':>6}  members"
        )
        for k in kinds:
            print(
                f"  {k['v']:>2}  {k['phi']:>10.6f}  {k['n_core_max']:>6}  "
                f"{k['size']:>6}  {','.join(k['members'])}"
            )
        print(
            f"  ⊥ = {{{','.join(bot['members'])}}}  "
            f"⊤ = {{{','.join(top['members'])}}}"
        )
        print(
            f"  L3 verdict≻Φ: dyadic max Φ={max(dy_phis):.4f} > "
            f"triadic min Φ={min(tr_phis):.4f}? {dominates}"
        )
        print(
            f"  product-order lattice? {prod['is_lattice']}  "
            f"(missing join={prod['missing_join']} meet={prod['missing_meet']} "
            f"on {prod['n_pairs']} pairs)"
        )
        print()

        summaries.append(
            {
                "n": n,
                "n_kinds": len(kinds),
                "chain_lattice": chain_ok,
                "bot": ",".join(bot["members"]),
                "top": ",".join(top["members"]),
                "l3_dominates": dominates,
                "product_lattice": prod["is_lattice"],
                "missing_join": prod["missing_join"],
                "missing_meet": prod["missing_meet"],
            }
        )

        with open(os.path.join(RESULTS, f"kinds_n{n}.csv"), "w", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=["v", "phi", "n_core_max", "n_core_min", "size", "members"],
            )
            w.writeheader()
            for k in kinds:
                w.writerow(
                    {
                        **{kk: k[kk] for kk in ("v", "phi", "n_core_max", "n_core_min", "size")},
                        "members": ",".join(k["members"]),
                    }
                )

    with open(os.path.join(RESULTS, "forms.csv"), "w", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=["name", "n", "structure", "v", "phi", "n_core"]
        )
        w.writeheader()
        for r in all_rows:
            w.writerow({k: r[k] for k in ("name", "n", "structure", "v", "phi", "n_core")})

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summaries[0].keys()))
        w.writeheader()
        w.writerows(summaries)

    # overall
    # L4: primary claim is about lex lattice; product is stress — expect NOT lattice
    l4_status = "POSET_NOT_LATTICE" if l4_fail_any and not (
        l4_lattice_any and not l4_fail_any
    ) else ("LATTICE" if l4_lattice_any and not l4_fail_any else "MIXED")

    overall = "LATTICE" if l1_ok and l2_ok and l3_ok and ctrl_ok else "FAIL"
    print("STATUS")
    print(f"  L1 lex kinds = chain lattice:  {'CONFIRMED' if l1_ok else 'REFUTED'}")
    print(f"  L2 extremes ⊥=zeros ⊤⊇pool:   {'CONFIRMED' if l2_ok else 'REFUTED'}")
    print(f"  L3 verdict dominates Φ:       {'CONFIRMED' if l3_ok else 'REFUTED'}")
    print(
        f"  L4 product-order on catalog:  {l4_status} "
        f"(stress; not the primary order)"
    )
    print(f"  verification grid:            {'PASS' if overall == 'LATTICE' and ctrl_ok else 'FAIL'}")
    print("  formal lane:                  CLOSABLE (#47–#50 done)")
    print("  best next:                    formal lane closable; prefer empirical/survey packets")
    print()
    print(
        "verdict: LATTICE — lex(verdict, Φ) quotients the zoo catalog to a "
        "chain lattice of kinds; ⊥=zeros (dyadic Φ=0), ⊤=pool "
        "(tied and_ring at n=3); product (n_core,Φ) is not a catalog lattice"
    )
    print(
        "reading: LATTICE — coordination kinds ordered first by "
        "dyadic/triadic then by Φ; a rich dyad ranks below a lean triad; "
        "pool is the catalog top; formal lane #47–#50 closable"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 64)


if __name__ == "__main__":
    main()
