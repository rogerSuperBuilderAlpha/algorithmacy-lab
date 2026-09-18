"""Hierarchy-of-mediators census (agenda #15).

Level-tagged exact IIT-4.0 grid on recurrent AND trees (q144 family) and
feedforward hub chains (q148 family). Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/mediator_hierarchy_census/analyze_hierarchy.py
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

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def _and_of(indices):
    idxs = tuple(indices)

    def f(x, idxs=idxs):
        v = 1
        for i in idxs:
            v &= x[i]
        return v

    return f


def _copy(i):
    return lambda x, i=i: x[i]


# ---------------------------------------------------------------------------
# Recurrent balanced AND tree (q144 construction) + level tags
# ---------------------------------------------------------------------------

def recurrent_tree(d, b):
    """Balanced b-ary tree of depth d; internals AND children; leaves read apex.

    Returns rules, labels, level_of (dict label -> 'apex'|'mid'|'leaf').
    """
    levels, nid = [], 0
    for L in range(d + 1):
        count = b ** L
        levels.append(list(range(nid, nid + count)))
        nid += count
    n = nid
    labels = tuple(chr(65 + i) for i in range(n))
    apex = levels[0][0]
    children = {}
    for L in range(d):
        for pi, p in enumerate(levels[L]):
            children[p] = levels[L + 1][pi * b:(pi + 1) * b]
    rules = [None] * n
    for L in range(d):
        for p in levels[L]:
            rules[p] = _and_of(children[p])
    for leaf in levels[d]:
        rules[leaf] = _copy(apex)

    level_of = {}
    for i in levels[0]:
        level_of[labels[i]] = "apex"
    for L in range(1, d):
        for i in levels[L]:
            level_of[labels[i]] = "mid"
    for i in levels[d]:
        level_of[labels[i]] = "leaf"
    # depth 1: only apex + leaves (no mid)
    return rules, labels, level_of, {"family": "recurrent_tree", "d": d, "b": b, "n": n}


def crossed_d2_b2():
    """Depth-2, breadth-2 with one leaf per mid (n=5), recurrent AND.

    Levels: apex S0; mids S1,S2; leaves L1,L2.
    S0'=S1∧S2; S1'=L1; S2'=L2; L1'=S0; L2'=S0  (mids AND one child; leaves read apex).
    Equivalent to a truncated balanced tree (second-level breadth 1).
    """
    # indices: 0=S0, 1=S1, 2=S2, 3=L1, 4=L2
    labels = ("S0", "S1", "S2", "L1", "L2")
    rules = [
        _and_of([1, 2]),  # S0
        _copy(3),         # S1' = L1
        _copy(4),         # S2' = L2
        _copy(0),         # L1' = S0
        _copy(0),         # L2' = S0
    ]
    level_of = {"S0": "apex", "S1": "mid", "S2": "mid", "L1": "leaf", "L2": "leaf"}
    return rules, labels, level_of, {"family": "recurrent_crossed", "d": 2, "b": 2, "n": 5}


# ---------------------------------------------------------------------------
# Feedforward hub chain (q148 family, g=1)
# ---------------------------------------------------------------------------

def hub_chain(L):
    """L hubs each with one party. Hub0 gates p0; hub k gates pk and reads hub k-1.

    Node order: H0, P0, H1, P1, ...
    P_i' = H_i; H0' = P0; H_k' = H_{k-1} ∧ P_k  (feedforward AND gate).
    """
    labels = []
    for k in range(L):
        labels.append(f"H{k}")
        labels.append(f"P{k}")
    labels = tuple(labels)
    n = 2 * L
    rules = [None] * n
    # index: H_k = 2k, P_k = 2k+1
    rules[1] = _copy(0)  # P0' = H0
    rules[0] = _copy(1)  # H0' = P0  (top loop)
    for k in range(1, L):
        hk, pk = 2 * k, 2 * k + 1
        rules[pk] = _copy(hk)
        rules[hk] = _and_of([2 * (k - 1), pk])  # H_{k-1} ∧ P_k
    level_of = {}
    for k in range(L):
        level_of[f"H{k}"] = "apex" if k == 0 else "mid"
        level_of[f"P{k}"] = "leaf" if k == 0 else "mid"  # own group with hub
    # For H4 "top-local": core ⊆ {H0, P0}
    return rules, labels, level_of, {"family": "hub_chain", "L": L, "n": n}


def run_cell(rules, labels, level_of, meta):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    tags = sorted({level_of[lab] for lab in core_t if lab in level_of})
    occupied = sorted(set(level_of.values()))
    spans_all_levels = all(tag in tags for tag in occupied) if core_t else False
    top_local = set(core_t).issubset({"H0", "P0"}) if meta["family"] == "hub_chain" else (
        tags == ["apex"] or tags == []
    )
    # For recurrent trees, "top-local" means only apex tag
    if meta["family"] != "hub_chain":
        top_local = tags == ["apex"]
    return {
        **meta,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": core_t,
        "core_phi": float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan"),
        "core_levels": tuple(tags),
        "occupied_levels": tuple(occupied),
        "spans_all_levels": spans_all_levels,
        "top_local": top_local,
        "n_core": len(core_t),
        "seconds": round(time.time() - t0, 2),
    }


def fmt_core(core):
    return "(" + ",".join(core) + ")" if core else "()"


def main():
    print("MEDIATOR HIERARCHY CENSUS — agenda #15 (extends q144 / q148)")
    print("=" * 80)
    print("  cited: q144 depth-flat/breadth-grows; q148 top-local hub chains;")
    print("         two_triad shared-mediator merge; ternary TOOLING_GAP")
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

    print("RECURRENT TREE — DEPTH AXIS (b=1)")
    print("-" * 80)
    depth_rows = []
    for d in (1, 2, 3, 4):
        rules, labels, level_of, meta = recurrent_tree(d, 1)
        r = run_cell(rules, labels, level_of, meta)
        rows.append(r)
        depth_rows.append(r)
        print(f"  d={d} n={r['n']}  whole={r['structure']:<8} Φ_MIP={r['whole_phi_mip']:.3f}  "
              f"core={fmt_core(r['core']):<18} coreΦ={r['core_phi']:.3f}  "
              f"levels={r['core_levels']}  spans_all={r['spans_all_levels']}  ({r['seconds']}s)")
    print()

    print("RECURRENT TREE — BREADTH AXIS (d=1)")
    print("-" * 80)
    breadth_rows = []
    for b in (2, 3, 4):
        rules, labels, level_of, meta = recurrent_tree(1, b)
        r = run_cell(rules, labels, level_of, meta)
        rows.append(r)
        breadth_rows.append(r)
        print(f"  b={b} n={r['n']}  whole={r['structure']:<8} Φ_MIP={r['whole_phi_mip']:.3f}  "
              f"core={fmt_core(r['core']):<18} coreΦ={r['core_phi']:.3f}  "
              f"levels={r['core_levels']}  spans_all={r['spans_all_levels']}  ({r['seconds']}s)")
    print()

    print("RECURRENT CROSSED — d=2, b=2 truncated (n=5)")
    print("-" * 80)
    rules, labels, level_of, meta = crossed_d2_b2()
    crossed = run_cell(rules, labels, level_of, meta)
    rows.append(crossed)
    print(f"  n={crossed['n']}  whole={crossed['structure']:<8} Φ_MIP={crossed['whole_phi_mip']:.3f}  "
          f"core={fmt_core(crossed['core']):<22} coreΦ={crossed['core_phi']:.3f}  "
          f"levels={crossed['core_levels']}  spans_all={crossed['spans_all_levels']}  "
          f"({crossed['seconds']}s)")
    print()

    print("FEEDFORWARD HUB CHAIN (q148 family)")
    print("-" * 80)
    chain_rows = []
    for L in (2, 3):
        rules, labels, level_of, meta = hub_chain(L)
        r = run_cell(rules, labels, level_of, meta)
        rows.append(r)
        chain_rows.append(r)
        print(f"  L={L} n={r['n']}  whole={r['structure']:<8} Φ_MIP={r['whole_phi_mip']:.3f}  "
              f"core={fmt_core(r['core']):<18} coreΦ={r['core_phi']:.3f}  "
              f"levels={r['core_levels']}  top_local={r['top_local']}  ({r['seconds']}s)")
    print()

    # ---- Hypotheses ----
    depth_phis = [r["core_phi"] for r in depth_rows]
    h1 = (
        ctrl
        and max(depth_phis) - min(depth_phis) < 1e-6
        and all(abs(p - 2.0) < 1e-6 for p in depth_phis)
    )
    bphis = [r["core_phi"] for r in breadth_rows]
    h2 = all(bphis[i + 1] > bphis[i] + PHI_EPS for i in range(len(bphis) - 1))

    recurrent = [r for r in rows if r["family"] in ("recurrent_tree", "recurrent_crossed")]
    h3 = all(r["spans_all_levels"] for r in recurrent)
    h4 = all(r["top_local"] and set(r["core"]).issubset({"H0", "P0"}) for r in chain_rows)
    h5 = h3 and h4

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  depth Φ (b=1, d=1..4):     {[round(p, 3) for p in depth_phis]}")
    print(f"  breadth Φ (d=1, b=2..4):   {[round(p, 3) for p in bphis]}")
    print(f"  crossed levels:            {crossed['core_levels']}  spans_all={crossed['spans_all_levels']}")
    print(f"  hub-chain top_local:       {[r['top_local'] for r in chain_rows]}  "
          f"cores={[r['core'] for r in chain_rows]}")
    print(f"  H1 (depth flat Φ=2.0):                 {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (breadth Φ increases):              {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (recurrent spans all levels):       {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (feedforward hub-chain top-local):  {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (closure decides level locus):      {'SUPPORTED' if h5 else 'REFUTED'}")

    if h1 and h2 and h5:
        reading = "WIN — depth flat / breadth grows; recurrent spans levels, feedforward top-local"
    elif h1 and h2:
        reading = "PARTIAL — scaling replicates; level-locus contrast incomplete"
    else:
        reading = "NULL — failed to replicate q144 scaling or level map"

    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  which level: recurrent trees → all occupied levels; "
          f"feedforward hub chains → top (H0,P0) only")
    print(f"  depth: Φ=2.0 flat (b=1); breadth: Φ grows {bphis[0]:.0f}→{bphis[-1]:.0f} (d=1)")
    print(f"  crossed d=2/b=2: spans_all={crossed['spans_all_levels']} "
          f"coreΦ={crossed['core_phi']:.3f}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "family", "d", "b", "L", "n", "structure", "whole_phi_mip",
            "core", "core_phi", "core_levels", "occupied_levels",
            "spans_all_levels", "top_local", "n_core", "seconds",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "d": r.get("d", ""),
                "b": r.get("b", ""),
                "L": r.get("L", ""),
                "n": r["n"],
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "core_levels": "|".join(r["core_levels"]),
                "occupied_levels": "|".join(r["occupied_levels"]),
                "spans_all_levels": str(r["spans_all_levels"]),
                "top_local": str(r["top_local"]),
                "n_core": r["n_core"],
                "seconds": r["seconds"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "depth_phis": ";".join(f"{p:.3f}" for p in depth_phis),
            "breadth_phis": ";".join(f"{p:.3f}" for p in bphis),
            "crossed_spans_all": str(crossed["spans_all_levels"]),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
