# q178 — The Bit Cut on a Graded Action Is Verdict-Bearing

A coded account of a coordination records each party's action and turns it into a Boolean rule.
Many actions are not Boolean to begin with. A coder watches a worker partly comply, or a system
half-bind a counterpart, and records a grade: none, partial, full. Before the rule set is built,
that grade is collapsed to one bit. The cut point of the collapse is a coding choice, and this
study asks whether the choice reaches the Φ verdict.

## Setup

A synthetic account fixes a graded counterpart-action level `g` in `{0, 1, 2}` over labels
`(W, S, C)`. A coder reads it with a threshold `t` and collapses the grade to `b = 1[g >= t]`. The
bit drives the system rule: `b = 1` gives the worker-system-counterpart triad `[x1, x0 & x2, x1]`,
`b = 0` gives the dyad `[x1, x0, x1]`. The q173 bridge `rule_to_phi` reads each collapsed rule set
to its exact IIT-4.0 Φ verdict. Φ is not reimplemented.

The grade-by-threshold map sets which accounts move. A grade of 0 reads dyadic at every cut; a
grade of 2 reads triadic at every cut; a grade of 1 reads triadic under the low cut and dyadic
under the high cut. The boundary grade is the one that flips.

## Result

On a balanced 200-account panel, the threshold flips the verdict for 66 accounts, a flip rate of
0.33. The bit cut is verdict-bearing for a third of accounts, not bookkeeping.

The disagreement carries into the confidence interval. One boundary account read by eight coders
split across the two cuts gives a Φ interval of [-0.14, 2.11], width 2.25, spanning the whole
dyadic-to-triadic range. The same eight coders all using one cut give [1.96, 2.00], width 0.05.
The split panel is wider by a factor of 47.6, and its negative Krippendorff alpha marks the cut as
the source. Same-cut coders agree; split-cut coders carry the verdict's full uncertainty.

## What this shows and does not show

The bit cut is a calibration step with verdict consequences, and a coding protocol that leaves it
unfixed leaves the verdict unfixed. Reporting a Φ verdict for a graded action without reporting the
cut hides a coder degree of freedom that can swing the structural reading.

The accounts are synthetic coded grades and rule sets. No worker action is measured, and the map
from a coded grade to an observed action is not validated. The result is about how the coding
machinery behaves, and it says where a real coding protocol must pin down the cut and report
inter-coder agreement on it before a Φ verdict can be trusted.
