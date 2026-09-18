# discriminant_scale_blur — hypotheses (fixed before computing)

**Question (#42).** Do the cycle-type / omit discriminants that separate nearby
Φ atoms stay sharp as n grows, or does scale blur them (same motif class
mixing Φ; purity collapsing)?

**Agenda note.** `RESEARCH_AGENDA_50_V2` #42 names “HMC / CMC / AI-MC
discriminants (#15, #19, #20).” Those probe-level construct discriminants at
n=3 are already mapped (`discriminant_boundaries`, probes 15/19/20). This
study answers the **scale-blur** reading of #42 on the omit cycle-type
discriminant just closed at n=5/6 — the sharpest scale-comparable separator
the queue produced. HMC/CMC/AI-MC at n>3 remains a parallel open arm.

**Already known.**
- **n=5 MOTIF_DISCRIMINANT:** same indeg (0,1,1,1,2); Φ=5 iff (3,)+recip0
  (N=12 pure); sibling orbit reps → Φ=6 (one each; purity weakly tested).
- **n=6 BAND_DISCRIMINANT:** same indeg (0,1,1,1,1,2); Φ=9 iff
  cycles∈{(5,),(2,3)}; else Φ=8; six classes pure at N_U=3; multi-class band.
- **omit_lift / PHI14_IS_33:** derangement atom separate; noted only.
- Ternary / residual-cascade noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. Minimal honest scale
comparison: **reuse** committed n=5/n=6 purity tables; **new** denser n=5
same-indeg sibling uniformity (N_U=3 × 3 sibling classes) — the purity gap
at n=5. No full n=6 recompute (~15 min already registered).

## H1 — class purity holds across n

Within each (cycles, recip) class at n=5 (same-indeg) and n=6 (same-indeg),
uniformity samples are Φ-pure (one Φ per class). Null: some class mixes.

## H2 — purity collapses / same motif mixes Φ at larger n

At n=6, at least one (cycles, recip) class mixes Φ=8 and Φ=9 (or n=5 sibling
classes mix under denser sample). Null: no within-class mixing at either n.

## H3 — discriminant morphs into a coarser band

The n=5 law is a **singleton** motif (only (3,)+recip0 → lower Φ); the n=6
law is a **multi-class band** (four cycle types → Φ=8; two → Φ=9). Null:
the same singleton form persists at n=6.

## H4 — n=5 singleton does not hold verbatim at n=6

At n=6, Φ=8 is not unique to cycles=(3,) ∧ recip=0. Null: only M3 gives Φ=8.

## H5 — denser n=5 siblings stay pure Φ=6

New N_U=3 samples of each n=5 same-indeg sibling class of motif M are all
Φ=6 (closing the single-orbit-rep gap). Null: some sibling sample ≠ 6.
