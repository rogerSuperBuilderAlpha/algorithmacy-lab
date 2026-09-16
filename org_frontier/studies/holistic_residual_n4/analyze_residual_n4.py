"""Build the n=4 Probe-125-style cheap-feature panel and measure the holistic residual (F26).

Sampling matches probe_n4_census: N=3000 strict-mediation n=4 forms, seed 4.
Features match Probe 125/131; RF protocol matches Probe 131.
Hypotheses fixed in hypotheses.md before this run.

Run:  python org_frontier/studies/holistic_residual_n4/analyze_residual_n4.py
      python org_frontier/studies/holistic_residual_n4/analyze_residual_n4.py --rebuild
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

N = 3000
SEED = 4
LABELS = ("W", "S", "C1", "C2")
N3_BASELINE_MISS = 196
N3_BASELINE_N = 4096
N3_BASELINE_RATE = N3_BASELINE_MISS / N3_BASELINE_N  # 0.0478515625 ≈ 4.8%
HOLD_LO = 0.033
HOLD_HI = 0.063

FEATURES = ("n_edges", "n_bidir", "strongly_connected", "syn_sum", "syn_min", "syn_max",
            "n_fixed", "n_reachable", "invertible", "max_period")

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PANEL = os.path.join(RESULTS, "residual_panel_n4.csv")


def _strongly_connected(cm):
    n = cm.shape[0]

    def reach(s):
        seen, st = set(), [s]
        while st:
            u = st.pop()
            for v in range(n):
                if cm[u, v] and v not in seen:
                    seen.add(v)
                    st.append(v)
        return seen

    return all(set(range(n)) - {s} <= reach(s) for s in range(n))


def _pairwise_interaction(table, n_in, i, j):
    """How much input i's marginal effect changes when co-input j flips (avg over other bits)."""
    others = [b for b in range(n_in) if b not in (i, j)]
    n_ctx = 1 << len(others)
    s0 = s1 = 0.0
    for ctx in range(n_ctx):
        base = 0
        for k, b in enumerate(others):
            if (ctx >> k) & 1:
                base |= 1 << b
        s0 += float(table[base] != table[base | (1 << i)])
        s1 += float(table[base | (1 << j)] != table[base | (1 << j) | (1 << i)])
    return abs(s0 / n_ctx - s1 / n_ctx)


def node_synergy(table, n_in):
    """Probe-125-style synergy: max pairwise co-input interaction; 0 for unary reads."""
    if n_in < 2:
        return 0.0
    return max(
        _pairwise_interaction(table, n_in, i, j)
        for i in range(n_in) for j in range(n_in) if i != j
    )


def _dynamics(rules):
    n = len(rules)
    n_states = 1 << n
    states = [tuple((s >> i) & 1 for i in range(n)) for s in range(n_states)]
    nxt = {s: tuple(int(rules[i](s)) for i in range(n)) for s in states}
    fixed = sum(nxt[s] == s for s in states)
    reachable = len(set(nxt.values()))
    invertible = int(reachable == n_states)
    periods = []
    for s in states:
        seen, cur = [], s
        while cur not in seen:
            seen.append(cur)
            cur = nxt[cur]
        periods.append(len(seen) - seen.index(cur))
    return fixed, reachable, invertible, max(periods)


def sample_form_with_tables(rng):
    """Strict-mediation n=4 draw; RNG call order matches multiparty.scaling.sample_form."""
    outer = [0, 2, 3]
    ts = _rand_table(rng, 3)
    tables = [None] * 4
    rules = [None] * 4
    rules[1] = _fn(ts, tuple(outer))
    tables[1] = (ts, 3)
    for i in outer:
        ti = _rand_table(rng, 1)
        rules[i] = _fn(ti, (1,))
        tables[i] = (ti, 1)
    return rules, tables


def instrument_control():
    """n=3 conjunctive triad and a known n=4 floor check before the sample."""
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    conj = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v3 = classify_rules(conj, labels=("W", "S", "C"))
    ok3 = v3.structure == "triadic" and abs(v3.max_phi - 2.0) < 1e-6
    print(f"  n=3 conjunctive triad: {v3.structure} Φ={v3.max_phi:.6f}  "
          f"{'PASS' if ok3 else 'FAIL'}")
    # n=4 all-AND hub: S'=W&C1&C2, parties copy S — triadic at the 2(n-1)=6 edge floor
    rules4 = [
        lambda x: x[1],
        lambda x: x[0] & x[2] & x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]
    v4 = classify_rules(rules4, labels=LABELS)
    ok4 = v4.structure == "triadic" and v4.max_phi > 0
    e4 = int(cm_from_rules(rules4).sum())
    print(f"  n=4 AND hub:           {v4.structure} Φ={v4.max_phi:.6f} edges={e4}  "
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
    print(f"BUILD PANEL — strict-mediation n=4, N={n}, seed={seed}")
    print("-" * 72)
    for k in range(n):
        rules, tables = sample_form_with_tables(rng)
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
        if (k + 1) % 500 == 0:
            n_tri = sum(r["triadic"] for r in rows)
            print(f"  {k + 1}/{n}  ({time.time() - start:.0f}s)  triadic so far={n_tri}")
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
    print("F26 — HOLISTIC RESIDUAL AT n=4 vs n=3 BASELINE")
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

    majority_pred = np.zeros(n, dtype=int)  # always dyadic (majority at n=4 SM)
    majority_miss = int((majority_pred != y).sum())
    majority_rate = majority_miss / n

    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    miss_tri = fn / n_tri if n_tri else float("nan")
    miss_dya = fp / (n - n_tri) if (n - n_tri) else float("nan")
    near = float(np.mean(np.abs(proba[miss] - 0.5) < 0.25)) if n_miss else float("nan")
    mean_margin = float(np.mean(np.abs(proba[miss] - 0.5))) if n_miss else float("nan")

    if HOLD_LO <= rate <= HOLD_HI:
        verdict = "H0"
        reading = "HOLDS"
    elif rate < HOLD_LO:
        verdict = "H1"
        reading = "SHRINKS"
    else:
        verdict = "H2"
        reading = "GROWS"

    print(f"  sample:                     N={n}, seed={SEED} (probe_n4_census protocol)")
    print(f"  triadic forms:              {n_tri}/{n} = {100 * tri_rate:.1f}%")
    print(f"  RF misclassified (n=4):     {n_miss}/{n} = {100 * rate:.1f}%")
    print(f"  n=3 baseline (Probe 131):   {N3_BASELINE_MISS}/{N3_BASELINE_N} = "
          f"{100 * N3_BASELINE_RATE:.1f}%")
    print(f"  delta (n4 - n3):            {100 * (rate - N3_BASELINE_RATE):+.1f} pp")
    print(f"  hold band:                  [{100 * HOLD_LO:.1f}%, {100 * HOLD_HI:.1f}%]")
    print(f"  majority-class miss rate:   {majority_miss}/{n} = {100 * majority_rate:.1f}% "
          f"(always-dyadic)")
    print(f"  false positives / negatives:{fp} / {fn}")
    print(f"  miss rate among triadic:    {100 * miss_tri:.1f}%")
    print(f"  miss rate among dyadic:     {100 * miss_dya:.1f}%")
    print(f"  residual near-boundary (|p-0.5|<0.25): {near:.2f}  "
          f"(mean |p-0.5|={mean_margin:.3f})")
    print(f"  F26 verdict:                {verdict} — residual {reading} at n=4")
    print()
    print("  note: F27 (affine = residual) remains REFUTED in template_coverage_census; not retested.")
    print()
    return {
        "n": n,
        "n_tri": n_tri,
        "tri_rate": tri_rate,
        "n_miss": n_miss,
        "rate": rate,
        "verdict": verdict,
        "reading": reading,
        "fp": fp,
        "fn": fn,
        "miss_tri": miss_tri,
        "miss_dya": miss_dya,
        "near": near,
        "majority_rate": majority_rate,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true",
                    help="recompute exact-Φ panel (N=3000); default loads committed panel")
    args = ap.parse_args()

    print("HOLISTIC RESIDUAL AT n=4 — RESEARCH_AGENDA_50_V2 F26")
    print("=" * 72)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  features: Probe-125/131 ten-feature panel; RF: 400 trees, seed 0, 5-fold CV")
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
    print(f"  n=4 residual rate:          {100 * result['rate']:.1f}% ({result['n_miss']}/{result['n']})")
    print(f"  n=3 residual rate:          {100 * N3_BASELINE_RATE:.1f}% ({N3_BASELINE_MISS}/{N3_BASELINE_N})")
    print(f"  F26:                        {result['verdict']} ({result['reading']})")
    print(f"  triadic in sample:          {result['n_tri']}/{result['n']} "
          f"({100 * result['tri_rate']:.1f}%)")
    print(f"  near-boundary among misses: {result['near']:.2f}  (F28 note only)")
    print("=" * 72)


if __name__ == "__main__":
    main()
