# A two-sided platform binds one side, the side where every member counts

*Make a platform strict with buyers and easy with sellers, and it holds together with the buyers only. Let buyers talk to each other, and they become their own unit.*

## The question

The [last post](2026-11-23-two-sided-markets.md) found that a platform matching "some buyer with some
seller" does not hold together with its users at all. Only rules where every single person can change the
outcome did. So what happens when a platform is strict on one side and loose on the other? And what if
the people on a side also pay attention to each other, not only to the platform?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far
a setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

A platform with two buyers and two sellers (three buyers in one case). Four rules where people just follow
the platform:

- **strict with buyers**: both buyers must be in, and at least one seller
- **strict with sellers**: the mirror image
- **strict with three buyers**: all three buyers, and at least one seller
- **either**: both buyers, or any one seller

And two cases using the "some buyer and some seller" rule, where each person also looks at the other
person on their side: they stay in only if their partner is in too ("and" link), or if either of them is
("or" link). Seven cases, about 30 seconds. Predictions were committed before running.

## What we found

| rule | whole-system Φ | tightest-bound group | its Φ |
|---|---:|---|---:|
| strict with buyers | 0 | platform + buyers | 2.0 |
| strict with sellers | 0 | platform + sellers | 2.0 |
| strict with three buyers | 0 | platform + all three buyers | 3.0 |
| either | 0 | platform + sellers | 2.0 |
| match, buyers and sellers linked by "and" | 0.83 | each side on its own, without the platform | 2.0 |
| match, linked by "or" | 0 | platform + whichever side is idle | 6.0 |

**The platform binds one side only, the side where every member counts.** Under "strict with buyers", each
buyer can block a trade, so the buyers are bound to the platform and the sellers drop out. Under "either",
any one seller can trigger a trade, so this time it is the sellers who are bound. Adding a third strict
buyer raised the bound group's Φ from 2 to 3.

**No rule binds both sides at once.** The whole five-person system is never the tightest-bound group.

**When people on a side watch each other, the side becomes its own unit.** With "and" links the whole
system does become slightly integrated (Φ = 0.83), but the tightest-bound groups are the two buyers
together and the two sellers together, without the platform (Φ = 2). With "or" links, the platform binds
tightly (Φ = 6) to whichever side it is still waiting for.

Two of our six predictions were wrong: we expected only the full buyer side to tie for first (single
buyer-platform pairs tied too), and we expected "or" links to integrate the whole system (they did not).

## What it means

In these models a platform does not bind "the market". It binds the people its rule makes decisive, and
lets the others float. When the people on one side coordinate among themselves, that side starts to hold
together on its own, and the platform's grip on the whole is weak. For algorithmacy this is a concrete
way to ask which participants a platform actually binds: look at whose choice can change its verdict.

## Limits

Yes/no units, everyone updates at once, at most six units, links only within a side. Ties are judged at a
1e-9 cutoff. The Φ = 6 value under "or" links is what PyPhi computed; we have not derived it.

## The code

- Study: [org_frontier/studies/asymmetric_sides/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/asymmetric_sides)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/asymmetric_sides/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/asymmetric_sides/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/asymmetric_sides/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
