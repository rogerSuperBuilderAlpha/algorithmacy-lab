"""Exact screen of the 4-node family F4 (PREREGISTRATION.md sections 3 and 5): S0-S4, V1, the sampling of
M = 40 study orbit pairs, and V2 on those pairs. Output: results/screen4.{txt,json}."""
import json
import os
import random
import sys
import time
from collections import defaultdict

import numpy as np

from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import f4

OUT = os.path.join(os.path.dirname(__file__), "results")
M_PAIRS = 40


def main():
    t0 = time.time()
    lines = []

    def log(s):
        print(s, flush=True); lines.append(s)

    As = f4.invertible_As()
    log("S0: |GL(4,2)| = %d ; systems = %d" % (len(As), 16 * len(As)))
    codes, orb = f4.orbit_ids(As)
    orbit = dict(zip(codes.tolist(), orb.tolist()))
    log("S3 prep: orbits under G (384 maps) = %d (%.1fs)" % (len(set(orb.tolist())), time.time() - t0))
    classes = defaultdict(list)
    for A in As:
        for c in range(16):
            classes[f4.signature(A, c)].append(A * 16 + c)
    sizes = [len(v) for v in classes.values()]
    log("S1/S2: recurrence-equal classes = %d ; multi-member = %d ; largest = %d (%.1fs)"
        % (len(classes), sum(s > 1 for s in sizes), max(sizes), time.time() - t0))
    multi_orbit, noniso_pairs, orbit_pairs = 0, 0, set()
    for members in classes.values():
        cnt = defaultdict(int)
        for code in members:
            cnt[orbit[code]] += 1
        if len(cnt) >= 2:
            multi_orbit += 1
            n = len(members)
            noniso_pairs += (n * n - sum(v * v for v in cnt.values())) // 2
            os_ = sorted(cnt)
            for x in range(len(os_)):
                for y in range(x + 1, len(os_)):
                    orbit_pairs.add((os_[x], os_[y]))
    log("S3: classes with >= 2 orbits = %d ; unordered non-isomorphic system pairs = %d ; unordered orbit pairs = %d"
        % (multi_orbit, noniso_pairs, len(orbit_pairs)))
    log("S4: law difference holds for every distinct (A,c) (distinct maps => distinct TPMs; Prop 2); checked in V2")
    if not orbit_pairs:
        log("STOP RULE: zero non-isomorphic recurrence-equal pairs at n = 4 (H1 false). Stopping.")
        open(os.path.join(OUT, "screen4.txt"), "w").write("\n".join(lines) + "\n")
        return
    # V1
    rng = np.random.default_rng(4210001)
    idx = rng.choice(len(As) * 16, 300, replace=False)
    v1_ok = 0
    for x in idx:
        A, c = As[int(x) // 16], int(x) % 16
        marg, prof = f4.exact_profiles(A, c, 20)
        p1 = f4.prop1_profiles(A, c, 20)
        v1_ok += int(all(m == f4.Fraction(1, 2) for m in marg) and all(prof[k] == p1[k] for k in prof))
    log("V1: Prop-1 closed form == brute-force exact profiles (lags 0..20, all i,j) and marginals 1/2: %d/300 (%.1fs)"
        % (v1_ok, time.time() - t0))
    if v1_ok != 300:
        log("STOP RULE: V1 failed."); open(os.path.join(OUT, "screen4.txt"), "w").write("\n".join(lines) + "\n"); return
    # sampling
    op = sorted(orbit_pairs)
    rng2 = np.random.default_rng(4210002)
    pick = rng2.choice(len(op), min(M_PAIRS, len(op)), replace=False)
    sig_of = {}
    for sig, members in classes.items():
        for code in members:
            sig_of[code] = sig
    pairs = []
    for q, ix in enumerate(pick):
        O1, O2 = op[int(ix)]
        a = O1  # orbit id == minimal code == canonical representative
        cls = classes[sig_of[a]]
        bs = sorted(code for code in cls if orbit[code] == O2)
        assert bs, "canonical rep of O1 has no O2 co-member (should be impossible)"
        b = bs[0]
        pairs.append(dict(q=q, a=[a // 16, a % 16], b=[b // 16, b % 16], orbit_a=O1, orbit_b=O2))
    # V2
    v2_ok = 0
    for pr in pairs:
        (Aa, ca), (Ab, cb) = pr["a"], pr["b"]
        ma, pa = f4.exact_profiles(Aa, ca, 20); mb, pb = f4.exact_profiles(Ab, cb, 20)
        prof_eq = ma == mb and pa == pb
        tpm_diff = not np.array_equal(f4.tpm_int(Aa, ca), f4.tpm_int(Ab, cb))
        noniso = not f4.isomorphic((Aa, ca), (Ab, cb))
        pr.update(v2_profiles_equal=prof_eq, v2_tpm_differ=tpm_diff, v2_non_isomorphic=noniso,
                  rows_a=f4.rows(Aa), rows_b=f4.rows(Ab))
        v2_ok += int(prof_eq and tpm_diff and noniso)
    log("V2: study pairs with exact profiles equal (lags 0..20) & TPMs differ & non-isomorphic (384 maps): %d/%d (%.1fs)"
        % (v2_ok, len(pairs), time.time() - t0))
    if v2_ok != len(pairs):
        log("STOP RULE: V2 failed.")
    rowdiff = defaultdict(int)
    for pr in pairs:
        rowdiff[sum(ra != rb for ra, rb in zip(pr["rows_a"], pr["rows_b"]))] += 1
    log("study pairs: number of differing update rows (A only) -> count: %s" % dict(sorted(rowdiff.items())))
    log("total %.1fs" % (time.time() - t0))
    json.dump(dict(counts=dict(GL42=len(As), systems=16 * len(As), orbits=len(set(orb.tolist())),
                               classes=len(classes), multi_member_classes=sum(s > 1 for s in sizes),
                               largest_class=max(sizes), classes_ge2_orbits=multi_orbit,
                               noniso_system_pairs=noniso_pairs, orbit_pairs=len(orbit_pairs)),
                   v1_pass=v1_ok, v2_pass=v2_ok, study_pairs=pairs),
              open(os.path.join(OUT, "screen4.json"), "w"), indent=1)
    open(os.path.join(OUT, "screen4.txt"), "w").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
