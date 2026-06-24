# Q146 methods — small-world rewiring sweep

## System

A conjunctive ring on n=6 nodes. Each node's next state is the AND of its two ring
neighbours' current states: node i reads i-1 and i+1 (mod 6). Each node keeps in-degree 2
throughout.

## Rewiring

Watts-Strogatz endpoint rewiring. For each of a node's two input edges, with probability p
the source is replaced by a uniformly random source drawn from the nodes that are neither
the node itself nor already one of its inputs. In-degree 2 is preserved, no self-loops, no
duplicate inputs. At p=0 the ring is untouched (the lattice control); at p=1 nearly every
endpoint is redrawn (the random-wiring control).

## Sweep

p in {0, 0.1, 0.25, 0.5, 1}. p=0 is deterministic and evaluated once. Interior p and p=1
are averaged over a fixed seed sweep (seeds 0, 1, 2), each seed offset from a fixed base so
the streams are independent and reproducible. All randomness uses numpy `default_rng`; the
run reproduces byte-for-byte.

## Readout

Per network, the reusable machinery returns:

- `verdict(rules, labels)` — the whole-system structure ('triadic'/'dyadic') and the max
  Φ_MIP over reachable states. This is the verdict the program reads.
- `major_complex(rules, labels)` — the maximal complex's core membership and its Φ.

## Decision rules

- H1 SUPPORTED iff mean max-Φ_MIP at some interior p strictly exceeds both the p=0 ring
  value and the p=1 mean (a strict interior peak). Otherwise REFUTED (monotone or boundary
  optimum).
- H2 SUPPORTED iff every evaluated network reads triadic. REFUTED if any p flips the
  verdict to dyadic.

## Instrument control

Before the sweep, the faithful triad `[x1, x0&x2, x1]` with labels (W,S,C) is classified;
it must read triadic with max Φ_MIP = 2.0 ('CONTROL ... PASS'). This validates the verdict
machinery on a known case.

## Scope and limits

In-silico. Synthetic Boolean networks, exact Φ, single n (6) and a coarse p grid with a
three-seed sweep. The AND coupling, the in-degree-preserving rewiring rule, and the small
seed count are design choices; other couplings, degree schemes, and larger n are untested.
No empirical data; results below are on synthetic networks only.
