"""Prespecified comparator study on the 3 surviving pairs (spec also recorded in protocol.md, section
"Comparator study"; committed BEFORE the first run). Exploratory / provisional; not confirmatory.

PAIRS (screen_exact.json survivors_48group_unique): S1 aff(9,6,10)/aff(9,15,10) [lead P/Q];
S2 aff(9,6,10)/aff(9,15,12); S3 aff(9,6,11)/aff(9,14,10).

GENERATOR: the repo's org_frontier.recurrence.crqa.trajectory (q220's), 600 steps, warmup 20, flip 0.08.
SEEDS: default_rng(47000 + 1000*pair_index + 500*member + r); r = 0..99 training, r = 100..299 test
(disjoint from all earlier q221 seed ranges).

COMPARATORS
 C1 transfer entropy (history length 1, binary, plug-in): TE_{i->j} = I(x_j(t+1); x_i(t) | x_j(t)), all 6
    ordered channel pairs, in bits.
 C2 joint recurrence (JRP, categorical, no embedding): JRR_ij(k) = P(x_i(t)=x_i(t+k) and x_j(t)=x_j(t+k)),
    3 unordered channel pairs x lags k = 1..10.
 C3 multidimensional recurrence (MdRQA, categorical): RR_3(k) = P(x(t) = x(t+k)) for the full 3-vector,
    k = 1..10.
 C4 SHREC: shrec.models.RecurrenceManifold (Gilpin; github.com/williamgilpin/shrec @ 49c6d3e0, installed in
    a separate venv) with library defaults (d_embed=3) and random_state=0, on the 600x3 series cast to float.
    Prespecified features of the reconstructed driver y: |corr(y, x_i)| for i in X,Y,H and the lag-1
    autocorrelation of y (4 features).
 C5 false-pair surrogates for q220's prominence statistic: the null is 199 false-pair surrogates, each a
    3-channel series assembled from three DIFFERENT training trajectories (pooled over both members, so it
    is label-agnostic); seed default_rng(47999). Features: z_ab = (prom_ab - mean_null_ab) / sd_null_ab for the
    3 channel pairs (q220 coupling: max lag 10, timestamp alignment, MIN_PAIRS 30). Also reported:
    Phipson-Smyth empirical p-values, and the fraction of test trajectories with p < 0.05 per member.

EXACT POPULATION SEPARATION (where feasible): C1, C2 and C3 are computed exactly from the stationary law
(exact rationals; TE takes a float log at the end). "Separates exactly" means some feature differs by more
than 1e-12. C5's population expectation is a function of the pairwise profiles, so it is equal by the
Corollary; this is stated, not tested. C4 has no population analogue; finite-sample only.

FINITE-SAMPLE TEST: nearest class centroid on features z-scored by the training SD (no tuning); test
accuracy on 400 test trajectories per pair (200 per member); Wilson 95% CI. DECISION: "separates (finite
sample)" if the Bonferroni-adjusted (15 tests: 3 pairs x 5 comparators; z = 2.935) Wilson lower bound is
> 0.5; "not separated" otherwise. Chance is 0.5.

THEORY-BASED EXPECTATIONS (written before running; not altered afterwards):
 C1: TE_{i->j} depends on the law of (x_i, x_j) over 2 steps. For S1 that law is equal for (X,H) but differs
     for (X,Y) and (Y,H), so a population difference is possible but not guaranteed.
 C2: depends on the bivariate law over (t, t+k); same expectation as C1.
 C3: depends on the full law, so a difference is possible.
 C4: no expectation.
 C5: no population separation; finite-sample accuracy expected near 0.5.
Output: results/comparators.{txt,json}."""
import json
import math
import os
import sys
import warnings
from fractions import Fraction

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES, tpm, stationary

OUT = os.path.join(os.path.dirname(__file__), "results")
PAIRS = [(("aff", 9, 6, 10), ("aff", 9, 15, 10)), (("aff", 9, 6, 10), ("aff", 9, 15, 12)),
         (("aff", 9, 6, 11), ("aff", 9, 14, 10))]
STEPS, WARM, FLIP, LAGS = 600, 20, 0.08, range(1, 11)
UPAIRS = [(0, 1), (0, 2), (1, 2)]
OPAIRS = [(i, j) for i in range(3) for j in range(3) if i != j]
ZB = 2.935  # two-sided Bonferroni z for 15 tests
NAMES = ["C1_TE", "C2_JRR", "C3_MdRR", "C4_SHREC", "C5_falsepair_q220"]


def bit(s, i):
    return (s >> i) & 1


# ---------- exact population values ----------
def exact_features(fid):
    P = tpm(TABLES[fid]); pi = stationary(P)
    te = []
    for i, j in OPAIRS:
        p = {}
        for s in range(8):
            for z in range(8):
                key = (bit(z, j), bit(s, j), bit(s, i))
                p[key] = p.get(key, Fraction(0)) + pi[s] * P[s][z]
        tot = 0.0
        for (a, b, c), v in p.items():
            if v == 0:
                continue
            p_bc = sum(p.get((x, b, c), 0) for x in (0, 1))
            p_ab = sum(p.get((a, b, y), 0) for y in (0, 1))
            p_b = sum(p.get((x, b, y), 0) for x in (0, 1) for y in (0, 1))
            tot += float(v) * math.log2(float(v * p_b) / float(p_bc * p_ab))
        te.append(tot)
    J = [[pi[s] if s == z else Fraction(0) for z in range(8)] for s in range(8)]
    jrr, md = [], []
    for k in range(1, 11):
        J = [[sum(J[s][u] * P[u][z] for u in range(8)) for z in range(8)] for s in range(8)]
        jrr.append([sum(J[s][z] for s in range(8) for z in range(8) if bit(s, a) == bit(z, a) and bit(s, b) == bit(z, b))
                    for a, b in UPAIRS])
        md.append(sum(J[s][s] for s in range(8)))
    jrr = [jrr[k][q] for q in range(3) for k in range(10)]
    return dict(C1_TE=te, C2_JRR=jrr, C3_MdRR=md)


# ---------- finite-sample features ----------
def te_hat(x):
    out = []
    for i, j in OPAIRS:
        c = np.zeros((2, 2, 2))
        np.add.at(c, (x[1:, j], x[:-1, j], x[:-1, i]), 1)
        p = c / c.sum()
        p_bc = p.sum(0, keepdims=True); p_ab = p.sum(2, keepdims=True); p_b = p.sum((0, 2), keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            t = np.where(p > 0, p * np.log2(p * p_b / (p_bc * p_ab)), 0.0)
        out.append(float(np.nansum(t)))
    return out


def jrr_hat(x):
    return [float(np.mean((x[:-k, a] == x[k:, a]) & (x[:-k, b] == x[k:, b]))) for a, b in UPAIRS for k in LAGS]


def md_hat(x):
    return [float(np.mean(np.all(x[:-k] == x[k:], axis=1))) for k in LAGS]


def shrec_feats(x):
    from shrec.models import RecurrenceManifold
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        y = RecurrenceManifold(random_state=0).fit_predict(x.astype(float))
    y = np.asarray(y, float)
    cs = []
    for i in range(3):
        c = np.corrcoef(y, x[:, i])[0, 1] if np.std(x[:, i]) > 0 and np.std(y) > 0 else 0.0
        cs.append(abs(float(np.nan_to_num(c))))
    ac = np.corrcoef(y[:-1], y[1:])[0, 1] if np.std(y) > 0 else 0.0
    return cs + [float(np.nan_to_num(ac))]


def prom3(x):
    pm = np.asarray(ob.coupling(np.arange(STEPS), x, 10, "timestamp", 30)["prom"], float)
    return [float(np.nan_to_num(pm[a, b])) for a, b in UPAIRS]


def wilson(k, n, z=1.96):
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return round(mid - half, 4), round(mid + half, 4)


def ncc(Ftr, ytr, Fte, yte):
    mu, sd = Ftr.mean(0), Ftr.std(0)
    sd[sd == 0] = 1.0
    A, B = (Ftr - mu) / sd, (Fte - mu) / sd
    c0, c1 = A[ytr == 0].mean(0), A[ytr == 1].mean(0)
    pred = (((B - c1) ** 2).sum(1) < ((B - c0) ** 2).sum(1)).astype(int)
    k = int((pred == yte).sum())
    return k, len(yte)


def main():
    res = {"spec": "see module docstring / protocol.md", "pairs": []}
    lines = []
    for pidx, (a, b) in enumerate(PAIRS):
        ex = {m: exact_features(f) for m, f in zip("ab", (a, b))}
        exact = {}
        for nm in ("C1_TE", "C2_JRR", "C3_MdRR"):
            d = max(abs(float(u) - float(v)) for u, v in zip(ex["a"][nm], ex["b"][nm]))
            exact[nm] = dict(max_abs_diff=d, separates_exactly=bool(d > 1e-12))
        exact["C5_falsepair_q220"] = dict(separates_exactly=False, note="population-equal by the Corollary")
        exact["C4_SHREC"] = dict(separates_exactly="not computable")
        trajs = {}
        for m, fid in enumerate((a, b)):
            rules = ps.table_form(TABLES[fid])
            trajs[m] = [trajectory(rules, STEPS, np.random.default_rng(47000 + 1000 * pidx + 500 * m + r),
                                   flip=FLIP, warmup=WARM).astype(int) for r in range(300)]
        feats = {nm: {m: [] for m in (0, 1)} for nm in NAMES}
        for m in (0, 1):
            for x in trajs[m]:
                feats["C1_TE"][m].append(te_hat(x)); feats["C2_JRR"][m].append(jrr_hat(x))
                feats["C3_MdRR"][m].append(md_hat(x)); feats["C4_SHREC"][m].append(shrec_feats(x))
                feats["C5_falsepair_q220"][m].append(prom3(x))
        # false-pair null from the pooled training trajectories (label-agnostic)
        pool = trajs[0][:100] + trajs[1][:100]
        rng = np.random.default_rng(47999)
        null = []
        for _ in range(199):
            r = rng.choice(len(pool), 3, replace=False)
            null.append(prom3(np.stack([pool[r[c]][:, c] for c in range(3)], 1)))
        null = np.array(null); nmu, nsd = null.mean(0), null.std(0); nsd[nsd == 0] = 1.0
        fp_rate = {}
        for m in (0, 1):
            P3 = np.array(feats["C5_falsepair_q220"][m])
            pv = (1 + (null[None, :, :] >= P3[:, None, :]).sum(1)) / 200.0
            fp_rate[m] = [float(v) for v in (pv[100:] < 0.05).mean(0)]
            feats["C5_falsepair_q220"][m] = list((P3 - nmu) / nsd)
        finite = {}
        for nm in NAMES:
            F0, F1 = np.array(feats[nm][0], float), np.array(feats[nm][1], float)
            Ftr = np.vstack([F0[:100], F1[:100]]); ytr = np.r_[np.zeros(100), np.ones(100)].astype(int)
            Fte = np.vstack([F0[100:], F1[100:]]); yte = np.r_[np.zeros(200), np.ones(200)].astype(int)
            k, n = ncc(Ftr, ytr, Fte, yte)
            lo_b, hi_b = wilson(k, n, ZB)
            finite[nm] = dict(acc=round(k / n, 4), wilson95=wilson(k, n), wilson_bonf=(lo_b, hi_b),
                              separates_finite_sample=bool(lo_b > 0.5))
        res["pairs"].append(dict(a=list(a), b=list(b), exact=exact, finite=finite,
                                 falsepair_reject_rate_p05={"a": fp_rate[0], "b": fp_rate[1]},
                                 exact_values={"a": {k: [float(v) for v in vv] for k, vv in ex["a"].items()},
                                               "b": {k: [float(v) for v in vv] for k, vv in ex["b"].items()}}))
        lines.append("== S%d %s vs %s" % (pidx + 1, a, b))
        for nm in NAMES:
            e, f = exact[nm], finite[nm]
            lines.append("  %-18s exact: %-40s finite: acc %.4f  W95 %s  Bonf %s  separates=%s"
                         % (nm, ("separates=%s maxdiff=%.3g" % (e["separates_exactly"], e["max_abs_diff"]))
                            if "max_abs_diff" in e else "separates=%s" % e["separates_exactly"],
                            f["acc"], f["wilson95"], f["wilson_bonf"], f["separates_finite_sample"]))
        lines.append("  false-pair p<0.05 rate on test trajectories (channel pairs XY, XH, YH): a %s ; b %s"
                     % ([round(v, 3) for v in fp_rate[0]], [round(v, 3) for v in fp_rate[1]]))
        lines.append("  exact TE (bits) a: %s" % [round(v, 6) for v in ex["a"]["C1_TE"]])
        lines.append("  exact TE (bits) b: %s" % [round(v, 6) for v in ex["b"]["C1_TE"]])
        print("\n".join(lines[-9:]), flush=True)
    json.dump(res, open(os.path.join(OUT, "comparators.json"), "w"), indent=1)
    open(os.path.join(OUT, "comparators.txt"), "w").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
