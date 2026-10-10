"""Settling-time measures for Boolean coordination forms (Strand G follow-on).

Reusable diagnostics that ask whether a form's residual Equality-of-Averages
gap under a basin-restricted reference is a finite-T burn-in effect rather
than ergodicity-breaking. No Φ computation lives here.

Measures (definitions frozen by studies that import them):

(a) **Transient length** — steps from a start until the trajectory first
    lands on its attractor cycle. Per-form summaries over an ensemble:
    mean, max, and basin-mass-weighted mean of per-basin means.

(b) **Time-average convergence T** — smallest horizon T at which the
    cumulative time average of a party observable lies within ε of the
    uniform mean on the attractor the start reaches. Reported as the
    mean / max over (start × party) cells.

(c) **Noisy-chain relaxation** — under flip noise ε_flip > 0, the
    spectral gap of the row-stochastic TPM and the implied relaxation
    time 1/gap (independent of the deterministic basin partition).

(d) **Attractor oscillation** — fraction of (party-bit × attractor)
    cells where the bit is non-constant on the cycle; mean Bernoulli
    variance of party bits on cycles; mean / max period.

(e) **Pre-cycle path diversity** — mean over starts of the number of
    distinct party-bit tuples visited strictly before cycle entry,
    scaled by ``2^{n_parties}`` into [0, 1].

(f) **Cycle ordering** — finite-T phase remainder of a party bit on a
    deterministic cycle, and sequence features of how those bits flip
    around the cycle. Definitions are frozen by
    ``studies/ergodic_cycle_ordering/hypotheses.md``. On a cycle of
    period ``p`` with values ``x_0,…,x_{p-1}`` and mean ``μ``, a start
    at phase ``φ`` and horizon ``T = qp + r`` (``r = T mod p``) has
    signed remainder

        (Ā_T(φ) − μ) = (1/T) · (Σ_{k=0}^{r-1} x_{(φ+k) mod p} − r μ)

    when ``r > 0``, and ``0`` when ``r = 0``. The cycle-only predicted
    gap averages ``|Ā_T − μ|`` over phases, party bits, and basins
    (basin-mass weights). Ordering-versus-amplitude uses the same
    window at the same ``T``: ``order_excess = R_obs − R_spread`` and
    ``order_index = (R_obs − R_spread) / (R_clump − R_spread)`` when
    the denominator is nonzero, else ``0``. ``R_spread`` is the mean
    absolute remainder of the most evenly spaced binary placement of
    the same weight; ``R_clump`` is the placement with all ones
    consecutive. Co-flip synchrony, folded phase lag, lag-1
    autocorrelation, the party-bit Hamming rate, and the canonical
    flip-mask signature are properties of the cycle and do not depend
    on ``T``, except that ``order_index`` / ``order_excess`` /
    ``pred_gap_cycle`` do.

Covariates recorded alongside: attractor periods, number of attractors,
state-space size. Extensions (d)–(f) are backward compatible: prior
call sites and summaries are unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Optional, Sequence, Union

import math

from org_frontier.ergodicity.eoa import (
    NextMap,
    Observable,
    Rules,
    State,
    attractor_partition,
    bit_observable,
    cycle_mean,
    noisy_transition_matrix,
    rules_to_next_map,
    uniform_ensemble,
)

# Frozen defaults for studies; override only under pre-registration.
DEFAULT_EPS_CONV = 0.01
DEFAULT_T_MAX = 256
DEFAULT_EPS_FLIP = 0.05
DEFAULT_TV_DELTA = 0.25


@dataclass(frozen=True)
class TransientSummary:
    """Per-form transient-length summary over an ensemble of starts."""

    mean: float
    max: float
    basin_weighted_mean: float
    n_starts: int
    n_attractors: int
    mean_period: float
    max_period: int
    state_space_size: int
    # Optional per-start lengths (omitted from CSV dumps when empty).
    lengths: tuple = field(default=(), repr=False)

    def to_dict(self) -> dict:
        d = asdict(self)
        d.pop("lengths", None)
        return d


@dataclass(frozen=True)
class ConvergenceSummary:
    """Per-form time-average convergence summary over (start × party) cells."""

    mean_T: float
    max_T: float
    median_T: float
    n_cells: int
    n_unresolved: int  # cells that never entered the ε-ball by T_max
    eps_conv: float
    t_max: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class MixingSummary:
    """Spectral gap / relaxation time of the flip-noise chain."""

    spectral_gap: float
    relaxation_time: float
    tv_mixing_bound: float  # ceil(log(1/δ) / gap); inf if gap=0
    eps_flip: float
    tv_delta: float
    n_states: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class OscillationSummary:
    """Party-bit oscillation on attractor cycles (phase-artifact covariate)."""

    party_osc_frac: float  # non-constant (party × cycle) / (n_parties × n_cycles)
    mean_cycle_var: float  # mean p(1-p) over (party × cycle) cells
    mean_period: float  # basin-mass-weighted mean cycle length over ens
    max_period: int
    n_attractors: int
    n_party_bits: int
    n_oscillating_cells: int
    n_cells: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class PathDiversitySummary:
    """Within-basin pre-cycle observable heterogeneity."""

    pre_cycle_div: float  # mean |distinct party tuples on transient| / 2^{n_p}
    mean_distinct: float  # unscaled mean distinct count
    mean_transient: float
    n_starts: int
    n_party_bits: int
    scale: int  # 2^{n_party_bits}

    def to_dict(self) -> dict:
        return asdict(self)


def _resolve_form(
    form: Union[NextMap, Rules], n: Optional[int]
) -> tuple[NextMap, int]:
    if isinstance(form, dict):
        nxt = form
        if n is None:
            n = len(next(iter(nxt.keys())))
        return nxt, n
    nxt = rules_to_next_map(form, n=n)
    n_out = len(form) if n is None else n
    return nxt, n_out


def transient_length(nxt: NextMap, start: State) -> int:
    """Steps from ``start`` until the trajectory first enters its cycle.

    Walks the deterministic map, recording first-visit times. When a
    previously seen state reappears, the cycle begins at that visit; the
    transient length is the index of the first cycle state (0 if ``start``
    already lies on the cycle). Caps at ``len(nxt)`` (finite maps always
    enter a cycle by then).
    """
    cur = start
    seen: dict[State, int] = {}
    t = 0
    limit = len(nxt)
    while cur not in seen and t <= limit:
        seen[cur] = t
        cur = nxt[cur]
        t += 1
    if cur not in seen:
        # Should not happen on a total finite map; treat path as all transient.
        return t
    return seen[cur]


def summarize_transients(
    form: Union[NextMap, Rules],
    *,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
) -> TransientSummary:
    """Mean / max / basin-weighted mean transient length over an ensemble.

    Basin-weighted mean: for each attractor basin, take the mean transient
    of ensemble starts that drain to it, then average those basin means
    weighted by the number of ensemble starts in the basin. On the full
    uniform state space this equals the ordinary mean; it remains well-
    defined for subsampled ensembles.
    """
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    part = attractor_partition(nxt)
    lengths = [transient_length(nxt, s) for s in ens]
    if not lengths:
        return TransientSummary(
            mean=float("nan"),
            max=float("nan"),
            basin_weighted_mean=float("nan"),
            n_starts=0,
            n_attractors=len(part["cycles"]),
            mean_period=float("nan"),
            max_period=0,
            state_space_size=len(nxt),
            lengths=(),
        )
    mean = sum(lengths) / float(len(lengths))
    mx = float(max(lengths))
    # Basin-weighted mean of per-basin means.
    buckets: dict[int, list[int]] = {}
    for s, L in zip(ens, lengths):
        buckets.setdefault(part["basin_of"][s], []).append(L)
    weighted = 0.0
    for vs in buckets.values():
        weighted += (sum(vs) / float(len(vs))) * len(vs)
    basin_w = weighted / float(len(ens))
    periods = [len(c) for c in part["cycles"]]
    # Basin-mass-weighted mean period over the ensemble.
    period_sum = 0.0
    for s in ens:
        period_sum += len(part["cycle_of_state"][s])
    mean_period = period_sum / float(len(ens))
    return TransientSummary(
        mean=mean,
        max=mx,
        basin_weighted_mean=basin_w,
        n_starts=len(ens),
        n_attractors=len(part["cycles"]),
        mean_period=mean_period,
        max_period=max(periods) if periods else 0,
        state_space_size=len(nxt),
        lengths=tuple(lengths),
    )


def time_avg_prefix(
    nxt: NextMap,
    start: State,
    observable: Observable,
    horizon: int,
) -> list[float]:
    """Cumulative time averages of ``observable`` for T = 1..horizon.

    Index 0 is the average after 1 sample (the start); index k−1 is the
    average of the first k states on the deterministic trajectory
    (transient then cycling). Trajectories longer than the state space
    wrap on the attracting cycle.
    """
    if horizon < 1:
        return []
    # Build a long enough series: transient + enough cycle repeats.
    cur = start
    seen: dict[State, int] = {}
    path: list[State] = []
    t = 0
    limit = max(horizon, len(nxt) + 1)
    while cur not in seen and t < limit:
        seen[cur] = t
        path.append(cur)
        cur = nxt[cur]
        t += 1
    if cur in seen and path:
        cycle = path[seen[cur] :]
        series = list(path)
        while len(series) < horizon:
            series.extend(cycle)
        series = series[:horizon]
    else:
        series = path[:horizon]
        if not series:
            return []
        while len(series) < horizon:
            series.append(series[-1])
    out: list[float] = []
    total = 0.0
    for i, st in enumerate(series):
        total += observable(st)
        out.append(total / float(i + 1))
    return out


def convergence_time(
    nxt: NextMap,
    start: State,
    observable: Observable,
    *,
    eps_conv: float = DEFAULT_EPS_CONV,
    t_max: int = DEFAULT_T_MAX,
    attractor_mean: Optional[float] = None,
) -> int:
    """Smallest T ∈ {1..t_max} with |Ā_T − μ| < ε_conv; else t_max + 1.

    μ is the uniform mean of ``observable`` on the attractor cycle that
    ``start`` reaches, unless ``attractor_mean`` is supplied. Returning
    ``t_max + 1`` marks unresolved cells (never entered the ε-ball).
    """
    if attractor_mean is None:
        part = attractor_partition(nxt)
        attractor_mean = cycle_mean(observable, part["cycle_of_state"][start])
    avgs = time_avg_prefix(nxt, start, observable, t_max)
    for t, a in enumerate(avgs, start=1):
        if abs(a - attractor_mean) < eps_conv:
            return t
    return t_max + 1


def summarize_convergence(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
    eps_conv: float = DEFAULT_EPS_CONV,
    t_max: int = DEFAULT_T_MAX,
) -> ConvergenceSummary:
    """Mean / max / median convergence T over (start × party) cells."""
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    part = attractor_partition(nxt)
    times: list[int] = []
    for idx in party_indices:
        obs = bit_observable(idx)
        # Cache cycle means per attractor index.
        cyc_means = {
            i: cycle_mean(obs, cyc) for i, cyc in enumerate(part["cycles"])
        }
        for start in ens:
            bid = part["basin_of"][start]
            T = convergence_time(
                nxt,
                start,
                obs,
                eps_conv=eps_conv,
                t_max=t_max,
                attractor_mean=cyc_means[bid],
            )
            times.append(T)
    if not times:
        return ConvergenceSummary(
            mean_T=float("nan"),
            max_T=float("nan"),
            median_T=float("nan"),
            n_cells=0,
            n_unresolved=0,
            eps_conv=eps_conv,
            t_max=t_max,
        )
    n_unresolved = sum(1 for T in times if T > t_max)
    srt = sorted(times)
    m = len(srt)
    if m % 2 == 1:
        med = float(srt[m // 2])
    else:
        med = 0.5 * (srt[m // 2 - 1] + srt[m // 2])
    return ConvergenceSummary(
        mean_T=sum(times) / float(len(times)),
        max_T=float(max(times)),
        median_T=med,
        n_cells=len(times),
        n_unresolved=n_unresolved,
        eps_conv=eps_conv,
        t_max=t_max,
    )


def spectral_gap(P: Sequence[Sequence[float]]) -> float:
    """1 − |λ₂| for a row-stochastic matrix (numpy eigvals).

    Returns 0.0 when the chain is not uniquely mixing (gap numerically
    ≤ 0) or when the state space is empty / singleton (trivial gap = 1
    for a 1×1 matrix — returned as 1.0).
    """
    import numpy as np

    m = len(P)
    if m == 0:
        return float("nan")
    if m == 1:
        return 1.0
    A = np.asarray(P, dtype=float)
    # Right eigenvalues of row-stochastic P; λ₁ = 1.
    w = np.linalg.eigvals(A)
    # Sort by descending magnitude.
    mags = sorted((abs(complex(z)) for z in w), reverse=True)
    lam2 = mags[1] if len(mags) > 1 else 0.0
    gap = 1.0 - float(lam2)
    # Numerical floor: gaps below 1e-10 are treated as 0 (reducible /
    # non-mixing under float64 eigendecomposition of small Boolean TPMs).
    if gap < 1e-10:
        gap = 0.0
    return gap


def relaxation_time_from_gap(gap: float) -> float:
    """1 / spectral_gap; +inf when gap is 0."""
    if gap <= 0.0 or math.isnan(gap):
        return float("inf")
    return 1.0 / gap


def tv_mixing_bound(gap: float, delta: float = DEFAULT_TV_DELTA) -> float:
    """Crude spectral mixing bound ⌈ln(1/δ) / gap⌉; +inf when gap=0."""
    if gap <= 0.0 or math.isnan(gap):
        return float("inf")
    if delta <= 0.0 or delta >= 1.0:
        raise ValueError("delta must lie in (0, 1)")
    return math.ceil(math.log(1.0 / delta) / gap)


def summarize_mixing(
    form: Union[NextMap, Rules],
    *,
    eps_flip: float = DEFAULT_EPS_FLIP,
    tv_delta: float = DEFAULT_TV_DELTA,
    n: Optional[int] = None,
) -> MixingSummary:
    """Spectral gap and relaxation time of the flip-noise chain."""
    if eps_flip <= 0.0:
        raise ValueError("eps_flip must be > 0 for a mixing chain")
    nxt, _ = _resolve_form(form, n)
    P = noisy_transition_matrix(nxt, eps_flip)
    gap = spectral_gap(P)
    rel = relaxation_time_from_gap(gap)
    bound = tv_mixing_bound(gap, tv_delta)
    return MixingSummary(
        spectral_gap=gap,
        relaxation_time=rel,
        tv_mixing_bound=bound,
        eps_flip=eps_flip,
        tv_delta=tv_delta,
        n_states=len(nxt),
    )


def summarize_oscillation(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
) -> OscillationSummary:
    """Party-bit non-constancy and cycle variance on attractors.

    ``party_osc_frac`` is the fraction of (party-bit × attractor-cycle)
    cells where the bit takes more than one value on the cycle.
    ``mean_cycle_var`` is the mean of ``p(1-p)`` over the same cells,
    where ``p`` is the uniform mean of the bit on the cycle.
    ``mean_period`` is the ensemble-averaged cycle length (basin-mass
    weighted when ``ensemble`` is the full state space).
    """
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    part = attractor_partition(nxt)
    cycles = part["cycles"]
    n_parties = len(party_indices)
    n_cells = n_parties * len(cycles)
    n_osc = 0
    var_sum = 0.0
    if n_cells == 0:
        return OscillationSummary(
            party_osc_frac=float("nan"),
            mean_cycle_var=float("nan"),
            mean_period=float("nan"),
            max_period=0,
            n_attractors=0,
            n_party_bits=n_parties,
            n_oscillating_cells=0,
            n_cells=0,
        )
    for cyc in cycles:
        for idx in party_indices:
            vals = [float(st[idx]) for st in cyc]
            p = sum(vals) / float(len(vals))
            var_sum += p * (1.0 - p)
            if min(vals) != max(vals):
                n_osc += 1
    period_sum = 0.0
    for s in ens:
        period_sum += len(part["cycle_of_state"][s])
    mean_period = period_sum / float(len(ens)) if ens else float("nan")
    periods = [len(c) for c in cycles]
    return OscillationSummary(
        party_osc_frac=n_osc / float(n_cells),
        mean_cycle_var=var_sum / float(n_cells),
        mean_period=mean_period,
        max_period=max(periods) if periods else 0,
        n_attractors=len(cycles),
        n_party_bits=n_parties,
        n_oscillating_cells=n_osc,
        n_cells=n_cells,
    )


def summarize_pre_cycle_diversity(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
) -> PathDiversitySummary:
    """Mean pre-cycle party-tuple diversity over an ensemble of starts.

    For each start, walk the deterministic map until the first revisit
    (cycle entry). Collect party-bit tuples on states visited *strictly
    before* the cycle; count distinct tuples; scale by ``2^{n_parties}``.
    Starts already on a cycle contribute 0. The form-level covariate is
    the mean of those scaled counts.
    """
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    n_parties = len(party_indices)
    scale = 1 << n_parties if n_parties > 0 else 1
    distincts: list[int] = []
    transients: list[int] = []
    for start in ens:
        L = transient_length(nxt, start)
        transients.append(L)
        if L == 0:
            distincts.append(0)
            continue
        # Replay the transient path and collect party tuples.
        cur = start
        seen: set = set()
        party_set: set = set()
        for _ in range(L):
            if cur in seen:
                break
            seen.add(cur)
            party_set.add(tuple(int(cur[i]) for i in party_indices))
            cur = nxt[cur]
        distincts.append(len(party_set))
    if not ens:
        return PathDiversitySummary(
            pre_cycle_div=float("nan"),
            mean_distinct=float("nan"),
            mean_transient=float("nan"),
            n_starts=0,
            n_party_bits=n_parties,
            scale=scale,
        )
    mean_d = sum(distincts) / float(len(distincts))
    return PathDiversitySummary(
        pre_cycle_div=mean_d / float(scale),
        mean_distinct=mean_d,
        mean_transient=sum(transients) / float(len(transients)),
        n_starts=len(ens),
        n_party_bits=n_parties,
        scale=scale,
    )


# ---------------------------------------------------------------------------
# Cycle ordering (f). Frozen by studies/ergodic_cycle_ordering/hypotheses.md.
# No Φ. Prior settling summaries are unchanged.
# ---------------------------------------------------------------------------

# Denominator below this is treated as "ordering cannot move the remainder".
_ORDER_DENOM_EPS = 1e-15


@dataclass(frozen=True)
class CycleOrderingSummary:
    """Per-form cycle-ordering covariates at one horizon.

    ``pred_gap_cycle`` averages the on-cycle phase remainder over party
    bits and basins. ``remainder_allstarts`` averages ``|Ā_T − μ_cycle|``
    over every ensemble start, so transients are included and the
    reference is the cycle mean rather than the basin mean of time
    averages. The other fields are sequence features; see the module
    docstring.
    """

    pred_gap_cycle: float
    remainder_allstarts: float
    order_index: float
    order_excess: float
    cofilip_sync: float
    phase_lag: float
    lag1_autocorr: float
    hamming_party_rate: float
    dominant_signature: str
    n_attractors: int
    n_party_bits: int
    horizon: int
    n_starts: int

    def to_dict(self) -> dict:
        return asdict(self)


def circular_signed_remainder(
    values: Sequence[float], phase: int, horizon: int
) -> float:
    """Signed finite-T remainder ``Ā_T(phase) − μ`` on a circular sequence.

    ``r = horizon mod p``. The remainder is ``0`` when ``r = 0`` (an
    integer number of periods). Otherwise it is
    ``(Σ_{k<r} x_{phase+k} − r μ) / horizon``.
    """
    p = len(values)
    if p == 0 or horizon <= 0:
        return float("nan")
    mu = sum(values) / float(p)
    r = horizon % p
    if r == 0:
        return 0.0
    window = 0.0
    for k in range(r):
        window += values[(phase + k) % p]
    return (window - r * mu) / float(horizon)


def circular_mean_abs_remainder(values: Sequence[float], horizon: int) -> float:
    """Mean over phases of ``|Ā_T(phase) − μ|``."""
    p = len(values)
    if p == 0 or horizon <= 0:
        return float("nan")
    total = 0.0
    for phase in range(p):
        total += abs(circular_signed_remainder(values, phase, horizon))
    return total / float(p)


def most_spread_binary(period: int, weight: int) -> list:
    """Most evenly spaced circular placement of ``weight`` ones in ``period``.

    The ``k``-th one sits at ``(k * period) // weight`` for
    ``k = 0..weight-1``. Successive gaps differ by at most one. Rotating
    the placement does not change ``circular_mean_abs_remainder``.
    """
    if period <= 0:
        return []
    weight = max(0, min(period, int(weight)))
    seq = [0] * period
    if weight == 0:
        return seq
    for k in range(weight):
        seq[(k * period) // weight] = 1
    return seq


def most_clumped_binary(period: int, weight: int) -> list:
    """All ones consecutive: ``1`` * weight followed by ``0`` * (period − weight)."""
    if period <= 0:
        return []
    weight = max(0, min(period, int(weight)))
    return [1] * weight + [0] * (period - weight)


def _binary_weight(values: Sequence[float]) -> tuple:
    bits = [1 if float(v) >= 0.5 else 0 for v in values]
    return bits, sum(bits)


def order_components(values: Sequence[float], horizon: int) -> tuple:
    """Return ``(R_obs, R_spread, R_clump)`` for a party-bit cycle.

    ``R_*`` is ``circular_mean_abs_remainder`` at ``horizon``. The
    observed sequence is thresholded at 1/2 so the comparison is among
    binary placements of the same weight. Boolean party bits are already
    in ``{0,1}``.
    """
    bits, weight = _binary_weight(values)
    period = len(bits)
    if period == 0 or horizon <= 0:
        return float("nan"), float("nan"), float("nan")
    observed = circular_mean_abs_remainder(bits, horizon)
    spread = circular_mean_abs_remainder(most_spread_binary(period, weight), horizon)
    clump = circular_mean_abs_remainder(most_clumped_binary(period, weight), horizon)
    return observed, spread, clump


def order_index_of_sequence(values: Sequence[float], horizon: int) -> float:
    """``(R_obs − R_spread) / (R_clump − R_spread)``, or ``0`` if the
    denominator is numerically zero (ordering cannot move the remainder
    at this horizon: ``r ∈ {0}`` or the weight forces a unique necklace).
    """
    observed, spread, clump = order_components(values, horizon)
    if any(isinstance(v, float) and math.isnan(v) for v in (observed, spread, clump)):
        return float("nan")
    denom = clump - spread
    if abs(denom) <= _ORDER_DENOM_EPS:
        return 0.0
    return (observed - spread) / denom


def order_excess_of_sequence(values: Sequence[float], horizon: int) -> float:
    """``R_obs − R_spread`` in the same units as a finite-T gap."""
    observed, spread, _clump = order_components(values, horizon)
    if isinstance(observed, float) and math.isnan(observed):
        return float("nan")
    return observed - spread


def lag1_autocorr(values: Sequence[float]) -> Optional[float]:
    """Circular lag-1 autocorrelation, or ``None`` if the series is constant."""
    p = len(values)
    if p == 0:
        return None
    mu = sum(values) / float(p)
    dev = [v - mu for v in values]
    den = sum(d * d for d in dev)
    if den <= _ORDER_DENOM_EPS:
        return None
    num = sum(dev[t] * dev[(t + 1) % p] for t in range(p))
    return num / den


def cofilip_sync_of_cycle(cycle: Sequence[State], party_indices: Sequence[int]) -> float:
    """Share of party-bit flip steps on which at least two party bits flip.

    A step with no party-bit change is not a flip step. No flip steps ⇒ 0.
    A single party bit cannot co-flip, so the value is 0.
    """
    p = len(cycle)
    n_parties = len(party_indices)
    if p == 0 or n_parties == 0:
        return 0.0
    n_flip = 0
    n_sync = 0
    for t in range(p):
        cur = cycle[t]
        nxt_st = cycle[(t + 1) % p]
        delta = sum(1 for i in party_indices if cur[i] != nxt_st[i])
        if delta >= 1:
            n_flip += 1
        if delta >= 2:
            n_sync += 1
    if n_flip == 0:
        return 0.0
    return n_sync / float(n_flip)


def phase_lag_of_cycle(cycle: Sequence[State], party_indices: Sequence[int]) -> float:
    """Mean folded lag of pairwise party-bit circular cross-correlation.

    For each pair of non-constant party bits, ``ℓ*`` is the smallest lag
    in ``0..p-1`` maximizing ``Σ_t (x_t−μ)(y_{t+ℓ}−μ)``. The folded lag
    is ``min(ℓ*, p−ℓ*) / (p/2)`` ∈ ``[0, 1]`` (0 in phase, 1 anti-phase).
    Pairs with a constant bit are skipped. No eligible pair ⇒ 0.
    """
    p = len(cycle)
    if p < 2 or len(party_indices) < 2:
        return 0.0
    series = {
        idx: [float(st[idx]) for st in cycle] for idx in party_indices
    }
    lags: list[float] = []
    for a, ia in enumerate(party_indices):
        for ib in list(party_indices)[a + 1 :]:
            da = series[ia]
            db = series[ib]
            mua = sum(da) / float(p)
            mub = sum(db) / float(p)
            dev_a = [v - mua for v in da]
            dev_b = [v - mub for v in db]
            if (
                sum(v * v for v in dev_a) <= _ORDER_DENOM_EPS
                or sum(v * v for v in dev_b) <= _ORDER_DENOM_EPS
            ):
                continue
            best_l = 0
            best_c = None
            for ell in range(p):
                corr = sum(dev_a[t] * dev_b[(t + ell) % p] for t in range(p))
                # Strict ``>`` keeps the smallest lag on a tie.
                if best_c is None or corr > best_c + 1e-15:
                    best_c = corr
                    best_l = ell
            lags.append(min(best_l, p - best_l) / (p / 2.0))
    if not lags:
        return 0.0
    return sum(lags) / float(len(lags))


def hamming_party_rate_of_cycle(
    cycle: Sequence[State], party_indices: Sequence[int]
) -> float:
    """Mean per-step party-bit Hamming distance, divided by ``n_parties``.

    Lies in ``[0, 1]``. Zero when no party bit changes around the cycle.
    """
    p = len(cycle)
    n_parties = len(party_indices)
    if p == 0 or n_parties == 0:
        return 0.0
    total = 0
    for t in range(p):
        cur = cycle[t]
        nxt_st = cycle[(t + 1) % p]
        total += sum(1 for i in party_indices if cur[i] != nxt_st[i])
    return (total / float(p)) / float(n_parties)


def flip_signature(cycle: Sequence[State], party_indices: Sequence[int]) -> str:
    """Canonical circular signature of which party bits flip at each step.

    Each step is a mask of ``0``/``1`` over ``party_indices`` (1 = that
    bit changes). The string is the lexicographically minimal rotation,
    masks joined by ``-``. Empty cycle ⇒ empty string.
    """
    p = len(cycle)
    if p == 0:
        return ""
    masks = []
    for t in range(p):
        cur = cycle[t]
        nxt_st = cycle[(t + 1) % p]
        masks.append(
            "".join("1" if cur[i] != nxt_st[i] else "0" for i in party_indices)
        )
    rotations = [tuple(masks[i:] + masks[:i]) for i in range(p)]
    best = min(rotations)
    return "-".join(best)


def finite_T_time_average(
    nxt: NextMap,
    start: State,
    observable: Observable,
    horizon: int,
) -> float:
    """Exact time average of the first ``horizon`` states on the deterministic map.

    Walks until the cycle is identified (a finite total map always cycles),
    then uses the closed form: transient sum plus ``q`` full periods and a
    residual window on the cycle. This is not a Monte Carlo estimate. It
    is the quantity ``trajectory_time_average`` computes at ``noise=0``.
    """
    if horizon <= 0:
        return float("nan")
    cur = start
    seen: dict[State, int] = {}
    path: list[State] = []
    # A total finite map repeats by step len(nxt). Guard one extra step.
    limit = len(nxt) + 1
    while cur not in seen and len(path) <= limit:
        seen[cur] = len(path)
        path.append(cur)
        cur = nxt[cur]
    if cur not in seen:
        series = path[:horizon]
        if not series:
            return 0.0
        return sum(observable(st) for st in series) / float(len(series))
    transient_len = seen[cur]
    if horizon <= transient_len:
        return sum(observable(path[i]) for i in range(horizon)) / float(horizon)
    cycle_states = path[transient_len:]
    period = len(cycle_states)
    trans_sum = sum(observable(path[i]) for i in range(transient_len))
    cycle_vals = [observable(st) for st in cycle_states]
    steps = horizon - transient_len
    q, r = divmod(steps, period)
    cyc_sum = q * sum(cycle_vals) + sum(cycle_vals[k] for k in range(r))
    return (trans_sum + cyc_sum) / float(horizon)


def _empty_ordering(n_parties: int, horizon: int, n_starts: int, n_attractors: int):
    return CycleOrderingSummary(
        pred_gap_cycle=float("nan"),
        remainder_allstarts=float("nan"),
        order_index=float("nan"),
        order_excess=float("nan"),
        cofilip_sync=float("nan"),
        phase_lag=float("nan"),
        lag1_autocorr=float("nan"),
        hamming_party_rate=float("nan"),
        dominant_signature="",
        n_attractors=n_attractors,
        n_party_bits=n_parties,
        horizon=horizon,
        n_starts=n_starts,
    )


def summarize_cycle_ordering(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    horizon: int,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
) -> CycleOrderingSummary:
    """Basin-mass-weighted cycle-ordering summary at one horizon.

    Weights are ensemble counts per basin divided by the number of
    starts (the full state space when ``ensemble`` is omitted). Within
    a cycle, phase averages are uniform on the cycle states. Party bits
    are averaged with equal weight. Constant bits contribute ``0`` to
    ``order_index``, ``order_excess``, and ``lag1_autocorr``.
    ``dominant_signature`` is the flip signature of the heaviest basin
    (lowest cycle index breaks a tie).
    """
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    part = attractor_partition(nxt)
    cycles = part["cycles"]
    n_parties = len(party_indices)
    if not ens or n_parties == 0 or not cycles or horizon <= 0:
        return _empty_ordering(n_parties, horizon, len(ens), len(cycles))

    mass = [0] * len(cycles)
    for st in ens:
        mass[part["basin_of"][st]] += 1
    total = float(len(ens))

    pred_acc = 0.0
    order_acc = 0.0
    excess_acc = 0.0
    sync_acc = 0.0
    lag_acc = 0.0
    ac_acc = 0.0
    ham_acc = 0.0
    dom = max(range(len(cycles)), key=lambda i: (mass[i], -i))

    for i, cyc in enumerate(cycles):
        weight = mass[i] / total
        bit_pred = []
        bit_order = []
        bit_excess = []
        bit_ac = []
        for idx in party_indices:
            vals = [float(st[idx]) for st in cyc]
            bit_pred.append(circular_mean_abs_remainder(vals, horizon))
            bit_order.append(order_index_of_sequence(vals, horizon))
            bit_excess.append(order_excess_of_sequence(vals, horizon))
            ac = lag1_autocorr(vals)
            bit_ac.append(0.0 if ac is None else ac)
        pred_acc += weight * (sum(bit_pred) / float(n_parties))
        order_acc += weight * (sum(bit_order) / float(n_parties))
        excess_acc += weight * (sum(bit_excess) / float(n_parties))
        ac_acc += weight * (sum(bit_ac) / float(n_parties))
        sync_acc += weight * cofilip_sync_of_cycle(cyc, party_indices)
        lag_acc += weight * phase_lag_of_cycle(cyc, party_indices)
        ham_acc += weight * hamming_party_rate_of_cycle(cyc, party_indices)

    # All-start remainder versus the cycle mean (transients included).
    rem_acc = 0.0
    n_cells = 0
    for idx in party_indices:
        obs = bit_observable(idx)
        cyc_mu = {
            i: cycle_mean(obs, cyc) for i, cyc in enumerate(cycles)
        }
        for st in ens:
            mu = cyc_mu[part["basin_of"][st]]
            avg = finite_T_time_average(nxt, st, obs, horizon)
            rem_acc += abs(avg - mu)
            n_cells += 1
    remainder_allstarts = rem_acc / float(n_cells) if n_cells else float("nan")

    return CycleOrderingSummary(
        pred_gap_cycle=pred_acc,
        remainder_allstarts=remainder_allstarts,
        order_index=order_acc,
        order_excess=excess_acc,
        cofilip_sync=sync_acc,
        phase_lag=lag_acc,
        lag1_autocorr=ac_acc,
        hamming_party_rate=ham_acc,
        dominant_signature=flip_signature(cycles[dom], party_indices),
        n_attractors=len(cycles),
        n_party_bits=n_parties,
        horizon=horizon,
        n_starts=len(ens),
    )


def exact_basin_gap(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    horizon: int,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
) -> float:
    """Closed-form basin-mode gap: mean ``|Ā_T − basin mean of Ā_T|``.

    The basin reference is the mean of the closed-form time averages over
    ensemble starts in the same zero-noise basin, pooled equally over
    party bits. At ``noise=0`` this is the basin-mode ``gap_mean`` from
    ``run_eoa_parties``.
    """
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    if not ens or not party_indices or horizon <= 0:
        return float("nan")
    part = attractor_partition(nxt)
    gaps: list[float] = []
    for idx in party_indices:
        obs = bit_observable(idx)
        avgs = [finite_T_time_average(nxt, st, obs, horizon) for st in ens]
        buckets: dict[int, list[float]] = {}
        bids = []
        for st, avg in zip(ens, avgs):
            bid = part["basin_of"][st]
            bids.append(bid)
            buckets.setdefault(bid, []).append(avg)
        refs = {bid: sum(vs) / float(len(vs)) for bid, vs in buckets.items()}
        for avg, bid in zip(avgs, bids):
            gaps.append(abs(avg - refs[bid]))
    return sum(gaps) / float(len(gaps))


# ---------------------------------------------------------------------------
# Known-answer control maps (no Φ; unit-test fixtures)
# ---------------------------------------------------------------------------

def control_chain_to_fixed() -> NextMap:
    """3-bit map: Gray-like drain into the fixed point 000.

    Explicit next-map (not maj3): every nonzero state flips its lowest
    set bit off, so the unique attractor is {(0,0,0)} and transient
    lengths are exactly the Hamming weights::

        000 → 000  (transient 0)
        100 → 000  (1)
        010 → 000  (1)
        001 → 000  (1)
        110 → 010 → 000  (2)
        101 → 001 → 000  (2)
        011 → 001 → 000  (2)
        111 → 011 → 001 → 000  (3)

    Mean transient over the uniform ensemble = (0+1+1+1+2+2+2+3)/8 = 1.5.
    """
    nxt: NextMap = {}
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        bits = list(cur)
        for i in range(3):
            if bits[i] == 1:
                bits[i] = 0
                break
        nxt[cur] = tuple(bits)
    return nxt


def control_two_step_cycle() -> NextMap:
    """Unique 2-cycle (000 ↔ 100); all other states drain in one step.

    Transient lengths: 0 on the cycle, 1 elsewhere. Period = 2.
    """
    nxt: NextMap = {
        (0, 0, 0): (1, 0, 0),
        (1, 0, 0): (0, 0, 0),
    }
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        if cur in nxt:
            continue
        # Drain toward 000.
        nxt[cur] = (0, 0, 0)
    return nxt
