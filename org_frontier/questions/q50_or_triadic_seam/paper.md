# Q50 — Party-read structure for OR triadic binding at the edge floor

## Question

What party-read structure lets an OR-labelled strict-mediation triad bind irreducibly (Φ=2.0) at the
four-edge floor, while otherwise-similar OR forms collapse to a dyad?

## Background

Probe #148 (Q45) found that two of sixteen OR-commit strict-mediation forms bind triadically at Φ=2.0
(W1_S7_C1, W2_S7_C2) while fourteen collapse to dyadic. All sixteen share S'=W∨C and exactly four causal
edges (#145). Probe #7 established that OR determinations can bind irreducibly when the mediator reads
both parties; probe #2 showed redundant OR readings drop non-pivotal dimensions. The open question is which
party reads of S restore the pivotality OR needs at the strict-mediation topology.

## Methods

Five hypotheses were fixed before computation (commit `7f03205`). Each probe asserts the instrument control
first: canonical triad W'=S, S'=W∧C, C'=S reads triadic, max_phi=2.0, MIP `2 parts: {W,SC}`. The
ensemble is the 256-form strict-mediation family (`enumerate_family`) with party-read indices decoded from
family labels. H4 reads the MIP tie seam set via PyPhi `sia.ties`. H5 tests all sixteen monotone forms at
Φ=2.0 from Q45 (#146).

## Results

**H1 (matched reads).** An OR form is triadic if and only if the worker and counterpart use the same
non-constant one-input read of S (W-index = C-index ∈ {1, 2}). Exactly two of sixteen OR forms satisfy
this: W1_S7_C1 (both identity: W'=S, C'=S) and W2_S7_C2 (both NOT: W'=¬S, C'=¬S). Zero false positives
or negatives.

**H2 (constant reads).** Twelve of sixteen OR forms have at least one constant party read (W-index or
C-index in {0, 3}). None is triadic. Constant reads decouple a party from S and block OR binding.

**H3 (asymmetric reads).** Twelve of sixteen OR forms have mismatched party-read indices (iw ≠ ic). None
is triadic. Identity-on-worker with NOT-on-counterpart (or the reverse) collapses OR to dyadic even though
both parties remain live.

**H4 (seam tie).** Both binding OR forms read triadic at max_phi=2.0 with seam set {W, C}, matching the
canonical conjunctive triad. OR binding at the floor carries the same W/C-symmetric seam tie Q49 documented
(#140–#141).

**H5 (commit symmetry).** Among sixteen monotone Φ=2.0 forms, eight symmetric commits (AND, OR, NOR, NAND)
all bind with matched reads (iw = ic ∈ {1, 2}). Eight implication commits (S-indices 2, 4, 11, 13) all bind
with complementary reads ({iw, ic} = {1, 2}, iw ≠ ic). Zero cross-rule violations. The party-read rule is
commit-class-specific: commutative mediator functions need phase-aligned party reads; non-commutative
implications need anti-aligned reads.

## Discussion

The fourteen dyadic OR forms fail for three separable reasons: constant reads (twelve forms affected),
asymmetric live reads (twelve forms), or both. The binding pair are the only OR forms where both parties
track S with the same polarity. That restores balanced pivotality (#16) for an either-forces commit: both
parties can change S' given the other, and both read S back, closing the four-edge feedback cycle (#39).

The commit-symmetry split (H5) explains why Q45 found fourteen non-AND monotone forms at Φ=2.0 (#146):
OR, NOR, NAND share the matched-read rule with AND, while implication variants occupy the complementary
anti-diagonal. OR is not special among symmetric commits; it is special only in how rarely the matched-read
condition is met (2/16 OR party-read combinations versus 2/16 for each symmetric commit class).

## Validation gap

These results hold for n=3 deterministic Boolean strict-mediation forms under synchronous update. Real
organizations may use richer party policies, timing, and mediator functions. The party-read indices map to
one-input truth tables; more complex reads were not tested.

## Conclusion

OR triadic binding at the four-edge floor requires matched non-constant party reads of S. Constant reads
and asymmetric identity/NOT pairings collapse OR to dyadic. Symmetric monotone commits (AND, OR, NOR, NAND)
share the matched-read rule; implication commits require complementary reads instead.
