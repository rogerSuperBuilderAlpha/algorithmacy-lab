# Q144 methods — building and reading mediator hierarchies

## Forms

A mediator tree is parameterized by depth d and breadth b. Level 0 is the apex (one node), level L holds
b**L nodes, and level d holds the leaves. Indices run level by level. Each internal node and the apex is
the AND of its b children. Every leaf reads the apex. The leaf-to-apex feedback closes the tree into a
recurrent dynamical system, which gives the exact instrument reachable states to evaluate.

Two axes are swept separately.

- **Depth axis (H1).** Breadth is fixed at one (b = 1) and depth runs d = 1, 2, 3, 4. With one child per
  node the tree is a single serial path of mediators from one leaf to the apex, so n = d + 1. This
  isolates depth at a fixed leaf count of one.
- **Breadth axis (H2).** Depth is fixed at one layer (d = 1) and breadth runs b = 2, 3, 4. The apex is the
  AND of its b leaves and each leaf reads the apex, so n = b + 1. This isolates breadth at a fixed depth
  of one.

Two scaling-zoo baselines anchor the verdicts. The serial chain is a pure copy ring of length L
(i' = x[i-1]), the zoo's constant-Φ law (predicted Φ = 2). The coupled pool has every node copy the parity
of the other n-1 nodes, so every node both reads and influences every other, the zoo's super-linear law
(predicted Φ = n(n-1)).

The whole grid stays at n ≤ 5 so the exact instrument is fast and the run reproduces exactly.

## Instrument

Φ is the exact IIT-4.0 major complex via `org_frontier.probes.lib.major_complex(rules, labels)`, which
returns the (core, Φ) of the maximal complex taken over reachable states. The whole-system verdict and the
control use `org_frontier.probes.lib.verdict`. The base triad's Shapley split of integration uses
`org_frontier.questions.q111_shapley_value.forms.shapley`. No Φ machinery is reimplemented.

## Control

The probe validates the instrument on the faithful triad `[x[1], x[0]&x[2], x[1]]` with labels (W, S, C),
which must read structure `triadic` at max Φ 2.0 before any tree is computed. The run aborts if the control
fails.

## Determinism

All RNG is seeded with `numpy.random.default_rng(0)`. The forms are deterministic Boolean rules and the
reachable-state scan is exhaustive, so the output is byte-identical on re-run.

## Verdict rules

- **H1** is supported when Φ across d = 1..4 is flat (range under 1e-6) and equal to the chain constant
  2.0 at every depth.
- **H2** is supported when Φ across b = 2, 3, 4 is strictly increasing. Super-linearity is the stronger
  reading and is claimed only when the second difference over b is positive; a strictly increasing but
  linear trend is reported as supported-but-linear.
