# construct_ladders_n6 — hypotheses (fixed before computing)

**Question.** At n=6, do HMC / CMC / AI-MC construct ladders still flip
at `pre_AND → full_AND` with Φ = n−1 (=5), or does some family morph?

**Already known.**
- `construct_ladders_n5` BOUNDARY_TRANSFERS: CMC and AI-MC share HMC’s
  last-party commit flip (Φ=4) and COMMIT_READ at n=5.
- `encoding_ladder_n6` PHI_TRACKS_NM1: HMC-style ladder at n=6 flips with
  Φ=5 (=n−1); boundary form unchanged.
- Gate arm: monotone AND/OR full-bind tracks n−1
  (MONO_EXTREMAL_VS_AFFINE / RULE_HOLDS_PANEL).

**Universe.** Binary exact IIT-4.0. n=6. Monotone AND/OR at the flip.
Trimmed ladders (candid about N; full-bind ~40 s/cell):
baseline → pre_AND → last_reads → full_AND/OR → drop_last_ro.
Families: HMC `("W1","S","W2","W3","W4","C")`; CMC
`("W","S","C","D","E","F")`; AI-MC `("W","A","C","D","E","F")`.

## H1 — all three families PHI_TRACKS_NM1 at n=6

For HMC, CMC, and AI-MC: pre_AND is dyadic with n_core=5; full_AND and
full_OR are whole triadic, n_core=6, core Φ = 5. Null: some family fails
the flip or has Φ ≠ 5.

## H2 — some family morphs

At least one family flips earlier than pre→full, never flips, or lands
on Φ ≠ n−1. Null: all three match H1.

## H3 — COMMIT_READ breaks

On some family, the last party enters the core by read-without-commit,
or survives a drop-from-commit while still reading. Null: COMMIT_READ
holds on all three (last out on reads-only and on drop).
