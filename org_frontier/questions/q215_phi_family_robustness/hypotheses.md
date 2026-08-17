# Q215 — Stage 3 hypotheses (fixed before computation)

**Question.** Are the OT-manuscript headline verdicts sign-robust across the Φ family — specifically
between IIT 4.0's system measure (`pyphi.new_big_phi`, the lab's standard instrument) and IIT 3.0's
big-Φ (`pyphi.compute.sia`), computed on identical TPMs at identical reachable states? The manuscript
(`submissions/proposals/ot_configurational_nature_2027_manuscript.md`) currently claims verdicts only
for the 4.0 operationalization; three review seats (Fable 01, 05, 06) demand either sign-robustness
or explicit scoping. This question answers empirically which of the two the manuscript can say.

A verdict is the sign of the maximum whole-system Φ over reachable states: Φ > 0 (binds) vs Φ = 0
(factors). Sign-robust means both arms agree on that sign. Magnitudes are expected to differ and are
not at issue.

## H1 — the extremes-only quorum law is measure-robust
- **Claim:** the 3-party quorum binds at k=1 and k=3 and factors at k=2 under both IIT 4.0 and
  IIT 3.0.
- **H0:** at least one threshold flips sign between measures; the interior-threshold collapse is an
  artifact of the 4.0 partition scheme.
- **Predicted outcome:** Φ>0 / Φ=0 / Φ>0 across k=1,2,3, identically in both arms.

## H2 — the rotation binds in both measures
- **Claim:** the four-node directed copy cycle (atlas B10) has Φ > 0 under both measures.
- **H0:** IIT 3.0 reads the pure permutation as reducible (Φ = 0); the "rotation binds" exhibit is
  4.0-specific.
- **Predicted outcome:** Φ > 0 in both arms.

## H3 — synchronization factoring is measure-robust
- **Claim:** the one-sided veto (atlas D1: W′=S, S′=W∧¬C, C′=S), which factors under 4.0 because the
  dynamics drive W and C into lockstep, also factors under 3.0.
- **H0:** 3.0's partition family scores the bidirectional wiring as Φ > 0; the synchronization
  exhibit is 4.0-specific.
- **Predicted outcome:** Φ = 0 in both arms.

## H4 — the dispatch pair is measure-robust in both directions
- **Claim:** the dispatch triad (W′=¬S, S′=W∧C, C′=C∧¬S) has Φ > 0 and its rider-dropped variant
  (S′=W) has Φ = 0, under both measures.
- **H0:** either the full triad factors or the dyadic variant binds under 3.0.
- **Predicted outcome:** Φ > 0 (full) and Φ = 0 (dropped) in both arms.

## H5 — maximal wiring factors in both measures
- **Claim:** the maximally-wired non-degenerate triad (W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S); all six
  directed edges, no constant rule) has Φ = 0 at every reachable state under both measures.
- **H0:** 3.0 assigns Φ > 0 at some reachable state; "density is not constitution" is 4.0-specific.
- **Predicted outcome:** Φ = 0 at every reachable state, in both arms.

## Instrument controls (must pass in BOTH arms before any hypothesis is read)
- **Irreducible control:** the read-recipient triad (E′=M, M′=E∧R, R′=M), the manuscript's worked
  example; established Φ = 2.0 under 4.0 (q111, q210). Must read Φ > 0 in both arms.
- **Factoring control:** two disjoint copy dyads (atlas B5: A↔B, C↔D). Must read Φ = 0 in both arms
  (the MIP across the disconnect severs nothing).

If either control fails in the 3.0 arm, the arm is mis-configured and no comparison is reported.
