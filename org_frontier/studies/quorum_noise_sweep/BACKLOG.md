# Experiment backlog (triadic forms), after quorum_noise_sweep

Ordered for the next runs. Each one is compact (minutes of compute on the venv).

1. **Correlated input noise on MAJ3.** Replace independent observation errors with a common-mode
   error (all of S's readings flip together with probability η, or a mixture with independent
   errors). Does the no-threshold positive whole Φ survive when the errors are correlated?
2. **Tie enumeration for noisy interior quorums.** Enumerate every candidate complex's φ per state
   (not just the one `maximal_complex` returns) for MAJ3 and 2of4 at η = 0.1 and 0.2, to settle
   whether {S,P3} / {S,P4} are symmetric ties and whether the full group is ever tied for maximum.
3. **The whole Φ = core φ / node-count regularity** (22 of 24 noisy interior cases; fails at η = 0.45
   on four parties). Test whether it holds on a five-party majority
   (3 of 5) at two noise rates, and on a weighted rule, before trying to derive it.
4. **Weighted quorums under the noise grid.** Weights (1,1,2,2), quotas 2–5, at η ∈ {0.05, 0.2, 0.4}:
   do the heavy-pair cores of probe 457 survive across rates (the open weighted half of O01)?
5. **Registry hygiene for O04.** `ternary_pivotality/` already answers the multivalued membership
   question (TWO_CONDITION_STATE_DEPENDENT) but OPEN_QUESTIONS still lists O04 as open; re-run its
   check and update the row, then extend with a ternary majority under input noise on the
   multivalued overlay.
6. **Asynchronous update on noisy quorums.** Does the positive interior Φ survive when parties update
   one at a time instead of synchronously?
