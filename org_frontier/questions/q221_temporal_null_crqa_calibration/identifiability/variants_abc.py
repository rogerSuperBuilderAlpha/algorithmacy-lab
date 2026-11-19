"""Variant reconciliation (Hassan's A/B/C naming): exact rational stationary law, H lag-1 self-match, CMI
I(H';X,Y|H) under the TRUE stationary law, and exact cross/auto profile equality vs A at lags 0..20.
A = A_self (H'=H), B = B_xor (H'=X^Y, in-family, NON-uniform stationary), C = B_xor_memory (H'=H^X^Y).
All: X'=X, Y'=Y, independent 0.08 flip on every node (q220 deterministic-rule-plus-flip family)."""
from fractions import Fraction
import math
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import ab_reproduce as ar

F = Fraction(2, 25)


def sbs(rules):
    P = []
    for s in range(8):
        b = tuple((s >> i) & 1 for i in range(3))
        nxt = [r(b) for r in rules]
        row = []
        for s2 in range(8):
            p = Fraction(1)
            for j in range(3):
                p *= (1 - F) if ((s2 >> j) & 1) == nxt[j] else F
            row.append(p)
        P.append(row)
    return P

V = {"A (A_self, H'=H)": [lambda s: s[0], lambda s: s[1], lambda s: s[2]],
     "B (B_xor, H'=X^Y)": [lambda s: s[0], lambda s: s[1], lambda s: s[0] ^ s[1]],
     "C (B_xor_memory, H'=H^X^Y)": [lambda s: s[0], lambda s: s[1], lambda s: s[0] ^ s[1] ^ s[2]]}


def cmi(P, pi):
    # I(H';X,Y|H) = sum p(x,y,h,h') log p(h'|x,y,h)/p(h'|h)
    j = {}
    for s in range(8):
        x, y, h = s & 1, (s >> 1) & 1, (s >> 2) & 1
        for s2 in range(8):
            h2 = (s2 >> 2) & 1
            j[(x, y, h, h2)] = j.get((x, y, h, h2), 0) + pi[s] * P[s][s2]
    tot = 0.0
    for (x, y, h, h2), p in j.items():
        if p == 0:
            continue
        pxyh = sum(j[(x, y, h, k)] for k in (0, 1))
        ph = sum(j[(a, b, h, k)] for a in (0, 1) for b in (0, 1) for k in (0, 1))
        phh2 = sum(j[(a, b, h, h2)] for a in (0, 1) for b in (0, 1))
        tot += float(p) * math.log2(float(p / pxyh) / float(phh2 / ph))
    return tot


res = {}
for nm, rules in V.items():
    P = sbs(rules)
    pi = ar.stationary_exact(P)
    prof = ar.profiles_exact(P, pi, K=20)
    res[nm] = prof
    selfH = prof[(2, 2, 1)]
    print("== %s\n   stationary π (little-endian X,Y,H) = %s ; uniform: %s" % (nm, [str(p) for p in pi], all(p == Fraction(1, 8) for p in pi)))
    print("   H lag-1 self-match = %s = %.8f ; CMI I(H';X,Y|H) = %.8f bits" % (selfH, float(selfH), cmi(P, pi)))
names = list(V)
for other in names[1:]:
    cross = [k for k in res[names[0]] if k[0] != k[1]]
    auto = [k for k in res[names[0]] if k[0] == k[1]]
    nc = sum(res[names[0]][k] == res[other][k] for k in cross)
    print("A vs %s: cross pair×lag values equal %d/%d ; auto equal %d/%d ; max |Δcross| = %.6g"
          % (other, nc, len(cross), sum(res[names[0]][k] == res[other][k] for k in auto), len(auto),
             max(abs(float(res[names[0]][k] - res[other][k])) for k in cross)))
