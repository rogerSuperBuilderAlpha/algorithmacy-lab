# Q221 4-node study of target A: preregistration

**Registered:** 2026-10-15, about 18:05 ET. This file was committed before any study code was written or run.

**Status.** Prespecified. The study may produce two kinds of result:
- **exact (mathematical) results** for the existence claim;
- **confirmatory empirical results** for the finite-sample hypotheses, *only* if every decision rule below is
  applied without an outcome-affecting deviation.

Everything else is exploratory. Deviations are logged in `DEVIATIONS.md` with their timestamp and reason.

## 1. Claim under test (target A)

Population pairwise categorical recurrence summaries do not identify the transition law. The summaries R are:
- all marginals P(x_i = 1);
- all auto- and cross-match probabilities P(x_i(t) = x_j(t+k)), for all i and j (i = j included) and all
  k ≥ 0. Negative lags are covered by swapping i and j.

Proposition 1 in `../THEORY.md` is proved for every n. This study (a) instantiates the claim at **n = 4**,
exactly, and (b) tests prespecified finite-sample consequences on independently generated data.

## 2. Family and generator

- **Family F4.** x(t+1) = A x(t) ⊕ c ⊕ n(t), with:
  - A ∈ GL(4, 2) (20,160 matrices);
  - c ∈ GF(2)^4 (16 vectors);
  - this gives **322,560 systems**;
  - n(t) is an i.i.d. Bernoulli(p) flip per node, with p = 2/25 = 0.08.
- **Stationary law.** It is uniform and unique, because A is invertible and p > 0.
- **Finite-sample generator.** The repo's `org_frontier.recurrence.crqa.trajectory` (q220's), with
  rules x ↦ A x ⊕ c, flip 0.08, warmup 20 and T = 600.

## 3. Exact screen (no sampling)

| stage | rule |
|---|---|
| S0 | enumerate all 322,560 systems |
| S1 | compute the Proposition-1 / Corollary signature for each system: for each source node j and lag k = 0..40, whether the path w_k = (A^T)^k e_j equals a unit vector e_i (and which i), together with S_k = Σ_{m<k} \|w_m\| and the parity Σ_{m<k} w_m·c (mod 2). By Proposition 1 (proved), two systems have identical R **iff** their signatures are equal. Why lags to 40 suffice: the path is periodic with period ord(A) ≤ 15, and every profile sequence satisfies a linear recurrence of order ≤ 16 (16-state chain; Cayley–Hamilton) |
| S2 | group systems by signature into **recurrence-equal classes** |
| S3 | **relabeling exclusion.** The group G = S4 (node permutations) × (Z2)^4 (per-node value flips) has 384 elements. It acts by (A, c) ↦ (ΠAΠ^T, Π(c ⊕ (A ⊕ I)m)). Each system gets an orbit id (the minimal encoding over G). A pair is **non-isomorphic** iff its orbit ids differ |
| S4 | **law difference.** Distinct (A, c) give distinct deterministic maps, hence distinct transition matrices; by Proposition 2 the laws differ. This is checked exactly for the study pairs (V2) |

**Reported counts:** systems; classes; multi-member classes; classes containing ≥ 2 orbits; unordered
non-isomorphic system pairs; unordered **orbit pairs** {O1, O2} that co-occur in some class (the sampling unit
of section 5).

**Exact verification.** Brute-force rational arithmetic on the 16-state chain, independent of the closed form.

| check | rule |
|---|---|
| V1 | 300 systems drawn uniformly from F4 (`numpy` `default_rng(4210001)`). For each, the Proposition-1 profiles equal the brute-force exact profiles at lags 0..20 for all (i, j), and the marginals are 1/2 |
| V2 | for every study pair: exact brute-force profiles and marginals equal at lags 0..20 (≥ 16, so all lags); exact TPMs differ; and non-isomorphism, by direct enumeration of all 384 maps of G |

## 4. Hypotheses

**H1 (exact).** F4 contains non-isomorphic pairs with identical R and different laws. Decided by S0–S4 together
with V1 and V2. There is no statistics here.

**H2 (primary finite-sample, summary blindness).** The pairwise-summary classifier R has mean held-out
accuracy across study pairs that is **equivalent to chance**: a TOST with margin ±0.05 at α = 0.05. The
decision is that the 90% t-interval of the mean per-pair accuracy over M pairs lies inside [0.45, 0.55].

**H3 (comparators).** For each classifier C, the proportion π_C of study pairs that C separates is reported
and classified by the rule in section 7. Directional predictions:
- **C0** (transition likelihood, positive control): generally separates (Proposition 2).
- **R** and **C5** (false-pair-calibrated q220 prominence): do not generally separate. Their population
  means are functions of R.
- **C1–C4:** no directional prediction. Their outcomes are estimates classified by the rule.

**Secondary (descriptive, no test).** For C1–C3, report the agreement between exact population separation and
finite-sample separation.

## 5. Study pairs and data

- **Sampling unit:** an unordered orbit pair {O1, O2} that co-occurs in a recurrence-equal class.
- **Representative of a pair:** a = the orbit-canonical representative of O1 (the smaller orbit id); b = the
  lexicographically smallest member of O2 in the same signature class as a.
- **Number of pairs:** M = 40, drawn uniformly without replacement with `default_rng(4210002)`. If fewer
  than 40 orbit pairs exist, all are used.
- **Trajectories:** per pair index q (0..M−1), member m (0, 1) and run r: `default_rng(4220000 + 1000·q +
  500·m + r)`. Runs r = 0..99 are training and r = 100..299 are test, so each pair has 400 test
  trajectories. These seeds are disjoint from every earlier q221 range.

## 6. Classifiers

Features are z-scored by the training SD. Every classifier except C0 is a nearest class centroid with no
tuning.

| classifier | features |
|---|---|
| **R** | marginals (4); auto-match k = 1..10 (40); cross-match k = 0..10 for the 12 ordered pairs (132) |
| **C0** | per-member TPM fitted on that member's training trajectories (add-one smoothing); classify by the log-likelihood ratio |
| **C1** | transfer entropy, history 1, plug-in, 12 ordered pairs (bits) |
| **C2** | categorical joint-recurrence rate P(x_i(t)=x_i(t+k) ∧ x_j(t)=x_j(t+k)), 6 unordered pairs × k = 1..10 |
| **C3** | full-vector recurrence rate P(x(t) = x(t+k)), k = 1..10 |
| **C4** | SHREC (`williamgilpin/shrec` @ `49c6d3e0`, `RecurrenceManifold`, library defaults, `random_state` = 0) on the 600×4 float series. Features: \|corr(y, x_i)\| for the 4 channels, plus the lag-1 autocorrelation of y |
| **C5** | q220 `observe.coupling` prominence (max lag 10, timestamp alignment, MIN_PAIRS 30) for 6 pairs, z-scored against 199 false-pair surrogates. Each surrogate takes its 4 channels from 4 different pooled training trajectories (both members; label-agnostic), with seed `4290000 + q` |

C1–C3 are also computed **exactly at the population level** (rational arithmetic, float log for TE).
"Exactly separates" means some feature differs by more than 1e-12.

## 7. Decision rules and multiplicity

| level | rule |
|---|---|
| per pair × classifier | Wilson interval with a Bonferroni correction over 7·M tests (two-sided α = 0.05/(7M)). **Separates** if the lower bound > 0.5 |
| per classifier (H3) | Wilson interval for π_C with a Bonferroni correction over 7 classifiers (α = 0.05/7). **Generally separates** if the lower bound > 0.5. **Generally fails** if the upper bound < 0.5. Otherwise **mixed (unresolved)** |
| H2 | the TOST rule in section 4 |
| H1 | exact |

**Outcome labels:**
- **verified theorem / exact result:** a proved statement plus passing exact checks;
- **counterexample:** an exact computation contradicts a stated claim;
- **confirmatory empirical:** a prespecified hypothesis decided by its rule with no outcome-affecting deviation;
- **unresolved:** the rule returns mixed, or the CI straddles the boundary;
- **exploratory:** anything post hoc.

## 8. Stop rules and compute budget

- **Budget** for all study jobs combined: **≤ 3 CPU-hours and ≤ 90 minutes wall-clock.**
  - Each job runs through `box-run`, with ≤ 2.5 GB memory per job and ≤ 2 concurrent jobs. The box has 16 GB,
    with about 3 GB free at registration.
  - If the budget would be exceeded, stop at the current pair. Report the completed pairs as **exploratory**,
    with no confirmatory labels.
- **If S3 yields zero non-isomorphic pairs:** H1 is false at n = 4. Stop after the screen and report it.
- **If V1 or V2 fails for any system or pair:** stop, report it as a counterexample to the implementation or
  to Proposition 1, and attach no confirmatory labels.
- **Locked after the first study run:**
  - no re-running with other seeds;
  - no changing features, classifiers, M or thresholds.
- **Smoke tests** are allowed only on seeds outside the study ranges (999000–999999) and on ≤ 2 pairs × 10
  trajectories. Their outputs are discarded.
- **Bugs:** a bug found after the study run is fixed in a separate commit and logged in `DEVIATIONS.md`. If
  the fix changes results that have already been seen, the affected outcome is labelled exploratory.

## 9. Outputs

- `confirmatory_4node/screen4.py` → `results/screen4.{txt,json}`, including the exact V1 and V2 results.
- `confirmatory_4node/study4.py` → `results/study4.{txt,json}`.
- Tests in `confirmatory_4node/test_confirmatory_4node.py`.
