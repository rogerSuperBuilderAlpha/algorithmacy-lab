# Same-indeg Φ=8 vs 9 band at n=6 — findings

**Verdict: BAND_DISCRIMINANT.** Within indeg signature **(0,1,1,1,1,2)** at
n=6 fixed_k=4, **Φ=9 iff cycles ∈ {(5,), (2,3)}**; otherwise **Φ=8**. All six
(cycles, recip) classes are Φ-pure under dense uniformity (N_U=3 each). This
is a **multi-class cycle-type band**, not an n=5-style 3-cycle singleton.
Recip alone and n_core alone do not separate the bands (all n_core=5; recip
0 and 1 each appear in both Φ values).

In-silico; binary exact IIT-4.0; n=6. Hypotheses fixed in `hypotheses.md`.
Extends `omit_lift_n6` LAWS_MORPH; compares to `omit_motif_phi5`
MOTIF_DISCRIMINANT. Ternary / residual-cascade / #42 noted only.

## Already known

| prior | result |
|---|---|
| omit_motif_phi5 | Φ=5 iff (3,)+recip0 at indeg (0,1,1,1,2); siblings → 6 |
| omit_lift_n6 | orbit reps: four classes → 8; two → 9; M3 not unique |
| PHI14_IS_33 | derangement atom separate from this arm |

## Contingency (tested)

| cycles | recip | class size | N_U | Φ | band |
|---|---:|---:|---:|---:|---|
| (2,) | 1 | 720 | 3 | **8** | BAND8 |
| (2,2) | 2 | 360 | 3 | **8** | BAND8 |
| **(3,)** | **0** | **720** | **3** | **8** | BAND8 (M3) |
| (4,) | 0 | 720 | 3 | **8** | BAND8 |
| **(2,3)** | **1** | **600** | **3** | **9** | BAND9 |
| **(5,)** | **0** | **720** | **3** | **9** | BAND9 |

All classes pure; all n_core=5. Designed omit_lift witnesses included.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 cycle-type band 8 vs 9 | **SUPPORTED** |
| H2 within-class mix collapse | **REFUTED** |
| H3 recip or n_core alone | **REFUTED** |
| H4 no 3-cycle singleton analogue | **SUPPORTED** |
| H5 class catalog stable | **SUPPORTED** |

## Reading

**vs n=5.** At n=5 the same-indeg story is a **singleton**: only the 3-cycle
motif yields the lower incomplete Φ. At n=6 the lower incomplete Φ (8) is a
**band** of four cycle types, and the higher (9) is the complementary pair
{(5,), (2,3)}. The discriminant **survives as cycle type**, but **morphs**
from singleton to band — consistent with omit_lift’s “sibling discriminant
fails” (fails as M3-uniqueness; holds as band law).

**Not collapse.** No (cycles, recip) class mixes 8 and 9 in the uniformity
sample. Softness is across classes, not within.

## Limits

N_U=3 per class (not full 3840). Conjunctive AND; one indeg signature only.
~45s/cell; runtime ~15 min. No organization measured.

## Best next experiment

**#42 discriminant scale-blur**, or lift the band law to another indeg
signature / n=7 omit. Skip residual/cascade/ternary.

## Reproduce

```
python org_frontier/studies/same_indeg_band_n6/analyze_band.py
```
(~15 min)
