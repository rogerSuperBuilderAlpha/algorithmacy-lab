# q200 — Φ_coord loads on the general algorithmacy factor, not a specific facet

The survey arm fields the Algorithmacy Competence Scale alongside coordination scales. A reader who
sees a coordination measure expects it to load on a coordination facet. This study asks the opposite
question and answers it: in a bifactor model of the ACS, a worker's Φ_coord predicts the general
algorithmacy factor, not the system-coordination facet.

The bifactor model separates a general algorithmacy factor g, on which every ACS item loads, from
three orthogonal specific facets: computational interpretation, system coordination, and recursive
thinking. Each facet carries the variance its three items share once the general factor is removed.
Φ_coord enters through the shared bridge `phi_bridge.py`: each simulated worker's reported task
interdependence, system-authority commit, and substitutability map to a W-S-C Boolean form, and
Φ_coord is the form's exact IIT-4.0 max Φ_MIP. The commit form is irreducible (Φ_coord = 2.0); the
convey form factors (Φ_coord = 0.0).

The simulated W2 cohort draws 400 workers. The coordination latent that drives the reported conditions
loads on the general factor g, so Φ_coord is built as a general-algorithmacy signal. The probe recovers
that placement. The standardized path from Φ_coord to g is +0.46, 95% CI [+0.37, +0.55]. The paths to
the three specific facets sit near zero, and each general-minus-facet difference has a bootstrap CI
excluding 0. Φ_coord rides the dimension every ACS item shares, not the variance peculiar to any one
block.

A competing model routes Φ_coord to the system-coordination facet, the facet a reader would guess. The
two routings are compared on the augmented covariance of the nine items plus Φ. When Φ is routed to g,
the implied covariance lets Φ correlate with all nine items, matching the data, and CFI reaches 0.99.
When Φ is routed to the SC facet, the implied covariance lets Φ correlate only with the three SC items,
so it cannot reproduce the observed Φ-to-CI and Φ-to-RT covariances, and CFI falls to 0.90. ΔCFI is
+0.09 in favour of the general path, above the .01 threshold.

The placement is the contribution. A coordination measure built from exact Φ behaves as a general
algorithmacy indicator, not a narrow coordination-facet indicator, which is what the construct theory
predicts and what a discriminant test should confirm before the sub-competence studies proceed. The
cohort is simulated and no worker is measured, so the loadings are evidence about the bridge and the
bifactor pipeline on synthetic data. A real W2 wave would replace the simulation and turn this scaffold
into a confirmatory bifactor test.
