# bot_crqa — behavioral cross-recurrence on the v11 bot-merged history

The behavioral complement to [`../bot_merged/`](../bot_merged/) (v11, Kubernetes/Prow). v11 read the
bot-merged history structurally — the Tide bot merges every PR and sits in the elicited triad's major
complex, with the author excluded. This runs cross-recurrence on the same frozen data and asks whether the
machine merger reads behaviorally as a transparent conduit, against v9, where a human merge gate was the
behavioral hub.

- [`HYPOTHESES.md`](HYPOTHESES.md) — the four predictions, committed before the analysis.
- [`analyze_crqa.py`](analyze_crqa.py) — daily role-activity series (author opens, human approvals, bot
  merges), quantized; coupling centrality with a time-shuffle null, lead-lag, and per-pair determinism.
- [`FINDINGS.md`](FINDINGS.md) — all four hypotheses refuted, coherently: the bot merge has no independent
  behavioral signature (centrality below chance), the author-opens rhythm dominates, and the merge is a
  same-day echo of it. The machine conduit is the behavioral opposite of v9's human hub.

Run from the repo root: `python org_frontier/recurrence/bot_crqa/analyze_crqa.py`
