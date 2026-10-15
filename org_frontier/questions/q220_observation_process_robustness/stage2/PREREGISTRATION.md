# q220 stage 2 — Follow-up preregistration (gap-aware CRQA and chance-corrected baselines)

**Status: fixed before any stage-2 simulation.** This file was committed and pushed before the
stage-2 code was run on any trajectory. Its git commit is the timestamp.

*Post-merge erratum (follow-up to #827; the preregistration text above is kept verbatim):* the record supports only
"committed before" (`48e479f4`, 09:22:58 ET 2026-10-15). The commit also reached the PR branch before the
results commit (a GitHub Actions run for head `48e479f4` was created at 09:23:06 ET; the results commit `f084e3f3` is
09:28:51 ET), but no record timestamps the start of the run itself.

**This is a follow-up, not a retrofit.** Stage 2 was designed *after* seeing the original q220 results
and the audit (`AUDIT.md`). The original preregistration (`../review.md`, `../hypotheses.md`,
`../methods.md`) and its verdicts stand unchanged. Every stage-2 hypothesis is new, was motivated by the
original results, and is tested on data the original run never produced: fresh seeds on the same
corpus (replication) and an independently drawn corpus (out-of-corpus validation). The two are reported
separately. The original seeds are re-analysed only descriptively, to link stage 2 to the original
numbers.

## Research questions

- **RQ1 (mechanism).** Under scattered (MAR) loss with gap-closing, does the bottleneck (BN) reading fail
  because information is lost, or because concatenation treats non-consecutive samples as adjacent?
- **RQ2 (mitigation).** Does a timestamp-aware estimator, which uses only observed pairs at their true
  lag, recover the clean reading? Does segmenting at gaps do as well, or does it lose long-lag
  support?
- **RQ3 (controls).** How much of the change comes from reduced effective length, from fewer usable
  pairs, from the sampling pattern (scattered vs bursty), and from finite-sample randomness?
- **RQ4 (baselines).** Does the clean BN reading beat chance levels that account for each form's
  bottleneck-set size and for the decoder's tie-breaking?
- **RQ5 (transfer).** Do the RQ1–RQ4 answers hold on forms selected independently of the q161 corpus?

## Corpora and seeds

| set | forms | seeds | role |
|---|---|---|---|
| **S0** | q161 `build_corpus()` (16 forms) | 0–19 (the original seeds) | descriptive only; must reproduce the original gap-closed MAR cells exactly |
| **R1** | the same 16 forms | **1000–1019** (fresh) | confirmatory replication on the same corpus |
| **R2** | 30 new forms (below) | **2000–2019** | confirmatory out-of-corpus validation |

**R2 selection (blind to CRQA).** The forms are drawn with q162's `random_wiring` generator (each node an
arbitrary Boolean function of all other nodes) from `numpy.random.default_rng(220)`. That stream is
independent of q162's (seed 162). The draw takes n = 3 forms until 15 are included, then n = 4 forms
from the same stream until 15 are included, with at most 400 draws per n. A form is included iff:

1. its exact-IIT-4.0 major complex over reachable states has a core of at least 2 nodes (q161's rule);
2. its leave-one-node-out bottleneck set B (q161's `bottleneck_set`) is non-empty;
3. |B| < n, so a wrong pick is possible;
4. its truth table differs from every form already included.

Selection uses only exact-Φ quantities. No CRQA quantity is computed before a form is included. If
fewer than 15 forms qualify for some n, the shortfall is reported and the found forms are used.

**Primary R1 set.** The 12 R1 forms with |B| < n. On the other 4 forms every pick scores 1, so they
cannot show a difference between methods. Results on all 16 forms are reported as secondary.

## Data generation

As in the original: `recurrence.crqa.trajectory(rules, 600, default_rng(seed), flip=0.08, warmup=20)`.
One raw trajectory per (form, seed) is shared by every method and control below, so every comparison is
paired on the same system, trajectory, seed and mask.

## Observation masks

- **MAR(m)**, m ∈ {0.1, 0.2, 0.3, 0.5}: row t is kept iff `default_rng(10_000 + seed).random(600)[t] >= m`.
  This is the original `mar` operator's mask: it is nested across m and identical to the original run.
- **BURST(0.3)**: the original `burst` operator's mask (mean drop run 10) from `default_rng(10_000 + seed)`.

Every mask deletes whole rows: all channels share the same observation times.

## Estimators of the diagonal cross-recurrence profile (lags −10…10)

For channels x, y, the profile at lag k is the share of pairs (x at t, y at t+k) whose categorical values
match. The four estimators differ only in which pairs they use:

- **CLEAN**: the uncorrupted series; every pair. This is the existing `crqa.dcrp`.
- **A, GAPCLOSE (reference)**: delete the missing rows, concatenate, and run `crqa.dcrp`. Index lag k pairs
  samples whose true time difference can be larger than k.
- **B, TIMESTAMP**: keep the true times. At lag k, use exactly the pairs (t, t+k) whose two rows were both
  observed. Nothing is filled, interpolated or bridged.
- **C, SEGMENT**: split at every gap. At lag k, use the pairs (t, t+k) for which every row from t to t+k
  was observed, i.e. pairs inside one contiguous segment. Matches and pairs are summed across segments
  (pooled count-weighted rate).

A lag is **usable** when it has at least `MIN_PAIRS = 30` pairs. At 30 pairs the standard error of a
match rate near 0.5 is about 0.09, already above the 0.05 prominence floor; fewer pairs would let noise
pass as coupling. Peak and median are taken over usable lags only. A channel pair with fewer than 3
usable lags gets prominence 0 and is counted as **insufficient**. With no missing data every lag has
at least 590 pairs, so CLEAN and A match the existing implementation exactly.

## Controls

- **LEN**: the clean series cut to its first L rows, where L is the number of rows the mask observed.
  Contiguous, with no gaps: isolates reduced effective length.
- **THIN**: clean pairs, randomly subsampled at each lag (`default_rng(30_000 + seed)`) to the exact pair
  count B has at that lag. Matches B's pair counts without the mask's structure: isolates
  finite-sample noise at a given pair count.
- **Matched nulls**: each channel of the raw trajectory is permuted independently in time
  (`default_rng(20_000 + seed)`), then passed through the *same* mask and the *same* estimator:
  NULL-CLEAN, NULL-A, NULL-B, NULL-C. These give each method's own chance level, tie-breaking
  included.
- **BURST(0.3)** under A, B and C: the same expected loss with about 7 times fewer junctions. Isolates the
  sampling pattern.

## Decoders

The q161/q220 decoders are unchanged: `MAX_LAG = 10`, `PROM_FLOOR = 0.05`. Prominence is the
profile peak minus its median over usable lags. Coupling centrality is the legacy formula. Nothing is
re-tuned.

- **Primary BN score (tie-aware).** Let M be the set of nodes with maximal centrality. Score = |M ∩ B| / |M|.
  If every centrality is 0, M is all nodes, the score equals the uniform chance level |B|/n, and the run
  is flagged **no-evidence**. This removes the node-order bias the audit found.
- **Secondary BN score (legacy).** `argmax` with lowest-index tie-break, as in the original.
- **TD call**: legacy spread threshold. Descriptive only, because the audit shows TD has no clean
  signal.

## Statistics

- The unit of analysis is the form. A (form, seed) run is not an independent structure.
- **Effect** = mean over runs of the per-run paired difference in tie-aware BN score.
- **Interval** = 95% percentile CI from a two-stage hierarchical bootstrap (forms with replacement, then
  seeds with replacement within each form; 2000 resamples; seed 220), in `stats.cluster_boot`.
- Also reported: per-form mean differences, an exact sign test on them, form-level dz, ICC and effective
  n, the original seed-only interval for comparison, pair counts per lag, insufficient and no-evidence
  rates.
- **Three-way verdicts** (`decision.py`): CONFIRMED, REFUTED, or INCONCLUSIVE (the interval neither
  supports nor excludes the predicted effect). Low precision is never reported as evidence of no effect.
- **Margins.** 0.10 is the original q220 H1 margin for a material BN change; 0.05 is the original H3/H5
  margin. Both are inherited, not tuned. No multiplicity adjustment: each hypothesis below is one
  pre-specified test, and all are reported.

## Hypotheses (confirmatory)

Tested on R1 primary forms at MAR 0.3 unless stated. Every difference is in tie-aware BN score.

| id | claim | statistic | rule |
|---|---|---|---|
| **S2-H1** | gap-closing distorts: the timestamp-aware estimator beats gap-closing by ≥ 0.10 | B − A | superiority, margin 0.10 |
| **S2-H2** | little information is lost: B is within 0.10 of clean | CLEAN − B | non-inferiority, margin 0.10 |
| **S2-H3** | reduced length is not the cause: a contiguous series of the observed length is within 0.10 of clean | CLEAN − LEN | non-inferiority, margin 0.10 |
| **S2-H4** | segmenting loses long-lag support under scattered loss | B − C | superiority, margin 0.05 |
| **S2-H5** | gap-closing is harmless when gaps are few (BURST 0.3) | B − A at BURST 0.3 | equivalence, margin 0.05 |
| **S2-H6a** | out-of-corpus: B beats A on R2 | B − A on R2, MAR 0.3 | superiority, margin 0.05 |
| **S2-H6b** | out-of-corpus: clean CRQA beats chance on R2 | CLEAN − \|B\|/n on R2 | positive (lower bound > 0) |
| **S2-H7a** | clean CRQA beats the per-form uniform pick on R1 | CLEAN − \|B\|/n | positive |
| **S2-H7b** | clean CRQA beats its matched shuffled null on R1 | CLEAN − NULL-CLEAN | positive |
| **S2-H8** | the timestamp-aware reading at 30% loss still beats chance on R1 | B − \|B\|/n | positive |

**Interpretation rule (fixed now).**
- *Reconstruction distortion* is the supported mechanism iff S2-H1, S2-H2 and S2-H3 are all CONFIRMED.
- *Information loss* is supported iff S2-H1 is REFUTED and CLEAN − B ≥ 0.10 with lower bound > 0.
- Any other pattern is reported as mixed or inconclusive, with the numbers.
- "Segment at gaps", the original recommendation, is supported only if C is not worse than B (S2-H4 not
  CONFIRMED) *and* C − A > 0 with lower bound > 0.

## Descriptive analyses (no verdicts)

- Dose-response of A, B, C, LEN and THIN at m = 0.1, 0.2, 0.3, 0.5 on R1 and R2.
- **Mechanism diagnostics.** For A, the share of index-lag-k pairs whose true lag is not k (fabricated
  adjacency), by lag. For each method, the share of supra-floor pairwise peaks located at lag 0. The
  audit's hypothesis predicts a higher lag-0 share under A than under B or CLEAN.
- Pair counts per lag for B and C, and insufficient and no-evidence rates per method.
- S0: A at every MAR dose must reproduce the original per-run legacy BN hits exactly (an equivalence
  check of the new code against the original output); then B and C on the original seeds.
- Per-form tables for every confirmatory contrast.

## Sensitivity checks (pre-specified, descriptive)

On R1 at MAR 0.3, for B − A and CLEAN − B: `MIN_PAIRS` ∈ {10, 100}; flip ∈ {0.05, 0.12} (new trajectories,
same seeds); `MAX_LAG = 5`; the legacy argmax score instead of the tie-aware score; all 16 forms instead
of the 12 informative ones.

## Exploratory (labelled as such; no verdicts)

TD diagnosis: per-form spread distributions on clean R1 against the exact-Φ label, and where the
corpus-level threshold falls relative to them. One alternative is evaluated only with held-out-by-form
splits: a normalised-spread threshold fit on training forms by balanced accuracy, evaluated
leave-one-form-out on R1 and trained on R1 then tested on R2. Neither replaces the original decoder, and
neither is used to re-score any original or confirmatory result.

## Exclusions and deviations

- No run-level exclusions. Every (form, seed, condition) is scored. A run that raises an exception is
  recorded as a failure and reported.
- Forms are excluded only by the R2 inclusion rules and the R1 primary-set rule above.
- One full run. If a bug is found after it, the bug, its fix and the full re-run are recorded in
  `DEVIATIONS.md`, and both sets of numbers are kept.
- If every hypothesis fails, the results are reported as they are.

## Outputs

`results/stage2_runs.csv` (one row per form × seed × condition), `results/stage2_summary.csv`,
`results/stage2_stdout.txt`, `results/stage2_forms_r2.csv` (the R2 forms with truth tables and labels), the
diagnostics, and the sensitivity and exploratory outputs in separate files. They are registered in
`ci/reproduce.json`, separately from the original q220 check.
