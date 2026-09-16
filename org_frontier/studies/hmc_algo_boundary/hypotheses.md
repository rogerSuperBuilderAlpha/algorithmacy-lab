# hmc_algo_boundary — hypotheses (fixed before computing)

**Question.** What minimal encoding change turns a literacy/HMC form into an
algorithmacy-irreducible form (and vice versa) at n>3?

**Already known (`constructs_n_gt3` SCALE_BLURS_CONSTRUCTS).**
- Classical HMC pad (W↔S + idle): n_core=2.
- Parallel HMC assist (S=W1∨W2, both read S): n_core=3 — blur.
- Algorithmacy multiparty (S=W∧C1∧C2, all read S): whole triadic Φ=3,
  n_core=4.
- Idle pads make wholes factor while cores preserve roles.
- Ternary / residual noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. Designed encoding
ladder at n=4 (honest small N). Report whole structure/Φ_MIP and major
complex (core, Φ, n_core).

**Proposed boundary (to test).** A party enters the irreducible core iff it
is **in S’s determination** and **reads S** (bidirectional constraining
coupling). Multi-worker OR/AND assist without a counterpart commit is
not yet algorithmacy; binding all outer parties into S’s rule with all
reading S is.

## H1 — second human in S’s rule expands core

From classical HMC (n_core=2), adding a second worker who both feeds S
(OR or AND) and reads S yields n_core≥3. Null: core stays 2.

## H2 — read-without-commit does not add a party

A party that reads S but is absent from S’s determination stays outside
the major complex. Null: such a party appears in the core.

## H3 — full joint commit is the algorithmacy flip

S = conjunction of all outer parties, each reading S, yields whole
structure triadic with core Φ≥3 and all those parties in core. Null:
still dyadic whole or incomplete core.

## H4 — removing a party from the commit drops them (vice versa)

From the full joint-commit form, dropping one outer party from S’s
determination (idle or read-only) removes that party from the core.
Null: core membership unchanged.
