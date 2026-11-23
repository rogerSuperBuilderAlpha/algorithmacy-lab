# A platform's loop can run through other people, and then it binds the whole group

*If the people a platform answers pass its decision on to the people it listens to, the platform is bound with all of them.*

## The question

The [last post](2026-11-23-who-hears-back.md) found that a platform binds only the people it both listens
to and answers. People it only listens to, or only answers, are left out. But in real life the two groups
are often connected: the platform tells some people something, and they tell others, who then act in ways
the platform reads. Does a loop that runs through other people count?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

A platform and four people. The platform listens to persons 1 and 2 and says "go" only if both are in. It
answers persons 3 and 4, who follow its decision. We varied what persons 1 and 2 do:

- **separate groups**: persons 1 and 2 just keep doing what they did (tried with "both" and "either" rules)
- **relay both**: person 1 copies person 3, person 2 copies person 4
- **relay one**: only person 1 copies person 3
- **relay crossed**: person 1 copies person 4, person 2 copies person 3

And a control where the platform answers the same two people it listens to. Six cases, about ten seconds.
Predictions were committed before running.

## What we found

| setup | whole-system Φ | tightest-bound group | its Φ |
|---|---:|---|---:|
| platform answers whom it reads (control) | 0 | platform + persons 1 and/or 2 | 2.0 |
| separate groups | 0 | persons 1 and 2, each alone | 1.0 |
| relay one | 0 | platform + persons 1 and 3 | 2.0 |
| relay both | 2.0 | each relay loop, tied with all five | 2.0 |
| relay crossed | 2.0 | each relay loop, tied with all five | 2.0 |

**When the two groups are separate, the platform binds no one.** The tightest units are the people it
listens to, each on their own.

**A loop through another person binds just like a direct one.** Platform → person 3 → person 1 → platform
holds together at Φ = 2, the same as a direct two-way tie.

**Two relay loops bind the whole group.** With both relays in place, the full five-member system is
irreducible (Φ = 2), and in the states where both people the platform listens to are in, the whole group
ties with each loop as the tightest unit. The control, where the platform answers the people it reads
directly, never holds together as a whole.

One prediction was scored wrong only because of how we read ties: we check the tie list at the first
state where the top value appears, and there the whole group was not yet in it. It joins the tie in 2 of
the 16 states.

## What it means

A platform does not have to answer the people it listens to in order to bind them. If its decisions reach
them through other people, the loop still closes, and with two such chains the platform and everyone in
them become one irreducible whole. For algorithmacy, the people who carry a platform's decisions to others
are part of how it binds.

## Limits

Yes/no units, everyone updates at once, one platform with four people, one-step relays only. Ties are
judged at a 1e-9 cutoff and read at the first top state.

## The code

- Study: [org_frontier/studies/indirect_loops/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/indirect_loops)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/indirect_loops/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/indirect_loops/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/indirect_loops/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
