# Construct ladders at n=6 — HMC / CMC / AI-MC — findings

**Verdict: PHI_TRACKS_NM1_ALL.** At n=6, HMC, CMC, and AI-MC all flip at
`pre_AND → full_AND` with whole triadic n_core=6, **Φ=5 (=n−1)** for AND
and OR. COMMIT_READ holds on every family. No family morphs.
`construct_ladders_n5` BOUNDARY_TRANSFERS **scales** with
`encoding_ladder_n6` PHI_TRACKS_NM1 across constructs.

In-silico; binary exact IIT-4.0; trimmed n=6 ladders (~5 min). Hypotheses
fixed in `hypotheses.md`. Assist path trimmed for N; pre-boundary + flip
+ one drop kept.

## Per-family ladders

### HMC

| encoding | n_core | Φ | whole | note |
|---|---:|---:|---|---|
| hmc_classical | 2 | 2 | dyadic | W1↔S |
| hmc_pre_AND | 5 | 4 | dyadic | **pre-boundary** |
| hmc_C_reads | 5 | 4 | dyadic | C out |
| **hmc_full_AND/OR** | **6** | **5** | **triadic** | **flip** |
| hmc_drop_C_ro | 5 | 4 | dyadic | reverse |

### CMC

| encoding | n_core | Φ | whole | note |
|---|---:|---:|---|---|
| cmc_chain | 1 | 1 | dyadic | classical convey |
| cmc_pre_AND | 5 | 4 | dyadic | **pre-boundary** |
| cmc_F_reads | 5 | 4 | dyadic | F out |
| **cmc_full_AND/OR** | **6** | **5** | **triadic** | **flip** |
| cmc_drop_F_ro | 5 | 4 | dyadic | reverse |

### AI-MC

| encoding | n_core | Φ | whole | note |
|---|---:|---:|---|---|
| aimc_rewrite | 3 | 2 | dyadic | transform boundary |
| aimc_pre_AND | 5 | 4 | dyadic | **pre-boundary** |
| aimc_F_reads | 5 | 4 | dyadic | F out |
| **aimc_full_AND/OR** | **6** | **5** | **triadic** | **flip** |
| aimc_drop_F_ro | 5 | 4 | dyadic | reverse |

**Boundary step (all three):** `pre_AND → full_AND`.

**Φ vs n−1:** at flip, Φ = 5 = n−1 (AND and OR, every family).

**COMMIT_READ:** last party out on reads-only and on drop (all three).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 all three PHI_TRACKS_NM1 at n=6 | **SUPPORTED** |
| H2 some family morphs | **REFUTED** |
| H3 COMMIT_READ breaks | **REFUTED** |

## Reading

Baselines keep construct signatures (HMC 2-core; CMC 1-core convey;
AI-MC 3-core transform). The literacy/construct→algorithmacy boundary
is shared and scale-stable: last outer party into the mediator’s
determination with all reading. n=5 BOUNDARY_TRANSFERS and n=6
PHI_TRACKS_NM1 compound — construct identity and Φ=n−1 co-hold.

## Limits

Trimmed ladders (assist path omitted). Monotone AND/OR at the flip.
One literal path per family. Full-bind ~40 s/cell. No organization
measured. n>6 not run (cost). Residual / cascade / ternary / omit
pointed only.

## Best next experiment

Close the construct×scale cell: synthesis note pairing
BOUNDARY_TRANSFERS with PHI_TRACKS_NM1_ALL, or probe one non-monotone
gate on a CMC/AI-MC full-bind (gate arm already says affine morphs).
Skip residual / cascade / ternary / omit-arc. Prefer that over another
multi-role indeg.

## Reproduce

```
python org_frontier/studies/construct_ladders_n6/analyze_ladders.py
```
(~5 min)
