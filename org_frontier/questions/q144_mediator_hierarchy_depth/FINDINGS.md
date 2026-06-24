# Q144 findings — depth holds Φ at the chain constant; breadth grows it linearly

Depth and breadth are separable axes with different scaling. Adding mediator layers between a leaf and the
apex leaves Φ pinned at the chain constant 2.0. Adding leaves per node raises Φ. The growth along breadth
is linear in leaf count, not the super-linear n(n-1) of a fully-coupled pool, so the mediator tree sits
between the two zoo laws: flat in depth like a chain, growing in breadth but short of a pool.

## Grid (exact IIT-4.0 major-complex Φ)

| axis | parameter | n | core | Φ |
|---|---|---|---|---|
| depth | d=1, b=1 | 2 | (A,B) | 2.000 |
| depth | d=2, b=1 | 3 | (A,B,C) | 2.000 |
| depth | d=3, b=1 | 4 | (A,B,C,D) | 2.000 |
| depth | d=4, b=1 | 5 | (A,B,C,D,E) | 2.000 |
| breadth | d=1, b=2 | 3 | (A,B,C) | 2.000 |
| breadth | d=1, b=3 | 4 | (A,B,C,D) | 3.000 |
| breadth | d=1, b=4 | 5 | (A,B,C,D,E) | 4.000 |

Baselines: serial chain Φ = 2.000 at n = 3, 4, 5 (constant). Coupled parity pool Φ = 1.500, 4.000, 2.500
at n = 3, 4, 5 (non-monotone; the parity coupling does not cleanly trace the n(n-1) law it is meant to
illustrate).

## Verdicts

| H | claim | result | verdict |
|---|---|---|---|
| H1 | depth at fixed leaf count holds Φ flat at chain constant 2.0 | Φ = 2.0 at d = 1..4, range 0 | SUPPORTED |
| H2 | breadth at fixed depth grows Φ super-linearly toward the pool law | Φ = 2, 3, 4 across b; strictly increasing, second difference 0 | SUPPORTED (linear, not super-linear) |

## What it says

Depth is a serial bottleneck. Each mediator layer copies a single bit upward, so stacking layers cannot
add irreducible structure: Φ stays at 2.0 from d = 1 to d = 4, exactly matching the serial-chain baseline.
A deeper hierarchy of two-input AND-gates is no more integrated than a shallow one when each node has a
single child.

Breadth adds integration. Widening the apex from two to four leaves raises Φ from 2.0 to 4.0, one unit per
added leaf. The growth is real and monotone, which separates breadth cleanly from depth. It is linear in
leaf count, not the convex n(n-1) growth of a fully-coupled pool. The mediator tree shares its leaves into
a single conjunctive apex rather than coupling every party to every other, and that single shared mediator
caps the growth at the linear rate. The strong form of H2 (super-linear toward the pool) is refuted; the
separability claim that breadth and depth scale differently holds.

The parity pool baseline did not behave as a clean n(n-1) exemplar at this size: its Φ is non-monotone
(1.5, 4.0, 2.5). The intended contrast is the published pool law; the parity construction used here is an
imperfect stand-in for it and is reported as measured.

## Caveats

- **In-silico.** Boolean dynamical models, exact major complex. No party is measured. The trees are
  synthetic constructions chosen to isolate depth and breadth, not models of a fielded organization.
- **Small grid.** n <= 5 throughout, so the breadth trend rests on three points (b = 2, 3, 4). Linearity is
  the reading over that range; behaviour at larger breadth is untested at the exact instrument.
- **Pool baseline imperfect.** The parity-coupling pool is non-monotone here and does not reproduce the
  n(n-1) law cleanly, so the "toward the pool" comparison is qualitative.
- **One closure.** Leaves read the apex. A different feedback closure could change the reachable-state set
  and the magnitudes; the depth-flat, breadth-growing split is shown for this closure only.
