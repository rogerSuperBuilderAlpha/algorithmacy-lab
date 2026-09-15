# Omit/derangement lift at n=6 — findings

**Verdict: LAWS_MORPH.** The n=5 omit laws do not copy forward. At n=6
fixed_k=4, **derangements split** into Φ=12 (cycle types 6, 4+2, 2+2+2) and
**Φ=14** (cycle type **3+3**) — not a single rung. Motif M3 (indeg
(0,1,1,1,1,2)+3-cycle+recip=0) still yields a stable **incomplete core**
(Φ=8, n_core=5), but the n=5 sibling discriminant **fails**: three of five
same-indeg siblings also give Φ=8; the other two give Φ=9. **Φ=14** is a new
atom outside the designed L6 landmarks.

In-silico; binary exact IIT-4.0; n=6. Hypotheses fixed in `hypotheses.md`.
Extends `fixed_k_atoms_n5` NEW_RUNGS and `omit_motif_phi5` MOTIF_DISCRIMINANT.
Ternary / residual-cascade noted only.

## Already known

| prior | result |
|---|---|
| fixed_k_atoms_n5 | Φ=9 = all 44 derangement omits; Φ=5 recurs on non-derang 4-cores |
| omit_motif_phi5 | Φ=5 iff motif M (indeg+(3,)+recip0); siblings → Φ=6 |
| interior_ring_pool | L6 full-core steps {4,6,8,9,12,30} |

## Derangement spectrum

| cycle type | N tested | core Φ | n_core |
|---|---:|---:|---:|
| (6,) | 2 designed+random | **12** | 6 |
| (2,4) | 2 | **12** | 6 |
| (2,2,2) | 1 | **12** | 6 |
| **(3,3)** | **2** | **14** | **6** |

H1 single rung: **REFUTED**. H2 cycle-type split: **SUPPORTED** (3+3 alone
at 14; others at 12). Both full-core triadic.

## Same-indeg motif → Φ (indeg (0,1,1,1,1,2))

| cycles | recip | class size | Φ | n_core | role |
|---|---:|---:|---:|---:|---|
| **(3,)** | **0** | **720** | **8** | **5** | **M3** |
| (2,) | 1 | 720 | 8 | 5 | sibling |
| (2,2) | 2 | 360 | 8 | 5 | sibling |
| (4,) | 0 | 720 | 8 | 5 | sibling |
| (2,3) | 1 | 600 | **9** | 5 | sibling |
| (5,) | 0 | 720 | **9** | 5 | sibling |

H3 M3 incomplete-core uniform: **SUPPORTED** (designed + alternate both
Φ=8, n_core=5). H4 sibling discriminant fails: **SUPPORTED** (3/5 siblings
match M3’s Φ — not the clean 5-vs-6 split).

## New atoms vs L6

Distinct Φ in this census: {8, 9, 12, **14**}. Outside L6={4,6,8,9,12,30}:
**Φ=14** only. H5: **SUPPORTED**. Φ=8 and Φ=9 sit on known landmarks but
here as **incomplete** 5-cores (M3-band / sibling-band), not the full-core
mh2/chord designs.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 single derangement rung | **REFUTED** |
| H2 3+3 differs from other cycle types | **SUPPORTED** |
| H3 M3 incomplete-core, uniform Φ | **SUPPORTED** |
| H4 sibling discriminant fails | **SUPPORTED** |
| H5 new atom outside L6 | **SUPPORTED** |

## Reading

**Morph, not copy.** n=5’s “derangement ⇒ Φ=9” becomes “derangement ⇒
{12,14} by cycle type,” with **double 3-cycles** as the higher rung.
n=5’s “3-cycle motif ⇒ unique incomplete Φ” becomes “indeg (0,1,1,1,1,2)
⇒ incomplete Φ ∈ {8,9},” with M3 inside a **band** of cycle types at 8,
not a singleton discriminant. No continuum: four discrete values, one of
them (14) new relative to designed landmarks.

## Limits

Designed cycle-type witnesses + N=2 random derangements (!6=265 not fully
enumerated). Same-indeg class: one orbit rep per (cycles, recip) key.
Conjunctive AND; n=6 only; ~45s/cell. No organization measured.

## Best next experiment

**Derangement 3+3 law** — is Φ=14 exactly the double-3-cycle class among
all !6, or do other types join? Thin full derangement sample by cycle type.
Else **#42 discriminant scale-blur**. Skip residual/cascade/ternary.

## Reproduce

```
python org_frontier/studies/omit_lift_n6/analyze_lift.py
```
(~11 min)
