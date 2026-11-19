# Deviations log: 4-node target-A study

The preregistration (`PREREGISTRATION.md`) was committed in `2ad11e69`. Commit timestamps (ET) are authoritative.

| # | what | effect on outcomes | label consequence |
|---|---|---|---|
| D1 | **Clerical.** The preregistration header says "about 18:05 ET". The commit `2ad11e69` is timestamped 17:56:20 ET. The file creation times show the study code (`f4.py` 17:56:45, `screen4.py` 17:56:56, `study4.py` 17:57:37) was created **after** the preregistration file (17:56:20), consistent with the header's statement that the preregistration preceded the code. The time written in the header is wrong; the order is right. | none | none |
| D2 | **Smoke-test size.** Section 8 allows "≤ 2 pairs × 10 trajectories". The `--smoke` run used 2 pairs × 2 members × 10 trajectories (5 train + 5 test per member) with 9 false-pair surrogates, on seeds 999000+ / 999999+ (outside every study range). If "10 trajectories" is read per pair rather than per member, this was 2× the allowance. The smoke outputs were discarded. The smoke run also printed the exact population C1–C3 differences for the two smoke pairs; these are deterministic functions of the pair and not finite-sample outcomes. `study4.py` was **not modified after the smoke run** (its file creation and modification times are identical, 17:57:37 ET), and the frozen script was committed in `11d34a7c` before the study run started (17:57:53 ET). | none: no code, seed, feature, threshold or M was changed after the smoke run | none |
| D3 | **Post-hoc diagnostic added.** `te_bias_diag.py` (seeds 4380000+ / 4390000+, outside the study ranges) investigates why finite-sample TE separates 11 pairs whose exact population TE is identical. It was not preregistered and is labelled **exploratory**. It does not change any preregistered result. | none | its outputs are exploratory |

No bugs were found after the study run. No re-runs were performed. The budget was not exceeded: 460 s wall-clock with 2 concurrent jobs (about 2 cores each), well under 3 CPU-hours and 90 min.
