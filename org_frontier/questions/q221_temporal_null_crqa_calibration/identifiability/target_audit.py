"""Step-11 audit of the q161 bottleneck target on the lead pair P/Q (pinned PyPhi, deterministic TPM).
(a) node-permutation equivariance: B(perm(P)) == perm(B(P)) for all 6 permutations;
(b) value-relabelling invariance (a harmless equivalence: rename 0/1 of some nodes): B(flip_m(P)) == B(P)?;
(c) mechanism: the residual network after freezing each node (rule := constant 0) -> its major complex and Phi;
(d) the same with freeze-to-1, to separate a convention effect from a structural one."""
from itertools import permutations

from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import bottleneck_set, major_complex, TOL
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.iso_check_hassan_pair import apply

L = ("X", "Y", "H")
PAIR = {"P": ("aff", 9, 6, 10), "Q": ("aff", 9, 15, 10)}


def B_of(t):
    B, base, drops = bottleneck_set(ps.table_form(t), L)
    return set(int(b) for b in B), base, [round(float(d), 6) for d in drops]


print("q161 TOL =", TOL)
for nm, fid in PAIR.items():
    t = TABLES[fid]
    B0, base, drops = B_of(t)
    print("== %s: B=%s base=%.3f drops=%s" % (nm, sorted(B0), base, drops))
    eq = []
    for p in permutations(range(3)):
        Bp, _, _ = B_of(apply(t, p, 0))
        eq.append(Bp == {p[b] for b in B0})
    print("   (a) node-permutation equivariant under all 6: %s" % all(eq))
    for m in range(1, 8):
        Bm, bm, dm = B_of(apply(t, (0, 1, 2), m))
        print("   (b) value flip mask %s (flip %s): B=%s base=%.3f drops=%s ; same as unflipped: %s"
              % (format(m, "03b")[::-1], "".join(L[j] for j in range(3) if (m >> j) & 1), sorted(Bm), bm, dm, Bm == B0))
    for c in (0, 1):
        for k in range(3):
            rules = list(ps.table_form(t))
            rules[k] = (lambda x, c=c: c)
            core, phi = major_complex(rules, L)
            print("   (c/d) freeze %s := %d -> residual major complex %s, Phi %s" % (L[k], c, core, phi))
