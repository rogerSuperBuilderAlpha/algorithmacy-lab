# v11 findings — a bot-merged coordination, and a refinement of channel and actor

v9 and v10 read projects where a human merges. v11 reads Kubernetes, where the Prow/Tide bot merges a pull
request mechanically once it has the required human approvals and passing checks. The merge actor is a
machine, which makes the case a model-bound field study, with the determination rule elicited from the
platform's documented process, and a test of the cognition arm's channel-versus-actor distinction on a real
arrangement. The result confirms the empirical predictions and refines the structural one. Reproduce with
[`analyze.py`](analyze.py).

## The machine merges, the humans approve

The Tide bot merged every one of the 150 pull requests, 140 as `k8s-ci-robot` and 10 as
`kubernetes-prow[bot]`, 100% by a machine. The approvals trace to humans, 15 distinct reviewers in the
partial view GitHub reviews give, none of them bots. The merge is mechanical and the decision is human, as
the documented process says. Where [v9](../event_series/)'s human maintainer both decided and merged, here
the two are split: the determination is the human approval, and the merge is a machine carrying it out.

## The bot is a member that commits nothing

The structural prediction was that the bot, a conduit, would be excluded from the irreducible core. It is
not. The elicited Prow model — the author opens a pull request, the human approval reads the pull request
and the code and commits, the bot merges if and only if approved, and the codebase changes on the merge —
is triadic at Φ of 2.0 with a major complex of approval, bot, and codebase. The bot is in the core, and
the author is the one excluded, the pattern v10 found under heavy review.

The bot is in the core because it sits in the merge cycle: the codebase reads the bot, the approval reads
the codebase, the bot reads the approval, and a relay inside a cycle is a member, where only a feedforward
relay is excluded. But membership is not the same as committing. Collapsing the mechanical merge step, so
that the codebase changes directly on the approval, leaves Φ at 2.0 with a major complex of approval and
codebase. The bot adds nothing to the binding. Its determination is a deterministic copy of the approval,
so it carries no information of its own; it is a member of the irreducible coordination that commits
nothing.

This refines the channel-versus-actor distinction rather than confirming it flat. The distinction is about
function, what a party commits of its own, and at the level of function the bot is a channel: it relays the
human decision and adds no information. At the level of membership the bot is a party to the coordination,
because it stands in the loop the determination runs through. The two come apart, and the computationalist
who calls the bot a mere channel is right about what it commits and wrong about whether it is in the
coordination at all. The actor the channel view misses is the human approval, which reads both the author
and the code and commits the determination the bot carries out.

## The gate moved upstream

In v9 the merge actor was the actor: the human who merged committed the determination, and the major
complex held the merger. Here the merge actor commits nothing, so the determination has moved upstream to
the human approval. Bot-merging disintermediates the committing from the merging: the machine does the
merge, and the veto lives in the approval, which is exactly where the OWNERS process places it. The
[disintermediation](../../threads/disintermediation/THREAD.md) prior reads on governance as the separation
of the act that commits from the act that executes.

## The predictions, settled

- **H1 — the bot is the universal merger.** Confirmed. 100% of merges by a machine.
- **H2 — the bot is a conduit, not an actor.** Refined. The bot is a member of the core but a functional
  conduit: it commits nothing, and removing it preserves the binding. Membership and committing come apart,
  and the channel-versus-actor distinction is the second one.
- **H3 — the gate moved upstream.** Confirmed. The merge actor commits nothing; the determination is the
  human approval, and the merge is mechanical.
- **H4 — the decision is human.** Confirmed. The approvers are humans spread across the reviewers, none
  bots.

## What v11 establishes

A bot-merged coordination separates the act that commits a determination from the act that executes it, and
the apparatus reads the separation. The machine that merges is a member of the irreducible coordination,
because it stands in the cycle, and a functional conduit, because it commits nothing of its own, and the
human approval upstream is the actor. The channel-versus-actor distinction the cognition arm tested is
sharpened: a party can be in the bound whole and still commit nothing, so being a member is not being an
actor. The limits stay marked. The window is a bounded recent sample, the GitHub-review approvals are a
partial view of an approval process that runs mostly through Prow labels, and the rule is elicited from the
documented institution, not from interviews, so no worker's experience of the arrangement is measured here.
