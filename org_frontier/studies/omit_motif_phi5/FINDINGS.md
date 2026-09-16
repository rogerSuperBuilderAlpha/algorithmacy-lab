# Omit-motif census Φ=5 vs Φ=6 — findings

**Verdict: MOTIF_DISCRIMINANT.** Among non-derangement fixed_k=3 forms at n=5,
**Φ=5 iff omit motif M**: indeg signature (0,1,1,1,2), a single **3-cycle**, and
recip=0. Same-indeg siblings with other cycle structures all give **Φ=6**. Motif
M has **120** designed witnesses (one S5-orbit); it is not noise.

In-silico; binary exact IIT-4.0; n=5. Hypotheses fixed in `hypotheses.md`.
Extends `fixed_k_atoms_n5` NEW_RUNGS. Ternary / residual-cascade noted only.

## Already known

| prior | result |
|---|---|
| fixed_k_atoms_n5 | Φ=9 = derangement rung; Φ=5 recurs on non-derang 4-cores |
| PARTIAL_N5 | first sightings of atoms 5 and 9 |

## Catalog (10 non-derangement omit classes)

| indeg_sig | cycles | recip | n | Φ | n_core |
|---|---|---:|---:|---:|---:|
| (0,0,1,2,2) | (2,) | 1 | 180 | 6 | 3 |
| (0,0,1,1,3) | (2,) | 1 | 120 | 6 | 3 |
| (0,0,1,2,2) | (3,) | 0 | 120 | 6 | 3 |
| (0,1,1,1,2) | (2,) | 1 | 120 | 6 | 3 |
| **(0,1,1,1,2)** | **(3,)** | **0** | **120** | **5** | **4** |
| (0,1,1,1,2) | (4,) | 0 | 120 | 6 | 3 |
| (0,0,0,2,3) | (2,) | 1 | 60 | 6 | 3 |
| (0,0,1,1,3) | (3,) | 0 | 60 | 6 | 3 |
| (0,1,1,1,2) | (2,2) | 2 | 60 | 6 | 3 |
| (0,0,0,1,4) | (2,) | 1 | 20 | 12 | 4 |

Motif M uniformity sample N=12: all Φ=5, all n_core=4. Derangement control: Φ=9.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 motif M → Φ=5, n_core=4 | **SUPPORTED** |
| H2 no other nonder class → Φ=5 | **SUPPORTED** |
| H3 same-indeg siblings → Φ=6 | **SUPPORTED** (3 siblings) |
| H4 Φ=5 exactly motif M | **SUPPORTED** |
| H5 designed witness \|M\|=120 | **SUPPORTED** |

## Reading

**Discriminant.** Within the non-derangement world, Φ=5 vs Φ=6 is decided by
the omit digraph’s **cycle type** once the indegree signature is
(0,1,1,1,2): a lone **3-cycle** (motif M) → Φ=5 with a 4-node major complex;
a 2-cycle, double 2-cycle, or 4-cycle → Φ=6 with a 3-node complex. Other
indeg signatures never produce Φ=5 (they yield 6 or 12).

**Not noise.** Motif M is a full conjugacy class of 120 omit functions. The
PARTIAL_N5 “outliers” were the first draws from this class.

**Alongside Φ=9.** Derangements remain the Φ=9 rung; motif M is the Φ=5 rung
for non-derangements. Together they exhaust the “new atoms” from the n=5
random ensemble under fixed_k=3.

## Limits

Orbit-representative evaluation plus M uniformity sample (not full 980 exact-Φ
evals). Relabeling invariance of Φ under S5 is used. Conjunctive AND; n=5
only. No organization measured.

## Best next experiment

**Done next:** `omit_lift_n6/` — **LAWS_MORPH**: derangements split 12 vs 14
(3+3); M3 incomplete-core persists but sibling discriminant fails; Φ=14 new
vs L6. Follow-on: derangement 3+3 law among !6, or #42 scale-blur.

## Reproduce

```
python org_frontier/studies/omit_motif_phi5/analyze_motifs.py
```
(~2 min)
