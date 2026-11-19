"""4-node follow-up for C2 (joint recurrence) and C4 (SHREC): PREREGISTRATION_FOLLOWUP.md (commit 74ef91c1).
Run in /workspace/shrec-venv with PYTHONPATH = repo root, single-threaded.
  python -m ...confirmatory_4node.followup --select          -> results/followup_pairs.json (600 pairs + exact checks)
  python -m ...confirmatory_4node.followup --part LO HI      -> results/followup_part_LO_HI.json
  python -m ...confirmatory_4node.followup --combine         -> results/followup.{txt,json}
  python -m ...confirmatory_4node.followup --smoke           -> 2 pairs x 2 members x (5+5) trajectories, seeds 999000+ (discarded)"""
import glob
import json
import math
import os
import sys
import time
from collections import defaultdict

import numpy as np
from scipy.stats import norm

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import f4
from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import study4 as s4

OUT = os.path.join(os.path.dirname(__file__), "results")
M_FU = 600
SEED_SAMPLE, SEED_TRAJ = 5210002, 5220000
Z_PAIR = norm.ppf(1 - 0.05 / (7 * 40) / 2)      # parent per-pair critical value, held fixed (prereg section 1)
Z_CLS = norm.ppf(1 - 0.05 / 2 / 2)              # Bonferroni over 2 classifiers
PRIMARY = ["C2_JRR", "C4_SHREC"]
CHECKS = ["R", "C0_likelihood"]
SECONDARY = ["C1_TE", "C1_TE_MM"]


def f_TE_MM(x):
    """Miller-Madow corrected plug-in TE (bits): each entropy + (K_nonzero - 1) / (2 N ln 2)."""
    out = []
    for i, j in s4.OP:
        cnt = np.zeros((2, 2, 2))
        np.add.at(cnt, (x[1:, j], x[:-1, j], x[:-1, i]), 1)
        n = cnt.sum()

        def H(c):
            c = c[c > 0]; p = c / n
            return float(-(p * np.log2(p)).sum() + (len(c) - 1) / (2 * n * math.log(2)))
        out.append(H(cnt.sum(2)) + H(cnt.sum(0)) - H(cnt.sum((0, 2))) - H(cnt))
    return out


def orbit_pairs():
    As = f4.invertible_As()
    codes, orb = f4.orbit_ids(As)
    orbit = dict(zip(codes.tolist(), orb.tolist()))
    classes = defaultdict(list)
    for A in As:
        for c in range(16):
            classes[f4.signature(A, c)].append(A * 16 + c)
    pairs, sig_of = set(), {}
    for sig, members in classes.items():
        for code in members:
            sig_of[code] = sig
        os_ = sorted({orbit[m] for m in members})
        pairs.update((x, y) for k, x in enumerate(os_) for y in os_[k + 1:])
    return sorted(pairs), classes, orbit, sig_of


def select():
    t0 = time.time()
    op, classes, orbit, sig_of = orbit_pairs()
    parent = {(p["orbit_a"], p["orbit_b"]) for p in json.load(open(os.path.join(OUT, "screen4.json")))["study_pairs"]}
    fresh = [p for p in op if p not in parent]
    assert len(op) == 1872 and len(parent) == 40 and len(fresh) == 1832
    pick = np.random.default_rng(SEED_SAMPLE).choice(len(fresh), M_FU, replace=False)
    pairs, ok = [], 0
    for q, ix in enumerate(pick):
        O1, O2 = fresh[int(ix)]
        a = O1
        b = sorted(code for code in classes[sig_of[a]] if orbit[code] == O2)[0]
        (Aa, ca), (Ab, cb) = (a // 16, a % 16), (b // 16, b % 16)
        prof_eq = f4.exact_profiles(Aa, ca, 20) == f4.exact_profiles(Ab, cb, 20)
        tpm_diff = not np.array_equal(f4.tpm_int(Aa, ca), f4.tpm_int(Ab, cb))
        noniso = not f4.isomorphic((Aa, ca), (Ab, cb))
        ok += int(prof_eq and tpm_diff and noniso)
        pairs.append(dict(q=q, a=[Aa, ca], b=[Ab, cb], orbit_a=O1, orbit_b=O2,
                          v_profiles_equal=prof_eq, v_tpm_differ=tpm_diff, v_non_isomorphic=noniso))
    msg = "follow-up selection: fresh orbit pairs %d ; drawn %d ; exact checks passed %d/%d (%.1fs)" % (
        len(fresh), len(pairs), ok, len(pairs), time.time() - t0)
    print(msg)
    if ok != len(pairs):
        print("STOP RULE: exact check failed")
    json.dump(dict(message=msg, exact_checks_passed=ok, pairs=pairs), open(os.path.join(OUT, "followup_pairs.json"), "w"), indent=1)


def run_pair(pr, smoke=False):
    q = pr["q"]
    systems = [tuple(pr["a"]), tuple(pr["b"])]
    ntr, nte = (5, 5) if smoke else (s4.N_TRAIN, s4.N_TEST)
    base = 999000 if smoke else SEED_TRAJ
    names = ["R", "C1_TE", "C1_TE_MM", "C2_JRR", "C4_SHREC"]
    feats = {nm: {0: [], 1: []} for nm in names}
    TC = {0: [], 1: []}
    for m, (A16, c) in enumerate(systems):
        rules = f4.rules_of(A16, c)
        for r in range(ntr + nte):
            x = trajectory(rules, s4.STEPS, np.random.default_rng(base + 1000 * q + 500 * m + r), flip=s4.FLIP,
                           warmup=s4.WARM).astype(int)
            feats["R"][m].append(s4.f_R(x)); feats["C1_TE"][m].append(s4.f_TE(x)); feats["C1_TE_MM"][m].append(f_TE_MM(x))
            feats["C2_JRR"][m].append(s4.f_JRR(x)); feats["C4_SHREC"][m].append(s4.f_SHREC(x))
            TC[m].append(s4.trans_counts(x))
    ytr = np.r_[np.zeros(ntr), np.ones(ntr)].astype(int); yte = np.r_[np.zeros(nte), np.ones(nte)].astype(int)
    res = {}
    for nm, F in feats.items():
        F0, F1 = np.array(F[0], float), np.array(F[1], float)
        res[nm] = s4.ncc(np.vstack([F0[:ntr], F1[:ntr]]), ytr, np.vstack([F0[ntr:], F1[ntr:]]), yte)
    L = [np.log((sum(TC[m][:ntr]) + 1) / (sum(TC[m][:ntr]) + 1).sum(1, keepdims=True)) for m in (0, 1)]
    res["C0_likelihood"] = sum(int(int((T * L[1]).sum() > (T * L[0]).sum()) == m) for m in (0, 1) for T in TC[m][ntr:])
    ex = [s4.exact_pop(*systems[0]), s4.exact_pop(*systems[1])]
    exact = {nm: max(abs(float(u) - float(v)) for u, v in zip(ex[0][nm], ex[1][nm])) for nm in ("C1_TE", "C2_JRR")}
    return dict(q=q, a=pr["a"], b=pr["b"], n_test=2 * nte, correct=res, exact_maxdiff=exact)


def verdict(k, n):
    lo, hi = s4.wilson(k, n, Z_CLS)
    return (lo, hi), ("generally separates" if lo > 0.5 else "generally fails" if hi < 0.5 else "unresolved")


def combine():
    rows = []
    for f in sorted(glob.glob(os.path.join(OUT, "followup_part_*.json"))):
        rows += json.load(open(f))["pairs"]
    rows.sort(key=lambda r: r["q"])
    qs = [r["q"] for r in rows]
    assert len(set(qs)) == len(qs)
    M = len(rows)
    for r in rows:
        r["separates"] = {nm: bool(s4.wilson(k, r["n_test"], Z_PAIR)[0] > 0.5) for nm, k in r["correct"].items()}
    lines = ["pairs completed: %d of %d ; per-pair z = %.4f (parent, fixed) ; per-classifier z = %.4f (Bonferroni over 2)"
             % (M, M_FU, Z_PAIR, Z_CLS)]
    # manipulation checks
    accR = np.array([r["correct"]["R"] / r["n_test"] for r in rows])
    sepR = sum(r["separates"]["R"] for r in rows); sep0 = sum(r["separates"]["C0_likelihood"] for r in rows)
    chk_ok = bool(0.45 <= accR.mean() <= 0.55 and sepR < 0.05 * M and sep0 >= 0.95 * M)
    lines.append("manipulation checks: R mean acc %.4f, R separated %d/%d ; C0 separated %d/%d -> %s"
                 % (accR.mean(), sepR, M, sep0, M, "PASS" if chk_ok else "FAIL"))
    summ = {}
    for nm in PRIMARY:
        k = sum(r["separates"][nm] for r in rows)
        ci, v = verdict(k, M)
        if not chk_ok:
            v = "unresolved (pipeline check failed)"
        acc = np.array([r["correct"][nm] / r["n_test"] for r in rows])
        summ[nm] = dict(pairs_separated=k, M=M, prop=k / M, wilson_bonf2=list(ci), verdict=v, mean_acc=float(acc.mean()))
        lines.append("PRIMARY %-9s separated %3d/%d  prop %.3f  Wilson(Bonf 2) [%.3f, %.3f]  -> %s   (mean acc %.3f)"
                     % (nm, k, M, k / M, ci[0], ci[1], v, acc.mean()))
    # pooled with parent (descriptive)
    parent = json.load(open(os.path.join(OUT, "study4.json")))["pairs"]
    pooled = {}
    for nm in PRIMARY:
        k = sum(r["separates"][nm] for r in rows) + sum(bool(r["separates"][nm]) for r in parent)
        n = M + len(parent)
        ci, v = verdict(k, n)
        pooled[nm] = dict(k=k, n=n, ci=list(ci), verdict=v)
        lines.append("pooled (descriptive) %-9s %d/%d  [%.3f, %.3f] -> %s" % (nm, k, n, ci[0], ci[1], v))
    # secondary
    sec = {}
    ex_te = [r["exact_maxdiff"]["C1_TE"] > 1e-12 for r in rows]
    ex_jr = [r["exact_maxdiff"]["C2_JRR"] > 1e-12 for r in rows]
    for nm, ex in (("C1_TE", ex_te), ("C1_TE_MM", ex_te), ("C2_JRR", ex_jr)):
        fs = [r["separates"][nm] for r in rows]
        sec[nm] = dict(exact_separates=sum(ex), finite_separates=sum(fs), agree=sum(e == f for e, f in zip(ex, fs)),
                       exact_only=sum(e and not f for e, f in zip(ex, fs)), finite_only=sum(f and not e for e, f in zip(ex, fs)))
        lines.append("secondary %-8s exact separates %d/%d ; finite separates %d ; agree %d ; exact-only %d ; finite-only %d"
                     % (nm, sec[nm]["exact_separates"], M, sec[nm]["finite_separates"], sec[nm]["agree"],
                        sec[nm]["exact_only"], sec[nm]["finite_only"]))
    txt = "\n".join(lines) + "\n"
    print(txt, end="")
    open(os.path.join(OUT, "followup.txt"), "w").write(txt)
    json.dump(dict(M=M, z_pair=Z_PAIR, z_cls=Z_CLS, manipulation_checks_pass=chk_ok, summary=summ, pooled=pooled,
                   secondary=sec, pairs=rows), open(os.path.join(OUT, "followup.json"), "w"), indent=1)


def main(argv):
    if argv[0] == "--select":
        select()
    elif argv[0] == "--smoke":
        pairs = json.load(open(os.path.join(OUT, "followup_pairs.json")))["pairs"][:2]
        for pr in pairs:
            t = time.time(); r = run_pair(pr, smoke=True)
            print("SMOKE (discarded)", r["q"], r["correct"], "%.1fs" % (time.time() - t))
    elif argv[0] == "--part":
        lo, hi = int(argv[1]), int(argv[2])
        pairs = json.load(open(os.path.join(OUT, "followup_pairs.json")))["pairs"][lo:hi]
        out = os.path.join(OUT, "followup_part_%03d_%03d.json" % (lo, hi))
        done = []
        t0 = time.time()
        for pr in pairs:
            done.append(run_pair(pr))
            json.dump(dict(pairs=done), open(out, "w"))
            print("pair %d done (%.0fs)" % (pr["q"], time.time() - t0), flush=True)
    elif argv[0] == "--combine":
        combine()


if __name__ == "__main__":
    main(sys.argv[1:])
