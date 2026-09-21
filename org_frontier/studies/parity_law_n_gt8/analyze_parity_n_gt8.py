"""Parity-hub law Φ=2^(2−n) for n>8 (RESEARCH_AGENDA_V4 #9).

Does V3 #10 LAW_HOLDS_NGT6 survive n>8 via H-cut / feasible SIA, or do
topology residuals appear?

Exact binary IIT-4.0 where feasible. Lean panel: V3 #10 census controls
n∈{3..7}; named H-cut φ at n∈{8,9,10}; full SIA MIP check at n=8.
Major-complex recompute at n≥8 out of lean scope (document cut/SIA
regime). Hypotheses fixed in hypotheses.md before computing.

Run:
  python org_frontier/studies/parity_law_n_gt8/analyze_parity_n_gt8.py

Rebuild H-cut panel (fast):
  python org_frontier/studies/parity_law_n_gt8/analyze_parity_n_gt8.py --rebuild-cuts

Rebuild n=8 SIA (long, ~16 min):
  python org_frontier/studies/parity_law_n_gt8/analyze_parity_n_gt8.py --rebuild-sia
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time

import numpy as np

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO not in sys.path:
    sys.path.insert(0, _REPO)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules, tpm_from_rules
from org_frontier.probes.lib import verdict as vlib
from org_frontier.probes.probe_parity_scaling import parity_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
V3_CENSUS = os.path.join(
    _REPO,
    "org_frontier",
    "studies",
    "parity_law_n_gt6",
    "results",
    "census.csv",
)

CUT_NS = (8, 9, 10)
PHI_TOL = max(PHI_EPS, 1e-9)


def near(a, b, eps=None):
    if eps is None:
        eps = PHI_TOL
    return abs(float(a) - float(b)) <= eps


def law(n: int) -> float:
    return float(2 ** (2 - n))


def is_H(cm: np.ndarray) -> bool:
    n = cm.shape[0]
    if not np.all(cm[0, :] == 0):
        return False
    for i in range(1, n):
        for j in range(n):
            if int(cm[i, j]) != (0 if i == j else 1):
                return False
    return True


def H_matrix(n: int) -> np.ndarray:
    cm = np.zeros((n, n), dtype=int)
    for i in range(1, n):
        for j in range(n):
            if i != j:
                cm[i, j] = 1
    return cm


def load_v3_controls():
    with open(V3_CENSUS, newline="") as fh:
        rows = list(csv.DictReader(fh))
    out = []
    for r in rows:
        out.append(
            {
                "n": int(r["n"]),
                "core_phi": float(r["core_phi"]),
                "law_phi": float(r["law_phi"]),
                "sia_phi": float(r["sia_phi"]),
                "full_core": str(r["full_core"]).lower() == "true",
                "H_mip": str(r["H_mip"]).lower() == "true",
                "law_holds": str(r["law_holds"]).lower() == "true",
                "cut_matches_exact": str(r["cut_matches_exact"]).lower() == "true",
                "family": r["family"],
            }
        )
    return out


def named_H_phi(n: int) -> dict:
    import pyphi
    from pyphi import new_big_phi
    from pyphi.models.cuts import GeneralSetPartition

    pyphi.config.PROGRESS_BARS = False
    rules = parity_hub(n)
    labels = tuple(f"n{i}" for i in range(n))
    idxs = tuple(range(n))
    net = pyphi.Network(
        tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels
    )
    sub = pyphi.Subsystem(net, tuple(1 for _ in range(n)))
    t0 = time.time()
    ss = new_big_phi.system_intrinsic_information(sub)
    t_ss = time.time() - t0
    part = GeneralSetPartition(
        idxs,
        H_matrix(n),
        node_labels=net.node_labels,
        set_partition=tuple(frozenset([i]) for i in range(n)),
    )
    t1 = time.time()
    out = new_big_phi.evaluate_partition(part, sub, ss)
    phi = float(out.phi)
    pred = law(n)
    return {
        "n": n,
        "H_phi": phi,
        "law_phi": pred,
        "match": near(phi, pred),
        "seconds_ss": round(t_ss, 2),
        "seconds_eval": round(time.time() - t1, 2),
    }


def sia_all1(n: int) -> dict:
    import pyphi
    from pyphi import new_big_phi

    pyphi.config.PROGRESS_BARS = False
    rules = parity_hub(n)
    labels = tuple(f"n{i}" for i in range(n))
    net = pyphi.Network(
        tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels
    )
    sub = pyphi.Subsystem(net, tuple(1 for _ in range(n)))
    t0 = time.time()
    sia = new_big_phi.sia(sub)
    cm = np.array(sia.partition._cut_matrix)
    phi = float(sia.phi)
    pred = law(n)
    return {
        "n": n,
        "sia_phi": phi,
        "law_phi": pred,
        "H_mip": is_H(cm),
        "match": near(phi, pred),
        "seconds": round(time.time() - t0, 2),
    }


def build_cuts():
    rows = []
    print("\nNAMED H-CUT PANEL n∈{8,9,10}")
    for n in CUT_NS:
        print(f"  H-cut n={n} ...", flush=True)
        row = named_H_phi(n)
        rows.append(row)
        print(
            f"    → HΦ={row['H_phi']} law={row['law_phi']} "
            f"match={row['match']} ss_t={row['seconds_ss']}s",
            flush=True,
        )
    path = os.path.join(RESULTS, "hcut_panel.csv")
    fields = ["n", "H_phi", "law_phi", "match", "seconds_ss", "seconds_eval"]
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(
                {
                    **r,
                    "H_phi": f"{r['H_phi']:.10f}",
                    "law_phi": f"{r['law_phi']:.10f}",
                    "match": str(r["match"]),
                }
            )
    print(f"wrote {path}")
    return rows


def load_cuts():
    path = os.path.join(RESULTS, "hcut_panel.csv")
    if not os.path.exists(path):
        return build_cuts()
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        r["n"] = int(r["n"])
        r["H_phi"] = float(r["H_phi"])
        r["law_phi"] = float(r["law_phi"])
        r["match"] = str(r["match"]).lower() == "true"
        r["seconds_ss"] = float(r.get("seconds_ss") or 0)
        r["seconds_eval"] = float(r.get("seconds_eval") or 0)
    print(f"\nLOADED H-CUT PANEL — {path} ({len(rows)} rows)")
    return rows


def build_sia8():
    print("\nSIA MIP CHECK n=8 (long)")
    print("  computing full SIA at all-1s ...", flush=True)
    row = sia_all1(8)
    print(
        f"    → siaΦ={row['sia_phi']} law={row['law_phi']} "
        f"H_mip={row['H_mip']} match={row['match']} t={row['seconds']}s",
        flush=True,
    )
    path = os.path.join(RESULTS, "sia_n8.json")
    with open(path, "w") as fh:
        json.dump(row, fh, indent=2)
    print(f"wrote {path}")
    return row


def load_sia8():
    path = os.path.join(RESULTS, "sia_n8.json")
    if not os.path.exists(path):
        raise SystemExit(
            f"ABORT: no committed {path}; run with --rebuild-sia "
            f"(~16 min) or provide the file"
        )
    with open(path) as fh:
        row = json.load(fh)
    print(f"\nLOADED SIA n=8 — {path}")
    return row


def evaluate(controls, cuts, sia8, ctrl_ok):
    print("\nHYPOTHESIS TESTS")
    h1 = (
        ctrl_ok
        and bool(controls)
        and all(r["law_holds"] and r["H_mip"] and r["full_core"] for r in controls)
        and {r["n"] for r in controls} >= {3, 4, 5, 6, 7}
    )
    print(
        f"  controls: "
        f"{[(r['n'], r['core_phi'], r['law_holds'], r['H_mip']) for r in controls]}"
    )
    print(
        f"  H1 (V3 #10 controls LAW_HOLDS_NGT6):     "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )

    h2 = bool(cuts) and set(r["n"] for r in cuts) >= set(CUT_NS) and all(
        r["match"] for r in cuts
    )
    print(
        f"  H-cuts: "
        f"{[(r['n'], r['H_phi'], r['match']) for r in cuts]}"
    )
    print(
        f"  H2 (H-cut φ = law at n∈{CUT_NS}):        "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )

    h3 = (
        sia8 is not None
        and int(sia8["n"]) == 8
        and bool(sia8["H_mip"])
        and bool(sia8["match"])
    )
    print(
        f"  sia8: φ={sia8.get('sia_phi') if sia8 else None} "
        f"H_mip={sia8.get('H_mip') if sia8 else None} "
        f"match={sia8.get('match') if sia8 else None}"
    )
    print(
        f"  H3 (H is MIP at n=8; φ = law):           "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )

    h4 = h1 and h2 and h3
    print(
        f"  H4 (no residual in checked window):      "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )

    if not h1:
        verdict = "CONTROLS_FAIL"
        reading = (
            "CONTROLS_FAIL — V3 #10 census does not reproduce "
            "LAW_HOLDS_NGT6 on n∈{3..7}"
        )
    elif not h2:
        verdict = "LAW_BREAKS_NGT8"
        reading = (
            f"LAW_BREAKS_NGT8 — named H-cut φ leaves 2^(2−n) on some "
            f"n∈{CUT_NS}: {[(r['n'], r['H_phi'], r['law_phi']) for r in cuts]}"
        )
    elif not h3:
        verdict = "CUT_HOLDS_MIP_BREAKS"
        reading = (
            "CUT_HOLDS_MIP_BREAKS — H-cut φ tracks the law at n>8 but "
            "full SIA at n=8 does not return H as MIP (or φ diverges); "
            "topology residual"
        )
    else:
        verdict = "LAW_HOLDS_NGT8"
        reading = (
            "LAW_HOLDS_NGT8 — parity hub Φ=2^(2−n) survives n>8: named "
            "H-cut φ matches the law at n∈{8,9,10}; full SIA at n=8 "
            "keeps H as MIP with φ=law (no residual); major-complex "
            "census left at n≤7 (V3 #10) under the cut/SIA regime"
        )

    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict}")
    print(f"  reading: {reading}")
    cut_str = ";".join(f"n{r['n']}={r['H_phi']:g}" for r in cuts)
    print(
        f"  metrics: n8_sia={sia8['sia_phi'] if sia8 else None}; "
        f"n8_H_mip={sia8['H_mip'] if sia8 else None}; "
        f"cuts={cut_str}; "
        f"law_n8={law(8):g}; law_n9={law(9):g}; law_n10={law(10):g}; "
        f"n_controls={len(controls)}"
    )
    print("  best next:         V4 #10 composed-topology landmarks at n≥6")
    return verdict, reading, h1, h2, h3, h4


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild-cuts", action="store_true")
    ap.add_argument("--rebuild-sia", action="store_true")
    args = ap.parse_args()
    os.makedirs(RESULTS, exist_ok=True)
    t_all = time.time()

    print("AGENDA V4 #9 — PARITY-HUB LAW FOR n>8")
    print("=" * 80)
    print("  cited: V3 #10 LAW_HOLDS_NGT6; V2 #47/#49")
    print("  scope: lean — controls n≤7 + H-cut n∈{8,9,10} + SIA n=8")
    print("  regime: cut/SIA for n≥8; major-complex census stays at n≤7")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
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

    print("H1 CONTROLS — V3 #10 census n∈{3..7}")
    print("-" * 80)
    controls = load_v3_controls()
    for r in controls:
        print(
            f"  n={r['n']} Φ={r['core_phi']:g} law={r['law_phi']:g} "
            f"H_mip={r['H_mip']} hold={r['law_holds']}"
        )
    print()

    cuts = build_cuts() if args.rebuild_cuts else load_cuts()
    sia8 = build_sia8() if args.rebuild_sia else load_sia8()

    verdict, reading, h1, h2, h3, h4 = evaluate(controls, cuts, sia8, ctrl_ok)
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    summary = {
        "verdict": verdict,
        "reading": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "sia8": sia8,
        "cuts": [
            {"n": r["n"], "H_phi": r["H_phi"], "law_phi": r["law_phi"], "match": r["match"]}
            for r in cuts
        ],
        "scope": (
            "lean: V3 #10 controls n≤7; named H-cut n∈{8,9,10}; "
            "full SIA MIP check at n=8; major-complex not recomputed for n≥8"
        ),
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)


if __name__ == "__main__":
    main()
