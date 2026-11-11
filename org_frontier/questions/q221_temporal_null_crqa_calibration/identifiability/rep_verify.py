"""Independent reproduction for the ONE representative surviving pair (adjudicate.py): rules written by hand as
explicit lambdas (not via pair_search tables), q161 functions + an own PyPhi loop with clamp-to-0 and clamp-to-1,
per-state system φ of every candidate subsystem, exact rational cross/auto profiles to lag 40, 48-group isomorphism."""
import itertools
from fractions import Fraction
import pyphi
from pyphi import new_big_phi
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import core_indices, bottleneck_set
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import ab_reproduce as ar
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import verify_candidates as vc

pyphi.config.PROGRESS_BARS = False
L = ("X", "Y", "H")
SYS = {
    "P": [lambda x: 1 - x[2], lambda x: x[0] ^ x[1], lambda x: x[0] ^ x[2]],
    "Q": [lambda x: 1 - x[2], lambda x: 1 - (x[0] ^ x[1] ^ x[2]), lambda x: x[0] ^ x[2]],
}
print("\n" + "#" * 60 + "\nREPRESENTATIVE: P: X'=~H, Y'=X^Y, H'=X^H ;  Q: X'=~H, Y'=~(X^Y^H), H'=X^H")
F = Fraction(2, 25)


def sbs(rules):
    P = []
    for s in range(8):
        b = tuple((s >> i) & 1 for i in range(3))
        nxt = [r(b) for r in rules]
        row = []
        for s2 in range(8):
            b2 = tuple((s2 >> i) & 1 for i in range(3))
            p = Fraction(1)
            for j in range(3):
                p *= (1 - F) if b2[j] == nxt[j] else F
            row.append(p)
        P.append(row)
    return P


prof = {}
for nm, rules in SYS.items():
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    ci, phi = core_indices(rules, L)
    B, base, drops = bottleneck_set(rules, L)
    print("== %s CM=%s ; q161 core=%s Φ=%.6f ; drops=%s ; B=%s" % (nm, cm.tolist(), ci, phi, [round(d, 6) for d in drops], sorted(B)))
    for c in (0, 1):
        o = vc.own_targets(rules, c)
        print("   own clamp-to-%d: base=%.6f core=%s drops=%s B=%s" % (c, o[0], o[1], [round(d, 6) for d in o[2]], o[3]))
    net = pyphi.Network(tpm, cm=cm, node_labels=L)
    for s in reachable_states(tpm, 3):
        st = tuple((s >> i) & 1 for i in range(3))
        ph = []
        for r in (1, 2, 3):
            for nodes in itertools.combinations(range(3), r):
                try:
                    v = "%.3f" % float(new_big_phi.sia(pyphi.Subsystem(net, st, nodes)).phi)
                except Exception as e:
                    v = "unreachable(%s)" % type(e).__name__
                ph.append("%s:%s" % ("".join(L[i] for i in nodes), v))
        print("   state %s: %s" % (st, " ".join(ph)))
    P = sbs(rules)
    pi = ar.stationary_exact(P)
    print("   stationary π = %s" % [str(p) for p in pi])
    prof[nm] = ar.profiles_exact(P, pi, K=40)
cross = [k for k in prof["P"] if k[0] != k[1]]
auto = [k for k in prof["P"] if k[0] == k[1]]
print("exact cross equal (6 ordered pairs x lags 0..40): %s ; exact auto equal (3 x 0..40): %s"
      % (all(prof["P"][k] == prof["Q"][k] for k in cross), all(prof["P"][k] == prof["Q"][k] for k in auto)))
tP = tuple(tuple(r(tuple((s >> i) & 1 for i in range(3))) for s in range(8)) for r in SYS["P"])
tQ = tuple(tuple(r(tuple((s >> i) & 1 for i in range(3))) for s in range(8)) for r in SYS["Q"])
print("isomorphic under 48-group (node perm x value relabel):", vc.ext_canon(tP) == vc.ext_canon(tQ))
