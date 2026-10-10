"""WHO BROKE PROD? — recompute every reported metric from the saved preregistered run.

Question: in a deterministic simulated incident, how do coordination topology (flat, hub, chain), blame
incentive (neutral, self_protective) and trace access (full, claims_only) affect root-cause attribution
accuracy, false-blame rate and steps to a stable correct attribution? Hypotheses: H1-H6 in
`hypotheses.md`, fixed before the run. Method: read `results/runs.csv` (2400 runs, 200 paired
(scenario, seed) units per cell), recompute per-cell rates with Wilson 95% intervals, and apply each
decision rule with an exact two-sided sign test on discordant pairs (alpha 0.01). Standard library only;
no Φ is computed.

Run (from the repo root):  python org_frontier/studies/who_broke_prod/analyze_who_broke_prod.py
"""
import csv
import os
import sys
from math import comb, sqrt
from statistics import mean

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "results", "runs.csv")
TOPOLOGIES = ("flat", "hub", "chain")
INCENTIVES = ("neutral", "self_protective")
ACCESS = ("full", "claims_only")
EXPECTED_ROWS = 2400
ALPHA = 0.01


def load():
    if not os.path.exists(RUNS):
        sys.exit(f"ERROR: missing {RUNS}; the saved run is required (it is not regenerated here).")
    with open(RUNS, newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != EXPECTED_ROWS:
        sys.exit(f"ERROR: {RUNS} has {len(rows)} rows, expected {EXPECTED_ROWS}.")
    for r in rows:
        for k in ("seed", "messages", "correct", "false_blame", "abstain"):
            r[k] = int(r[k])
        r["steps"] = int(r["steps"]) if r["steps"] else None
    return rows


def wilson(k, n, z=1.959964):
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, mid - half), min(1.0, mid + half)


def sign_test(a, b):
    pos = sum(x > y for x, y in zip(a, b))
    neg = sum(x < y for x, y in zip(a, b))
    n = pos + neg
    if n == 0:
        return 1.0
    return min(1.0, 2 * sum(comb(n, i) for i in range(min(pos, neg) + 1)) / 2 ** n)


def sel(rows, **kw):
    out = [r for r in rows if all(r[k] == v for k, v in kw.items())]
    return sorted(out, key=lambda r: (r["topology"], r["scenario"], r["seed"]))


def rate(rows, col):
    return sum(r[col] for r in rows) / len(rows)


def mean_steps(rows):
    st = [r["steps"] for r in rows if r["steps"] is not None]
    return mean(st) if st else None


def verdict(ok):
    return "SUPPORTED" if ok else "REFUTED"


def main():
    rows = load()
    print("WHO BROKE PROD? — preregistered run, recomputed from results/runs.csv")
    print("=" * 78)
    print(f"runs: {len(rows)}")
    print(f"{'topology':<8}{'incentive':<17}{'access':<12}{'acc':>7}{'ci95':>17}{'false':>7}{'abst':>7}{'steps':>7}")
    for t in TOPOLOGIES:
        for i in INCENTIVES:
            for a in ACCESS:
                c = sel(rows, topology=t, incentive=i, access=a)
                k = sum(r["correct"] for r in c)
                lo, hi = wilson(k, len(c))
                ms = mean_steps(c)
                print(f"{t:<8}{i:<17}{a:<12}{k / len(c):>7.3f}   [{lo:.3f},{hi:.3f}]"
                      f"{rate(c, 'false_blame'):>7.3f}{rate(c, 'abstain'):>7.3f}"
                      f"{(f'{ms:.2f}' if ms is not None else '-'):>7}")
    print("=" * 78)
    sp = dict(incentive="self_protective")
    full, co = sel(rows, access="full", **sp), sel(rows, access="claims_only", **sp)
    d1 = rate(full, "correct") - rate(co, "correct")
    p1 = sign_test([r["correct"] for r in full], [r["correct"] for r in co])
    print(f"H1 acc_full={rate(full, 'correct'):.4f} acc_claims_only={rate(co, 'correct'):.4f} "
          f"diff={d1:.4f} p={p1:.3e}: {verdict(d1 >= 0.10 and p1 < ALPHA)}")
    f_f, f_c = rate(full, "false_blame"), rate(co, "false_blame")
    print(f"H2 false_blame_full={f_f:.4f} false_blame_claims_only={f_c:.4f}: {verdict(f_f <= 0.5 * f_c)}")
    dc = rate(co, "false_blame") - rate(sel(rows, access="claims_only", incentive="neutral"), "false_blame")
    df = rate(full, "false_blame") - rate(sel(rows, access="full", incentive="neutral"), "false_blame")
    print(f"H3 fb_diff_claims_only={dc:.4f} fb_diff_full={df:.4f}: {verdict(dc >= 0.10 and df <= 0.05)}")
    cell = {t: sel(rows, topology=t, access="full", **sp) for t in TOPOLOGIES}
    s = {t: mean_steps(cell[t]) for t in TOPOLOGIES}
    ok4 = s["flat"] <= s["hub"] <= s["chain"] and s["flat"] < s["chain"]
    print(f"H4 mean_steps flat={s['flat']:.4f} hub={s['hub']:.4f} chain={s['chain']:.4f}: {verdict(ok4)}")
    acc = {t: rate(cell[t], "correct") for t in TOPOLOGIES}
    p5 = sign_test([r["correct"] for r in cell["flat"]], [r["correct"] for r in cell["chain"]])
    d5 = acc["flat"] - acc["chain"]
    print(f"H5 acc_flat={acc['flat']:.4f} acc_chain={acc['chain']:.4f} diff={d5:.4f} p={p5:.3e}: "
          f"{verdict(d5 >= 0.10 and p5 < ALPHA)}")
    p6 = sign_test([r["correct"] for r in cell["hub"]], [r["correct"] for r in cell["flat"]])
    d6 = acc["hub"] - acc["flat"]
    print(f"H6 acc_hub={acc['hub']:.4f} acc_flat={acc['flat']:.4f} diff={d6:.4f} p={p6:.3e}: "
          f"{verdict(d6 >= 0.05 and p6 < ALPHA)}")
    print("=" * 78)
    print("scope: evidence about the model, not about a real organization. No Φ computed.")


if __name__ == "__main__":
    main()
