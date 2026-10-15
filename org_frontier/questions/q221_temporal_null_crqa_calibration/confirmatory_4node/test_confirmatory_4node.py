"""Property tests for the preregistered 4-node study of target A (PREREGISTRATION.md).
Fast tier runs by default; the full exact screen re-run needs Q221_SLOW=1."""
import json
import os
from fractions import Fraction

import numpy as np
import pytest

from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import f4
from org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node import study4 as s4

HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "results")
slow = pytest.mark.skipif(os.environ.get("Q221_SLOW") != "1", reason="expensive tier: set Q221_SLOW=1")


def _screen():
    return json.load(open(os.path.join(RES, "screen4.json")))


def _study():
    return json.load(open(os.path.join(RES, "study4.json")))


@pytest.fixture(scope="module")
def As():
    return f4.invertible_As()


def test_gl42_order(As):
    assert len(As) == (16 - 1) * (16 - 2) * (16 - 4) * (16 - 8) == 20160


def test_prop1_closed_form_equals_bruteforce_exact(As):
    rng = np.random.default_rng(7310001)          # outside every study seed range
    for x in rng.choice(len(As) * 16, 8, replace=False):
        A, c = As[int(x) // 16], int(x) % 16
        marg, prof = f4.exact_profiles(A, c, 20)
        p1 = f4.prop1_profiles(A, c, 20)
        assert marg == [Fraction(1, 2)] * 4
        assert all(prof[k] == p1[k] for k in prof)


def test_signature_decides_profile_equality_on_random_pairs(As):
    rng = np.random.default_rng(7310002)
    for _ in range(10):
        i, j = rng.choice(len(As) * 16, 2, replace=False)
        a, b = (As[int(i) // 16], int(i) % 16), (As[int(j) // 16], int(j) % 16)
        same_sig = f4.signature(*a) == f4.signature(*b)
        same_prof = f4.exact_profiles(*a, 20) == f4.exact_profiles(*b, 20)
        assert same_sig == same_prof


def test_orbit_id_is_invariant_and_matches_direct_enumeration(As):
    rng = np.random.default_rng(7310003)
    sample = [As[int(i)] for i in rng.choice(len(As), 6, replace=False)]
    codes, orb = f4.orbit_ids(sample)
    oid = dict(zip(codes.tolist(), orb.tolist()))
    for A in sample:
        c = int(rng.integers(16))
        direct = min(t[0] * 16 + t[1] for t in (f4.transform(A, c, p, m) for p in f4.PERMS for m in range(16)))
        assert oid[A * 16 + c] == direct
        p, m = f4.PERMS[int(rng.integers(24))], int(rng.integers(16))
        A2, c2 = f4.transform(A, c, p, m)
        assert f4.isomorphic((A, c), (A2, c2))
        _, o2 = f4.orbit_ids([A2])
        assert int(o2[c2]) == oid[A * 16 + c]
        # relabeling preserves the pairwise summaries up to relabeling and value flips (p <-> 1 - p)
        dev = lambda sys_: sorted(abs(2 * v - 1) for v in f4.exact_profiles(*sys_, 6)[1].values())
        assert dev((A, c)) == dev((A2, c2))


def test_screen_counts_and_verifications_recorded():
    s = _screen()
    assert s["counts"] == dict(GL42=20160, systems=322560, orbits=1864, classes=66121, multi_member_classes=64201,
                               largest_class=192, classes_ge2_orbits=30216, noniso_system_pairs=1366408,
                               orbit_pairs=1872)
    assert s["v1_pass"] == 300 and s["v2_pass"] == 40 and len(s["study_pairs"]) == 40
    assert all(p["v2_profiles_equal"] and p["v2_tpm_differ"] and p["v2_non_isomorphic"] for p in s["study_pairs"])


def test_study_pairs_recurrence_equal_law_different_nonisomorphic():
    for p in _screen()["study_pairs"][:4]:
        a, b = tuple(p["a"]), tuple(p["b"])
        assert f4.signature(*a) == f4.signature(*b)
        assert f4.exact_profiles(*a, 20) == f4.exact_profiles(*b, 20)
        assert not np.array_equal(f4.tpm_int(*a), f4.tpm_int(*b))
        assert not f4.isomorphic(a, b)
        assert f4.orbit_ids([a[0]])[1][a[1]] != f4.orbit_ids([b[0]])[1][b[1]]


def test_mdrr_is_trace_invariant_and_not_always_equal_at_n4():
    pairs = {p["q"]: p for p in _screen()["study_pairs"]}
    # q = 2 shares A and differs only in c; recorded exact MdRR difference is non-zero
    a, b = tuple(pairs[2]["a"]), tuple(pairs[2]["b"])
    ea, eb = s4.exact_pop(*a), s4.exact_pop(*b)
    M = f4.tpm_int(*a); den = f4.P_DEN ** 4
    Pk = np.identity(16, dtype=object) * 1
    for k in range(3):
        Pk = Pk.dot(M)
        assert ea["C3_MdRR"][k] == Fraction(sum(Pk[s, s] for s in range(16)), 16 * den ** (k + 1))
    assert ea["C3_MdRR"] != eb["C3_MdRR"]        # unlike the n = 3 survivors, MdRR can separate at n = 4
    assert ea["C1_TE"] == pytest.approx(eb["C1_TE"], abs=1e-12)   # while exact TE is equal for this pair


def test_study_summary_reproduces_decision_rules():
    d = _study()
    rows = d["pairs"]; M = len(rows)
    assert M == 40 and all(r["n_test"] == 400 for r in rows)
    acc = np.array([r["correct"]["R"] / r["n_test"] for r in rows])
    from scipy import stats
    half = stats.t.ppf(0.95, M - 1) * acc.std(ddof=1) / np.sqrt(M)
    assert 0.45 < acc.mean() - half and acc.mean() + half < 0.55               # H2 (TOST) as recorded
    for nm in s4.NAMES:
        k = sum(s4.wilson(r["correct"][nm], r["n_test"], d["z_pair"])[0] > 0.5 for r in rows)
        assert k == sum(bool(r["separates"][nm]) for r in rows)
    assert all(r["correct"]["C0_likelihood"] == 400 for r in rows)
    assert sum(bool(r["separates"]["R"]) for r in rows) == 0


@slow
def test_full_exact_screen_counts_rerun(As):
    from collections import defaultdict
    codes, orb = f4.orbit_ids(As)
    orbit = dict(zip(codes.tolist(), orb.tolist()))
    assert len(set(orb.tolist())) == 1864
    classes = defaultdict(list)
    for A in As:
        for c in range(16):
            classes[f4.signature(A, c)].append(A * 16 + c)
    pairs = set()
    for members in classes.values():
        os_ = sorted({orbit[m] for m in members})
        pairs.update((x, y) for i, x in enumerate(os_) for y in os_[i + 1:])
    assert len(classes) == 66121 and len(pairs) == 1872
