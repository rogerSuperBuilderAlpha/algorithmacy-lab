# Agenda: ten gaps in the corpus (Q89–Q98)

Ten runnable questions that probe gaps the program has left open. Each is grounded in a specific finding
or a stated caveat, reuses existing machinery, and is computable now on the binary IIT-4.0 instrument —
unlike the parked designs (Q76–Q78, Q86, Q87, Q88), which wait on data, multivalued IIT, or a written
correspondence. The format follows `RESEARCH_AGENDA_Q74.md`: the question, the gap it fills, the machinery
to reuse, and the discriminator that would settle it. Entries are ordered by expected payoff. Each runs
through the six-stage protocol: pre-register the hypotheses before computing, validate the instrument on a
control, report nulls.

## Priority 1 — Do the laws generalize, and how robust are they?

- **Q90 — Does the core-membership law generalize in size?** The bidirectional-plus-pivotality account of
  major-complex membership was validated at rank-AUC 0.89 on the 256-form **n=3** family. Q81 showed a
  *learned* surrogate fails to cross sizes; the *structural* law's size-generalization is untested.
  *Reuse:* `corpus/determination.py` lifted to n = 4, 5, 6. *Discriminator:* whether the pivotality →
  membership monotonicity holds, degrades, or breaks as parties multiply — a structural counterpart to
  Q81's null.

- **Q93 — Margin-to-dyadic: a fragility metric.** The verdict is binary at Φ_MIP = 0, with no measure of
  how close a triadic form sits to collapse. For each triadic form, find the minimal structural
  perturbation (a single edge or function-bit flip) that collapses it to dyadic. *Reuse:* the 256-form
  census with a perturbation sweep. *Discriminator:* whether this structural margin predicts which triads
  survive the Q71 noise, connecting structure to robustness.

## Priority 2 — Heterogeneity and asymmetry

- **Q89 — The heterogeneous agent market.** Q85's market was symmetric, and its caveat marks heterogeneous
  agents as untested. When agents differ in what they read (one reads the recipient, one only the sender,
  one a back-channel), which enter the major complex, and does a stable heterogeneous core subset form?
  *Reuse:* the Q85 market with `major_complex`. *Discriminator:* a core that tracks each agent's coupling
  and pivotality (Finding 8) rather than the all-or-nothing collapse of the interchangeable market.

- **Q98 — Decoupling pivotality from bidirectionality.** Finding 8 ties membership to bidirectional
  coupling and pivotality together; their interplay at the extremes is unmapped. Can a party sit in the
  core with near-zero outgoing influence (a near-pure sink that is still pivotal), or near-zero incoming?
  *Reuse:* the 16-form principal sweep, extended to asymmetric coupling strengths. *Discriminator:* whether
  bidirectionality is strictly necessary, or extreme pivotality on one side alone suffices.

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
