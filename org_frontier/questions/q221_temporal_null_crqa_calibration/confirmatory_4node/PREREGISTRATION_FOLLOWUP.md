# Q221 4-node follow-up: resolving joint recurrence (C2) and SHREC (C4). Preregistration

**Registered:** 2026-10-15. The commit that adds this file is the registration; its timestamp is authoritative.
No follow-up data have been generated when this is committed. The only pre-registration computations are:
- the power analysis (`power_followup.py` → `results/power_followup.txt`), which uses only the published
  4-node summary;
- a SHREC timing/memory pilot on 120 trajectories of one system with seeds 999500–999619. It measured time and
  memory only, with no classification, and its output was discarded.

**Parent study:** `PREREGISTRATION.md` (commit `2ad11e69`). Its H3 verdicts for C2 (23/40, Wilson-Bonferroni
[0.370, 0.757]) and C4 (28/40, [0.487, 0.851]) were *mixed (unresolved)*. This follow-up estimates the same
estimand on fresh pairs and fresh seeds. Everything not stated here is as in the parent preregistration: family
F4, generator, T = 600, warmup 20, flip 0.08, features, and nearest-centroid classifier with train-SD z-scoring.

## 1. Estimand

For classifier C ∈ {C2, C4}, π_C is the proportion of recurrence-equal, non-isomorphic orbit pairs that C
separates. **Separates** uses the parent's per-pair rule *unchanged*:
- 100 training and 200 test trajectories per member (400 test trajectories per pair);
- Wilson lower bound > 0.5 at the parent's per-pair critical value **z = 3.7476** (two-sided α = 0.05/280).

The per-pair threshold is held fixed rather than re-derived from the new M, so that π_C is the same quantity
the parent study left unresolved.

**Population:** the 1,832 unordered orbit pairs among the 1,872 from the exact screen (`screen4.py`) that were
not used as parent study pairs.

## 2. Sample

- **M = 600** orbit pairs, drawn uniformly without replacement from those 1,832 with `default_rng(5210002)`.
  They are sorted, as in `screen4.py`, by (O1, O2) before drawing.
- **Representatives:** a is the canonical member of O1; b is the lexicographically smallest member of O2 in a's
  recurrence-equal class (the parent rule).
- **Exact checks before any trajectory is generated, on all 600 pairs:**
  - exact brute-force profiles and marginals equal at lags 0..20;
  - exact TPMs differ;
  - non-isomorphic under all 384 maps.
- **Trajectories:** pair index q (0..599), member m (0/1), run r (0..299): `default_rng(5220000 + 1000·q +
  500·m + r)`. Runs r < 100 are training and 100 ≤ r < 300 are test.
- **Seed disjointness:** the seed range 5,220,000–5,819,799 and the sampling seed 5210002 are disjoint from every
  earlier q221 seed: 4210001/2, 4220000–4259799, 4290000+q, 4380000–4430000, 44xxx, 47xxx and 999xxx smoke.

## 3. Hypotheses and decision rules

There are **no directional predictions** for C2 or C4. Each classifier is classified by this rule:

| verdict | condition on the Wilson interval for π_C (Bonferroni over **2** classifiers, two-sided α = 0.025 each, z = 2.2414) |
|---|---|
| **generally separates** | lower bound > 0.5 |
| **generally fails** | upper bound < 0.5 |
| **unresolved** | otherwise |

The primary analysis uses the 600 fresh pairs only. A secondary analysis pools them with the parent's 40 (640
pairs, same rule); it is descriptive and does not change the primary verdict.

## 4. Power (`results/power_followup.txt`)

These are exact binomial probabilities of a resolved verdict in the true direction:

| true π | M = 600 |
|---|---|
| 0.70 (the SHREC point estimate) | ≈ 1.00 |
| 0.575 (the JR point estimate) | 0.93 |
| 0.55 | 0.58 |
| 0.45 | 0.58 |

M = 600 is chosen for ≥ 0.9 power at the JR point estimate. If π is close to 0.5, an unresolved verdict remains
possible, and it will be reported as such. Sampling without replacement from a finite population of 1,832 makes
the binomial calculation conservative.

## 5. Manipulation checks (pipeline validity; not hypotheses)

The R classifier (176 features) and C0 (transition likelihood) are run on every pair, as in the parent.

| check | pass condition |
|---|---|
| R | mean accuracy within [0.45, 0.55], and fewer than 5% of pairs separated |
| C0 | ≥ 95% of pairs separated |

**If either check fails,** the C2/C4 verdicts are reported as **unresolved (pipeline check failed)**.

## 6. Secondary: TE estimator bias (descriptive only; no verdict)

For every pair, report the following:
- (a) exact population TE separation (lag-1, history 1, 12 ordered pairs; "separates" means some feature
  differs by more than 1e-12);
- (b) plug-in TE nearest-centroid separation (the parent's C1, same per-pair rule);
- (c) **Miller–Madow bias-corrected TE** nearest-centroid separation. TE is H(a,b) + H(b,c) − H(b) − H(a,b,c),
  and each plug-in entropy gets (K_nonzero − 1)/(2N ln 2) added;
- the agreement table of (b) and (c) with (a).

These results bear on whether the parent's C1 finite-only separations were estimator artefacts. They are labelled
descriptive or exploratory and are not used for any verdict. Exact population C2 (JRR) separation is also reported
with its agreement table.

## 7. Stop rules

- **Exact-check failure:** if any of the 600 exact checks fails, stop before generating trajectories and report
  it as a counterexample to the implementation or to Proposition 1.
- **Locked after the first data run:**
  - no other seeds, no changes to M, features, classifiers or thresholds;
  - no re-runs except an identical re-run of a crashed chunk (same seeds), which is logged in
    `DEVIATIONS_FOLLOWUP.md`.
- **Smoke tests:** seeds 999000–999999 only, with at most 2 pairs × 2 members × 10 trajectories in total. The
  outputs are discarded.
- **Bugs:** a bug found after data are seen is fixed in a separate commit and logged. Any affected verdict
  becomes exploratory.

## 8. Compute budget (stated before running)

- **Totals:** ≤ **6 CPU-hours** and ≤ **150 minutes wall-clock** for all follow-up jobs together. The estimate is
  about 21 s per pair single-threaded, so about 3.5 CPU-hours.
- **Jobs:** each runs through `box-run` with a 1.5 GB memory cap, single-threaded (OMP/NUMBA/OPENBLAS threads = 1;
  measured peak RSS 361 MB). There are **at most 3 concurrent jobs**, each a chunk of 50 pairs.
- **Memory guard:** a new chunk starts only if MemAvailable ≥ 3 GB. If MemAvailable drops below 2 GB, no new
  chunk starts until it recovers.
- **If the budget would be exceeded,** stop launching chunks. Pairs are processed in random draw order. The
  completed pairs are reported as **exploratory**, with no confirmatory verdict.

## 9. Outputs

| file | contents |
|---|---|
| `followup.py --select` | `results/followup_pairs.json` (pairs and exact checks) |
| `followup.py --part LO HI` | `results/followup_part_LO_HI.json` |
| `followup.py --combine` | `results/followup.{txt,json}` |
| `DEVIATIONS_FOLLOWUP.md`, `RESULTS.md` (follow-up section) | deviations and results |
| `test_confirmatory_4node.py` | new tests |
