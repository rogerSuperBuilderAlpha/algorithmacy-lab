# What decides it is how the go-between treats the platform's own message

*A prediction written down in advance held on all four new cases. The group stays irreducible when the go-between's one sensitive point treats the platform's message the way the platform listens for it.*

## The question

The [last post](2026-11-23-a-rule-that-failed.md) showed that reversing a go-between's output changes
nothing, and that a go-between combining the platform's message with a switch works with a "both" platform
when it is "both"-like and with an "either" platform when it is "either"-like. Each of those go-between
rules has one input pattern where it behaves differently from the other three. Does the platform's message
or the switch's setting at that point decide the outcome? We picked four rules that tell the two apart and
wrote the predictions down first.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members, with the platform working the switch. Go-between rules like "pass on yes only if the
platform says yes and the switch is off", and its mirror images. Two with a "both" platform, two with an
"either" platform, plus the "both"/"both" control. Five cases, about 18 seconds.

## What we found

| platform says go if… | go-between's sensitive point | we predicted | whole-system Φ |
|---|---|---|---:|
| both | platform yes, switch yes (control) | — | 2.0 |
| both | platform **yes**, switch no | irreducible | 0.415 |
| both | platform **no**, switch yes | splits | 0 |
| either | platform **no**, switch yes | irreducible | 0.415 |
| either | platform **yes**, switch no | splits | 0 |

**All four predictions held.** The group stays irreducible when the go-between's sensitive point has the
platform saying what the platform itself listens for: "yes" for a "both" platform, "no" for an "either"
platform. The switch's setting at that point does not decide it.

**But the binding is weaker.** These new cases reach Φ = 0.415, not the 2.0 of the matched control, and
the whole group is no longer among the tightest-bound groups. Only the platform and its direct listener
reach the top value.

## What it means

When a go-between mixes a platform's message with something else the platform controls, whether the
group holds together depends on how the go-between treats the platform's own message at its one sensitive
point. For algorithmacy, people who pass on a platform's decisions stay part of its whole if they respond
to the same signal the platform responds to. They are bound most tightly when they treat the other
input the same way too.

## Limits

Yes/no units, everyone updates at once, five members, the platform always works the switch, one rule per
case. Ties are judged at a 1e-9 cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/odd_input/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/odd_input)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/odd_input/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/odd_input/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/odd_input/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
