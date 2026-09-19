"""Interior atoms at n=7–8 (RESEARCH_AGENDA_V3 #9).

Do the discrete Φ atoms of V2 #18 / interior_ring_pool at n≤6 sprout new
interior atoms at n=7–8, or only thicken existing landmark multiplicities?
Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Designed families lifted from interior_ring_pool: ring/pool anchors,
sym multihub, chordal ring, k-regular ring, lattice strip (even n).

Run (default — load committed census, reprint verdict):
  python org_frontier/studies/interior_atoms_n78/analyze_atoms_n78.py

Rebuild (exact Φ; n=7 ~8 min/cell, n=8 longer):
  python org_frontier/studies/interior_atoms_n78/analyze_atoms_n78.py --rebuild
"""

from __future__ import annotations

import argparse
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
from org_frontier.probes.probe_multihub_law import sym_multihub
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

# Prior interior landmarks from interior_ring_pool n≤6 full-core steps
L_INTERIOR_PRIOR = {6.0, 8.0, 9.0, 12.0}
RING_POLE = 4.0


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def in_prior(phi):
    return any(near(phi, a) for a in L_INTERIOR_PRIOR)


def _and_of(srcs):
    srcs = tuple(srcs)

    def f(x, srcs=srcs):
        r = 1
        for s in srcs:
            r &= x[s]
        return r

    return f


def k_regular_ring(n, d):
    rules = [None] * n
    for i in range(n):
        nbrs = []
        for off in range(1, d + 1):
            nbrs.extend([(i - off) % n, (i + off) % n])
        seen, nb = set(), []
        for x in nbrs:
            if x not in seen and x != i:
                seen.add(x)
                nb.append(x)
        rules[i] = _and_of(nb)
    return rules


def chordal_ring(n, n_chords):
    extras = {i: set() for i in range(n)}
    half = n // 2
    for c in range(n_chords):
        a = c % n
        b = (a + half) % n
        if a != b:
            extras[a].add(b)
            extras[b].add(a)
    rules = [None] * n
    for i in range(n):
        nbrs = [(i - 1) % n, (i + 1) % n] + sorted(extras[i])
        seen, nb = set(), []
        for x in nbrs:
            if x not in seen:
                seen.add(x)
                nb.append(x)
        rules[i] = _and_of(nb)
    return rules


def lattice_strip(n):
    if n % 2 != 0:
        raise ValueError("lattice_strip needs even n")
    w = n // 2
    rules = [None] * n
    for i in range(n):
        row, col = divmod(i, w)
        nbrs = [
            row * w + (col - 1) % w,
            row * w + (col + 1) % w,
            (1 - row) * w + col,
        ]
        seen, nb = set(), []
        for x in nbrs:
            if x not in seen and x != i:
                seen.add(x)
                nb.append(x)
        rules[i] = _and_of(nb)
    return rules


def run_cell(name, family, n, param, rules):
    labels = tuple(f"N{i}" for i in range(n))
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    pool_phi = float(n * (n - 1))
    full = len(core_t) == n
    interior = (
        v.structure == "triadic"
        and full
        and cp > RING_POLE + PHI_EPS
        and cp < pool_phi - PHI_EPS
    )
    prior_hit = interior and in_prior(cp)
    new_atom = interior and not in_prior(cp)
    return {
        "name": name,
        "family": family,
        "n": n,
        "param": param,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": "|".join(core_t),
        "core_phi": cp,
        "n_core": len(core_t),
        "full_core": full,
        "interior": interior,
        "prior_atom": prior_hit,
        "new_atom": new_atom,
        "seconds": round(time.time() - t0, 2),
    }


def panel_spec():
    """Lean designed panel: n=7 decisive + lean n=8 lift."""
    cells = []
    # n=7
    cells.append(("ring7", "ring", 7, 0, ring(7)))
    cells.append(("pool7", "pool", 7, 7, pool(7)))
    cells.append(("mh2_n7", "multihub", 7, 2, sym_multihub(7, 2)))
    cells.append(("mh3_n7", "multihub", 7, 3, sym_multihub(7, 3)))
    cells.append(("chord_n7_c2", "chordal", 7, 2, chordal_ring(7, 2)))
    cells.append(("chord_n7_c3", "chordal", 7, 3, chordal_ring(7, 3)))
    cells.append(("kreg_n7_d2", "kregular", 7, 2, k_regular_ring(7, 2)))
    # n=8 lean
    cells.append(("ring8", "ring", 8, 0, ring(8)))
    cells.append(("mh2_n8", "multihub", 8, 2, sym_multihub(8, 2)))
    cells.append(("chord_n8_c2", "chordal", 8, 2, chordal_ring(8, 2)))
    cells.append(("chord_n8_c3", "chordal", 8, 3, chordal_ring(8, 3)))
    cells.append(("kreg_n8_d2", "kregular", 8, 2, k_regular_ring(8, 2)))
    cells.append(("strip_n8", "lattice_strip", 8, 4, lattice_strip(8)))
    return cells


def compute_panel():
    rows = []
    print("\nDESIGNED PANEL (n=7 + lean n=8)")
    for name, family, n, param, rules in panel_spec():
        print(f"  computing {name} ...", flush=True)
        row = run_cell(name, family, n, param, rules)
        rows.append(row)
        flag = (
            "NEW" if row["new_atom"]
            else ("PRIOR" if row["prior_atom"]
                  else ("POLE" if row["full_core"] and row["structure"] == "triadic"
                        else "other"))
        )
        print(
            f"    → struct={row['structure']} coreΦ={row['core_phi']:.3f} "
            f"n_core={row['n_core']} full={row['full_core']} "
            f"{flag} t={row['seconds']}s",
            flush=True,
        )
    path = os.path.join(RESULTS, "census.csv")
    fields = [
        "name", "family", "n", "param", "structure", "whole_phi_mip",
        "core", "core_phi", "n_core", "full_core", "interior",
        "prior_atom", "new_atom", "seconds",
    ]
    os.makedirs(RESULTS, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                **r,
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core_phi": f"{r['core_phi']:.6f}",
                "full_core": str(r["full_core"]),
                "interior": str(r["interior"]),
                "prior_atom": str(r["prior_atom"]),
                "new_atom": str(r["new_atom"]),
            })
    return rows


def load_panel():
    path = os.path.join(RESULTS, "census.csv")
    if not os.path.exists(path):
        raise SystemExit(f"ABORT: no committed census at {path}; run with --rebuild")
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["n"] = int(r["n"])
        r["param"] = int(float(r["param"]))
        r["core_phi"] = float(r["core_phi"])
        r["n_core"] = int(float(r["n_core"]))
        r["whole_phi_mip"] = float(r["whole_phi_mip"])
        r["full_core"] = str(r["full_core"]).lower() == "true"
        r["interior"] = str(r["interior"]).lower() == "true"
        r["prior_atom"] = str(r["prior_atom"]).lower() == "true"
        r["new_atom"] = str(r["new_atom"]).lower() == "true"
        r["seconds"] = float(r["seconds"]) if r.get("seconds") else 0.0
    print(f"\nLOADED CENSUS — {path} ({len(rows)} rows)")
    return rows


def evaluate(rows, ctrl):
    print("\nHYPOTHESIS TESTS")
    by = {r["name"]: r for r in rows}

    ring7 = by.get("ring7")
    pool7 = by.get("pool7")
    ring8 = by.get("ring8")  # optional lean lift; not required for H1
    h1 = bool(
        ctrl
        and ring7
        and near(ring7["core_phi"], 4.0)
        and ring7["full_core"]
        and pool7
        and near(pool7["core_phi"], 42.0)
        and pool7["full_core"]
    )
    print(
        f"  ring7 Φ={ring7['core_phi'] if ring7 else None}  "
        f"pool7 Φ={pool7['core_phi'] if pool7 else None}  "
        f"ring8 Φ={ring8['core_phi'] if ring8 else 'omitted'}"
    )
    print(f"H1 (anchors ring7=4 / pool7=42):             {'SUPPORTED' if h1 else 'REFUTED'}")

    interiors = [r for r in rows if r["interior"]]
    h2 = len(interiors) >= 1
    print(f"  interiors ({len(interiors)}): "
          f"{[(r['name'], round(r['core_phi'], 3)) for r in interiors]}")
    print(f"H2 (full-core interiors exist):              {'SUPPORTED' if h2 else 'REFUTED'}")

    new_atoms = [r for r in interiors if r["new_atom"]]
    prior_atoms = [r for r in interiors if r["prior_atom"]]
    new_phi = sorted({round(r["core_phi"], 6) for r in new_atoms})
    prior_phi = sorted({round(r["core_phi"], 6) for r in prior_atoms})
    h3 = len(new_atoms) >= 1
    print(f"  prior-atom interiors Φ={prior_phi} (n={len(prior_atoms)})")
    print(f"  new-atom interiors Φ={new_phi} (n={len(new_atoms)})")
    print(f"H3 (new interior atoms sprout):              {'SUPPORTED' if h3 else 'REFUTED'}")

    if not h1:
        token = "CONTROLS_FAIL"
    elif not h2:
        token = "COLLAPSES_ONLY"
    elif h3:
        token = "SPROUTS_NEW_ATOMS"
    else:
        token = "THICKENS_LANDMARKS"

    h4 = token in ("SPROUTS_NEW_ATOMS", "THICKENS_LANDMARKS")
    print(f"H4 (panel closed):                           {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")
    if token == "SPROUTS_NEW_ATOMS":
        print(
            "reading: SPROUTS_NEW_ATOMS — designed ring–pool interiors at n=7 "
            f"yield new full-core Φ atoms {new_phi} outside L≤6 interiors "
            f"{{6,8,9,12}}; prior atoms recalled={prior_phi}"
        )
    elif token == "THICKENS_LANDMARKS":
        print(
            "reading: THICKENS_LANDMARKS — designed interiors at n=7 land only "
            f"on L≤6 interior landmarks {prior_phi}; no new atoms; multiplicities "
            "thicken with n"
        )
    elif token == "COLLAPSES_ONLY":
        print(
            "reading: COLLAPSES_ONLY — no full-core interior between ring and "
            "pool at n=7 on the designed panel"
        )
    else:
        print(f"reading: {token}")

    print(
        f"atom_law: L_prior={{6,8,9,12}}; new={new_phi}; prior_hits={prior_phi}; "
        f"n_interior={len(interiors)}"
    )

    summary = {
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "verdict": token,
        "n_interiors": len(interiors),
        "n_new_atoms": len(new_atoms),
        "new_phi_set": ";".join(str(p) for p in new_phi),
        "prior_phi_set": ";".join(str(p) for p in prior_phi),
    }
    sp = os.path.join(RESULTS, "summary.csv")
    with open(sp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)
    print(f"wrote {os.path.join(RESULTS, 'census.csv')}")
    print(f"wrote {sp}")
    return token


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--rebuild",
        action="store_true",
        help="recompute exact-Φ panel; default loads committed census",
    )
    args = ap.parse_args()

    os.makedirs(RESULTS, exist_ok=True)
    print("INTERIOR ATOMS n=7–8 — V3 #9")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 80)

    print("INSTRUMENT CONTROL")
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")

    census_path = os.path.join(RESULTS, "census.csv")
    if args.rebuild or not os.path.exists(census_path):
        rows = compute_panel()
    else:
        rows = load_panel()

    evaluate(rows, ctrl)


if __name__ == "__main__":
    main()
