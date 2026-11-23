# Testing the matching pattern: it holds for "both" and "either" platforms, not for "exactly one"

*We wrote down the matching pattern before running it this time. It held on every new "both"/"either" case and failed on a platform that says go when exactly one person is in.*

## The question

The [last post](2026-11-23-gate-must-match.md) spotted a pattern after the fact: a go-between who depends
on a switch stays bound with the platform when it combines the message and the switch the same way the
platform combines what it hears. Patterns found after the fact need a fresh test, so this time we wrote the
predictions down first.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members. Three new "either"-platform cases with an "either" go-between, with the switch worked
by each of the other members. One "either" platform with a "both" go-between. Then a new platform rule,
"go if exactly one of the two is in", with an "exactly one" go-between and with a "both" go-between. Seven
cases, about 55 seconds.

## What we found

| platform says go if… | go-between passes on if… | switch worked by | whole-system Φ | prediction |
|---|---|---|---:|---|
| either | either | platform (control) | 2.0 | — |
| either | either | direct listener | 2.0 | held |
| either | either | the other listener | 2.0 | held |
| either | either | go-between | 2.0 | held |
| either | both | direct listener | 0 | held |
| exactly one | exactly one | platform | 0.5 | held |
| exactly one | both | platform | 0.5 | **failed** (predicted 0) |

**For "both" and "either" platforms, the pattern held.** Every new case went the predicted way. Counting
the earlier studies, that is 14 cases with no exception.

**For an "exactly one" platform, it failed.** The group stayed bound at Φ = 0.5 even when the go-between
used a different rule. That is the same value this platform gets with no switch at all.

Three of four predictions held, so the matching pattern is wrong as a general rule.

## What it means

The matching pattern is real for platforms where one person's input can settle the outcome on its own
("both": one "no" settles it; "either": one "yes" settles it). It does not carry over to an "exactly one"
platform, where no single input settles anything. For algorithmacy, how a go-between's terms must line up
with the platform's depends on the kind of rule the platform runs. A narrower version of the pattern,
limited to rules where one input can settle the outcome, is the next thing to test. It is not
established yet.

## Limits

Yes/no units, everyone updates at once, five members, two "exactly one" cases. Ties are judged at a 1e-9
cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/gate_match_test/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/gate_match_test)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_match_test/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_match_test/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/gate_match_test/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
