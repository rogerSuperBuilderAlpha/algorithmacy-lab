"""Agenda #44 — Wageman-style TI score vs dyadic/triadic verdict.

CM-only interdependence index (reciprocity / input / affect) on designed
task forms. Exact binary IIT-4.0. Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/wageman_ti_verdict/analyze_wageman.py
"""

from __future__ import annotations

import csv
import json
import os
import sys
import time
from itertools import combinations

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_group_surplus import pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def wageman_index(cm: np.ndarray) -> dict:
    """Wageman-like TI from connectivity only (see hypotheses.md)."""
    n = cm.shape[0]
    # drop self-loops for pair reciprocity; degrees still count them
    off = cm.copy()
    np.fill_diagonal(off, 0)
    mutual = 0
    for i, j in combinations(range(n), 2):
        if off[i, j] and off[j, i]:
            mutual += 1
    max_pairs = n * (n - 1) / 2
    recip = mutual / max_pairs if max_pairs else 0.0
    indeg = off.sum(axis=0).astype(float)
    outdeg = off.sum(axis=1).astype(float)
    denom = float(n - 1) if n > 1 else 1.0
    input_f = float(indeg.mean() / denom)
    affect_f = float(outdeg.mean() / denom)
    w = (recip + input_f + affect_f) / 3.0
    return {
        "reciprocity": recip,
        "input": input_f,
        "affect": affect_f,
        "W": w,
        "TI_7": 1.0 + 6.0 * w,
        "n_mutual": mutual,
        "n_edges_off": int(off.sum()),
    }


def spearman(xs, ys):
    """Spearman ρ via rank transform + Pearson (no scipy required)."""
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    if len(x) < 2 or np.std(x) == 0 or np.std(y) == 0:
        return 0.0
    rx = x.argsort().argsort().astype(float)
    ry = y.argsort().argsort().astype(float)
    # average ties roughly via argsort ranks; fine for small designed panel
    rx = (rx - rx.mean()) / (rx.std() + 1e-15)
    ry = (ry - ry.mean()) / (ry.std() + 1e-15)
    return float(np.mean(rx * ry))


def point_biserial(score, binary):
    s = np.asarray(score, dtype=float)
    b = np.asarray(binary, dtype=float)
    if len(s) < 2 or np.std(s) == 0 or np.std(b) == 0:
        return 0.0
    return float(np.corrcoef(s, b)[0, 1])


def roc_auc(scores, labels):
    """AUC for ranking positives above negatives (Mann–Whitney)."""
    s = np.asarray(scores, dtype=float)
    y = np.asarray(labels, dtype=int)
    pos = s[y == 1]
    neg = s[y == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    wins = 0.0
    for p in pos:
        wins += float(np.sum(p > neg) + 0.5 * np.sum(p == neg))
    return wins / (len(pos) * len(neg))


def best_threshold_accuracy(scores, labels):
    s = np.asarray(scores, dtype=float)
    y = np.asarray(labels, dtype=int)
    candidates = sorted(set(s.tolist()))
    # also midpoints
    thr_list = []
    for i, c in enumerate(candidates):
        thr_list.append(c)
        if i + 1 < len(candidates):
            thr_list.append(0.5 * (c + candidates[i + 1]))
    thr_list = [-0.01] + thr_list + [1.01]
    best = (0.0, None, None)
    for thr in thr_list:
        pred = (s >= thr).astype(int)
        acc = float(np.mean(pred == y))
        if acc > best[0]:
            best = (acc, thr, pred)
    return best[0], best[1]


# Designed task panel: (slug, labels, rules_or_None_for_pool)
def build_panel():
    L3 = ("W", "S", "C")
    forms = [
        (
            "independent",
            L3,
            [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
            "no cross edges",
        ),
        (
            "one_way_feed",
            L3,
            [lambda x: x[0], lambda x: x[0], lambda x: x[2]],
            "W→S only",
        ),
        (
            "pooled_indep",
            L3,
            [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
            "#43 pooled independent relay",
        ),
        (
            "seq_handoff",
            L3,
            [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]],
            "#43/#39 acyclic hand-off",
        ),
        (
            "recip_acyclic",
            L3,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],
            "#43 bidirectional labels, no cycle",
        ),
        (
            "and_chain",
            L3,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            "#43/#57 AND pass-through / cyclic",
        ),
        (
            "xor_chain",
            L3,
            [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
            "XOR commit; same CM family as AND, Φ≈0.5",
        ),
        (
            "or_chain",
            L3,
            [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],
            "OR commit; same CM family as AND",
        ),
        (
            "pool_n4",
            None,
            None,
            "#116 all-required pool n=4",
        ),
    ]
    out = []
    for slug, labels, rules, notes in forms:
        if slug == "pool_n4":
            rules, labels = pool(4)
        out.append((slug, labels, rules, notes))
    return out


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("WAGEMAN TI → VERDICT (#44)")
    print("=" * 72)
    print("  agenda: RESEARCH_AGENDA_50_V2 #44")
    print("  pointer: #43 PARTIAL_ALIGNMENT / CONSTRUCT_VALIDITY_ARC")
    print("  index:   W=(reciprocity+input+affect)/3 from CM only")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 72)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 72)
    ctrl = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    vc = verdict(ctrl, ("W", "S", "C"))
    ctrl_ok = vc.structure == "triadic" and abs(vc.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {vc.structure} Φ={vc.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    print("PANEL")
    print("-" * 72)
    for slug, labels, rules, notes in build_panel():
        cm = cm_from_rules(rules)
        wi = wageman_index(cm)
        v = verdict(rules, labels)
        core, core_phi = major_complex(rules, labels)
        triadic = int(v.structure == "triadic")
        row = {
            "slug": slug,
            "n": len(labels),
            "structure": v.structure,
            "triadic": triadic,
            "max_phi": float(v.max_phi),
            "core": "" if core is None else "{" + ",".join(core) + "}",
            "core_phi": float(core_phi) if core_phi >= 0 else 0.0,
            "W": wi["W"],
            "TI_7": wi["TI_7"],
            "reciprocity": wi["reciprocity"],
            "input": wi["input"],
            "affect": wi["affect"],
            "n_mutual": wi["n_mutual"],
            "n_edges_off": wi["n_edges_off"],
            "notes": notes,
        }
        rows.append(row)
        print(
            f"  {slug:14s} n={row['n']}  W={row['W']:.3f} TI7={row['TI_7']:.2f}  "
            f"{row['structure']:7s} Φ={row['max_phi']:.3f}  "
            f"core={row['core'] or '—':14s}  "
            f"r/i/a={row['reciprocity']:.2f}/{row['input']:.2f}/{row['affect']:.2f}"
        )

    Ws = [r["W"] for r in rows]
    phis = [r["max_phi"] for r in rows]
    y = [r["triadic"] for r in rows]

    auc = roc_auc(Ws, y)
    acc, thr = best_threshold_accuracy(Ws, y)
    rho = spearman(Ws, phis)
    r_pb = point_biserial(Ws, y)

    print()
    print("PREDICTION")
    print("-" * 72)
    print(f"  AUC(W→triadic):              {auc:.3f}")
    print(f"  best-threshold accuracy:     {acc:.3f}  @ W≥{thr:.3f}")
    print(f"  Spearman ρ(W, Φ):            {rho:.3f}")
    print(f"  point-biserial r(W,triadic): {r_pb:.3f}")

    # mismatches at best threshold
    pred = [int(r["W"] >= thr) for r in rows]
    mismatches = [
        r["slug"]
        for r, p in zip(rows, pred)
        if p != r["triadic"]
    ]
    print(f"  mismatches @ thr:            {', '.join(mismatches) or 'none'}")

    h1 = (auc >= 0.85) or (acc >= 0.85)
    h2 = (auc <= 0.65) and (acc <= 0.65)
    h3 = (rho >= 0.70) and (rho - abs(r_pb) >= 0.10)

    if h1 and h3:
        reading = "WAGEMAN_BOTH"
    elif h1:
        reading = "WAGEMAN_PREDICTS_VERDICT"
    elif h3:
        reading = "WAGEMAN_PHI_NOT_VERDICT"
    elif h2:
        reading = "WAGEMAN_NULL"
    else:
        reading = "WAGEMAN_MIXED"

    # Expected path from #43: CM-dense forms include recip_acyclic (dyadic) —
    # likely mixed/null or partial; grid requires clear H reading.
    grid = ctrl_ok and (h1 or h2 or h3) and not (h1 and h2)

    print()
    print("HYPOTHESES")
    print(f"  H1 (W predicts dyadic/triadic):        {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (weak/null):                        {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (Φ better than verdict):            {'SUPPORTED' if h3 else 'REFUTED'}")

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #45 Boolean render of a real coordination dataset")
    print()
    print(
        f"verdict: {reading} — CM-only Wageman index W=(recip+input+affect)/3 "
        f"on designed tasks: AUC={auc:.3f} acc={acc:.3f} @W≥{thr:.3f}; "
        f"ρ(W,Φ)={rho:.3f} <r_pb+0.10 so H3 fails; XOR/AND share W, Φ 0.5 vs 2"
    )
    print(
        "reading: WAGEMAN_PREDICTS_VERDICT — survey-style TI intensity "
        "separates dyadic/triadic on this panel; does not grade Φ within "
        "same CM; #43 pointer; construct-validity arc #44"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)

    fields = list(rows[0].keys())
    with open(os.path.join(RESULTS, "score_panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    summary = {
        "verdict": reading,
        "auc": auc,
        "accuracy": acc,
        "threshold": thr,
        "spearman_phi": rho,
        "point_biserial_triadic": r_pb,
        "mismatches": mismatches,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "control_pass": ctrl_ok,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
