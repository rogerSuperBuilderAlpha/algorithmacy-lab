# v11, pre-registered hypotheses — a bot-merged coordination, and the channel-or-actor test

Committed before the analysis runs. The series is a bounded recent window of Kubernetes pull requests
(`prs.csv`, `approvals.csv`), a project whose Prow/Tide bot merges a pull request mechanically once it has
the required human approvals and passing checks. The totals are known — 150 merged pull requests, 50
approvals captured as GitHub reviews — but no merge-actor distribution, approver set, or Φ result has been
computed.

## A model-bound field case, and what it tests

This is a model-bound field study: a real coordination read against the catalog, with the determination
rule elicited from the platform's documented process instead of from interviews. Kubernetes documents the
rule. A change enters the codebase if and only if a reviewer lgtms, an OWNER approves, and CI passes, after
which the Tide bot merges. The merge actor is a machine, which makes the case a direct test of the
cognition arm's channel-versus-actor distinction on real data: the merge bot is the computationalist's
channel, a function that commits the institutional decision and nothing of its own, and the question is
whether the bot is a member of the irreducible coordination or a conduit.

A caveat fixed in advance: Kubernetes approves mostly through Prow label commands, outside the GitHub reviews, so
the 50 approvals captured here undercount the human approval, which the documented process requires on every
merge regardless.

## Predictions

- **H1 — the bot is the universal merger.** The merge actor is the Tide bot on essentially every merged
  pull request, a mechanical conduit where a human once decided.
- **H2 — the bot is a conduit, not an actor.** In the elicited Prow model, where the codebase changes iff a
  human approval is in place and the bot then merges, the bot is excluded from the major complex. The
  irreducible coordination is the human-approval loop — author, approver, codebase — and the bot is the
  channel. This is the channel-versus-actor distinction of [the cognition arm](../../cognition/) confirmed
  on a real arrangement: the documented merge bot is the channel the computationalist would see, and the
  human approval is the actor.
- **H3 — the gate moved upstream.** Where [v9](../event_series/)'s human maintainer was both the actor and
  the merge actor, here the merge actor commits nothing of its own and the determination sits in the human
  approval. Bot-merging disintermediates the merge step and moves the veto upstream to the approval, the
  [disintermediation](../../threads/disintermediation/THREAD.md) prior read on governance.
- **H4 — the decision is human, the merge is mechanical.** The approving parties are humans, distinct from
  the bot and spread across the project's reviewers, so the determination the bot commits is one humans
  made.

## What would refute each

H1 fails if a meaningful share of merges were human. H2 fails if the bot sits in the major complex
of the elicited model, an actor, inside the bound whole. H3 fails if the merge actor still carries the
determination, with no human approval upstream. H4 fails if the approvals trace to the bot or a single
party rather than a spread of human reviewers. Nulls and refutations are results here, reported as they
fall.
