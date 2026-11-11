"""Shared definitions for the 4-node study (PREREGISTRATION.md): the family F4, the relabeling group, the
Proposition-1 signature, and exact brute-force profiles in integer/rational arithmetic.

Encoding: A is a 16-bit int whose row j (bits 4j..4j+3) holds the coefficients of x_0..x_3 in x_j'. c is a 4-bit
int. A system code is A16 * 16 + c. State s = sum_i x_i 2^i (little-endian, as in the 3-node study)."""
from fractions import Fraction
from itertools import permutations

import numpy as np

N = 4
NS = 1 << N
P_NUM, P_DEN = 2, 25                      # flip p = 2/25
K_SIG = 40                                # signature lags (PREREGISTRATION S1)
PERMS = list(permutations(range(N)))      # 24


def rows(A16):
    return [(A16 >> (4 * j)) & 15 for j in range(N)]


def pc(x):
    return bin(x).count("1")


def apply_map(A16, c, s):
    """deterministic update x -> A x + c"""
    out = 0
    for j, r in enumerate(rows(A16)):
        out |= ((pc(r & s) & 1) ^ ((c >> j) & 1)) << j
    return out


def rank2(rs):
    rs = list(rs); rk = 0
    for bit in range(N):
        piv = next((i for i in range(rk, len(rs)) if (rs[i] >> bit) & 1), None)
        if piv is None:
            continue
        rs[rk], rs[piv] = rs[piv], rs[rk]
        for i in range(len(rs)):
            if i != rk and (rs[i] >> bit) & 1:
                rs[i] ^= rs[rk]
        rk += 1
    return rk


def invertible_As():
    return [a for a in range(1 << 16) if rank2(rows(a)) == N]


def AT(A16, w):
    """(A^T w): XOR of rows j with w_j = 1"""
    out = 0
    for j, r in enumerate(rows(A16)):
        if (w >> j) & 1:
            out ^= r
    return out


def a_part(A16):
    """c-independent part of the signature, plus the cumulative XOR vectors u_k used for the parities."""
    struct, us = [], []
    for j in range(N):
        w, S, u = 1 << j, 0, 0
        for k in range(K_SIG + 1):
            if w & (w - 1) == 0:
                struct.append((j, k, w.bit_length() - 1, S))
                us.append(u)
            S += pc(w); u ^= w; w = AT(A16, w)
    return tuple(struct), us


def signature(A16, c, cache={}):
    if A16 not in cache:
        cache[A16] = a_part(A16)
    st, us = cache[A16]
    return st, tuple(pc(u & c) & 1 for u in us)


# ---- relabeling group G = S4 x (Z2)^4 ----
def transform(A16, c, perm, m):
    """y = x xor m, then relabel node j -> perm[j]. Returns (A', c')."""
    am = 0
    for j, r in enumerate(rows(A16)):
        am |= (pc(r & m) & 1) << j
    c1 = c ^ am ^ m
    rs = rows(A16)
    nr = [0] * N
    for j in range(N):
        for i in range(N):
            if (rs[j] >> i) & 1:
                nr[perm[j]] |= 1 << perm[i]
    c2 = 0
    for j in range(N):
        if (c1 >> j) & 1:
            c2 |= 1 << perm[j]
    return sum(nr[j] << (4 * j) for j in range(N)), c2


def orbit_ids(As):
    """Vectorised canonical code (min over the 384 maps) for every (A, c) with A in As."""
    As = np.asarray(As, dtype=np.int64)
    A = np.repeat(As, 16); C = np.tile(np.arange(16, dtype=np.int64), len(As))
    # tables
    allA = np.arange(1 << 16, dtype=np.int64)
    Am = np.zeros((1 << 16, 16), dtype=np.int64)
    for m in range(16):
        v = np.zeros(1 << 16, dtype=np.int64)
        for j in range(N):
            r = (allA >> (4 * j)) & 15
            par = np.zeros_like(r)
            x = r & m
            for b in range(N):
                par ^= (x >> b) & 1
            v |= par << j
        Am[:, m] = v
    best = np.full(len(A), np.iinfo(np.int64).max, dtype=np.int64)
    for perm in PERMS:
        pa = np.zeros(1 << 16, dtype=np.int64)
        for j in range(N):
            for i in range(N):
                pa |= ((allA >> (4 * j + i)) & 1) << (4 * perm[j] + perm[i])
        pcv = np.zeros(16, dtype=np.int64)
        for cc in range(16):
            for j in range(N):
                if (cc >> j) & 1:
                    pcv[cc] |= 1 << perm[j]
        Ap = pa[A]
        for m in range(16):
            c1 = C ^ Am[A, m] ^ m
            code = Ap * 16 + pcv[c1]
            np.minimum(best, code, out=best)
    return A * 16 + C, best


# ---- exact profiles ----
def tpm_int(A16, c):
    """integer numerators N with P = N / 25^4"""
    q, p = P_DEN - P_NUM, P_NUM
    M = np.zeros((NS, NS), dtype=object)
    for s in range(NS):
        f = apply_map(A16, c, s)
        for z in range(NS):
            d = pc(f ^ z)
            M[s, z] = (p ** d) * (q ** (N - d))
    return M


def exact_profiles(A16, c, K=20):
    """Brute force: P(x_i(t) = x_j(t+k)) for all i, j, k = 0..K under the exact stationary law (checked uniform),
    as Fractions; plus marginals. Independent of Proposition 1."""
    M = tpm_int(A16, c)
    den = P_DEN ** N
    # stationary check: uniform is invariant iff column sums equal den
    assert all(sum(M[s, z] for s in range(NS)) == den for z in range(NS))
    marg = [Fraction(sum(1 for s in range(NS) if (s >> i) & 1), NS) for i in range(N)]
    vecs = {}
    for i in range(N):
        for b in (0, 1):
            vecs[(i, b)] = np.array([1 if ((s >> i) & 1) == b else 0 for s in range(NS)], dtype=object)
    prof = {}
    cur = dict(vecs); scale = 1
    for k in range(K + 1):
        for i in range(N):
            for j in range(N):
                tot = sum(cur[(i, b)][z] for b in (0, 1) for z in range(NS) if ((z >> j) & 1) == b)
                prof[(i, j, k)] = Fraction(tot, NS * scale)
        cur = {key: v.dot(M) for key, v in cur.items()}
        scale *= den
    return marg, prof


def prop1_profiles(A16, c, K=20):
    r = 1 - Fraction(2 * P_NUM, P_DEN)
    out = {}
    for j in range(N):
        w, sign, dec = 1 << j, 0, Fraction(1)
        for k in range(K + 1):
            for i in range(N):
                corr = (-1) ** sign * dec if w == (1 << i) else 0
                out[(i, j, k)] = (1 + Fraction(corr)) / 2
            sign ^= pc(w & c) & 1
            dec *= r ** pc(w)
            w = AT(A16, w)
    return out


def isomorphic(a, b):
    """direct enumeration of all 384 maps"""
    return any(transform(a[0], a[1], perm, m) == tuple(b) for perm in PERMS for m in range(16))


def rules_of(A16, c):
    rs = rows(A16)
    return [(lambda x, r=r, cj=(c >> j) & 1: (sum(x[i] for i in range(N) if (r >> i) & 1) + cj) & 1)
            for j, r in enumerate(rs)]
