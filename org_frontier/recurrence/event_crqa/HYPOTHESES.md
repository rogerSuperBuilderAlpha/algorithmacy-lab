# event_crqa — pre-registered hypotheses (behavioral complement to v9)

Committed before the analysis runs. v9 read the PyPhi pull-request history *structurally*: the merge gate
is a veto player (wmayner 59% of merges), the elicited merge triad is triadic with the gate in the major
complex, and the lifecycle is directed but time-compressed (median open→merge latency 0 days). v9 did not
run the behavioral instrument. This experiment runs cross-recurrence quantification (CRQA) on the same
frozen data (`../event_series/prs.csv`, `reviews.csv`) and asks whether the gate that the structure names
also shows up behaviorally.

## Series

Three role-activity series, binned by month over the project span: author opens (PR `created`), reviews
(`submitted_at`), and merges (`merged_at`). Each month's event count is quantized into three levels
(0 = none, 1 = at or below the median positive month, 2 = above it) so the categorical cross-recurrence
reads matching activity levels across roles. The trajectory is the three columns (author, review, merge).

## Predictions

- **bH1 — the gate is the behavioral hub.** The merge role has the highest coupling centrality of the
  three, and that centrality exceeds a time-shuffle null (p < 0.05). The veto player the structure names is
  the behaviorally most-coupled role.
- **bH2 — the gate does not lead.** The peak lags author→merge and review→merge are ≥ 0 (author and review
  lead the merge or coincide with it); the gate does not lead the parties. At monthly resolution a lag of 0
  is expected and consistent with v9's time-compressed lifecycle.
- **bH3 — author–merge is the behavioral spine.** Of the three pairs, author–merge has the highest
  determinism (DET), the sustained coupling matching the institutional rule that a change enters iff a PR
  is opened and a party with merge rights merges it.
- **bH4 — behavior agrees with structure.** The role the behavioral centrality ranks first is the merge
  gate, the same role v9's structural major complex includes. The two instruments name the same party.

## What would refute each

bH1 fails if merge is not the most central role, or its centrality does not beat the shuffle null. bH2
fails if the gate leads either party (a negative peak lag). bH3 fails if author–merge is not the
highest-DET pair. bH4 fails if the behaviorally-central role is not the structural gate. Nulls and
refutations are results here, reported as they fall. At monthly resolution the lead-lag may be unresolved
(lags near 0), which bH2 anticipates and bH1/bH4 do not depend on.
