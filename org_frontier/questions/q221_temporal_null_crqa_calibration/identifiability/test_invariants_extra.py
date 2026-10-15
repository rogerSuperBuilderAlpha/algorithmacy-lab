"""Additional q221 invariant tests (mandate addendum). Fast tier: exact-arithmetic process-law and isomorphism
checks. Expensive tier (pinned PyPhi; ~seconds each but requires the IIT-4.0 PyPhi build) runs only when
Q221_SLOW=1, e.g.
  Q221_SLOW=1 /workspace/algorithmacy-827-venv/bin/python -m pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration/identifiability/test_invariants_extra.py"""
import os
from itertools import permutations

import pytest

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import (
    TABLES, ext_canon, stats)
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.iso_check_hassan_pair import apply
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.process_law_equivalence import equivalent

P, Q = ("aff", 9, 6, 10), ("aff", 9, 15, 10)
SURVIVORS = [(P, Q), (("aff", 9, 6, 10), ("aff", 9, 15, 12)), (("aff", 9, 6, 11), ("aff", 9, 14, 10))]
slow = pytest.mark.skipif(os.environ.get("Q221_SLOW") != "1", reason="expensive tier: set Q221_SLOW=1")


def test_iso_checker_detects_relabelled_copy():
    # every permuted + value-flipped copy of P must canonicalise to the same class as P
    for p in permutations(range(3)):
        for m in range(8):
            assert ext_canon(apply(TABLES[P], p, m)) == ext_canon(TABLES[P])


def test_all_survivors_pairwise_equal_and_non_isomorphic():
    for a, b in SURVIVORS:
        sa, sb = stats(a), stats(b)
        assert not sa[0] and sa[1:] == sb[1:]
        assert ext_canon(TABLES[a]) != ext_canon(TABLES[b])


def test_process_law_sanity_and_lead_pair_projection_pattern():
    assert equivalent((0, 1, 2), P, P)[0]
    assert equivalent((0,), ("aff", 6, 9, 5), ("aff", 11, 9, 5))[0]      # isomorphic pair, X fixed by the map
    assert not equivalent((0,), ("nsi", 0, 3, 3), ("aff", 6, 9, 5))[0]   # X marginal differs
    expected = {(0,): True, (1,): True, (2,): True, (0, 1): False, (0, 2): True, (1, 2): False, (0, 1, 2): False}
    for chans, eq in expected.items():
        assert equivalent(chans)[0] is eq, chans


@slow
def test_lead_pair_phi_and_q161_targets():
    from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import bottleneck_set, major_complex
    from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
    L = ("X", "Y", "H")
    out = {}
    for fid in (P, Q):
        rules = ps.table_form(TABLES[fid])
        core, phi = major_complex(rules, L)
        B, base, drops = bottleneck_set(rules, L)
        out[fid] = (tuple(core), round(float(phi), 6), sorted(int(b) for b in B))
    assert out[P][:2] == out[Q][:2] and out[P][1] == 2.0
    assert out[P][2] == [0, 2] and out[Q][2] == [2]
    # determinism: second evaluation identical
    rules = ps.table_form(TABLES[Q])
    assert sorted(int(b) for b in bottleneck_set(rules, L)[0]) == [2]


@slow
def test_q161_target_invariant_under_value_flips():
    from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import bottleneck_set
    from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
    L = ("X", "Y", "H")
    for fid in (P, Q):
        B0 = set(bottleneck_set(ps.table_form(TABLES[fid]), L)[0])
        for m in range(1, 8):
            assert set(bottleneck_set(ps.table_form(apply(TABLES[fid], (0, 1, 2), m)), L)[0]) == B0


@slow
def test_background_condition_variant_removes_lead_pair_target_difference():
    from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
    from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.target_variants import background_variant
    for v in (0, 1):
        bp = background_variant(ps.table_form(TABLES[P]), v)
        bq = background_variant(ps.table_form(TABLES[Q]), v)
        assert bp == bq and bp[2] == [0, 2]
