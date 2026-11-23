# With four people in step, the software's coin-flip decides most close calls

*With two people, the IIT software's arbitrary tie-break never changed an answer. With three, it changed 24
of 256. We added a fourth person to see whether the problem grows. It does.*

## The question

This lab asks whether a coordination setup hangs together as a whole or splits into parts. It answers
with integrated information, Φ, from IIT 4.0, computed exactly with the PyPhi software. Φ above zero means
no cut separates the parts without losing something. It measures structure, not life or awareness.

Partway through each calculation, the software picks the most likely past and future states. When several
tie, it takes the first on its list; its code says ties are "arbitrarily broken (for now)". In
[Reading it backwards](2026-11-23-reading-it-backwards.md) we showed that, with three people, this
arbitrary pick is the only reason relabelled twins ever disagree.

The setup here: four people each copy a coordinator's last signal, and the coordinator makes its next call
from what the four did. When everyone copies the same signal, they are always in step, and in-step groups
produce many tied states.

## What we ran

There are 65,536 possible rules for the coordinator, too many to run, so we took 222: all 30 rules that
only count how many people said yes, 128 "one-sided" rules (every person can swing the call, but only when
all agree on one particular answer), and 64 rules picked at random. For each, we computed Φ the default way
and under every possible tie choice. We wrote three predictions down and pushed them before running.

## What we found

- **The earlier rule still holds when ties are counted.** "Every person can swing the call when all agree"
  matches "hangs together under some tie choice" for all 222 rules.
- **Most one-sided rules now depend on the coin-flip.** 116 of 128 (91%) change verdict depending on the
  tie choice, up from 24 of 56 (43%) with three people. We predicted a rise.
- **Even some counting rules are affected, which we predicted would not happen.** Four of the 30 counting
  rules, such as "yes when exactly one or two say yes", range from 0 to 0.235840 depending on the pick.
  Under the default, two of them score 0.235840 and their mirror images score 0.
- **The clear cases stay clear.** "All yes" and "any yes" score 4.0 under every choice, and the
  middle-threshold rules (at least two, at least three) score 0 under every choice.

Two of three predictions held; the one about counting rules failed.

## What it means

The more people move in step, the more the software's default answer is a coin-flip for borderline rules:
none with two people, 24 of 256 with three, and 116 of 128 one-sided rules with four. The way out is the
same as before: report whether a setup hangs together under some tie choice and under every tie choice,
rather than one arbitrary pick. Rules that clearly bind or clearly split are unaffected.

## Source

- Study: [org_frontier/studies/four_party_ties/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/four_party_ties)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/four_party_ties/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/four_party_ties/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/four_party_ties/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
