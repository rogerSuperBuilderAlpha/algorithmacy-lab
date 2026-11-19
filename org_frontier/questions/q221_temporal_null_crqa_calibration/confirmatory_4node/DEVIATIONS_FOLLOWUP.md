# Deviations log: JR/SHREC follow-up (`PREREGISTRATION_FOLLOWUP.md`, commit `74ef91c1`)

Times are ET on 2026-10-15. Commit timestamps are authoritative.

## Chronology

| time (ET) | event |
|---|---|
| 18:24 | SHREC timing/memory pilot (disclosed in the preregistration; no classification; seeds 999500–999619) |
| 18:25:21 | preregistration and power-analysis commit **`74ef91c1`**, pushed to the PR branch right after |
| 18:25:43 | `followup.py` created; it was never modified afterwards (file creation time equals modification time) |
| 18:25:56 | `--select`: 600/600 exact checks passed |
| after selection | smoke run |
| 18:26:21 | script frozen in **`21f705e9`** |
| 18:26:21–19:40:06 | data run: 12 chunks × 50 pairs; 4,425 s wall-clock; 13,033 s summed job time (3.62 job-hours, single-threaded); every job rc = 0 |

The data run stayed within the stated budget (≤ 6 CPU-hours and ≤ 150 min).

**Smoke run.** It used 2 pairs × 2 members × 10 trajectories with seeds 999000+. Its outputs were discarded, and it was within the rule. `--combine` was also dry-run on synthetic numbers in `/tmp`; it read no study data.

## Deviations

| # | what | effect on outcomes | label consequence |
|---|---|---|---|
| F1 | **Clerical.** The preregistration states the parent per-pair critical value as "z = 3.7476". The parent's exact value, `norm.ppf(1 − 0.05/280/2)` = 3.747548, rounds to 3.7475. The code uses the exact parent formula, which is what the preregistration's estimand definition requires. | none | none |
| F2 | **Memory floor briefly breached by other workloads.** MemAvailable fell to 1,929–1,937 MB at 18:44:54–18:45:04. Our three running jobs used about 0.37 GB RSS each. The guard held all new launches until memory recovered (next launch 19:02:15 at 9.4 GB), and no job was killed or restarted. | none | none |
| F3 | **Executor session interruption.** The executor's monitoring shell was aborted at about 19:00, and the session was resumed at 19:14. The launcher and jobs ran on, unaffected. At 19:14, every existing part file was validated: parts 000–300 had 50 pairs each, with contiguous q, all six classifier keys and n_test = 400; parts 300–450 were still being written by live jobs. After completion, all 12 parts were re-validated as complete. **No part was re-run or truncated, and no seed was reused.** | none | none |
| F4 | **The Miller–Madow secondary is uninformative by construction.** This was noticed after registration and before any data. When all cells of the 2×2×2 table are occupied (essentially always at T = 600, p = 0.08), the MM correction to TE is a constant, −1/(N ln 2). Train-SD z-scored nearest-centroid classification is invariant to a constant shift. So (c) essentially equals (b): correct counts coincide in 599/600 pairs (pair 162: 207 vs 206, where a rare empty cell breaks the constant shift), and separation decisions coincide in 600/600 (both 521/600). The secondary was run as registered and is reported, but it cannot address the TE-bias question. | none on the primary results | the secondary is read as non-diagnostic |

No bugs were found after the data were seen. There were no re-runs.
