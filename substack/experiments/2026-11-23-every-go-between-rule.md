# Every possible go-between rule, checked

*We ran all 16 ways a go-between can combine a platform's message with a switch, under three platform rules. Every prediction we wrote down in advance held.*

## The question

The last five posts tested go-betweens who combine a platform's message with a switch, a few rules at a
time. The [last one](2026-11-23-the-sensitive-point.md) supported a rule: for "both" and "either"
platforms, what matters is how the go-between treats the platform's own message at its one sensitive point.
A go-between combining two yes/no inputs can follow only 16 possible rules, so we ran all of them under a
"both", an "either" and an "exactly one" platform. That is 48 cases, with five predictions written down
first.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members as before: a platform listening to two people, one hearing it directly, one hearing it
through a go-between, and a switch the platform works. Only the go-between's rule and the platform's rule
change. About four and a half minutes of computing.

## What we found

Whole-system Φ takes only four values across all 48 cases: 0, 0.415, 0.5 and 2.

| go-between… | "both" platform | "either" platform | "exactly one" platform |
|---|---:|---:|---:|
| ignores both inputs (always yes or always no) | 0 | 0 | 0 |
| ignores the switch | 0 | 0 | 0 |
| ignores the platform, follows the switch | 2 | 2 | 0.5 |
| says yes when the inputs differ (or when they agree) | 2 | 2 | 0.5 |
| sensitive point: platform yes, switch yes | 2 | 0 | 0.5 |
| sensitive point: platform yes, switch no | 0.415 | 0 | 0.5 |
| sensitive point: platform no, switch yes | 0 | 0.415 | 0.5 |
| sensitive point: platform no, switch no | 0 | 2 | 0.5 |

**All five predictions held.** Three patterns run through the table.

**Reversing the output never matters.** Each rule and its reverse give the same numbers in all 48 cases.

**A go-between who ignores the switch splits the group.** That sounds backwards, but in this setup the
switch only listens to the platform. If the go-between ignores it, nothing listens to the switch, so the
switch can be cut off at no cost.

**For "both" and "either" platforms, the sensitive point decides.** If the go-between's sensitive point
has the platform saying what the platform itself listens for, the group stays irreducible. It is bound
most tightly (Φ = 2) when the switch is treated the same way too. The "exactly one" platform stays at 0.5
for every rule that uses the switch.

## What it means

This closes the go-between-with-a-switch question for this setup: every possible rule has been checked,
and the rules predicted in advance hold on all of them. For algorithmacy, people relaying a platform's
decisions stay bound with it as long as they respond to the platform's own signal on the platform's terms
and the parts they depend on are tied back into the group. Passing the result on straight or reversed
makes no difference.

## Limits

Yes/no units, everyone updates at once, five members, and the switch always follows the platform. Ties are
judged at a 1e-9 cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/gate_census/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/gate_census)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_census/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_census/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/gate_census/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
