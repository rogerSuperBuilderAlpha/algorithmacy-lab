# Findings — q160

Coupling-centrality recovery of major-complex membership holds at five parties at the four-node
level. The structure-behavior dissociation does not widen with scale. On `deep_pool_all`, the worker
that exact Φ excludes from the irreducible core is also the lowest-coupled node behaviorally, so the
behavior agrees with the structural exclusion rather than inventing a relay-style false positive.

| measure | value |
|---|---|
| named five-node forms, full separation (testable) | 2/4 |
| `rand_form5` ensemble, full separation | 13/39 = 33.3% |
| pooled five-node full-separation fraction | 15/43 = 34.9% |
| four-node baseline (control) | 36% |
| deep_pool_all core (Φ=3.00) | {S1,S2,C1,C2}, excludes W |
| worker out-couples weakest core member | 5/20 seeds |
| worker mean coupling rank (0=top of 5) | 3.45 |

## Verdicts
- H1 (five-node full-separation is LOWER than 36%, dissociation widens): SUPPORTED on the literal
  threshold. The pooled fraction is 34.9%, below 36% by one form out of 43. The substantive reading
  is that the rate is indistinguishable from the four-node rate: scale does not meaningfully widen
  the dissociation. The recovery limit found at three and four nodes carries to five.
- H2 (the excluded worker is a relay-style false positive among the top-coupled nodes): REFUTED. The
  worker out-couples the weakest core member in only 5 of 20 seeds and sits at mean rank 3.45 of 5,
  near the bottom. As a chain endpoint reading one input, the worker is weakly coupled, so behavior
  confirms the structural exclusion.

## Reading
The two instruments measure different things and agree about a third of the time, the same partial
recovery seen at smaller n. Adding a fifth party does not erode that agreement further. Where exact Φ
excludes a node for a structural reason (an endpoint with a single read), coupling centrality can
agree with the exclusion. The dissociation is not a one-directional drift toward more disagreement at
larger scale.
