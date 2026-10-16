"""Finite-sample comparator study on the M = 40 preregistered pairs (PREREGISTRATION.md sections 5-7).
Run in /workspace/shrec-venv (SHREC needed) with PYTHONPATH = repo root.
  python -m ...confirmatory_4node.study4 --part LO HI   -> results/study4_part_LO_HI.json (pairs LO <= q < HI)
  python -m ...confirmatory_4node.study4 --combine      -> results/study4.{txt,json} (decision rules)
  python -m ...confirmatory_4node.study4 --smoke        -> 2 pairs x 10 trajectories on seeds 999000+ (discarded)"""
import json
import math
import os
import sys
import time
import warnings
from fractions import Fraction

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import f4

OUT = os.path.join(os.path.dirname(__file__), "results")
STEPS, WARM, FLIP = 600, 20, 0.08
N = 4
UP = [(a, b) for a in range(N) for b in range(a + 1, N)]                 # 6
OP = [(i, j) for i in range(N) for j in range(N) if i != j]              # 12
NAMES = ["R", "C0_likelihood", "C1_TE", "C2_JRR", "C3_MdRR", "C4_SHREC", "C5_falsepair_q220"]
N_TRAIN, N_TEST = 100, 200


# ---------------- features ----------------
def f_R(x):
    a = list(x.mean(0))
    b = [np.mean(x[:-k, i] == x[k:, i]) for i in range(N) for k in range(1, 11)]
    c = [np.mean(x[:STEPS - k, i] == x[k:, j]) for i, j in OP for k in range(0, 11)]
    return [float(v) for v in a + b + c]


def f_TE(x):
    out = []
    for i, j in OP:
        cnt = np.zeros((2, 2, 2))
        np.add.at(cnt, (x[1:, j], x[:-1, j], x[:-1, i]), 1)
        p = cnt / cnt.sum()
        p_bc = p.sum(0, keepdims=True); p_ab = p.sum(2, keepdims=True); p_b = p.sum((0, 2), keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            t = np.where(p > 0, p * np.log2(p * p_b / (p_bc * p_ab)), 0.0)
        out.append(float(np.nansum(t)))
    return out


def f_JRR(x):
    return [float(np.mean((x[:-k, a] == x[k:, a]) & (x[:-k, b] == x[k:, b]))) for a, b in UP for k in range(1, 11)]


def f_MD(x):
    return [float(np.mean(np.all(x[:-k] == x[k:], axis=1))) for k in range(1, 11)]


def f_SHREC(x):
    from shrec.models import RecurrenceManifold
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        y = np.asarray(RecurrenceManifold(random_state=0).fit_predict(x.astype(float)), float)
    cs = []
    for i in range(N):
        c = np.corrcoef(y, x[:, i])[0, 1] if np.std(x[:, i]) > 0 and np.std(y) > 0 else 0.0
        cs.append(abs(float(np.nan_to_num(c))))
    ac = np.corrcoef(y[:-1], y[1:])[0, 1] if np.std(y) > 0 else 0.0
    return cs + [float(np.nan_to_num(ac))]


def f_prom(x):
    pm = np.asarray(ob.coupling(np.arange(STEPS), x, 10, "timestamp", 30)["prom"], float)
    return [float(np.nan_to_num(pm[a, b])) for a, b in UP]


def trans_counts(x):
    s = (x * (1 << np.arange(N))).sum(1)
    T = np.zeros((16, 16))
    np.add.at(T, (s[:-1], s[1:]), 1)
    return T


# ---------------- exact population values (C1-C3) ----------------
def exact_pop(A16, c):
    M = f4.tpm_int(A16, c); den = f4.P_DEN ** N
    pi = Fraction(1, 16)
    te = []
    for i, j in OP:
        p = {}
        for s in range(16):
            for z in range(16):
                key = ((z >> j) & 1, (s >> j) & 1, (s >> i) & 1)
                p[key] = p.get(key, 0) + pi * Fraction(M[s, z], den)
        tot = 0.0
        for (a, b, cc), v in p.items():
            if v == 0:
                continue
            p_bc = sum(p.get((u, b, cc), 0) for u in (0, 1)); p_ab = sum(p.get((a, b, w), 0) for w in (0, 1))
            p_b = sum(p.get((u, b, w), 0) for u in (0, 1) for w in (0, 1))
            tot += float(v) * math.log2(float(v * p_b) / float(p_bc * p_ab))
        te.append(tot)
    jrr, md = [], []
    Pk = np.identity(16, dtype=object) * 1; scale = 1
    pw = []
    for k in range(1, 11):
        Pk = Pk.dot(M); scale *= den
        pw.append((Pk, scale))
    for a, b in UP:
        for Pk, sc in pw:
            tot = sum(Pk[s, z] for s in range(16) for z in range(16)
                      if ((s >> a) & 1) == ((z >> a) & 1) and ((s >> b) & 1) == ((z >> b) & 1))
            jrr.append(Fraction(tot, 16 * sc))
    for Pk, sc in pw:
        md.append(Fraction(sum(Pk[s, s] for s in range(16)), 16 * sc))
    return dict(C1_TE=te, C2_JRR=jrr, C3_MdRR=md)


# ---------------- classifiers ----------------
def ncc(Ftr, ytr, Fte, yte):
    mu, sd = Ftr.mean(0), Ftr.std(0)
    sd[sd == 0] = 1.0
    A, B = (Ftr - mu) / sd, (Fte - mu) / sd
    c0, c1 = A[ytr == 0].mean(0), A[ytr == 1].mean(0)
    pred = (((B - c1) ** 2).sum(1) < ((B - c0) ** 2).sum(1)).astype(int)
    return int((pred == yte).sum())


def run_pair(pr, smoke=False):
    q = pr["q"]
    systems = [tuple(pr["a"]), tuple(pr["b"])]
    ntr, nte = (5, 5) if smoke else (N_TRAIN, N_TEST)
    base = 999000 if smoke else 4220000
    feats = {nm: {0: [], 1: []} for nm in NAMES if nm != "C0_likelihood"}
    TC = {0: [], 1: []}
    for m, (A16, c) in enumerate(systems):
        rules = f4.rules_of(A16, c)
        for r in range(ntr + nte):
            x = trajectory(rules, STEPS, np.random.default_rng(base + 1000 * q + 500 * m + r), flip=FLIP,
                           warmup=WARM).astype(int)
            feats["R"][m].append(f_R(x)); feats["C1_TE"][m].append(f_TE(x)); feats["C2_JRR"][m].append(f_JRR(x))
            feats["C3_MdRR"][m].append(f_MD(x)); feats["C4_SHREC"][m].append(f_SHREC(x))
            feats["C5_falsepair_q220"][m].append(f_prom(x)); TC[m].append(trans_counts(x))
            if m == 0 and r == 0:
                pool_traj = []
            if r < ntr:
                pool_traj.append(x) if m == 0 else pool_traj.append(x)
    # false-pair null (label-agnostic pool of training trajectories of both members)
    rng = np.random.default_rng((999999 if smoke else 4290000) + q)
    null = []
    nnull = 9 if smoke else 199
    for _ in range(nnull):
        idx = rng.choice(len(pool_traj), N, replace=False)
        null.append(f_prom(np.stack([pool_traj[idx[ch]][:, ch] for ch in range(N)], 1)))
    null = np.array(null); nmu, nsd = null.mean(0), null.std(0); nsd[nsd == 0] = 1.0
    for m in (0, 1):
        P = np.array(feats["C5_falsepair_q220"][m]); feats["C5_falsepair_q220"][m] = ((P - nmu) / nsd).tolist()
    ytr = np.r_[np.zeros(ntr), np.ones(ntr)].astype(int); yte = np.r_[np.zeros(nte), np.ones(nte)].astype(int)
    res = {}
    for nm, F in feats.items():
        F0, F1 = np.array(F[0], float), np.array(F[1], float)
        res[nm] = ncc(np.vstack([F0[:ntr], F1[:ntr]]), ytr, np.vstack([F0[ntr:], F1[ntr:]]), yte)
    # C0: transition likelihood
    L = [np.log((sum(TC[m][:ntr]) + 1) / (sum(TC[m][:ntr]) + 1).sum(1, keepdims=True)) for m in (0, 1)]
    k = 0
    for m in (0, 1):
        for T in TC[m][ntr:]:
            pred = int((T * L[1]).sum() > (T * L[0]).sum())
            k += int(pred == m)
    res["C0_likelihood"] = k
    ex = [exact_pop(*systems[0]), exact_pop(*systems[1])]
    exact = {nm: max(abs(float(u) - float(v)) for u, v in zip(ex[0][nm], ex[1][nm])) for nm in ("C1_TE", "C2_JRR", "C3_MdRR")}
    return dict(q=q, a=pr["a"], b=pr["b"], n_test=2 * nte, correct=res, exact_maxdiff=exact)


def wilson(k, n, z):
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return mid - half, mid + half


def combine():
    from scipy.stats import norm, t as tdist
    parts = sorted(f for f in os.listdir(OUT) if f.startswith("study4_part_"))
    rows = []
    for f in parts:
        rows += json.load(open(os.path.join(OUT, f)))["pairs"]
    rows.sort(key=lambda r: r["q"])
    M = len(rows)
    z_pair = norm.ppf(1 - 0.05 / (7 * M) / 2)
    z_cls = norm.ppf(1 - 0.05 / 7 / 2)
    lines = ["pairs completed: %d ; per-pair Bonferroni z = %.3f (7*M tests) ; per-classifier z = %.3f (7 tests)"
             % (M, z_pair, z_cls)]
    summ = {}
    for nm in NAMES:
        accs, sep = [], 0
        for r in rows:
            k, n = r["correct"][nm], r["n_test"]
            lo, hi = wilson(k, n, z_pair)
            r.setdefault("separates", {})[nm] = bool(lo > 0.5)
            sep += int(lo > 0.5); accs.append(k / n)
        lo, hi = wilson(sep, M, z_cls)
        verdict = "generally separates" if lo > 0.5 else ("generally fails" if hi < 0.5 else "mixed (unresolved)")
        accs = np.array(accs)
        summ[nm] = dict(pairs_separated=sep, M=M, prop=sep / M, wilson_bonf=(lo, hi), verdict=verdict,
                        mean_acc=float(accs.mean()), min_acc=float(accs.min()), max_acc=float(accs.max()))
        lines.append("%-18s separated %2d/%d  prop %.3f  Wilson(Bonf) [%.3f, %.3f]  -> %-20s  acc mean %.3f (min %.3f, max %.3f)"
                     % (nm, sep, M, sep / M, lo, hi, verdict, accs.mean(), accs.min(), accs.max()))
    a = np.array([r["correct"]["R"] / r["n_test"] for r in rows])
    se = a.std(ddof=1) / math.sqrt(M); tq = tdist.ppf(0.95, M - 1)
    ci = (a.mean() - tq * se, a.mean() + tq * se)
    h2 = bool(ci[0] > 0.45 and ci[1] < 0.55)
    lines.append("H2 (TOST, margin 0.05): R mean acc %.4f, 90%% t-CI [%.4f, %.4f] -> %s"
                 % (a.mean(), ci[0], ci[1], "EQUIVALENT TO CHANCE (H2 supported)" if h2 else "not shown equivalent"))
    agree = {}
    for nm in ("C1_TE", "C2_JRR", "C3_MdRR"):
        ex_sep = [r["exact_maxdiff"][nm] > 1e-12 for r in rows]
        fs = [r["separates"][nm] for r in rows]
        agree[nm] = dict(exact_separates=sum(ex_sep), finite_separates=sum(fs),
                         agree=sum(e == f for e, f in zip(ex_sep, fs)),
                         exact_sep_but_finite_not=sum(e and not f for e, f in zip(ex_sep, fs)),
                         finite_sep_but_exact_not=sum(f and not e for e, f in zip(ex_sep, fs)))
        lines.append("secondary %-8s exact-population separates %d/%d ; finite separates %d/%d ; agree %d/%d ; exact-only %d ; finite-only %d"
                     % (nm, agree[nm]["exact_separates"], M, agree[nm]["finite_separates"], M, agree[nm]["agree"], M,
                        agree[nm]["exact_sep_but_finite_not"], agree[nm]["finite_sep_but_exact_not"]))
    json.dump(dict(M=M, z_pair=z_pair, z_cls=z_cls, summary=summ, H2=dict(mean=float(a.mean()), ci90=ci, supported=h2),
                   secondary=agree, pairs=rows), open(os.path.join(OUT, "study4.json"), "w"), indent=1)
    open(os.path.join(OUT, "study4.txt"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main(argv):
    pairs = json.load(open(os.path.join(OUT, "screen4.json")))["study_pairs"]
    if argv[0] == "--smoke":
        t = time.time()
        for pr in pairs[:2]:
            r = run_pair(pr, smoke=True)
            print("SMOKE (discarded)", r["q"], r["correct"], {k: round(v, 4) for k, v in r["exact_maxdiff"].items()})
        print("smoke seconds %.1f for 2 pairs x 20 trajectories" % (time.time() - t))
    elif argv[0] == "--part":
        lo, hi = int(argv[1]), int(argv[2])
        out = []
        t = time.time()
        for pr in pairs[lo:hi]:
            out.append(run_pair(pr))
            print("pair %d done (%.0fs): %s" % (pr["q"], time.time() - t, out[-1]["correct"]), flush=True)
            json.dump(dict(pairs=out), open(os.path.join(OUT, "study4_part_%02d_%02d.json" % (lo, hi)), "w"), indent=1)
    elif argv[0] == "--combine":
        combine()


if __name__ == "__main__":
    main(sys.argv[1:])
