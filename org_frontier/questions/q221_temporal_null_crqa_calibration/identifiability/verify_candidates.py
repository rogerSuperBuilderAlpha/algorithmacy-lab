"""Rule-2 / rule-7 follow-up on the post-rules search candidates (results/pair_search.json).

1. Extended isomorphism: rule 7 excludes pairs related by one of the 6 node permutations. Here every candidate is
   also checked against the 48-element group {node permutation} x {per-node 0/1 value relabeling}. Global or
   per-node value relabeling leaves cross match *equality* events unchanged only when the same relabeling is
   applied to both channels, so it can create profile-equal pairs that are the same transition system with
   renamed states. q161's leave-one-out target clamps a node to the value 0, which is not invariant under value
   relabeling. Such pairs are reported separately (they are a ground-truth-convention effect, not a dynamics one).
2. For representative candidates, an independent recomputation:
     (a) q161 core_indices / bottleneck_set / mc_phi on hand-decoded rules written as explicit lambdas;
     (b) an own PyPhi loop (not q161 code): max over reachable states of new_big_phi.maximal_complex, and
         leave-one-out with clamp-to-0 AND clamp-to-1;
     (c) exact rational cross profiles (Fraction, flip 2/25), lags -20..20, via ab_reproduce-style code.
"""
import itertools
import json
import os
from fractions import Fraction

import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    core_indices, bottleneck_set, mc_phi)
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
OUT = os.path.join(os.path.dirname(__file__), "results")
L = ("X", "Y", "H")

TABLES = {}
for gen in (ps.nsi_forms, ps.affine_forms):
    for fid, tab in gen():
        TABLES[tuple(fid)] = tab


def complement(tables, mask):
    """Relabel node k's values 0<->1 for k in mask (inputs and outputs)."""
    new = []
    for j in range(3):
        out = []
        for s in range(8):
            s_old = s ^ mask
            v = tables[j][s_old]
            out.append(v ^ ((mask >> j) & 1))
        new.append(tuple(out))
    return tuple(new)


def ext_canon(tables):
    return min(ps.permute_tables(complement(tables, m), p) for m in range(8) for p in ps.PERMS)


def own_targets(rules, clamp):
    def mcphi(rs):
        tpm, cm = tpm_from_rules(rs), cm_from_rules(rs)
        net = pyphi.Network(tpm, cm=cm, node_labels=L)
        best, core = 0.0, None
        for s in reachable_states(tpm, 3):
            st = tuple((s >> i) & 1 for i in range(3))
            try:
                mc = new_big_phi.maximal_complex(net, st)
            except (exceptions.StateUnreachableError, ValueError):
                continue
            if isinstance(mc, new_big_phi.NullPhiStructure):
                continue
            if float(mc.phi) > best:
                best, core = float(mc.phi), tuple(mc.node_indices)
        return best, core
    base, core = mcphi(rules)
    drops = []
    for k in range(3):
        fr = list(rules)
        fr[k] = (lambda x, c=clamp: c)
        drops.append(base - mcphi(fr)[0])
    mx = max(drops)
    B = sorted(i for i, d in enumerate(drops) if mx > 1e-6 and abs(d - mx) <= 1e-6)
    return base, core, drops, B


def exact_cross(tables):
    return ps.exact_profile(tables)


def describe(tables):
    """Human-readable minimal truth-table description of each node's rule."""
    out = []
    for j, t in enumerate(tables):
        terms = []
        for s in range(8):
            if t[s]:
                terms.append("".join(("" if (s >> k) & 1 else "~") + L[k] for k in range(3)))
        out.append("%s' = %s" % (L[j], " | ".join(terms) if terms else "0"))
    return "; ".join(out)


d = json.load(open(os.path.join(OUT, "pair_search.json")))
cands = [(tuple(a), tuple(b)) for a, b in d["all_candidates"]]
classes = {}
ext_iso, real = 0, []
for a, b in cands:
    ta, tb = TABLES[a], TABLES[b]
    if ext_canon(ta) == ext_canon(tb):
        ext_iso += 1
    else:
        real.append((a, b))
uniq = {}
for a, b in real:
    k = tuple(sorted([str(ps.canon(TABLES[a])[0]), str(ps.canon(TABLES[b])[0])]))
    uniq.setdefault(k, (a, b))
print("candidates (non-iso under 6 perms, distinct eligible B, margin ok): %d" % len(cands))
print("  of which isomorphic under perm x value-relabeling (48-group): %d" % ext_iso)
print("  remaining (not isomorphic under the 48-group): %d ; unique up to node relabeling: %d" % (len(real), len(uniq)))
ue = {}
for a, b in real:
    k = tuple(sorted([str(ext_canon(TABLES[a])), str(ext_canon(TABLES[b]))]))
    ue.setdefault(k, (a, b))
print("  unique up to the 48-group: %d" % len(ue))
fam = {}
for a, b in ue.values():
    fam[(a[0], b[0])] = fam.get((a[0], b[0]), 0) + 1
print("  family breakdown of 48-group-unique pairs:", fam)

# representatives: simplest by total number of 1s / prefer nsi-nsi
def complexity(fid):
    return sum(sum(t) for t in TABLES[fid])
reps = sorted(ue.values(), key=lambda ab: (not (ab[0][0] == "nsi" and ab[1][0] == "nsi"),
                                           complexity(ab[0]) + complexity(ab[1])))[:4]
report = {"n_candidates": len(cands), "ext_iso": ext_iso, "real": len(real), "unique_48": len(ue),
          "family_breakdown": {str(k): v for k, v in fam.items()}, "reps": []}
for a, b in reps:
    rec = {}
    for nm, fid in (("a", a), ("b", b)):
        tab = TABLES[fid]
        rules = ps.table_form(tab)
        ci, phi = core_indices(rules, L)
        bset, base, drops = bottleneck_set(rules, L)
        o0 = own_targets(rules, 0)
        o1 = own_targets(rules, 1)
        rec[nm] = {"id": list(fid), "rules": describe(tab), "q161_core": list(ci), "q161_phi": phi,
                   "q161_B": sorted(bset), "q161_base": base, "q161_drops": [float(x) for x in drops],
                   "own_clamp0": {"base": o0[0], "core": o0[1], "drops": o0[2], "B": o0[3]},
                   "own_clamp1": {"base": o1[0], "core": o1[1], "drops": o1[2], "B": o1[3]}}
    pa, pb = exact_cross(TABLES[a]), exact_cross(TABLES[b])
    rec["exact_cross_equal_lags_m20_20"] = pa == pb
    rec["cross_values"] = sorted({str(v) for v in pa.values()})[:6]
    report["reps"].append(rec)
    print("\n==== representative pair")
    for nm in ("a", "b"):
        r = rec[nm]
        print(" %s %s :: %s" % (nm, r["id"], r["rules"]))
        print("    q161: core=%s Φ=%.4f base=%.4f drops=%s B=%s" % (r["q161_core"], r["q161_phi"], r["q161_base"],
              [round(x, 4) for x in r["q161_drops"]], r["q161_B"]))
        print("    own clamp0: base=%.4f core=%s drops=%s B=%s" % (r["own_clamp0"]["base"], r["own_clamp0"]["core"],
              [round(x, 4) for x in r["own_clamp0"]["drops"]], r["own_clamp0"]["B"]))
        print("    own clamp1: base=%.4f core=%s drops=%s B=%s" % (r["own_clamp1"]["base"], r["own_clamp1"]["core"],
              [round(x, 4) for x in r["own_clamp1"]["drops"]], r["own_clamp1"]["B"]))
    print(" exact cross profiles equal (6 ordered pairs, lags 0..20 each way):", rec["exact_cross_equal_lags_m20_20"],
          "; distinct values:", rec["cross_values"])
json.dump(report, open(os.path.join(OUT, "verify_candidates.json"), "w"), indent=1, default=str)
