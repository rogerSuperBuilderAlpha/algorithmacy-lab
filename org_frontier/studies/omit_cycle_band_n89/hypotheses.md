# omit_cycle_band_n89 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #8).** Does V3 #8’s **band grammar** at
n=7 (indeg `(0,1,1,1,1,1,2)`) still hold at **n=8–9**, or does a new
morph appear once more cycle types fit?

**Already known (cited, not reopened).**
- n=5 (`omit_motif_phi5`): singleton — Φ=5 iff cycles=`(3,)`+recip0.
- n=6 (`same_indeg_band_n6`): multi-class band — Φ=9 iff
  `{(5,),(2,3)}`; else Φ=8; classes pure.
- n=7 (`omit_cycle_morph_n7`): **BAND_GRAMMAR_HOLDS** — lower Φ=12 on
  six cycle types; upper Φ=14 on four; class-pure; no singleton return.
- V2 #42 `SCALE_MORPHS`: singleton→band across n=5→n=6; n=7 stabilized
  the grammar.

**Gap.** Whether the cycle-type → discrete Φ-band grammar survives the
indeg lift to n=8 `(0,1,…,1,2)` and n=9, or morphs again (purity break,
continuum, singleton return, new grain) once longer cycles fit.

**Universe.** Exact binary IIT-4.0. Conjunctive AND omit family
(`fixed_k = n−2`). Indeg lifts: n=8 → `(0,1,1,1,1,1,1,2)`; n=9 →
`(0,1,1,1,1,1,1,1,2)`.

**Scope (lean panel).** Full designed+uniformity census at n=8–9 is
expected to be intractable (n=7 cells were 7–24 min; n=8
`maximal_complex` on dense states exceeds session budget). Primary
exact-Φ probe: micro panel of designed cycle-type witnesses at n=8 on
the all-1 state (where sparse-state Φ is null). Combinatorial MC
catalogs at n=7/8/9 document how many cycle types fit. n=7 committed
census is the control.

**Band grammar (holds).** (i) Class purity within (cycles, recip).
(ii) Distinct classes fall into a small number of discrete Φ bands
partitioned by cycle type. (iii) Not a singleton motif.

**Morphs again.** Purity fails; Φ continuum; singleton return; or a new
grain beyond cycle type is required.

## H1 — n=7 control replicates BAND_GRAMMAR_HOLDS

Committed n=7 census remains two-band class-pure (Φ∈{12,14}). Null:
control broken.

## H2 — more cycle types fit at n=8–9

MC catalog under the indeg lift yields strictly more (cycles, recip)
classes at n=8 than n=7, and at n=9 than n=8. Null: class count does not
grow.

## H3 — exact-Φ micro panel at n=8 is adjudicable

Designed n=8 witnesses spanning predicted lower/upper cycle types yield
finite exact core Φ (all-1 major complex) within the compute budget.
Null: decisive states time out / return only null Φ → scale blocks
exact adjudication.

## H4 — band grammar holds at n=8 (conditional on H3)

Given H3, n=8 exact Φ forms ≥2 discrete cycle-type bands with no
singleton-only special Φ. Null: morph / purity break / continuum.

## H5 — n=9 (conditional)

If H3 holds and budget remains, at least one n=9 witness is finite and
consistent with the n=8 band reading. Null: skipped for scope / timeout.

## Reading keys

- **BAND_GRAMMAR_HOLDS:** H1 ∧ H2 ∧ H3 ∧ H4 — grammar survives; more
  cycle types fit into the same band form.
- **MORPHS_AGAIN:** H1 ∧ H2 ∧ H3 ∧ ¬H4 — exact Φ shows a new form.
- **SCALE_BLOCKS_EXACT_PHI:** H1 ∧ H2 ∧ ¬H3 — cycle-type domain expands
  but exact core-Φ band adjudication is blocked at n=8–9 under the lab
  stack; n=7 grammar unrebutted.
- **CONTROLS_FAIL:** ¬H1.
