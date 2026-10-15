"""For candidate pairs unique up to the 48-group {node permutation} x {per-node value relabeling}: do the two
members also share (i) single-channel marginal means and (ii) auto match profiles (lags 1..20)?
numpy linear algebra on the exact noisy chain, tolerance 1e-12. No PyPhi."""
import json
import os
import numpy as np
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps

OUT = os.path.join(os.path.dirname(__file__), "results")
TABLES = {}
for gen in (ps.nsi_forms, ps.affine_forms):
    for fid, tab in gen():
        TABLES[tuple(fid)] = tab


def complement(tables, mask):
    return tuple(tuple(tables[j][s ^ mask] ^ ((mask >> j) & 1) for s in range(8)) for j in range(3))


def ext_canon(t):
    return min(ps.permute_tables(complement(t, m), p) for m in range(8) for p in ps.PERMS)


def stats(t):
    P = ps.sbs(t)
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1))]); pi /= pi.sum()
    means = ps.IND @ pi
    autos, Pk = [], np.eye(8)
    for k in range(1, 21):
        Pk = Pk @ P
        autos.append([pi @ ((ps.IND[i][:, None] == ps.IND[i][None, :]) * Pk).sum(1) for i in range(3)])
    return means, np.array(autos)


d = json.load(open(os.path.join(OUT, "pair_search.json")))
ue = {}
for a, b in d["all_candidates"]:
    ta, tb = TABLES[tuple(a)], TABLES[tuple(b)]
    ca, cb = ext_canon(ta), ext_canon(tb)
    if ca == cb:
        continue
    ue.setdefault(tuple(sorted([str(ca), str(cb)])), (tuple(a), tuple(b)))
same_mean = same_auto = same_both = 0
rows = []
for a, b in ue.values():
    ma, aa = stats(TABLES[a]); mb, ab = stats(TABLES[b])
    sm = np.allclose(ma, mb, atol=1e-12, rtol=0)
    sa = np.allclose(aa, ab, atol=1e-12, rtol=0)
    same_mean += sm; same_auto += sa; same_both += sm and sa
    rows.append({"a": a, "b": b, "same_means": bool(sm), "same_auto": bool(sa),
                 "max_mean_diff": float(np.abs(ma - mb).max()), "max_auto_diff": float(np.abs(aa - ab).max())})
print("48-group-unique candidate pairs: %d" % len(ue))
print("  same single-channel means: %d ; same auto profiles (lags 1..20): %d ; both: %d" % (same_mean, same_auto, same_both))
print("  min over pairs of max |mean diff| = %.4f ; min over pairs of max |auto diff| = %.4f"
      % (min(r["max_mean_diff"] for r in rows), min(r["max_auto_diff"] for r in rows)))
json.dump(rows, open(os.path.join(OUT, "candidate_marginals.json"), "w"), indent=1)
