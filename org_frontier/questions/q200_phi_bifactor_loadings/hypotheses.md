# q200 — hypotheses

Question: in a bifactor model of the Algorithmacy Competence Scale (a general algorithmacy factor g
plus three orthogonal specific facets — computational interpretation CI, system coordination SC,
recursive thinking RT), does a worker's Φ_coord predict the GENERAL factor rather than one specific
facet, in the simulated W2 cohort?

Fixed before computing.

**H1.** Φ_coord predicts the bifactor GENERAL algorithmacy factor (β > 0, 95% CI excludes 0), and
this general-factor path exceeds each specific-facet path: Δ = β_g − β_facet has a 95% CI that
excludes 0 for every facet (CI, SC, RT).
Null: Φ_coord's general-factor path is no larger than its specific-facet paths.

**H2.** The model where Φ_coord predicts the general factor fits better than the competing model where
Φ_coord predicts only the SC specific factor, by ΔCFI ≥ .01 favouring the general path.
Null: routing Φ_coord to the SC specific facet fits as well as routing it to the general factor.

Controls fixed in advance:
- the three specific-facet scores are residualized on the general-factor score, so the bifactor scores
  are orthogonal and the facet paths carry only facet-specific variance;
- the SC facet is the named competitor in H2 because SC (system coordination) is the facet a reader
  would expect a coordination measure to load on; the test asks whether Φ_coord nonetheless routes to g;
- a forced-dyadic control cohort (Φ_coord ≡ 0) is available through the shared bridge as the null form,
  carrying no variance to load on any factor.
