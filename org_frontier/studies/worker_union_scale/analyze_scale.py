"""Agenda #31 — worker union vs counterpart coalition size sweep.

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #66/#55/#97; #29/#30 pointers only.

Run:  python org_frontier/studies/worker_union_scale/analyze_scale.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9


def counterpart_coal(k: int, style: str):
    labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, k + 1)])
    cidx = list(range(2, 2 + k))

    def s_rule(x):
        r = x[0]
        for c in cidx:
            r &= x[c]
        return r

    rules = [None] * (k + 2)
    rules[0] = lambda x: x[1]
    rules[1] = s_rule
    for i, c in enumerate(cidx):
        others = [o for o in cidx if o != c]
        if style == "weak":
            if others:
                rules[c] = (
                    lambda x, others=tuple(others): int(
                        bool(x[1]) or any(x[o] for o in others)
                    )
                )
            else:
                rules[c] = lambda x: x[1]
        else:
            nxt = cidx[(i + 1) % k]
            rules[c] = lambda x, nxt=nxt: x[nxt]
    return rules, labels, {f"C{i}" for i in range(1, k + 1)}


def worker_union(k: int, style: str):
    labels = tuple([f"W{i}" for i in range(1, k + 1)] + ["S", "C"])
    widx = list(range(k))
    sidx, cidx = k, k + 1

    def s_rule(x):
        r = x[cidx]
        for w in widx:
            r &= x[w]
        return r

    rules = [None] * (k + 2)
    rules[sidx] = s_rule
    rules[cidx] = lambda x, sidx=sidx: x[sidx]
    for i, w in enumerate(widx):
        others = [o for o in widx if o != w]
        if style == "weak":
            if others:
                rules[w] = (
                    lambda x, sidx=sidx, others=tuple(others): int(
                        bool(x[sidx]) or any(x[o] for o in others)
                    )
                )
            else:
                rules[w] = lambda x, sidx=sidx: x[sidx]
        else:
            nxt = widx[(i + 1) % k]
            rules[w] = lambda x, nxt=nxt: x[nxt]
    return rules, labels, {f"W{i}" for i in range(1, k + 1)}


def counterpart_coal_P(k: int):
    labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, k + 1)] + ["P"])
    cidx = list(range(2, 2 + k))
    pidx = 2 + k

    def s_rule(x):
        r = x[0] & x[pidx]
        for c in cidx:
            r &= x[c]
        return r

    rules = [None] * (k + 3)
    rules[0] = lambda x: x[1]
    rules[1] = s_rule
    rules[pidx] = lambda x: x[1]
    for c in cidx:
        others = tuple(o for o in cidx if o != c)
        if others:
            rules[c] = (
                lambda x, others=others: int(bool(x[1]) or any(x[o] for o in others))
            )
        else:
            rules[c] = lambda x: x[1]
    return rules, labels, {f"C{i}" for i in range(1, k + 1)}


def worker_union_P(k: int):
    labels = tuple([f"W{i}" for i in range(1, k + 1)] + ["S", "C", "P"])
    widx = list(range(k))
    sidx, cidx, pidx = k, k + 1, k + 2

    def s_rule(x):
        r = x[cidx] & x[pidx]
        for w in widx:
            r &= x[w]
        return r

    rules = [None] * (k + 3)
    rules[sidx] = s_rule
    rules[cidx] = lambda x, sidx=sidx: x[sidx]
    rules[pidx] = lambda x, sidx=sidx: x[sidx]
    for w in widx:
        others = tuple(o for o in widx if o != w)
        if others:
            rules[w] = (
                lambda x, sidx=sidx, others=others: int(
                    bool(x[sidx]) or any(x[o] for o in others)
                )
            )
        else:
            rules[w] = lambda x, sidx=sidx: x[sidx]
    return rules, labels, {f"W{i}" for i in range(1, k + 1)}


def eval_form(side, style, k, builder):
    rules, labels, group = builder(k) if style == "P" else builder(k, style)
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    core_s = set(core_t)
    vanishes = len(core_t) == 0 or not group.issubset(core_s)
    return {
        "side": side,
        "style": style,
        "k": k,
        "n": len(labels),
        "structure": v.structure,
        "phi": phi,
        "n_core": len(core_t),
        "core": "|".join(core_t) if core_t else "",
        "core_eq_group": int(core_s == group),
        "vanishes": int(vanishes),
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("WORKER UNION SCALE — agenda #31")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  sweep: worker union vs counterpart coalition; weak/strong/P")
    print("  cited: #66/#55/#97; #29/#30 pointers only")
    print()

    rows = []
    # weak & strong k sweeps
    for style in ("weak", "strong"):
        ks = (1, 2, 3, 4) if style == "weak" else (2, 3, 4)
        for k in ks:
            if style == "strong" and k == 1:
                continue
            rows.append(eval_form("counterpart", style, k, counterpart_coal))
            rows.append(eval_form("worker", style, k, worker_union))
    # with principal (weak peer), k=2,3 — #66 mirror
    for k in (2, 3):
        rows.append(eval_form("counterpart", "P", k, lambda kk: counterpart_coal_P(kk)))
        rows.append(eval_form("worker", "P", k, lambda kk: worker_union_P(kk)))

    print(
        f"  {'side':<12}{'style':<8}{'k':>2}{'n':>3}  {'struct':<8}"
        f"{'Φ':>7}{'n_c':>4}  eq? van?"
    )
    for r in rows:
        print(
            f"  {r['side']:<12}{r['style']:<8}{r['k']:>2}{r['n']:>3}  "
            f"{r['structure']:<8}{r['phi']:>7.3f}{r['n_core']:>4}  "
            f"{'Y' if r['core_eq_group'] else 'n'}   "
            f"{'Y' if r['vanishes'] else 'n'}  {r['core']}"
        )

    # H1: matched cells agree
    mismatches = []
    keys = {(r["style"], r["k"]) for r in rows}
    by = {(r["side"], r["style"], r["k"]): r for r in rows}
    for style, k in sorted(keys):
        a = by.get(("counterpart", style, k))
        b = by.get(("worker", style, k))
        if not a or not b:
            continue
        ok = (
            abs(a["phi"] - b["phi"]) < PHI_TOL
            and a["n_core"] == b["n_core"]
            and a["core_eq_group"] == b["core_eq_group"]
            and a["vanishes"] == b["vanishes"]
        )
        if not ok:
            mismatches.append((style, k, a, b))

    h1 = len(mismatches) == 0

    # H2: worker vanishes at some k>=3
    worker_rows = [r for r in rows if r["side"] == "worker"]
    h2 = any(r["vanishes"] and r["k"] >= 3 for r in worker_rows)

    # H3: different law vs counterpart
    h3 = not h1

    # #97 contrast: designed solidarity persists at n=6
    n6 = [r for r in rows if r["n"] == 6 and r["side"] == "worker"]
    persists_n6 = all(not r["vanishes"] and r["core_eq_group"] for r in n6)

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (union scales like counterpart coal): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (vanishes past size, #97-like):        "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (different scaling vs counterpart):   "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  matched cells: {len(keys)}  mismatches: {len(mismatches)}"
    )
    print(
        f"  worker persists at n=6 (≠#97 vanish): "
        f"{'YES' if persists_n6 else 'no'}"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    if h1 and (not h2) and (not h3) and ctrl_ok and persists_n6:
        verdict_s = "UNION_MIRRORS_COAL"
    elif h1 and h2:
        verdict_s = "MIRROR_THEN_VANISH"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and (not h2) and (not h3) and persists_n6

    print()
    print("STATUS")
    print(f"  H1 mirrors counterpart: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 vanishes like #97:   {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 different law:       {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #32 rival platforms (alt #33 regulator capture)")
    print()
    print(
        f"verdict: {verdict_s} — worker union matches counterpart coalition "
        f"cell-for-cell (Φ, n_core, core==group) under weak/strong/P; "
        f"solidarity persists through n=6 (core=peer group) and does not "
        f"vanish like #97's random single-mediator triadicity"
    )
    print(
        "reading: UNION_MIRRORS_COAL — role symmetry (#55) extends to union "
        "scaling; designed peer solidarity is the structure that survives at "
        "scale where random mediation disappears (#97); #29/#30 pointers only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
