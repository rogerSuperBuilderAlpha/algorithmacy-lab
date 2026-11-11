"""Post-rules reproduction for the A/B pair (EXACT_PHI_DECISION_RULES.md): Hassan's Phase-10 analytic claims,
for BOTH readings of his systems, plus the lab's exact-Φ targets (deterministic TPM, q161 functions).
  in-family  (q220 family: deterministic rule + 8% flip on every node)
      A: X'=X, Y'=Y, H'=H          B: X'=X, Y'=Y, H'=X xor Y
  fair-coin  (X, Y i.i.d. fair coins each step; only H has rule + 8% flip; NOT expressible in the family)
      A: H'=H                      B: H'=X xor Y
"""
import itertools
import math
from fractions import Fraction

import numpy as np

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import exact_profiles as ep
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps

F = Fraction(2, 25)
L = ("X", "Y", "H")


def sbs_exact(kind, system):
    """Exact (Fraction) state-by-state noisy TPM, rows/cols little-endian states (X bit0, Y bit1, H bit2)."""
    P = [[Fraction(0)] * 8 for _ in range(8)]
    for s in range(8):
        x, y, h = ep.bits(s, 3)
        hn = h if system == "A" else (x ^ y)
        for s2 in range(8):
            x2, y2, h2 = ep.bits(s2, 3)
            ph = (1 - F) if h2 == hn else F
            if kind == "in-family":
                px = (1 - F) if x2 == x else F
                py = (1 - F) if y2 == y else F
            else:
                px = py = Fraction(1, 2)
            P[s][s2] = px * py * ph
    return P


def stationary_exact(P):
    A = [[P[r][c] - (1 if r == c else 0) for r in range(8)] for c in range(8)]
    A[-1] = [Fraction(1)] * 8
    M = [row[:] + [Fraction(0) if i < 7 else Fraction(1)] for i, row in enumerate(A)]
    for c in range(8):
        piv = next(r for r in range(c, 8) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for r in range(8):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[i][8] / M[i][i] for i in range(8)]


def profiles_exact(P, pi, K=20):
    out = {}
    J = [[pi[s] if s == t else Fraction(0) for t in range(8)] for s in range(8)]
    for k in range(K + 1):
        for i in range(3):
            for j in range(3):
                out[(i, j, k)] = sum(J[s][t] for s in range(8) for t in range(8) if ((s >> i) & 1) == ((t >> j) & 1))
        J = [[sum(J[s][u] * P[u][t] for u in range(8)) for t in range(8)] for s in range(8)]
    return out


def cmi(P, pi):
    j = {}
    for s in range(8):
        x, y, h = ep.bits(s, 3)
        for s2 in range(8):
            k = (x, y, h, ep.bits(s2, 3)[2])
            j[k] = j.get(k, 0) + float(pi[s] * P[s][s2])
    m = lambda idx: {kk: sum(v for k, v in j.items() if tuple(k[i] for i in idx) == kk)
                     for kk in {tuple(k[i] for i in idx) for k in j}}
    ph, pxyh, phh = m([2]), m([0, 1, 2]), m([2, 3])
    return sum(v * math.log2(v * ph[(k[2],)] / (pxyh[k[:3]] * phh[(k[2], k[3])])) for k, v in j.items() if v > 0)


h2 = lambda p: -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
print("reference 1 - h2(0.08) = %.8f" % (1 - h2(0.08)))
for kind in ("in-family", "fair-coin"):
    print("=" * 30, kind)
    PA, PB = sbs_exact(kind, "A"), sbs_exact(kind, "B")
    print("max |TPM_A - TPM_B| entry = %.6f" % float(max(abs(PA[r][c] - PB[r][c]) for r in range(8) for c in range(8))))
    for nm, P in (("A", PA), ("B", PB)):
        pi = stationary_exact(P)
        print("  %s stationary uniform: %s   pi = %s" % (nm, all(p == Fraction(1, 8) for p in pi), [str(p) for p in pi]))
        print("  %s CMI I(H';X,Y|H) = %.8f bits" % (nm, cmi(P, pi)))
    prA, prB = profiles_exact(PA, stationary_exact(PA)), profiles_exact(PB, stationary_exact(PB))
    cross = [(i, j, k) for (i, j, k) in prA if i != j]
    eq = sum(prA[c] == prB[c] for c in cross)
    allhalf = all(prA[c] == Fraction(1, 2) and prB[c] == Fraction(1, 2) for c in cross)
    print("  cross pair x lag values compared (6 ordered pairs x lags 0..20 = 126): %d equal exactly; all = 1/2: %s"
          % (eq, allhalf))
    for i in range(3):
        d = max(abs(prA[(i, i, k)] - prB[(i, i, k)]) for k in range(21))
        print("  auto %s max |A-B| over lags 0..20 = %.6f" % (L[i], float(d)))
# isomorphism of the in-family deterministic systems (and of the noisy TPMs, same flip on all nodes)
tA = tuple(tuple(r(ep.bits(s, 3)) for s in range(8)) for r in [lambda x: x[0], lambda x: x[1], lambda x: x[2]])
tB = tuple(tuple(r(ep.bits(s, 3)) for s in range(8)) for r in [lambda x: x[0], lambda x: x[1], lambda x: x[0] ^ x[1]])
iso = [p for p in itertools.permutations(range(3)) if ps.permute_tables(tA, p) == tB]
print("isomorphic under some of the 6 node permutations:", bool(iso), iso)
