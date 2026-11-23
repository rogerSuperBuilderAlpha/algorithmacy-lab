# A platform's decision can pass through a chain of people and still bind them all

*Make the loop between a platform and the people it listens to longer, through one, two or three go-betweens, and the whole group holds together exactly as tightly.*

## The question

The [last post](2026-11-23-loops-through-people.md) found that a platform's loop can run through another
person: the platform tells someone, they tell someone else, and that second person's choice feeds back
into the platform. Such a loop bound the platform as tightly as a direct one. Does that last as the chain
gets longer?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

A platform listens to two people and says "go" only if both are in. The first person hears the platform
directly. The second hears it through a chain of zero, one, two or three go-betweens, each passing on
what the previous one said. That gives systems of three to six members. We also re-checked the
two-chain setup from the last post. Five cases, about 100 seconds. Predictions were committed first.

## What we found

| go-betweens in the chain | members | whole-system Φ | whole group among the tightest-bound? |
|---:|---:|---:|---|
| 0 | 3 | 2.0 | yes |
| 1 | 4 | 2.0 | yes |
| 2 | 5 | 2.0 | yes |
| 3 | 6 | 2.0 | yes |

**Chain length makes no difference.** The whole system's Φ is exactly 2 at every length, the same value
as the basic three-way setup with no go-betweens.

**Everyone in the chain is bound.** The tightest-bound groups are always the same three kinds: the
platform with the person who hears it directly, the platform with the chain and the person at its end,
and the whole group. All tie at Φ = 2.

All four predictions held.

## What it means

In these models, the people who pass a platform's decisions along are bound to it as tightly as the
people it deals with directly, and adding more of them does not loosen the whole. For algorithmacy, a
platform's binding reach extends along chains of people relaying its decisions, at least for chains of
up to three.

## Limits

Yes/no units, everyone updates at once, go-betweens copy perfectly, chains of at most three, one platform
rule. Ties are judged at a 1e-9 cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/relay_length/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/relay_length)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/relay_length/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/relay_length/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/relay_length/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
