# q186 — Three spread components vary independently across an account-pair census

When two parties give divergent accounts of one coordination, the q183 bridge scores the
divergence as a tuple: do the accounts agree on the structural verdict, how far apart are their
whole-system max Phi values, and how much do their major-complex cores overlap. A natural worry is
that the tuple is redundant. If accounts that diverge more do so on every axis at once, then one
scalar would carry the same information and the three numbers would be decoration.

The worry is testable. Across a synthetic census of account pairs at n=3 and n=4, the three
components were computed for every pair and their rank correlations measured. If the spread were
rank-one, the three divergence axes (verdict disagreement, Phi gap, core divergence) would be
monotone in one another and every pairwise Spearman correlation would equal +1. The off-diagonal
cells of the joint pattern, where two components point in opposite directions, would be empty.

## Census

The census draws on two curated palettes of Boolean accounts. The n=3 palette spans faithful and
OR/XOR triads, a chain, all-AND and all-OR triads, a dyad, and a self-loop, covering max Phi from 0
to 6 and cores from one node to three. The n=4 palette adds coupled quads, a whole-system-dyadic
account whose major complex is a three-node subset, a two-node dyad, an account that reads triadic
yet integrates only the AB pair, and two independent dyads. Every unordered pair within a node
count enters the census: 43 pairs in total. Each account's verdict and core were computed once
through the reused classifier and probe library; the per-pair components were read from the q183
bridge definition.

## Result

The three axes are not collinear. The Spearman correlations are +0.23 (verdict disagreement vs Phi
gap), +0.51 (verdict disagreement vs core divergence), and -0.09 (Phi gap vs core divergence). None
reaches +1, and one runs slightly negative. Both off-diagonal cells are populated. Fourteen pairs
agree on verdict yet carry a positive Phi gap; the faithful triad and the XOR triad both read
triadic with the same core and still differ by 1.5 in max Phi. One pair disagrees on verdict yet
shares an identical core; a two-node dyad and a triadic-reading account both seat exactly the AB
pair in the major complex. Across the census, 34.88 percent of pairs show at least one off-diagonal
pattern, far above the sub-1-percent floor that numerical Phi noise would produce.

H1 holds: the three components are not rank-one collinear. H2 holds: the off-diagonal fraction
exceeds 10 percent by a wide margin. The spread tuple is not redundant. Verdict agreement, Phi gap,
and core divergence each measure something the other two miss. A coordination can change which
parties are bound into the integrated core without moving the structural verdict, and it can move
the verdict without moving the core.

## Scope

The accounts are coder-supplied rule sets, not measured worker states. No worker is measured. The
result characterizes the spread construct on a synthetic census and is in-silico. Whether real
party accounts populate the same off-diagonal cells is not shown here; the instrument is validated
on controls and the empirical reach is the next step.
