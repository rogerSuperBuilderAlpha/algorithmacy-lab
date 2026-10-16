# Adversarial disqualification of matched auto/cross candidate

**Exploratory audit; not a confirmatory result.**

Pair A `aff(6,9,5)` versus B `aff(11,9,5)` had matched stationary marginal probabilities and all auto/cross categorical recurrence mean profiles at lags 0..20. A fresh exact truth-table transformation check found **two** mappings under the 48-element group (six node permutations × eight per-node binary value flips): node permutation `(0,2,1)` and value-flip masks `6` or `7` (mask bits refer to the original node labels). These map A's deterministic truth tables exactly onto B's. Consequently the pair is **not distinct under the broader symmetry criterion** used in the parallel verification. The differing q161 bottleneck targets may arise from clamp-to-zero intervention conventions under value relabeling, rather than distinct unlabeled dynamics. This must be independently investigated before any invariance claim.

Independent 300-seed-per-system finite-sample simulation (T=600, warmup=20, flip=0.08, lag ±10, prominence floor 0.05) found:
- A max prominence mean 0.04898337, max centrality mean 0.02683794, any prominence >0.05 in 38.33%, no-evidence 61.67%.
- B max prominence mean 0.04855918, max centrality mean 0.02493362, any prominence >0.05 in 36.33%, no-evidence 63.67%.
- A logistic regression on 3 cross-channel prominence and 3 centrality features, trained on 200 trajectories per system and tested on 100 per system, achieved 53.5% test accuracy. This is a *trajectory-held-out* descriptive classification, not a proof of equal finite-sample feature laws.

**Disposition:** REJECT this pair as evidence of genuinely different dynamics under the 48-element symmetry. Preserve the valid restricted-profile observation but do not present it as a non-isomorphic IIT structural-identifiability theorem. Prioritize candidates explicitly certified non-isomorphic under the full symmetry group, and test whether their auto/cross profiles also match. Avoid further search expansion without a defined information-gain objective.
