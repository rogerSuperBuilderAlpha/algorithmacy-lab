# Round 11 — robustness and dynamics (Q6–Q11, probes 140–169)

Six agenda questions run end to end through the six-stage protocol. Three test how stochastic noise
acts on the dyadic/triadic verdict (Q6, Q7, Q8); three test how temporal structure acts on it (Q9, Q10,
Q11). The forms are the n=3 conjunctive mediated triad and its relatives, with the parity and pool hubs
and the ring as scaling references. Every run validated a known control before any comparison. Probes
140–169 carry the numbers; each question has its own paper and FINDINGS.

## The questions

- **Q6 — noise phase transition (140–144).** Mediator commit noise drives Φ_MIP down as a clean
  exponential. No interior kink, no susceptibility peak. The verdict holds triadic across the whole
  interior and flips only at the degenerate p=0.5 endpoint. H1 partial, H2 refuted, H3/H4/H5 confirmed.
- **Q7 — party vs mediator noise (145–149).** The seat that carries the flip-noise shapes Φ(p): party
  and mediator noise trace distinct curves, and the worker and counterpart are one symmetric seat. The
  asymmetry stays in the magnitude. Both sites flip the verdict only at p=0.5. H1/H2 confirmed, H3/H4
  refuted, H5 partial.
- **Q8 — parity vs conjunctive hub under noise (150–154).** The parity hub's small clean Φ (2^(2−n))
  leaves its verdict as robust as the conjunctive hub's. Both flip only at p=0.5, and the conjunctive hub
  sheds the larger Φ fraction. H4 partial, the rest refuted.
- **Q9 — timescale separation (155–159).** A deterministic hold-for-k mediator flips the verdict to
  dyadic at k=2 and sheds the parties into a self-absorbed {S} core. The probabilistic 1/k commit holds
  triadic across the whole grid. The construction decides the verdict. H1/H3/H5 confirmed, H2/H4 refuted.
- **Q10 — commit→response delay (160–164).** A fixed transport delay keeps the verdict triadic at every
  delay and never produces the {S} core. Φ is non-monotone, dipping at d=1 and recovering. A buffer
  pipeline and a lagged read disagree on the verdict at d=2. H3/H5 confirmed, H1/H2/H4 refuted.
- **Q11 — oscillatory scaling (165–169).** A rotating-update ring is a fifth Φ(n) law: constant Φ=2.0
  with a full core at every n, distinct from the AND-ring's capped Φ=4. The attractor period is a term
  in the law. Cycling alone is not a triadicity predicate. H1/H2/H3 confirmed, H4/H5 refuted.

## What holds across the six

**The verdict is robust to noise; the magnitude carries the structure.** Across Q6, Q7, and Q8 the
dyadic/triadic call flips only at the degenerate endpoint where the commit becomes a coin flip. The
parity hub flips there too, with clean Φ as low as 0.25. The robustness-until-the-endpoint pattern is a
property of the verdict, holding for the parity hub at clean Φ=0.25 as firmly as for the conjunctive hub.
Everything that distinguishes a noise site, a hub type, or a noise level lives in Φ(p), not in the verdict.

**Timescale flips the verdict where noise leaves it.** Q9 is the first axis in the round that moves the
verdict at an interior point: a mediator that updates half as often as its parties drops the triad to
dyadic at k=2. A pure transport delay (Q10) leaves it triadic. Slowing the clock and buffering the channel are
different operations, with different fingerprints — the slowed clock self-absorbs to {S}, the delay
keeps a party core.

**The modeling choice is load-bearing.** Q9 and Q10 both turn on which model of the timing is used.
Deterministic hold-for-k flips at k=2 while probabilistic 1/k holds triadic (Q9 H3). A buffer pipeline
stays triadic at d=2 while a lagged read factors to dyadic (Q10 H3). The construction is not cosmetic;
it sets the verdict. This sharpens the #112 catalogue of timing choices the verdict depends on.

**The scaling zoo gains a fifth law.** Q11 adds the rotating ring's constant Φ=2.0 to the four known
Φ(n) laws (constant chain/ring, conjunctive n−1, pool n(n−1), parity 2^(2−n)), and shows the attractor
period enters a coordination law as a term the fixed-point families have no room for.

## Limitations

Every result is in silico, on small Boolean forms read by the exact IIT-4.0 instrument. A passed
computational test is evidence about the model and about a second model that reproduces it, not yet about
a real organization. The probabilistic-commit results use the stochastic TPM flagged in #61. The Q11
period bookkeeping reported the measured attractor periods where they differed from the nominal
construction.
