# q148 — Hypotheses

Question. Arrange hubs in a chain: hub 0 gates its own party group, hub k reads the upstream hub and
gates its own group, and each party reads its hub. As the chain grows, does the major complex span every
group, or does it fragment at a hub seam and leave the terminal groups out?

H1 (fixed before computing). A chain of hubs keeps the full core only up to a critical chain length,
beyond which the terminal groups drop out at the weakest hub seam, so hierarchy depth caps the integrable
group size.
Null: core size is independent of hub-chain length.

H2 (fixed before computing). The break falls at a hub seam, between adjacent hubs, rather than inside a
party group, which identifies hub-to-hub links as the integration bottleneck.
Null: the break isolates a single party, not a hub seam.

Decision rule. H1 is supported if the chain fails to span all groups at one or more tested depths, so the
integrable group span is capped below the chain length. H2 is confirmed if every break leaves whole upstream
groups intact and drops whole downstream groups, the signature of a seam rather than a within-group split.
