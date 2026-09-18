# Discriminant scale-blur (#42) — findings

**Verdict: SCALE_MORPHS.** Scale does **not** blur the omit cycle-type
discriminant into within-class Φ mixing. Class purity holds at n=5 and n=6.
What changes with n is the **form** of the law: a **singleton** motif at n=5
(MOTIF_DISCRIMINANT) becomes a **multi-class band** at n=6
(BAND_DISCRIMINANT). Not copy, not collapse — morph.

In-silico; binary exact IIT-4.0. Hypotheses fixed in `hypotheses.md`. Answers
`RESEARCH_AGENDA_50_V2` #42 on the omit cycle-type discriminant. Ternary /
residual-cascade noted only. HMC/CMC/AI-MC at n>3 remains a parallel open arm.

## Already known

| prior | result |
|---|---|
| omit_motif_phi5 | Φ=5 iff (3,)+recip0; siblings orbit-rep → 6 |
| same_indeg_band_n6 | Φ=9 iff {(5,),(2,3)}; else 8; classes pure N_U=3 |
| PHI14_IS_33 / omit_lift | derangement thread closed; separate atom |

## Purity across scale

| n | class grain | N tested | pure? | Φ law |
|---|---|---|---|---|
| 5 | (3,)+recip0 (M) | 13 committed | **yes** | → 5 |
| 5 | siblings (2,), (2,2), (4,) | **3×3 new** | **yes** | → 6 |
| 6 | six (cyc,recip) classes | 3 each committed | **yes** | 8 vs 9 band |

New denser n=5 sibling sample closes the single-orbit-rep gap: all three
sibling classes stay Φ=6 (n_core=3).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 class purity holds across n | **SUPPORTED** |
| H2 purity collapses / mixes at scale | **REFUTED** |
| H3 morphs into coarser band | **SUPPORTED** |
| H4 n=5 singleton not verbatim at n=6 | **SUPPORTED** |
| H5 denser n=5 siblings pure Φ=6 | **SUPPORTED** |

## Reading

**#42 scale-blur?** No. Blur would be the same motif class yielding mixed Φ
as n grows. That does not happen here. The discriminant **survives as cycle
type** with **pure classes**, and **morphs** from “one special cycle” to “a
partition of cycle types into bands.”

**vs agenda HMC/CMC/AI-MC.** This closes the scale-blur reading on the omit
atom separator. Construct discriminants (HMC/CMC/AI-MC) at n>3 are still open.

## Limits

Reuses committed n=6 N_U=3 (no recompute). New compute is n=5 siblings only.
One indeg family per n. Conjunctive AND. No organization measured.

## Best next experiment

**HMC/CMC/AI-MC at n>3** (literal agenda #42 construct arm), or another indeg
signature band at n=6. Skip residual/cascade/ternary.

## Reproduce

```
python org_frontier/studies/discriminant_scale_blur/analyze_blur.py
```
(~1 min; reads committed n=5/n=6 CSVs + 9 new n=5 cells)
