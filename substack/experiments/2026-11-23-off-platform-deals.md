# When buyers and sellers deal directly, the kind of deal decides whether the platform stays in

*If a deal needs both the partner and the platform, the platform locks onto that pair. If either one is enough, the pair holds together without it.*

## The question

The last two posts put buyers and sellers around a platform. When people only followed the platform, a
"some buyer and some seller" rule did not hold together at all; when people on the same side watched each
other, each side became its own unit. Real markets also have direct ties *across* sides: a buyer and a
seller who know each other and deal partly off the platform. What does that do?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

A platform, two buyers, two sellers, with the "some buyer and some seller" rule. Buyer 1 is paired with
seller 1, buyer 2 with seller 2. We tried:

- **"and" deals**: each person stays in only if the platform says go *and* their partner is in
- **"or" deals**: each person stays in if the platform says go *or* their partner is in
- **one pair fully off the platform**: buyer 1 and seller 1 only watch each other
- **one pair with an "and" deal**, the other pair just following the platform
- **four strict buyers**: all four buyers must be in, and at least one seller (seven units)

Six cases including a control, about 90 seconds. Predictions were committed before running.

## What we found

| setup | whole-system Φ | tightest-bound group | its Φ |
|---|---:|---|---:|
| "and" deals | 0.83 | platform + one trading pair | 6.0 |
| "or" deals | 1.19 | each pair on its own, without the platform | 2.0 |
| one pair off the platform | 0 | that pair | 2.0 |
| one pair with an "and" deal | 0 | that pair (ties with platform + the other pair) | 2.0 |
| four strict buyers | 0 | platform + the four buyers | 4.0 |

**With "and" deals, the platform locks onto a pair.** When one pair is active and the other is not, the
platform and that buyer and seller form the tightest unit in the system, at Φ = 6. In other states the
pairs tie at Φ = 2.

**With "or" deals, the pairs hold together without the platform.** The whole system is more integrated
than in any other case here (Φ up to 1.19), but the tightest units are the two buyer–seller pairs alone.

**This is the reverse of what same-side links did** in the previous post, where "and" links made each
side its own unit and "or" links let the platform lock onto a side. Which way the link runs, and what kind
it is, decides which group comes out on top.

**The strict-side pattern continues.** Two, three and four strict buyers give the platform-plus-buyers
group Φ = 2, 3 and 4.

Three of our five predictions were wrong. We expected "and" deals to leave the pairs on top, "or" deals to
keep the platform in, and a single "and" pair to integrate the whole; none of those happened.

## What it means

When people on a platform can also deal with each other directly, the platform does not simply lose its
grip. If each deal still needs the platform's go-ahead, the platform binds that relationship tightly. If
the relationship can keep going on its own, it holds together without the platform. For algorithmacy this
separates a platform that is a binding third party to a relationship from one the relationship can route
around.

## Limits

Yes/no units, everyone updates at once, at most seven units, one platform rule for the deal cases. Ties are
judged at a 1e-9 cutoff. The Φ = 6 three-member units are what PyPhi computed; we have not derived them.

## The code

- Study: [org_frontier/studies/off_platform_deals/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/off_platform_deals)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/off_platform_deals/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/off_platform_deals/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/off_platform_deals/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
