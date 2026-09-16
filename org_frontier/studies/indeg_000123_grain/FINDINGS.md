# Joint role-target grain on indeg (0,0,0,1,2,3) — findings

**Verdict: JOINT_TZ_LAW.** On indeg **(0,0,0,1,2,3)** both t_targets and
z_targets vary. Joint subtypes are Φ-pure:

```
(t_targets, z_targets) = ((2,), (1, 2, 3))  → Φ=6,  n_core=3
else                                       → Φ=12, n_core=4
```

t_targets alone is **insufficient** (tt=(2,) still mixes 6/12 by z).
z_targets alone is a **sufficient cut** (zt=(1,2,3)→6; else→12). Cycle
alone mixes. Multi-role interaction does **not** create irreducible mix.

In-silico; binary exact IIT-4.0; n=6 fixed_k=4. Hypotheses fixed in
`hypotheses.md`. Extends ROLE_TARGETS_LAW / Z_TARGETS_LAW.

## Discriminant

| (tt, zt) | cycles | Φ | n_core |
|---|---|---:|---:|
| ((2,), (1,2,3)) | (2,) | **6** | 3 |
| ((1,), (2,2,3)) | (2,) | 12 | 4 |
| ((2,), (1,3,3)) | (2,) | 12 | 4 |
| ((2,), (3,3,3)) | (2,) | 12 | 4 |
| ((1,), (2,3,3)) | (3,) | 12 | 4 |
| ((2,), (2,3,3)) | (3,) | 12 | 4 |

All tested joint subtypes pure.

## vs prior laws

| indeg | roles vary | purifying grain | verdict |
|---|---|---|---|
| (0,0,1,1,2,2) | t (z on (3,)) | hubs / t_targets | ROLE_TARGETS_LAW |
| (0,0,1,1,1,3) | z only (t const) | zeros / z_targets | Z_TARGETS_LAW |
| **(0,0,0,1,2,3)** | **t and z** | **joint; z-cut sufficient** | **JOINT_TZ_LAW** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 joint subtypes Φ-pure / law | **SUPPORTED** |
| H2 t_targets alone insufficient | **SUPPORTED** |
| H3 z_targets cut sufficient | **SUPPORTED** |
| H4 cycle alone insufficient | **SUPPORTED** |
| H5 multi-role grain, no irr. mix | **SUPPORTED** |

## Reading

When both roles have degrees of freedom, the MIX still dissolves under
(tt×zt) grain. The predictive cut can collapse to z (here), but stating
the law jointly records that t alone would mis-classify the tt=(2,)
slice. Role-target grain remains fingerprint-morphic, not a single
universal (t or z) rule — and not an irreducible multi-role fog.

## Limits

Dense samples (N_U≤3), not full enum. Conjunctive AND. One indeg. ~10 min.

## Best next experiment

Another multi-role indeg, or construct arm. Skip residual / cascade /
ternary / encoding unless tooling lands.

## Reproduce

```
python org_frontier/studies/indeg_000123_grain/analyze_grain.py
```
(~10 min)
