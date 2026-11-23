# A group holds together only if the coordinator moves first, and not alone

*We tried all 75 ways to split a coordinator and three people into turns, where some act together and some wait. The group stayed whole in 13 of them: the ones where the coordinator acts in the first turn alongside at least one person.*

## The question

The [taking-turns post](2026-11-23-taking-turns.md) found that if the coordinator and three people act
strictly one at a time, the group never holds together as a whole. Acting all at once, "any yes" and "all
yes" do. What about everything in between: some people acting together, others waiting their turn?

We measured integrated information Φ (IIT 4.0, computed exactly with PyPhi), which says how far a setup
fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Four members can be split into turns in 75 ways (one where everyone acts at once, 24 strictly one at a
time, and 50 mixed). Three rules ("any yes", majority, "all yes") make 225 setups, with no noise, in about
23 seconds. For every state the system can reach, we computed Φ for every sub-group. Predictions
committed first. We expected only the everyone-at-once schedule to stay whole. That was wrong.

## What we found

**The coordinator has to act first, and with company.** "Any yes" and "all yes" hold together as a whole
in exactly 13 of the 75 schedules: the ones where the coordinator's turn comes first and at least one
person acts in that same turn. Every other schedule splits.

| first turn | how many schedules | whole-system Φ |
|---|---:|---:|
| coordinator and all three people (everyone at once) | 1 | 3 |
| coordinator and two people | 3 | 2 |
| coordinator and one person | 9 | 1 |
| anything else | 62 | 0 |

**The more people act with the coordinator, the tighter the group.** Φ drops from 3 to 2 to 1 as fewer
people share the coordinator's turn.

**A coordinator acting alone first gets cut out.** If it goes first by itself and then everyone else
acts, the three people bind each other (Φ = 6) and the coordinator drops out, the same pattern as in
strict turn-taking.

**Majority never holds together,** under any of the 75 schedules.

## What it means

Timing decides whether a third party binds a group. It isn't enough for the coordinator to act at all,
or to act first. It has to act at the same moment as some of the people it coordinates. A coordinator
that always moves alone, before or after everyone else, becomes a relay or a bystander. For algorithmacy,
a platform binds people most when its decisions and their actions happen together.

## Limits

Three-person yes/no models, no noise, fixed schedules. The "first turn with company" rule is what the
table shows. We spotted it after the run, so it needs testing on other rules before we rely on it.

## The code

- Study: [org_frontier/studies/partial_sync_quorum/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/partial_sync_quorum)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/partial_sync_quorum/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/partial_sync_quorum/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/partial_sync_quorum/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
