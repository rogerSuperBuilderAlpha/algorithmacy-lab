# Q221 — Information limits of pairwise recurrence summaries for IIT-defined bottleneck targets

**Exploratory methods report — draft for scientific review, 2026-10-15.** This document reports retrospective computational discovery, not a prospectively preregistered or confirmatory hypothesis test. It does not claim a new estimator, a universal impossibility theorem, or indistinguishability from complete trajectories.

## Abstract

We investigate whether population-level categorical recurrence summaries uniquely determine an IIT-4.0-derived leave-one-node-out bottleneck target in small Boolean systems. A bounded search of 8,192 three-node rule sets under independent 8% node-flip observation noise produced 7,488 initial eligible pairs with matching cross-channel lag profiles and different q161 bottleneck sets. After excluding constant-node examples, matching channel marginals and within-channel recurrence, and removing node-permutation/value-relabeling isomorphisms, three distinct symmetry classes remained. For a representative pair, the repository's pinned PyPhi calculation reports identical major-complex membership and Φ but different leave-one-node-out bottleneck sets, with exact-rational recurrence-profile equality through lag 40. In held-out trajectories, simple recurrence-summary classifiers perform near chance, while transition-aware classifiers distinguish the generating systems perfectly in the recorded tests. These results show information loss in a **restricted population pairwise recurrence representation**, not observational equivalence of the underlying dynamical systems. Generalization, inferential calibration, and novelty beyond established recurrence and surrogate-data literature remain open.

## Research question and scope

For three-node Boolean update rules and a fixed 8% independent per-node flip observation model, can two non-isomorphic systems have the same stationary marginal and categorical auto/cross match-rate profiles but different q161-defined structural bottleneck targets?

The target is the maximizer set of the decrease in major-complex Φ after replacing each node's deterministic update rule with a constant (the lab's leave-one-node-out intervention). It is **not** a theory-independent causal ground truth. Exact Φ is computed from the deterministic transition rule under the pinned IIT-4.0 implementation; stochastic flip noise is applied to observed trajectories and recurrence profiles, not to that ground-truth computation.

## Methods

### Search and provenance

The bounded exploratory search examined 4,096 no-self-input Boolean forms and 4,096 GF(2)-affine forms, grouping them by stationary population cross-channel categorical match probabilities at ordered-pair lags −20 through +20. The search evaluated q161 targets for 8,016 forms in multi-member groups. It applied target eligibility (core size ≥2, nonempty proper bottleneck set), node-permutation exclusion, and a positive bottleneck margin. Twenty selected pairs were checked with exact rational recurrence profiles. The completed run took 290.4 seconds including selected re-verification, below its 1,800-second budget. See `identifiability/SEARCH_RECORD.md` and `results/pair_search.{json,txt}`.

The subsequent stricter **post-hoc** screen excluded constant nodes, required matching stationary channel marginals and self-recurrence profiles, rechecked cross-profiles, and excluded isomorphism under six node permutations and eight per-node binary value relabelings. The count sequence was 7,488 → 6,816 → 6,432 → 180 → 180 → 144 pair records, yielding three unique 48-group classes. These are not independent samples or 144 unique discoveries.

### Exact-Φ target

The representative lead pair is P=`aff(9,6,10)` and Q=`aff(9,15,10)`. The repository's pinned PyPhi IIT-4.0 run reports a major complex {X,H} and maximum Φ=2.0 for both. The q161 leave-one-out Φ drops are [2,0,2] for P and [1,0,2] for Q, giving bottleneck sets {X,H} and {H}. The pinned verification independently implements the target loop and both clamp-to-0 and clamp-to-1 variants; it reports matching results, a positive margin, and no isomorphism under the 48-element symmetry group. See `identifiability/results/rep_verify.txt`. This is independent *implementation* verification within the lab environment, not an external cross-platform replication.

### Observation and prediction controls

Under the 8% flip model, the representative systems have equal stationary channel marginals and exact-rational categorical auto/cross match profiles through lag 40 in the pinned verification. A finite-lag match alone is not full observational equivalence.

The repository's q220 observation pipeline uses off-diagonal recurrence prominence and centrality, with a 0.05 prominence floor and lag window ±10. The lead-pair finite-sample analysis uses 600 observations, 20 warm-up steps, 400 seeded trajectories, and tie-aware bottleneck scoring. Additional baseline tests used disjoint training/test seeds and 400 held-out trajectories per pair, with fixed nearest-centroid classifiers for marginal, self-recurrence, cross-recurrence and transition-count features, plus a fitted transition likelihood classifier. See `identifiability/adjudicate.py`, `baselines_survivors.py`, and their recorded results.

## Results

### Search and structural target

Three 48-group-unique candidate classes survived the retrospective filters. The representative P/Q pair differs in the **set of maximizing leave-one-out drops**, not in the major complex or its maximum Φ. The original A/B XOR candidate was rejected because both targets were degenerate; a later fully matched pair `aff(6,9,5)` versus `aff(11,9,5)` was rejected because it is isomorphic under the larger symmetry group.

### Finite-sample behavior

For the lead pair, q220's recorded bottleneck scores are approximately 0.643 (P) and 0.330 (Q), close to their respective set-size-adjusted chance baselines 2/3 and 1/3. These are descriptive estimates for the selected systems, not evidence of performance on a new form population.

Across three surviving pairs, the recorded held-out accuracy of marginal, self-recurrence and cross-recurrence summary classifiers ranges roughly from 0.4275 to 0.525. Full 8×8 transition-count and fitted transition-likelihood classifiers each achieve 1.0 accuracy on the recorded 400 test trajectories per pair (Wilson 95% lower bound approximately 0.9905). A near-chance classifier is not proof that the underlying feature distributions are identical. The perfect transition results demonstrate that the systems are **not** observationally indistinguishable from complete trajectories.

### Separate null-calibration pilot

An independent exploratory pilot of **zero-lag Pearson correlation**, not q220's recurrence classifier, shows that naive shuffling of independent persistent binary series can inflate nominal 5% false-positive rates. This reproduces a known methodological issue and is not presented as a novel or confirmatory Q221 result. See `independent_audit/NULL_CALIBRATION_AND_FINITE_SAMPLE.md` and `REPRODUCTION_STATUS.md`.

## Exact mathematical certificate and correct-node distinction

The independent standard-library rational certificate in independent_audit/exact_all_lags_certificate.py reconstructs the lead pair's 8-state noisy kernels from the affine rule codes, verifies the uniform stationary law exactly, and checks 144 exact rational recurrence equalities (all nine ordered channel profiles at lags 0–15). The Cayley–Hamilton argument in independent_audit/EXACT_ALL_LAGS_PROOF.md extends that finite exact check to **all integer lags** for the declared stationary categorical match statistic. A 48-element relabeling search rules out the specified node/value equivalences. Four lightweight regression tests pass locally. This is a mathematical verification of recurrence profiles, **not** a separate PyPhi rerun.

**Target-set qualification:** The pinned PyPhi record reports bottleneck sets {X,H} and {H}. They differ as complete sets, but share node H. Accordingly, no deterministic decoder given only the common exact *population summary* can reconstruct both **complete sets** exactly. That does *not* imply no decoder can select a correct bottleneck node for both: predicting H would score as a correct singleton in both under the q220 tie-aware scoring rule. The result does not establish different maximum Phi or different major-complex membership, and it does not prove failure of a finite-sample q220 decoder.

### Loss-function dependence

For a hypothetical balanced choice between these two systems when the input is only their **common exact population recurrence summary**, the maximum accuracy of any deterministic or randomized **complete bottleneck-set classifier** under zero-one exact-set loss is 50%: the target sets differ and the input is identical. In contrast, a **single-node classifier** always choosing H is correct for both sets, yielding 100% membership accuracy and singleton tie-aware score. These are mathematical optimum values for different tasks, not measured performance of q220 on held-out network forms. See independent_audit/EXACT_ALL_LAGS_PROOF.md.

## Constructive sufficiency result under full-state observation

For the model used in the experiment, each deterministic rule bit can be recovered from the full-state one-step conditional node probabilities. Specifically, with independent update flips at rate epsilon < 0.5, the conditional mean of next node j at current state s is epsilon + (1-2epsilon) f_j(s). Thresholding this value at 0.5 reconstructs the deterministic Boolean update table f exactly at the population level. The independent exact-rational certificate checks all 24 conditional state/node probabilities for each lead system and reconstructs both rule tables correctly.

This provides a **sufficient alternative information representation** to the restricted recurrence profiles, not a minimality theorem. Under full observation and the stated noise mechanism, the recovered deterministic rules can be submitted to the specified q161 IIT computation to obtain the lab-defined bottleneck target. With hidden state variables, altered noise mechanisms, or finite data, this guarantee requires new assumptions and analysis. It is consistent with the recorded finding that full transition-aware classifiers distinguish the lead systems.

## Discussion

The experiments illustrate that compressing multivariate trajectories to selected population one- and two-point categorical match summaries can remove information relevant to a *particular IIT-defined perturbational target*. A finite-sample decoder may still exploit differences in feature sampling distributions, and a transition-aware observer can recover distinctions discarded by the summaries. The observed mismatch is thus about **representation and task definition**, not a general inability to infer structure from observed dynamics.

The leave-one-out bottleneck is convention-sensitive: clamping a rule to a constant can leave residual complexes outside the original major complex. Its invariance under value relabeling is not guaranteed; symmetry screening and both clamp conventions are therefore necessary safeguards.

## Limitations and future work

The candidate families are synthetic, three-node and retrospectively selected; exact-Φ results depend on the pinned IIT-4.0 implementation and reachable-state conventions. The results do not establish an optimal recurrence statistic, calibrated CRQA null, generalization to unseen forms, a formal all-lag theorem for every candidate, or practical relevance to real organizations. There is no confirmatory registration. A future independent-form study should specify the target, null, primary statistic, unit of replication, multiplicity, computational budget and inference procedure **before** examining confirmatory outcomes.

## Related literature and novelty status

Theiler et al. (1992), Schreiber & Schmitz (2000), and Yuan & Shou (2022, 2024) establish surrogate-testing and time-series dependence issues. Marwan et al. (2007) and Marwan (2011) document recurrence methods and pitfalls. Gilpin (2025) addresses recurrence and shared causal drivers. Albantakis et al. (2023) defines IIT 4.0. The present search is a specific computational example in the lab's IIT bottleneck setting; **the originality of that exact conjunction has not been established by an exhaustive source-level review**. See `literature/LITERATURE_REGISTER_DRAFT.md`.

## Reproduction

The search scripts, exact-rational checks, pinned PyPhi receipts, q220 finite-sample evaluation, independent audits, and baseline results are under `identifiability/` and `independent_audit/`. See `GATES.md` for the latest validation status. No q161 or q220 historical output is altered by this report.

## Selected references

- Albantakis et al. (2023). *Integrated information theory (IIT) 4.0.* DOI: 10.1371/journal.pcbi.1011465.
- Gilpin (2025). *Recurrences Reveal Shared Causal Drivers of Complex Time Series.* DOI: 10.1103/PhysRevX.15.011005.
- Marwan et al. (2007). *Recurrence plots for the analysis of complex systems.* DOI: 10.1016/j.physrep.2006.11.001.
- Marwan (2011). *How to avoid potential pitfalls in recurrence plot based data analysis.* DOI: 10.1142/S0218127411029008.
- Schreiber & Schmitz (2000). *Surrogate time series.* DOI: 10.1016/S0167-2789(00)00043-9.
- Theiler et al. (1992). *Testing for nonlinearity in time series: The method of surrogate data.* DOI: 10.1016/0167-2789(92)90102-S.
- Yuan & Shou (2022). *Data-driven causal analysis of observational biological time series.* DOI: 10.7554/eLife.72518.
- Yuan & Shou (2024). *A rigorous and versatile statistical test for correlations between stationary time series.* DOI: 10.1371/journal.pbio.3002758.

## Addendum (2026-10-15, executor; mandate 13:02 ET)

- **Target audit (`TARGET_AUDIT.md`).**
  - For P/Q, the q161 target is permutation-equivariant and invariant under all 7 value relabellings.
  - The P/Q difference comes from q161's rule-freeze convention: the frozen node stays a perturbed element and
    keeps its edges, and a residual {Y} complex survives in Q.
  - Under an IIT background-condition reading (node k held fixed, outside every candidate subsystem), B(P) =
    B(Q) = {X,H}.
  - The third survivor pair also becomes equal. In the second pair, one member becomes ineligible (|B| = 3).
  - **The structural-target difference is therefore convention-dependent.**
- **Equality (2) is decided exactly** (`identifiability/process_law_equivalence.py`, Schützenberger/Tzeng span
  algorithm).
  - The projected laws of X, Y, H and (X,H) are equal for all T.
  - The laws of (X,Y), (Y,H) and the full process differ.
- **Theory (`THEORY.md`).** For invertible GF(2)-affine noisy systems, Proposition 1 gives the closed form of
  every pairwise categorical recurrence statistic. It explains all three survivor classes, and was checked
  against exact computation for 1344 of 1344 forms.
- **Held-out families (frozen spec `ecd014dd`).** q220's score above chance is +0.04 [−0.05, +0.12] on `nsi`
  and +0.02 [−0.04, +0.08] on `aff`. A plug-in transition-law comparator scores 1.0.
- **Gate E extension (frozen spec `6ad206a3`).** It measures the shuffle-null FPR of q220's own prominence
  statistic: 0.272 at stay probability 0.9 and 0.428 at 0.98. Circular-shift, block and fitted-Markov
  surrogates stay at 0.02–0.07.
