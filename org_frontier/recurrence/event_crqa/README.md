# event_crqa — behavioral cross-recurrence on the v9 PR/review history

The behavioral complement to [`../event_series/`](../event_series/) (v9). v9 read the PyPhi pull-request
history structurally — the merge gate is a veto player and sits in the elicited triad's major complex. This
runs cross-recurrence quantification on the same frozen data and asks whether the gate the structure names
is also the behaviorally most-coupled role.

- [`HYPOTHESES.md`](HYPOTHESES.md) — the four predictions, committed before the analysis.
- [`analyze_crqa.py`](analyze_crqa.py) — monthly role-activity series (author opens, reviews, merges),
  quantized to three levels; coupling centrality with a time-shuffle null, lead-lag, and per-pair
  determinism.
- [`FINDINGS.md`](FINDINGS.md) — the structural gate is the behavioral hub (p = 0.0005); the gate follows
  rather than leads; the most sustained coupling is review–merge, not author–merge.

Run from the repo root: `python org_frontier/recurrence/event_crqa/analyze_crqa.py`
