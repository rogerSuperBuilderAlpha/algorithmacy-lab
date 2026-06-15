# Core-membership law — Stage 3 hypotheses (pre-registered)

Fixed before the confirmatory run, and framed by the Stage-2 literature pass
(`literature/deep_research_report.md`). Each hypothesis states its predicted outcome, its decision
rule, and its relationship to prior theory, so the contribution is clear before any number is seen.

## H1 — Necessity of bidirectional coupling (confirmatory of IIT 4.0)
A node that is not bidirectionally coupled — it does not both feed and get fed by the determination —
is **never** in the major complex. Prediction: across 600 random 3-node forms, non-bidirectional
nodes appear in the major complex at a rate of ~0%. Decision rule: confirmed if the rate is under 1%
(a handful attributable to numerical ties), refuted otherwise. **Relation to prior work:** this
confirms IIT 4.0's own requirement that a substrate unit must both affect and be affected by the rest
of the system (Marshall et al. 2023; φ_s = min{φ_c, φ_e}). The hypothesis is confirmatory; the
contribution is the quantification on coordination forms, not the condition.

## H2 — Graded pivotality (novel relative to IIT)
Among bidirectionally coupled nodes, the probability of major-complex membership rises **monotonically**
with the determination's Boolean sensitivity to the node (its influence). Prediction: rank-AUC of
influence predicting membership is well above 0.5 (target ≳ 0.75 in the unconstrained 3-node family),
and the bucketed inclusion rate is monotone increasing in influence. Decision rule: confirmed if AUC
> 0.65 and the bucket trend is monotone non-decreasing. **Relation to prior work:** IIT membership is
per-form binary (strict argmax exclusion; Albantakis et al. 2023), so a graded across-form membership
law is not stated in IIT. It is the cause-effect-structure analogue of Shapley pivotality
(average marginal contribution) and the Null Player axiom (Shapley 1953). This bridge is the paper's
novel claim.

## H3 — Joint sufficiency at the corners, additive trade-off in the interior
The two conditions are jointly near-sufficient at the extremes — a coupled node of near-zero
influence is excluded, a coupled node of near-maximal influence is included — and trade off in the
interior rather than acting as a strict conjunction. Prediction: the lowest influence bucket has a low
inclusion rate and the highest has a high inclusion rate, with intermediate buckets between.
Decision rule: confirmed if corner buckets separate by a wide margin with a monotone interior.

## H4 — Rarity of triadicity
Triadic forms are a small minority of the random 3-node population. Prediction: the triadic rate over
600 random forms is order 10%. Decision rule: confirmed if it falls in roughly 5–20% (consistent with
the 9.4% strict-mediation population figure; the unconstrained family may differ). **Relation:** the
rarity itself is the empirical content; the law it reduces to is that irreducibility requires every
party bound into one joint determination.

## H5 — The conjunctive all-required law
A mediator that is the AND of all parties, with each party reading it, is irreducible at Φ = n−1 with
the full node set in the core. Prediction: for n = 3, 4, 5, Φ = n−1 and the core is all n nodes.
Decision rule: confirmed if both hold at every size. **Relation:** this is the constructive witness
that the membership law admits arbitrarily large irreducible cores (against the rarity of H4), and the
conjunctive form is the O-ring/all-essential structure (Kremer 1993) where every party is pivotal.

## What would refute the account
Non-bidirectional nodes routinely entering the core would refute H1 and contradict IIT 4.0. A flat or
non-monotone influence–membership relation would refute H2 and remove the bridge to pivotality. Either
would mean the standing two-condition account does not hold on a fresh, pre-registered run.
