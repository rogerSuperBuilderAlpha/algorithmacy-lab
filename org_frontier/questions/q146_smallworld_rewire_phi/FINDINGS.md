# Q146 findings — rewiring lowers Φ monotonically; no small-world peak

Both hypotheses fail. Rewiring a conjunctive ring toward random shortcuts lowers mean Φ at
every step, with the lattice (p=0) at the top and the random graph (p=1) at the bottom. There
is no interior small-world peak. The verdict does not hold triadic either: a dyadic verdict
appears at p=0.5 and dominates at p=1. The ring is the most integrated topology in this
family, and disorder only destroys integration.

| p | n_seeds | mean max-Φ_MIP | verdicts |
|---|---|---|---|
| 0.00 | 1 | 4.0000 | triadic |
| 0.10 | 3 | 3.0000 | triadic, triadic, triadic |
| 0.25 | 3 | 2.1383 | triadic, triadic, triadic |
| 0.50 | 3 | 0.6667 | dyadic, triadic, triadic |
| 1.00 | 3 | 0.4717 | triadic, dyadic, dyadic |

| H | Claim | Result | Verdict |
|---|---|---|---|
| H1 | non-monotone, interior small-world peak in Φ | mean Φ falls monotonically (4.0 -> 3.0 -> 2.14 -> 0.67 -> 0.47); peak at p=0.10 (3.0) is below the ring (4.0) | REFUTED |
| H2 | verdict stays triadic across the whole sweep | dyadic appears at p=0.50 (seed 0) and at p=1.00 (seeds 1, 2); 8 distinct cores | REFUTED |

From `probe_smallworld_rewire_phi.py`.

## What it says

The conjunctive ring is the most integrated topology in this family. At p=0 the ring carries
the maximum max-Phi_MIP of 4.0 with the whole six-node system as its core. Every rewiring step
lowers the mean: 3.0 at p=0.10, 2.14 at p=0.25, 0.67 at p=0.50, 0.47 at p=1.00. The
small-world hypothesis predicted an interior maximum where a few shortcuts add integration.
The data show the opposite: shortcuts subtract. The first rewiring already pulls some seeds
off the ring's full-system complex onto small two-node cores, and the mean never recovers.

The verdict tracks the same collapse. The ring and light rewiring stay triadic, but at p=0.50
one seed factors along a party-respecting cut and reads dyadic, and at p=1.00 two of three
seeds read dyadic. Random conjunctive wiring on six nodes often leaves a node constant or a
sub-block disconnected, and the system factors. Rewiring does not merely move the major
complex; past a point it dissolves it.

The core churns throughout, as H2's framing anticipated, but not while preserving the
verdict. Eight distinct cores appear across thirteen networks, ranging from the full
{N0..N5} at the lattice to scattered pairs like {N2,N4} and {N3,N5} at the random extreme.
Topology relocates and then destroys the integration, rather than holding a stable triadic
verdict while only the membership moves.

## Caveats

- Both hypotheses refuted. The result is a clean monotone decline, not a failure to find a
  weak peak: Phi at the first interior point (3.0) already sits below the ring (4.0).
- n=6 only, with a three-seed sweep and a five-point p grid. The monotone trend is clear at
  this resolution, but a finer grid or larger n could in principle expose structure between
  the sampled points. Untested here.
- Conjunctive (AND) coupling and in-degree-preserving endpoint rewiring are fixed design
  choices. Other couplings (parity, threshold) or degree schemes could behave differently and
  are not swept.
- The degenerate random networks (a node losing all variation, a disconnected sub-block)
  drive much of the p=1 collapse. That is a property of random conjunctive wiring at small n,
  not necessarily of disorder in general.
- In-silico. Synthetic Boolean networks, exact IIT-4.0 Phi. No empirical coordination is
  wired; the findings are on synthetic data and transfer to real systems only through a
  validation step not taken here.
