"""Minimal property tests for the comparator study (comparators.py). These are fast and need no SHREC or PyPhi."""
from fractions import Fraction

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.comparators import (
    PAIRS, exact_features, te_hat, jrr_hat, md_hat, ncc)
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES, tpm, stationary


def test_mdrqa_rate_equal_for_all_survivors_and_is_trace_invariant():
    # stationary law is uniform, so RR_3(k) = trace(P^k)/8: a spectral invariant, equal for every survivor pair
    for a, b in PAIRS:
        ea, eb = exact_features(a)["C3_MdRR"], exact_features(b)["C3_MdRR"]
        assert ea == eb
        P = tpm(TABLES[a]); assert stationary(P) == [Fraction(1, 8)] * 8
        Pk = P
        assert ea[0] == sum(Pk[s][s] for s in range(8)) / 8


def test_transfer_entropy_and_joint_recurrence_separate_lead_pair_exactly():
    a, b = PAIRS[0]
    ea, eb = exact_features(a), exact_features(b)
    assert abs(ea["C1_TE"][0] - 0.597821) < 1e-6 and abs(eb["C1_TE"][0]) < 1e-12   # TE X->Y: P > 0, Q = 0
    assert ea["C1_TE"][1:] == eb["C1_TE"][1:]                                      # other directions equal
    assert ea["C2_JRR"][10:20] == eb["C2_JRR"][10:20]                              # (X,H) block equal (XH law equal)
    assert ea["C2_JRR"][:10] != eb["C2_JRR"][:10]                                  # (X,Y) block differs


def test_plugin_estimators_consistent_with_exact_values():
    a, _ = PAIRS[0]
    x = trajectory(ps.table_form(TABLES[a]), 20000, np.random.default_rng(1), flip=0.08, warmup=20).astype(int)
    ex = exact_features(a)
    assert np.max(np.abs(np.array(te_hat(x)) - ex["C1_TE"])) < 0.03
    assert np.max(np.abs(np.array(jrr_hat(x)) - [float(v) for v in ex["C2_JRR"]])) < 0.03
    assert np.max(np.abs(np.array(md_hat(x)) - [float(v) for v in ex["C3_MdRR"]])) < 0.03


def test_ncc_classifier_basic():
    rng = np.random.default_rng(0)
    Ftr = np.r_[rng.normal(0, 1, (50, 2)), rng.normal(5, 1, (50, 2))]; ytr = np.r_[np.zeros(50), np.ones(50)].astype(int)
    k, n = ncc(Ftr, ytr, Ftr, ytr)
    assert n == 100 and k >= 98
