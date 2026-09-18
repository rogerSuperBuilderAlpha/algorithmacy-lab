# same_indeg_band_n6 — hypotheses (fixed before computing)

**Question.** Within n=6 fixed_k=4 omit forms of indeg signature
**(0,1,1,1,1,2)**, what cleanly separates **Φ=8** from **Φ=9**? Is there a
true n=5-style singleton motif, or only a soft multi-class band?

**Already known.**
- **n=5 MOTIF_DISCRIMINANT:** same indeg (0,1,1,1,2); Φ=5 iff cycles=(3,) ∧
  recip=0; all same-indeg siblings → Φ=6.
- **omit_lift_n6 LAWS_MORPH:** orbit reps of six (cycles, recip) classes —
  {(3,),0}, {(2,),1}, {(2,2),2}, {(4,),0} → Φ=8; {(2,3),1}, {(5,),0} → Φ=9;
  all n_core=5. Sibling discriminant vs M3 alone **fails** (3/5 siblings also 8).
- **PHI14_IS_33:** derangement atom separate; not this arm.
- Ternary / residual-cascade / #42 noted only.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n=6, fixed_k=4. Same-indeg
universe size 3840, partitioned into 6 (cycles, recip) classes (sizes
720/720/360/720/600/720). Dense uniformity: N_U per class (designed witness +
random), not full enum (~45s/cell).

**Proposed band law (to test).** Φ=9 iff cycles ∈ {(5,), (2,3)}; else Φ=8
(within this indeg). Not a 3-cycle singleton.

## H1 — cycle-type band discriminates 8 vs 9

Every tested form in BAND8 = {(3,), (2,), (2,2), (4,)} has Φ=8, and every
tested form in BAND9 = {(2,3), (5,)} has Φ=9 (uniform within class). Null:
some class breaks the band assignment.

## H2 — discriminant collapses (within-class mix)

At least one (cycles, recip) class has both Φ=8 and Φ=9 among its uniformity
sample. Null: every class is Φ-pure.

## H3 — 8 vs 9 tracks recip alone or n_core alone

Either (a) recip alone separates 8 from 9 across classes, or (b) n_core differs
between Φ=8 and Φ=9 forms. Null: recip values appear in both bands and all
forms share n_core=5.

## H4 — no n=5-style 3-cycle singleton analogue

Φ=8 is **not** unique to cycles=(3,) ∧ recip=0: at least one other same-indeg
class also yields Φ=8. (Already suggested by omit_lift; reconfirmed here.)
Null: only M3 gives Φ=8.

## H5 — class catalog stable

The six classes and sizes match omit_lift
{((2,),1):720, ((2,2),2):360, ((2,3),1):600, ((3,),0):720, ((4,),0):720,
((5,),0):720}.
