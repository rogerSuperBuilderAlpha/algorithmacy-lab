# One heavy voter breaks the counting rule

*The formula that predicted every equal-vote case fails as soon as one voter counts double.*

## The question

[Last time](2026-11-23-a-counting-law.md) a simple count predicted, exactly, how much weaker a noisy
vote's whole is than its strongest part. Count the groups of voters too small to settle the vote alone;
that number was the ratio, every time. But all those voters had equal votes. Real organizations rarely
work that way. What happens when one voter's reading counts double?

As before, we compute integrated information Φ (IIT 4.0, exactly, with PyPhi): how far a setup fails to
split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Four voters, three with one vote and one with two, five votes in all. The coordinator needs 1, 2, 3, 4 or
5 votes to say "yes", and misreads each voter 5%, 10% or 20% of the time. 15 cases, about 40 seconds.
Predictions committed first, including the formula's prediction for each quota.

## What we found

**For the in-between quotas, the rule fails.** With 3 of 5 votes needed, the formula predicted a ratio of
8. The real ratio is about 25 (24.54, 24.97, 25.46 across the three error rates), and it drifts with
noise. With 2 of 5 needed, it falls from 58 to 17 as noise rises.

| votes needed | predicted ratio | actual, 5% | 10% | 20% |
|---:|---:|---:|---:|---:|
| 1 or 5 | 1 | 1 | 1 | 1 |
| 2 or 4 | 4 | 58.33 | 30.55 | 16.59 |
| 3 | 8 | 24.54 | 24.97 | 25.46 |

**The heavy voter takes over.** In every in-between case the single most tightly bound part is the
coordinator plus the heavy voter, alone. With equal votes, the strongest parts were always a tie among
many small groups.

**The whole group is still never the strongest part,** and the "any yes" and "all yes" rules still bind
the whole as tightly as any part.

## What it means

The counting rule is a law about interchangeable voters. Give one party's reading more weight and the
coordinator's binding concentrates on that party; the three-way whole gets thinner in a way no count of
coalitions predicts. For algorithmacy, which is about living inside arrangements where a third party reads
you and binds you to others, this says weighting matters: who the coordinator listens to most decides
where the binding sits.

## Limits

One weight pattern; three error rates; the coordinator's errors are independent; people copy the
decision exactly. A different weighted rule (two pairs of equal voters) did follow the formula, so the
boundary is not yet mapped.

## The code

- Study: [org_frontier/studies/weighted_ratio_law/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/weighted_ratio_law)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/weighted_ratio_law/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/weighted_ratio_law/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/weighted_ratio_law/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
