"""Invariant tests for q221 identifiability claims (fast; no PyPhi). Exact rational arithmetic throughout.
Run: python -m pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration/identifiability/test_invariants.py"""
from fractions import Fraction
from itertools import permutations

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import (
    TABLES, ext_canon, stats, tpm, stationary)
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.affine_theory import affine_of, prop1, det2
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.iso_check_hassan_pair import apply

P, Q = ("aff", 9, 6, 10), ("aff", 9, 15, 10)
HA, HB = ("aff", 6, 9, 5), ("aff", 11, 9, 5)
FAIL_A, FAIL_B = ("nsi", 0, 3, 3), ("aff", 6, 9, 5)


def bit(s, i):
    return (s >> i) & 1


def test_state_ordering_and_rules_of_lead_pair():
    # little-endian s = X + 2Y + 4H; P: X'=~H, Y'=X^Y, H'=X^H ; Q differs only in Y'=~(X^Y^H)
    for s in range(8):
        x, y, h = bit(s, 0), bit(s, 1), bit(s, 2)
        assert TABLES[P][0][s] == 1 - h and TABLES[Q][0][s] == 1 - h
        assert TABLES[P][1][s] == x ^ y and TABLES[Q][1][s] == 1 - (x ^ y ^ h)
        assert TABLES[P][2][s] == x ^ h and TABLES[Q][2][s] == x ^ h


def test_tpm_normalised_and_stationary_uniform():
    for fid in (P, Q):
        M = tpm(TABLES[fid])
        assert all(sum(row) == 1 for row in M)
        assert stationary(M) == [Fraction(1, 8)] * 8


def test_lead_pair_pairwise_equal_but_laws_differ():
    a, b = stats(P), stats(Q)
    assert a[0] is False and b[0] is False          # no constant node
    assert a[1] == b[1] == (Fraction(1, 2),) * 3     # marginals
    assert a[2] == b[2] and a[3] == b[3]             # auto and cross profiles, lags 0..20
    assert tpm(TABLES[P]) != tpm(TABLES[Q])


def test_lead_pair_not_isomorphic_hassan_pair_isomorphic():
    assert ext_canon(TABLES[P]) != ext_canon(TABLES[Q])
    hits = [(p, m) for p in permutations(range(3)) for m in range(8) if apply(TABLES[HA], p, m) == TABLES[HB]]
    assert hits == [((0, 2, 1), 6), ((0, 2, 1), 7)]
    assert not [p for p in permutations(range(3)) if apply(TABLES[HA], p, 0) == TABLES[HB]]


def test_prop1_closed_form_matches_exact_for_lead_pair():
    for fid in (P, Q):
        A, c = affine_of(TABLES[fid])
        assert det2(A) == 1
        cf = prop1(A, c)
        _, _, auto, cross = stats(fid)
        assert tuple(cf[(i, i, k)] for i in range(3) for k in range(21)) == auto
        assert tuple(cf[(i, j, k)] for i in range(3) for j in range(3) if i != j for k in range(21)) == cross


def test_prop2_three_point_statistic_separates_lead_pair():
    # P(Y_{t+1} = X_t xor Y_t) = 23/25 under P and 1/2 under Q
    vals = []
    for fid in (P, Q):
        M = tpm(TABLES[fid]); pi = stationary(M)
        vals.append(sum(pi[s] * M[s][z] for s in range(8) for z in range(8) if bit(z, 1) == bit(s, 0) ^ bit(s, 1)))
    assert vals == [Fraction(23, 25), Fraction(1, 2)]


def test_preserved_failing_example_marginal_separates():
    # first bounded-search candidate: equal cross profiles, but X marginal 2/25 vs 1/2 (constant X'=0)
    a, b = stats(FAIL_A), stats(FAIL_B)
    assert a[3] == b[3]
    assert a[0] is True and a[1][0] == Fraction(2, 25) and b[1][0] == Fraction(1, 2)
