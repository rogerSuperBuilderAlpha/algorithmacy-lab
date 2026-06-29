# Q213 — Stage 3 hypotheses (fixed before computation)

The instrument is the bypass-counterfactual, implemented in `classifier/contingency.py`: take a party in a
triad's core, restore the forbidden direct edge between the two parties it sits between, recompute the major
complex, and read whether the party survives. The contingency margin is the whole-system Φ_MIP lost when the
bypass opens. The four-way taxonomy: contingent (party leaves), intrinsic (stays, margin ≈ 0), partial
(stays, 0 < margin), reducible (not in core to begin with).

Four constructed forms instantiate the categories. Node order and rules are fixed here before the probe runs.

- **Conjunctive clearinghouse** (intrinsic), labels (W, S, C): W'=S, S'=W∧C, C'=S. Bypass: C reads W directly
  instead of S (disintermediation).
- **Car dealer** (contingent), labels (M, D, B): M'=B, D'=M, B'=D — the dealer relays, the buyer is bound by
  franchise law to source through the dealer. Bypass: the maker sells direct, B'=M (disintermediation).
- **Clearinghouse with a back-channel** (partial), labels (W, S, C): W'=S, S'=W∧C, C'=S. Bypass: a parallel
  channel is opened, C'=S∨W (the back-channel runs alongside the mediator, not replacing it).
- **Free conduit** (reducible), labels (M, D, B): M'=B, D'=M, B'=M — the same relay dealer with no constraint,
  the buyer already sourcing direct.

## H1 — instrument control

The conjunctive triad reads triadic at Φ=2.0.
- **H0:** the control does not reproduce the triad's known value.
- **Predicted outcome:** triadic, Φ_MIP = 2.000000.

## H2 — a conduit is irreducible under constraint

The car-dealer relay triad, with the buyer bound to the dealer, is irreducible with the dealer in the core,
even though the dealer integrates nothing.
- **H0:** the relay conduit factors; the dealer is not in the core.
- **Predicted outcome:** constrained car dealer triadic at Φ_MIP=2.0, core contains D.

## H3 — the bypass-counterfactual removes the contingent party

Restoring the bypass (the maker sells direct) disintermediates the dealer: it leaves the core and the triad
collapses to a dyad. The classifier labels the dealer "contingent" with margin = full Φ.
- **H0:** the dealer stays in the core under the bypass (its role is not contingent on the constraint).
- **Predicted outcome:** kind="contingent"; D not in core under bypass; whole-system dyadic; margin = 2.0.

## H4 — the same test leaves an intrinsic mediator in place

Under the same disintermediating bypass, the conjunctive mediator stays in the core: the direct edge cannot
reproduce its joint condition. The classifier labels it "intrinsic" with margin ≈ 0. The test discriminates
the two.
- **H0:** the conjunctive mediator also leaves the core under the bypass (the test cannot tell them apart).
- **Predicted outcome:** kind="intrinsic"; S in core under bypass; margin = 0.0.

## H5 — the four-way taxonomy is realized and the margin orders it

The partial form (clearinghouse with a parallel back-channel) classifies "partial": the mediator stays in the
core but the system sheds integration, 0 < margin < full. The free-conduit form classifies "reducible": the
dealer is not in the core to begin with. The contingency margin orders the cases contingent ≥ partial >
intrinsic ≈ reducible.
- **H0:** the partial or reducible case is mislabeled, or the margins do not order as stated.
- **Predicted outcome:** kind="partial" with 0 < margin < 2.0; kind="reducible" with D not in core; margins
  contingent (2.0) ≥ partial (≈1.585) > intrinsic (0.0).
