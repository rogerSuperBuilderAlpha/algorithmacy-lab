# Joint determination — hypotheses (pre-registered addendum)

Fixed 2026-09-24, before any form below was computed under the criterion. The commit that lands this file
and [`jd_methods.md`](jd_methods.md) is the pre-registration.

## Why an addendum

The Peirce paper's H1 was refuted as pre-registered: branching gave one-input wirings three-term facts. The
split into a cause side and an effect side, which showed every excess on the effect side, came afterward
and is labelled *post hoc* in [`FINDINGS.md`](FINDINGS.md). The talk in
[`../../../submissions/triadic_reduction/`](../../../submissions/triadic_reduction/) now fixes a criterion
for an irreducible triad — *joint determination in a whole* — and a critic of that talk found two gaps.
First, the criterion was chosen after the results. Second, the registered record has wholes without joint
determination (the mutual dyad, the copy ring, the imitation of giving) but no registered case of joint
determination in a system that factors. This addendum fixes the criterion in advance, states what it
predicts on the lab's registered forms, on Simmel's majority, and on two families nobody has read under
it, and lets the results come in against those predictions.

## The criterion (fixed here)

A form shows **joint determination** when, at some reachable state, a first-order distinction — a mechanism
of one element X with φ > 0 — has an irreducible cause purview that contains at least two elements other
than X. It shows **joint determination in a whole** when, in addition, the whole system is irreducible
(Φ_MIP > 0) and X and at least two of those other purview elements lie in the major complex. Full
definitions, the state set and the decision rules are in [`jd_methods.md`](jd_methods.md).

## JD1 — the criterion reads the registered exemplars as the talk says (calibration)

- **Prediction.** Joint determination in a whole in the control (A′ = M, M′ = A ∧ B, B′ = M), in genuine
  giving, and in the pragmatic sign. No joint determination at all in the mutual dyad, the copy ring
  copy_BCA, the branch copy_CCA, the imitation of giving, the dyadically degenerate chain, the monadically
  degenerate form, or the sign with an exogenous object.
- **Null.** At least one form reads otherwise.
- **Lab prior.** The registered maximal distinctions already show M ← AB, R ← GT and I ← OS, and every
  negative form has cause-side adicity 2 (#374–#377). JD1 is a consistency check of the criterion, not a
  test of a new claim.

## JD2 — Simmel's majority: a party jointly determined, in a system that factors

- **Prediction.** In the majority triad (every member's next state is the majority of all three), at least
  one member is jointly determined by the other two, and the system factors (Φ_MIP = 0). In the mutual
  triad (each member is the AND of the other two) and in Simmel's mediator (A′ = A ∧ M, M′ = A ∧ B,
  B′ = B ∧ M), joint determination sits inside a whole.
- **Null.** The majority triad shows no joint determination; or the mutual triad or the mediator does not
  show it inside a whole.
- **Lab prior.** The majority triad is Φ_MIP = 0 with no complex (#371); the mutual triad is Φ = 6.0 and the
  mediator Φ = 2.0 (#369, #372). If JD2 holds, the record gains its missing cell: joint determination and
  wholeness come apart in both directions, not only one.

## JD3 — confirmation on families not read before

- **(a) One-input wirings at n = 5**, one representative per isomorphism class (13 classes).
  - *Prediction:* no joint determination in any class.
  - This is near-definitional. A one-input rule gives each element one cause, so it is registered as a
    calibration of the reader at a size the paper did not reach, not as a finding.
- **(b) A fresh two-input sample**: 30 four-element forms, generated with seed 1 by the paper's own
  `two_input_sample`. The paper's H5 read seed 0.
  - *Prediction:* both cells are non-empty. At least one form shows joint determination in a whole, and at
    least one shows joint determination in a system that factors (Φ_MIP = 0).
  - *Null:* one cell or both are empty.
- **Verdict.**
  - CONFIRMED when (a) holds and both cells in (b) are non-empty.
  - PARTIAL when (a) holds and one cell is non-empty.
  - REFUTED otherwise.

## What this does not test

It does not run IIT 4.0's exclusion (grain) test on a paired re-encoding of the control. That test is the
direct answer to the objection that joint determination depends on treating the parties as units; it is
named here as the open next test. Nothing here concerns people or platforms. The forms are Boolean models.
