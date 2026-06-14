# Q59 — directed cut edges · Stage 1 review

**Question.** Which directed edges in the min-norm partition cut matrices differ between the recipient
and non-recipient outer singletons, and does back-channel cross-edge placement alone account for the
invariant 4-versus-2 severed-connection split?

**Agenda id.** Close-out of the Q51–Q58 back-channel / normalization thread. Grows from Q58 probes
#190/#194 (severed-connection counts and inverse cut-size law) and Q57 #185 (back-channel recipient
determines tied singleton).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #190 (Q58 H1) | Recipient min-norm cut severs 4 connections; non-recipient severs 2; ratio 2.0 on 16/16. | Counts severed connections; does not name which directed edges differ. |
| #194 (Q58 H5) | Normalized_phi ratio equals cut_ones ratio on 16/16. | Links ratio to cut size; edge-level decomposition untested. |
| #185 (Q57 H1) | Back-channel recipient determines tied singleton seam. | Names which cut is tied; does not enumerate severed directed edges. |
| #186 (Q57 H2) | Tied norm 0.5, excluded norm 1.0 on dual at-system-Phi outer cuts. | Supplies normalized_phi values the cut edges must explain. |
| #173 (Q54 H4) | One-sided Phi=2.0 requires commit-topology alignment. | Defines the sixteen aligned one-sided ceiling pairs. |
| #142–#143 (Q51) | Back-channel adds W↔C cross-edge; worker vs counterpart topologies differ in direction. | Supplies the cross-edge construction whose sole responsibility for the 4-vs-2 split is untested. |

## The gap

Q58 (#190) established that the recipient singleton min-norm partition severs exactly four cut-matrix
connections and the non-recipient severs two, with zero spread across sixteen aligned one-sided ceiling
pairs. No probe has enumerated which directed edges appear in each cut matrix, whether the back-channel
cross-edge is exclusive to one cut or shared, or whether subtracting the cross-edge from the severed count
would equalize the 4-versus-2 split. Q57 (#185) identified the recipient from back-channel direction but
left the edge-level geometry open. The panel and partition scan from Q56–Q58 are available; the directed
edge inventory and the cross-edge accounting test are not.
