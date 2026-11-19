"""Fast regression for the exact affine minimum-size certificate (exploratory)."""
from .minimality_affine import certificate


def test_minimum_nonisomorphic_profile_collision_is_three_nodes():
    result = certificate()
    assert result["dimensions"]["1"]["systems"] == 2
    assert result["dimensions"]["1"]["equal_profile_pairs"] == 0
    assert result["dimensions"]["2"]["systems"] == 24
    assert result["dimensions"]["2"]["profile_classes"] == 16
    assert result["dimensions"]["2"]["equal_profile_pairs"] == 8
    assert result["dimensions"]["2"]["nonisomorphic_equal_profile_pairs"] == 0
    assert result["first_nonisomorphic_ambiguity_n"] == 3
    assert result["witness_affine_codes"] == {"A": [9, 6, 10], "B": [9, 15, 10]}
