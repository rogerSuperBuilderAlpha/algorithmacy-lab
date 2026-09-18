# Indeg (0,0,1,1,2,2) at n=6 — findings

**Verdict: MIX.** On indeg fingerprint **(0,0,1,1,2,2)** — different from
the closed (0,1,1,1,1,2) band — cycle-type classes are **not Φ-pure**.
Uniformity samples mix **Φ=6** (full-core) and **Φ=12** (n_core=4) inside
((2,2),2) and ((4,),0). Cycle type alone does not yield a clean discriminant
here. The band law is **fingerprint-dependent**.

In-silico; binary exact IIT-4.0; n=6 fixed_k=4. Hypotheses fixed in
`hypotheses.md`. Extends `same_indeg_band_n6` / `OMIT_ATOM_ARC.md`. Ternary /
residual noted only.

## Already known

| prior | result |
|---|---|
| same_indeg_band_n6 | indeg (0,1,1,1,1,2): pure cycle bands 8 vs 9 |
| omit_motif_phi5 | n=5 cousin (0,0,1,2,2): (2,) and (3,) both Φ=6 |

## Contingency (N_U=3)

| cycles | recip | class size | Φ hist | pure? |
|---|---:|---:|---|---|
| (2,) | 1 | 2160 | {6: 3} | yes |
| **(2,2)** | **2** | **540** | **{6: 2, 12: 1}** | **no** |
| (3,) | 0 | 1800 | {6: 3} | yes |
| **(4,)** | **0** | **1080** | **{6: 2, 12: 1}** | **no** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 cycle-type band/discriminant | **REFUTED** |
| H2 flat (one Φ all classes) | **REFUTED** (mix, not flat) |
| H3 within-class mix | **SUPPORTED** |
| H4 recip alone does not separate | **SUPPORTED** (recip 0 and 2 both see 6 and 12) |

## Reading

**Fingerprint-dependent purity.** The closed (0,1,1,1,1,2) band was pure
under (cycles, recip). This denser dual-omitted-hub signature is not. Same
cycle type can land on full-core Φ=6 or incomplete Φ=12. Motif-ruled atoms
still appear as discrete values, but the **class grain** that worked for the
first band is insufficient here.

## Limits

N_U=3 per class (not full 5580). Conjunctive AND. One new indeg only.

## Best next experiment

Finer grain inside impure classes (e.g. core-membership / omit digraph
features beyond cycles), or HMC/CMC/AI-MC at n>3.

## Reproduce

```
python org_frontier/studies/indeg_002122_n6/analyze_indeg.py
```
(~9 min)
