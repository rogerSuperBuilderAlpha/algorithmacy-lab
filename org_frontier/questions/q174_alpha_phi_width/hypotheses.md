# q174 — hypotheses

A coded account of a coordination is read by more than one coder, and coders disagree
about which states are active. The bridge `org_frontier/field/rule_to_phi.py` encodes each
coder's reading as a per-party rule set, reads its exact-Φ verdict, and propagates the
disagreement into a confidence interval on Φ. Two claims fix before computing.

## H1 — CI width tracks agreement

Across a synthetic alpha-sweep (Krippendorff alpha from about 0.5 to 1.0 under fixed
consensus rules), mean Φ-CI width decreases monotonically with alpha: Spearman
rho(alpha, width) <= -0.9 with p < 0.01.

NULL: |rho| < 0.5 or the relation is non-monotone, so CI width does not track agreement.

## H2 — an indeterminacy threshold

There is an agreement threshold alpha* below which the propagated CI straddles zero, so the
dyadic-vs-triadic verdict goes indeterminate, for more than 50% of forms. alpha* is stable
to within +/-0.05 across two independent synthetic ensembles.

NULL: no such threshold, or alpha* differs by more than 0.1 between ensembles.

## Scope

All inputs are synthetic coded rule sets, not measured worker states. The study tests
whether the disagreement-to-CI machinery behaves as a measurement instrument should: tighter
agreement, tighter interval; enough disagreement, an honestly indeterminate verdict.
