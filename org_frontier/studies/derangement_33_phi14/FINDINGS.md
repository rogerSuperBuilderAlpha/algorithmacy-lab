# Derangement 3+3 Φ=14 law — findings

**Verdict: PHI14_IS_33.** Among omit-derangements at n=6 fixed_k=4, **Φ=14
iff cycle type 3+3**. Dense sample: 6/40 of the 3+3 class all give full-core
Φ=14; 9 forms from the other three !6 types all give Φ=12 (no Φ=14); thin
non-derangement sample (N=3) also has no Φ=14. Class sizes match
120/90/40/15.

In-silico; binary exact IIT-4.0; n=6. Hypotheses fixed in `hypotheses.md`.
Extends `omit_lift_n6` LAWS_MORPH. Ternary / residual-cascade / #42 noted only.

## Already known

| prior | result |
|---|---|
| omit_lift_n6 | derangements split 12 vs 14; designed 3+3 → 14 |
| interior_ring_pool | L6={4,6,8,9,12,30}; Φ=14 outside landmarks |

## Contingency (tested)

| cycle type | class size | N tested | Φ |
|---|---:|---:|---|
| **(3,3)** | **40** | **6** | **14** (all) |
| (6,) | 120 | 3 | 12 |
| (2,4) | 90 | 3 | 12 |
| (2,2,2) | 15 | 3 | 12 |
| non-derangement | — | 3 | 12 (n_core=4) |

Designed witnesses from omit_lift (both 3+3) included; four additional random
3+3 forms also Φ=14 full-core.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 Φ=14 ⟺ 3+3 among ders | **SUPPORTED** |
| H2 other !6 types hit 14 | **REFUTED** |
| H3 non-ders hit 14 | **REFUTED** (thin N=3) |
| H4 !6 sizes 120/90/40/15 | **SUPPORTED** |
| H5 3+3 uniformity Φ=14 | **SUPPORTED** |

## Reading

**Law.** Under fixed_k=4 omit-derangements, the new atom Φ=14 is the
**double 3-cycle** class. The remaining !6 types share the Φ=12 rung.
Relabeling invariance plus conjugacy (one S6 class per cycle type) makes the
dense sample the right test; full 265 enum is unnecessary for the law once
uniformity holds inside 3+3 and no contamination appears outside.

**Scope.** H3 is only a thin non-derangement check — Φ=14 remains unseen
outside derangements here, but is not exhaustively excluded from all
5⁶−265 non-derangement omits.

## Limits

Dense sample (6+9+3 cells), not full !6. Conjunctive AND; n=6 only;
~45s/cell. No organization measured.

## Best next experiment

**Same-indeg Φ=8 vs 9 band law** at n=6 (omit_lift motif table: which cycle
types share M3’s Φ=8?), or **#42 discriminant scale-blur**. Skip
residual/cascade/ternary.

## Reproduce

```
python org_frontier/studies/derangement_33_phi14/analyze_33.py
```
(~14 min)
