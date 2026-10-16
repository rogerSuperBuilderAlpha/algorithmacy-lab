"""Adjudication inputs for the bounded-search candidates (EXACT_PHI_DECISION_RULES.md), on the 74 pairs that are
unique up to the 48-group {node permutation} x {per-node value relabeling}:
 (a) constant-node flag: a member has a node whose deterministic rule is constant (0 or 1);
 (b) all-lag equality: exact rational profiles to lag 40 for representatives (beyond the 16 needed by the
     order-16 linear-recurrence argument);
 (c) finite-sample q220 pipeline on a representative no-constant-node pair (rule 5, separate);
 (d) tie/tolerance: B margin and core tie gap for every member (rule 2);
 (e) univariate marginal means and auto profiles (what else distinguishes the pair).
Seeds for (c): trajectory default_rng(43_000 + r), r < 400 (disjoint from q220 and other q221 ranges)."""
import json
import os
import sys
from fractions import Fraction

import numpy as np

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.pair_search_data import load as load_pair_search

OUT = os.path.join(os.path.dirname(__file__), "results")
TABLES = {}
for gen in (ps.nsi_forms, ps.affine_forms):
    for fid, tab in gen():
        TABLES[tuple(fid)] = tab


def complement(t, m):
    return tuple(tuple(t[j][s ^ m] ^ ((m >> j) & 1) for s in range(8)) for j in range(3))


def ext_canon(t):
    return min(ps.permute_tables(complement(t, m), p) for m in range(8) for p in ps.PERMS)


def const_nodes(t):
    return [j for j in range(3) if len(set(t[j])) == 1]


def marg(t):
    P = ps.sbs(t)
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1))]); pi /= pi.sum()
    autos, Pk = [], np.eye(8)
    for k in range(1, 21):
        Pk = Pk @ P
        autos.append([pi @ ((ps.IND[i][:, None] == ps.IND[i][None, :]) * Pk).sum(1) for i in range(3)])
    return ps.IND @ pi, np.array(autos)


d = load_pair_search()
ue = {}
for a, b in d["all_candidates"]:
    ta, tb = TABLES[tuple(a)], TABLES[tuple(b)]
    ca, cb = ext_canon(ta), ext_canon(tb)
    if ca != cb:
        ue.setdefault(tuple(sorted([str(ca), str(cb)])), (tuple(a), tuple(b)))
pairs = list(ue.values())
cache = {}
rows = []
for a, b in pairs:
    r = {"a": a, "b": b}
    for nm, fid in (("a", a), ("b", b)):
        t = TABLES[fid]
        tg = ps.targets(t, cache)
        r[nm + "_const_nodes"] = const_nodes(t)
        r[nm + "_target"] = tg
        r[nm + "_B_margin"] = ps.b_margin(tg)
        r[nm + "_rules"] = ps_desc = None
    ma, aa = marg(TABLES[a]); mb, ab = marg(TABLES[b])
    r["same_means"] = bool(np.allclose(ma, mb, atol=1e-12, rtol=0))
    r["same_auto"] = bool(np.allclose(aa, ab, atol=1e-12, rtol=0))
    r["no_constant_node"] = not r["a_const_nodes"] and not r["b_const_nodes"]
    rows.append(r)
nc = [r for r in rows if r["no_constant_node"]]
print("48-group-unique candidate pairs: %d" % len(rows))
print("  with a constant-rule node in either member: %d ; with NO constant node: %d" % (len(rows) - len(nc), len(nc)))
print("  same univariate means: %d (no-constant subset %d); same auto profiles: %d (no-constant subset %d); both: %d"
      % (sum(r["same_means"] for r in rows), sum(r["same_means"] for r in nc), sum(r["same_auto"] for r in rows),
         sum(r["same_auto"] for r in nc), sum(r["same_means"] and r["same_auto"] for r in rows)))
print("  min B margin over all members: %.4f" % min(min(r["a_B_margin"], r["b_B_margin"]) for r in rows))

# (d) core tie gap for every member of the no-constant subset (and all if small)
gaps = []
for r in (nc if nc else rows):
    for nm in ("a", "b"):
        g, _ = ps.core_tie_gap(TABLES[r[nm]])
        r[nm + "_core_tie_gap"] = g
        gaps.append(g)
print("  core tie gap over checked members: min %.4f (n=%d)" % (min(gaps), len(gaps)))


def desc(t):
    L = "XYH"
    out = []
    for j in range(3):
        ones = [s for s in range(8) if t[j][s]]
        out.append("%s'=%s" % (L[j], "{" + ",".join("".join(L[k] if (s >> k) & 1 else "~" + L[k] for k in range(3)) for s in ones) + "}"))
    return "; ".join(out)


rep_pool = nc if nc else rows
rep_pool = sorted(rep_pool, key=lambda r: (r["same_means"] is False, r["same_auto"] is False,
                                            sum(map(sum, TABLES[r["a"]])) + sum(map(sum, TABLES[r["b"]]))))
rep = rep_pool[0]
print("\nREPRESENTATIVE pair:", rep["a"], "vs", rep["b"])
for nm in ("a", "b"):
    print("  %s rules (minterms where next=1): %s" % (nm, desc(TABLES[rep[nm]])))
    print("     target: %s ; B margin %.4f ; core tie gap %s ; const nodes %s"
          % (rep[nm + "_target"], rep[nm + "_B_margin"], rep.get(nm + "_core_tie_gap"), rep[nm + "_const_nodes"]))
print("  same means %s ; same auto %s" % (rep["same_means"], rep["same_auto"]))

# (b) exact rational to lag 40
pa = ps.exact_profile(TABLES[rep["a"]], max_lag=40)
pb = ps.exact_profile(TABLES[rep["b"]], max_lag=40)
print("  (b) exact rational cross profiles equal at all 6 ordered pairs x lags 0..40 (=> -40..40):", pa == pb)

# (c) finite-sample, q220 pipeline
from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
R = int(os.environ.get("Q221_ADJ_R", "400"))
fs = {}
for nm in ("a", "b"):
    rules = ps.table_form(TABLES[rep[nm]])
    Bset = set(rep[nm + "_target"]["B"])
    other = set(rep[("b" if nm == "a" else "a") + "_target"]["B"])
    st = {k: [] for k in ("maxprom", "anyev", "noev", "score_own", "score_other", "mean_x", "mean_y", "mean_h")}
    picks = np.zeros(3)
    for r in range(R):
        raw = trajectory(rules, 600, np.random.default_rng(43_000 + r), flip=0.08, warmup=20)
        c = ob.coupling(np.arange(600), raw, 10, "timestamp", 30)
        cc = ob.centrality(c["prom"], 0.05)
        s_own, _, noev = ob.bottleneck_scores(cc, Bset)
        s_oth, _, _ = ob.bottleneck_scores(cc, other)
        p = c["prom"][np.triu_indices(3, 1)]
        st["maxprom"].append(p.max()); st["anyev"].append(float((p > 0.05).any())); st["noev"].append(float(noev))
        st["score_own"].append(s_own); st["score_other"].append(s_oth)
        m = raw.mean(0); st["mean_x"].append(m[0]); st["mean_y"].append(m[1]); st["mean_h"].append(m[2])
        M = np.flatnonzero(cc >= cc.max() - 1e-12)
        picks[M] += 1.0 / M.size
    fs[nm] = {k: (float(np.mean(v)), float(np.std(v, ddof=1) / np.sqrt(R))) for k, v in st.items()}
    fs[nm]["pick_share_XYH"] = (picks / R).round(4).tolist()
    print("  (c) %s: " % nm + "; ".join("%s %.4f±%.4f" % (k, v[0], v[1]) for k, v in fs[nm].items() if k != "pick_share_XYH")
          + "; tie-aware pick share X/Y/H %s" % fs[nm]["pick_share_XYH"])
json.dump({"rows": rows, "representative": rep, "finite_sample": fs, "R": R},
          open(os.path.join(OUT, "adjudicate.json"), "w"), indent=1, default=str)
