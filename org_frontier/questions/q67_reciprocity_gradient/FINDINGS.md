# Q67 findings — the reciprocity gradient

Three hypotheses confirmed, one refuted. Instrument control passed (dyadic relay Φ=0.000, fully-coupled
triad Φ=0.830).

| H | Test | Result | Verdict |
|---|------|--------|---------|
| H1 | feed-forward relay (L0) | dyadic Φ=0 | confirmed |
| H2 | one reciprocal end-loop (L1) | whole-system dyadic Φ=0 (a local {A2,R} complex exists at Φ=2.0) | **refuted** |
| H3 | core jumps at closure | L2 core size 2, L3 core size 4 | confirmed |
| H4 | Φ monotone with reciprocity | L0=0 < L2=2.0 < L3=4.0 | confirmed |

All from `probe_reciprocity_gradient.py`.

## What it says

Reciprocity buys whole-system irreducibility, but not in small change. A feed-forward relay with no
feedback is dyadic (H1). A single reciprocal loop at the recipient end leaves the whole exchange dyadic
(H2 refuted): the form factors at the minimum-information partition even though a local two-element
complex {A2, R} of Φ = 2.0 has already formed inside it. Whole-system triadicity arrives only when the
chain is mutually coupled end to end (L2, the open chain, Φ_MIP = 2.0). Closing the loop then jumps the
core from the two-element end pair to the full four-element set (H3) and doubles Φ to 4.0. Across the
gradient Φ_MIP rises monotonically, 0 to 2.0 to 4.0 (H4).

The refuted hypothesis is the finding. A local irreducible core can exist inside a coordination whose
whole-system verdict is still dyadic. Partial reciprocity seeds the core without binding the exchange; the
binding is a threshold at full mutual coupling, and the core's growth to the whole is a sharp jump at loop
closure, not a gradual fill.

## Caveats

- **One refutation.** H2's prediction that a single end-loop makes the exchange triadic was wrong; the
  whole system stays dyadic while harbouring a local complex. The whole-system verdict and the
  maximal-complex reading diverge here, and both are reported.
- **In-silico.** Boolean models; Φ magnitude read ordinally.
- **n = 4.** The gradient is mapped at four elements; finer gradients need longer exchanges.
