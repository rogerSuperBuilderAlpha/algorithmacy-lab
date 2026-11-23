# The party nobody needs, and why vote weights don't matter

*Under noise, a weighted vote acts exactly like whatever yes/no rule it computes. Add one voter who can never change the outcome and the whole group stops holding together.*

## The question

[Last time](2026-11-23-one-heavy-voter.md), giving one voter a double vote broke a counting rule that had
predicted every equal-vote case. So when does a weighted vote behave like a plain "k of n" count, and when
does it not?

As in the rest of this series, a coordinator reads each person's yes/no signal (misreading each one 5%,
10% or 20% of the time), applies the rule, and everyone acts on the result. We compute integrated
information Φ (IIT 4.0, exactly, with PyPhi): how far the setup fails to split into independent parts.
It is not a claim that anything is alive or aware.

## What we ran

Two weight patterns for four voters, (1,2,2,2) and (1,1,2,3), with every quota from 1 to 7 votes.
22 cases, about 30 seconds. Predictions committed first.

## What we found

**Same yes/no rule, same numbers.** With weights (1,2,2,2) and 3 votes needed, any two voters carry it.
That is just "2 of 4", and it gives exactly the 2-of-4 values (strongest part 5 times the whole). Two
other weighted rules matched earlier weighted runs to every decimal, because they compute the same rule
with the voters relabeled.

**A voter nobody needs unbinds the whole.** With weights (1,2,2,2) and 2 votes needed, any single heavy
voter carries it alone, and the light voter can never change anything. The coordinator and the three
heavy voters bind exactly as "any yes among three" does (Φ 1.0415 at 20% error), but the whole group's Φ
is exactly zero, at every error rate. The coordinator reads the light voter and ignores what it reads, so
the light voter has no effect on anyone.

**One strongest voter takes over.** With weights (1,1,2,3), the coordinator plus the weight-3 voter is the
single strongest part, and how much stronger it is than the whole drifts with noise: from 96 times at 5%
error to 27 times at 20% (3 votes needed).

| weights, votes needed | whole group Φ at 20% | strongest part at 20% | strongest ÷ whole, 5% → 20% |
|---|---:|---:|---|
| (1,2,2,2), 3 = "2 of 4" | 0.0358 | 0.1791 | 5 → 5 |
| (1,2,2,2), 2 | 0 | 1.0415 | – |
| (1,2,2,2), 4 | 0 | 0.1465 | – |
| (1,1,2,3), 3 | 0.0188 | 0.5034 | 96.3 → 26.8 |

We had predicted a ratio of 4 for (1,2,2,2) with 4 votes needed. That was wrong: there is no ratio, because
the whole is not bound at all.

## What it means

Weights matter only through the yes/no rule they produce. For organizations read through algorithmacy,
this gives a concrete test: a party whose input the coordinator collects but never acts on is not just
unimportant. Including it means the arrangement no longer holds together as a whole, even though everyone
else is bound to the coordinator as tightly as before.

## Limits

Two weight patterns, four voters, three error rates; the coordinator misreads independently; people copy
the decision exactly.

## The code

- Study: [org_frontier/studies/weighted_equivalence/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/weighted_equivalence)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/weighted_equivalence/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/weighted_equivalence/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/weighted_equivalence/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
