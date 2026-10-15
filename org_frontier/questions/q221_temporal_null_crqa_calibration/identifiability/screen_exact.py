"""Stricter EXACT screen over the existing 7488 bounded-search candidate pairs (no new search; Hassan 2026-10-15).
Stages (each exact rational, flip = 2/25, noisy chain, true stationary law):
  S0 all candidate pairs (pair_search.json all_candidates)
  S1 no constant-rule node in either member
  S2 + equal stationary single-channel marginals P(x_i = 1), i = X, Y, H
  S3 + equal within-channel self-recurrence profiles P(x_i(t) = x_i(t+k)), k = 0..20, all 3 channels
  S4 + exact cross-profile re-check (6 ordered pairs, lags 0..20) on survivors
Counts are reported for raw pairs, pairs unique up to node permutation, and up to the 48-group."""
import json
import os
from fractions import Fraction

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps

OUT = os.path.join(os.path.dirname(__file__), "results")
F = Fraction(2, 25)
TABLES = {}
for gen in (ps.nsi_forms, ps.affine_forms):
    for fid, tab in gen():
        TABLES[tuple(fid)] = tab


def complement(t, m):
    return tuple(tuple(t[j][s ^ m] ^ ((m >> j) & 1) for s in range(8)) for j in range(3))


def ext_canon(t):
    return min(ps.permute_tables(complement(t, m), p) for m in range(8) for p in ps.PERMS)


def perm_canon(t):
    return min(ps.permute_tables(t, p) for p in ps.PERMS)


def tpm(t):
    P = []
    for s in range(8):
        row = []
        for z in range(8):
            p = Fraction(1)
            for j in range(3):
                p *= (1 - F) if ((z >> j) & 1) == t[j][s] else F
            row.append(p)
        P.append(row)
    return P


def stationary(P):
    # solve pi (P - I) = 0, sum pi = 1 by exact Gaussian elimination
    n = 8
    A = [[P[j][i] - (1 if i == j else 0) for j in range(n)] for i in range(n)]
    A[-1] = [Fraction(1)] * n
    b = [Fraction(0)] * (n - 1) + [Fraction(1)]
    M = [A[i] + [b[i]] for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    pi = [M[i][n] for i in range(n)]
    assert all(sum(pi[s] * P[s][z] for s in range(8)) == pi[z] for z in range(8))
    return pi


CACHE = {}


def stats(fid):
    if fid in CACHE:
        return CACHE[fid]
    t = TABLES[fid]
    P = tpm(t)
    pi = stationary(P)
    marg = tuple(sum(pi[s] for s in range(8) if (s >> i) & 1) for i in range(3))
    prof = {}
    J = [[pi[s] if s == z else Fraction(0) for z in range(8)] for s in range(8)]
    for k in range(21):
        for i in range(3):
            for j in range(3):
                prof[(i, j, k)] = sum(J[s][z] for s in range(8) for z in range(8) if ((s >> i) & 1) == ((z >> j) & 1))
        J = [[sum(J[s][u] * P[u][z] for u in range(8)) for z in range(8)] for s in range(8)]
    auto = tuple(prof[(i, i, k)] for i in range(3) for k in range(21))
    cross = tuple(prof[(i, j, k)] for i in range(3) for j in range(3) if i != j for k in range(21))
    const = any(len(set(t[j])) == 1 for j in range(3))
    CACHE[fid] = (const, marg, auto, cross)
    return CACHE[fid]


def main():
    d = json.load(open(os.path.join(OUT, "pair_search.json")))
    pairs = [(tuple(a), tuple(b)) for a, b in d["all_candidates"]]


    def counts(ps_):
        nperm = {tuple(sorted([str(perm_canon(TABLES[a])), str(perm_canon(TABLES[b]))])) for a, b in ps_}
        ext = {tuple(sorted([str(ext_canon(TABLES[a])), str(ext_canon(TABLES[b]))])) for a, b in ps_
               if ext_canon(TABLES[a]) != ext_canon(TABLES[b])}
        return dict(pairs=len(ps_), unique_node_perm=len(nperm), unique_48group_nonisomorphic=len(ext))


    stages = [("S0 all candidates", pairs)]
    s1 = [(a, b) for a, b in pairs if not stats(a)[0] and not stats(b)[0]]
    stages.append(("S1 no constant node", s1))
    s2 = [(a, b) for a, b in s1 if stats(a)[1] == stats(b)[1]]
    stages.append(("S2 + equal stationary channel marginals", s2))
    s3 = [(a, b) for a, b in s2 if stats(a)[2] == stats(b)[2]]
    stages.append(("S3 + equal self-recurrence profiles (lags 0..20)", s3))
    s4 = [(a, b) for a, b in s3 if stats(a)[3] == stats(b)[3]]
    stages.append(("S4 + exact cross-profile re-check", s4))
    s5 = [(a, b) for a, b in s4 if ext_canon(TABLES[a]) != ext_canon(TABLES[b])]
    stages.append(("S5 + not 48-group isomorphic", s5))
    res = {"stages": []}
    for name, sp in stages:
        c = counts(sp)
        res["stages"].append(dict(stage=name, **c))
        print("%-52s pairs=%5d  unique(node perm)=%4d  unique(48-group, non-iso)=%3d" % (name, c["pairs"], c["unique_node_perm"], c["unique_48group_nonisomorphic"]))
    seen, surv = set(), []
    for a, b in s5:
        k = tuple(sorted([str(ext_canon(TABLES[a])), str(ext_canon(TABLES[b]))]))
        if k not in seen:
            seen.add(k)
            surv.append(dict(a=a, b=b, a_tables=TABLES[a], b_tables=TABLES[b],
                             marginals=[str(x) for x in stats(a)[1]]))
    res["survivors_48group_unique"] = surv
    for s in surv:
        print("survivor:", s["a"], s["b"], "marginals", s["marginals"])
    json.dump(res, open(os.path.join(OUT, "screen_exact.json"), "w"), indent=1, default=list)


if __name__ == "__main__":
    main()
