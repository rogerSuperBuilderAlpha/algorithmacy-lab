# With five people in step, the coin-flip decides every close call

*The IIT software settles tied states arbitrarily. With four people moving in step, that arbitrary pick
decided 91% of borderline cases. We added a fifth person. It now decides all of them.*

## The question

This lab asks whether a coordination setup hangs together as a whole or splits into parts. It answers
with integrated information, Φ, from IIT 4.0, computed exactly with the PyPhi software. Φ above zero means
no cut separates the parts without losing something. It measures structure, not life or awareness.

When several past or future states tie, the software takes the first on its list; its code says ties are
"arbitrarily broken (for now)". In [Four in step](2026-11-23-four-in-step.md) we found that this pick
matters more as more people copy the same coordinator: 0 affected setups with two people, 24 of 256 with
three, 116 of 128 borderline rules with four.

## What we ran

Five people each copy a coordinator's last signal, and the coordinator makes its next call from what the
five did. We ran all 62 rules that only count how many people said yes, and 128 "one-sided" rules (every
person can swing the call, but only when all agree on one particular answer). Each was scored the default
way and under every tie choice. Four predictions were pushed before the run.

## What we found

- **Every one of the 128 one-sided rules depends on the coin-flip.** Each hangs together under some tie
  choice and under none of them under every choice. The default picks "hangs together" for 75 of them.
- **More counting rules are affected.** 14 of 62 (23%) change verdict with the tie choice, up from 4 of 30
  (13%) with four people. Four more keep their verdict but their Φ moves between 0.299560 and 0.402506.
- **The rule from earlier still holds when ties are counted.** "Every person can swing the call when all
  agree" matches "hangs together under some tie choice" for all 190 rules.
- **"All yes" scores 5.0**, continuing 3.0 for three people and 4.0 for four.

All four predictions held.

## What it means

For groups of five people moving in step, PyPhi's single default answer is not a reliable verdict for
borderline rules; the tie-break decides it. The rules that clearly bind ("all yes", "any yes") or clearly
split (middle thresholds) are unaffected. Reporting the result under some tie choice and under every tie
choice removes the problem.

## Source

- Study: [org_frontier/studies/five_party_ties/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/five_party_ties)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/five_party_ties/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/five_party_ties/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/five_party_ties/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
