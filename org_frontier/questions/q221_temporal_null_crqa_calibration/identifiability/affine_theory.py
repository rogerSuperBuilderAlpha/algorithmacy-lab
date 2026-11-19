"""Exact check of the affine-class proposition (THEORY.md) on every GF(2)-affine 3-node form in the enumerated class.

Class: x(t+1) = A x(t) + c + n(t) over GF(2), n(t) i.i.d. Bernoulli(p) per node, p = 2/25, with A invertible
(so the uniform law is stationary). Proposition 1 (closed form): with w_m = (A^T)^m e_j,
   E[(-1)^{x_i(t) + x_j(t+k)}] = 1[w_k = e_i] * (-1)^{sum_{m<k} w_m . c} * prod_{m<k} (1-2p)^{|w_m|}
and P(x_i(t) = x_j(t+k)) = (1 + E[...]) / 2.  Proposition 2: the one-step parity statistics
   E[(-1)^{v . x(t) + x_j(t+1)}] = 1[v = A^T e_j] * (-1)^{c_j} * (1-2p)    (all v in GF(2)^3)
identify (A, c) exactly.  Checks: (1) Prop 1 equals the exact rational profiles for every invertible form at lags
0..20, all (i, j) incl. i = j; (2) the partition of invertible forms by Prop-1 signature equals the partition by
exact profiles + marginals; (3) Prop 2 equals exact enumeration for every invertible form."""
from fractions import Fraction
from itertools import product

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES, stats, tpm, stationary

p = Fraction(2, 25)
r = 1 - 2 * p
K = 20


def affine_of(t):
    c = [t[j][0] for j in range(3)]
    A = [[t[j][1 << i] ^ c[j] for i in range(3)] for j in range(3)]
    for s in range(8):
        for j in range(3):
            if t[j][s] != (sum(A[j][i] * ((s >> i) & 1) for i in range(3)) + c[j]) % 2:
                return None
    return A, c


def det2(A):
    a = A
    d = (a[0][0] * (a[1][1] * a[2][2] + a[1][2] * a[2][1]) + a[0][1] * (a[1][0] * a[2][2] + a[1][2] * a[2][0])
         + a[0][2] * (a[1][0] * a[2][1] + a[1][1] * a[2][0]))
    return d % 2


def AT_apply(A, w):  # (A^T w)_i = sum_j A[j][i] w_j
    return tuple(sum(A[j][i] * w[j] for j in range(3)) % 2 for i in range(3))


def prop1(A, c):
    out = {}
    for j in range(3):
        w = tuple(1 if i == j else 0 for i in range(3))
        sign, dec = 0, Fraction(1)
        for k in range(K + 1):
            for i in range(3):
                e = tuple(1 if q == i else 0 for q in range(3))
                corr = (-1) ** sign * dec if w == e else 0
                out[(i, j, k)] = (1 + Fraction(corr)) / 2
            sign = (sign + sum(a * b for a, b in zip(w, c))) % 2
            dec *= r ** sum(w)
            w = AT_apply(A, w)
    return out


def main():
    aff = [fid for fid in TABLES if fid[0] == "aff"]
    inv, sing, nonaff = [], [], 0
    for fid in aff:
        ac = affine_of(TABLES[fid])
        if ac is None:
            nonaff += 1
        elif det2(ac[0]):
            inv.append((fid, ac))
        else:
            sing.append(fid)
    print("affine forms %d: invertible A %d, singular A %d, not affine %d" % (len(aff), len(inv), len(sing), nonaff))
    ok1 = ok3 = 0
    sig_p, sig_e = {}, {}
    for fid, (A, c) in inv:
        P1 = prop1(A, c)
        const, marg, auto, cross = stats(fid)
        exact = {}
        auto_keys = [(i, i, k) for i in range(3) for k in range(K + 1)]
        cross_keys = [(i, j, k) for i in range(3) for j in range(3) if i != j for k in range(K + 1)]
        exact.update(zip(auto_keys, auto))
        exact.update(zip(cross_keys, cross))
        # stats() profiles are P(x_i(t) = x_j(t+k)) with the same (i, j, k) convention
        if all(P1[key] == exact[key] for key in exact) and all(m == Fraction(1, 2) for m in marg):
            ok1 += 1
        sig_p.setdefault(tuple(P1[k] for k in sorted(P1)), set()).add(fid)
        sig_e.setdefault((marg, auto, cross), set()).add(fid)
        # Prop 2 by exact enumeration under the (uniform) stationary law
        P = tpm(TABLES[fid]); pi = stationary(P)
        good = True
        for j in range(3):
            for v in product((0, 1), repeat=3):
                val = sum(pi[s] * P[s][z] * (-1) ** ((sum(v[i] * ((s >> i) & 1) for i in range(3)) + ((z >> j) & 1)) % 2)
                          for s in range(8) for z in range(8))
                col = tuple(A[j][i] for i in range(3))
                pred = (-1) ** c[j] * r if tuple(v) == col else 0
                good &= val == pred
        ok3 += good
    part_p = sorted(sorted(map(str, g)) for g in sig_p.values())
    part_e = sorted(sorted(map(str, g)) for g in sig_e.values())
    print("Prop 1 closed form == exact profiles (lags 0..%d, all i,j) and marginals 1/2: %d/%d" % (K, ok1, len(inv)))
    print("partition by Prop-1 signature == partition by exact (marginals, auto, cross): %s ; classes %d ; multi-member classes %d"
          % (part_p == part_e, len(part_p), sum(len(g) > 1 for g in part_p)))
    print("Prop 2 one-step parity statistics == exact (all 8 v x 3 j): %d/%d" % (ok3, len(inv)))
    for nm, fid in (("P", ("aff", 9, 6, 10)), ("Q", ("aff", 9, 15, 10))):
        A, c = affine_of(TABLES[fid])
        print("%s: A rows (X,Y,H coefficients) = %s ; c = %s ; det = %d" % (nm, A, c, det2(A)))
        for j in range(3):
            w = tuple(1 if i == j else 0 for i in range(3)); path = []
            for m in range(5):
                path.append("".join(map(str, w))); w = AT_apply(A, w)
            print("   unit-vector path (A^T)^m e_%s, m=0..4: %s" % ("XYH"[j], " ".join(path)))


if __name__ == "__main__":
    main()
