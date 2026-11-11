# Post-hoc finite-population inference robustness for the JR/SHREC follow-up

**Status: after outcomes were available, 2026-10-15. NOT a new preregistered hypothesis, interval, or replacement for the registered Wilson verdicts.** Source: the 600 distinct orbit-pair identities in results/followup_pairs.json and binary per-pair separation decisions in results/followup.json. See independent_audit/finite_population_tail_bound.py.

## Inferential question

The preregistration drew n=600 unordered orbit pairs uniformly **without replacement** from a finite population of N=1,832 remaining eligible pairs. Pair-specific classification uses independently seeded trajectories for each pair, even if the same underlying *network orbit* appears in two different orbit pairs. The inferential object is the average probability of a separation event across these N **pair identities**, not the fraction of distinct networks which would be separated by a model.

Let theta_i in [0,1] be the probability that the registered train/test classification procedure declares separation for orbit pair i when given its own independently generated trajectories. The null is finite-population mean mu=(1/N) sum_i theta_i <= 1/2. The observed Y_r is a Bernoulli separation indicator after one orbit pair is selected by simple random sampling without replacement, with independent pair-index-specific simulation randomness conditional on the selected pair identities.

## Conservative tail inequality (valid under the stated design)

For t>0 let a_i=E[exp(t Y_i) | pair i]=1+theta_i (exp(t)-1). Because sample indices are drawn without replacement, the moment-generating function of S=sum_r Y_r is the normalized elementary symmetric polynomial of degree n in the positive numbers a_i. Maclaurin's inequality gives

    E[exp(t S)] <= ((1/N) sum_i a_i)^n
                = (1 + mu(exp(t)-1))^n
                <= ((1+exp(t))/2)^n  under H0: mu <= 1/2.

Chernoff optimization therefore yields, for observed k/n > 1/2,

    Pr_H0(S >= k) <= exp(-n * D(k/n || 1/2)),

where D(p||q)=p ln(p/q)+(1-p) ln((1-p)/(1-q)) is Bernoulli KL divergence. No assumption that all theta_i are identical is needed. The finite-population, without-replacement sampling and the independently generated trajectory draws are the key conditions. The inequality is conservative; it is not a confidence interval and is not a test of SHREC versus JR superiority.

## Independent recalculation from recorded decisions

| Registered comparator | Recorded separated pairs | Fraction | One-sided upper tail probability | Bonferroni bound over 2 |
|---|---:|---:|---:|---:|
| C2 joint recurrence | 347/600 | 0.578333 | <= 0.000615083 | <= 0.00123017 |
| C4 SHREC | 363/600 | 0.605000 | <= 0.00000162664 | <= 0.00000325327 |

These bounds are **post-hoc robustness checks** under a specified finite-pair-population estimand. They do not alter the registered Bonferroni-Wilson analyses: both remain labelled `generally separates` under their frozen rule. No claim of generalization to independently sampled network-orbit *superpopulations*, new network families, or real-world systems is implied.

## How this relates to the component resampling sensitivity

POSTHOC_ORBIT_COMPONENT_SENSITIVITY.md resamples connected components of the observed graph to explore a **different**, more ambitious superpopulation notion of dependence among network orbits. Its wide JR interval is not a calibrated estimate for the registered finite population of orbit pairs. The concentration inequality above is justified for that registered finite pair population under simple random sampling without replacement plus independent simulations; it does not resolve or dismiss the superpopulation limitation.

## Reproduction

Run `python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.finite_population_tail_bound`. The script validates the 600 distinct selected pair IDs, chronological row alignment, 400 test trajectories per pair, primary verdict counts, and prints the conservative bounds. It uses only the Python standard library and unchanged raw receipts. The original preregistration, outcomes, and verdicts are untouched.
