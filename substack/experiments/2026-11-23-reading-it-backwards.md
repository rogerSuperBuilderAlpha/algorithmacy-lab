# Reading the hub backwards changes nothing real, but it still moves 80 verdicts in the software

*If one person in a group reads the coordinator's signal backwards, the group's structure is the same; only
the labels changed. We checked that across 2,048 three-person setups. The structure held. The software's
answers did not always hold.*

## The question

This lab asks whether a coordination setup hangs together as a whole or splits into parts. It answers
with integrated information, Φ, from IIT 4.0, computed exactly with the PyPhi software. Φ above zero means
no cut separates the parts without losing something. It measures structure, not life or awareness.

The setup here: three people and a coordinator. Each round, each person looks at the coordinator's last
signal, and the coordinator makes its next call from what the three people did. Earlier today we ran
all 256 ways the coordinator could make its call, with everyone taking the signal at face value
([Each could swing it](2026-11-23-each-could-swing-it.md)).

Now suppose one person reads the signal backwards: when the coordinator says "yes", they hear "no". That
is the same arrangement with that person's "yes" and "no" swapped. Nothing about who depends on whom has
changed, so Φ should not change either. We wanted to know whether the software agrees.

## What we ran

Every combination of who reads the signal backwards (8 patterns) with every coordinator rule (256), so
2,048 setups. For each one we computed Φ the default way, and also under every way of settling the tied
states the software picks between (it settles them "arbitrarily (for now)", in its own words). We wrote our
four predictions down and pushed them before running anything.

## What we found

- **Under the default setting, 80 of the 1,792 setups with a backwards reader get a different verdict from
  their relabelled twin.** In each case one side scores 0 and the other 0.471679 or 0.25. For example, with
  the second person reading backwards and rule 38, the default Φ is 0. The relabelled twin (rule 137, everyone
  reading normally) scores 0.471679.
- **The count of setups that hang together moves with the labels.** It is 50 of 256 for some patterns of
  backwards readers and 46 of 256 for others, though the structures are the same.
- **All 80 come from the tie-break.** Every one has a twin among the 24 rules where the earlier study
  found the tie choice mattered. When we score every tied choice, all 2,048 setups match their twins
  exactly.
- **The earlier rule still works.** Counting a setup as hanging together if any tied choice gives Φ above
  zero, the rule "every person can swing the call when all agree" gets all 2,048 right.

All four predictions held.

## What it means

Reading a signal backwards is just relabelling, and IIT treats it that way. PyPhi's default output doesn't
quite, because its tie-break depends on the order in which states happen to be listed. For three-person
groups this can shift a count by 4 out of 256. The fix is to report the range over tied choices, not one
arbitrary pick. With two people this never came up: our [coin-flip check](2026-11-23-the-coin-flip-check.md)
found no tie that mattered in any of the 4,096 three-node setups.

## Source

- Study: [org_frontier/studies/mixed_reads/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/mixed_reads)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/mixed_reads/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/mixed_reads/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/mixed_reads/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
