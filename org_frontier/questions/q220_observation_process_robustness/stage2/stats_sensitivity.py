"""q220 stage 2 - POST-HOC interval-method sensitivity of the confirmatory family (no new runs).

Post-hoc sensitivity analysis, written by an external review after the results were known. It reads ONLY
the committed per-run table (results/stage2_runs.csv.gz) plus the exact-Phi labels margin_audit.py uses,
and recomputes every confirmatory contrast (S2-H1..S2-H8) under several interval methods:

  pct    two-stage form/seed percentile bootstrap (stats.cluster_boot, the method of the run)
  basic  two-stage "basic" (reverse-percentile) bootstrap from the same resamples
  bca    two-stage BCa: bias-correction z0 from the same resamples, acceleration from a
         leave-one-form-out jackknife on form means
  form   one-stage bootstrap of the per-form means (forms resampled, seeds fixed)
  t      Student t interval on the per-form means (df = forms - 1)
  run    naive run-level i.i.d. bootstrap (ignores clustering; shown only as a contrast)

at the 95% level and the Bonferroni level 99.5% (family of 10), with NBOOT resamples and several bootstrap
seeds (Monte Carlo spread). For each method it re-applies the decision rule actually used (and, for
superiority, the margin reading lo >= margin). Nothing here replaces a preregistered verdict.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.stats_sensitivity
"""
import csv, math, os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import numpy as np
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import build_corpus
from org_frontier.questions.q220_observation_process_robustness.stage2 import decision as dec
from org_frontier.questions.q220_observation_process_robustness.stage2.probe_stage2 import RESULTS, SEEDS, read_runs

NBOOT = int(os.environ.get("Q220_SENS_BOOT", "20000"))
BOOT_SEEDS = (220, 1, 2)
LEVELS = (0.95, 0.995)
H = [("S2-H1", "R1", "B", "A", "MAR", "superiority", 0.10),
     ("S2-H2", "R1", "CLEAN", "B", "MAR", "noninferiority", 0.10),
     ("S2-H3", "R1", "CLEAN", "LEN", "MAR", "noninferiority", 0.10),
     ("S2-H4", "R1", "B", "C", "MAR", "superiority", 0.05),
     ("S2-H5", "R1", "B", "A", "BURST", "equivalence", 0.05),
     ("S2-H6a", "R2", "B", "A", "MAR", "superiority", 0.05),
     ("S2-H6b", "R2", "CLEAN", "CHANCE", "MAR", "positive", None),
     ("S2-H7a", "R1", "CLEAN", "CHANCE", "MAR", "positive", None),
     ("S2-H7b", "R1", "CLEAN", "NULL-CLEAN", "MAR", "positive", None),
     ("S2-H8", "R1", "B", "CHANCE", "MAR", "positive", None)]


def _ndtri(p):
    # inverse standard normal (Acklam); adequate for interval endpoints
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02, 1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02, 6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00]
    if p < 0.02425:
        q = math.sqrt(-2 * math.log(p)); return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > 1 - 0.02425:
        return -_ndtri(1 - p)
    q = p - 0.5; r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)


def _ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _tq(p, df):
    try:
        from scipy import stats
        return float(stats.t.ppf(p, df))
    except Exception:          # Cornish-Fisher fallback
        z = _ndtri(p); return z + (z**3 + z) / (4 * df) + (5*z**5 + 16*z**3 + 3*z) / (96 * df**2)


def two_stage(a, boot, seed):
    f, s = a.shape
    rng = np.random.default_rng(seed)
    fi = rng.integers(0, f, size=(boot, f))
    si = rng.integers(0, s, size=(boot, f, s))
    return a[fi[:, :, None], si].mean(axis=(1, 2))


def intervals(a, level, boot, seed):
    f, s = a.shape
    q = (1 - level) / 2
    m = float(a.mean())
    bs = two_stage(a, boot, seed)
    pct = (float(np.quantile(bs, q)), float(np.quantile(bs, 1 - q)))
    basic = (2 * m - pct[1], 2 * m - pct[0])
    # BCa
    prop = float(np.mean(bs < m))
    z0 = _ndtri(min(max(prop, 1.0 / (boot + 1)), boot / (boot + 1.0)))
    fm = a.mean(axis=1)
    jack = np.array([np.delete(fm, i).mean() for i in range(f)])
    jd = jack.mean() - jack
    den = 6 * (np.sum(jd ** 2) ** 1.5)
    acc = float(np.sum(jd ** 3) / den) if den > 0 else 0.0
    def adj(alpha):
        z = _ndtri(alpha); return _ncdf(z0 + (z0 + z) / (1 - acc * (z0 + z)))
    bca = (float(np.quantile(bs, adj(q))), float(np.quantile(bs, adj(1 - q))))
    # one-stage form bootstrap of form means
    rng = np.random.default_rng(seed + 1)
    fb = fm[rng.integers(0, f, size=(boot, f))].mean(axis=1)
    form = (float(np.quantile(fb, q)), float(np.quantile(fb, 1 - q)))
    # t on form means
    se = fm.std(ddof=1) / math.sqrt(f) if f > 1 else 0.0
    tq = _tq(1 - q, f - 1)
    tint = (m - tq * se, m + tq * se)
    # naive run-level
    flat = a.ravel()
    rng = np.random.default_rng(seed + 2)
    rb = np.empty(boot)
    for k in range(0, boot, 5000):
        n = min(5000, boot - k)
        rb[k:k + n] = flat[rng.integers(0, flat.size, size=(n, flat.size))].mean(axis=1)
    run = (float(np.quantile(rb, q)), float(np.quantile(rb, 1 - q)))
    return m, {"pct": pct, "basic": basic, "bca": bca, "form": form, "t": tint, "run": run}


def verdict(rule, m, lo, hi, margin, strict=False):
    if rule == "superiority":
        return (dec.superiority_strict if strict else dec.superiority)(m, lo, hi, margin)
    fn = getattr(dec, rule)
    return fn(m, lo, hi, margin) if margin is not None else fn(m, lo, hi)


def main():
    rows = [r for r in read_runs() if r["variant"] == "main" and r["set"] in ("R1", "R2")]
    corpus = build_corpus()
    prim = {"R1": [f["key"] for f in corpus if len(f["bottleneck"]) < f["n"]]}
    chance = {"R1": {f["key"]: len(f["bottleneck"]) / f["n"] for f in corpus}}
    with open(os.path.join(RESULTS, "stage2_forms_r2.csv")) as fh:
        r2 = list(csv.DictReader(fh))
    prim["R2"] = [f["form"] for f in r2]
    chance["R2"] = {f["form"]: len(f["bottleneck"].split()) / int(f["n"]) for f in r2}
    idx = {(r["set"], r["form"], int(r["seed"]), r["mask"], float(r["dose"]), r["method"]): float(r["bn_score"])
           for r in rows}

    def get(s, meth, mask):
        if meth == "CHANCE":
            return np.array([[chance[s][f]] * len(SEEDS[s]) for f in prim[s]])
        if meth in ("CLEAN", "NULL-CLEAN"):
            return np.array([[idx[(s, f, x, "NONE", 0.0, meth)] for x in SEEDS[s]] for f in prim[s]])
        return np.array([[idx[(s, f, x, mask, 0.3, meth)] for x in SEEDS[s]] for f in prim[s]])

    print("POST-HOC interval-method sensitivity (external review; committed table only; %d resamples; seeds %s)"
          % (NBOOT, BOOT_SEEDS))
    print("verdict = rule as run; for superiority also the margin reading (lo >= margin) after '/'")
    for hid, s, m1, m2, mask, rule, margin in H:
        d = get(s, m1, mask) - get(s, m2, mask)
        fm = d.mean(axis=1)
        # seed (crossed) structure: share of variance explained by seed after removing form means
        resid = d - fm[:, None]
        seed_means = resid.mean(axis=0)
        f_, s_ = d.shape
        ms_seed = f_ * np.sum(seed_means ** 2) / (s_ - 1)
        ms_res = np.sum((resid - seed_means[None, :]) ** 2) / ((f_ - 1) * (s_ - 1))
        print("")
        print("%s %s (%s - %s), point %+.4f | forms +%d/-%d/0:%d | seed-effect F = %.2f"
              % (hid, s, m1, m2, d.mean(), (fm > 0).sum(), (fm < 0).sum(), (fm == 0).sum(),
                 ms_seed / ms_res if ms_res > 0 else float("nan")))
        for level in LEVELS:
            res = {}
            for bs in BOOT_SEEDS:
                m, ints = intervals(d, level, NBOOT, bs)
                for k, v in ints.items():
                    res.setdefault(k, []).append(v)
            for k, vs in res.items():
                los = [v[0] for v in vs]; his = [v[1] for v in vs]
                vv = sorted({verdict(rule, m, v[0], v[1], margin) + ("/" + verdict(rule, m, v[0], v[1], margin, True) if rule == "superiority" else "") for v in vs})
                print("  %.3f %-5s lo %+.4f..%+.4f  hi %+.4f..%+.4f  %s%s"
                      % (level, k, min(los), max(los), min(his), max(his), ",".join(vv),
                         "" if len(vv) == 1 else "  <- MC-UNSTABLE"))


if __name__ == "__main__":
    main()
