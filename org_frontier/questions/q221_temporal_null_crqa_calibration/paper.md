# Q221 — Pairwise recurrence summaries do not identify the transition law of noisy Boolean networks (exploratory)

**Draft scientific report, updated 2026-10-15.** The three-node candidate search, q161 bottleneck-target comparison, temporal-null pilots and general theory development are exploratory or exact mathematics. A separate four-node **target-A** classification study was prospectively preregistered (`confirmatory_4node/PREREGISTRATION.md`) and supports specific confirmatory empirical decisions only within that study's fixed synthetic model family and protocol; see `confirmatory_4node/RESULTS.md` and `DEVIATIONS.md`. No confirmatory IIT-specific bottleneck claim, new estimator, universal observational-impossibility theorem, or equivalence of complete trajectories is asserted.


## Headline (revised 2026-10-15; exploratory and provisional)

*This section leads the report. Hassan's original framing follows unchanged from "Abstract" onward. The
original title was "Information limits of pairwise recurrence summaries for IIT-defined bottleneck targets".*

**Target A, statistical identifiability (main result).** Population pairwise categorical recurrence summaries
do not identify the multivariate transition law. These summaries are the stationary marginals and the auto-
and cross-match profiles at every lag.
- *Proved* for invertible GF(2)-affine noisy networks (`THEORY.md`, Proposition 1 and Corollary). The proof is
  checked exhaustively on 1344 of 1344 three-node forms.
- *Instantiated* by three non-isomorphic 3-node pairs, found by an exact screen of the 7,488 existing candidates.
  Hassan independently certified the all-lag equality (`independent_audit/EXACT_ALL_LAGS_PROOF.md`).
- The systems are **not** observationally equivalent. The full process law, and the (X,Y) and (Y,H)
  bivariate laws, differ: this was decided exactly for all T (`identifiability/process_law_equivalence.py`).
  The univariate laws and the (X,H) law are equal.

**Minimum-node exact result (post-hoc):** An independent exhaustive audit of all invertible one- and two-node affine models finds no non-isomorphic models with equal population recurrence summaries (n=1: two models/two classes; n=2: 24 models/16 profile classes, eight collisions, all relabelings). Together with the verified three-node witness, **n=3 is the minimum** for this type of ambiguity within the specified invertible GF(2)-affine class for 0<p<1/2. See independent_audit/MINIMALITY_AFFINE.md. This is not IIT bottleneck-target minimality or a general Boolean-network theorem.

**Which statistics recover the difference** (prespecified comparator study, `identifiability/comparators.py`;
specs in `protocol.md`):

| statistic | population level | finite samples (T = 600) |
|---|---|---|
| transfer entropy | separates all 3 pairs exactly (TE X→Y: 0.598 bits vs 0) | accuracy 1.00 |
| categorical joint-recurrence rates | separate all 3 pairs exactly | 0.995–1.00 |
| full-state transition counts | separate | 1.00 |
| Gilpin's SHREC (library defaults, prespecified features) | — | 0.90–1.00 |
| full-vector (MdRQA-type) recurrence rate | **exactly equal** in all 3 pairs (with a uniform stationary law it equals trace(P^k)/8) | chance |
| false-pair-calibrated q220 prominence | equal by the theorem | 0.48–0.58 |

**Targets B–D.**

| target | result |
|---|---|
| B: q161 structural target | **Convention-dependent.** The bottleneck sets differ only under q161's rule-freeze convention. Under an IIT background-condition reading, they coincide or become ineligible (`TARGET_AUDIT.md`, `OPEN_QUESTION_FOR_MAINTAINER.md`). |
| C: IIT quantities | **Negative.** Same major complex {X,H}, same Φ = 2. |
| D: q220 decoder | **At chance** on held-out families: +0.04 and +0.02 above chance, CIs include 0. Exploratory. |

**Not claimed:** observational indistinguishability, failure of q220 in general, an IIT theorem, or
confirmatory evidence.

**Novelty is narrow.** Pairwise blindness to higher-order structure (Gilpin 2025; Williams & Beer) and
observational equivalence of hidden Markov chains (Gilbert 1959; Ito et al. 1992) are established. Q221
contributes:
- an exact closed form for categorical recurrence in this class;
- instances in the lab's own model space;
- an audit of the lab's target definition;
- measured null false-positive rates for q220's statistic.

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

The independent standard-library rational certificate in independent_audit/exact_all_lags_certificate.py reconstructs the lead pair's 8-state noisy kernels from the affine rule codes, verifies the uniform stationary law exactly, and checks 144 exact rational recurrence equalities (all nine ordered channel profiles at lags 0–15). The Cayley–Hamilton argument in independent_audit/EXACT_ALL_LAGS_PROOF.md extends that finite exact check to **all integer lags** for the declared stationary categorical match statistic. A 48-element relabeling search rules out the specified node/value equivalences. Six focused independent regression tests now pass locally (including the population decoder diagnostic). This is a mathematical verification of recurrence profiles, **not** a separate PyPhi rerun.

**Target-set qualification:** The pinned PyPhi record reports bottleneck sets {X,H} and {H}. They differ as complete sets, but share node H. Accordingly, no deterministic decoder given only the common exact *population summary* can reconstruct both **complete sets** exactly. That does *not* imply no decoder can select a correct bottleneck node for both: predicting H would score as a correct singleton in both under the q220 tie-aware scoring rule. The result does not establish different maximum Phi or different major-complex membership, and it does not prove failure of a finite-sample q220 decoder.

### Population q220 decoder diagnostic

For the lead pair at the original q220 lag window ±10, the exact population **peak-minus-median** prominence is zero for all three unordered cross-channel pairs, despite nonflat negative-lag deviations in parts of the raw match profiles. With the 0.05 prominence threshold, the population centrality vector is all zero, the predicted max-centrality set is all three nodes, and the tie-aware scores are **2/3 for P and 1/3 for Q**—exactly their respective set-size chance baselines. The rational script and regression test check these statements without Monte Carlo error.

This is an exact **population functional** result for these designed systems, not a guarantee that empirical prominence is always zero for finite trajectories. It explains why the current peak-only decoder can return no evidence on this pair without implying that the entire recurrence representation has no temporal information or that q220 generally fails.

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

### Addendum 2: comparator study (2026-10-15, executor)

These are the prespecified comparators: spec commit `311a6477`, results in
`identifiability/results/comparators.txt`.

**Exact population separation:**
- Transfer entropy and joint recurrence: yes, for all 3 pairs.
- MdRQA full-vector recurrence rate: no. It is exactly equal (trace invariant).
- False-pair q220: no, by the Corollary.
- SHREC: not computable at the population level.

**Finite-sample accuracy** (400 test trajectories, nearest centroid; the rule is a Bonferroni-adjusted Wilson
lower bound > 0.5):

| comparator | S1 | S2 | S3 |
|---|---|---|---|
| TE | 1.00 | 1.00 | 1.00 |
| joint recurrence | 1.00 | 1.00 | 0.995 |
| MdRQA | 0.488 | 0.490 | 0.493 |
| SHREC | 0.895 | 1.00 | 0.918 |
| false-pair q220 | 0.583 (lower bound 0.509, so it passes the rule weakly) | 0.483 | 0.505 |

The weak S1 false-pair signal, despite equal population means, indicates that the prominence statistic's
sampling distribution differs beyond its mean. It is not evidence against target A.

### Addendum 3: preregistered 4-node study of target A (2026-10-15, executor)

- **Preregistration** `confirmatory_4node/PREREGISTRATION.md` (commit `2ad11e69`) was pushed before any study
  code was run. Results are in `confirmatory_4node/RESULTS.md`; deviations (none affect outcomes) are in
  `DEVIATIONS.md`.
- **Exact result (H1).** Among 322,560 four-node affine noisy Boolean systems, 1,872 non-isomorphic orbit pairs
  share every pairwise recurrence summary at all lags but have different transition laws.
- **Confirmatory (H2).** A classifier on those summaries is equivalent to chance on 40 held-out pairs (mean 0.4999,
  90% CI [0.493, 0.507]).
- **Confirmatory (H3).**
  - Transition likelihood separates 40/40.
  - Lag-1 transfer entropy generally separates (36/40). Its population value separates only 25/40; the
    excess is attributed, on an exploratory basis, to finite-sample estimator bias.
  - The MdRQA rate (8/40) and the false-pair-calibrated q220 statistic (1/40) generally fail.
  - Joint recurrence (23/40) and SHREC (28/40) are unresolved.
- **Scope.** These results are limited to family F4, T = 600 and these implementations. They make no claim
  about IIT targets.
