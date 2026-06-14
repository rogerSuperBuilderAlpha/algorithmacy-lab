# Q61 — MIP seam vs return-path typing · Stage 1 review

**Question.** On aligned one-sided back-channel forms held at uniform triadic max_phi=2.0, does the official
MIP singleton seam ({W,SC} vs {WS,C}) track return-path sequential/reciprocal typing even though max_phi
offers no subpanel discrimination?

**Agenda id.** Reconnect Q57 recipient→seam mapping to Q60 recipient→type mapping. Grows from Q60 probes
#204/#201 (uniform verdict, no Phi split) and Q57 #185 (recipient→singleton seam).

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #185 (Q57 H1) | Back-channel recipient determines tied singleton seam; worker→{W,SC}, counterpart→{WS,C}. | Supplies the official MIP singleton seam partition this question cross-tabulates against return-path type. |
| #200 (Q60 H1) | Return-path typing tracks recipient: worker→sequential, counterpart→reciprocal; 16/16. | Supplies the return-path sequential/reciprocal partition to compare with the seam partition. |
| #204 (Q60 H5) | Sequential and reciprocal subpanels identical at verdict; max_phi spread 0. | Establishes that max_phi cannot discriminate subpanels; asks whether the seam can. |
| #201 (Q60 H2) | All sixteen pairs triadic at max_phi=2.0. | Fixes the uniform triadic ceiling under which seam–type co-extensiveness is tested. |
| #135–#139 (Q43) | Return-path operationalization splits sequential vs reciprocal on connectivity, not verdict alone. | Defines return-path typing reused here. |
| #49 seam.py | Official singleton seam read from MIP tie set at max-Phi state. | Instrument for seam extraction. |

## The gap

Q57 (#185) showed recipient party fixes the official singleton seam; Q60 (#200) showed the same recipient
party fixes return-path sequential/reciprocal typing on the identical sixteen aligned one-sided ceiling pairs,
all triadic at max_phi=2.0 (#201, #204). No probe cross-tabulates seam against return-path type directly or
tests whether the two partitions are co-extensive, strictly finer, or strictly coarser. The open question is
whether the MIP singleton seam acts as a verdict-level discriminator that recovers the typing max_phi loses,
or whether seam and type merely share the recipient as a common cause without identical partition geometry.
