# q143 — methods

## Form

`scaling_zoo.ring(n)` builds the conjunctive ring: node i updates to `x[(i-1)%n] & x[(i+1)%n]`.
The study runs n=3..7. Labels are `x0..x{n-1}`.

## Measurement

`verdict(rules, labels)` from `org_frontier.probes.lib` returns the whole-system classifier
output: `.structure` ('triadic' or 'dyadic'), `.max_phi` (exact Φ_MIP maximised over reachable
states), `.mip_state` (the maximising state), and `.mip_partition` (the human-readable MIP cut at
that state, e.g. `'2 parts: {x0x1,x2x3}'`). `major_complex(rules, labels)` returns the maximal
complex as `(core_label_tuple, phi)`, also maximised over reachable states. Core membership is read
from the returned tuple.

H1 splits into three clauses, each tested on the computed numbers: every n is triadic with
max_phi above 1e-6; every MIP names two parts (a two-arc cut); the max_phi values are equal across
n=3..7 to within 1e-6. H1 holds only if all three hold. H2 holds if the core tuple has length n at
every n.

## Controls

The instrument control runs the faithful worker-system-counterpart triad
`[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` and requires `structure == 'triadic'`
and `max_phi == 2.0`; the probe exits non-zero otherwise and prints `CONTROL ... PASS` on success.
Two topology anchors from `probe_topology_map` frame the ring: `chain(5)`, a serial form whose MIP
splits off an end pair and whose core is a sub-segment, and `pool(5)`, whose core is the full node
set. The anchors show that the read on core membership distinguishes a form that sheds nodes from
one that does not.

## Determinism

Φ over reachable states is exact and deterministic. The probe seeds `numpy.random.default_rng(0)`
to pin any RNG the exact-Φ backend draws. Two runs produce byte-identical stdout.

## Scope

Synthetic Boolean forms; exact IIT-4.0 Φ. The empirical-data arm of this line is separate; these
numbers are in-silico baselines.
