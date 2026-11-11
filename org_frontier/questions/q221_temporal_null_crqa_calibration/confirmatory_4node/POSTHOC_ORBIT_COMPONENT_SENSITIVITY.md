# Post-hoc orbit-component sensitivity for the 600-pair follow-up

**Exploratory design sensitivity only, 2026-10-15. Not a prospective hypothesis, valid replacement confidence interval, or change to preregistered decisions.**

## Why perform this check?

The registered follow-up draws 600 unique **unordered orbit pairs** without replacement from a finite population of 1,832. It does *not* draw 1,200 independent network orbits: 782 distinct orbits appear in the 600 edges, 413 selected edges share an orbit with at least one other edge, and a sampled orbit appears in up to seven edges. Every edge gets separate, disjoint trajectory seeds. The protocol's Wilson analysis targets a **finite orbit-pair population**; repeated orbit participation does not invalidate the identity of the sampled edge unit.

This separate calculation deliberately tests a *different*, more ambitious interpretation: how stable would the observed fraction separated look if one treated **connected components of the sampled orbit-pair graph** as the resampling units? Such components are nonoverlapping in orbit identities, but are constructed from the **observed** graph rather than randomly sampled as population clusters. The resulting ranges are only an exploratory fragility diagnostic, **not** calibrated design-based confidence intervals.

## Independent calculation

Source: original 600 pair identities in `results/followup_pairs.json` and binary method decisions in `results/followup.json`. Union-find over orbit endpoints yields **279 observed connected components**, of which **187 are single-edge components**; the largest contains **34 sampled edges**. The component sizes are nonuniform.

With a frozen 32-bit xorshift seed 22155013, sample 279 observed components **with replacement** in each of 12,000 replicates. For each replicate, calculate the number of successful edges divided by the total edges in the resampled components. Values below are empirical 2.5th/50th/97.5th percentiles, rounded to three decimals:

| Metric | Original registered fraction | Post-hoc component-resample 95% percentile range |
|---|---:|---:|
| C2 joint recurrence | 347/600 = 0.578 | **[0.493, 0.662]** |
| C4 SHREC | 363/600 = 0.605 | **[0.545, 0.666]** |
| SHREC minus joint recurrence | +0.027 | **[−0.061, +0.119]** |

The corresponding published Bonferroni-Wilson intervals under the registered finite-pair analysis are [0.533,0.623] for joint recurrence and [0.560,0.649] for SHREC. The exploratory component resampling is wider, particularly for C2, because it probes between-orbit structural clustering with a different sampling model.

As a separate deterministic leave-one-component-out stress test, the smallest observed separation fraction is **0.553** for C2 and **0.597** for C4. These are point-estimate perturbations, not intervals.

## Interpretation

- The **registered finite-population orbit-pair estimand and its frozen inference rule remain unchanged.** The two registered `generally separates` labels stand *under that protocol*. This note does not claim the Wilson CI is invalid or that an alternative test replaces it.
- The graph-component sensitivity shows that **transporting the C2 conclusion to a hypothetical independent-network-orbit superpopulation would require additional justification**. Under one conservative, *post-hoc and non-design-based* resampling diagnostic, C2's lower percentile crosses 0.5; C4's does not. Neither range is a calibrated CI for that superpopulation.
- The observed paired difference between SHREC and JR is small and uncertain; see `POSTHOC_PAIRED_METHOD_AUDIT.md`. This audit does **not** establish SHREC superiority.
- Orbit pairs may share structural properties even without shared orbit endpoints; the component partition is not a full dependence model. Conversely, the original simple random sample **without replacement** and separate trajectory streams matter; it is not appropriate to relabel these 600 pairs simply as 279 independent trials.

## Reproduce

Run, from repo root:

`python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.orbit_overlap_sensitivity`

The script reads the two unchanged original JSON receipts and uses a fixed xorshift32 PRNG with 12,000 component resamples. It does not import PyPhi, SHREC, or rerun any expensive simulations. Neither preregistration, recorded results, nor primary decision rules are modified.

**Scientific disposition:** Retain the original finite orbit-pair conclusions under their prespecified rules, but qualify any generalized interpretation that implicitly treats the 600 orbit pairs as independent *network forms*.
