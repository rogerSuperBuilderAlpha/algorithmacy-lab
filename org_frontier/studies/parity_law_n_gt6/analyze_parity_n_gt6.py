"""Parity Φ = 2^(2−n) under n>6 hub embeddings (RESEARCH_AGENDA_V3 #10).

Does the parity law remain exact past the #49 n≤5 MIP window, or do
topology residuals appear when the named H-cut formula replaces exact
enumeration? Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run (default — load committed census, reprint verdict):
  python org_frontier/studies/parity_law_n_gt6/analyze_parity_n_gt6.py

Rebuild (exact Φ; n=7 takes minutes):
  python org_frontier/studies/parity_law_n_gt6/analyze_parity_n_gt6.py --rebuild
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time

import numpy as np
import pyphi
from pyphi import new_big_phi

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules, tpm_from_rules
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_parity_scaling import parity_hub

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

CONTROL_NS = (3, 4, 5)
NEW_NS = (6, 7)  # bridge n=6 + decisive n>6
PHI_TOL = max(PHI_EPS, 1e-9)


def near(a, b, eps=None):
    if eps is None:
        eps = PHI_TOL
    return abs(float(a) - float(b)) <= eps


def law(n: int) -> float:
    return float(2 ** (2 - n))


def is_H(cm: np.ndarray) -> bool:
    """Hub-preserving atomic cut: row 0 zero; all other off-diagonals one."""
    n = cm.shape[0]
    if not np.all(cm[0, :] == 0):
        return False
    for i in range(1, n):
        for j in range(n):
            want = 0 if i == j else 1
            if int(cm[i, j]) != want:
                return False
    return True


def sia_at_all_ones(n: int) -> dict:
    rules = parity_hub(n)
    labels = tuple(f"n{i}" for i in range(n))
    net = pyphi.Network(
        tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels
    )
    sub = pyphi.Subsystem(net, tuple(1 for _ in range(n)))
    t0 = time.time()
    sia = new_big_phi.sia(sub)
    cm = np.array(sia.partition._cut_matrix)
    return {
        "sia_phi": float(sia.phi),
        "H_mip": is_H(cm),
        "seconds_sia": round(time.time() - t0, 2),
    }


def run_cell(n: int, family: str) -> dict:
    labels = tuple(f"n{i}" for i in range(n))
    t0 = time.time()
    core, phi = major_complex(parity_hub(n), labels)
    t_exact = round(time.time() - t0, 2)
    pred = law(n)
    full = core is not None and len(core) == n
    hold = full and near(phi, pred)

    cut = sia_at_all_ones(n)
    cut_match = (
        near(cut["sia_phi"], phi)
        and near(cut["sia_phi"], pred)
        and cut["H_mip"]
    )
    return {
        "name": f"parity_hub_n{n}",
        "family": family,
        "n": n,
        "core_phi": float(phi),
        "law_phi": pred,
        "n_core": len(core) if core else 0,
        "full_core": full,
        "law_holds": hold,
        "seconds_exact": t_exact,
        "sia_phi": cut["sia_phi"],
        "H_mip": cut["H_mip"],
        "cut_matches_exact": cut_match,
        "seconds_sia": cut["seconds_sia"],
    }


def compute_panel():
    rows = []
    print("\nCONTROL GRID n∈{3,4,5}")
    for n in CONTROL_NS:
        print(f"  computing parity_hub n={n} ...", flush=True)
        row = run_cell(n, "control")
        rows.append(row)
        print(
            f"    → Φ={row['core_phi']:.6f} law={row['law_phi']:.6f} "
            f"H_mip={row['H_mip']} hold={row['law_holds']} "
            f"t={row['seconds_exact']+row['seconds_sia']:.1f}s",
            flush=True,
        )

    print("\nNEW GRID n∈{6,7}")
    for n in NEW_NS:
        print(f"  computing parity_hub n={n} ...", flush=True)
        row = run_cell(n, "new")
        rows.append(row)
        print(
            f"    → Φ={row['core_phi']:.6f} law={row['law_phi']:.6f} "
            f"sia={row['sia_phi']:.6f} H_mip={row['H_mip']} "
            f"cut_match={row['cut_matches_exact']} "
            f"t={row['seconds_exact']+row['seconds_sia']:.1f}s",
            flush=True,
        )

    path = os.path.join(RESULTS, "census.csv")
    fields = [
        "name", "family", "n", "core_phi", "law_phi", "n_core", "full_core",
        "law_holds", "seconds_exact", "sia_phi", "H_mip", "cut_matches_exact",
        "seconds_sia",
    ]
    os.makedirs(RESULTS, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                **r,
                "core_phi": f"{r['core_phi']:.10f}",
                "law_phi": f"{r['law_phi']:.10f}",
                "full_core": str(r["full_core"]),
                "law_holds": str(r["law_holds"]),
                "sia_phi": f"{r['sia_phi']:.10f}",
                "H_mip": str(r["H_mip"]),
                "cut_matches_exact": str(r["cut_matches_exact"]),
            })
    print(f"wrote {path}")
    return rows


def load_panel():
    path = os.path.join(RESULTS, "census.csv")
    if not os.path.exists(path):
        raise SystemExit(f"ABORT: no committed census at {path}; run with --rebuild")
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["n"] = int(r["n"])
        r["core_phi"] = float(r["core_phi"])
        r["law_phi"] = float(r["law_phi"])
        r["n_core"] = int(float(r["n_core"]))
        r["full_core"] = str(r["full_core"]).lower() == "true"
        r["law_holds"] = str(r["law_holds"]).lower() == "true"
        r["sia_phi"] = float(r["sia_phi"])
        r["H_mip"] = str(r["H_mip"]).lower() == "true"
        r["cut_matches_exact"] = str(r["cut_matches_exact"]).lower() == "true"
        r["seconds_exact"] = float(r.get("seconds_exact") or 0)
        r["seconds_sia"] = float(r.get("seconds_sia") or 0)
    print(f"\nLOADED CENSUS — {path} ({len(rows)} rows)")
    return rows


def evaluate(rows, ctrl):
    print("\nHYPOTHESIS TESTS")
    controls = [r for r in rows if r["family"] == "control"]
    news = [r for r in rows if r["family"] == "new"]

    h1 = bool(ctrl) and bool(controls) and all(r["law_holds"] for r in controls)
    print(f"  controls: {[(r['n'], round(r['core_phi'], 6), r['law_holds']) for r in controls]}")
    print(f"H1 (controls n=3..5 reproduce law):          {'SUPPORTED' if h1 else 'REFUTED'}")

    h2 = (
        bool(news)
        and any(r["n"] > 6 for r in news)
        and all(r["law_holds"] for r in news)
    )
    print(f"  new cells: {[(r['n'], round(r['core_phi'], 6), r['law_holds']) for r in news]}")
    print(f"H2 (exact law at n>6):                       {'SUPPORTED' if h2 else 'REFUTED'}")

    h3 = bool(news) and all(r["cut_matches_exact"] and r["H_mip"] for r in news)
    print(
        f"  cut/MIP: "
        f"{[(r['n'], round(r['sia_phi'], 6), r['H_mip'], r['cut_matches_exact']) for r in news]}"
    )
    print(f"H3 (H-cut MIP matches exact; no residual):   {'SUPPORTED' if h3 else 'REFUTED'}")

    if not h1:
        token = "CONTROLS_FAIL"
    elif not h2:
        token = "LAW_BREAKS_NGT6"
    elif not h3:
        token = "CUT_RESIDUAL"
    else:
        token = "LAW_HOLDS_NGT6"

    h4 = token in ("LAW_HOLDS_NGT6", "CUT_RESIDUAL", "LAW_BREAKS_NGT6")
    print(f"H4 (panel closed):                           {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")
    if token == "LAW_HOLDS_NGT6":
        print(
            "reading: LAW_HOLDS_NGT6 — parity hub Φ = 2^(2−n) remains exact at "
            "n∈{6,7} with full cores; named H-cut is the MIP and matches exact Φ "
            "(no topology residual when the cut formula stands in for enumeration)"
        )
    elif token == "CUT_RESIDUAL":
        print(
            "reading: CUT_RESIDUAL — exact Φ may track 2^(2−n), but the named "
            "H-cut is not the MIP (or cut φ diverges) at n>6; a residual appears "
            "when enumeration is replaced by the cut alone"
        )
    elif token == "LAW_BREAKS_NGT6":
        print(
            "reading: LAW_BREAKS_NGT6 — exact major-complex Φ leaves 2^(2−n) "
            "at some n≥6 hub embedding"
        )
    else:
        print(f"reading: {token}")

    print(
        "law_grid: "
        + "; ".join(
            f"n={r['n']} Φ={r['core_phi']:g} law={r['law_phi']:g} hold={r['law_holds']}"
            for r in rows
        )
    )

    summary = {
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "verdict": token,
        "n_new": len(news),
        "new_hold_all": str(all(r["law_holds"] for r in news)) if news else "False",
        "cut_match_all": str(all(r["cut_matches_exact"] for r in news)) if news else "False",
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
    print("PARITY LAW n>6 HUB EMBEDDINGS — V3 #10")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 80)

    print("INSTRUMENT CONTROL")
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl else 'FAIL'}"
    )
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
