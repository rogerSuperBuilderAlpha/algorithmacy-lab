# Finer grain on MIX indeg (0,0,1,1,2,2) — findings

**Verdict: ROLE_TARGETS_LAW.** The MIX dissolves under role-target grain.
Within indeg **(0,0,1,1,2,2)**: **t_targets=(1,1) ⇒ Φ=12** (n_core=4);
within cycle **(3,)**, **z_targets=(2,2) ⇒ Φ=8** (n_core=5); otherwise
**Φ=6** full-core. All tested subtypes are Φ-pure.

In-silico; binary exact IIT-4.0; n=6 fixed_k=4. Hypotheses in
`hypotheses.md` (H5 fixed after H3 failed, before confirmatory sample).
Extends `indeg_002122_n6` MIX. Ternary / residual noted only.

## Discriminant

| grain | condition | Φ | n_core |
|---|---|---:|---:|
| t_targets | **(1,1)** (hubs omit only singles) | **12** | 4 |
| z_targets on (3,) | **(2,2)** (zeros omit only hubs) | **8** | 5 |
| else | — | **6** | 6 |

t_targets law holds on cycle classes (2,), (2,2), and (4,). The (3,) class
has no t_targets=(1,1) slice; its residual 6/8 mix is purified by z_targets.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 tt=(1,1)⇒12 on (2,2)/(4,) | **SUPPORTED** |
| H2 law extends to cycle (2,) | **SUPPORTED** |
| H3 (3,) stays flat Φ=6 | **REFUTED** (led to H5) |
| H4 all subtypes pure / MIX dissolved | **SUPPORTED** |
| H5 (3,) z_targets 8 vs 6 | **SUPPORTED** |

## Reading

Cycle type alone was too coarse for this indeg fingerprint. **Hub omit
targets** (and, on 3-cycles, **zero-node omit targets**) restore purity.
Discrete motif-ruled Φ again — finer motifs, not a continuum.

## Limits

Dense subtype samples, not full enum. Conjunctive AND. One indeg.

## Best next experiment

Lift role-target grain to another indeg, or n=5 HMC encoding ladder.
Skip residual/cascade/ternary.

## Reproduce

```
python org_frontier/studies/indeg_002122_grain/analyze_grain.py
```
(~15 min)
