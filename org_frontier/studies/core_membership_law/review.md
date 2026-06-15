# Core-membership law — Stage 1 review

## The question

Which parties of a coordination form belong to its IIT-4.0 major complex (the maximally irreducible
subset), and what rule property decides membership?

## Prior internal work this builds on

The lab has a validated but un-papered answer, recorded across the probe loop and synthesized in
`org_frontier/STRUCTURAL_FINDINGS.md`. The standing account is two conditions:

- **Bidirectional constraining coupling** (necessary): a party must both feed the determination and
  be fed by it. Emit-only sources and read-only sinks stay out of the core. Verified categorical:
  non-bidirectional nodes appear in the core 0/435 times across a sample of the complete 4,096-wiring
  three-node family.
- **Pivotality** (graded): given coupling, the probability a party is in the major complex rises
  monotonically with the determination's Boolean sensitivity to it. Zero influence excludes;
  influence ≥ 0.75 guarantees inclusion (rank-AUC 0.89 over the 256 strict-mediation determinations;
  AUC drops to ~0.70 in the unconstrained family where higher-order joint effects matter).

Supporting results already in the record: triadic forms are rare and dilute with breadth
(9.4% at n=3 → 2.3% at n=4 → 0% at n=5); a conjunctive all-required mediator gives Φ = n−1 with the
full party set in the core; substitutability of any role (counterpart or mediator) collapses
irreducibility; the principal study (`principal/`) shows a corporate owner joins the core iff its
coupling is bidirectional, pinning the necessity condition on a clean 16-form sweep. Related question
papers: `q98_pivotality_bidirectionality` (the membership gate), `q74_verdict_vs_complex` and
`q75_spectator_robustness` (why membership must be read on the major complex, not whole-system Φ).

## The gap

This account has never been through the protocol: no literature grounding, no pre-registered
hypotheses, no paper. The two specific risks the deep-research stage must resolve:

1. **Is the necessity condition (bidirectional coupling) already implied by IIT's exclusion
   postulate?** If an element with no outgoing cause power or no incoming effect power is excluded by
   construction in IIT 4.0, then finding 8 / the necessity half is a corollary of the theory, not a
   discovery, and the paper must say so and cite it.
2. **Is the pivotality result — graded inclusion by causal influence — a known IIT property, or
   novel?** And does it have an analogue in cooperative game theory (pivotal players, Shapley) or the
   o-ring/transaction-cost accounts of essential members?

The paper's contribution stands or falls on the answers. If both halves are implied by existing
theory, the contribution is the *quantification* on coordination forms, not the conditions. The
deep-research report (`literature/deep_research_report.md`) settles this before the hypotheses are
fixed.
