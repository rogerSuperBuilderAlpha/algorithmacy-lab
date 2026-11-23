# Who flips the switch decides whether the group holds together

*A go-between who waits on an outside switch splits the group. Let someone inside the group work the switch, and the whole comes back together, at least for one kind of switch.*

## The question

The [last post](2026-11-23-relay-flips.md) found that a go-between who passes a platform's message on only
when an outside switch is on makes the whole group come apart (Φ = 0). There, the switch just kept its own
setting, and nothing in the group touched it. What if someone inside the group works the switch?

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members as before: a platform that says "go" only if two people are both in, one person who hears
the platform directly, one who hears it through a go-between, and the switch. We changed who sets the
switch: nobody (it keeps its own setting), the platform, the person who hears the platform directly, or the
go-between. We also tried a go-between who passes the message on if either the platform or the switch says
so. Six cases, about 18 seconds. Predictions were committed first.

## What we found

| go-between passes it on… | switch set by | whole-system Φ | switch in the tightest-bound group? |
|---|---|---:|---|
| only if the switch is on | nobody (keeps itself) | 0 | no |
| only if the switch is on | the platform | 2.0 | yes |
| only if the switch is on | the direct listener | 2.0 | yes |
| only if the switch is on | the go-between | 2.0 | yes |
| if either says so | nobody (keeps itself) | 0 | no |
| if either says so | the platform | 0 | no |

**Inside hands on the switch bring the group back.** For the "only if the switch is on" go-between, it does
not matter which member sets the switch. Each one restores the whole to Φ = 2, the same as with no switch
at all, and the switch becomes part of the tightest-bound group.

**The "either" go-between is different.** Even with the platform setting the switch, the whole stays at
Φ = 0, and the loop through the go-between drops out of the tightest-bound groups. Only the platform and
its direct listener reach the top value of 2. We had predicted the whole would come back here. It did not,
and this study does not show why.

Five of six predictions held.

## What it means

A go-between who depends on an outside condition breaks up the group the platform binds. If someone in the
group controls that condition, the condition is bound in too. For algorithmacy, a platform's binding reach
includes the switches its own people work, but not switches no one inside touches. The "either" result
shows this is not a general rule for every kind of switch.

## Limits

Yes/no units, everyone updates at once, five members, one platform rule, one inside-driven case for the
"either" go-between. Ties are judged at a 1e-9 cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/gate_source/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/gate_source)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_source/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_source/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/gate_source/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
