"""Fast standalone exact-rational regression tests, no PyPhi dependency."""
from fractions import Fraction
from itertools import permutations

from .exact_all_lags_certificate import (
    LEAD_A, LEAD_B, NOISE, recurrence, tables, transform, transition, reconstruct_rules_from_one_step_marginals, population_q220_peak_prominences
)

def test_stochastic_and_stationary_exactly():
    for code in (LEAD_A, LEAD_B):
        p = transition(code)
        assert all(sum(row) == 1 for row in p)
        assert all(sum(p[i][j] for i in range(8)) == 1 for j in range(8))

def test_exact_144_profile_values():
    a, b = recurrence(transition(LEAD_A)), recurrence(transition(LEAD_B))
    assert len(a) == 144 and a == b
    assert a[(2, 0, 1)] == NOISE
    assert a[(0, 1, 0)] == Fraction(1, 2)

def test_no_relabeling_in_48_group():
    assert transition(LEAD_A) != transition(LEAD_B)
    a, b = tables(LEAD_A), tables(LEAD_B)
    assert all(transform(a, perm, mask) != b for perm in permutations(range(3)) for mask in range(8))

def test_distinct_sets_but_common_correct_node():
    # Reported pinned-PyPhi target sets: no IIT computation is made by this test.
    p, q = {0, 2}, {2}
    assert p != q and p & q == {2}

def test_one_step_conditional_recovery():
    for code in (LEAD_A, LEAD_B):
        P = transition(code)
        assert reconstruct_rules_from_one_step_marginals(P) == tables(code)

def test_population_peak_prominence_zero():
    from fractions import Fraction
    for code in (LEAD_A, LEAD_B):
        assert population_q220_peak_prominences(transition(code)) == (0, 0, 0)
