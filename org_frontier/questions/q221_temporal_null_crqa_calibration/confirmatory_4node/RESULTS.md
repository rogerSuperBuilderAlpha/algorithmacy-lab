# 4-node target-A study: results and classification

**Preregistration:** `PREREGISTRATION.md`, commit `2ad11e69`. **Frozen scripts:** `89118627` (screen) and `11d34a7c` (study).
**Run:** 2 `box-run` jobs, 17:57:53–18:05:33 ET 2026-10-15 (460 s each). This is about 0.5 CPU-hours, within the
budget (≤ 3 CPU-hours, ≤ 90 min). Deviations: `DEVIATIONS.md` (D1 clerical, D2 smoke-test size; neither affects outcomes).

## H1: exact existence. **Exact result (verified instance of the proved Proposition 1)**

The exact rational screen (`results/screen4.txt`) found:
- **counts:** 322,560 systems in F4, forming 1,864 relabeling orbits (G = S4 × (Z2)^4, 384 maps) and 66,121
  recurrence-equal classes. Of those classes, 64,201 have more than one member and 30,216 contain ≥ 2 orbits.
- **non-isomorphic recurrence-equal pairs:** 1,366,408 unordered system pairs and **1,872 unordered orbit pairs**.
- **V1:** the Proposition-1 closed form equals brute-force exact profiles for 300/300 random systems.
- **V2:** all 40/40 study pairs have exactly equal R (all lags; Cayley–Hamilton), different TPMs, and are
  non-isomorphic (checked by direct enumeration of all 384 maps).

Of the study pairs, 2 share A and differ only in c; the others differ in 1–4 update rows.

## H2: R classifier at chance. **Confirmatory empirical: supported**

Mean held-out accuracy is 0.4999. The 90% t-interval [0.4929, 0.5070] lies inside [0.45, 0.55] (TOST, margin 0.05).
The classifier separated no pair: 0/40 under the per-pair Bonferroni rule (range 0.448–0.550).

## H3: comparators (Wilson, Bonferroni over 7 classifiers). **Confirmatory empirical**

| classifier | pairs separated (of 40) | π̂ | Bonferroni Wilson CI | verdict | prediction | mean acc. |
|---|---|---|---|---|---|---|
| C0 transition likelihood (positive control) | 40 | 1.00 | [0.847, 1.000] | **generally separates** | separates (met) | 1.000 |
| R pairwise recurrence summaries | 0 | 0.00 | [0.000, 0.153] | **generally fails** | fails (met) | 0.500 |
| C5 false-pair-calibrated q220 prominence | 1 | 0.025 | [0.003, 0.193] | **generally fails** | fails (met) | 0.505 |
| C1 transfer entropy (h = 1) | 36 | 0.90 | [0.706, 0.971] | **generally separates** | none | 0.874 |
| C3 MdRQA full-vector recurrence rate | 8 | 0.20 | [0.083, 0.409] | **generally fails** | none | 0.582 |
| C2 joint recurrence rate | 23 | 0.575 | [0.370, 0.757] | **mixed → unresolved** | none | 0.758 |
| C4 SHREC (library defaults) | 28 | 0.70 | [0.487, 0.851] | **mixed → unresolved** | none | 0.748 |

All three directional predictions were met. C2 and C4 are **unresolved** under the preregistered rule: their
intervals contain 0.5. The single C5 separation is pair q = 2 (accuracy 0.648). This pair shares A and differs only
in c, and its JRR and MdRR population values differ strongly.

## Secondary (descriptive): exact population separation versus finite-sample separation

| | exact population separates | finite separates | agree | exact only | finite only |
|---|---|---|---|---|---|
| C1 TE | 25/40 | 36/40 | 29 | 0 | **11** |
| C2 JRR | 25/40 | 23/40 | 38 | 2 | 0 |
| C3 MdRR | 9/40 | 8/40 | 39 | 1 | 0 |

**Caution on C1.** At the population level, lag-1 pairwise TE is identical for 15/40 pairs. The finite-sample
"generally separates" verdict therefore partly rests on 11 pairs where only the finite-sample estimator distribution
differs. The post-hoc diagnostic `te_bias_diag.py` is **exploratory**:
- the simulator agrees with the exact TPM and with exact TE in long runs (T = 200,000);
- at T = 600, the plug-in TE bias differs between the members of these pairs by 0.004–0.011 bits on some ordered
  pair (per-trajectory SD is about 0.002–0.007).

So population TE does not identify these laws. The finite-sample classifier exploits estimator bias, which depends on
higher-order temporal structure.

**MdRR at n = 4.** At n = 3, MdRR was exactly equal for the three survivors (round 2). At n = 4 it differs exactly
for 9/40 pairs: MdRR(k) = trace(P^k)/16 is not a function of R in general. This is tested in
`test_confirmatory_4node.py`.

Of the five pairs where C1–C3 are all exactly equal (q = 4, 20, 28, 31, 37), SHREC separates two: q = 4 at 400/400 and
q = 31. No C1–C4 comparator separates q = 28 or q = 37. This observation is exploratory.

## Classification summary

| claim | label |
|---|---|
| Target A (R does not identify the law), proved for all n | **verified theorem** (Proposition 1/2) |
| H1 at n = 4 | **exact result**: 1,872 non-isomorphic orbit pairs |
| H2 | **confirmatory empirical, supported** |
| H3 for C0, R, C5 (predicted) and C1, C3 | **confirmatory empirical** (as in the verdict column) |
| H3 for C2, C4 | **unresolved** |
| Secondary agreement table | descriptive |
| TE bias explanation; SHREC on pairs where C1–C3 are exactly equal; the C5 pair q = 2 | **exploratory** |

**Scope.** The confirmatory results cover only F4 (affine GF(2) maps with independent flip noise p = 0.08, T = 600)
and these classifier implementations. They say nothing about q161 IIT targets, other families, or other noise
models. No counterexample to any stated claim was found.

---

# Follow-up: resolving C2 (joint recurrence) and C4 (SHREC)

- **Preregistration:** `PREREGISTRATION_FOLLOWUP.md`, commit **`74ef91c1`**, pushed before any follow-up data.
- **Frozen script:** `followup.py` at `21f705e9`.
- **Results:** `results/followup.{txt,json}`, with per-chunk files `results/followup_part_*.json`.
- **Deviations:** `DEVIATIONS_FOLLOWUP.md` (F1–F4; none affect outcomes).

## Design

| item | value |
|---|---|
| pairs | M = 600 fresh orbit pairs, drawn from the 1,832 not used before (`default_rng(5210002)`) |
| exact checks before any trajectory | 600/600 |
| seeds | 5,220,000–5,819,799, disjoint from all earlier seeds |
| per-pair rule | the parent's, unchanged: z = 3.7475, 400 test trajectories per pair |
| per-classifier rule | Wilson interval, Bonferroni over 2 (z = 2.2414) |
| power at the parent point estimates | 0.93 for JR, ≈ 1 for SHREC |

## Manipulation checks: **PASS**

| check | result |
|---|---|
| R | mean accuracy 0.5008. It separated 1/600 pairs (q = 92, 239/400): one per-pair false positive on a pair whose population R is exactly equal, consistent with the per-pair α |
| C0 | separated 600/600 |

## Primary verdicts: **confirmatory empirical**

| classifier | pairs separated | π̂ | Wilson (Bonferroni over 2) | verdict | mean acc. | accuracy quartiles (min / Q1 / median / Q3 / max) |
|---|---|---|---|---|---|---|
| **C2 joint recurrence** | 347/600 | 0.578 | [0.533, 0.623] | **generally separates** | 0.760 | 0.44 / 0.51 / 0.85 / 1.00 / 1.00 |
| **C4 SHREC** | 363/600 | 0.605 | [0.560, 0.649] | **generally separates** | 0.707 | 0.43 / 0.56 / 0.65 / 0.91 / 1.00 |

Pooled with the parent's 40 pairs (descriptive), the verdicts are unchanged:
- JR: 370/640, [0.534, 0.621];
- SHREC: 391/640, [0.567, 0.653].

**How to read "generally separates".** The rule tests π > 0.5. It does **not** say the comparators separate
nearly every pair. At T = 600, each one fails on about 40% of pairs (JR on 253/600, SHREC on 237/600), and
121/600 pairs are separated by neither. Both point
estimates are modest (0.58 and 0.61).

## Secondary (descriptive)

| | exact population separates | finite separates | agree | exact only | finite only |
|---|---|---|---|---|---|
| C2 JRR (lags 1–10) | 379/600 | 347 | 568 | 32 | **0** |
| C1 TE plug-in | 374/600 | 521 | 453 | 0 | **147** |
| C1 TE Miller–Madow | 374/600 | 521 | 453 | 0 | 147 |

- **JR is bounded by its population value.** Its population value is exactly equal for 221/600 pairs (37%), and
  finite JR never separates a pair whose population JRR is equal. Its finite-sample failures are therefore mostly
  structural. They are not a power problem.
- **SHREC goes beyond JR.** It separates 115 of those 221 pairs (exploratory observation).
- **The TE estimator artefact replicates at scale.** 147 pairs are separated by finite-sample TE although their
  population TE is identical. The registered Miller–Madow correction gives identical separation decisions (600/600 agree); it
  is a constant shift whenever all cells are occupied, see F4. It cannot fix this, so the bias is not the leading-order cell-count term (exploratory reading).
- **Coverage.** 31/600 pairs are separated by none of TE, JR or SHREC; all 600 are separated by the transition
  likelihood.

## Classification

| item | label |
|---|---|
| C2 JR | **generally separates: confirmatory empirical** (replaces the parent's "unresolved") |
| C4 SHREC | **generally separates: confirmatory empirical** (replaces the parent's "unresolved") |
| manipulation checks | pass |
| secondary tables | descriptive |
| "JR is bounded by its population value", "SHREC beyond JR", "TE bias is not the MM term" | **exploratory** |

**Scope.** The same as the parent: F4, p = 0.08, T = 600, these implementations and library defaults (SHREC
`49c6d3e0`). The results say nothing about IIT targets.

