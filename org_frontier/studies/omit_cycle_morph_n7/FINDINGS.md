# Omit cycle-type morph at n=7 — findings

**Verdict: BAND_GRAMMAR_HOLDS.** At n=7 the omit cycle-type discriminant
does **not** morph again. The n=5→n=6 singleton→band shift (V2 #42
`SCALE_MORPHS`) **stabilizes** into a fixed band grammar: class-pure
discrete Φ bands partitioned by cycle type. No singleton return, no
continuum, no within-class purity break.

In-silico; binary exact IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers `RESEARCH_AGENDA_V3` #8. Ternary / residual-cascade / derangement
arm noted only.

## Already known

| prior | result |
|---|---|
| omit_motif_phi5 | n=5: Φ=5 iff (3,)+recip0; siblings → 6 (singleton) |
| same_indeg_band_n6 | n=6: Φ=9 iff {(5,),(2,3)}; else 8; classes pure (band) |
| discriminant_scale_blur (#42) | SCALE_MORPHS — purity holds; law morphs singleton→band |

## n=7 panel (indeg (0,1,1,1,1,1,2), fixed_k=5)

MC catalog: 10 (cycles, recip) classes. Designed witness per class +
N_U=2 uniformity on one class from each Φ band.

| band | cycle-type classes | core Φ | n_core |
|---|---|---:|---:|
| lower | (2,), (2,2), (2,2,2), (2,4), (4,), (6,) | **12** | 6 |
| upper | (2,3), (3,), (3,3), (5,) | **14** | 6 |

Purity: ((2,),1) → Φ=12 (n=2); ((2,3),1) → Φ=14 (n=2).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 class purity at n=7 | **SUPPORTED** |
| H2 discrete cycle-type bands | **SUPPORTED** |
| H3 not n=5-style singleton | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

**#8 morph again at n=7?** No. The separator stays a **cycle-type band
law** with **pure classes**, now at Φ=12 vs Φ=14 (six classes vs four).
That is the same grammar as n=6 (Φ=8 vs 9), lifted one incomplete-core
step — not a new grain, not a singleton return, not a continuum.

**vs V2 #42.** SCALE_MORPHS named the singleton→band form change across
n=5→n=6. At n=7 that form **holds**. Scale still morphs the Φ numbers;
it does not morph the grammar again.

## Limits

One indeg family; conjunctive AND; N_U=2 on two classes; MC catalog not
exhaustive enumeration. Evidence about the model, not a real organization.

## Best next experiment

**V3 #9** (interior atoms at n=7–8) — natural scale companion — or
**V3 #11** (graded×topo on ring/hub/necklace).

## Reproduce

```
python org_frontier/studies/omit_cycle_morph_n7/analyze_morph_n7.py
```
(loads committed census; `--rebuild` recomputes ~12 exact-Φ cells, ~90 min)
