# A platform binds only the people it both listens to and answers

*Taking input from people it never answers, or broadcasting to people it never listens to, adds nothing to what a platform holds together.*

## The question

The earlier posts in this series kept finding that a platform binds the people whose input can change its
decision. But a real platform's ties run in two directions: it reads some people (their clicks, bids,
data) and it answers some people (it shows them a result, and they act on it). These are not always the
same people. Some are only read, like a data source. Some are only told, like an audience. Which of them
end up bound together with the platform?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far
a setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

One platform and four people. The platform reads between one and four of them and says "go" only if all
the people it reads are in. It answers between zero and four of them: those people follow its decision.
Anyone it does not answer just keeps doing what they did last time. That gives 20 combinations, plus two
where the platform says "go" if anyone it reads is in. Predictions were committed before running.

## What we found

**The whole group holds together only when the platform reads and answers all four** (Φ = 4). In every
other combination the whole is fully reducible (Φ = 0).

**The tightest-bound group is always the platform plus the people it both reads and answers.** People it
only reads, and people it only answers, never join that group, in any of the 20 combinations.

| people both read and answered | tightest-bound group | its Φ |
|---:|---|---:|
| 0 | each person alone (platform not included) | 1.0 |
| 1 | platform + that person | 2.0 |
| 2 | platform + one or both of them (tie) | 2.0 |
| 3 | platform + all three | 3.0 |
| 4 | platform + all four | 4.0 |

We predicted the bound group's Φ would equal the number of people in the loop. That held for three and
four, but not for one or two, where it was 2 both times.

## What it means

In these models, reach is not what makes a platform a binding third party. A platform that collects data
from people it never answers, or broadcasts to people it never listens to, does not hold those people
together with it. Only the people in a two-way relation with it, read and answered, are bound. For
algorithmacy this gives a simple test of whom a platform binds: follow the loops, not the audience.

## Limits

Yes/no units, everyone updates at once, one platform with four people, and the people read and the people
answered always overlap from the first person on, so we did not test completely separate groups. Ties are
judged at a 1e-9 cutoff.

## The code

- Study: [org_frontier/studies/who_hears_back/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/who_hears_back)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/who_hears_back/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/who_hears_back/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/who_hears_back/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
