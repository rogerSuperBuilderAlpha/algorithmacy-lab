# How fast a group bounces back doesn't tell you whether it holds together

*We nudged one person in each of 108 setups and timed how long the group took to settle again. Settling speed had nothing to do with whether the group was integrated as a whole. How many resting patterns it had did.*

## The question

A natural guess is that a tightly integrated group should recover from a disturbance quickly and come
back to where it was. An earlier lab study found that the time a setup takes to settle from a random
start doesn't track integration. Here we tried a sharper test: knock one person off their current answer
and watch what happens.

We used the setups from two earlier posts: [habits that depend on your own last move](2026-11-23-memory-that-only-goes-one-way.md)
(36 setups, 13 of which hold together as a whole) and [taking turns](2026-11-23-taking-turns.md) (72
setups, none of which do). Integrated information Φ (IIT 4.0, computed exactly with PyPhi) had already
been computed and committed for all of them. It says how far a setup fails to split into independent
parts, and is not a claim that anything is alive or aware. This study only adds the timing.

## What we ran

For each setup we started from every state it can rest in (a fixed state or a repeating cycle), flipped
one person's answer, and counted the steps until it was resting again. We also recorded whether it came
back to the same resting pattern. 108 setups, about two seconds. Predictions committed first; three of
the four were wrong.

## What we found

**Bounce-back speed is the same either way.** The typical setup was resting again one step after the
nudge, whether it held together as a whole or not.

| among the 36 habit setups | holds together | splits apart |
|---|---:|---:|
| steps to settle after a nudge (median) | 1.0 | 1.0 |
| share of nudges that return to the same pattern (median) | 0.50 | 0.125 |
| resting patterns (median) | 2 | 5 |

**Integrated setups come back to where they were more often,** half the time versus one in eight. That
difference wasn't strong enough to count (p = 0.087).

**The clearest difference is how many resting patterns there are.** Setups that hold together have
about two; setups that split have about five (p = 0.003). We noticed this after looking at the data, so
it needs its own test before we lean on it.

**Slower recovery went with tighter pieces, not looser ones.** Across all 108 setups, the more steps
recovery took, the higher the tightest sub-group's Φ (rank correlation +0.37).

## What it means

Being integrated as a whole is not the same as being stable or quick to recover. A group can bounce
back fast and still split into separate parts, or take longer and be tightly bound. For algorithmacy, a
platform that absorbs shocks quickly isn't, for that reason, a binding third party. The better clue here
was how few settled outcomes the arrangement allows.

## Limits

Deterministic yes/no setups only, from two earlier studies, so not a random sample. One nudge at a time,
always to a person and never to the coordinator. The resting-pattern finding is exploratory.

## The code

- Study: [org_frontier/studies/flip_recovery/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/flip_recovery)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/flip_recovery/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/flip_recovery/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/flip_recovery/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the Φ values
are PyPhi's, and the timing comes from the study script.
