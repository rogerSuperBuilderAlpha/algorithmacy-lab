# construct_ladders_n5 — hypotheses (fixed before computing)

**Question.** Do FULL_JOINT_FLIP and COMMIT_READ_BOUNDARY transfer from
the HMC encoding ladder to **CMC** and **AI-MC** literal construct
paths at n=5, or do the boundary steps morph?

**Already known.**
- `encoding_ladder_n5` FULL_JOINT_FLIP: assist grows core; last outer
  party’s commit into S → whole triadic Φ=4 (=n−1), n_core=5.
- `hmc_algo_boundary` COMMIT_READ_BOUNDARY: party ∈ core iff in S’s
  determination ∧ reads S.
- `constructs_n_gt3` SCALE_BLURS_CONSTRUCTS: CMC conveyors stay
  non-commit; AI-MC ≥3-core boundary persists; algo multiparty flips.
- Gate arm: Φ=n−1 holds for monotone AND/OR full-bind
  (MONO_EXTREMAL_VS_AFFINE).

**Universe.** Binary exact IIT-4.0. n=5. Monotone AND/OR at the flip.
Two parallel ladders (minimal edits):
- **CMC** labels `("W","S","C","D","E")` — convey → joint bind.
- **AI-MC** labels `("W","A","C","D","E")` — transform → joint bind
  (A as mediator, then committing rule).

## H1 — CMC classical stays non-algorithmacy

cmc_chain / cmc_echo wholes are dyadic; cores ≤2 (convey). Null: classical
CMC already whole-triadic.

## H2 — AI-MC baseline keeps ≥3-core boundary, whole dyadic

aimc_rewrite has n_core≥3 with whole dyadic (transform boundary). Null:
collapses to ≤2-core, or already whole-triadic.

## H3 — full joint bind flips on both ladders (Φ = n−1)

cmc_full_AND/OR and aimc_full_AND/OR are whole **triadic**, n_core=5,
core Φ = 4. Null: either family fails the flip or Φ ≠ 4.

## H4 — COMMIT_READ transfers on both ladders

A party that reads the mediator but is absent from its determination
stays outside the major complex; dropping a party from the commit
removes them from the core. Null: COMMIT_READ fails on CMC or AI-MC.

## H5 — boundary step transfers (not morphs)

Pre-boundary (all-but-one outer parties bound; last idle) stays dyadic;
the flip is the last outer party’s commit — same form as HMC
`workers_*_Cidle → *_full`. Null: CMC or AI-MC flips earlier or never.
