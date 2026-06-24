# q172 — Methods

## Forms

The faithful baseline is one of the four Q127 gates over the two party inputs (W, C): AND, OR, XNOR
(agree, W==C), XOR (differ, W!=C). The interested gate at level k imposes the agenda a on the k
(W, C) states the baseline least warrants the agenda in, and commits the faithful baseline on the
rest. This is the construction Q127 already uses for every baseline. Opaque is the faithful gate
(k=0); interested is the gate at k=1, the agenda on the single least-warranted state. Both agendas,
approve (a=1) and deny (a=0), are averaged into every reported gap.

## Facet readers

Each facet reuses the difficulty measure its prior study read, wrapped in the shared bridge
`org_frontier.cognition.interested_mediator_forms`. Each reader takes a gate over (W, C) and returns
a difficulty oriented so larger is harder.

- **commitment** (computationalism, q163). The committing triad W'=S, S'=gate, C'=S, scored by
  whole-system Φ. Difficulty is 2.0 − Φ: the binding the worker would have to supply herself.
- **counterpart_inference** (direct perception, q164). With C hidden and uniform, the worker fits
  the worker-marginal f(W) by majority over C. Difficulty is the share of (W, C) states f(W)
  mispredicts.
- **signal_compression** (embodiment, q165). The parties read S at fidelity q; q<1 mixes in 0.5
  noise. Difficulty is the Φ shed from full read to half read, Φ(q=1) − Φ(q=0.5).
- **phantom_addressee** (theory of mind, q166). The phantom triad W'=S, S'=gate, C'=C, scored by
  the major-complex Φ that binds the worker. Difficulty is 2.0 − coreΦ.
- **opacity_floor** (predictive processing, q168). The residual surprise H(out|W) with C hidden and
  uniform — the bits no W-only model removes.
- **rule_change_tracking** (predictive processing, q171). The PP4 drift: S commits the gate with
  probability 1−d and a flipped arm (W∨C on the non-overridden states) with probability d=0.25.
  Difficulty is the Φ lost to drift, Φ(static) − Φ(drift).

## Aggregation

For each facet and baseline, the gap is interested − opaque, averaged over the two agendas. The
per-facet interest tax is the mean absolute gap over the four baselines, in native units. For
cross-facet display the gaps are min-max normalized within each facet to [0, 1] across baselines.

H1 reads whether the two pre-named survey facets are the two largest by tax and whether at least one
other facet sits at least ten times below the smaller named facet. H2 reads whether the facet
pairwise ordering by absolute gap is concordant across all four baselines (every pair keeps its
order, ties allowed); discordant pairs are reported.

## Instrument control

The faithful committing triad [x1, x0&x2, x1] must read verdict 'triadic' with max_phi 2.0 before
any facet is computed.

## Determinism and scope

Every facet reader is an exact Φ or closed-form information computation over a small Boolean truth
table. No RNG enters any reported number; a generator is seeded for reproducibility hygiene. The
results are exact Φ and closed-form information on three- and four-node Boolean models. They are
evidence about the instrument and the construct. "Agenda", "interest", "facet" label output values
and rule structure, not measured intent. The empirical reading and the mapping to the survey scale
are on synthetic forms; the link to the scale is a formal prediction.
