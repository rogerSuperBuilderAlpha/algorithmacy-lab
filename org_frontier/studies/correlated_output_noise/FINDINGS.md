# Correlated output noise — findings

**Verdict: CORE_SHIFT_NO_FLIP.** True correlated party-output noise
(a shared-coin SBS TPM that is not conditionally independent) does
**not** flip the dyadic/triadic verdict where #61's static shared input
did not. Exact IIT-4.0 Φ cannot see the correlation: PyPhi's CI
projection of the shared-coin SBS is identical to independent
dual-party flip-noise, and that projection decays smoothly (Φ
2.0→0, max step **3.4%** of total fall) with first dyadic only at
p=0.5. One interior grid point (p=0.40) dips to n_core=2 while staying
triadic — a core shift without verdict flip, against #61's fixed
n_core=3 at Φ=2.

In-silico; exact IIT-4.0; conjunctive mediated triad n=3 (W,S,C);
shared-coin SBS on (W′,C′); 51-point grid. Hypotheses fixed in
`hypotheses.md`. Cited: #61; `commit_noise_phase/` (#6); 
`party_vs_mediator_noise/` (#7). #6–#11 pointers only.
Estimation / construct / omit / ladder closed.

## Witnesses (correlation is real; Φ sees only the projection)

| p | CI? | max\|SBS−roundtrip\| | max\|joint−product\| | max\|proj−indep_WC\| |
|---:|---|---:|---:|---:|
| 0.00 | yes | 0 | 0 | 0 |
| 0.10 | no | 0.090 | 0.090 | 0 |
| 0.25 | no | 0.188 | 0.188 | 0 |
| 0.50 | no | 0.250 | 0.250 | 0 |

## Φ / verdict / n_core (CI projection vs node baselines)

| p | Φ_proj (=indep WC) | struct | n_core | Φ_med | Φ_W |
|---:|---:|---|---:|---:|---:|
| 0.00 | 2.000 | tri | 3 | 2.000 | 2.000 |
| 0.10 | 1.374 | tri | 3 | 1.189 | 0.763 |
| 0.25 | 0.658 | tri | 3 | 0.500 | 0.439 |
| 0.40 | 0.189 | tri | **2** | 0.138 | 0.158 |
| 0.49 | 0.015 | tri | 3 | 0.011 | 0.015 |
| 0.50 | 0 | dyadic | 0 | 0 | 0 |

## vs #61 (static shared input)

| form | whole | major complex |
|---|---|---|
| no_shock | dyadic Φ=0 | {W,S,C} Φ=2.0 |
| shared_shock | dyadic Φ=0 | {W,S,C} Φ=2.0 |
| shock_in_commit | dyadic Φ=0 | {W,S,C} Φ=2.0 |

Static shared input never moves the core verdict. Correlated *output*
SBS is non-CI, but the Φ-visible object matches independent dual-party
node noise and also leaves the verdict unflipped below p=0.5.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 interior verdict flip vs #61/node | **REFUTED** |
| H2 same smooth decay / Φ≡indep_WC | **SUPPORTED** |
| H3 core shift without verdict flip | **SUPPORTED** (p=0.40 only) |

## Reading

#61's modeling flag is confirmed as an instrument limit, not as a
hidden verdict flip. A shared-coin SBS really is non-factorable
(residual up to 0.25), and exact binary IIT-4.0 Φ — which assumes
conditional independence — evaluates only the CI envelope of that TPM.
That envelope is independent dual-party flip-noise: same smooth decay
as #6/#7, same p*=0.5 endpoint, plus a one-point core dip. The
correlation beyond the envelope does not enter the Φ verdict.
Designed witnesses: non-CI residual; proj≡indep identity; #61 core
unchanged; projection sweep.

## Limits

n=3; one shared-coin parameterization; Φ on the CI projection only
(IIT-4.0/PyPhi cannot retain non-CI structure). No organization
measured.

## Best next experiment

Done: #13 **GENUINE_COEXISTENCE** (`genuine_bistability/`). Prefer
agenda **#12** (continuous-time / stoch-temporal synthesis) or **#14**
(adaptive mediator). Do not reopen estimation / construct / omit /
ladder.

## Reproduce

```
python org_frontier/studies/correlated_output_noise/analyze_correlated.py
```
(~30 s)
