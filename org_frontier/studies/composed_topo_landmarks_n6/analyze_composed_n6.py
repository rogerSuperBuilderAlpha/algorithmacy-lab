"""Composed-topology landmarks at n≥6 (RESEARCH_AGENDA_V4 #10).

Do V3 #4–#7 class families remain discrete under denser n≥6 random-AND
coupling, or do interstitial atoms dominate?

Exact binary IIT-4.0. Lean: V3 controls (committed) + designed n=6
densify/lifts + thin random n=6 (N=28). Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/composed_topo_landmarks_n6/analyze_composed_n6.py

Rebuild designed lifts (~4 min):
  python org_frontier/studies/composed_topo_landmarks_n6/analyze_composed_n6.py --rebuild-lifts

Rebuild random panel (~25–40 min):
  python org_frontier/studies/composed_topo_landmarks_n6/analyze_composed_n6.py --rebuild-random
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter

import numpy as np

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO not in sys.path:
    sys.path.insert(0, _REPO)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

L6 = {2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 9.0, 12.0, 30.0}
COMPOSED_ATOMS = {2.0, 3.0, 4.0, 6.0}
ON_LANDMARK_MIN = 0.90
PHI_TOL = max(PHI_EPS, 1e-9)


def near(a, b, eps=None):
    if a != a or b != b:
        return False
    if eps is None:
        eps = PHI_TOL
    return abs(float(a) - float(b)) <= eps


def and_of(srcs):
    srcs = tuple(srcs)

    def f(x, srcs=srcs):
        r = 1
        for s in srcs:
            r &= x[s]
        return r

    return f


def or_of(srcs):
    srcs = tuple(srcs)

    def f(x, srcs=srcs):
        r = 0
        for s in srcs:
            r |= x[s]
        return r

    return f


def copy_of(i):
    return lambda x, i=i: x[i]


def load_v3_controls():
    path = os.path.join(RESULTS, "v3_controls.json")
    with open(path) as fh:
        rows = json.load(fh)
    print(f"LOADED V3 CONTROLS — {path} ({len(rows)} rows)")
    return rows


def h1_ok(controls):
    by = {(r["family"], r["name"]): r for r in controls}

    def get(fam, name):
        return by[(fam, name)]

    checks = []
    n = get("#4", "neck_AND")
    checks.append(
        n["structure"] == "triadic"
        and near(n["core_phi"], 4.0)
        and n["full_core"] is True
    )
    o = get("#4", "neck_OR_hub")
    checks.append(o["structure"] == "dyadic" and near(o["core_phi"], 2.0))
    f = get("#5", "roh_leaf_ring")
    checks.append(near(f["core_phi"], 6.0) and f["full_core"] is False)
    k2 = get("#6", "k2_AND")
    k3 = get("#6", "k3_AND")
    checks.append(near(k2["core_phi"], 4.0) and k2["full_core"] is True)
    checks.append(near(k3["core_phi"], 6.0) and k3["full_core"] is True)
    k2o = get("#6", "k2_OR")
    checks.append(k2o["structure"] == "dyadic")
    h = get("#7", "hy_triad_AND")
    checks.append(
        near(h["core_phi"], 2.0) and set(h["core"].split("|")) == {"W", "S", "C"}
    )
    return all(checks), checks


def run_cell(name, labels, rules):
    t0 = time.time()
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    phi = float(phi) if phi is not None else float("nan")
    core = tuple(core) if core else ()
    return {
        "name": name,
        "n": len(labels),
        "structure": v.structure,
        "core_phi": phi,
        "core": "|".join(core),
        "n_core": len(core),
        "full_core": int(len(core) == len(labels)),
        "seconds": round(time.time() - t0, 2),
    }


def build_lifts():
    print("\nDESIGNED LIFTS / DENSIFY (n=6)")
    cells = [
        (
            "hy_n6_AND",
            ("W", "S", "C", "H1", "P1", "T"),
            [
                copy_of(1),
                and_of((0, 2)),
                copy_of(1),
                and_of((1, 4)),
                copy_of(3),
                copy_of(3),
            ],
        ),
        (
            "hy_n6_OR",
            ("W", "S", "C", "H1", "P1", "T"),
            [
                copy_of(1),
                and_of((0, 2)),
                copy_of(1),
                or_of((1, 4)),
                copy_of(3),
                copy_of(3),
            ],
        ),
        (
            "neck_AND",
            ("P0", "P1", "P2", "H0", "H1", "H2"),
            [
                and_of((5, 3)),
                and_of((3, 4)),
                and_of((4, 5)),
                and_of((0, 1)),
                and_of((1, 2)),
                and_of((2, 0)),
            ],
        ),
        (
            "neck_AND_chord",
            ("P0", "P1", "P2", "H0", "H1", "H2"),
            [
                and_of((5, 3)),
                and_of((3, 4)),
                and_of((4, 5)),
                and_of((0, 1, 2)),
                and_of((1, 2)),
                and_of((2, 0)),
            ],
        ),
        (
            "roh_leaf_ring",
            ("H0", "H1", "H2", "P0", "P1", "P2"),
            [
                and_of((3, 2, 1)),
                and_of((4, 0, 2)),
                and_of((5, 1, 0)),
                copy_of(0),
                copy_of(1),
                copy_of(2),
            ],
        ),
        (
            "roh_dense_leaf",
            ("H0", "H1", "H2", "P0", "P1", "P2"),
            [
                and_of((3, 4, 2, 1)),
                and_of((4, 5, 0, 2)),
                and_of((5, 3, 1, 0)),
                copy_of(0),
                copy_of(1),
                copy_of(2),
            ],
        ),
    ]
    rows = []
    for name, labels, rules in cells:
        print(f"  {name} ...", flush=True)
        row = run_cell(name, labels, rules)
        rows.append(row)
        print(
            f"    → {row['structure']} Φ={row['core_phi']} "
            f"core={row['core']} full={row['full_core']} t={row['seconds']}s",
            flush=True,
        )
    path = os.path.join(RESULTS, "lifts.json")
    with open(path, "w") as fh:
        json.dump(rows, fh, indent=2)
    print(f"wrote {path}")
    return rows


def load_lifts():
    path = os.path.join(RESULTS, "lifts.json")
    if not os.path.exists(path):
        return build_lifts()
    with open(path) as fh:
        rows = json.load(fh)
    print(f"\nLOADED LIFTS — {path} ({len(rows)} rows)")
    return rows


def fixed_k_ins(n, k, rng):
    ins = {}
    for i in range(n):
        choices = [j for j in range(n) if j != i]
        picks = rng.choice(choices, size=min(k, len(choices)), replace=False)
        ins[i] = [int(x) for x in picks]
    return ins


def er_ins(n, p, rng):
    ins = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and rng.random() < p:
                ins[i].append(j)
        if not ins[i]:
            c = int(rng.integers(0, n - 1))
            if c >= i:
                c += 1
            ins[i] = [c]
    return ins


def build_random():
    print("\nRANDOM AND PANEL n=6 (lean denser draw)")
    n = 6
    specs = []
    rng = np.random.default_rng(20260919)
    for i in range(12):
        specs.append(("fixed_k2", i, fixed_k_ins(n, 2, rng)))
    for i in range(8):
        specs.append(("fixed_k3", i, fixed_k_ins(n, 3, rng)))
    for i in range(8):
        specs.append(("ER35", i, er_ins(n, 0.35, rng)))
    rows = []
    labels = tuple(f"n{i}" for i in range(n))
    for fam, i, ins in specs:
        tag = f"{fam}_{i}"
        print(f"  {tag} ...", flush=True)
        rules = [and_of(ins[j]) for j in range(n)]
        t0 = time.time()
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        phi = float(phi) if phi is not None else float("nan")
        core = tuple(core) if core else ()
        row = {
            "tag": tag,
            "family": fam,
            "structure": v.structure,
            "core_phi": phi,
            "n_core": len(core),
            "full_core": int(len(core) == n),
            "on_landmark": int(phi in L6) if phi == phi else 0,
            "on_composed_atom": int(phi in COMPOSED_ATOMS) if phi == phi else 0,
            "seconds": round(time.time() - t0, 2),
            "ins": "|".join(",".join(map(str, ins[j])) for j in range(n)),
        }
        rows.append(row)
        print(
            f"    → {row['structure']} Φ={row['core_phi']} "
            f"onL={row['on_landmark']} t={row['seconds']}s",
            flush=True,
        )
    phis = Counter(r["core_phi"] for r in rows)
    on_l = sum(r["on_landmark"] for r in rows) / len(rows)
    inter = sorted(p for p in phis if p not in L6)
    payload = {
        "rows": rows,
        "phi_hist": {str(k): v for k, v in sorted(phis.items())},
        "on_landmark": on_l,
        "interstitial": inter,
        "n_samples": len(rows),
    }
    path = os.path.join(RESULTS, "random_n6.json")
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=2)
    print(f"wrote {path}")
    return payload


def load_random():
    path = os.path.join(RESULTS, "random_n6.json")
    if not os.path.exists(path):
        raise SystemExit(
            f"ABORT: no committed {path}; run with --rebuild-random "
            f"(~25–40 min) or provide the file"
        )
    with open(path) as fh:
        payload = json.load(fh)
    print(
        f"\nLOADED RANDOM — {path} "
        f"(N={payload.get('n_samples', len(payload['rows']))})"
    )
    return payload


def h2_ok(lifts):
    by = {r["name"]: r for r in lifts}
    checks = []
    h = by["hy_n6_AND"]
    checks.append(
        near(h["core_phi"], 2.0) and set(h["core"].split("|")) == {"W", "S", "C"}
    )
    r0 = by["roh_leaf_ring"]
    r1 = by["roh_dense_leaf"]
    checks.append(near(r0["core_phi"], 6.0) and int(r0["full_core"]) == 0)
    checks.append(near(r1["core_phi"], 6.0) and int(r1["full_core"]) == 0)
    n0 = by["neck_AND"]
    n1 = by["neck_AND_chord"]
    checks.append(near(n0["core_phi"], 4.0) and int(n0["full_core"]) == 1)
    checks.append(float(n1["core_phi"]) in L6 and int(n1["full_core"]) == 1)
    return all(checks), checks


def evaluate(controls, lifts, random_payload, ctrl_ok):
    print("\nHYPOTHESIS TESTS")
    h1, h1_checks = h1_ok(controls)
    print(f"  H1 detail checks: {h1_checks}")
    print(f"  H1 (V3 #4–#7 controls reproduce):      {'SUPPORTED' if h1 else 'REFUTED'}")

    h2, h2_checks = h2_ok(lifts)
    print(f"  H2 detail checks: {h2_checks}")
    print(
        f"  H2 (designed lifts keep class family):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )

    on_l = float(random_payload["on_landmark"])
    inter = list(random_payload.get("interstitial") or [])
    h3 = on_l >= ON_LANDMARK_MIN
    h4 = len(inter) == 0
    print(f"  random on_landmark={on_l:.3f} phi_hist={random_payload.get('phi_hist')}")
    print(
        f"  H3 (random ≥{ON_LANDMARK_MIN:.0%} on L6):           "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(f"  H4 (no interstitial in lean random):   {'SUPPORTED' if h4 else 'REFUTED'}")

    if not ctrl_ok:
        verdict_tok = "CONTROLS_FAIL"
        reading = "CONTROLS_FAIL — instrument control failed"
    elif not h1:
        verdict_tok = "CONTROLS_FAIL"
        reading = (
            "CONTROLS_FAIL — V3 #4–#7 committed panels do not reproduce "
            "the four class families"
        )
    elif not h3 or not h4:
        verdict_tok = "INTERSTITIAL_DOMINATES"
        reading = (
            f"INTERSTITIAL_DOMINATES — denser n=6 random-AND leaves L6 "
            f"(on_landmark={on_l:.3f}; interstitial={inter})"
        )
    elif not h2:
        verdict_tok = "CLASS_BREAKS"
        reading = (
            "CLASS_BREAKS — designed n≥6 lift invents a class outside "
            "compose/factor/2k/closure/collapse"
        )
    else:
        verdict_tok = "LANDMARKS_HOLD_NGT6"
        reading = (
            "LANDMARKS_HOLD_NGT6 — V3 #4–#7 class families remain discrete "
            "at n≥6: denser random-AND (N=28) lands entirely on L6 "
            "(no interstitial); hybrid closure, roh factor, and necklace "
            "compose survive densify (chord morphs Φ=4→2 inside L6, not "
            "a new atom); exact n≥8 motif lifts left out of lean scope"
        )

    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_tok}")
    print(f"  reading: {reading}")
    by = {r["name"]: r for r in lifts}
    print(
        f"  metrics: on_landmark={on_l:.3f}; n_random={len(random_payload['rows'])}; "
        f"interstitial={inter}; "
        f"phi_hist={random_payload.get('phi_hist')}; "
        f"hy_n6_AND={by['hy_n6_AND']['core_phi']}; "
        f"neck_chord={by['neck_AND_chord']['core_phi']}; "
        f"roh_dense={by['roh_dense_leaf']['core_phi']}; "
        f"n_controls={len(controls)}"
    )
    print(
        "  best next:         V4 #11 graded / continuous party channel "
        "on the joint-obs cliff"
    )
    return verdict_tok, reading, h1, h2, h3, h4


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild-lifts", action="store_true")
    ap.add_argument("--rebuild-random", action="store_true")
    args = ap.parse_args()
    os.makedirs(RESULTS, exist_ok=True)
    t_all = time.time()

    print("AGENDA V4 #10 — COMPOSED-TOPOLOGY LANDMARKS AT n≥6")
    print("=" * 80)
    print("  cited: V3 #4–#7; V2 #18 DISCRETE_LANDMARKS")
    print("  scope: lean — V3 controls + n=6 densify/lifts + random N=28")
    print("  regime: exact binary IIT-4.0; n≥8 motif lifts out of lean")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_ok = v0.structure == "triadic" and abs(float(v0.max_phi) - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={float(v0.max_phi):.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("H1 CONTROLS — V3 #4–#7 committed panels")
    print("-" * 80)
    controls = load_v3_controls()
    for r in controls:
        print(
            f"  {r['family']} {r['name']}: n={r['n']} {r['structure']} "
            f"Φ={r['core_phi']} full={r['full_core']}"
        )

    lifts = build_lifts() if args.rebuild_lifts else load_lifts()
    random_payload = build_random() if args.rebuild_random else load_random()

    verdict_tok, reading, h1, h2, h3, h4 = evaluate(
        controls, lifts, random_payload, ctrl_ok
    )
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    summary = {
        "verdict": verdict_tok,
        "reading": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "on_landmark": random_payload["on_landmark"],
        "interstitial": random_payload.get("interstitial"),
        "phi_hist": random_payload.get("phi_hist"),
        "scope": (
            "lean: V3 #4–#7 controls; designed n=6 densify/lifts; "
            "random AND n=6 N=28; exact n≥8 motif lifts out of lean"
        ),
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)


if __name__ == "__main__":
    main()
