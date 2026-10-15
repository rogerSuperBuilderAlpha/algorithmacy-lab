"""Estimator B is a classical estimator (post-merge audit, literature check L1).

The timestamp-aware lag profile (`observe.lag_profile(..., "timestamp")`, estimator B) equals, at every lag:
  * Parzen's (1963) amplitude-modulated estimator: sum_t a_t a_{t+k} 1[x_t == y_{t+k}] / sum_t a_t a_{t+k},
    with a_t the observation indicator on the full grid;
  * the Edelson & Krolik (1988) discrete correlation function with unit lag bins centred on integer lags,
    i.e. all observed pairs (i, j) with t_j - t_i in [k - 1/2, k + 1/2).
The gap-closing profile (estimator A, mode "index") does not. These tests pin the identities stated in
`literature/deep_research_report.md`; they change no estimator. numpy only."""

import numpy as np
import pytest

from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob

T, MAX_LAG, K = 600, 10, 3


def _case(seed, m):
    rng = np.random.default_rng(seed)
    x = rng.integers(0, K, T)
    y = np.where(rng.random(T) < 0.7, np.roll(x, 2), rng.integers(0, K, T))
    keep = rng.random(T) >= m
    return x, y, keep


def _parzen(x, y, keep, k):
    a = keep.astype(float)
    t1, t2 = (np.arange(0, T - k), np.arange(k, T)) if k >= 0 else (np.arange(-k, T), np.arange(0, T + k))
    w = a[t1] * a[t2]
    return (w * (x[t1] == y[t2])).sum() / w.sum(), int(w.sum())


@pytest.mark.parametrize("seed,m", [(s, m) for s in range(4) for m in (0.1, 0.3, 0.5)])
def test_timestamp_profile_equals_parzen_and_unit_bin_dcf(seed, m):
    x, y, keep = _case(seed, m)
    times = np.flatnonzero(keep)
    xo, yo = x[keep], y[keep]
    lags, rate, count = ob.lag_profile(times, xo, yo, MAX_LAG, "timestamp")
    dt = times[None, :] - times[:, None]
    match = xo[:, None] == yo[None, :]
    for idx, k in enumerate(lags):
        p, n = _parzen(x, y, keep, int(k))
        assert count[idx] == n
        assert rate[idx] == pytest.approx(p, abs=1e-12)
        sel = (dt >= k - 0.5) & (dt < k + 0.5)
        assert rate[idx] == pytest.approx(match[sel].mean(), abs=1e-12)


def test_gap_closed_profile_differs_when_rows_are_missing():
    x, y, keep = _case(7, 0.3)
    times = np.flatnonzero(keep)
    _, rb, _ = ob.lag_profile(times, x[keep], y[keep], MAX_LAG, "timestamp")
    _, ra, _ = ob.lag_profile(times, x[keep], y[keep], MAX_LAG, "index")
    assert np.nanmax(np.abs(rb - ra)) > 0.05
