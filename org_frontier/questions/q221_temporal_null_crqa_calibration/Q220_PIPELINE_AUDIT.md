# q220 pipeline audit, for q221 (read-only; q220 is not modified)

## Exact statistic

q220 does **not** run full CRQA: there is no embedding, no recurrence threshold, and no line-based
quantifiers. It computes a **categorical lagged cross-match profile**, a diagonal cross-recurrence profile
(DCRP) for binary series. The pipeline in `q220_observation_process_robustness/stage2/observe.py`:

1. **`lag_profile(times, x, y, max_lag=10, mode)`**
   - Rate at lag k = mean of 1[x_i = y_j] over the pairs at that lag, for k in −10..10.
   - In `"timestamp"` mode, pairs are matched by true time difference.
2. **`peak_prominence`**
   - Peak = the first maximum in lag order, over usable lags (count ≥ `min_pairs`).
   - Prominence = peak − median over usable lags.
   - Stage 2 uses `MIN_PAIRS` = 30.
3. **`coupling`** computes this for every unordered pair a < b. The prominence matrix is symmetric, and **no
   auto (i = i) profile is used**.
4. **`centrality(prom, 0.05)`**
   - Zeroes the diagonal and masks entries ≤ 0.05.
   - Node centrality = (row sum + column sum) / 2.
5. **`bottleneck_scores(cc, B)`**
   - Tie-aware score = |argmax-set ∩ B| / |argmax-set|.
   - If centrality is all zero, the argmax set is all nodes (score |B|/n) and the run is flagged
     "no evidence".

The trajectory generator is `org_frontier.recurrence.crqa.trajectory`: a deterministic rule, then an
independent flip on each node with probability `flip` (0.08 in stage 2), from a uniform random start, with
`warmup` steps.

## The structural target (q161)

- `q161_noise_robust_verdict.probe_noise_robust_verdict.core_indices`: the major complex, taken as the maximum
  over reachable states of PyPhi IIT-4.0 `maximal_complex`, computed on the **deterministic** TPM.
- `bottleneck_set`: for each node k, replace k's **rule** with the constant 0 ("freeze"; called "clamp-to-0"
  elsewhere in q221). Recompute the major-complex Φ of the modified 3-node network over its reachable states.
  The drop for k is base Φ − residual Φ, and B is the argmax of the drops, with ties within `TOL`.
- The residual network still contains every node. That is why a node outside the major complex (Y in the lead
  pair) can change the residual Φ, and therefore change B.
- q220 R2 eligibility: |core| ≥ 2, B ≠ ∅, |B| < n.

## The shuffle null

- `corruptions.shuffle_null` permutes **each channel's time order independently**.
- This destroys both cross-dependence and within-channel serial dependence.
- As a null for cross-dependence it is therefore valid only for serially independent channels. Gate E
  quantifies how badly it fails under persistence.

## Relevance to q221's claims

- The q220 decoder's inputs are exactly the cross-profiles (step 3), so the **cross-only** part of the pairwise
  representation in `THEORY.md` is what it can use. Auto-profiles are not inputs to it.
- The lead survivor pair P/Q is equal even on auto-profiles and marginals, so the result also covers any
  extension of q220 that adds one-point or self-recurrence information.
- The finite-sample run (`identifiability/adjudicate.py`) calls these functions unmodified. It does not use a
  reimplementation.

## Discrepancies found

- **None in the code path q221 uses.** Hassan's earlier finite-sample numbers came from a reimplementation.
  They agree with the repo pipeline wherever the same system was run (`results/pinned_env_runs/`), and the
  apparent discrepancies traced to rule-variant differences (A/B/C), not to the pipeline.
