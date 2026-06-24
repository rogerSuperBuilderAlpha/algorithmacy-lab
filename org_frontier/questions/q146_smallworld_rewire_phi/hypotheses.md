# Q146 hypotheses — small-world rewiring and Φ

Fixed before computing.

## H1 — non-monotone small-world peak in Φ

Φ is non-monotone in the rewiring probability p, with a small-world peak at intermediate
p. A few random shortcuts add integration before randomness destroys the balanced
bottleneck, so the mean max-Φ_MIP at some interior p strictly exceeds both the pure ring
(p=0) and the random graph (p=1).

Null: Φ is monotone in p, with no interior peak.

Decision rule: SUPPORTED iff the mean max-Φ_MIP at some interior p (0 < p < 1) strictly
exceeds both the p=0 value and the p=1 mean; otherwise REFUTED.

## H2 — verdict holds triadic across the sweep

The verdict stays triadic across the whole rewiring sweep at fixed n=6 even as the major
complex (core membership) churns. Topology shifts which nodes carry the integration without
flipping the dyadic/triadic verdict.

Null: rewiring flips the verdict to dyadic at some p.

Decision rule: SUPPORTED iff every evaluated network reads triadic; REFUTED if any p
produces a dyadic verdict.

## Scope

In-silico. The subjects are synthetic conjunctive Boolean networks on n=6 nodes, not
measured systems. The verdict and Φ are exact (IIT-4.0 over reachable states). No empirical
coordination is wired here; the gap to real organisational data is open.
