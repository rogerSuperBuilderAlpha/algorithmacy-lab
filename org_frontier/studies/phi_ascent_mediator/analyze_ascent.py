"""Agenda #14 — Φ-ascent adaptive mediator (vs #79 drop-a-party).

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #79; zoo #104/#116/#132; STOCH_TEMPORAL_ARC pointer.
Estimation / construct / omit / ladder closed.

Run:  python org_frontier/studies/phi_ascent_mediator/analyze_ascent.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, PHI_EPS
from org_frontier.probes.lib import verdict as vlib
from org_frontier.probes.probe_adaptive import build as build79, max_phi_float
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_parity_scaling import parity_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

LABELS3 = ("W", "S", "C")


def and_mask():
    table = []
    for s in range(8):
        w, _s, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        table.append(w & c)
    return sum(table[i] << i for i in range(8))


def or_mask():
    table = []
    for s in range(8):
        w, _s, c = s & 1, (s >> 1) & 1, (s >> 2) & 1
        table.append(w | c)
    return sum(table[i] << i for i in range(8))


def rules_from_mask(mask: int):
    table = [(mask >> i) & 1 for i in range(8)]

    def Sp(x, table=table):
        s = x[0] + 2 * x[1] + 4 * x[2]
        return int(table[s])

    return [lambda x: x[1], Sp, lambda x: x[1]]


def cache_panel_a():
    """Φ and structure for all 256 S' masks."""
    phis = []
    structs = []
    for mask in range(256):
        v = classify_rules(rules_from_mask(mask), labels=LABELS3)
        phis.append(float(v.max_phi))
        structs.append(v.structure)
    return phis, structs


def hillclimb_mask(start: int, phis: list[float]) -> int:
    cur = start
    seen = set()
    while cur not in seen:
        seen.add(cur)
        best = cur
        best_phi = phis[cur]
        for b in range(8):
            nxt = cur ^ (1 << b)
            if phis[nxt] > best_phi + 1e-12:
                best_phi = phis[nxt]
                best = nxt
        if best == cur:
            return cur
        cur = best
    return cur


def topology_catalog(n: int):
    builders = {
        "chain": chain,
        "conjunctive_hub": single_hub,
        "two_hub": two_hub,
        "pool": pool,
        "ring": ring,
        "parity_hub": parity_hub,
    }
    labels = tuple(f"N{i}" for i in range(n))
    out = {}
    for name, build in builders.items():
        rules = build(n)
        v = classify_rules(rules, labels=labels)
        out[name] = {
            "phi": float(v.max_phi),
            "structure": v.structure,
            "rules": rules,
            "labels": labels,
        }
    return out


def hillclimb_topo(start: str, catalog: dict) -> str:
    cur = start
    seen = set()
    while cur not in seen:
        seen.add(cur)
        best = cur
        best_phi = catalog[cur]["phi"]
        for name, spec in catalog.items():
            if spec["phi"] > best_phi + 1e-12:
                best_phi = spec["phi"]
                best = name
        if best == cur:
            return cur
        cur = best
    return cur


def main():
    print("AGENDA #14 — Φ-ASCENT ADAPTIVE MEDIATOR (vs #79 drop-a-party)")
    print("=" * 80)
    print("  cited: #79; zoo #104/#116/#132; STOCH_TEMPORAL_ARC pointer")
    print("  Panel A: n=3 S' truth-table hill-climb (parties W'=C'=S)")
    print("  Panel B: n=3,4 topology-catalog hill-climb (incl. pool)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    t_all = time.time()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        LABELS3,
    )
    ctrl_faithful = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl_faithful else 'FAIL'}"
    )

    # #79 contrast
    print()
    print("PROBE #79 CONTRAST (drop-a-party reliability path)")
    print("-" * 80)
    print(f"  {'epoch':>5}  {'r':>6}  {'Φ':>10}  verdict")
    path79 = []
    for e, rc in enumerate([1.0, 0.75, 0.5, 0.25, 0.0]):
        phi, _ = max_phi_float(build79(rc))
        verdict = "triadic" if phi > PHI_EPS else "dyadic"
        path79.append({"epoch": e, "r": rc, "phi": float(phi), "structure": verdict})
        print(f"  {e:>5}  {rc:>6.2f}  {phi:>10.4f}  {verdict}")
    ctrl_79 = (
        abs(path79[0]["phi"] - 2.0) < 1e-3
        and path79[0]["structure"] == "triadic"
        and path79[-1]["phi"] < PHI_EPS
        and path79[-1]["structure"] == "dyadic"
    )
    print(f"  #79 Φ falls 2→0, flips at r=0: {'PASS' if ctrl_79 else 'FAIL'}")

    # Panel A
    print()
    print("PANEL A — mechanism ascent (256 S' masks, n=3)")
    print("-" * 80)
    t_a = time.time()
    phis, structs = cache_panel_a()
    phi_star = max(phis)
    maximizers = [m for m, p in enumerate(phis) if abs(p - phi_star) < 1e-9]
    AND = and_mask()
    OR = or_mask()
    print(f"  Φ*={phi_star:.6f}  n_maximizers={len(maximizers)}  "
          f"AND_mask={AND} in_max={AND in maximizers}  "
          f"OR_mask={OR} in_max={OR in maximizers}")

    terminals = {}
    term_rows = []
    for start in range(256):
        term = hillclimb_mask(start, phis)
        terminals[term] = terminals.get(term, 0) + 1
        term_rows.append({
            "start": start,
            "terminal": term,
            "phi_start": phis[start],
            "phi_term": phis[term],
            "struct_term": structs[term],
            "is_and": int(term == AND),
            "is_or": int(term == OR),
            "is_maximizer": int(term in maximizers),
        })
    n_to_and = terminals.get(AND, 0)
    n_to_or = terminals.get(OR, 0)
    n_to_max = sum(terminals.get(m, 0) for m in maximizers)
    print(f"  terminals: n_distinct={len(terminals)}  "
          f"to_AND={n_to_and}/256 ({n_to_and/256:.1%})  "
          f"to_OR={n_to_or}/256 ({n_to_or/256:.1%})  "
          f"to_any_max={n_to_max}/256")
    top = sorted(terminals.items(), key=lambda kv: -kv[1])[:8]
    print("  top terminals:")
    for m, c in top:
        print(f"    mask={m:<3} count={c:<3} Φ={phis[m]:.4f} "
              f"{'AND' if m==AND else 'OR' if m==OR else 'other'}")
    print(f"  panel A elapsed={round(time.time()-t_a,1)}s")

    h1_panel_a = (n_to_and / 256) > 0.5
    h3_panel_a = len(maximizers) > 1 and not h1_panel_a and (n_to_or / 256) <= 0.5

    # Panel B
    print()
    print("PANEL B — topology ascent (catalog, n=3 and n=4)")
    print("-" * 80)
    topo_rows = []
    traj_rows = []
    h2_ok = True
    h1_panel_b = False
    for n in (3, 4):
        cat = topology_catalog(n)
        print(f"  n={n} catalog Φ:")
        for name, spec in cat.items():
            print(f"    {name:<16} {spec['structure']:<8} Φ={spec['phi']:.4f}")
            topo_rows.append({
                "n": n, "form": name,
                "phi": spec["phi"], "structure": spec["structure"],
            })
        pool_phi = cat["pool"]["phi"]
        hub_phi = cat["conjunctive_hub"]["phi"]
        if not (pool_phi > hub_phi + 1e-9):
            h2_ok = False
        max_phi = max(s["phi"] for s in cat.values())
        maxima = [nm for nm, s in cat.items() if abs(s["phi"] - max_phi) < 1e-9]
        print(f"  catalog max Φ={max_phi:.4f}  argmax={maxima}  "
              f"pool_in_max={('pool' in maxima)}")
        if "pool" not in maxima:
            h2_ok = False
        if n == 4 and maxima != ["pool"]:
            h2_ok = False
        n_to_hub = 0
        n_to_pool = 0
        n_to_max = 0
        for start in cat:
            term = hillclimb_topo(start, cat)
            traj_rows.append({"n": n, "start": start, "terminal": term,
                              "phi_start": cat[start]["phi"],
                              "phi_term": cat[term]["phi"]})
            if term == "conjunctive_hub":
                n_to_hub += 1
            if term == "pool":
                n_to_pool += 1
            if abs(cat[term]["phi"] - max_phi) < 1e-9:
                n_to_max += 1
            if n == 4 and term != "pool":
                h2_ok = False
            if n == 3 and abs(cat[term]["phi"] - max_phi) >= 1e-9:
                h2_ok = False
        print(f"  trajectories: to_pool={n_to_pool}/{len(cat)}  "
              f"to_hub={n_to_hub}/{len(cat)}  "
              f"to_catalog_max={n_to_max}/{len(cat)}")
        if n_to_hub > len(cat) / 2:
            h1_panel_b = True

    ctrl_pool = all(
        next(r["phi"] for r in topo_rows if r["n"] == n and r["form"] == "pool")
        >
        next(r["phi"] for r in topo_rows if r["n"] == n and r["form"] == "conjunctive_hub")
        for n in (3, 4)
    )
    print(f"  pool Φ > hub Φ at n=3,4: {'PASS' if ctrl_pool else 'FAIL'}")

    ctrl = ctrl_faithful and ctrl_79 and ctrl_pool
    if not ctrl:
        raise SystemExit("ABORT: instrument / #79 / pool control failed")

    h1 = ctrl and (h1_panel_a or h1_panel_b)
    h2 = ctrl and h2_ok
    h3 = ctrl and h3_panel_a

    if h2 and h3 and not h1:
        verdict_word = "PLATEAU_ELSE_POOL"
        reading = (
            "PLATEAU_ELSE_POOL — under fixed party reads, S' ascent "
            "stops on a multi-form Φ=2 plateau (hub not selected); when "
            "topology can open, greedy Φ-ascent reaches the catalog max "
            "(pool uniquely at n=4; pool/ring tie at n=3)"
        )
    elif h2 and not h1 and not h3:
        verdict_word = "TO_POOL"
        reading = (
            "TO_POOL — topology-catalog Φ-ascent terminates at the "
            "all-required pool; conjunctive hub is not the attractor"
        )
    elif h1 and not h2:
        verdict_word = "TO_HUB"
        reading = (
            "TO_HUB — Φ-ascent majority-terminates at the conjunctive hub"
        )
    elif h3 and not h2:
        verdict_word = "ELSEWHERE"
        reading = (
            "ELSEWHERE — mechanism ascent lands on a Φ plateau / "
            "non-hub terminal; pool not reached on topology panel"
        )
    else:
        verdict_word = "ASCENT_MIXED"
        reading = "ASCENT_MIXED — see panel stats"

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  Panel A: n_max={len(maximizers)}  to_AND={n_to_and}/256  "
          f"to_OR={n_to_or}/256  h3_plateau={h3_panel_a}")
    print(f"  Panel B: all→pool={h2_ok}  hub_majority={h1_panel_b}")
    print(f"  H1 (to conjunctive hub): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (to pool / catalog max): {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (somewhere else / plateau): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "panel_a_terminals.csv"), "w", newline="") as fh:
        fields = ["start", "terminal", "phi_start", "phi_term", "struct_term",
                  "is_and", "is_or", "is_maximizer"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in term_rows:
            w.writerow({
                **r,
                "phi_start": f"{r['phi_start']:.8f}",
                "phi_term": f"{r['phi_term']:.8f}",
            })

    with open(os.path.join(RESULTS, "panel_a_summary.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "phi_star", "n_maximizers", "and_mask", "or_mask",
            "n_to_and", "n_to_or", "n_terminals",
        ])
        w.writeheader()
        w.writerow({
            "phi_star": f"{phi_star:.8f}",
            "n_maximizers": len(maximizers),
            "and_mask": AND,
            "or_mask": OR,
            "n_to_and": n_to_and,
            "n_to_or": n_to_or,
            "n_terminals": len(terminals),
        })

    with open(os.path.join(RESULTS, "panel_b_catalog.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["n", "form", "phi", "structure"])
        w.writeheader()
        for r in topo_rows:
            w.writerow({**r, "phi": f"{r['phi']:.8f}"})

    with open(os.path.join(RESULTS, "panel_b_trajectories.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "n", "start", "terminal", "phi_start", "phi_term",
        ])
        w.writeheader()
        for r in traj_rows:
            w.writerow({
                **r,
                "phi_start": f"{r['phi_start']:.8f}",
                "phi_term": f"{r['phi_term']:.8f}",
            })

    with open(os.path.join(RESULTS, "probe79.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["epoch", "r", "phi", "structure"])
        w.writeheader()
        for r in path79:
            w.writerow({
                "epoch": r["epoch"],
                "r": f"{r['r']:.2f}",
                "phi": f"{r['phi']:.8f}",
                "structure": r["structure"],
            })

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "n_maximizers": len(maximizers),
            "n_to_and": n_to_and,
            "n_to_or": n_to_or,
            "panel_b_all_to_pool": int(h2_ok),
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
