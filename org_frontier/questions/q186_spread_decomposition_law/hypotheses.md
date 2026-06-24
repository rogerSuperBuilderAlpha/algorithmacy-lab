# q186 — Hypotheses

The spread between two party accounts of one coordination is reported as a tuple of three
components: verdict agreement, Φ gap, and core-membership divergence (defined by the q183 bridge
`disagreement_phi.spread`). The question is whether those three numbers carry separate information
or whether they collapse onto one underlying axis, so the tuple could be replaced by a single
scalar.

## H1
There exist account pairs that agree on verdict (verdict_agreement = 1) yet have phi_gap > 0, and
pairs that disagree on verdict (verdict_agreement = 0) yet have core_jaccard = 1. Both off-diagonal
cells are populated, so the three components are not rank-one collinear.

H1-null: all three components are monotone functions of one another, so the spread is effectively
one number and the tuple is redundant.

## H2
The fraction of the census exhibiting at least one off-diagonal pattern (agree-but-gapped or
disagree-but-same-core) exceeds 10 percent.

H2-null: such patterns occur at or below the rate expected from numerical Φ noise (< 1 percent), so
the components are practically collinear.

Both hypotheses were fixed before the census was computed. The accounts are synthetic; any verdict
holds on synthetic data.
