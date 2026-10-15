"""Tests for the timestamp-aware observation / recurrence utilities. Small synthetic cases with
answers known analytically, plus exact equivalence to the existing CRQA code. Passing tests show the
code does what its contract says; they do not show the science is valid."""

import numpy as np
import pytest

from org_frontier.recurrence import crqa
from org_frontier.questions.q220_observation_process_robustness import corruptions
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob

TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def _traj(seed=0, steps=600):
    return crqa.trajectory(TRIAD, steps, np.random.default_rng(seed), flip=0.08, warmup=20)


# ---------------------------------------------------------------- equivalence with nothing missing

@pytest.mark.parametrize("mode", ob.MODES)
def test_full_record_equals_legacy_dcrp(mode):
    T = _traj()
    t = np.arange(T.shape[0])
    for a in range(3):
        for b in range(3):
            lags, rate, cnt = ob.lag_profile(t, T[:, a], T[:, b], 10, mode)
            l0, p0 = crqa.dcrp(T[:, a], T[:, b], 10)
            assert np.array_equal(lags, l0)
            assert np.array_equal(rate, p0)
            assert np.array_equal(cnt, T.shape[0] - np.abs(lags))


@pytest.mark.parametrize("mode", ob.MODES)
def test_full_record_equals_legacy_coupling_and_centrality(mode):
    for seed in range(3):
        T = _traj(seed)
        res = ob.coupling(np.arange(T.shape[0]), T, 10, mode, min_pairs=30)
        lag0, prom0 = crqa.coupling_matrix(T, 10)
        assert np.array_equal(res["prom"], prom0)
        iu = np.triu_indices(3, 1)
        assert np.array_equal(res["lag"][iu], lag0[iu])
        assert np.array_equal(ob.centrality(res["prom"]), crqa.coupling_centrality(T, 10, 0.05))
        assert res["insufficient"] == 0


def test_index_mode_equals_gap_closed_legacy():
    T = _traj(1)
    keep = ob.mar_mask(T.shape[0], 0.3, np.random.default_rng(5))
    t, V = ob.observe(T, keep)
    res = ob.coupling(t, V, 10, "index")
    _, prom0 = crqa.coupling_matrix(T[keep], 10)
    assert np.array_equal(res["prom"], prom0)


# ---------------------------------------------------------------- masks reproduce the original operators

@pytest.mark.parametrize("m", [0.0, 0.1, 0.3, 0.5])
def test_masks_match_original_operators(m):
    T = _traj(2)
    for seed in range(5):
        k1 = ob.mar_mask(T.shape[0], m, np.random.default_rng(10_000 + seed))
        assert np.array_equal(T[k1], corruptions.mar(T, m, np.random.default_rng(10_000 + seed)))
        k2 = ob.burst_mask(T.shape[0], m, np.random.default_rng(10_000 + seed))
        assert np.array_equal(T[k2], corruptions.burst(T, m, np.random.default_rng(10_000 + seed)))


def test_mar_masks_nested_across_doses():
    a = ob.mar_mask(1000, 0.1, np.random.default_rng(3))
    b = ob.mar_mask(1000, 0.3, np.random.default_rng(3))
    assert np.all(b <= a)


# ---------------------------------------------------------------- known-lag recovery

def test_known_lag_recovered_exactly_by_timestamp_not_by_gap_closing():
    rng = np.random.default_rng(0)
    x = rng.integers(0, 2, 3000)
    y = np.roll(x, 3)                        # y[t] = x[t-3]: x leads by 3
    y[:3] = rng.integers(0, 2, 3)
    keep = ob.mar_mask(3000, 0.3, np.random.default_rng(1))
    t = np.flatnonzero(keep)
    lags, rate, cnt = ob.lag_profile(t, x[keep], y[keep], 10, "timestamp")
    assert rate[lags == 3][0] == pytest.approx(1.0)
    assert ob.peak_prominence(lags, rate, cnt, 30)[0] == 3
    lags, rate_s, _ = ob.lag_profile(t, x[keep], y[keep], 10, "segment")
    assert rate_s[lags == 3][0] == pytest.approx(1.0)
    _, rate_i, _ = ob.lag_profile(t, x[keep], y[keep], 10, "index")
    # gap-closing pairs index lag 3 with true lags >= 3: only (1-m)^3 ~ 0.34 are true lag-3 pairs
    assert rate_i[lags == 3][0] < 0.8


def test_lag_zero_untouched_by_row_deletion():
    T = _traj(4)
    keep = ob.mar_mask(T.shape[0], 0.5, np.random.default_rng(9))
    t, V = ob.observe(T, keep)
    for mode in ob.MODES:
        lags, rate, _ = ob.lag_profile(t, V[:, 0], V[:, 2], 3, mode)
        assert rate[lags == 0][0] == pytest.approx(float((V[:, 0] == V[:, 2]).mean()))


# ---------------------------------------------------------------- pair counts on a hand-checked pattern

def test_pair_counts_by_mode():
    t = np.array([0, 1, 2, 4, 5, 7])
    # timestamp: lag1 (0,1)(1,2)(4,5); lag2 (0,2)(2,4)(5,7); lag3 (1,4)(2,5)(4,7)
    # segment: segments {0,1,2},{4,5},{7}: lag1 3, lag2 1, lag3 0
    # index: n - k
    exp = {"timestamp": [3, 3, 3], "segment": [3, 1, 0], "index": [5, 4, 3]}
    for mode, want in exp.items():
        got = [ob.lag_pairs(t, k, mode)[0].size for k in (1, 2, 3)]
        assert got == want, mode
        # negative lags mirror positive lags
        assert [ob.lag_pairs(t, -k, mode)[0].size for k in (1, 2, 3)] == want


def test_timestamp_and_segment_never_bridge():
    rng = np.random.default_rng(7)
    for _ in range(20):
        t = np.flatnonzero(rng.random(200) > 0.4)
        seg = ob.segment_ids(t)
        for k in range(-6, 7):
            i, j = ob.lag_pairs(t, k, "timestamp")
            assert np.all(t[j] - t[i] == k)
            i, j = ob.lag_pairs(t, k, "segment")
            assert np.all(t[j] - t[i] == k) and np.all(seg[i] == seg[j])
            lo, hi = np.minimum(t[i], t[j]), np.maximum(t[i], t[j])
            assert all(np.all(np.isin(np.arange(a, b + 1), t)) for a, b in zip(lo, hi))


def test_segment_ids():
    assert list(ob.segment_ids(np.array([0, 1, 2, 4, 5, 7]))) == [0, 0, 0, 1, 1, 2]
    assert ob.segment_ids(np.array([], dtype=int)).size == 0


# ---------------------------------------------------------------- too few observations

def test_empty_and_tiny_records():
    for t in (np.array([], dtype=int), np.array([5])):
        V = np.zeros((t.size, 3), dtype=int)
        for mode in ob.MODES:
            lags, rate, cnt = ob.lag_profile(t, V[:, 0], V[:, 1], 4, mode)
            assert cnt.sum() == t.size          # only lag 0 can pair, once per observation
            res = ob.coupling(t, V, 4, mode, min_pairs=30)
            assert res["insufficient"] == 3 and np.all(res["prom"] == 0)


def test_min_pairs_and_min_lags():
    lags = np.arange(-2, 3)
    rate = np.array([0.5, 0.9, 0.5, 0.5, 0.5])
    cnt = np.array([100, 100, 100, 100, 100])
    assert ob.peak_prominence(lags, rate, cnt, 30) == (-1, pytest.approx(0.4), True)
    cnt2 = np.array([100, 10, 100, 100, 100])     # the peak lag is no longer usable
    assert ob.peak_prominence(lags, rate, cnt2, 30) == (-2, pytest.approx(0.0), True)
    cnt3 = np.array([100, 0, 0, 0, 100])
    assert ob.peak_prominence(lags, rate, cnt3, 30) == (0, 0.0, False)


def test_validate_times_rejects_bad_input():
    for bad in (np.array([0, 0, 1]), np.array([3, 2]), np.array([-1, 0]), np.array([0.0, 1.0])):
        with pytest.raises(ValueError):
            ob.validate_times(bad)
    with pytest.raises(ValueError):
        ob.lag_pairs(np.array([0, 1]), 1, "bogus")
    with pytest.raises(ValueError):
        ob.observe(np.zeros((4, 2)), np.ones(3, bool))


# ---------------------------------------------------------------- determinism and null behaviour

def test_deterministic_replay():
    T = _traj(3)
    target = np.full(21, 200)
    r1 = ob.thinned_profile(T[:, 0], T[:, 1], 10, target, np.random.default_rng(30_000))
    r2 = ob.thinned_profile(T[:, 0], T[:, 1], 10, target, np.random.default_rng(30_000))
    assert all(np.array_equal(a, b, equal_nan=True) for a, b in zip(r1, r2))
    assert np.array_equal(r1[2], target)
    k1 = ob.mar_mask(600, 0.3, np.random.default_rng(11))
    k2 = ob.mar_mask(600, 0.3, np.random.default_rng(11))
    assert np.array_equal(k1, k2)
    a = ob.coupling(*ob.observe(T, k1), 10, "timestamp", 30)
    b = ob.coupling(*ob.observe(T, k2), 10, "timestamp", 30)
    assert np.array_equal(a["prom"], b["prom"])


def test_independent_channels_have_no_prominent_peak():
    rng = np.random.default_rng(0)
    proms = []
    for s in range(20):
        V = rng.integers(0, 2, size=(5000, 2))
        keep = ob.mar_mask(5000, 0.3, np.random.default_rng(s))
        res = ob.coupling(*ob.observe(V, keep), 10, "timestamp", 30)
        proms.append(res["prom"][0, 1])
    assert max(proms) < 0.05


def test_fabricated_share():
    assert np.all(ob.fabricated_share(np.arange(100), 5) == 0)
    keep = ob.mar_mask(200_000, 0.3, np.random.default_rng(0))
    share = ob.fabricated_share(np.flatnonzero(keep), 3)
    # true lag k behind index lag k requires the k-1 intermediate and the endpoint all observed
    assert share[0] == pytest.approx(0.3, abs=0.01)
    assert share[1] == pytest.approx(1 - 0.7 ** 2, abs=0.01)


# ---------------------------------------------------------------- bottleneck scoring

def test_bottleneck_scores():
    assert ob.bottleneck_scores([0.1, 0.3, 0.2], {1}) == (1.0, 1, False)
    assert ob.bottleneck_scores([0.3, 0.3, 0.2], {1}) == (0.5, 0, False)     # tie: half credit
    assert ob.bottleneck_scores([0, 0, 0, 0], {0, 2}) == (0.5, 0, True)       # chance, flagged
    assert ob.bottleneck_scores([0.2, 0.1], set()) == (0.0, 0, False)


# ---- pre-review audit: brute-force references with no shared code path

def _brute_profile(times, x, y, max_lag, segment):
    """Every (i, j) with times[j] - times[i] == k; if segment, also no missing timestamp between them."""
    t = list(times)
    tset = set(t)
    out = {}
    for k in range(-max_lag, max_lag + 1):
        hits = n = 0
        for i in range(len(t)):
            for j in range(len(t)):
                if t[j] - t[i] != k:
                    continue
                lo_, hi_ = min(t[i], t[j]), max(t[i], t[j])
                if segment and any(u not in tset for u in range(lo_, hi_ + 1)):
                    continue
                n += 1
                hits += int(x[i] == y[j])
        out[k] = (n, hits / n if n else np.nan)
    return out


@pytest.mark.parametrize("seed", range(6))
@pytest.mark.parametrize("mode", ["timestamp", "segment"])
def test_lag_profile_matches_brute_force(seed, mode):
    rng = np.random.default_rng(seed)
    T = 60
    keep = rng.random(T) > rng.uniform(0.1, 0.6)
    keep[rng.integers(T)] = True
    t = np.flatnonzero(keep) + int(rng.integers(0, 3))   # also a non-zero first timestamp
    x, y = rng.integers(0, 2, t.size), rng.integers(0, 2, t.size)
    lags, rate, cnt = ob.lag_profile(t, x, y, 7, mode)
    ref = _brute_profile(t, x, y, 7, mode == "segment")
    for k, r, c in zip(lags, rate, cnt):
        assert c == ref[int(k)][0]
        if c:
            assert r == pytest.approx(ref[int(k)][1])
        else:
            assert np.isnan(r)


def test_thinned_profile_matches_target_counts_and_never_exceeds_available():
    rng = np.random.default_rng(0)
    x, y = rng.integers(0, 2, 50), rng.integers(0, 2, 50)
    target = np.array([5, 0, 49, 50, 1000])          # lags -2..2; available 48, 49, 50, 49, 48
    lags, rate, cnt = ob.thinned_profile(x, y, 2, target, np.random.default_rng(1))
    assert list(cnt) == [5, 0, 49, 49, 48]
    assert np.isnan(rate[1]) and not np.isnan(rate[0])


def test_bottleneck_tie_within_tolerance_is_a_tie():
    cc = np.array([0.3, 0.3 + 1e-15, 0.1])
    score, pick, noev = ob.bottleneck_scores(cc, {0})
    assert score == 0.5 and not noev
