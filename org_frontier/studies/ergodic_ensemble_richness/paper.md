# Basin richness and Φ on the strict-mediation census

## Abstract

Exact IIT-4.0 Φ_MIP was computed on all 256 strict-mediation Boolean
forms at three nodes, and compared with basin entropy and attractor
count. The pre-registered rank tests stay under |ρ| = 0.20. The verdict
is `NO_ENSEMBLE_LINK`. A mean entropy gap between the triadic class and
the dyadic class clears its own margin. The result is about these models.

## Introduction

A finite deterministic Boolean map decomposes into attractors and the
basins that reach them (Birkhoff 1931). Integrated information Φ_MIP
asks whether the same map's cause-effect structure factors (Albantakis
et al. 2023; Mayner et al. 2018). Strand B of the ergodicity track asks
whether those two descriptions travel together. On a designed panel of
nine forms they did not, at the pre-registered mean margins. Agenda item
B5 asks the population version: a rank correlation on an ensemble at
fixed n.

## Related work

The association measure is Spearman's ρ (Spearman 1904), with a
permutation null. Peters (2019) is the reason a basin decomposition
matters for this track: a time average and an ensemble average can part,
and a single scalar computed on the rule can still miss that parting.
The sources underwrite the two quantities. They do not state a sign for
this census. The lab's population script already enumerated these 256
forms and reported the triadic rate. It did not record basins.

## Hypotheses

H1 and H2 require Spearman ρ ≥ 0.20 and a positive one-sided permutation
p < 0.05, for basin entropy and for attractor count. H3 and H4 repeat
the designed panel's mean margins (0.1 bits, 0.5 components) on the
census class means. H5 asks the enumeration's two halves to agree in
sign with |ρ| ≥ 0.10. The primary word is fixed in `hypotheses.md` and
was committed before this script existed. The instrument gate is the
memoryless triad at Φ = 2 and the sticky mediator at Φ = 0.

## Methods

`enumerate_family` yields the 256 forms. `classify_rules` supplies
whole-form Φ_MIP. `find_attractors` and `basin_entropy` supply the
structural pair. Permutations: 2000 shuffles, `default_rng(7)`. Details
and the abort rule are in `methods.md`.

## Results

The gate passed. The census has 24 triadic forms and 232 dyadic forms.
ρ(Φ, basin entropy) = 0.1015, p = 0.0510. ρ(Φ, component count) =
0.1286, p = 0.0185. H1 refuted. H2 refuted. Mean basin entropy is 0.4685
on triadic forms and 0.2521 on dyadic forms (H3 supported). Mean
component counts are 1.6667 and 1.3448 (H4 refuted). The two halves
carry the same multiset of rows, so their shared ρ of 0.1015 is one
distribution written twice (H5 supported under the letter of the rule).
The primary word is `NO_ENSEMBLE_LINK`.

Φ on this family takes the values 0, 0.5, and 2.

## Discussion

The designed panel and the census agree that component count does not
clear a half-component mean gap, and that a positive rank link of the
size B5 called support is absent. The entropy class means do separate.
With 232 forms at Φ = 0, a gap between the small triadic class and the
dyadic mass can clear 0.1 bits while the rank correlation across all
256 forms stays near 0.10. That is a property of a rare triadic class
inside a three-level Φ ladder.

## Limitations

Evidence about the 256-form strict-mediation family at n=3. The rank
test is coarse because Φ takes three values here. H5's split repeats
one multiset. Nothing in the run measures a firm, a platform, or a
worker. B4 remains open.

## References

Albantakis, Larissa, et al. 2023. "Integrated information theory (IIT)
4.0." *PLOS Computational Biology* 19(10): e1011465.
doi:10.1371/journal.pcbi.1011465.

Birkhoff, George David. 1931. "Proof of the ergodic theorem."
*PNAS* 17(2): 656–660. doi:10.1073/pnas.17.2.656.

Mayner, William G. P., et al. 2018. "PyPhi: A toolbox for integrated
information theory." *PLOS Computational Biology* 14(7): e1006343.
doi:10.1371/journal.pcbi.1006343.

Peters, Ole. 2019. "The ergodicity problem in economics." *Nature
Physics* 15: 1216–1221. doi:10.1038/s41567-019-0732-0.

Spearman, C. 1904. "The proof and measurement of association between two
things." *The American Journal of Psychology* 15(1): 72–101.
