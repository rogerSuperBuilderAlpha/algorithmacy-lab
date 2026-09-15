# Fixed-k atoms 5/9 at n=5 — findings

**Verdict: NEW_RUNGS.** Atom **Φ=9** is a clean **derangement rung**: all 44
omit-derangements at fixed_k=3 give full-core triadic Φ=9.0. Atom **Φ=5** is a
**recurring non-derangement** form (6/48 in the denser sample), always with an
**incomplete 4-node core**. No continuum — denser fixed_k=3 only hits
{5, 6, 9, 12}.

In-silico; binary exact IIT-4.0; n=5. Hypotheses fixed in `hypotheses.md`.
Extends `random_coupling_ensemble` PARTIAL_N5; cites `interior_ring_pool` L5.
Ternary / residual-cascade noted only.

## Already known

| prior | result |
|---|---|
| n=4 ensemble | all Φ ∈ {2,4,6,12} |
| n=5 ensemble N=92 | 95.7% on L5; off-atoms 5 (×3) and 9 (×1), all fixed_k=3 |
| outlier reconstruction | Φ=9 omit = derangement; Φ=5 omit non-bijective, 4-core |

## Census

### Derangement omits (fixed_k=3) — full enum !5 = 44

| Φ | count | core |
|---:|---:|---|
| **9.0** | **44/44** | full 5, triadic |

### Non-derangement fixed_k=3 — N=48

| Φ | count | note |
|---:|---:|---|
| 6.0 | 40 | L5 interior atom |
| **5.0** | **6** | all n_core=4 |
| 12.0 | 2 | incomplete-pool-like |
| 9.0 | **0** | derangement-only |

### fixed_k=2 contrast — N=24

| Φ | count |
|---:|---:|
| 2.0 | 23 |
| 4.0 | 1 |

on_L5∪{5,9}=1.0; no Φ=9.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 all derangements Φ=9 full-core | **SUPPORTED** |
| H2 no Φ=9 in non-derangement | **SUPPORTED** |
| H3 Φ=5 recurs, incomplete core | **SUPPORTED** (6×, all n_core=4) |
| H4 no continuum; atoms ⊆ L5∪{5,9} | **SUPPORTED** |
| H5 k=2 on known atoms, no Φ=9 | **SUPPORTED** |

## Reading

**Outlier?** No — both atoms reproduce under denser sampling.

**Continuum?** No — only four distinct Φ values under denser k=3.

**New discrete rungs?** Yes.
- **Φ=9** = structural law: fixed_k=3 + **omit derangement** (each node omits a
  unique other). Designed witness: all 44 derangements.
- **Φ=5** = recurring incomplete-core atom on non-derangement omits (~12.5% of
  the N=48 sample). Not a full-system rung; the major complex sheds one node.

The n=5 PARTIAL_N5 “new atoms” were the first sightings of these rungs, not
noise.

## Limits

n=5 only; non-derangement arm is a sample (N=48), not a full 4⁵−44 enum.
Conjunctive AND. No organization measured. Runtime ~11.5 min.

## Best next experiment

**Done next:** `omit_motif_phi5/` — **MOTIF_DISCRIMINANT**: Φ=5 iff omit motif
M (indeg (0,1,1,1,2) + 3-cycle + recip=0); siblings → Φ=6. Then
`omit_lift_n6/` **LAWS_MORPH**. Follow-on: 3+3 law among !6, or #42 scale-blur.

## Reproduce

```
python org_frontier/studies/fixed_k_atoms_n5/analyze_atoms.py
```
(~11.5 min)
