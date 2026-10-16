"""Gate D: structural-prediction baselines across independently generated forms with held-out families.
SPEC (committed before this script was run; exploratory pilot, NOT confirmatory):
- Families: 'nsi' (q220 R2: q162 random_wiring, no self-inputs) and 'aff' (GF(2)-affine with self-inputs), 4096 each.
- Forms: from each family draw forms uniformly without replacement with numpy default_rng(2210001 [nsi] /
  2210002 [aff]) until 80 ELIGIBLE forms are collected. Eligibility = q220 R2 rule on q161 targets (deterministic
  TPM): |core| >= 2, B non-empty, |B| < 3. Every draw, eligible or not, is logged.
- Data: 2 trajectories per form with q220's generator org_frontier.recurrence.crqa.trajectory, 600 steps,
  warmup 20, flip 0.08, seeds default_rng(450000 + 10*form_index + r), r = 0, 1 (form_index within family; aff
  forms offset by 100000).
- Unit of replication: the FORM (trajectory scores averaged within form). Score of a predicted node set M:
  |M ∩ B| / |M| (q220's tie-aware score); chance = |B|/3.
- Predictors:
  P0 chance        : M = all nodes.
  P1 node prior    : nodes most often in B on the TRAINING family (train-only class frequency).
  P2 marginal      : node(s) with max (or min, chosen on TRAINING family) |mean - 1/2|.
  P3 autocorr-only : node(s) with max (or min, chosen on TRAINING family) lag-1 self-match.
  P4 q220 rule     : q220 stage2 observe.coupling(timestamp, MAX_LAG 10, MIN_PAIRS 30) -> centrality(0.05)
                     -> tie-aware argmax set (all-zero -> all nodes).
  P5 plug-in       : estimate each node's deterministic rule as the majority next value per observed state
                     (ties/unseen -> 0), then q161 bottleneck_set on the estimated rules; empty -> all nodes.
- Held-out family: P1-P3 learn only on the other family; P0, P4, P5 have nothing to learn. Results are reported
  per evaluation family.
- Uncertainty: 95% percentile bootstrap over forms (2000 resamples, default_rng(2210003)) for mean score and for
  mean (score - chance).
- Pre-stated expectation: P5 well above chance; P0-P4 near chance. No threshold is tuned on evaluation data."""
import json
import os
import time

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import core_indices, bottleneck_set
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps

OUT = os.path.join(os.path.dirname(__file__), "results")
L = ("X", "Y", "H")
N_ELIG, STEPS, WARM, FLIP = 80, 600, 20, 0.08


def target(tables):
    rules = ps.table_form(tables)
    ci, phi = core_indices(rules, L)
    B, base, drops = bottleneck_set(rules, L)
    B = set(int(b) for b in B)
    ci = list(ci) if ci else []  # no complex in any reachable state -> ineligible
    elig = len(ci) >= 2 and 0 < len(B) < 3
    return elig, sorted(B), ci


def sample_family(name, gen, seed, offset):
    forms = list(gen())
    order = np.random.default_rng(seed).permutation(len(forms))
    log, chosen = [], []
    for idx in order:
        fid, tab = forms[int(idx)]
        elig, B, ci = target(tab)
        log.append(dict(fid=list(fid), eligible=elig, B=B, core=ci))
        if elig:
            chosen.append(dict(fid=list(fid), tables=tab, B=B, index=len(chosen) + offset))
            if len(chosen) == N_ELIG:
                break
    return chosen, log


def argset(v, mode):
    v = np.asarray(v, float)
    t = v.max() if mode == "max" else v.min()
    return set(np.flatnonzero(np.abs(v - t) <= 1e-12).tolist())


def score(M, B):
    return sum(m in B for m in M) / len(M)


def features(f):
    out = []
    for r in range(2):
        raw = np.array(trajectory(ps.table_form(f["tables"]), STEPS, np.random.default_rng(450000 + 10 * f["index"] + r),
                                  flip=FLIP, warmup=WARM)).astype(int)
        marg = np.abs(raw.mean(0) - 0.5)
        auto = np.array([np.mean(raw[:-1, i] == raw[1:, i]) for i in range(3)])
        c = ob.coupling(np.arange(STEPS), raw, 10, "timestamp", 30)
        cc = ob.centrality(c["prom"], 0.05)
        M4 = set(range(3)) if cc.max() <= 0 else argset(cc, "max")
        s = raw[:, 0] + 2 * raw[:, 1] + 4 * raw[:, 2]
        est = []
        for j in range(3):
            row = []
            for st in range(8):
                nxt = raw[1:, j][s[:-1] == st]
                row.append(int(nxt.size > 0 and nxt.mean() > 0.5))
            est.append(tuple(row))
        exact_rule = tuple(est) == tuple(tuple(t) for t in f["tables"])
        try:
            Bh, _, _ = bottleneck_set(ps.table_form(tuple(est)), L)
            M5 = set(int(b) for b in Bh) or set(range(3))
        except Exception:
            M5 = set(range(3))
        out.append(dict(marg=marg, auto=auto, M4=M4, M5=M5, exact_rule=exact_rule))
    return out


def boot(x, rng):
    x = np.asarray(x, float)
    bs = [x[rng.integers(0, len(x), len(x))].mean() for _ in range(2000)]
    return [round(float(x.mean()), 4), round(float(np.percentile(bs, 2.5)), 4), round(float(np.percentile(bs, 97.5)), 4)]


def main():
    t0 = time.time()
    fam = {}
    fam["nsi"], log_n = sample_family("nsi", ps.nsi_forms, 2210001, 0)
    fam["aff"], log_a = sample_family("aff", ps.affine_forms, 2210002, 100000)
    # These generator families overlap (some no-self-input forms are affine).
    # A held-out *family* comparison should never evaluate a truth table
    # already encountered in the training family. Fail closed if seeds or
    # eligibility changes ever create cross-family identity leakage.
    def canonical_tables(f):
        return tuple(tuple(int(v) for v in row) for row in f["tables"])
    train_tables = {canonical_tables(f) for f in fam["nsi"]}
    test_tables = {canonical_tables(f) for f in fam["aff"]}
    if len(train_tables) != len(fam["nsi"]) or len(test_tables) != len(fam["aff"]):
        raise AssertionError("repeated truth table within sampled family")
    shared_tables = train_tables & test_tables
    if shared_tables:
        raise AssertionError("train/test family overlap: identical truth tables")

    print("draws: nsi %d (eligible %d) ; aff %d (eligible %d) ; %.0fs"
          % (len(log_n), sum(d["eligible"] for d in log_n), len(log_a), sum(d["eligible"] for d in log_a), time.time() - t0))
    for name in fam:
        for f in fam[name]:
            f["feat"] = features(f)
    print("features done %.0fs" % (time.time() - t0))
    res = {}
    rng = np.random.default_rng(2210003)
    for ev, tr in (("nsi", "aff"), ("aff", "nsi")):
        cnt = np.zeros(3)
        for f in fam[tr]:
            for b in f["B"]:
                cnt[b] += 1
        M1 = argset(cnt, "max")
        modes = {}
        for key, nm in (("marg", "P2"), ("auto", "P3")):
            best = None
            for mode in ("max", "min"):
                sc = np.mean([np.mean([score(argset(x[key], mode), set(f["B"])) for x in f["feat"]]) for f in fam[tr]])
                if best is None or sc > best[1]:
                    best = (mode, sc)
            modes[nm] = best[0]
        rows = {k: [] for k in ("P0", "P1", "P2", "P3", "P4", "P5")}
        ch = []
        exact = []
        for f in fam[ev]:
            B = set(f["B"])
            ch.append(len(B) / 3)
            rows["P0"].append(len(B) / 3)
            rows["P1"].append(score(M1, B))
            rows["P2"].append(np.mean([score(argset(x["marg"], modes["P2"]), B) for x in f["feat"]]))
            rows["P3"].append(np.mean([score(argset(x["auto"], modes["P3"]), B) for x in f["feat"]]))
            rows["P4"].append(np.mean([score(x["M4"], B) for x in f["feat"]]))
            rows["P5"].append(np.mean([score(x["M5"], B) for x in f["feat"]]))
            exact.append(np.mean([x["exact_rule"] for x in f["feat"]]))
        ch = np.array(ch)
        res[ev] = dict(train_family=tr, n_forms=len(fam[ev]), P1_nodes=sorted(M1), P2_mode=modes["P2"], P3_mode=modes["P3"],
                       plug_in_exact_rule_rate=round(float(np.mean(exact)), 4),
                       predictors={k: dict(score=boot(v, rng), minus_chance=boot(np.array(v) - ch, rng)) for k, v in rows.items()})
        print("== evaluate on %s (train-only rules learned on %s), n_forms=%d, plug-in exact-rule rate %.3f"
              % (ev, tr, len(fam[ev]), res[ev]["plug_in_exact_rule_rate"]))
        for k, v in res[ev]["predictors"].items():
            print("   %s score %.4f [%.4f, %.4f]   minus chance %+.4f [%+.4f, %+.4f]" % ((k,) + tuple(v["score"]) + tuple(v["minus_chance"])))
    json.dump(dict(results=res, draws=dict(nsi=log_n, aff=log_a),
                   forms={k: [dict(fid=f["fid"], B=f["B"], index=f["index"]) for f in v] for k, v in fam.items()}),
              open(os.path.join(OUT, "structural_baselines.json"), "w"), indent=1)
    print("total %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
