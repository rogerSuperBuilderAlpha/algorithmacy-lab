# HMC / CMC / AI-MC at n>3 — findings

**Verdict: SCALE_BLURS_CONSTRUCTS (narrowly).** Classical padded HMC (W↔S
plus idle parties) stays a **2-core**. CMC conveyors stay non-commit (whole
Φ_MIP=0; cores ≤2). AI-MC’s **≥3-core boundary persists**. Algorithmacy
controls stay irreducible (idle-padded cores Φ=2; multiparty whole Φ=3).
The blur case is **multi-worker HMC-like assist** (S = W1∨W2): major complex
grows to **{W1,S,W2}** (n_core=3) — so “HMC” at n>3 is encoding-sensitive.

In-silico; binary exact IIT-4.0; n∈{4,5}. Hypotheses fixed in
`hypotheses.md`. Lab defs from `discriminant_boundaries` / probes 15–20.
Complements omit-atom arc (`OMIT_ATOM_ARC.md`). Ternary / residual noted only.

## Already known (n=3)

Convey → dyadic; commit → triadic; AI-MC W→A→C can be structurally triadic
(probe 20 boundary). HMC two-node mutual is irreducible but not a triad by
party count (`discriminant_boundaries`).

## Census (selected)

| form | family | n | whole | core | Φ | n_core |
|---|---|---:|---|---|---:|---:|
| hmc_pad4/5 | HMC | 4–5 | dyadic/0 | {W,S} | 2 | **2** |
| **hmc_parallel4** | HMC | 4 | dyadic/0 | {W1,S,W2} | 2 | **3** |
| cmc_chain4/5 | CMC | 4–5 | dyadic/0 | {W} | 1 | 1 |
| cmc_echo4 | CMC | 4 | dyadic/0 | {W,S} | 2 | 2 |
| aimc_rewrite/blend4 | AI-MC | 4 | dyadic/0 | {W,A,C} | 2 | **3** |
| aimc_dual5 | AI-MC | 5 | dyadic/0 | {W,A1,A2,C} | 2 | **4** |
| algo_joint4/5 | ALGO | 4–5 | dyadic/0 | {W,S,C} | 2 | **3** |
| algo_multiparty4 | ALGO | 4 | **triadic/3** | {W,S,C1,C2} | 3 | **4** |

Idle padding makes many **wholes** factor while **cores** preserve the
construct story — report both.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 HMC ≤2-core / non-algorithmacy | **REFUTED** (parallel assist → 3-core) |
| H2 CMC non-commit at n>3 | **SUPPORTED** |
| H3 AI-MC ≥3-core boundary persists | **SUPPORTED** |
| H4 algorithmacy controls irreducible | **SUPPORTED** |

## Reading

**vs omit-atom picture.** Omit atoms are digraph-motif laws on fixed_k
couplings. Construct discriminants are **role encodings** (commit vs convey;
party count). They are complementary. Scale does not erase CMC or
algorithmacy controls; it stresses HMC’s definition when one machine serves
multiple humans without a joint commit.

## Limits

Designed forms only (N=12). Idle pads are a modeling choice. Conjunctive AND.

## Best next experiment

Sharpen multi-party HMC vs algorithmacy encodings, or finer grain on indeg
MIX classes. Skip residual/cascade/ternary.

## Reproduce

```
python org_frontier/studies/constructs_n_gt3/analyze_constructs.py
```
(~10 s)
