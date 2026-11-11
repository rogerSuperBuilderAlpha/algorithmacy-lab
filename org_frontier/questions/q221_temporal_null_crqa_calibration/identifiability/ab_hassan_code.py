"""Hassan's A/B pair exactly as coded in independent_audit/finite_sample.py (commit 211bacf6):
    A: X'=X, Y'=Y, H'=H            B: X'=X, Y'=Y, H'=H XOR X XOR Y        (8% flip on every node)
Both are in q220's deterministic-rule-plus-flip family. Exact checks (rational, flip = 2/25) of his Phase-10 claims,
and the lab's exact-Φ targets on the DETERMINISTIC TPM (rule 8) with q161 functions (read-only)."""
import itertools
import math
from fractions import Fraction

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import (
    core_indices, bottleneck_set, mc_phi)
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import exact_profiles as ep
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import ab_reproduce as ar  # noqa (prints its own block)

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
L = ("X", "Y", "H")
F = Fraction(2, 25)
RULES = {"A": [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
         "B": [lambda x: x[0], lambda x: x[1], lambda x: x[2] ^ x[0] ^ x[1]]}
print("\n" + "#" * 70 + "\nHassan's coded pair (finite_sample.py): B has H' = H xor X xor Y")


def sbs_exact(rules):
    P = [[Fraction(0)] * 8 for _ in range(8)]
    for s in range(8):
        nxt = [r(ep.bits(s, 3)) for r in rules]
        for s2 in range(8):
            b = ep.bits(s2, 3)
            p = Fraction(1)
            for j in range(3):
                p *= (1 - F) if b[j] == nxt[j] else F
            P[s][s2] = p
    return P


PA, PB = sbs_exact(RULES["A"]), sbs_exact(RULES["B"])
print("max |TPM_A - TPM_B| = %.6f" % float(max(abs(PA[r][c] - PB[r][c]) for r in range(8) for c in range(8))))
for nm, P in (("A", PA), ("B", PB)):
    pi = ar.stationary_exact(P)
    print("%s stationary uniform: %s ; CMI I(H';X,Y|H) = %.8f bits" % (nm, all(p == Fraction(1, 8) for p in pi), ar.cmi(P, pi)))
prA, prB = ar.profiles_exact(PA, ar.stationary_exact(PA)), ar.profiles_exact(PB, ar.stationary_exact(PB))
cross = [k for k in prA if k[0] != k[1]]
print("cross pair x lag values (126): %d exactly equal; all 1/2: %s"
      % (sum(prA[k] == prB[k] for k in cross), all(prA[k] == Fraction(1, 2) == prB[k] for k in cross)))
for i in range(3):
    print("auto %s: max |A-B| lags 0..20 = %.6f" % (L[i], float(max(abs(prA[(i, i, k)] - prB[(i, i, k)]) for k in range(21)))))
tab = {k: tuple(tuple(r(ep.bits(s, 3)) for s in range(8)) for r in v) for k, v in RULES.items()}
print("isomorphic under 6 node permutations:", any(ps.permute_tables(tab["A"], p) == tab["B"] for p in ps.PERMS))
for nm, rules in RULES.items():
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    v = verdict(rules, L)
    ci, phi = core_indices(rules, L)
    bset, base, drops = bottleneck_set(rules, L)
    print("== %s deterministic TPM %s ; CM %s" % (nm, tpm.astype(int).tolist(), cm.tolist()))
    print("   verdict max_phi=%s ; q161 core=%s Φ=%.4f mc_phi=%.4f ; drops=%s ; B=%s"
          % (v.max_phi, ci, phi, mc_phi(rules, L), [round(d, 6) for d in drops], sorted(bset)))
    net = pyphi.Network(tpm, cm=cm, node_labels=L)
    for s in reachable_states(tpm, 3):
        st = ep.bits(s, 3)
        phis = []
        for r in (1, 2, 3):
            for nodes in itertools.combinations(range(3), r):
                phis.append("%s:%.3f" % ("".join(L[i] for i in nodes),
                                          float(new_big_phi.sia(pyphi.Subsystem(net, st, nodes)).phi)))
        print("   state %s : %s" % (st, " ".join(phis)))
    print("   eligible (core>=2, B nonempty, |B|<n):", bool(ci) and len(ci) >= 2 and 0 < len(bset) < 3)
