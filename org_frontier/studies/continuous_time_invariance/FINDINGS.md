# Continuous-time grain/schedule invariance — findings

**Verdict: STILL_DEPENDENT.** A defensible CTMC→expm(Q·Δt) embedding
softens #112’s discrete wipeout but does **not** restore a
modeling-free invariant. On the 24 canonically triadic corpus forms:
equal-rate and slow-mediator schedules keep **72/72** cells triadic
across Δt∈{0.1,1,5}; extreme rate asymmetry (`seq_like=(100,10,1)`)
flips **8/24** forms at Δt∈{1,5} (16 cells). Overall **200/216**
(92.6%) CT cells stay triadic — vs discrete grain-2 and sequential at
**0/24**. Native continuous-time IIT-4.0 Φ remains **unavailable** on
the PyPhi pin; Φ here is exact discrete IIT-4.0 on the CI projection of
the embedded TPM (non-CI residual up to ~0.24).

In-silico; candid N (n=3; 24 #112 forms; 3 Δt × 3 schedules).
Hypotheses fixed in `hypotheses.md`. Cited: #112;
`STOCH_TEMPORAL_ARC.md`. Estimation / construct / omit / ladder closed.

## vs #112 (discrete)

| condition | triadic |
|---|---|
| grain-1 sync | **24/24** |
| grain-2 sync | **0/24** |
| sequential | **0/24** |
| majority | **0/24** |

## CT embedding aggregates

| slice | triadic cells |
|---|---|
| all CT cells | **200/216** (92.6%) |
| schedule `equal` | 72/72 |
| schedule `slow_S` | 72/72 |
| schedule `seq_like` | 56/72 |
| Δt=0.1 (all schedules) | 72/72 |
| forms flipped on any cell | **8/24** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 CT restores invariance | **REFUTED** |
| H2 still schedule/grain dependent | **SUPPORTED** |
| H3 NOT_TESTABLE (no runnable path) | **REFUTED** (proxy ran; native CT Φ still absent) |

## Reading

Continuous time does not dissolve #112’s lesson. Under equal rates the
embedding is grain-robust on this panel; under a strong rate ordering
that mimics sequential priority, coarse observation grains still call
some triadic forms dyadic. The instrument gap remains for *native*
continuous-time Φ — PyPhi only sees discrete TPMs — so the claim is
about CT-generated dynamics under discrete IIT-4.0 observation, not a
new continuous Φ calculus. Designed witnesses: #112 reaffirm; equal vs
`seq_like` split; non-CI embedding residual.

## Limits

Async competing-clock CTMC only; CI-projected Φ; n=3 corpus; three
schedules. No organization measured.

## Best next experiment

**Lane closable.** Discrete + CT-proxy stoch–temporal arc is complete
(`STOCH_TEMPORAL_ARC.md`). Prefer agenda **#15+** (topology /
hierarchy) or empirical/survey packets. Do not reopen estimation /
construct / omit / ladder unless a native continuous-time IIT pin
lands.

## Reproduce

```
python org_frontier/studies/continuous_time_invariance/analyze_ct.py
```
(~30 s)
