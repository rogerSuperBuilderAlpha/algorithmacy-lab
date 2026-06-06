# Q59 — Stage 2 deep research

## Question

Which directed edges in the min-norm partition cut matrices differ between recipient and non-recipient
outer singletons, and does back-channel cross-edge placement alone account for the invariant 4-versus-2
severed-connection split?

## IIT-4.0 cut matrices and directed connectivity

IIT 4.0 evaluates partitions by severing directed cause-effect connections between subsystems
(`albantakis2023iit4`). PyPhi represents each partition cut as a binary `_cut_matrix` aligned with the
connectivity matrix: entry (i,j) marks whether the directed edge from node i to node j is cut
(`mayner2018pyphi`). Normalization under `NUM_CONNECTIONS_CUT` sums these entries, so the count of ones
is the normalization denominator Q58 (#190) measured. The present study reads which directed edges
contribute those ones rather than only their total.

## Back-channel direction and outer-party asymmetry

The Q51–Q57 thread adds a single cross-edge between outer parties (worker: W reads C; counterpart: C reads
W). A back-channel edge is incident on both outer parties, so it preserves total connectivity-degree
symmetry; directional asymmetry is the only structural signal the cross-edge adds (lab reference gotcha).
Q57 (#185) showed the back-channel recipient determines which outer singleton co-enters the official MIP
tie set. Q58 (#190) showed the recipient cut severs twice as many connections without naming which edges
differ. The close-out tests whether the cross-edge alone explains the count asymmetry or whether
mediator-incident edges also contribute.

## Prior lab context

Q58 (#194) confirmed the normalized_phi ratio equals the inverse cut-ones ratio, implying the entire
2.0 split is normalization-driven given equal unnormalized phi (#192). If the cross-edge appears in both
cuts' severed sets, subtracting it cannot equalize counts; mediator edges in the symmetric difference
would then be the residual source of the 3-versus-1 edge gap within the 4-versus-2 total.

## Validation gap

Results apply to deterministic n=3 Boolean models at finest grain with synchronous update. Cut-matrix edge
labels follow PyPhi's indexing convention on the three-node connectivity matrix; independent analytic
verification of each severed directed edge against Albantakis et al. partition definitions remains open.
