"""Graded commit × topology carriers (RESEARCH_AGENDA_V3 #11).

On ring vs hub vs necklace, does graded min-commit keep sharp class
labels while Φ grades (V2 #2 SHARP_CLASS_GRADED_PATH), or does topology
force class flips?

Exact IIT-4.0 via pyphi_iit4_mv. Hypotheses fixed in hypotheses.md.

Run (default — recompute hub/ring; load committed necklace census):
  python org_frontier/studies/graded_topo_carriers/analyze_graded_topo.py

Rebuild necklace census (size≤4 exhaustive; minutes):
  python org_frontier/studies/graded_topo_carriers/analyze_graded_topo.py --rebuild-necklace
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from itertools import combinations

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_THIRD = os.path.join(_REPO_ROOT, "third_party")
for p in (_THIRD, _REPO_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import convert, new_big_phi

from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules
from org_frontier.probes.lib import major_complex
from pyphi_iit4_mv import MultivaluedNetwork, MultivaluedSubsystem, maximal_complex
from pyphi_iit4_mv.conditional_independence import decode_state, encode_state
from pyphi_iit4_mv.sia_mv import sia

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
K = 3
REF_PATH = ("NULL", "DYADIC", "TRIADIC")


def structure_of(n_core: int, phi: float) -> str:
    if n_core <= 0 or phi <= PHI_TOL:
        return "NULL"
    if n_core == 1:
        return "MONADIC"
    if n_core == 2:
        return "DYADIC"
    return "TRIADIC"


def binary_control():
    labels = ("W", "S", "C")
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    core, phi = major_complex(rules, labels)
    core_t = tuple(core) if core is not None else ()
    phi = float(phi) if core_t else 0.0
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    sbs = convert.state_by_node2state_by_state(tpm)
    net = MultivaluedNetwork(sbs, [2, 2, 2], cm=cm, node_labels=labels)
    mc = maximal_complex(net, (1, 1, 1))
    if isinstance(mc, new_big_phi.NullPhiStructure) or mc.node_indices is None:
        mv_core, mv_phi = (), 0.0
    else:
        mv_core = tuple(labels[i] for i in mc.node_indices)
        mv_phi = float(mc.phi)
    return {
        "stock_structure": structure_of(len(core_t), phi),
        "stock_phi": phi,
        "mv_structure": structure_of(len(mv_core), mv_phi),
        "mv_phi": mv_phi,
        "ok": (
            set(core_t) == {"W", "S", "C"}
            and abs(phi - 2.0) < PHI_TOL
            and set(mv_core) == {"W", "S", "C"}
            and abs(mv_phi - 2.0) < PHI_TOL
        ),
    }


def hub_net(k: int = K):
    labels = ("W", "S", "C")
    ks = (k,) * 3
    N = k**3
    sbs = np.zeros((N, N), dtype=float)
    for i in range(N):
        w, s, c = decode_state(i, ks)
        sbs[i, encode_state((s, min(w, c), s), ks)] = 1.0
    cm = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
    return MultivaluedNetwork(sbs, list(ks), cm=cm, node_labels=labels), labels


def ring_net(n: int, k: int = K):
    labels = tuple(f"x{i}" for i in range(n))
    ks = (k,) * n
    N = k**n
    sbs = np.zeros((N, N), dtype=float)
    for i in range(N):
        st = decode_state(i, ks)
        nxt = tuple(min(st[(j - 1) % n], st[(j + 1) % n]) for j in range(n))
        sbs[i, encode_state(nxt, ks)] = 1.0
    cm = np.zeros((n, n), dtype=float)
    for j in range(n):
        cm[(j - 1) % n, j] = 1.0
        cm[(j + 1) % n, j] = 1.0
    return MultivaluedNetwork(sbs, list(ks), cm=cm, node_labels=labels), labels


def necklace_net(k: int = K):
    labels = ("P0", "P1", "P2", "H0", "H1", "H2")
    n = 6
    ks = (k,) * n
    N = k**n
    sbs = np.zeros((N, N), dtype=float)
    for i in range(N):
        p0, p1, p2, h0, h1, h2 = decode_state(i, ks)
        nxt = (
            min(h2, h0),
            min(h0, h1),
            min(h1, h2),
            min(p0, p1),
            min(p1, p2),
            min(p2, p0),
        )
        sbs[i, encode_state(nxt, ks)] = 1.0
    cm = np.zeros((n, n), dtype=float)
    for pi, hs in ((0, (5, 3)), (1, (3, 4)), (2, (4, 5))):
        for h in hs:
            cm[h, pi] = 1.0
    for hi, ps in ((3, (0, 1)), (4, (1, 2)), (5, (2, 0))):
        for p in ps:
            cm[p, hi] = 1.0
    return MultivaluedNetwork(sbs, list(ks), cm=cm, node_labels=labels), labels


def major_full(net, labels, state):
    mc = maximal_complex(net, state)
    if isinstance(mc, new_big_phi.NullPhiStructure) or mc.node_indices is None:
        return (), 0.0, "NULL"
    core = tuple(labels[i] for i in mc.node_indices)
    phi = float(mc.phi)
    return core, phi, structure_of(len(core), phi)


def major_bounded(net, labels, state, max_size: int = 4):
    """Max-Φ complex among subsystems with size ≤ max_size.

    On Φ ties prefer larger n (aligns with largest-first major complex
    when a larger subsystem matches the dyad Φ).
    """
    n = len(labels)
    best_phi = 0.0
    best_nodes: tuple[int, ...] = ()
    for r in range(1, min(max_size, n) + 1):
        for nodes in combinations(range(n), r):
            try:
                sub = MultivaluedSubsystem(net, state, nodes=nodes)
                res = sia(sub)
                phi = float(res.phi) if res else 0.0
            except Exception:
                phi = 0.0
            if phi > best_phi + PHI_TOL or (
                abs(phi - best_phi) <= PHI_TOL
                and phi > PHI_TOL
                and r > len(best_nodes)
            ):
                best_phi = phi
                best_nodes = nodes
    if not best_nodes or best_phi <= PHI_TOL:
        return (), 0.0, "NULL"
    core = tuple(labels[i] for i in best_nodes)
    return core, best_phi, structure_of(len(core), best_phi)


def make_row(carrier, n, L, core, phi, struct, note=""):
    return {
        "carrier": carrier,
        "n": n,
        "L": L,
        "structure": struct,
        "n_core": len(core),
        "core": "|".join(core) if core else "",
        "phi": phi,
        "note": note,
    }


def write_csv(path: str, rows: list[dict]) -> None:
    if not rows:
        return
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def load_csv(path: str) -> list[dict]:
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["n"] = int(r["n"])
        r["L"] = int(r["L"])
        r["n_core"] = int(r["n_core"])
        r["phi"] = float(r["phi"])
    return rows


def compute_hub_ring() -> list[dict]:
    rows: list[dict] = []
    net, labels = hub_net()
    for L in (0, 1, 2):
        core, phi, st = major_full(net, labels, (L,) * 3)
        rows.append(make_row("hub", 3, L, core, phi, st, "full_maximal"))
        print(
            f"  hub3 L={L}  {st:<8} n_core={len(core)}  Φ={phi:.4f}  "
            f"core={rows[-1]['core'] or '∅'}",
            flush=True,
        )
    for n in (3, 4):
        net, labels = ring_net(n)
        for L in (0, 1, 2):
            t0 = time.time()
            core, phi, st = major_full(net, labels, (L,) * n)
            rows.append(
                make_row(
                    "ring",
                    n,
                    L,
                    core,
                    phi,
                    st,
                    f"full_maximal ({time.time() - t0:.1f}s)",
                )
            )
            print(
                f"  ring{n} L={L}  {st:<8} n_core={len(core)}  Φ={phi:.4f}  "
                f"core={rows[-1]['core'] or '∅'}",
                flush=True,
            )
    return rows


def compute_necklace(max_size: int = 4) -> list[dict]:
    rows: list[dict] = []
    net, labels = necklace_net()
    for L in (0, 1, 2):
        t0 = time.time()
        if L == 0:
            core, phi, st = major_full(net, labels, (0,) * 6)
            note = f"full_maximal ({time.time() - t0:.1f}s)"
        else:
            core, phi, st = major_bounded(
                net, labels, (L,) * 6, max_size=max_size
            )
            note = f"bounded_max_size={max_size} ({time.time() - t0:.1f}s)"
        rows.append(make_row("necklace", 6, L, core, phi, st, note))
        print(
            f"  neck6 L={L}  {st:<8} n_core={len(core)}  Φ={phi:.4f}  "
            f"core={rows[-1]['core'] or '∅'}  [{note}]",
            flush=True,
        )
    return rows


def path_for(rows: list[dict], carrier: str, n: int) -> list[dict]:
    out = [r for r in rows if r["carrier"] == carrier and int(r["n"]) == n]
    return sorted(out, key=lambda r: int(r["L"]))


def evaluate(ctrl: dict, rows: list[dict]) -> str:
    print()
    print("PANEL")
    print(
        f"  {'carrier':<10}{'n':>3}  {'L':>2}  {'structure':<8}  "
        f"{'n_core':>6}  {'Φ':>8}  core"
    )
    for r in sorted(rows, key=lambda x: (x["carrier"], int(x["n"]), int(x["L"]))):
        print(
            f"  {r['carrier']:<10}{int(r['n']):>3}  {int(r['L']):>2}  "
            f"{r['structure']:<8}  {int(r['n_core']):>6}  "
            f"{float(r['phi']):>8.4f}  {r['core'] or '∅'}"
        )

    carriers = [("hub", 3), ("ring", 3), ("ring", 4), ("necklace", 6)]
    paths = {c: path_for(rows, c[0], c[1]) for c in carriers}

    sharp_ok = True
    grade_ok = True
    path_ok = True
    print()
    print("PER-CARRIER PATHS")
    for key, seq in paths.items():
        structs = [r["structure"] for r in seq]
        phis = [float(r["phi"]) for r in seq]
        sharp = all(
            s in {"NULL", "MONADIC", "DYADIC", "TRIADIC"} for s in structs
        )
        grades = (
            len(phis) == 3
            and phis[0] <= phis[1] + PHI_TOL
            and phis[1] < phis[2] - PHI_TOL
        )
        matches = tuple(structs) == REF_PATH
        sharp_ok = sharp_ok and sharp
        grade_ok = grade_ok and grades
        path_ok = path_ok and matches
        print(
            f"  {key[0]} n={key[1]}: {' → '.join(structs)}  "
            f"Φ={[round(p, 4) for p in phis]}  "
            f"sharp={'Y' if sharp else 'N'} grade={'Y' if grades else 'N'} "
            f"ref={'Y' if matches else 'N'}"
        )

    h1, h2, h3 = sharp_ok, grade_ok, path_ok
    print()
    print("HYPOTHESES")
    print(
        f"H1 (structure class stays sharp on all carriers): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"H2 (Φ grades with L on all carriers):             "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"H3 (class path = hub NULL→DYADIC→TRIADIC):        "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )

    if not ctrl["ok"] or not h1:
        verdict = "CONTROLS_FAIL"
    elif not h2:
        verdict = "GRADED_BREAKS"
    elif not h3:
        verdict = "TOPOLOGY_FORCES_FLIPS"
    else:
        verdict = "SHARP_HOLDS_ACROSS_TOPO"

    h4 = verdict in (
        "SHARP_HOLDS_ACROSS_TOPO",
        "TOPOLOGY_FORCES_FLIPS",
        "GRADED_BREAKS",
    )
    print(
        f"H4 (panel closed):                                "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )

    print()
    print("STATUS")
    print(f"  control: {'PASS' if ctrl['ok'] else 'FAIL'}")
    grid = ctrl["ok"] and h1 and h2 and h3
    print(f"  verification grid: {'PASS' if grid else 'FAIL'}")
    print("  best next:         #12 noise×composed (necklace/multi-hub span)")
    print(f"verdict: {verdict}")
    if verdict == "SHARP_HOLDS_ACROSS_TOPO":
        reading = (
            "SHARP_HOLDS_ACROSS_TOPO — graded min-commit keeps discrete "
            "NULL/DYADIC/TRIADIC labels while Φ grades on hub, ring (n=3,4), "
            "and necklace; no topology-forced class flip relative to V2 #2"
        )
    elif verdict == "TOPOLOGY_FORCES_FLIPS":
        reading = (
            "TOPOLOGY_FORCES_FLIPS — some carrier’s class path leaves the "
            "hub NULL→DYADIC→TRIADIC sequence; topology forces flips the "
            "fixed-hub panel never saw"
        )
    elif verdict == "GRADED_BREAKS":
        reading = (
            "GRADED_BREAKS — Φ fails to grade with L on at least one carrier"
        )
    else:
        reading = verdict
    print(f"reading: {reading}")

    # Stable one-liners for reproduce.json expect hooks
    print()
    print(f"  faithful triad: {ctrl['stock_structure']} Φ={ctrl['stock_phi']:.6f}  "
          f"{'PASS' if ctrl['ok'] else 'FAIL'}")
    print(f"H1 (sharp classes on all carriers):              {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 (Φ grades with L on all carriers):            {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"H3 (path = NULL→DYADIC→TRIADIC on all carriers): {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"H4 (panel closed):                               {'SUPPORTED' if h4 else 'REFUTED'}")
    print(
        "path_grid: "
        + "; ".join(
            f"{k[0]}{k[1]}={'→'.join(r['structure'] for r in paths[k])}"
            for k in carriers
        )
    )

    summary = {
        "verdict": verdict,
        "reading": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "control_ok": ctrl["ok"],
        "ref_path": list(REF_PATH),
        "panel": rows,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    write_csv(os.path.join(RESULTS, "panel.csv"), rows)
    print("wrote results/panel.csv results/summary.json")
    return verdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--rebuild-necklace",
        action="store_true",
        help="recompute necklace census (size≤4 exhaustive; minutes)",
    )
    args = ap.parse_args()

    os.makedirs(RESULTS, exist_ok=True)
    t0 = time.time()
    print("GRADED × TOPOLOGY CARRIERS — V3 #11")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 72)
    print("  form: graded min-commit (k=3) on hub / ring / necklace")
    print("  commit level L on diagonal state (L,…,L)")
    print("  instrument: pyphi_iit4_mv maximal_complex (exact IIT-4.0)")
    print()

    ctrl = binary_control()
    print("BINARY CONTROL (AND triad @ (1,1,1))")
    print(
        f"  stock: {ctrl['stock_structure']} Φ={ctrl['stock_phi']:.3f}  "
        f"overlay: {ctrl['mv_structure']} Φ={ctrl['mv_phi']:.3f}  "
        f"{'PASS' if ctrl['ok'] else 'FAIL'}"
    )
    if not ctrl["ok"]:
        raise SystemExit("ABORT: instrument control failed")

    print()
    print("HUB + RING (full maximal_complex)")
    live = compute_hub_ring()

    neck_path = os.path.join(RESULTS, "necklace_census.csv")
    print()
    print("NECKLACE (bounded major complex, max_size=4)")
    if args.rebuild_necklace or not os.path.exists(neck_path):
        neck = compute_necklace(max_size=4)
        write_csv(neck_path, neck)
        print(f"  wrote {neck_path}")
    else:
        neck = load_csv(neck_path)
        for r in neck:
            print(
                f"  neck6 L={r['L']}  {r['structure']:<8} n_core={r['n_core']}  "
                f"Φ={r['phi']:.4f}  core={r['core'] or '∅'}  [loaded census]",
                flush=True,
            )

    evaluate(ctrl, live + neck)
    print(f"elapsed {time.time() - t0:.1f}s")
    print("=" * 72)


if __name__ == "__main__":
    main()
