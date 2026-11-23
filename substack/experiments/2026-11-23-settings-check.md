# Change the measuring tool's settings, and the yes/no answer stays the same

*We re-ran 271 small coordination setups under seven settings of the IIT 4.0 software. The verdict on which ones hang together never moved. The size of the number did.*

## The question

This lab asks one yes/no question of a coordination setup: does it split into independent parts, or
does it hang together as a whole? A chat between one person and one system splits. A hiring system that
only advances a résumé when both the applicant and the manager have signalled does not. We answer the
question with integrated information, Φ, from IIT 4.0, computed exactly with the PyPhi software. Φ above
zero means no cut separates the parts without losing something. It is a measure of structure, not a
claim that anything is alive or aware.

Every result so far used PyPhi's default way of cutting a system into parts. The software offers others.
If the answer changed with that choice, the lab's verdicts would be an artifact of a setting nobody
chose on purpose. So we checked.

## What we ran

Every three-party setup in which a coordinator reads two people and each person reacts only to the
coordinator: 256 setups, 24 of which hang together under the default. Plus 15 named setups the lab's
papers rely on (quorum votes, a dispatch platform, a rotation, two disjoint pairs, and others). Each one
under seven settings: four ways of cutting, one with an extra "cut everything" option, one with a
different normalisation, and one cutting scheme exactly as the software ships it. About seven minutes.
Predictions committed before the run.

## What we found

**The yes/no answer never changed.** Under all six settings that work, the same 24 of 256 setups hang
together and the other 232 split. None of the 15 named setups changed its verdict, including the majority
vote, which splits under every setting (an older version of the theory, IIT 3.0, says it doesn't).

**The size of Φ did change.** Under the settings that cut in one direction only, the "both must signal"
hiring hub drops from 2 to 1, and the "anyone can trigger it" and "everyone must agree" votes drop from
3 to 1.

| setup | default | one-way cuts | shipped "general" scheme |
|---|---:|---:|---:|
| any-one or all-three vote | 3 | 1 | 0 |
| both-must-signal hiring hub | 2 | 1 | 0 |
| either-but-not-both (parity) hub | 0.5 | 0.5 | 0 |
| majority vote, chat dyad, disjoint pairs | 0 | 0 | 0 |

**One setting is broken.** The "general" cutting scheme, as shipped in this PyPhi build, gives zero to
everything. It allows cuts of connections that do not exist, and cutting nothing costs nothing. The
software contains a filter meant to prevent that, but the line that would apply it can never run. With
the filter applied by hand, "general" agrees with the others.

## What it means

The lab's central claim, that some three-way arrangements cannot be reduced to pairs while dyads can,
does not depend on how the measuring tool is set up. The amount of Φ does. That supports the rule the lab
already follows: trust the verdict, and treat the number as a rough ranking at best.

## Limits

Small yes/no setups of three or four parties, one software build. Two other settings (alternative
distance measures) crash inside the software, so we could not test them.

## The code

- Study: [org_frontier/studies/iit4_settings_robustness/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/iit4_settings_robustness)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/iit4_settings_robustness/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/iit4_settings_robustness/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/iit4_settings_robustness/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
