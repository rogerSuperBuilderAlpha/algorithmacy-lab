"""Wageman W × Φ landmark (RESEARCH_AGENDA_V3 #14).

Can survey-style W (V2 #44) paired with an in-silico form predict
ring-4 vs hub-(n−1) vs pool landmarks — not only dyadic/triadic?

Exact binary IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:
  python org_frontier/studies/wageman_phi_landmark/analyze_wageman_landmark.py
"""

from __future__ import annotations

import csv
import json
import os
import sys
import time
from itertools import combinations

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import pool as all_pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-6
W_GAP = 0.05
ACC_BAR = 0.85
AUC_BAR = 0.85


def wageman_index(cm: np.ndarray) -> dict:
    n = cm.shape[0]
    off = cm.copy()
    np.fill_diagonal(off, 0)
    mutual = sum(
        1 for i, j in combinations(range(n), 2) if off[i, j] and off[j, i]
    )
    max_pairs = n * (n - 1) / 2.0
    recip = mutual / max_pairs if max_pairs else 0.0
    denom = float(n - 1) if n > 1 else 1.0
    input_f = float(off.sum(axis=0).mean() / denom)
    affect_f = float(off.sum(axis=1).mean() / denom)
    w = (recip + input_f + affect_f) / 3.0
    return {
        "reciprocity": float(recip),
        "input": input_f,
        "affect": affect_f,
        "W": float(w),
        "TI_7": 1.0 + 6.0 * float(w),
        "n_edges": int(off.sum()),
    }


def landmark_of(family: str, n: int, phi: float, core) -> str:
    if core is None or len(core) != n:
        return "OTHER"
    if family == "hub" and abs(phi - (n - 1)) < PHI_TOL:
        return "HUB"
    if family == "ring" and n >= 4 and abs(phi - 4.0) < PHI_TOL:
        return "RING4"
    if family == "pool" and abs(phi - n * (n - 1)) < PHI_TOL:
        return "POOL"
    return "OTHER"


def roc_auc(scores, labels) -> float:
    s = np.asarray(scores, dtype=float)
    y = np.asarray(labels, dtype=int)
    pos, neg = s[y == 1], s[y == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    wins = 0.0
    for p in pos:
        wins += float(np.sum(p > neg) + 0.5 * np.sum(p == neg))
    return wins / (len(pos) * len(neg))


def nearest_proto(w: float, protos: dict) -> str:
    return min(protos, key=lambda k: abs(protos[k] - w))


def accuracy(rows, predict):
    labs = [r for r in rows if r["landmark"] != "OTHER"]
    if not labs:
        return 0.0, 0, 0
    ok = sum(1 for r in labs if predict(r) == r["landmark"])
    return ok / len(labs), ok, len(labs)


def eval_form(slug, family, panel, rules, labels, notes):
    n = len(labels)
    cm = cm_from_rules(rules, n=n)
    widx = wageman_index(cm)
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    phi_f = float(phi) if phi is not None and float(phi) >= 0 else 0.0
    core_t = () if core is None else tuple(core)
    return {
        "slug": slug,
        "family": family,
        "panel": panel,
        "n": n,
        "W": widx["W"],
        "TI_7": widx["TI_7"],
        "reciprocity": widx["reciprocity"],
        "input": widx["input"],
        "affect": widx["affect"],
        "n_edges": widx["n_edges"],
        "structure": v.structure,
        "triadic": int(v.structure == "triadic"),
        "phi": phi_f,
        "core": "{" + ",".join(core_t) + "}" if core_t else "",
        "core_size": len(core_t),
        "landmark": landmark_of(family, n, phi_f, core_t),
        "notes": notes,
    }


def build_rows():
    rows = []
    families = (
        ("hub", single_hub, "conjunctive hub Φ=n−1"),
        ("ring", ring, "ring landmark Φ=4"),
        ("pool", all_pool, "all-required pool Φ=n(n−1)"),
    )

    for family, builder, note in families:
        rules = builder(4)
        labels = tuple(f"x{i}" for i in range(4))
        rows.append(eval_form(f"{family}4", family, "n4_triad", rules, labels, note))

    for n in (3, 4, 5, 6):
        for family, builder, note in families:
            if family != "hub" and n < 4:
                continue
            rules = builder(n)
            labels = tuple(f"x{i}" for i in range(n))
            rows.append(
                eval_form(f"{family}{n}", family, "cross_n", rules, labels, note)
            )

    L3 = ("W", "S", "C")
    holdout = [
        ("independent", [lambda x: x[0], lambda x: x[1], lambda x: x[2]], "no edges"),
        ("one_way_feed", [lambda x: x[0], lambda x: x[0], lambda x: x[2]], "W→S"),
        (
            "seq_handoff",
            [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]],
            "acyclic hand-off",
        ),
        (
            "and_chain",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            "AND cyclic",
        ),
        (
            "xor_chain",
            [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
            "XOR same CM",
        ),
        (
            "or_chain",
            [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],
            "OR same CM",
        ),
    ]
    for slug, rules, notes in holdout:
        rows.append(eval_form(slug, "holdout", "verdict", rules, L3, notes))
    return rows


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("WAGEMAN W × Φ LANDMARK — V3 #14")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 72)
    print("  index: W=(reciprocity+input+affect)/3 from CM (V2 #44)")
    print("  landmarks: HUB Φ=n−1; RING4 Φ=4; POOL Φ=n(n−1)")
    print("  instrument: exact binary IIT-4.0")
    print("  pairing: survey-style W (+n) with in-silico Boolean form")
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 72)
    ctrl = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v0 = verdict(ctrl, ("W", "S", "C"))
    ctrl_ok = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-9
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    for family, builder, target in (
        ("hub", single_hub, 3.0),
        ("ring", ring, 4.0),
        ("pool", all_pool, 12.0),
    ):
        core, phi = major_complex(builder(4), tuple(f"x{i}" for i in range(4)))
        ok = (
            core is not None
            and len(core) == 4
            and abs(float(phi) - target) < PHI_TOL
        )
        ctrl_ok = ctrl_ok and ok
        print(
            f"  landmark {family}4: Φ={float(phi):.3f} (expect {target:g})  "
            f"{'PASS' if ok else 'FAIL'}"
        )
    if not ctrl_ok:
        raise SystemExit("ABORT: controls failed")
    print()

    rows = build_rows()
    n4 = [r for r in rows if r["panel"] == "n4_triad"]
    cross = [r for r in rows if r["panel"] == "cross_n"]
    hold = [r for r in rows if r["panel"] == "verdict"]

    print("N4 LANDMARK TRIAD")
    print("-" * 72)
    for r in sorted(n4, key=lambda x: x["W"]):
        print(
            f"  {r['slug']:8s} W={r['W']:.4f}  Φ={r['phi']:.3f}  "
            f"landmark={r['landmark']}"
        )
    ws = {r["landmark"]: r["W"] for r in n4}
    ordered = [r["landmark"] for r in sorted(n4, key=lambda x: x["W"])]
    order_ok = (
        ordered == ["HUB", "RING4", "POOL"]
        and (ws["RING4"] - ws["HUB"]) >= W_GAP
        and (ws["POOL"] - ws["RING4"]) >= W_GAP
    )
    protos_n4 = dict(ws)
    acc_n4, ok_n4, tot_n4 = accuracy(
        n4, lambda r: nearest_proto(r["W"], protos_n4)
    )
    h1 = order_ok and acc_n4 == 1.0
    print(
        f"  order hub<ring<pool gaps≥{W_GAP}: {'YES' if order_ok else 'NO'}; "
        f"acc={ok_n4}/{tot_n4}"
    )
    print(f"  H1: {'SUPPORTED' if h1 else 'REFUTED'}")
    print()

    print("CROSS-N LANDMARKS")
    print("-" * 72)
    for r in cross:
        print(
            f"  {r['slug']:8s} W={r['W']:.4f}  Φ={r['phi']:.3f}  "
            f"landmark={r['landmark']}"
        )
    acc_w, ok_w, tot_w = accuracy(
        cross, lambda r: nearest_proto(r["W"], protos_n4)
    )
    h2 = acc_w < ACC_BAR
    print(f"  W-alone acc vs n4 prototypes: {ok_w}/{tot_w} = {acc_w:.3f}")
    for r in cross:
        if r["landmark"] == "OTHER":
            continue
        pred = nearest_proto(r["W"], protos_n4)
        if pred != r["landmark"]:
            print(
                f"  miss: {r['slug']} W={r['W']:.4f} true={r['landmark']} "
                f"pred={pred}"
            )
    print(f"  H2 (acc < {ACC_BAR}): {'SUPPORTED' if h2 else 'REFUTED'}")

    table = {
        (r["n"], r["landmark"]): r["W"]
        for r in cross
        if r["landmark"] != "OTHER"
    }

    def pred_wn(r):
        cands = [lab for (n, lab) in table if n == r["n"]]
        if not cands:
            return "OTHER"
        return min(cands, key=lambda lab: abs(table[(r["n"], lab)] - r["W"]))

    acc_wn, ok_wn, tot_wn = accuracy(cross, pred_wn)
    h3 = acc_wn >= ACC_BAR
    print(f"  (W,n) acc: {ok_wn}/{tot_wn} = {acc_wn:.3f}")
    print(f"  H3 (acc ≥ {ACC_BAR}): {'SUPPORTED' if h3 else 'REFUTED'}")
    print()

    print("VERDICT HOLD (#44)")
    print("-" * 72)
    for r in hold:
        print(
            f"  {r['slug']:14s} W={r['W']:.3f}  {r['structure']:<8} "
            f"Φ={r['phi']:.3f}"
        )
    auc = roc_auc([r["W"] for r in hold], [r["triadic"] for r in hold])
    h4 = auc >= AUC_BAR
    print(f"  AUC(W→triadic) = {auc:.3f}")
    print(f"  H4 (AUC ≥ {AUC_BAR}): {'SUPPORTED' if h4 else 'REFUTED'}")
    print()

    if not ctrl_ok:
        verdict_tok = "CONTROLS_FAIL"
        reading = "CONTROLS_FAIL — instrument or landmark controls failed"
    elif h1 and h2 and h3 and h4:
        verdict_tok = "W_N_PREDICTS_LANDMARK"
        reading = (
            "W_N_PREDICTS_LANDMARK — survey-style W paired with form size n "
            "predicts ring-4 / hub-(n−1) / pool landmarks; at n=4 W alone "
            "orders hub<ring<pool; across n, W alone collides and needs n; "
            "dyadic/triadic verdict hold from V2 #44 intact"
        )
    elif h1 and (not h2) and h4:
        verdict_tok = "W_ALONE_PREDICTS_LANDMARK"
        reading = (
            "W_ALONE_PREDICTS_LANDMARK — W alone predicts landmark even "
            "across sizes; verdict hold intact"
        )
    elif (not h1) and h4:
        verdict_tok = "W_VERDICT_NOT_LANDMARK"
        reading = (
            "W_VERDICT_NOT_LANDMARK — W still predicts verdict class but "
            "not Φ landmark"
        )
    elif not h4:
        verdict_tok = "W_NULL"
        reading = "W_NULL — W fails verdict hold on the paired panel"
    else:
        verdict_tok = "MIXED"
        reading = "MIXED — see hypothesis table"

    h5 = verdict_tok in (
        "W_N_PREDICTS_LANDMARK",
        "W_ALONE_PREDICTS_LANDMARK",
        "W_VERDICT_NOT_LANDMARK",
        "W_NULL",
    )

    print("HYPOTHESES")
    print(
        f"H1 (n=4 W separates hub<ring<pool):      "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"H2 (W alone fails cross-n, acc<{ACC_BAR}):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"H3 ((W,n) recovers landmark cross-n):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"H4 (W→triadic verdict hold AUC≥{AUC_BAR}):  "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"H5 (panel closed):                       "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()
    print("STATUS")
    print(f"  control: {'PASS' if ctrl_ok else 'FAIL'}")
    grid = ctrl_ok and h1 and h2 and h3 and h4
    print(f"  verification grid: {'PASS' if grid else 'FAIL'}")
    print("  best next:         #15 topology-aware imputer (role-gated collapse)")
    print(f"verdict: {verdict_tok}")
    print(f"reading: {reading}")
    print(
        f"metrics: n4_acc={acc_n4:.3f}; w_alone_acc={acc_w:.3f}; "
        f"wn_acc={acc_wn:.3f}; verdict_auc={auc:.3f}"
    )
    print()
    print(f"  faithful triad: triadic Φ=2.000000  {'PASS' if ctrl_ok else 'FAIL'}")
    print(
        f"H1 (n=4 W separates hub<ring<pool):      "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"H2 (W alone fails cross-n, acc<{ACC_BAR}):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"H3 ((W,n) recovers landmark cross-n):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"H4 (W→triadic verdict hold AUC≥{AUC_BAR}):  "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"H5 (panel closed):                       "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "verdict": verdict_tok,
        "reading": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "control_ok": ctrl_ok,
        "n4_W": ws,
        "acc_n4": acc_n4,
        "acc_w_alone": acc_w,
        "acc_wn": acc_wn,
        "verdict_auc": auc,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote results/ ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
