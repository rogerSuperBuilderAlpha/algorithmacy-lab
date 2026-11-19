# Candidate-specific finite-sample stress test (exploratory)

Independent NumPy reimplementation of q220's off-diagonal peak-prominence and tie-aware bottleneck scoring; **not** a run of the pinned PyPhi environment. Executed 2026-10-15, 300 trajectories per candidate, seeds 0..299, 600 observations, 20 warm-up steps, flip=0.08, lag window ±10, prominence floor 0.05.

First verified candidate: A truth tables X=00000000, Y=11110000, H=11001100; B truth tables X=01100110, Y=11110000, H=11001100 (little-endian states s=0..7). The parallel PyPhi run reports core {Y,H} and Φ=2 for both, with bottleneck sets A={Y,H}, B={H}.

| Statistic | A | B |
|---|---:|---:|
| Mean maximum pairwise prominence | 0.0419410 | 0.0489834 |
| Mean maximum centrality | 0.0161992 | 0.0268379 |
| Any prominence above 0.05 | 74/300 = 24.67% | 115/300 = 38.33% |
| No-evidence centrality | 226/300 = 75.33% | 185/300 = 61.67% |
| Mean tie-aware bottleneck score | 0.748889 | 0.365556 |
| Chance | 2/3 | 1/3 |

**Interpretation:** Equal population mean cross-channel profiles at tested lags do **not** imply identical finite-sample peak-prominence distributions. Most trajectories in both systems trigger q220's no-evidence condition. Mean bottleneck score minus set-size chance is about 0.0822 for A and 0.0322 for B. These are descriptive estimates across seeds on **one form per system**, not independent-form replication.

This is a separate finite-sample stress test, not a preregistered result, structural impossibility theorem, or evidence that the complete observed time series cannot distinguish the systems.

**Further checks needed:** independent execution with `stage2/observe.py`; form-level confidence intervals across genuinely distinct forms; candidate-target PyPhi replication; source-level literature novelty assessment.
