# No kind of memory makes a majority vote hold together

*We gave the people and the coordinator fixed habits that depend on their own last state. A majority vote never became one whole. "Any yes" and "all yes" broke when the people's memory only went one way.*

## The question

In the [last post](2026-11-23-the-slow-coordinator.md), members sometimes kept their last state at random.
Here the memory is a fixed habit, not chance. Each person's next move depends on the coordinator's
decision *and* on what that person did last time:

- **copy**: do what the coordinator says (no memory; the usual setup)
- **and**: say yes only if the coordinator says yes *and* you said yes last time (once you say no, you stay no)
- **or**: say yes if the coordinator says yes *or* you said yes last time (once you say yes, you stay yes)
- **toggle**: switch your answer whenever the coordinator says yes

The coordinator either applies the rule plainly, toggles its own last decision, or counts its own last
decision as a fourth vote. We measured integrated information Φ (IIT 4.0, computed exactly with PyPhi),
which says how far a setup fails to split into independent parts. It is not a claim that anything is
alive or aware.

## What we ran

Three rules ("any yes", majority, "all yes"), four habits for the people, three for the coordinator: 36
setups, no noise, about 24 seconds. For every state the system can reach, we computed Φ for every
sub-group. Predictions committed first; three of the five were wrong.

## What we found

**A majority vote never holds together as a whole,** under any of the 12 habit combinations. Whole-system
Φ is exactly zero in every one. Habits do bind smaller pieces: the coordinator plus one person reaches
Φ = 2. But the whole group always splits.

**"Any yes" and "all yes" break when people's memory runs against the rule.** Both normally have Φ = 3.
"Any yes" drops to zero when people, once they say no, can never go back to yes on their own. "All yes"
drops to zero when people, once they say yes, can never go back to no. The opposite habit leaves each at
Φ = 3.

| whole-system Φ, plain coordinator | copy | and (no sticks) | or (yes sticks) | toggle |
|---|---:|---:|---:|---:|
| any yes | 3 | 0 | 3 | 3 |
| majority | 0 | 0 | 0 | 0 |
| all yes | 3 | 3 | 0 | 3 |

**A coordinator that votes for itself binds less.** The whole group was the tightest-bound unit in 6 of
12 setups with a plain coordinator, 5 with a toggling one, and 2 with one that counts its own vote.
"Any yes" with a self-voting coordinator drops to zero under every habit.

## What it means

This post and the last one point the same way. When the third party leans on its own past (sticking
with its last decision, or counting itself as a voter), the whole arrangement binds less. What holds a
three-way arrangement together is the coordinator reading the others. A majority rule doesn't hold
together on memory at all; earlier posts found it does when the coordinator misreads people.

## Limits

Three-person yes/no models, no noise. Every person has the same habit. Four habits for people, three for
the coordinator. Why the habit that runs against the rule breaks it is something we observed, not
explained.

## The code

- Study: [org_frontier/studies/memory_rules/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/memory_rules)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/memory_rules/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/memory_rules/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/memory_rules/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
