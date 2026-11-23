# The go-between's switch may need to work the same way the platform does

*Whether a switch-dependent go-between stays bound with the platform depends on how it combines the message with the switch. "Both" fits a "both" platform; "either" fits an "either" platform.*

## The question

The [last post](2026-11-23-gate-source.md) found that a go-between who passes a platform's message on
"only if the switch is on" stays bound with the group as long as someone inside works the switch. A
go-between who passes it on "if either the platform or the switch says so" did not, at least when the
platform worked the switch. Is that because of who works the switch, or something else?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members: a platform that listens to two people, one who hears it directly, one who hears it
through a go-between, and the switch. For the "either" go-between, we let each member in turn work the
switch. Then we swapped the platform's own rule from "go only if both are in" to "go if either is in", and
tried both kinds of go-between with it. Seven cases, about 16 seconds. Predictions were committed first.

## What we found

| platform says go if… | go-between passes on if… | switch worked by | whole-system Φ |
|---|---|---|---:|
| both | either | platform | 0 |
| both | either | direct listener | 0 |
| both | either | the other listener | 0 |
| both | either | go-between | 0 |
| both | both | the other listener | 2.0 |
| either | both | platform | 0 |
| either | either | platform | 2.0 |

**Who works the switch does not rescue the "either" go-between.** With a "both" platform, it stays at
Φ = 0 no matter which of the four members works the switch.

**What matters is whether the rules match.** Putting this together with the last post, every time the
go-between's rule matched the platform's ("both" with "both", "either" with "either") the whole group was
bound at Φ = 2. Every time they differed, it was 0. That is ten cases, five each way. We noticed this
pattern after the run; we did not predict it, and only one case has "either" on both sides.

Two of six predictions held. We had expected the "either" go-between to come back once someone inside
worked the switch.

## What it means

In these models, a go-between who also depends on a switch stays part of the platform's group only if it
combines the platform's message with the switch the same way the platform combines what it hears. For
algorithmacy, that suggests a platform binds people along a chain when they handle its decisions on the
same terms it uses itself, and the chain splits where the terms change. That is a pattern to test next,
not a settled rule.

## Limits

Yes/no units, everyone updates at once, five members, only one "either"–"either" case, and the matching
pattern was found after the fact. Ties are judged at a 1e-9 cutoff, pooled over all states where the top
value appears.

## The code

- Study: [org_frontier/studies/or_gate_source/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/or_gate_source)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/or_gate_source/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/or_gate_source/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/or_gate_source/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
