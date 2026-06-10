# Agenda: ten gaps in the corpus (Q89–Q98) — done

All ten questions below have been run through the six-stage protocol and are on the record; each entry
links its study. The results were mixed by design: confirmations, refutations, and several surprises
(composition decides heterogeneous membership; cores compete rather than fuse; structural and dynamical
robustness anti-align; the membership gate is hard-cornered but soft inside; a coalition can capture the
mediator). The headings are kept for the record, each now marked done.

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

## Priority 3 — Beyond a single core (done)

- **Q94 — Multiple coexisting complexes.** *Done.* Coordination holds multiple cores: two uncoupled units
  give two disjoint complexes and a one-way bridge keeps both. But coupling does not fuse cores — a mutual
  bridge collapses to one smaller core rather than a spanning one (the cores compete), and a
  self-referential spectator forms its own complex. H1, H3 confirmed; H2, H4 refuted. See
  `questions/q94_multiple_complexes/`.

- **Q95 — Composition of coordination units.** *Done.* Composing two read-recipient triads through a shared
  node fragments rather than unifies: the form is whole-system dyadic, splits into two complexes, Φ does not
  add (stays 2.0), and the shared node binds only the upstream core. Composition keeps units modular. H4
  confirmed; H1, H2, H3 refuted. See `questions/q95_composition_of_triads/`.

## Priority 4 — Degraded information and memory (done)

- **Q91 — Partial observability: the lossy channel.** *Done.* The triad degrades gracefully under a lossy
  read: with the mediator reading the recipient through a binary symmetric channel, Φ falls monotonically
  (2.0 → 0.16) and stays triadic until the channel carries no information (error 0.5). Input-side
  degradation mirrors Q79's commit-side emergence. All four hypotheses confirmed. See
  `questions/q91_lossy_channel/`.

- **Q92 — The stateful mediator.** *Done.* A memory that tracks the recipient substitutes for a live read:
  the tracking-memory triad stays triadic at Φ = 2.0, the core reorganizing to {M, R, Mem} with the worker
  displaced. A frozen memory and a self-referential mediator are dyadic. Liveness (Finding 3) is the
  recipient being bound through some path, not the current read. All four hypotheses confirmed. See
  `questions/q92_stateful_mediator/`.

## Priority 5 — Contingency and adversarial security (done)

- **Q96 — State-contingent membership.** *Done.* Contingent participation factors the whole, the way
  optionality does (Finding 5): gating the recipient's read gives a whole-system dyadic form with a
  localized {M, R} core, the recipient bound to the mediator while the worker and the gate are excluded.
  H2, H3 confirmed; H1, H4 refuted. See `questions/q96_contingent_membership/`.

- **Q97 — The coordinated adversary.** *Done.* A coalition gains no influence without membership — but it
  can. Two observers leave the core {E, M, R} intact and two sources cannot manufacture a triad, while a
  bridging coalition becomes triadic with core {M, X1, X2}, capturing the mediator and displacing the
  legitimate worker and recipient. Influence still requires membership; a coalition can achieve it
  collectively. H2, H3, H4 confirmed; H1 refuted on the whole-system reading. See
  `questions/q97_coordinated_adversary/`.

## Sequencing

Q90 and Q93 first: they test whether the program's central claims, the membership law and the verdict's
robustness, hold beyond the n=3 family they were established on, so every later question inherits a firmer
or a qualified foundation. The heterogeneity pair (Q89, Q98) and the beyond-one-core pair (Q94, Q95) open
the widest new ground. Q91, Q92, Q96, and Q97 each take one well-scoped step past a stated assumption. All
ten run on the existing instrument; none waits on an external anchor.
