# Commit-noise phase transition — findings

**Verdict: SMOOTH_DECAY.** Probabilistic commit flip-noise drives Φ
down as a monotone glide on both the conjunctive hub (Φ 2.0→0) and the
parity hub (Φ 0.5→0). No interior phase transition: verdict stays
triadic through p=0.49 and flips dyadic only at the coin-flip endpoint
p=0.5. Major complex stays the full triad until that endpoint. Max
single-step Φ drop is **5.0%** (conjunctive) / **2.4%** (parity) of
total fall — under the 25% H1 bar.

In-silico; exact IIT-4.0; N=2 designed n=3 forms × 51-point grid
p=0.00…0.50. Noise: `P(out=1)=(1−p)·clean+p·(1−clean)` on the hub
column. Hypotheses fixed in `hypotheses.md`. Cited: #27, #38;
`questions/q6_noise_phase_transition/` (prior fine grid, same
reading). Estimation / construct / omit / ladder closed.

## Φ / verdict / n_core (selected p)

| family | p=0 | p=0.25 | p=0.49 | p=0.5 |
|---|---|---|---|---|
| conjunctive_hub | Φ=2.000 tri n_core=3 | 0.500 tri 3 | 0.011 tri 3 | 0 dyadic 0 |
| parity_hub | Φ=0.500 tri n_core=3 | 0.219 tri 3 | 0.007 tri 3 | 0 dyadic 0 |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 sharp phase (interior verdict or ≥25% Φ step) | **REFUTED** |
| H2 only smooth decay (both families) | **SUPPORTED** |
| H3 interior core/Φ decoupling | **REFUTED** |

## Reading

The coarse reliability sweeps (#27, #38) were not hiding a kink. Fine
sampling reproduces a smooth magnitude decay; the only sharp object is
the binary verdict at the degenerate endpoint. The small-Φ parity hub
is as verdict-robust as the conjunctive hub — robustness is a property
of the verdict, not of clean Φ size. Designed witnesses: both hubs at
n=3 under hub-column flip-noise.

## Limits

n=3 only; two hub families; state-by-node flip-noise (not correlated
state-by-state TPM — that is agenda #5). No organization measured.

## Best next experiment

Within stochastic/temporal (#5–#14): prefer agenda **#7** (party vs
mediator noise thresholds) — same noise model, different seat. Alternate
**#5** (correlated TPM noise the state-by-node form cannot express).
Do not reopen estimation / construct / omit / ladder.

## Reproduce

```
python org_frontier/studies/commit_noise_phase/analyze_phase.py
```
(~16 s)
