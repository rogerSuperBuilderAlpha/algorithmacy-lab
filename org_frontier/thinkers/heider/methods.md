# Heider — Stage 4 methods

## Shared infrastructure

- Whole-system verdict Φ_MIP: `org_frontier.probes.lib.verdict`; major complex: `major_complex` (max over
  reachable states). Attractors from the deterministic TPM directly.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

Conjunctive triad A'=M, M'=A∧B, B'=M: Φ = 2.000000, core {A, M, B}. No comparison is read until it passes.

## Forms

**Signed triad** `triad(signs)`, nodes (p, o, q), `signs = (σ_po, σ_pq, σ_oq)` with σ ∈ {+1, −1}:

    s_i' = maj(σ_ij·s_j, σ_ik·s_k, s_i),   where σ·s = s if σ = +1 else 1 − s.

Named patterns: `ppp` (+,+,+), `ppm` (+,+,−), `pmm` (+,−,−), `mmm` (−,−,−). H1 runs all eight sign
vectors; the other probes use the four named representatives.

**Coevolving form** `coevolving()`, six nodes (p, o, q, Lpo, Lpq, Loq): attitudes as above with σ_ij read
from the L node (1 = +, 0 = −); `L_ij' = [s_i = s_j]`.

**Signed K4** `k4(signs)`, four nodes, six signs in the order (01, 02, 03, 12, 13, 23):

    s_i' = maj over the three signed inputs and s_i (four inputs; a 2–2 tie holds s_i).

Switching classes: for each of the 64 sign vectors, the canonical representative is the vector with the
fewest negative signs reachable by complementing any subset of nodes (complementing node v negates every
sign at v), ties broken by placing negatives last.
Degree of balance b(G) = positive cycles / 7 (four triangles, three 4-cycles).

**Dynamics.** From the state-by-node TPM, iterate every state to its attractor; classify attractors as fixed
points or cycles; a fixed point is a **rest state** iff every relation is satisfied there.

## Decision rules

- **H1** CONFIRMED iff (a) the eight patterns partition into exactly two classes by (Φ_MIP, core, attractor
  multiset) and the classes are {product +} and {product −}, and (b) Φ_MIP(balanced) > Φ_MIP(unbalanced).
  PARTIAL iff (a) holds and (b) fails. REFUTED iff (a) fails.
- **H2** CONFIRMED iff balanced patterns have rest states and all their attractors are rest states, and
  unbalanced patterns have no rest state. PARTIAL iff rest states sort as predicted but a balanced pattern
  has a non-rest attractor. REFUTED iff an unbalanced pattern has a rest state. Report whether unbalanced
  attractors are cycles or fixed points.
- **H3** CONFIRMED iff `mmm` and `ppm` differ in Φ_MIP, core size, or attractor count. REFUTED iff identical
  on all three.
- **H4** CONFIRMED iff the major complex of the coevolving form contains at least one attitude node and at
  least one L node. REFUTED otherwise; report which side the core falls on.
- **H5** CONFIRMED iff, over the switching-class representatives ordered by b(G), Φ_MIP is non-decreasing and
  the b = 1 class is at the maximum. PARTIAL iff monotone but not maximal at b = 1, or maximal at b = 1 but
  not monotone. REFUTED otherwise.

## Reporting

Each probe prints the control line, one line per form, and one verdict line `H<k> (...): CONFIRMED | PARTIAL
| REFUTED`. Results in `results/<probe>.json`. Whole-system Φ_MIP is the headline; the core and the attractor
structure are reported beside it.
