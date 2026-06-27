# bot_crqa — pre-registered hypotheses (behavioral complement to v11)

Committed before the analysis runs. v11 read Kubernetes' bot-merged history *structurally*: the Tide bot
merged all 150 pull requests, the humans approve, and the elicited Prow triad is triadic at Φ=2.0 with the
major complex {approval, bot, codebase} — the bot is in the irreducible core and the author is excluded.
v11 did not run the behavioral instrument. This runs cross-recurrence quantification (CRQA) on the same
frozen data (`../bot_merged/prs.csv`, `approvals.csv`) and asks whether the machine merger reads
behaviorally as a transparent conduit — its merge timing mechanically driven by upstream events — in
contrast to v9, where a human merge gate was the behavioral hub.

## Series

Three role-activity series, binned by day over the project span (2026-06-01 to 2026-06-22, 22 days):
author opens (PR `created`, 150 events), human approvals (`approved_at`, 50 events — a partial GitHub-review
view), and bot merges (`merged_at`, 150 events). Each day's count is quantized to three levels (0 = none,
1 = at or below the median positive day, 2 = above it). Pairwise CRQA uses a small max-lag (4 days) given
the short dense window.

## Predictions

- **bH1 — the conduit fires downstream.** The bot merge follows the upstream events: the peak lag of
  approval→merge and of open→merge is ≥ 0 (the merge does not lead). A machine that merges iff approved
  cannot precede its trigger.
- **bH2 — the merge is still behaviorally central.** Bot merges have the highest coupling centrality of the
  three roles and beat a time-shuffle null (p < 0.05): the merge is where activity routes, as in v9, even
  though the actor is a machine.
- **bH3 — approval and merge are the most coupled pair.** Of the three role pairs, approval–merge has the
  highest determinism, the bot mechanically carrying the human approval — matching v11's structural core
  {approval, bot}.
- **bH4 — the author is behaviorally peripheral.** The author-opens role has the lowest coupling
  centrality, matching v11's structural exclusion of the author from the core.

## What would refute each

bH1 fails if the merge leads approval or open (a negative peak lag). bH2 fails if merge is not the most
central role or does not beat the shuffle null. bH3 fails if approval–merge is not the highest-determinism
pair. bH4 fails if the author is not the least central role. The approval series is a partial view, so a
weak or null approval–merge coupling (bH3) is an expected risk, reported as it falls. Nulls and refutations
are results here.
