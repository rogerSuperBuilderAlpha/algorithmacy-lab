# indeg_002122_n6 — hypotheses (fixed before computing)

**Question.** Within n=6 fixed_k=4 omit forms of indeg signature
**(0,0,1,1,2,2)** — a *different* fingerprint from the closed
(0,1,1,1,1,2) band — does cycle type (or recip) still yield a pure
discriminant / band, or does this signature mix / collapse to one Φ?

**Already known.**
- Closed band: indeg (0,1,1,1,1,2) → BAND_DISCRIMINANT (Φ=8 vs 9 by cycle type).
- n=5 cousin indeg (0,0,1,2,2): orbit reps for (2,) and (3,) both Φ=6
  (omit_motif_phi5) — no within-indeg cycle discriminant.
- Arc: [`OMIT_ATOM_ARC.md`](../../OMIT_ATOM_ARC.md). Ternary / residual noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6, fixed_k=4.
Classes: ((2,),1)=2160, ((2,2),2)=540, ((3,),0)=1800, ((4,),0)=1080.
Dense uniformity N_U=3 per class (not full enum; ~45s/cell).

## H1 — cycle-type band / discriminant

At least two distinct core Φ values appear across the four (cycles, recip)
classes, each class Φ-pure, with Φ tracking cycle type. Null: one Φ only,
or impure classes.

## H2 — flat (no cycle discriminant)

All tested forms across all four classes share one common core Φ (and
classes are pure). Null: ≥2 distinct Φ across classes.

## H3 — within-class mix (collapse)

At least one (cycles, recip) class mixes two distinct Φ values in its
uniformity sample. Null: every class is Φ-pure.

## H4 — recip alone does not separate

If ≥2 Φ values appear, they are not separated by recip alone (same recip
appears with both Φ, or one recip maps to multiple Φ). Null: recip alone
is a perfect separator.
