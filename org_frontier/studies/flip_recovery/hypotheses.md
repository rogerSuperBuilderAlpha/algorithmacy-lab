# Flip recovery: how fast a quorum hub settles after one party's bit is flipped, and whether that tracks Φ

Fixed before this study's computation.

## Gap

`ergodic_settling_time` found settling time does not separate triadic from dyadic forms on the frozen
42-form panel (transient AUC 0.540). It did not test recovery from a single-party perturbation, and it
did not use the quorum-hub timing families built today: `memory_rules` (36 deterministic cases, 13 with
whole Φ > 0) and `update_order_quorum` (72 cases, all whole Φ 0, top subset φ from 1.0 to 6.0). Both
families' Φ values are already committed; this study computes only dynamics and joins them.

## Measures (deterministic TPMs)

- **recovery time**: start in a state on an attractor, flip one party's bit, count steps until the
  trajectory is on an attractor again; mean over all attractor states × three parties.
- **same-attractor rate**: share of those flips after which the trajectory returns to the attractor it
  started on.
- **transient length**: steps from each of the 16 start states until first reaching an attractor; mean
  over starts (the `ergodic_settling_time` measure, on these TPMs).

## Outcomes

One-sided Mann–Whitney U, α = 0.05; Spearman with a two-sided p from `scipy.stats`.

- H1: in `memory_rules`, recovery time is shorter for whole Φ > 0 cases than whole Φ = 0 cases.
- H2: in `memory_rules`, the same-attractor rate is higher for whole Φ > 0 cases.
- H3: across all 108 cases, Spearman(recovery time, top subset φ) < 0 with p < 0.05.
- H4 (replicating the null): in `memory_rules`, transient length does not separate whole Φ > 0 from
  whole Φ = 0 cases (p ≥ 0.05).
