"""Bounded exhaustive search for an IIT-target counterexample inside the q220 family (3 nodes, flip 0.08):
two forms with IDENTICAL population pairwise cross match profiles (all ordered pairs, lags -20..20) but
DIFFERENT, NON-DEGENERATE q161 bottleneck sets.

Spaces searched:
  S1 "nsi"    every 3-node form in q162's random_wiring family (each node an arbitrary Boolean function of the
              OTHER two nodes; this is q220's R2 family) : 16^3 = 4096 forms
  S2 "affine" every 3-node form whose rules are affine over GF(2) of all three nodes (self-inputs allowed;
              contains Hassan's A/B pair)                                                  : 16^3 = 4096 forms
Non-degenerate target (q220 R2 inclusion rule, forms_r2.py): q161 core size >= 2 and bottleneck set B
non-empty with |B| < n.

Stage 1 (numpy only): exact profiles by linear algebra on the 8-state chain; group by profile (rounded 1e-9).
Stage 2 (pyphi): q161 core_indices / bottleneck_set for every form in a multi-member group, computed once per
node-permutation orbit (targets are relabelled back), checkpointed to results/pair_search_phi.json.
Stage 3: exact rational re-verification (fractions, flip = 2/25) of every candidate pair at lags -20..20.
"""
import itertools
import json
import os
import sys
import time
from collections import defaultdict
from fractions import Fraction

import numpy as np

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import exact_profiles as ep

OUT = os.path.join(os.path.dirname(__file__), "results")
PHI_CACHE = os.path.join(OUT, "pair_search_phi.json")
L = ("X", "Y", "H")
PERMS = list(itertools.permutations(range(3)))


# ---------------------------------------------------------------- forms as truth tables over the full state
def table_form(tables):
    """tables[j] = tuple of 8 output bits indexed by state s (little-endian)."""
    return [(lambda x, t=t: t[x[0] | (x[1] << 1) | (x[2] << 2)]) for t in tables]


def nsi_forms():
    for codes in itertools.product(range(16), repeat=3):
        tables = []
        for j, c in enumerate(codes):
            ins = [k for k in range(3) if k != j]
            tables.append(tuple((c >> (((s >> ins[0]) & 1) | (((s >> ins[1]) & 1) << 1))) & 1 for s in range(8)))
        yield ("nsi",) + codes, tuple(tables)


def affine_forms():
    opts = [(m, c) for m in range(8) for c in (0, 1)]
    for combo in itertools.product(opts, repeat=3):
        tables = tuple(tuple(c ^ (bin(s & m).count("1") & 1) for s in range(8)) for (m, c) in combo)
        yield ("aff",) + tuple(m * 2 + c for (m, c) in combo), tables


def permute_tables(tables, p):
    """Relabel nodes: new node p[j] is old node j. Returns the new tables."""
    inv = [0] * 3
    for j in range(3):
        inv[p[j]] = j
    new = [None] * 3
    for j in range(3):
        out = []
        for s_new in range(8):
            b_new = [(s_new >> k) & 1 for k in range(3)]
            s_old = sum(b_new[p[k]] << k for k in range(3))
            out.append(tables[j][s_old])
        new[p[j]] = tuple(out)
    return tuple(new)


def canon(tables):
    best = None
    for p in PERMS:
        t = permute_tables(tables, p)
        if best is None or t < best[0]:
            best = (t, p)
    return best


# ---------------------------------------------------------------- exact profiles (vectorised over lags)
NM = None


def sbs(tables, flip=ep.FLIP):
    global NM
    if NM is None:
        NM = np.array([[np.prod([(1 - flip) if ((a >> k) & 1) == ((b >> k) & 1) else flip for k in range(3)])
                        for b in range(8)] for a in range(8)])
    f = [sum(tables[j][s] << j for j in range(3)) for s in range(8)]
    return NM[f, :]


IND = np.array([[(s >> j) & 1 for s in range(8)] for j in range(3)], dtype=float)


def profile_vec(tables, max_lag=ep.MAX_LAG):
    P = sbs(tables)
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1))]); pi /= pi.sum()
    Pk = [np.eye(8)]
    for _ in range(max_lag):
        Pk.append(Pk[-1] @ P)
    Pk = np.array(Pk)                                            # (K+1, 8, 8)
    out = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            a, b = IND[i], IND[j]
            pos = np.einsum("s,s,kst,t->k", pi, a, Pk, b) + np.einsum("s,s,kst,t->k", pi, 1 - a, Pk, 1 - b)
            out.append(pos)                                      # lags 0..K for (i -> j); negative lags = (j -> i)
    return np.concatenate(out), pi


def stage1():
    t0 = time.time()
    groups = defaultdict(list)
    for gen in (nsi_forms, affine_forms):
        for fid, tables in gen():
            vec, _ = profile_vec(tables)
            groups[tuple(np.round(vec, 9).tolist())].append((fid, tables))
    multi = [g for g in groups.values() if len(g) > 1]
    n_forms = sum(len(g) for g in groups.values())
    print("stage1: %d forms, %d distinct cross-profile classes, %d classes with >1 member covering %d forms (%.1fs)"
          % (n_forms, len(groups), len(multi), sum(len(g) for g in multi), time.time() - t0), flush=True)
    return multi


def targets(tables, cache):
    from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
        core_indices, bottleneck_set)
    ct, p = canon(tables)
    key = str(ct)
    if key not in cache:
        rules = table_form(ct)
        ci, phi = core_indices(rules, L)
        bset, base, drops = bottleneck_set(rules, L)
        cache[key] = {"core": list(ci) if ci else [], "phi": phi, "B": sorted(bset), "base": base,
                      "drops": [float(d) for d in drops]}
    c = cache[key]
    # canonical node p[j] is original node j  ->  map back
    inv = {p[j]: j for j in range(3)}
    return {"core": sorted(inv[i] for i in c["core"]), "phi": c["phi"], "B": sorted(inv[i] for i in c["B"]),
            "base": c["base"], "drops": [c["drops"][p[j]] for j in range(3)]}


def eligible(t):
    return len(t["core"]) >= 2 and 0 < len(t["B"]) < 3


def exact_profile(tables, max_lag=ep.MAX_LAG):
    fl = Fraction(2, 25)
    f = [sum(tables[j][s] << j for j in range(3)) for s in range(8)]
    N = [[np.prod([(1 - fl) if ((a >> k) & 1) == ((b >> k) & 1) else fl for k in range(3)]) for b in range(8)]
         for a in range(8)]
    P = [N[f[s]] for s in range(8)]
    # stationary law: solve pi P = pi exactly by power-free Gaussian elimination
    A = [[P[r][c] - (1 if r == c else 0) for r in range(8)] for c in range(8)]   # (P^T - I)
    A[-1] = [Fraction(1)] * 8
    rhs = [Fraction(0)] * 7 + [Fraction(1)]
    M = [row[:] + [rhs[i]] for i, row in enumerate(A)]
    for c in range(8):
        piv = next(r for r in range(c, 8) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for r in range(8):
            if r != c and M[r][c] != 0:
                fac = M[r][c] / M[c][c]
                M[r] = [x - fac * y for x, y in zip(M[r], M[c])]
    pi = [M[i][8] / M[i][i] for i in range(8)]
    out = {}
    dist = pi[:]
    rows = [[pi[s] if t == s else Fraction(0) for t in range(8)] for s in range(8)]  # joint at lag k: pi_s P^k(s,t)
    J = [[pi[s] * (1 if s == t else 0) for t in range(8)] for s in range(8)]
    for k in range(max_lag + 1):
        for i in range(3):
            for j in range(3):
                if i != j:
                    out[(i, j, k)] = sum(J[s][t] for s in range(8) for t in range(8)
                                         if ((s >> i) & 1) == ((t >> j) & 1))
        J = [[sum(J[s][u] * P[u][t] for u in range(8)) for t in range(8)] for s in range(8)]
    return out


def main():
    multi = stage1()
    cache = json.load(open(PHI_CACHE)) if os.path.exists(PHI_CACHE) else {}
    found, n_done, t0 = [], 0, time.time()
    budget = float(os.environ.get("Q221_SEARCH_BUDGET_S", "1800"))
    stats = {"groups": len(multi), "groups_with_2plus_eligible": 0, "groups_with_distinct_eligible_B": 0}
    for gi, g in enumerate(multi):
        if time.time() - t0 > budget:
            print("BUDGET EXHAUSTED at group %d/%d" % (gi, len(multi)), flush=True)
            stats["budget_exhausted_at_group"] = gi
            break
        tg = [(fid, tables, targets(tables, cache)) for fid, tables in g]
        el = [x for x in tg if eligible(x[2])]
        if len(el) >= 2:
            stats["groups_with_2plus_eligible"] += 1
            bs = {tuple(x[2]["B"]) for x in el}
            if len(bs) > 1:
                stats["groups_with_distinct_eligible_B"] += 1
                found.append([(list(fid), [list(t) for t in tables], x) for fid, tables, x in el])
        n_done += 1
        if gi % 25 == 0:
            json.dump(cache, open(PHI_CACHE, "w"))
            print("group %d/%d  orbits cached %d  found %d  %.0fs" % (gi, len(multi), len(cache), len(found),
                                                                   time.time() - t0), flush=True)
    json.dump(cache, open(PHI_CACHE, "w"))
    stats["groups_processed"] = n_done
    stats["phi_orbits_computed"] = len(cache)
    # exact re-verification of the first members of each found group
    verified = []
    for grp in found[:50]:
        a, b = None, None
        for x in grp:
            for y in grp:
                if tuple(x[2]["B"]) != tuple(y[2]["B"]):
                    a, b = x, y
                    break
            if a:
                break
        pa, pb = exact_profile(tuple(map(tuple, a[1]))), exact_profile(tuple(map(tuple, b[1])))
        verified.append({"a": a, "b": b, "exact_equal_lags_0_20_all_ordered_pairs": pa == pb})
    json.dump({"stats": stats, "found_groups": found, "verified_pairs": verified},
              open(os.path.join(OUT, "pair_search.json"), "w"), indent=1)
    print("STATS", stats)
    for v in verified[:10]:
        print("PAIR", v["a"][0], v["a"][2]["B"], v["a"][2]["core"], "|", v["b"][0], v["b"][2]["B"], v["b"][2]["core"],
              "| exact-equal:", v["exact_equal_lags_0_20_all_ordered_pairs"])
    print("verified pairs:", len(verified), "all exact-equal:", all(v["exact_equal_lags_0_20_all_ordered_pairs"] for v in verified))


if __name__ == "__main__":
    main()
