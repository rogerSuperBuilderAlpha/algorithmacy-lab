# Independent audit — reproduction status (2026-10-15)

**Exploratory only. No confirmatory or IIT-specific claim.**

## Reproduction completed

The original local Python pilot from `q221_phase2/pilot.py` was rerun using NumPy's seeded default RNG (seed 2212026), 250 independent pairs per persistence, 240 time points, and 199 surrogate draws per method. All six observed rejection counts reproduced exactly:

| Persistence | Naive shuffle | Circular shift | Degenerate pairs |
|---|---:|---:|---:|
| 0.50 | 14/250 (5.6%) | 12/250 (4.8%) | 0 |
| 0.90 | 85/250 (34.0%) | 14/250 (5.6%) | 0 |
| 0.98 | 168/250 (67.2%) | 5/250 (2.0%) | 4 |

The original pilot and the GitHub port `null_pilot.py` implement the same RNG draw order, state-transition convention, absolute Pearson statistic, surrogate generation, and finite Monte Carlo p-value threshold. **The exact committed GitHub-port script has not yet been executed in the lab environment.** The table is therefore verified against the original local script, not claimed as a completed CI run of the GitHub module.

Constant series are assigned correlation zero, which is a design convention rather than a mathematically defined Pearson correlation. This should be tested for sensitivity in any later study.

## Still pending

- Run the exact committed `null_pilot.py` module in the lab environment and compare its JSON output with the recorded counts.
- Run `finite_sample.py` with q220's pinned `observe.py` module and record its outputs; do not cite its results before execution.
- Review the bounded exact-Φ search separately. The original A/B pair is **ineligible** as an IIT-bottleneck counterexample according to the parallel draft PR.
- Complete prospective literature novelty and surrogate-null validity assessments before any confirmatory preregistration.

## Scientific interpretation

Naive temporal permutation can substantially inflate false-positive rates for independent, persistent binary series under the tested correlation statistic. Circular shifts show better calibration in this limited pilot but are not generally valid without assumptions. The experiment is **not** an exact-Φ study and does not directly test the q220 structural bottleneck decoder.
