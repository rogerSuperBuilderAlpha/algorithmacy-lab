# Role-target grain on indeg (0,0,1,1,1,3) — findings

**Verdict: Z_TARGETS_LAW.** On indeg **(0,0,1,1,1,3)**, cycle class
((2,),1) **mixes** Φ=6/12 until split by **z_targets**. t_targets is
constant `(1,)` (uninformative). Role-target grain **generalizes** beyond
ROLE_TARGETS_LAW, but the operative role morphs from hubs (t) to zeros (z).

```
z_targets=(1,1)  → Φ=6,  n_core=3   (only in cycle (2,))
cycles=(3,)      → Φ=6,  n_core=3
else             → Φ=12, n_core=4
```

In-silico; binary exact IIT-4.0; n=6 fixed_k=4. Hypotheses fixed in
`hypotheses.md`. Extends `indeg_002122_grain` ROLE_TARGETS_LAW.

## Discriminant

| grain | condition | Φ | n_core |
|---|---|---:|---:|
| z_targets | **(1,1)** | **6** | 3 |
| cycles | **(3,)** | **6** | 3 |
| else | (2,)∧zt=(1,3); (2,2); (4,) | **12** | 4 |

All tested subtypes Φ-pure. Designed witnesses: (2,)+zt=(1,1)→6;
(2,)+zt=(1,3)→12; (3,)→6; (2,2)/(4,)→12.

## vs ROLE_TARGETS_LAW

| | (0,0,1,1,2,2) | (0,0,1,1,1,3) |
|---|---|---|
| t_targets | splits (→12) | **constant** |
| z_targets | splits (3,) 8 vs 6 | **splits (2,) 6 vs 12** |
| cycle alone | insufficient (MIX) | insufficient on (2,) |
| verdict | ROLE_TARGETS_LAW | **Z_TARGETS_LAW** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 z_targets dissolves (2,) mix | **SUPPORTED** |
| H2 (3,) stays Φ=6 | **SUPPORTED** |
| H3 (2,2)/(4,) stay Φ=12 | **SUPPORTED** |
| H4 all subtypes pure | **SUPPORTED** |
| H5 grain generalizes via z_targets | **SUPPORTED** |

## Reading

Role-target grain is **fingerprint-morphic**: which role’s omit targets
purify the mix depends on the indeg signature. Dual-hub (0,0,1,1,2,2)
needs hub targets; triple-hub (0,0,1,1,1,3) needs zero targets. Discrete
motif-ruled Φ again — not a continuum, not irreducible mix.

## Limits

Dense subtype samples (N_U≤3), not full enum. Conjunctive AND. One new
indeg. ~11 min.

## Best next experiment

Done: [`indeg_000123_grain/`](../indeg_000123_grain/) JOINT_TZ_LAW.
Next: construct arm, or another multi-role indeg. Skip residual /
cascade / ternary / encoding.

## Reproduce

```
python org_frontier/studies/indeg_001113_grain/analyze_grain.py
```
(~11 min)
