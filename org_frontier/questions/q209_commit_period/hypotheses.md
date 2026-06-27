# Q209 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses, each with its null and predicted outcome, committed before any test runs.

The period-p form **F_p** gates the conjunctive mediator with a mod-p counter: the mediator recomputes
`S'=W∧C` only on the step the counter resets to zero, holding otherwise, while the parties update every
step (`W'=S, C'=S`). F_1 is the synchronous triad (n=3, no counter; triadic, Φ_MIP=2.0). F_2 uses a 1-bit
toggle (n=4, q207's form). F_3 and F_4 use a 2-bit counter (n=5) cycling mod 3 and mod 4. The sweep is
p = 1, 2, 3, 4.

## H1 — Instrument control
- **Claim:** F_1 reads triadic with Φ_MIP = 2.0.
- **H0:** —
- **Predicted outcome:** triadic, max_phi = 2.000000. No comparison number is trusted unless this passes.

## H2 — Synchronous commitment is the unique binding cadence
- **Claim:** F_p reads dyadic at every period p = 2, 3, 4: any slowing of the commit cadence factors the
  triad, so only p=1 binds.
- **H0:** Some period p ≥ 2 keeps F_p triadic.
- **Predicted outcome:** F_2, F_3, F_4 all dyadic.

## H3 — The triad leaves the core at every period
- **Claim:** At every p ≥ 2 the major complex excludes the coordination — {W, S, C} ⊄ core; the surviving
  complex is the counter.
- **H0:** {W, S, C} ⊆ core at some period.
- **Predicted outcome:** for each p ∈ {2,3,4}, the major complex contains no triad member, or contains the
  counter nodes only.

## H4 — The surviving counter's Φ is non-decreasing in period
- **Claim:** The residual integration carried by the gating counter does not fall as the period grows: a
  longer counter cycle carries at least as much Φ. core_Φ(p=2) ≤ core_Φ(p=3) ≤ core_Φ(p=4).
- **H0:** The residual Φ falls with longer period.
- **Predicted outcome:** the core Φ sequence over p = 2, 3, 4 is non-decreasing.

## H5 — Whole-system Φ_MIP is zero at every period ≥ 2
- **Claim:** Once the mediator is slowed at all, the worker, system, and counterpart contribute no
  integration: the whole-system Φ_MIP is 0 at every p ≥ 2, in contrast to q208 where represented latency
  kept it positive.
- **H0:** Whole-system Φ_MIP is positive at some p ≥ 2.
- **Predicted outcome:** max_phi(F_p) reflects only the counter, with the triad contributing zero — read as
  a dyadic verdict at every p ≥ 2.
