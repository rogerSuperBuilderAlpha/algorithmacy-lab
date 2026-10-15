"""q220 stage 2 - Monte Carlo stability of the Bonferroni (99.5%) intervals (no new runs).

Robustness check for stage2/margin_audit.py, which estimates 99.5% two-stage bootstrap intervals from
2,000 resamples, so each 0.25% tail rests on ~5 resamples. This script reads ONLY the committed per-run
table (results/stage2_runs.csv.gz) and the same labels margin_audit.py uses, and re-estimates the 95% and
99.5% intervals of S2-H1, S2-H7a, S2-H7b and S2-H8 with st.cluster_boot (the exact estimator of the run)
at 2,000 / 20,000 / 50,000 resamples and several bootstrap seeds. It reports the Monte Carlo spread of
each lower bound and whether the verdict (as run and, for H1, the margin reading) is stable.
It does not change any recorded result or verdict.

Run (repo root):
    python -m org_frontier.questions.q220_observation_process_robustness.stage2.bonferroni_mc_stability
"""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import numpy as np
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import build_corpus
from org_frontier.questions.q220_observation_process_robustness.stage2 import decision as dec
from org_frontier.questions.q220_observation_process_robustness.stage2 import stats as st
from org_frontier.questions.q220_observation_process_robustness.stage2.probe_stage2 import SEEDS, read_runs

FAMILY = 10
LEVELS = (0.95, 1 - 0.05 / FAMILY)
BOOTS = (2000, 20000, 50000)
BOOT_SEEDS = (220, 1, 2, 3, 4)
H = [("S2-H1", "B", "A", "superiority", 0.10),
     ("S2-H7a", "CLEAN", "CHANCE", "positive", None),
     ("S2-H7b", "CLEAN", "NULL-CLEAN", "positive", None),
     ("S2-H8", "B", "CHANCE", "positive", None)]


def verdicts(rule, t, margin):
    if rule == "superiority":
        return dec.superiority(*t, margin), dec.superiority_strict(*t, margin)
    v = dec.positive(*t)
    return v, v


def main():
    rows = [r for r in read_runs() if r["variant"] == "main" and r["set"] == "R1"]
    corpus = build_corpus()
    prim = [f["key"] for f in corpus if len(f["bottleneck"]) < f["n"]]    # corpus order, as the run
    chance = {f["key"]: len(f["bottleneck"]) / f["n"] for f in corpus}
    idx = {(r["form"], int(r["seed"]), r["mask"], float(r["dose"]), r["method"]): float(r["bn_score"])
           for r in rows}

    def get(meth):
        if meth == "CHANCE":
            return np.array([[chance[f]] * len(SEEDS["R1"]) for f in prim])
        if meth in ("CLEAN", "NULL-CLEAN"):
            return np.array([[idx[(f, x, "NONE", 0.0, meth)] for x in SEEDS["R1"]] for f in prim])
        return np.array([[idx[(f, x, "MAR", 0.3, meth)] for x in SEEDS["R1"]] for f in prim])

    print("Monte Carlo stability of two-stage bootstrap intervals (R1 primary, MAR 0.3; committed run only)")
    print("verdict pair = (rule as run, margin reading); they differ only for superiority (S2-H1)")
    for hid, m1, m2, rule, margin in H:
        d = get(m1) - get(m2)
        print("")
        print("%s (%s - %s), point %+.4f" % (hid, m1, m2, d.mean()))
        for level in LEVELS:
            for boot in BOOTS:
                los, his, vs = [], [], set()
                for bs in BOOT_SEEDS:
                    t = st.cluster_boot(d, boot=boot, seed=bs, level=level)
                    los.append(t[1]); his.append(t[2]); vs.add(verdicts(rule, t, margin))
                print("  level %.3f boot %6d: lo %+.4f..%+.4f (sd %.4f)  hi %+.4f..%+.4f  verdicts %s %s"
                      % (level, boot, min(los), max(los), np.std(los, ddof=1), min(his), max(his),
                         sorted(vs), "STABLE" if len(vs) == 1 else "UNSTABLE"))
    print("")
    print("seeds %s; estimator stats.cluster_boot (percentile, numpy linear quantile)" % (BOOT_SEEDS,))


if __name__ == "__main__":
    main()
