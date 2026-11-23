# A marketplace that needs "some buyer and some seller" does not hold together as a whole

*Put two buyers and two sellers around one platform. If the platform's rule treats them as sides, the whole setup splits into independent pieces.*

## The question

The earlier posts in this series put one coordinator between people who all play the same role. Real
platforms are often two-sided: buyers on one side, sellers on the other, and the platform decides when a
trade happens. Does that side structure change whether the platform and its users form one irreducible
whole?

We measure that with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Five yes/no units: a platform, two buyers, two sellers. Each person simply follows the platform's last
decision. We tried six rules for the platform:

- **everyone** must be in (control)
- **anyone** is enough (control)
- **a match**: at least one buyer and at least one seller
- **fixed pairs**: buyer 1 only trades with seller 1, buyer 2 with seller 2
- **exactly one** buyer and exactly one seller
- **one full side**: both buyers, or both sellers

For every state the system can reach, we computed Φ for every sub-group. Six cases, about ten seconds.
Predictions were committed before running.

## What we found

| platform rule | whole-system Φ | tightest-bound group |
|---|---:|---|
| everyone | 4.0 | all five |
| anyone | 4.0 | all five |
| a match | 0 | none |
| fixed pairs | 0 | none |
| exactly one per side | 0 | none |
| one full side | 0 | none |

**Only the two all-or-none rules hold together.** They reach Φ = 4, the known value for a hub with four
people, and the whole group is the one tightest-bound unit.

**Every rule that treats buyers and sellers as sides gives zero everywhere.** Not just the whole: no
sub-group, not even a single buyer with the platform, is irreducible. We had predicted the "a match"
rule would bind all five, and that fixed pairs would form buyer–seller trios. Both predictions were wrong.

## Why

Because everyone copies the platform, the people always end up agreeing with each other. From those
states, no one person can change the platform's next decision under a side rule. If everyone is in, a
match still happens when one buyer drops out; if everyone is out, one buyer showing up is not enough
without a seller. Under "everyone" or "anyone", by contrast, a single person is always decisive. This is
the same thing the lab found earlier for a 2-of-3 majority vote, now for rules built from sides and pairs.

## What it means

A two-sided market rule has built-in slack: from the states this system actually visits, no single buyer
or seller is decisive, so the platform and its users do not form an irreducible whole. The side structure
alone does not make a platform a binding third party in this sense. What binds is a rule under which each
person can change the platform's verdict.

## Limits

Yes/no units, everyone updates at once, people only copy the platform, one size (two plus two). Earlier
posts showed that a coordinator who sometimes misreads people can make a majority slightly integrated;
we did not test that here.

## The code

- Study: [org_frontier/studies/two_sided_platform/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/two_sided_platform)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/two_sided_platform/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/two_sided_platform/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/two_sided_platform/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
