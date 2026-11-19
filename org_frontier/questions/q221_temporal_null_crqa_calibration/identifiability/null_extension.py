"""Gate E extension: temporal-null comparison on Hassan's pilot DGP (exploratory methods check, NOT confirmatory).
SPEC (committed before this script was run):
- DGP (identical to independent_audit/null_pilot.py): two INDEPENDENT symmetric binary Markov channels, stay
  probability p in {0.5, 0.9, 0.98}, T = 240, uniform start. H0 (no cross-dependence) is true by construction.
- Units: N = 250 independently generated pairs per p (seed default_rng(2215001)); B = 199 surrogates per test.
- Statistics: (S1) |zero-lag Pearson| (constant series -> 0), as in the pilot; (S2) q220's pairwise prominence:
  stage2 observe.coupling(np.arange(T), [x, y], MAX_LAG 10, "timestamp", MIN_PAIRS 30)["prom"][0, 1].
- Surrogates (applied to y only):
  shuffle   : i.i.d. permutation (assumes exchangeability; invalid under serial dependence);
  circular  : np.roll by U{1..T-1} (preserves y's serial dependence up to the wrap; assumes stationarity);
  block     : non-overlapping block permutation, block length 16 ~ sqrt(T) (preserves within-block dependence);
  markov1   : parametric bootstrap from y's fitted first-order stay probability (clipped to [1/T, 1-1/T]); the
              estimate is refitted per observed series, so estimation uncertainty is NOT propagated (stated
              limitation; Gate E asks for this to be visible).
- p-value: Phipson-Smyth (1 + #{T* >= T_obs - 1e-12}) / (B + 1); reject at alpha = 0.05.
- Report: rejections/N, FPR, Wilson 95% CI, per statistic x surrogate x p. Calibration band (from the plan,
  approved by Hassan): 0.025-0.075 at 5%; a method is 'within band' only if its Wilson CI lies inside it, 'outside'
  if its CI excludes the band, else 'inconclusive'.
- No improved-calibration claim is made from this pilot (it is not prespecified as confirmatory)."""
import json
import math
import os

import numpy as np

from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob

OUT = os.path.join(os.path.dirname(__file__), "results")
N, T, B, ALPHA, BL = 250, 240, 199, 0.05, 16
PERS = (0.5, 0.9, 0.98)


def series(p, rng, start=None):
    x = np.empty(T, dtype=np.int8)
    x[0] = rng.integers(2) if start is None else start
    fl = rng.random(T - 1) > p
    for t in range(1, T):
        x[t] = x[t - 1] ^ fl[t - 1]
    return x


def pearson(a, b):
    x = a - a.mean(); y = b - b.mean()
    d = np.linalg.norm(x) * np.linalg.norm(y)
    return abs(float(x @ y / d)) if d > 1e-12 else 0.0


def prom(a, b):
    return float(ob.coupling(np.arange(T), np.column_stack([a, b]), 10, "timestamp", 30)["prom"][0, 1])


def surrogate(y, method, rng):
    if method == "shuffle":
        return rng.permutation(y)
    if method == "circular":
        return np.roll(y, int(rng.integers(1, T)))
    if method == "block":
        blocks = [y[i:i + BL] for i in range(0, T, BL)]
        return np.concatenate([blocks[k] for k in rng.permutation(len(blocks))])
    stay = float(np.mean(y[1:] == y[:-1]))
    stay = min(max(stay, 1 / T), 1 - 1 / T)
    return series(stay, rng)


def wilson(k, n, z=1.96):
    p = k / n; den = 1 + z * z / n; mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(mid - half, 4), round(mid + half, 4)]


def band(ci):
    if ci[0] >= 0.025 and ci[1] <= 0.075:
        return "within"
    if ci[1] < 0.025 or ci[0] > 0.075:
        return "outside"
    return "inconclusive"


def main():
    rng = np.random.default_rng(2215001)
    methods = ("shuffle", "circular", "block", "markov1")
    stats = (("pearson", pearson), ("q220_prominence", prom))
    rows = []
    for p in PERS:
        rej = {(s, m): 0 for s, _ in stats for m in methods}
        degenerate = 0
        for _ in range(N):
            x, y = series(p, rng).astype(float), series(p, rng).astype(float)
            degenerate += int(np.all(x == x[0]) or np.all(y == y[0]))
            obs = {s: f(x, y) for s, f in stats}
            for m in methods:
                exc = {s: 0 for s, _ in stats}
                for _ in range(B):
                    z = surrogate(y, m, rng).astype(float)
                    for s, f in stats:
                        exc[s] += int(f(x, z) >= obs[s] - 1e-12)
                for s, _ in stats:
                    rej[(s, m)] += int((1 + exc[s]) / (B + 1) <= ALPHA)
        for (s, m), k in rej.items():
            ci = wilson(k, N)
            rows.append(dict(persistence=p, statistic=s, surrogate=m, rejections=k, n=N, fpr=k / N, wilson95=ci,
                             band=band(ci), degenerate_pairs=degenerate))
            print("p=%.2f %-16s %-9s %3d/%d FPR %.3f  CI %s  %s" % (p, s, m, k, N, k / N, ci, band(ci)))
    json.dump(dict(status="exploratory", seed=2215001, rows=rows), open(os.path.join(OUT, "null_extension.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
