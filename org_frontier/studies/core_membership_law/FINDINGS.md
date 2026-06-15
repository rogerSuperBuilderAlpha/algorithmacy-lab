# Core-membership law — findings

A pre-registered confirmatory run of the two-condition account of major-complex membership. The
hypotheses (`hypotheses.md`) and the deep-research framing (`literature/deep_research_report.md`)
were committed before any number was computed. The run diverged from the prior synthesis in two
informative ways, and the divergence is the reason to pre-register. Reproduce with
`python -m org_frontier.studies.core_membership_law.core_membership`.

## H1 — Necessity of bidirectional coupling: confirmed in the construct's domain

In the strict-mediation family — a mediator between two outer parties with no direct edge between
them, the natural domain of the construct — a node that is not bidirectionally coupled appears in the
major complex **0 of 660 times**. Necessity is categorical, exactly as IIT 4.0 requires: a substrate
unit must both affect and be affected by the rest of the system (Marshall et al. 2023; φ_s = min{φ_c,
φ_e}). The deep-research pass found this is enforced by the instrument itself — PyPhi only considers
nodes with both an input and an output as complex candidates — so the 0/660 is near-tautological by
construction. The necessity half is a confirmation of the theory and the tool on coordination forms,
not a discovery.

The pre-registered *primary* run, on the unconstrained 3-node family, recorded a 15.8% (6/38)
exception rate — and the run itself shows why: **all six exceptions are self-loop nodes**, units
coupled to themselves. A node that feeds only itself is non-bidirectional by the off-diagonal
structural definition used here, yet it can carry cause-effect power and enter the core. The
exception is a definitional edge case (self-coupling), not a counterexample to the IIT requirement,
and the run reports it transparently rather than hiding it behind the strict-mediation figure.

## H2 — Pivotality grades membership: confirmed, and this is the novel part

Among bidirectionally coupled nodes, the probability of major-complex membership rises monotonically
with the determination's Boolean sensitivity to the node: 38.9% at influence ≈ 0.25, then 57.9%,
73.7%, and 87.5% at influence ≈ 1.0. The rank-AUC is 0.629 in the unconstrained family — moderate,
consistent with the prior unconstrained figure (≈0.70) and below the strict-mediation figure (≈0.89),
because single-node influence misses higher-order joint effects in the unconstrained family. The
monotone trend, the substantive claim, is clear; the AUC sits just under the pre-registered 0.65
cutoff in this hardest population.

This graded law is the paper's novel content. IIT 4.0 membership is per-form binary — the exclusion
postulate selects a definite set by strict argmax of φ_s, with no notion of graded inclusion by an
element's causal strength. A membership probability that rises with influence is an across-form
regularity IIT does not state, and it is the cause-effect-structure analogue of Shapley pivotality
(average marginal contribution) and the Null Player axiom (Shapley 1953).

## H3 — Corner separation, additive interior: confirmed

The conditions are near-sufficient at the extremes and trade off in the interior. The lowest coupled
bucket sits at 38.9% inclusion, the highest at 87.5% — a wide corner separation with a monotone
interior, the additive trade-off the prior probe loop reported, not a strict conjunction.

## H4 — Rarity of triadicity: confirmed in the domain, population-dependent

In the strict-mediation family the triadic rate is **9.5%**, reproducing the prior 9.4% population
figure. In the unconstrained family it is 55.7% — triadicity is common when direct outer-party edges
and self-loops are allowed. The pre-registered primary run (unconstrained) surfaced this
population-dependence, which the strict-mediation-only prior figure had obscured: irreducibility is
rare among *mediated* forms specifically, not among Boolean dynamical systems in general.

## H5 — The conjunctive all-required law: confirmed

A mediator that is the AND of all parties, with each party reading it, is irreducible at Φ = n−1 with
the full node set in the core, at n = 3, 4, 5 (Φ = 2, 3, 4). This is the constructive witness that the
membership law admits arbitrarily large irreducible cores against the rarity of H4, and it is the
O-ring / all-essential structure (Kremer 1993) in which every party is pivotal.

## What the pre-registration earned

Writing the paper straight from the prior synthesis would have asserted categorical necessity (0%)
and 9.4% rarity as universal. The pre-registered run on the unconstrained family showed instead that
necessity is categorical only once self-coupling is handled, and that the rarity figure is specific to
mediated forms. Neither changes the law; both sharpen it, and both were invisible until a fresh,
committed run was executed.

## The law

A party is in the irreducible coordination — the major complex — when it is bidirectionally coupled to
the determination (necessary; IIT 4.0's own requirement, confirmed here on coordination forms) and
causally pivotal to it (its membership probability rises with the determination's sensitivity to it;
novel relative to IIT, the cause-effect image of Shapley pivotality). Substitutability, which drives a
party's pivotality to zero, removes it from the core — the Null Player axiom in cause-effect terms.

## Limits

In-silico, on small Boolean models; Φ is read as the binary verdict and membership. Influence is a
single-node Boolean sensitivity, which undercounts higher-order joint effects (hence the moderate
unconstrained AUC). The bidirectionality definition is structural (the connectivity matrix); a
dynamical definition over reachable states would absorb the self-loop edge case. The mapping to Shapley
pivotality is an analogy made precise only at the Null Player corner; a full correspondence between
major-complex membership and the Shapley value is not established here and is the natural next study.
