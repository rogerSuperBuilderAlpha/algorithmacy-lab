# Experiment design — validating the structure axis of the Φ model

**Internal working doc. Not reader-facing.** Purpose: organize the experiment that tests whether the
Paper 3 model's score (Φ) predicts coordination difficulty. This is the empirical step the dissertation
currently defers; it is the thing the cut Chicago anchor could not do.

## The problem this fixes (why the prior attempt failed)

The Chicago rideshare "anchor" varied **pool size**, and in the pooling model Φ = k + 1, so Φ moved only
with the number of parties. The correlation (friction r ≈ +0.98) therefore validated the **party-count
axis** — the one axis you do not need Φ (or any of the machinery) to see. It said nothing about the model's
**novel content**: that *determination structure* sets difficulty at a **fixed** number of parties. That
structure axis is currently a model-internal claim with zero outcome validation.

## The core idea: manipulate structure, don't observe it

A field study of real organizations is hard for three reasons, all of which this design removes:
1. **No comparable outcome across org types** (what single DV moves between a court, Uber, a staffing
   agency?). → We use one task with one outcome metric.
2. **Mapping a real org to a determination structure is an analyst judgment** (the structure variable
   carries modeling noise). → We *build* the structure, so it is exact.
3. **Party count confounds everything in observational data.** → We **hold party count fixed at three** and
   vary only the determination structure.

Because we manipulate rather than infer, **the three modeling choices become exact controls instead of
assumptions** (see `CONDITIONS.md`): the representation is what we build, the state rule is the task's round
structure, and the party partition is the three roles by construction. The modeling ambiguity that made the
field study impossible disappears.

## Research question

At a **fixed** number of parties (n = 3), does the model's score Φ — varied by changing only the mediator's
determination structure — predict how hard the parties find it to coordinate?

## Hypotheses (fixed before any data)

- **H1 (structure axis, primary).** Among three-party forms, coordination difficulty increases with Φ:
  forms the model scores higher are coordinated less successfully, more slowly, and at higher cost.
- **H1a (the money contrast — "eliminate the dyad").** Holding the mediator's determination fixed (AND),
  **removing the direct back-channel** between the parties (partial Φ = 0.83 → strict Φ = 2.0) makes
  coordination measurably harder. This is the single structural change the dissertation's political-economy
  claim rests on, tested behaviorally.
- **H0 (informative null).** At fixed party count, Φ does not predict difficulty — i.e., the structure axis
  is vacuous and only party count ever mattered. This is the null the Chicago anchor could not rule out.
- **H2 (Cerullo probe).** Parity determinations (Φ = 0.5) are a known concern: trivially regular XOR-type
  structures can carry high Φ (Cerullo 2015). Test whether parity's *observed* difficulty matches its Φ
  rank or comes out anomalously. An anomaly here is an informative result *about the measure*, not a failure
  of the experiment.

## Independent variable: determination structure (4 levels, all n = 3)

Exact node rules and computed Φ in `CONDITIONS.md`. Summary:

| Condition | Structure | Mediator rule | Back-channel | Φ |
|---|---|---|---|---|
| C0 Dyadic | parties coordinate directly; mediator inert | — | yes (direct) | 0.00 |
| C1 Parity | strict topology, parity determination | S′ = W ⊕ C | no | 0.50 |
| C2 Partial | mediated match + direct channel | S′ = W ∧ C | yes | 0.83 |
| C3 Strict | parties reach each other only through the determination | S′ = W ∧ C | no | 2.00 |

Φ is **continuous IV** for H1 (rank-order Φ vs difficulty across C0–C3); **C2 vs C3** is the clean planned
contrast for H1a (identical determination, back-channel is the only difference).

## Dependent variables (coordination difficulty)

- **Success** — did the parties reach the coordinated/correct joint outcome within the episode? (primary)
- **Time-to-coordinate** — rounds/steps to reach it (efficiency).
- **Cost** — wasted/uncoordinated moves, detours, or payoff lost relative to the optimal joint action.
- **Error** — rate of miscoordinated outcomes.

## Predicted pattern

Difficulty ordering predicted by the model: **C0 < C1 < C2 < C3** (Φ-monotone), with the **C3 > C2** gap
(H1a) the most theoretically load-bearing. A flat or non-monotone result supports H0. A parity anomaly
(C1 out of order) speaks to H2 / Cerullo.

## Three ways to run it (strongest → weakest)

1. **Human study** (online, e.g. Prolific) — real coordinators in W/C roles coordinate through a programmed
   mediator of structure X. Strongest external validity. Proper empirical chapter; months of work
   (design → IRB → recruit → run → analyze). Protocol scoped separately if pursued.
2. **Agent-based simulation** — buildable now; see `SIM_SPEC.md`. Bounded-rational agents coordinate through
   structure X; we measure performance and test whether Φ(X) predicts it. **Non-circular**: agents do not
   "know" Φ, so Φ predicting their performance is a real test of whether Φ captures coordination difficulty.
   Honest scope: validates the **mechanism in silico** (the structure axis is not vacuous; the model behaves
   as claimed), not that humans coordinate as the agents do.
3. **Vignette/survey** — scenarios of varying structure, perceived-difficulty ratings. Weakest; fallback.

Recommended sequence: **(2) first** (cheap, runnable now, settles H0/H1/H2 in silico and de-risks the
design), then **(1)** if an empirical chapter is required or wanted.

## Threats to validity / pre-commitments

- **Sim discipline (critical).** The agent decision rule must be fixed *a priori* and independently
  motivated (bounded-rational best-response to observed signals), never tuned to make Φ win. Document the
  rule before running; report it verbatim. NB: this avoids *trivial* circularity (the agents are told
  nothing), but Φ and difficulty both derive from the wiring, so the result is a consistency check, not an
  independent validation — report it as such.
- **External validity (sim).** State plainly that a simulation establishes internal/construct validity of
  the mechanism, not field generalization.
- **Confound control.** Party count fixed at 3 across all conditions (the whole point). Hold task payoff
  structure, episode length cap, and information per role constant across conditions; the *only* thing that
  varies is the determination structure.
- **Parity is two changes from partial.** C1 (parity, no back-channel) differs from C2 (AND, back-channel)
  on two factors. For a clean single-factor read, lean on **C2 vs C3** (back-channel only) and on the
  Φ-monotonicity across all four; treat C1's absolute placement as the H2 probe, not a clean contrast.
- **Magnitude is ordinal.** Per Cerullo, we test *ordering*, not that difficulty scales linearly with Φ.

## What success / failure means

- **H1 + H1a supported** → the structure axis is real: Φ predicts coordination difficulty at fixed party
  count. This is the validation the dissertation currently lacks and the empirical-chapter the format audit
  flagged.
- **H0 not rejected** → the model's novel content is empirically vacuous; the honest move is to say so and
  retreat Paper 3's claims to the model-characterization level (where they already are).
- **Parity anomaly (H2)** → informative about the measure; supports reading magnitude ordinally and flags a
  refinement (e.g., a synergy/redundancy decomposition that down-weights parity).

## Open decisions (resolve before building — see DECISIONS in README)

- Strengthen Paper 3 vs. stand up a new empirical Paper 4?
- The coordination task itself (what are W and C trying to jointly achieve?). Candidate in `SIM_SPEC.md`.
- Within- vs between-subjects (human); episodes-per-condition and agent-population size (sim).
