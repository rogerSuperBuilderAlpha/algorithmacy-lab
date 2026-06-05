# Q62 — Stage 2 deep research

## Question

On aligned one-sided back-channel forms at uniform max_phi=2.0, does the excluded (non-tied) outer singleton
cut with normalized_phi=1.0 carry independent return-path signal once tied-seam and type are known to be
co-extensive?

## Excluded outer cut and normalization geometry

IIT 4.0 evaluates partitions at the max-Phi reachable state and breaks MIP ties by minimum normalized phi
(`albantakis2023iit4`; `mayner2018pyphi`). Q57 (#186, #187) showed both outer-party singleton cuts reach
system Phi on sixteen aligned one-sided back-channel pairs; the tied (recipient) cut carries normalized_phi
0.5 and the excluded (non-recipient) cut carries 1.0. Q58 (#190–#194) traced the two-to-one ratio to
`NUM_CONNECTIONS_CUT` on the min-norm representative. The excluded cut is therefore a well-defined geometric
object in the partition scan, distinct from the official tied seam Q61 cross-tabulated against return-path
type.

## Co-extensive seam and type as prior constraint

Q61 (#206, #208) established perfect co-extensiveness between official tied singleton seam and Q43
return-path sequential/reciprocal typing on the same panel: W seam iff sequential, C seam iff reciprocal.
Recipient party remains the common cause (`thompson1967organizations`; Q60 #200). The open test is whether
the excluded singleton — the non-recipient outer cut at norm 1.0 — adds a third partition dimension or
merely encodes the complement of the tied seam once type is known.

## Complement partitions and redundant encodings

Malone and Crowston (1994) treat coordination dependencies as relational structure among activities. When two
labels partition a finite panel identically, a third label that is a deterministic function of either adds no
information (`tononi2004information` on integration as irreducibility, not mere correlation). The excluded
singleton is predicted to be the non-recipient complement of the tied seam if recipient direction alone
governs both cuts (`oizumi2014phenomenology` on mechanism over phenomenology). An independent third label would
require excluded to partition the panel differently from both tied seam and return-path type.

## Pre-registration and validation gap

Hypotheses and decision rules are committed before probe code (`brodeur2024preregistration`;
`chamberlin1890multiple`). Results apply to deterministic n=3 Boolean models at finest grain with synchronous
update. Excluded extraction follows Q57; typing follows Q43/Q60; tied seam follows Q49/Q61. Real
organizations remain beyond reach.
