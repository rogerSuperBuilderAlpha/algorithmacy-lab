# omit_cycle_morph_n7 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #8).** Does the omit cycle-type discriminant
**morph again at n=7**, or does the n=5→n=6 singleton→band shift (V2 #42
`SCALE_MORPHS`) **stabilize into a fixed band grammar**?

**Already known (cited, not reopened).**
- **n=5** (`omit_motif_phi5`): within indeg (0,1,1,1,2), Φ=5 iff
  cycles=(3,)+recip0 — **singleton** motif; siblings → Φ=6.
- **n=6** (`same_indeg_band_n6`): within indeg (0,1,1,1,1,2), Φ=9 iff
  cycles∈{(5,),(2,3)}; else Φ=8 — **multi-class band**; classes pure.
- **V2 #42** (`discriminant_scale_blur`): `SCALE_MORPHS` — purity holds;
  law morphs singleton→band; not within-class blur.
- Ternary / residual-cascade / derangement Φ=14 arm noted only.

**Gap.** Whether n=7 keeps the **band grammar** (cycle-type partitions,
class-pure discrete Φ) or morphs again (singleton return, continuum,
purity break, new grain).

**Universe.** Binary exact IIT-4.0. Conjunctive AND. fixed_k=n−2 (one omit
per node). Focal indeg family lift: n=7 → (0,1,1,1,1,1,2).

**Band grammar (stabilizes).** (i) Within each (cycles, recip) class,
uniformity samples share one core Φ (purity). (ii) Distinct classes fall
into a small number of discrete Φ bands partitioned by cycle type. (iii)
Not a singleton motif; not a continuum of Φ values.

**Morphs again.** Purity fails; or Φ sprays with no cycle-type band law;
or the separator reverts to a singleton motif; or a new grain (beyond
cycle type) is required to restore purity.

## H1 — class purity at n=7

On at least two (cycles, recip) classes with N_U≥2, all samples share one
core Φ (within PHI_EPS). Null: some tested class mixes Φ.

## H2 — discrete cycle-type bands (not continuum)

Designed witnesses across the (0,1,1,1,1,1,2) cycle-type catalog yield a
small set of distinct core Φ values (≥2 bands, ≤ half the class count as
unique singletons-per-class with no shared bands). Null: each class a
unique Φ with no multi-class banding, or a near-continuum (≥6 distinct Φ
with no cycle-type grouping).

## H3 — not an n=5-style singleton

No single cycle type is the unique carrier of the lower (or higher)
incomplete-core Φ band; at least two cycle types share a band, or the
lower band has ≥2 classes. Null: exactly one cycle type occupies a
special Φ alone (singleton returns).

## H4 — panel verdict

H1–H3 support band grammar → `BAND_GRAMMAR_HOLDS`.
H1 fails → `PURITY_BREAKS_N7`.
H1 holds but H2/H3 show new form → `MORPHS_AGAIN`.
Controls / catalog fail → `CONTROLS_FAIL`.
