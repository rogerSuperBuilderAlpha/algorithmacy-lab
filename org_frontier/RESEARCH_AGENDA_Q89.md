# Agenda: ten gaps in the corpus (Q89–Q98)

Ten runnable questions that probe gaps the program has left open. Each is grounded in a specific finding
or a stated caveat, reuses existing machinery, and is computable now on the binary IIT-4.0 instrument —
unlike the parked designs (Q76–Q78, Q86, Q87, Q88), which wait on data, multivalued IIT, or a written
correspondence. The format follows `RESEARCH_AGENDA_Q74.md`: the question, the gap it fills, the machinery
to reuse, and the discriminator that would settle it. Entries are ordered by expected payoff. Each runs
through the six-stage protocol: pre-register the hypotheses before computing, validate the instrument on a
control, report nulls.

## Priority 1 — Do the laws generalize, and how robust are they? (done)

- **Q90 — Does the core-membership law generalize in size?** *Done.* The law generalizes in kind:
  bidirectional coupling stays strictly necessary (non-bidir in-core 0.000 at n = 3, 4, 5) and the
  pivotality gradient persists without collapsing (rank-AUC 0.71/0.62/0.73, flat across size). The
  single-scalar pivotality predictor is moderately strong on the full family, below the 0.75 bar set from
  the strict-mediation 0.89. n = 6 is beyond the exact ceiling. See `questions/q90_membership_law_scaling/`.

- **Q93 — Margin-to-dyadic: a fragility metric.** *Done.* Every triadic form sits one single-bit flip from
  collapse, and the margin is near-binary, set by the mediator's function. Structural and dynamical
  robustness come apart: parity mediators give the structurally sturdier triads (0.250 vs 0.125) but the
  noise-fragile ones (Φ 0.38 vs 1.16), so the structural margin does not predict noise survival. See
  `questions/q93_fragility_margin/`.

## Priority 2 — Heterogeneity and asymmetry (done)

- **Q89 — The heterogeneous agent market.** *Done.* Membership is a property of the joint determination,
  not the agent: a passive agent is excluded and substitutability still collapses, but a partial-reading
  required agent drops out in a two-agent market (the core localizes to {M1, C}) and binds in a three-agent
  mixed market (full core). Composition decides which heterogeneous agents are core, refining Finding 8's
  pivotality. See `questions/q89_heterogeneous_market/`.

- **Q98 — Decoupling pivotality from bidirectionality.** *Done.* The membership gate is hard-conjunctive at
  the corners (P(core) is 0.000 at zero reading or zero influence, 1.000 at strong both) but additive in
  the interior, where the sum of the two influences predicts membership as well as
  the minimum (rank-AUC 0.783 vs 0.772). Each side is strictly necessary; within the bidirectional region
  they substitute. See `questions/q98_pivotality_bidirectionality/`.

## Priority 3 — Beyond a single core

- **Q94 — Multiple coexisting complexes.** Finding 8 always reads the *major* complex; the corpus never
  asks whether coordination fragments into two disjoint irreducible cores. Build two mediated pairs sharing
  a spectator or a channel and ask when the form holds two separate triads, one merged core, or none.
  *Reuse:* PyPhi's full complex enumeration, not only the maximal. *Discriminator:* the structural
  condition for multi-complex coordination, a regime the program has not entered.

- **Q95 — Composition of coordination units.** Q65 chained mediators; no study chains whole triads, where
  the output of one triadic unit becomes a party in the next. Does Φ compose additively, unify into a
  higher-order core spanning both units, or fragment? *Reuse:* the read-recipient triad composed with
  itself. *Discriminator:* additive Φ, a single spanning complex, or decoupling — the modularity question.

## Priority 4 — Degraded information and memory

- **Q91 — Partial observability: the lossy channel.** Every read in the corpus is exact, and Q79 made the
  *commit* stochastic, but the *input* read is never degraded. When the mediator reads a coarsened or noisy
  version of a party at fidelity f, at what fidelity does the triad collapse? *Reuse:* `max_phi_float` on a
  TPM with a noisy input map. *Discriminator:* a fidelity threshold for triadicity against a smooth decay,
  distinct from Q79's commit-side noise.

- **Q92 — The stateful mediator.** All determinations are memoryless, with the next state a function of the
  current state alone. If the mediator's update depends on its own history, a two-bit memory, does
  internal memory substitute for a live read, manufacturing or destroying a triad? *Reuse:* the classifier
  with an augmented mediator node. *Discriminator:* whether memory can stand in for liveness (Finding 3),
  or whether liveness is irreducibly about the current read.

## Priority 5 — Contingency and adversarial security

- **Q96 — State-contingent membership.** Finding 5 shows substitutability collapses the triad, but
  participation is always unconditional; a party bound into the core only in some states is untested. Does
  contingent binding yield a state-averaged triad, or factor? *Reuse:* the Q67 reciprocity machinery with a
  gating condition. *Discriminator:* whether contingent participation integrates on average, or the
  conditionality factors it out.

- **Q97 — The coordinated adversary.** Q84 showed a single read-only agent cannot flip the verdict; a
  coalition of outside agents is untested. Can two or more non-core agents jointly manufacture or destroy a
  triad that none can alone? *Reuse:* the Q84 adversarial form with several external agents.
  *Discriminator:* whether influence-without-membership becomes possible for a coalition, sharpening the
  single-agent boundary that matters for security.

## Sequencing

Q90 and Q93 first: they test whether the program's central claims, the membership law and the verdict's
robustness, hold beyond the n=3 family they were established on, so every later question inherits a firmer
or a qualified foundation. The heterogeneity pair (Q89, Q98) and the beyond-one-core pair (Q94, Q95) open
the widest new ground. Q91, Q92, Q96, and Q97 each take one well-scoped step past a stated assumption. All
ten run on the existing instrument; none waits on an external anchor.
