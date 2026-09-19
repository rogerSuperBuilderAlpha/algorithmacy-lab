"""Noise × composed carriers (RESEARCH_AGENDA_V3 #12).

Does party-vs-mediator flip-noise still share p*=0.5 on a composed
necklace or shared-mediator span (V2 #7 SAME_THRESHOLD_DIFF_CURVE
on a single hub)?

Exact binary IIT-4.0. Hypotheses fixed in hypotheses.md.

Run (default — load committed sweep, reprint verdict):
  python org_frontier/studies/noise_composed_carriers/analyze_noise_composed.py

Rebuild (~8 min; necklace dominates):
  python org_frontier/studies/noise_composed_carriers/analyze_noise_composed.py --rebuild
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_THIRD = os.path.join(_REPO_ROOT, "third_party")
for p in (_THIRD, _REPO_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
SWEEP_PATH = os.path.join(RESULTS, "sweep.csv")
SUMMARY_PATH = os.path.join(RESULTS, "summary.json")

GRID = [0.00, 0.10, 0.20, 0.25, 0.30, 0.40, 0.45, 0.49, 0.50]
PSTAR_TOL = 0.02


def flip_noise(tpm, cols, p):
    out = tpm.copy()
    for c in cols:
        out[:, c] = (1.0 - p) * tpm[:, c] + p * (1.0 - tpm[:, c])
    return out


def hub3():
    labels = ("S", "P1", "P2")
    rules = [lambda x: x[1] & x[2], lambda x: x[0], lambda x: x[0]]
    return "hub3", labels, rules, {"mediator": [0], "party": [1]}


def shared_k2():
    labels = ("W1", "C1", "W2", "C2", "S")
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: (x[0] & x[1]) & (x[2] & x[3]),
    ]
    return "shared_k2", labels, rules, {"mediator": [4], "party": [0]}


def necklace():
    labels = ("P0", "P1", "P2", "H0", "H1", "H2")
    rules = [
        lambda x: x[5] & x[3],
        lambda x: x[3] & x[4],
        lambda x: x[4] & x[5],
        lambda x: x[0] & x[1],
        lambda x: x[1] & x[2],
        lambda x: x[2] & x[0],
    ]
    return "necklace", labels, rules, {"mediator": [3], "party": [0]}


CARRIERS = (hub3, shared_k2, necklace)


def compute_sweep() -> list[dict]:
    rows: list[dict] = []
    for builder in CARRIERS:
        name, labels, rules, loci = builder()
        clean = tpm_from_rules(rules, n=len(rules))
        cm = cm_from_rules(rules, n=len(rules))
        print(f"CARRIER {name} n={len(labels)}", flush=True)
        for locus, cols in loci.items():
            for p in GRID:
                t0 = time.time()
                v = classify(
                    flip_noise(clean, cols, p), cm, labels=labels, eps=PHI_EPS
                )
                dt = round(time.time() - t0, 2)
                rows.append(
                    {
                        "carrier": name,
                        "n": len(labels),
                        "locus": locus,
                        "p": f"{p:.2f}",
                        "structure": v.structure,
                        "phi": f"{float(v.max_phi):.8f}",
                        "seconds": dt,
                    }
                )
                print(
                    f"  {locus:<9} p={p:.2f}  {v.structure:<8} "
                    f"Φ={float(v.max_phi):.6f} ({dt}s)",
                    flush=True,
                )
    return rows


def load_sweep(path: str) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def write_sweep(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def pstar(rows: list[dict], carrier: str, locus: str) -> float | None:
    subset = sorted(
        (r for r in rows if r["carrier"] == carrier and r["locus"] == locus),
        key=lambda r: float(r["p"]),
    )
    for r in subset:
        if r["structure"] == "dyadic":
            return float(r["p"])
    return None


def max_phi_gap(rows: list[dict], carrier: str) -> float:
    med = {
        float(r["p"]): float(r["phi"])
        for r in rows
        if r["carrier"] == carrier and r["locus"] == "mediator"
    }
    party = {
        float(r["p"]): float(r["phi"])
        for r in rows
        if r["carrier"] == carrier and r["locus"] == "party"
    }
    gap = 0.0
    for p, pm in med.items():
        if p >= 0.5 or p not in party:
            continue
        gap = max(gap, abs(pm - party[p]))
    return gap


def evaluate(rows: list[dict], ctrl_ok: bool) -> str:
    carriers = ("hub3", "shared_k2", "necklace")
    composed = ("shared_k2", "necklace")

    print()
    print("P* TABLE")
    print(f"  {'carrier':<12}{'p*_med':>8}{'p*_party':>10}{'|Δ|':>8}{'max|ΔΦ|':>10}")
    stats = {}
    for c in carriers:
        pm = pstar(rows, c, "mediator")
        pp = pstar(rows, c, "party")
        gap = (
            abs(pm - pp)
            if pm is not None and pp is not None
            else float("nan")
        )
        dphi = max_phi_gap(rows, c)
        stats[c] = {
            "p_med": pm,
            "p_party": pp,
            "gap": gap,
            "max_phi_gap": dphi,
        }
        print(f"  {c:<12}{pm!s:>8}{pp!s:>10}{gap:>8.2f}{dphi:>10.4f}")

    h1 = (
        ctrl_ok
        and stats["hub3"]["p_med"] == 0.5
        and stats["hub3"]["p_party"] == 0.5
    )
    h2 = all(
        stats[c]["p_med"] is not None
        and stats[c]["p_party"] is not None
        and abs(stats[c]["p_med"] - stats[c]["p_party"]) < PSTAR_TOL
        for c in composed
    )
    h3 = all(
        stats[c]["p_med"] == 0.5 and stats[c]["p_party"] == 0.5
        for c in composed
    )

    print()
    print("HYPOTHESES")
    print(f"H1 (hub3 control p*=0.5 both seats):     {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 (composed seats share p*):            {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"H3 (composed p* stays 0.5):              {'SUPPORTED' if h3 else 'REFUTED'}")

    if not h1:
        verdict = "CONTROLS_FAIL"
        reading = (
            "CONTROLS_FAIL — hub3 control failed to reproduce V2 #7 "
            "shared p*=0.5"
        )
    elif not h2:
        verdict = "COMPOSE_SPLITS_PSTAR"
        reading = (
            "COMPOSE_SPLITS_PSTAR — necklace or shared-mediator span "
            "separates party vs mediator collapse thresholds"
        )
    elif not h3:
        verdict = "COMPOSE_SHIFTS_PSTAR"
        reading = (
            "COMPOSE_SHIFTS_PSTAR — seats still match under composition "
            "but leave the coin-flip p*=0.5"
        )
    else:
        verdict = "SAME_PSTAR_COMPOSED"
        reading = (
            "SAME_PSTAR_COMPOSED — party and mediator flip-noise still "
            "share p*=0.5 on necklace and shared-mediator span; V2 #7 "
            "coin-flip threshold survives composition"
        )

    h4 = verdict in (
        "SAME_PSTAR_COMPOSED",
        "COMPOSE_SPLITS_PSTAR",
        "COMPOSE_SHIFTS_PSTAR",
    )
    print(f"H4 (panel closed):                       {'SUPPORTED' if h4 else 'REFUTED'}")

    print()
    print("STATUS")
    print(f"  control: {'PASS' if ctrl_ok else 'FAIL'}")
    print(f"  verification grid: {'PASS' if h1 and h2 and h3 else 'FAIL'}")
    print("  best next:         #13 validation bridge (weakest Boolean render)")
    print(f"verdict: {verdict}")
    print(f"reading: {reading}")
    print(
        "pstar_grid: "
        + "; ".join(
            f"{c} med={stats[c]['p_med']} party={stats[c]['p_party']}"
            for c in carriers
        )
    )
    print()
    print(f"  faithful triad: triadic Φ=2.000000  {'PASS' if ctrl_ok else 'FAIL'}")
    print(f"H1 (hub3 control p*=0.5 both seats):     {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 (composed seats share p*):            {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"H3 (composed p* stays 0.5):              {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"H4 (panel closed):                       {'SUPPORTED' if h4 else 'REFUTED'}")

    summary = {
        "verdict": verdict,
        "reading": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "control_ok": ctrl_ok,
        "stats": {
            c: {
                "p_med": stats[c]["p_med"],
                "p_party": stats[c]["p_party"],
                "gap": stats[c]["gap"],
                "max_phi_gap": stats[c]["max_phi_gap"],
            }
            for c in carriers
        },
    }
    with open(SUMMARY_PATH, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"wrote {SUMMARY_PATH}")
    return verdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--rebuild",
        action="store_true",
        help="recompute exact-Φ sweep (necklace ~minutes)",
    )
    args = ap.parse_args()

    os.makedirs(RESULTS, exist_ok=True)
    t0 = time.time()
    print("NOISE × COMPOSED CARRIERS — V3 #12")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 72)
    print("  noise: flip-noise on mediator vs party TPM columns")
    print("  carriers: hub3 control; shared_k2 span; AND necklace")
    print("  instrument: exact binary IIT-4.0 classify")
    print()

    print("INSTRUMENT CONTROL")
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_ok = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-9
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")

    if args.rebuild or not os.path.exists(SWEEP_PATH):
        print()
        print("REBUILD SWEEP")
        rows = compute_sweep()
        write_sweep(SWEEP_PATH, rows)
        print(f"  wrote {SWEEP_PATH}")
    else:
        rows = load_sweep(SWEEP_PATH)
        print()
        print(f"LOADED SWEEP ({len(rows)} rows from results/sweep.csv)")

    evaluate(rows, ctrl_ok)
    print(f"elapsed {time.time() - t0:.1f}s")
    print("=" * 72)


if __name__ == "__main__":
    main()
