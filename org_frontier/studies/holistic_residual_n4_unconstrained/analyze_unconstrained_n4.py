"""F26 asterisk fix — unconstrained n=4 holistic residual (k=2 RBN analogue of Probe 131).

Primary: N=1000 unconstrained n=4 forms, each node a random 2-input Boolean of two random others.
Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py
      python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py --rebuild
"""

import argparse
import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.multiparty.run import _fn, _rand_table
from org_frontier.studies.holistic_residual_n4.analyze_residual_n4 import (
    FEATURES,
    _dynamics,
    _strongly_connected,
    node_synergy,
)

N = 1000
SEED = 40
LABELS = ("A", "B", "C", "D")
N3_BASELINE_MISS = 196
N3_BASELINE_N = 4096
N3_BASELINE_RATE = N3_BASELINE_MISS / N3_BASELINE_N
F26_SM_RATE = 71 / 3000
HOLD_LO = 0.033
HOLD_HI = 0.063

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PANEL = os.path.join(RESULTS, "residual_panel_n4_unconstrained.csv")


def sample_unconstrained_k2(rng):
    """Each node reads two randomly chosen others via a random 2-input table."""
    rules = [None] * 4
    tables = [None] * 4  # (table, n_in)
    for j in range(4):
        others = [k for k in range(4) if k != j]
        idxs = tuple(int(x) for x in rng.choice(others, size=2, replace=False))
        t = _rand_table(rng, 2)
        rules[j] = _fn(t, idxs)
        tables[j] = (t, 2)
    return rules, tables


def instrument_control():
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    conj = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v3 = classify_rules(conj, labels=("W", "S", "C"))
    ok3 = v3.structure == "triadic" and abs(v3.max_phi - 2.0) < 1e-6
    print(f"  n=3 conjunctive triad: {v3.structure} Φ={v3.max_phi:.6f}  "
          f"{'PASS' if ok3 else 'FAIL'}")
    # n=4 k=2 ring of ANDs should be computable
    rng = np.random.default_rng(0)
    rules, _ = sample_unconstrained_k2(rng)
    v4 = classify_rules(rules, labels=LABELS)
    ok4 = v4.structure in ("triadic", "dyadic")
    print(f"  n=4 k=2 sample form:   {v4.structure} Φ={v4.max_phi:.6f}  "
          f"{'PASS' if ok4 else 'FAIL'}")
    if not (ok3 and ok4):
        raise SystemExit("ABORT: instrument control failed")
    print("  instrument control: PASS")
    print()


def build_panel(n=N, seed=SEED):
    os.makedirs(RESULTS, exist_ok=True)
    rng = np.random.default_rng(seed)
    rows = []
    start = time.time()
    print(f"BUILD PANEL — unconstrained n=4 k=2, N={n}, seed={seed}")
    print("-" * 72)
    for k in range(n):
        rules, tables = sample_unconstrained_k2(rng)
        v = classify_rules(rules, labels=LABELS)
        cm = cm_from_rules(rules)
        in_deg, out_deg = cm.sum(axis=0), cm.sum(axis=1)
        n_bidir = int(sum((in_deg[i] > 0) and (out_deg[i] > 0) for i in range(4)))
        syn = [node_synergy(t, nin) for (t, nin) in tables]
        fixed, reach, inv, per = _dynamics(rules)
        rows.append({
            "idx": k,
            "n_edges": int(cm.sum()),
            "n_bidir": n_bidir,
            "strongly_connected": int(_strongly_connected(cm)),
            "syn_sum": float(sum(syn)),
            "syn_min": float(min(syn)),
            "syn_max": float(max(syn)),
            "n_fixed": fixed,
            "n_reachable": reach,
            "invertible": inv,
            "max_period": per,
            "triadic": int(v.structure == "triadic"),
            "max_phi": f"{v.max_phi:.6f}",
        })
        if (k + 1) % 100 == 0:
            n_tri = sum(r["triadic"] for r in rows)
            print(f"  {k + 1}/{n}  ({time.time() - start:.0f}s)  triadic so far={n_tri} "
                  f"({100 * n_tri / (k + 1):.1f}%)")
    with open(PANEL, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {PANEL}  ({time.time() - start:.0f}s)")
    print()
    return rows


def load_panel():
    with open(PANEL) as fh:
        return list(csv.DictReader(fh))


def analyze(rows):
    print("F26* — UNCONSTRAINED n=4 HOLISTIC RESIDUAL vs BASELINES")
    print("-" * 72)
    X = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    y = np.array([int(r["triadic"]) for r in rows])
    n = len(y)
    n_tri = int(y.sum())
    tri_rate = n_tri / n

    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    proba = cross_val_predict(clf, X, y, cv=5, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    miss = pred != y
    n_miss = int(miss.sum())
    rate = n_miss / n

    # majority class in this sample
    maj_label = 1 if n_tri >= (n - n_tri) else 0
    majority_pred = np.full(n, maj_label, dtype=int)
    majority_miss = int((majority_pred != y).sum())
    majority_rate = majority_miss / n

    n_pred_tri = int(pred.sum())
    n_pred_dya = int((pred == 0).sum())
    h3 = (n_pred_tri > 0) and (n_pred_dya > 0)

    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    miss_tri = fn / n_tri if n_tri else float("nan")
    miss_dya = fp / (n - n_tri) if (n - n_tri) else float("nan")
    near = float(np.mean(np.abs(proba[miss] - 0.5) < 0.25)) if n_miss else float("nan")
    mean_margin = float(np.mean(np.abs(proba[miss] - 0.5))) if n_miss else float("nan")

    if HOLD_LO <= rate <= HOLD_HI:
        verdict, reading = "H0", "HOLDS"
    elif rate < HOLD_LO:
        verdict, reading = "H1", "SHRINKS"
    else:
        verdict, reading = "H2", "GROWS"

    if not h3:
        controlled = "INCONCLUSIVE (majority-floor; H3 failed)"
    else:
        controlled = f"{verdict} ({reading}) with both classes predicted"

    print(f"  sample:                     N={n}, seed={SEED}, unconstrained k=2")
    print(f"  triadic forms:              {n_tri}/{n} = {100 * tri_rate:.1f}%")
    print(f"  RF misclassified (n=4 unc): {n_miss}/{n} = {100 * rate:.1f}%")
    print(f"  n=3 baseline (Probe 131):   {N3_BASELINE_MISS}/{N3_BASELINE_N} = "
          f"{100 * N3_BASELINE_RATE:.1f}%")
    print(f"  F26 SM baseline:            71/3000 = {100 * F26_SM_RATE:.1f}%")
    print(f"  delta (unc - n3):           {100 * (rate - N3_BASELINE_RATE):+.1f} pp")
    print(f"  delta (unc - F26 SM):       {100 * (rate - F26_SM_RATE):+.1f} pp")
    print(f"  hold band:                  [{100 * HOLD_LO:.1f}%, {100 * HOLD_HI:.1f}%]")
    print(f"  majority-class miss rate:   {majority_miss}/{n} = {100 * majority_rate:.1f}% "
          f"(always-{'triadic' if maj_label else 'dyadic'})")
    print(f"  predicted triadic / dyadic: {n_pred_tri} / {n_pred_dya}")
    print(f"  H3 (predicts both classes): {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  false positives / negatives:{fp} / {fn}")
    print(f"  miss rate among triadic:    {100 * miss_tri:.1f}%")
    print(f"  miss rate among dyadic:     {100 * miss_dya:.1f}%")
    print(f"  residual near-boundary (|p-0.5|<0.25): {near:.2f}  "
          f"(mean |p-0.5|={mean_margin:.3f})")
    print(f"  raw F26* band verdict:      {verdict} — residual {reading}")
    print(f"  base-rate-controlled:       {controlled}")
    print()
    print("  note: F27 (affine = residual) remains REFUTED; not retested.")
    print("  note: full 3-input unconstrained was ~93% triadic — rejected for primary panel.")
    print()
    return {
        "n": n,
        "n_tri": n_tri,
        "tri_rate": tri_rate,
        "n_miss": n_miss,
        "rate": rate,
        "verdict": verdict,
        "reading": reading,
        "h3": h3,
        "controlled": controlled,
        "fp": fp,
        "fn": fn,
        "n_pred_tri": n_pred_tri,
        "n_pred_dya": n_pred_dya,
        "miss_tri": miss_tri,
        "miss_dya": miss_dya,
        "near": near,
        "majority_rate": majority_rate,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true",
                    help="recompute exact-Φ panel (N=1000); default loads committed panel")
    args = ap.parse_args()

    print("HOLISTIC RESIDUAL n=4 UNCONSTRAINED — F26 asterisk fix")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  universe: k=2 unconstrained n=4 (Probe-131 analogue); N=1000 seed=40")
    print("=" * 72)
    print()

    instrument_control()
    if args.rebuild or not os.path.exists(PANEL):
        rows = build_panel()
    else:
        rows = load_panel()
        print(f"LOADED PANEL — {PANEL} ({len(rows)} rows)")
        print()
    assert len(rows) == N, f"expected N={N} panel rows, got {len(rows)}"

    result = analyze(rows)
    print("=" * 72)
    print("SUMMARY")
    print(f"  n=4 unc residual rate:      {100 * result['rate']:.1f}% "
          f"({result['n_miss']}/{result['n']})")
    print(f"  n=3 residual rate:          {100 * N3_BASELINE_RATE:.1f}%")
    print(f"  F26 SM residual rate:       {100 * F26_SM_RATE:.1f}%")
    print(f"  triadic in sample:          {result['n_tri']}/{result['n']} "
          f"({100 * result['tri_rate']:.1f}%)")
    print(f"  predicted both classes:     {result['h3']}  "
          f"(pred tri={result['n_pred_tri']} dya={result['n_pred_dya']})")
    print(f"  F26* band:                  {result['verdict']} ({result['reading']})")
    print(f"  controlled verdict:         {result['controlled']}")
    print("=" * 72)


if __name__ == "__main__":
    main()
