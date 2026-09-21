"""Fielded W × Φ landmark (RESEARCH_AGENDA_V4 #6).

Does V3 #14 W_N_PREDICTS_LANDMARK survive under a fielded / noisier
instrument (rater noise, missing subscales), or does landmark
prediction collapse while verdict-class hold survives?

Exact binary IIT-4.0. Hypotheses fixed in hypotheses.md before computing.

Run:
  python org_frontier/studies/fielded_w_landmark/analyze_fielded.py
"""

from __future__ import annotations

import csv
import json
import os
import sys
import time
from itertools import combinations

import numpy as np

_REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
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

SEED = 46
N_TRIALS = 40
SIGMA = 0.20
ACC_BAR = 0.85
AUC_BAR = 0.85
W_GAP = 0.05
PHI_TOL = 1e-6


def wageman_parts(cm: np.ndarray):
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
    return float(recip), float(input_f), float(affect_f)


def w_from_parts(parts, mode: str = "full") -> float:
    recip, inp, aff = parts
    if mode == "full":
        return (recip + inp + aff) / 3.0
    if mode == "drop_recip":
        return (inp + aff) / 2.0
    if mode == "drop_input":
        return (recip + aff) / 2.0
    if mode == "drop_affect":
        return (recip + inp) / 2.0
    if mode == "recip_only":
        return recip
    raise ValueError(mode)


def noisy_w(parts, sigma: float, rng: np.random.Generator) -> float:
    recip, inp, aff = parts
    z = rng.normal(0.0, sigma, size=3)
    recip = float(np.clip(recip + z[0], 0.0, 1.0))
    inp = float(np.clip(inp + z[1], 0.0, 1.0))
    aff = float(np.clip(aff + z[2], 0.0, 1.0))
    return (recip + inp + aff) / 3.0


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


def nearest_w(w: float, protos: dict) -> str:
    return min(protos, key=lambda k: abs(protos[k] - w))


def nearest_wn(w: float, n: int, table: dict) -> str:
    cands = [lab for (nn, lab) in table if nn == n]
    return min(cands, key=lambda lab: abs(table[(n, lab)] - w))


def build_landmark_forms():
    forms = []
    for n in (3, 4, 5, 6):
        for family, builder in (
            ("hub", single_hub),
            ("ring", ring),
            ("pool", all_pool),
        ):
            if family != "hub" and n < 4:
                continue
            rules = builder(n)
            labels = tuple(f"x{i}" for i in range(n))
            cm = cm_from_rules(rules, n=n)
            core, phi = major_complex(rules, labels)
            phi_f = float(phi) if phi is not None else 0.0
            core_t = () if core is None else tuple(core)
            lab = landmark_of(family, n, phi_f, core_t)
            if lab == "OTHER":
                continue
            parts = wageman_parts(cm)
            forms.append({
                "slug": f"{family}{n}",
                "family": family,
                "n": n,
                "parts": parts,
                "W_clean": w_from_parts(parts, "full"),
                "phi": phi_f,
                "landmark": lab,
            })
    return forms


def build_verdict_holdout():
    L3 = ("W", "S", "C")
    specs = [
        ("independent", [lambda x: x[0], lambda x: x[1], lambda x: x[2]]),
        ("one_way", [lambda x: x[0], lambda x: x[0], lambda x: x[2]]),
        ("handoff", [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]]),
        ("and_chain", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]),
        ("xor_chain", [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]]),
        ("or_chain", [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]]),
    ]
    rows = []
    for slug, rules in specs:
        cm = cm_from_rules(rules, n=3)
        parts = wageman_parts(cm)
        v = verdict(rules, L3)
        rows.append({
            "slug": slug,
            "parts": parts,
            "W_clean": w_from_parts(parts, "full"),
            "triadic": int(v.structure == "triadic"),
            "structure": v.structure,
        })
    return rows


def n4_order_ok(get_w, forms_n4) -> bool:
    ordered = sorted(forms_n4, key=get_w)
    if [f["landmark"] for f in ordered] != ["HUB", "RING4", "POOL"]:
        return False
    ws = {f["landmark"]: get_w(f) for f in forms_n4}
    return (
        (ws["RING4"] - ws["HUB"]) >= W_GAP
        and (ws["POOL"] - ws["RING4"]) >= W_GAP
    )


def accuracy(forms, predict) -> float:
    if not forms:
        return float("nan")
    return float(np.mean([predict(f) == f["landmark"] for f in forms]))


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("AGENDA V4 #6 — FIELDED W × Φ LANDMARK")
    print("=" * 80)
    print("  cited: V3 #14 W_N_PREDICTS_LANDMARK; V2 #44 WAGEMAN_PREDICTS_VERDICT")
    print("  pointer: clean CM echo vs fielded / noisy survey instrument")
    print(
        f"  protocol: landmark hold acc≥{ACC_BAR}; verdict AUC≥{AUC_BAR}; "
        f"rater σ={SIGMA}; trials={N_TRIALS}; seed={SEED}"
    )
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
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
        raise SystemExit("ABORT: instrument control failed")
    print()

    forms = build_landmark_forms()
    holds = build_verdict_holdout()
    n4 = [f for f in forms if f["n"] == 4]
    proto_n4 = {f["landmark"]: f["W_clean"] for f in n4}
    proto_wn = {(f["n"], f["landmark"]): f["W_clean"] for f in forms}

    print("BUILD PANELS")
    print("-" * 80)
    print(
        f"  landmarks: {len(forms)} "
        f"(n4={len(n4)}; hubs/rings/pools across n=3..6)"
    )
    print(f"  verdict holdout: {len(holds)}")
    print()

    print("CLEAN CM ECHO (V3 #14 control)")
    print("-" * 80)
    for f in sorted(n4, key=lambda x: x["W_clean"]):
        print(
            f"  {f['slug']:8s} W={f['W_clean']:.4f}  Φ={f['phi']:.3f}  "
            f"landmark={f['landmark']}"
        )
    clean_order = n4_order_ok(lambda f: f["W_clean"], n4)
    clean_n4_acc = accuracy(
        n4, lambda f: nearest_w(f["W_clean"], proto_n4)
    )
    clean_w_acc = accuracy(
        forms, lambda f: nearest_w(f["W_clean"], proto_n4)
    )
    clean_wn_acc = accuracy(
        forms, lambda f: nearest_wn(f["W_clean"], f["n"], proto_wn)
    )
    clean_auc = roc_auc(
        [h["W_clean"] for h in holds],
        [h["triadic"] for h in holds],
    )
    print(
        f"  N4 order+gaps: {'YES' if clean_order else 'NO'}; "
        f"n4_acc={clean_n4_acc:.3f}"
    )
    print(
        f"  W-alone cross-n acc={clean_w_acc:.3f}; "
        f"(W,n) acc={clean_wn_acc:.3f}"
    )
    print(f"  verdict AUC={clean_auc:.3f}")
    h1 = (
        ctrl_ok
        and clean_order
        and clean_wn_acc >= ACC_BAR
        and clean_w_acc < ACC_BAR
        and clean_auc >= AUC_BAR
    )
    print(
        f"  H1 (clean #14 replicate):               "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print()

    print("MISSING / PARTIAL SUBSCALES (same panel, clean prototypes)")
    print("-" * 80)
    miss_accs = {}
    for mode in ("drop_recip", "drop_input", "drop_affect", "recip_only"):
        order = n4_order_ok(
            lambda f, mode=mode: w_from_parts(f["parts"], mode), n4
        )
        wn = accuracy(
            forms,
            lambda f, mode=mode: nearest_wn(
                w_from_parts(f["parts"], mode), f["n"], proto_wn
            ),
        )
        miss_accs[mode] = wn
        print(
            f"  {mode:12s}  N4_order={'YES' if order else 'NO'}  "
            f"(W,n) acc={wn:.3f}"
        )
    h4 = ctrl_ok and all(
        miss_accs[m] >= ACC_BAR
        for m in ("drop_recip", "drop_input", "drop_affect")
    )
    h5 = ctrl_ok and n4_order_ok(
        lambda f: w_from_parts(f["parts"], "recip_only"), n4
    )
    print(
        f"  H4 (any single drop keeps (W,n)≥{ACC_BAR}): "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (recip-only keeps N4 order+gaps):      "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()

    print(f"RATER NOISE (subscale Gaussian σ={SIGMA}, {N_TRIALS} trials)")
    print("-" * 80)
    wn_trials = []
    auc_trials = []
    order_trials = []
    for trial in range(N_TRIALS):
        rng = np.random.default_rng(SEED + 1000 * trial + 17)
        fw = {id(f): noisy_w(f["parts"], SIGMA, rng) for f in forms}
        rng_h = np.random.default_rng(SEED + 5000 * trial + 29)
        hw = {id(h): noisy_w(h["parts"], SIGMA, rng_h) for h in holds}

        def get_w(f, fw=fw):
            return fw[id(f)]

        order_trials.append(n4_order_ok(get_w, n4))
        wn_trials.append(
            accuracy(
                forms,
                lambda f, fw=fw: nearest_wn(fw[id(f)], f["n"], proto_wn),
            )
        )
        auc_trials.append(
            roc_auc(
                [hw[id(h)] for h in holds],
                [h["triadic"] for h in holds],
            )
        )
    field_wn = float(np.mean(wn_trials))
    field_wn_sd = float(np.std(wn_trials))
    field_auc = float(np.mean(auc_trials))
    field_auc_sd = float(np.std(auc_trials))
    field_order = float(np.mean(order_trials))
    print(f"  (W,n) acc mean±sd = {field_wn:.3f}±{field_wn_sd:.3f}")
    print(f"  verdict AUC mean±sd = {field_auc:.3f}±{field_auc_sd:.3f}")
    print(f"  N4 order+gaps rate = {field_order:.3f}")
    h2 = ctrl_ok and field_wn < ACC_BAR
    h3 = ctrl_ok and field_auc >= AUC_BAR
    print(
        f"  H2 (rater noise collapses landmark):      "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (verdict holds under same noise):      "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print()

    if not h1:
        verdict_tok = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — clean #14 replicate failed "
            f"(order={clean_order}, wn={clean_wn_acc:.3f}, "
            f"w_alone={clean_w_acc:.3f}, auc={clean_auc:.3f})"
        )
    elif h2 and h3:
        verdict_tok = "LANDMARK_COLLAPSES_VERDICT_HOLDS"
        reading = (
            f"LANDMARK_COLLAPSES_VERDICT_HOLDS — clean (W,n) holds "
            f"({clean_wn_acc:.3f}) but fielded rater noise σ={SIGMA} "
            f"collapses landmark acc to {field_wn:.3f} while verdict AUC "
            f"stays {field_auc:.3f}; missing-subscale alone does not "
            f"collapse this symmetric panel (H4={'Y' if h4 else 'N'})"
        )
    elif (not h2) and h3:
        verdict_tok = "BOTH_HOLD"
        reading = (
            f"BOTH_HOLD — fielded rater noise σ={SIGMA} leaves "
            f"(W,n) acc={field_wn:.3f} and verdict AUC={field_auc:.3f} "
            f"above bars"
        )
    elif h2 and (not h3):
        verdict_tok = "BOTH_COLLAPSE"
        reading = (
            f"BOTH_COLLAPSE — fielded rater noise σ={SIGMA} breaks "
            f"landmark ({field_wn:.3f}) and verdict ({field_auc:.3f})"
        )
    else:
        verdict_tok = "MIXED"
        reading = (
            f"MIXED — H1={h1} H2={h2} H3={h3} H4={h4} H5={h5}; "
            f"field_wn={field_wn:.3f} field_auc={field_auc:.3f}"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  clean:   order={str(clean_order):5s}  w_alone={clean_w_acc:.3f}  "
        f"wn={clean_wn_acc:.3f}  auc={clean_auc:.3f}"
    )
    print(
        f"  fielded: order_rate={field_order:.3f}  wn={field_wn:.3f}  "
        f"auc={field_auc:.3f}  (σ={SIGMA})"
    )
    print(
        f"  H1 (clean #14 replicate):               "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (rater noise collapses landmark):      "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (verdict holds under same noise):      "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (missing subscale keeps landmark):     "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (recip-only keeps N4 order):           "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_tok}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
        f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
        f"H5={('SUPPORTED' if h5 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(
        f"  metrics: clean_wn={clean_wn_acc:.3f}; clean_w={clean_w_acc:.3f}; "
        f"clean_auc={clean_auc:.3f}; field_wn={field_wn:.3f}; "
        f"field_wn_sd={field_wn_sd:.3f}; field_auc={field_auc:.3f}; "
        f"field_auc_sd={field_auc_sd:.3f}; field_order={field_order:.3f}; "
        f"drop_recip={miss_accs['drop_recip']:.3f}; "
        f"drop_input={miss_accs['drop_input']:.3f}; "
        f"drop_affect={miss_accs['drop_affect']:.3f}; "
        f"recip_only={miss_accs['recip_only']:.3f}; "
        f"sigma={SIGMA}; n_trials={N_TRIALS}"
    )
    print("  best next:         V4 #7 anti-correlated duty on logged graphs")
    print(f"  elapsed_total={round(time.time() - t0, 1)}s")
    print("=" * 80)

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = [
            "slug", "family", "n", "landmark", "phi",
            "W_clean", "reciprocity", "input", "affect",
            "W_drop_recip", "W_drop_input", "W_drop_affect", "W_recip_only",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for f in forms:
            recip, inp, aff = f["parts"]
            writer.writerow({
                "slug": f["slug"],
                "family": f["family"],
                "n": f["n"],
                "landmark": f["landmark"],
                "phi": f"{f['phi']:.6f}",
                "W_clean": f"{f['W_clean']:.6f}",
                "reciprocity": f"{recip:.6f}",
                "input": f"{inp:.6f}",
                "affect": f"{aff:.6f}",
                "W_drop_recip": f"{w_from_parts(f['parts'], 'drop_recip'):.6f}",
                "W_drop_input": f"{w_from_parts(f['parts'], 'drop_input'):.6f}",
                "W_drop_affect": f"{w_from_parts(f['parts'], 'drop_affect'):.6f}",
                "W_recip_only": f"{w_from_parts(f['parts'], 'recip_only'):.6f}",
            })

    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["regime", "metric", "value"]
        )
        writer.writeheader()
        for metric, value in [
            ("clean_order", float(clean_order)),
            ("clean_n4_acc", clean_n4_acc),
            ("clean_w_acc", clean_w_acc),
            ("clean_wn_acc", clean_wn_acc),
            ("clean_auc", clean_auc),
            ("field_wn", field_wn),
            ("field_wn_sd", field_wn_sd),
            ("field_auc", field_auc),
            ("field_auc_sd", field_auc_sd),
            ("field_order_rate", field_order),
            ("drop_recip_wn", miss_accs["drop_recip"]),
            ("drop_input_wn", miss_accs["drop_input"]),
            ("drop_affect_wn", miss_accs["drop_affect"]),
            ("recip_only_wn", miss_accs["recip_only"]),
        ]:
            writer.writerow({
                "regime": "summary",
                "metric": metric,
                "value": f"{value:.6f}",
            })

    summary = {
        "verdict": verdict_tok,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "clean_wn_acc": round(float(clean_wn_acc), 6),
        "clean_w_acc": round(float(clean_w_acc), 6),
        "clean_auc": round(float(clean_auc), 6),
        "field_wn": round(field_wn, 6),
        "field_auc": round(field_auc, 6),
        "sigma": SIGMA,
        "n_trials": N_TRIALS,
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
