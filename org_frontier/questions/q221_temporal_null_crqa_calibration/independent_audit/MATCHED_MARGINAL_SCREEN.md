# Follow-up screen: stationary marginal matching

**Exploratory screening of the 20 selected pairs**, not all 7,488 search candidates. An independent 8-state transition-matrix implementation using flip probability 0.08 finds that **13/20** pairs have matching stationary per-channel P(node=1) at numerical tolerance 1e-10. This is a screening result, not 13 independent discoveries or a population prevalence estimate.

A representative matched pair is `nsi(6,3,3)` versus `aff(6,9,5)`. All three stationary marginals equal 0.5 in both systems. The prior search reports exact equality of pairwise cross-channel lag profiles over ±20, and q161 targets A={Y,H} and B={H}, both with core {Y,H} and Φ=2.

This pair avoids the obvious marginal-frequency separation of `nsi(0,3,3)` versus `aff(6,9,5)`. It is **not** yet a full-observation identifiability counterexample. Within-channel lag structure, multivariate transitions, finite-sample variance, and higher-order statistics may still distinguish the systems.

**Next:** Compare within-channel lag profiles and finite-sample q220 features for the matched-marginal pair. Run the exact committed screening module in the pinned lab environment; this note reports independent calculations on the already-committed selected-candidate JSON. Retain draft status and avoid confirmatory or novelty claims.
