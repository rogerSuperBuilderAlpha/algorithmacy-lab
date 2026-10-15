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
