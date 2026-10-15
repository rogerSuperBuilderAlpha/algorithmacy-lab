# Independent null-calibration and finite-sample audit (provisional)

**Status:** Exploratory research note; not preregistered, not confirmatory. No IIT-specific structural-identifiability result is claimed.

## Scope and division of work

This note covers statistical calibration and finite-sample interpretation only. The separate exact-Φ gate and bounded Boolean-rule search are owned by the parallel q221 investigation. Do not overwrite its results or treat the present note as a substitute.

## Null-calibration pilot

The candidate pilot generates two **independent**, stationary binary Markov channels, each with probability `p` of retaining its previous value. It compares an absolute zero-lag Pearson-correlation statistic against (a) independently permuted time indices and (b) relative circular shifts. Candidate persistence levels: 0.50, 0.90, 0.98. Repeated independently generated *pairs*, not surrogate draws, are the units used to estimate empirical rejection rates.

The null of cross-channel independence is true by construction. Naive shuffling destroys within-channel serial dependence and is not generally exchangeable under this null. Circular shifts preserve each realized sequence's internal cyclic structure but **do not automatically guarantee** calibrated inference, especially under periodicity, nonstationarity, finite-sample dependence, or inappropriate shift selection.

A previous exploratory local pilot reported strongly elevated naive-shuffle rejection rates at high persistence. Those reported percentages must **not** be imported as verified q221 results until the exact original code, seeds, degeneracy handling, and raw outcomes are committed and independently reproduced.

### Minimum reproduction requirements

1. Freeze the RNG algorithm and seed, series length, burn-in, number of independent pairs, surrogate count, test statistic, and tail.
2. Define constant-series handling *before* execution; report its frequency and sensitivity to alternative handling. Replacing undefined Pearson correlations with zero changes the statistic and requires justification.
3. Use finite Monte Carlo p-values `(1 + count(T_surrogate >= T_observed))/(B + 1)` only when the underlying randomization is valid for the stated null.
4. Report numerator and denominator of every false-positive rate, uncertainty intervals across independent pairs, and a nominal 5% reference.
5. Distinguish Monte Carlo p-value resolution from independent replication.
6. Include negative controls, periodic processes, and at least one nonstationary regime before interpreting circular shifts as a broadly valid solution.

## Finite-sample cross-recurrence issue

The earlier fully observed A/B Boolean construction has matching **population mean cross-channel categorical lag profiles** under its stationary assumptions, but different higher-order dynamics and self-recurrence. The lab's q220 bottleneck centrality excludes diagonal/self-channel recurrence directly. Nevertheless, self-dynamics affect the sampling distribution of estimated off-diagonal peak prominences, threshold crossings, and centrality.

Thus:

- Equal population mean profiles **do not** imply equal finite-sample feature distributions.
- Equal mean profiles **do not** imply that a classifier based on finite-sample prominences is incapable of discriminating the systems.
- A within-trajectory classifier score is not evidence of generalization to unseen Boolean network forms.
- The higher-order XOR diagnostic was constructed with prior knowledge of the generating mechanism; it is a positive control, not an unbiased generic competitor.
- The parallel exact-Φ investigation reports that the original A/B pair has degenerate IIT bottleneck targets. It must **not** be presented as an IIT-specific counterexample.

### Proposed next audit

Use the repository's actual `org_frontier/questions/q220_observation_process_robustness/stage2/observe.py` functions `coupling`, `centrality`, and `bottleneck_scores` to reproduce finite-sample outcomes. Match `STEPS=600`, `WARMUP=20`, `FLIP=0.08`, `MAX_LAG=10`, `PROM_FLOOR=0.05`, and the applicable minimum-pair convention. Report the distribution of per-run peak prominence, maximum centrality, no-evidence calls, and within-channel diagnostics **separately**. Avoid tuning the threshold to maximize A/B discrimination.

## Adversarial interpretation

The strongest presently defensible claim is **representation insufficiency**: population mean pairwise categorical cross-recurrence profiles need not identify the complete multivariate transition law. It is not yet an IIT bottleneck-identifiability theorem, an exact-Φ difference, or an assertion that the q220 finite-sample decoder fails.

For a future confirmatory study, distinguish (1) null calibration, (2) predictive information about the exact IIT target, and (3) causal/structural identification. Use independently generated network forms as units for out-of-form generalization, with prespecified selection and exclusion rules.

## Relevant prior art for targeted verification

- Theiler et al. (1992), *Testing for nonlinearity in time series: The method of surrogate data*, DOI 10.1016/0167-2789(92)90102-S.
- Schreiber & Schmitz (2000), *Surrogate time series*, DOI 10.1016/S0167-2789(00)00043-9.
- Politis & Romano (1994), *The stationary bootstrap*, DOI 10.1080/01621459.1994.10476870.
- Marwan (2011), *How to avoid potential pitfalls in recurrence plot based data analysis*, DOI 10.1142/S0218127411029008.
- Phipson & Smyth (2010), *Permutation P-values should never be zero*, DOI 10.2202/1544-6115.1585.

These are literature leads, not a completed novelty review. Check original methods, assumptions, and source-to-claim alignment before treating them as authoritative support.

## Gate

**GO** for independently reproducible methods checks. **NO-GO** for a confirmatory claim, new IIT-specific result, or merge based on this note alone.
