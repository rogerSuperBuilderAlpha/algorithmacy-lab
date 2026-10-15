"""Gate 3: prespecified simple baselines on the 3 surviving pairs (screen_exact.json survivors_48group_unique).
SPEC (committed before this script was run):
- Task per pair: given ONE trajectory, say which member generated it. Generator = the repo's
  org_frontier.recurrence.crqa.trajectory (q220's), 600 steps, warmup 20, flip 0.08.
- Seeds: training 44000..44099, test 44100..44299, each member of each pair (disjoint from all prior q221 seeds).
- Feature sets:
  (a) marginals: mean of X, Y, H                                   (population-equal by construction)
  (b) self-recurrence: P(x_i(t)=x_i(t+k)), i in XYH, k=1..10      (population-equal by construction)
  (c) cross-recurrence: P(x_i(t)=x_j(t+k)), i!=j, k=0..10          (population-equal by construction; control)
  (d) transition counts: empirical 8x8 transition frequency matrix (64 features)
  (e) transition likelihood: per-class TPM fitted on the pooled training trajectories (add-one smoothing);
      classify by log-likelihood ratio of the test trajectory's transitions.
- Classifier for (a)-(d): nearest class centroid on features z-scored by the training SD (no tuning).
- Metric: test accuracy over 400 test trajectories per pair (200 per class; balanced), Wilson 95% CI; chance 0.5.
- Pre-stated expectation: (a)-(c) within CI of 0.5; (d)-(e) near 1. No threshold is tuned on test data.
- Uncertainty "across independently generated forms" is NOT applicable: the 3 pairs are the complete survivor set of a
  deterministic search, not a sample of forms; results are reported per pair, with no pooled population inference."""
import json
import math
import os

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps

OUT = os.path.join(os.path.dirname(__file__), "results")
STEPS, WARM, FLIP = 600, 20, 0.08


def feats(raw):
    x = raw.astype(int)
    a = x.mean(0)
    b = [np.mean(x[:-k, i] == x[k:, i]) for i in range(3) for k in range(1, 11)]
    c = [np.mean(x[:STEPS - k, i] == x[k:, j]) for i in range(3) for j in range(3) if i != j for k in range(0, 11)]
    s = x[:, 0] + 2 * x[:, 1] + 4 * x[:, 2]
    T = np.zeros((8, 8))
    np.add.at(T, (s[:-1], s[1:]), 1)
    return dict(a=np.array(a), b=np.array(b), c=np.array(c), d=(T / T.sum()).ravel(), T=T)


def wilson(k, n, z=1.96):
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return round(mid - half, 4), round(mid + half, 4)


def main():
    surv = json.load(open(os.path.join(OUT, "screen_exact.json")))["survivors_48group_unique"]
    TABLES = {}
    for gen in (ps.nsi_forms, ps.affine_forms):
        for fid, tab in gen():
            TABLES[tuple(fid)] = tab
    res = []
    for sv in surv:
        ids = [tuple(sv["a"]), tuple(sv["b"])]
        F = {}
        for ci, fid in enumerate(ids):
            rules = ps.table_form(TABLES[fid])
            F[ci] = {sp: [feats(np.array(trajectory(rules, STEPS, np.random.default_rng(seed), flip=FLIP, warmup=WARM)))
                          for seed in rng_] for sp, rng_ in (("train", range(44000, 44100)), ("test", range(44100, 44300)))}
        row = dict(pair=[list(i) for i in ids])
        for key in "abcd":
            tr = {ci: np.array([f[key] for f in F[ci]["train"]]) for ci in (0, 1)}
            allt = np.vstack([tr[0], tr[1]])
            sd = allt.std(0, ddof=1)
            sd[sd == 0] = 1.0
            cen = {ci: tr[ci].mean(0) / sd for ci in (0, 1)}
            k = n = 0
            for ci in (0, 1):
                for f in F[ci]["test"]:
                    z = f[key] / sd
                    pred = int(np.sum((z - cen[1]) ** 2) < np.sum((z - cen[0]) ** 2))
                    k += pred == ci
                    n += 1
            row[key] = dict(acc=round(k / n, 4), ci95=wilson(k, n), n=n)
        logP = {}
        for ci in (0, 1):
            C = sum(f["T"] for f in F[ci]["train"]) + 1.0
            logP[ci] = np.log(C / C.sum(1, keepdims=True))
        k = n = 0
        for ci in (0, 1):
            for f in F[ci]["test"]:
                llr = np.sum(f["T"] * (logP[1] - logP[0]))
                k += int(llr > 0) == ci
                n += 1
        row["e"] = dict(acc=round(k / n, 4), ci95=wilson(k, n), n=n)
        res.append(row)
        print(row["pair"], " ".join("%s=%.3f%s" % (key, row[key]["acc"], row[key]["ci95"]) for key in "abcde"))
    json.dump(res, open(os.path.join(OUT, "baselines_survivors.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
