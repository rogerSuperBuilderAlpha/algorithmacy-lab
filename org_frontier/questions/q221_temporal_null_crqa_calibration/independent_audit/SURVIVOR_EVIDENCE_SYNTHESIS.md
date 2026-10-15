# Independent synthesis of completed survivor screens and baselines

**Status: exploratory / retrospective audit, 2026-10-15. Not a preregistered confirmatory study.**

## New evidence inspected

The parallel agent has now committed:
- `identifiability/results/screen_exact.json`: 7,488 eligible recorded candidate pairs; 6,816 without constant nodes; 6,432 with matching channel marginals; 180 with matching self profiles and exact cross-profile recheck; **144** after excluding 48-group isomorphism, collapsing to **three** distinct 48-group representative classes.
- `identifiability/results/baselines_survivors.json` and `identifiability/baselines_survivors.py`: independent held-out trajectory baselines for the three representative pairs.
- `identifiability/results/verify_candidates.json`: earlier PyPhi/clamp comparisons for selected representatives.

The count 144 is a **pair count**, not 144 independent findings. The three representative classes are a more defensible summary.

## Held-out classification (200 trajectories per class, 400 total per pair)

| Pair | Marginal-only (a) | Self recurrence (b) | Cross recurrence (c) | 8x8 transitions (d) | Fitted transition likelihood (e) |
|---|---:|---:|---:|---:|---:|
| aff(9,6,10) vs aff(9,15,10) | 46.25% | 52.5% | 46.5% | 100% | 100% |
| aff(9,6,10) vs aff(9,15,12) | 50.25% | 42.75% | 44.0% | 100% | 100% |
| aff(9,6,11) vs aff(9,14,10) | 52.0% | 45.5% | 49.75% | 100% | 100% |

Source: `baselines_survivors.json`. Training uses seeds 44000–44099; test uses 44100–44299, per class. The script documents the feature construction and Wilson intervals. The 100% results concern **transition-aware** classification of the generating system; they do not demonstrate identification of exact Φ from an arbitrary new form.

### Adversarial reading

1. Matching **population mean** auto/cross recurrence rates at lags 0..20 is not equivalence of full observed trajectories or of finite-sample feature laws.
2. The near-chance results for simple summaries are evidence about these specified, fixed classifiers at this trajectory length and noise level, not an impossibility theorem for all algorithms operating on those summaries.
3. The full transition-count and fitted-transition likelihood baselines perfectly distinguish the systems in the recorded test sets. Thus **general observational non-identifiability is false for these examples**.
4. The surviving candidate pairs were selected retrospectively by a deterministic search. Their success is exploratory; no population-level inference over independently sampled network forms is justified.
5. The reported q161 bottleneck-set differences require exact PyPhi/clamp receipts for the **three specific survivors**; do not assume the first four previously verified representatives establish all three survivors.
6. The lab's bottleneck definition is intervention-convention dependent. Node-value relabeling, clamp-to-zero, and clamp-to-one sensitivity should remain disclosed.

## Scientific disposition

**GO** for a narrow methodological feasibility contribution: pairwise categorical recurrence summaries may discard information needed to distinguish different q161-defined bottleneck targets even when population marginal and auto/cross match profiles agree over the tested lag window.

**NO-GO** for claims of observational equivalence, a universal impossibility theorem, a new surrogate estimator, or a prospectively confirmed IIT result.

Before ready-for-review: verify the pinned exact-Φ outputs for each of the three survivors, execute the committed independent modules, finish targeted source-level prior-art review, and reconcile the PR body with the actual completed work. Keep the PR draft until those checks are documented.
