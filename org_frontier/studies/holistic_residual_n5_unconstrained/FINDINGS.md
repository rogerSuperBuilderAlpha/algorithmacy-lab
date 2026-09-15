# Unconstrained n=5 holistic residual — findings

**Verdict: H0 — the residual holds near the n=4 unc rate.** On N=500 unconstrained k=2 n=5
forms (seed 50), Probe-131 RF miss rate = **9.0% (45/500)**, inside the pre-registered hold band
[5.5%, 9.5%] relative to n=4's 7.5% (+1.5 pp). The forest predicts both classes (H3 supported).

In-silico; exact IIT-4.0 Φ. Hypotheses fixed in `hypotheses.md` before computing. F26 SM 2.4% is
not a size-trend baseline. F27 not reopened.

## Size series (unconstrained k=2 / Probe 131)

| | n=3 Probe 131 | n=4 unc k=2 | **n=5 unc k=2** |
|---|---|---|---|
| N | 4096 (exhaustive) | 1000 seed 40 | **500 seed 50** |
| triadic rate | 55.9% | 29.7% | **17.0% (85)** |
| RF miss rate | **4.8%** | **7.5%** | **9.0% (45)** |
| majority-class miss | — | 29.7% | 17.0% |
| predicted tri / dya | — | 312 / 688 | **88 / 412** |
| FP / FN | — | 45 / 30 | **24 / 21** |
| miss among tri / dya | — | 10.1% / 6.4% | **24.7% / 5.8%** |
| near-boundary among misses | 0.91 | 0.56 | **0.51** |
| band vs prior | — | H2 grows vs n=3 | **H0 holds vs n=4** |

Trend in one line: **4.8% → 7.5% → 9.0%** — a step up from n=3 to n=4, then flat within ±2 pp at n=5.

## Scope and compute

N=500 was chosen after a 30-form pilot (mean ~0.55 s/form; max ~7 s). Full panel build took
**~700 s (~12 min)** on this host. Larger N is feasible but was not required for the band test;
binomial SE at rate 0.09 with N=500 is ~1.3 pp, so the hold band (±2 pp) is resolvable. Triadic
rate fell again (29.7% → 17.0%) but stayed high enough for both-class prediction — unlike F26 SM.

## Reading

Once base rate is controlled, the cheap-feature ceiling does not keep climbing without bound from
n=4 to n=5: it sits near 9%, statistically compatible with the n=4 7.5% under the pre-registered
band. Errors remain two-sided. Miss rate among triadic forms rises (24.7% vs 10.1% at n=4), so the
residual at n=5 is more a failure to recover rarer triads than a dyadic false-positive problem.

## Best next experiment

**F28 on n=4 unc misses** is in `org_frontier/studies/residual_phase_boundary_unc/` (phase boundary
vs far-hit; not residual-specific). Next: **surrogate/feature redesign** for the triadic FN tail.

## Reproduce

```
python org_frontier/studies/holistic_residual_n5_unconstrained/analyze_unconstrained_n5.py
python org_frontier/studies/holistic_residual_n5_unconstrained/analyze_unconstrained_n5.py --rebuild
```
