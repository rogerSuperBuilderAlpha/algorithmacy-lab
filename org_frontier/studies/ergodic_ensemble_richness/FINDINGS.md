# ergodic_ensemble_richness — findings

**Verdict: NO_ENSEMBLE_LINK.** On the complete 256-form strict-mediation
census at n=3, Spearman ρ(Φ_MIP, basin entropy) = **0.1015** (positive
one-sided permutation p = **0.0510**) and ρ(Φ_MIP, component count) =
**0.1286** (p = **0.0185**). Both sit under the pre-registered margin
|ρ| ≥ 0.20, so H1 and H2 are refuted. The primary word follows that pair.

Secondary witnesses: mean basin entropy is higher for the 24 triadic forms
(**0.4685**) than for the 232 dyadic forms (**0.2521**), a gap of
**0.2164** bits, so H3 is supported at δ_h = 0.1. Mean component count
differs by **0.3218** (1.6667 vs 1.3448), under δ_c = 0.5, so H4 is
refuted. H5 prints SUPPORTED because the two enumeration halves share a
sign and |ρ| = 0.1015 ≥ 0.10. Those halves are the same multiset of
(Φ, entropy, count, verdict) rows, so the equal coefficient is an identity
of `enumerate_family`'s order. H5 does not supply a second sample.

Whole-form Φ on this census takes three values: 0 (232 forms), 0.5
(8 forms), and 2 (16 forms). Twenty-four forms are triadic, 24/256 =
9.375%, the census rate the population script already reported as 9.4%.

In-silico. Hypotheses committed in `67f408ee` before `analyze_ensemble.py`
existed. Instrument control passed before the census: memoryless triadic
at Φ = 2, sticky dyadic at Φ = 0.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 basin entropy tracks Φ (ρ ≥ 0.20 and p < 0.05) | **REFUTED** |
| H2 attractor count tracks Φ | **REFUTED** |
| H3 triadic mean entropy − dyadic ≥ 0.1 bits | **SUPPORTED** |
| H4 triadic mean count − dyadic ≥ 0.5 | **REFUTED** |
| H5 split-half entropy ρ | **SUPPORTED** (halves are one multiset) |

## Reading

B1's designed panel refuted a mean-count link and left the population
correlation open. The census agrees on the rank question: Φ_MIP and
ergodic richness do not clear a modest positive Spearman margin on this
family. The class-mean entropy gap (H3) can hold while the rank
correlation stays near the margin, because 232 of 256 forms sit at
Φ = 0 and dominate the ranks. Component count remains inside the B1
margin of 0.5.

## Limits

Strict-mediation n=3 only. Φ on this family is a three-level ladder, so
the rank test is coarse. The enumeration split in H5 repeats one joint
distribution. No organization is measured. B4, mediator-in-core versus
component count on a wider corpus, stays open.

## Reproduce

```
python org_frontier/studies/ergodic_ensemble_richness/analyze_ensemble.py
```
