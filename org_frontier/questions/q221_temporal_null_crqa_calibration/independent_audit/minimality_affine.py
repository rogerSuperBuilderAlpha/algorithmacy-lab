"""Exact minimal-node certificate for non-isomorphic pairwise-recurrence ambiguity.

Only invertible noisy GF(2)-affine Boolean systems, with stationary categorical
marginal and auto/cross match profiles. No PyPhi or preregistered IIT claim.
"""
import itertools
import json
from fractions import Fraction
from functools import reduce

FLIP = Fraction(2, 25)


def invertible(rows, n):
    images = {tuple((row & s).bit_count() & 1 for row in rows)
              for s in range(1 << n)}
    return len(images) == 1 << n


def signature(rows, c, n, lags):
    """Walsh character signature. Equal profiles iff equal signatures for 0<p<1/2."""
    result = []
    for j in range(n):
        w, parity, weight_sum = 1 << j, 0, 0
        for _ in range(lags):
            result.append((w.bit_length() - 1, weight_sum, parity)
                          if w.bit_count() == 1 else (-1, 0, 0))
            parity ^= (w & c).bit_count() & 1
            weight_sum += w.bit_count()
            nxt = 0
            for rowidx, row in enumerate(rows):
                if (w >> rowidx) & 1:
                    nxt ^= row
            w = nxt
    return tuple(result)


def truth(rows, c, n):
    return tuple(tuple(((row & s).bit_count() & 1) ^ ((c >> j) & 1)
                       for s in range(1 << n)) for j, row in enumerate(rows))


def relabel(table, n, perm, mask):
    result = [[0] * (1 << n) for _ in range(n)]
    for state in range(1 << n):
        old = sum(((((state >> perm[j]) & 1) ^ ((mask >> j) & 1)) << j)
                  for j in range(n))
        for j in range(n):
            result[perm[j]][state] = table[j][old] ^ ((mask >> j) & 1)
    return tuple(tuple(row) for row in result)


def isomorphic(a, b, n):
    table_a, table_b = truth(*a, n), truth(*b, n)
    return any(relabel(table_a, n, perm, mask) == table_b
               for perm in itertools.permutations(range(n))
               for mask in range(1 << n))


def exact_profile(rows, c, n, lags):
    """Independent exact stationary Markov-kernel calculation."""
    states = range(1 << n)
    P = []
    for s in states:
        goal = tuple(((rows[j] & s).bit_count() & 1) ^ ((c >> j) & 1)
                     for j in range(n))
        P.append(tuple(reduce(lambda x, y: x * y,
                    ((1 - FLIP) if ((z >> j) & 1) == goal[j] else FLIP
                     for j in range(n)), Fraction(1)) for z in states))
    assert all(sum(P[s]) == 1 for s in states)
    assert all(sum(P[s][z] for s in states) == 1 for z in states)
    K = tuple(tuple(Fraction(int(s == z)) for z in states) for s in states)
    result = []
    for _ in range(lags):
        for i in range(n):
            for j in range(n):
                result.append(sum((K[s][z] for s in states for z in states
                                   if ((s >> i) & 1) == ((z >> j) & 1)),
                                  Fraction(0)) / (1 << n))
        K = tuple(tuple(sum((K[s][t] * P[t][z] for t in states), Fraction(0))
                        for z in states) for s in states)
    return tuple(result)


def all_small_systems(n):
    return [(rows, c) for rows in itertools.product(range(1 << n), repeat=n)
            if invertible(rows, n) for c in range(1 << n)]


def certificate():
    summary = {}
    for n in (1, 2):
        models = all_small_systems(n)
        lags = 2 * (1 << n)
        sigs = {m: signature(*m, n, lags) for m in models}
        exacts = {m: exact_profile(*m, n, lags) for m in models}
        sigpairs, expairs = [], []
        for a, b in itertools.combinations(models, 2):
            if sigs[a] == sigs[b]:
                sigpairs.append((a, b))
            if exacts[a] == exacts[b]:
                expairs.append((a, b))
        assert sigpairs == expairs, "Walsh signature vs exact TPM mismatch"
        assert all(isomorphic(a, b, n) for a, b in expairs)
        summary[str(n)] = {
            "systems": len(models),
            "profile_classes": len(set(exacts.values())),
            "equal_profile_pairs": len(expairs),
            "nonisomorphic_equal_profile_pairs": 0,
            "all_collisions_explained_by_relabeling": True,
        }
    assert summary["1"]["systems"] == 2 and summary["1"]["equal_profile_pairs"] == 0
    assert summary["2"]["systems"] == 24 and summary["2"]["profile_classes"] == 16
    assert summary["2"]["equal_profile_pairs"] == 8
    a, b = (9, 6, 10), (9, 15, 10)
    a_model = (tuple(code >> 1 for code in a),
               sum((code & 1) << j for j, code in enumerate(a)))
    b_model = (tuple(code >> 1 for code in b),
               sum((code & 1) << j for j, code in enumerate(b)))
    assert signature(*a_model, 3, 16) == signature(*b_model, 3, 16)
    assert not isomorphic(a_model, b_model, 3)
    return {
        "status": "exact enumerative minimality in invertible GF2-affine family",
        "flip": "2/25",
        "dimensions": summary,
        "first_nonisomorphic_ambiguity_n": 3,
        "witness_affine_codes": {"A": list(a), "B": list(b)},
        "theorem_scope": "all integer-lag stationary categorical match summaries; modulo node permutations and per-node value flips; 0<p<1/2",
        "limitation": "No minimum claim for general Boolean, hidden-state or IIT-target models.",
    }


def main():
    print(json.dumps(certificate(), indent=2))


if __name__ == "__main__":
    main()
