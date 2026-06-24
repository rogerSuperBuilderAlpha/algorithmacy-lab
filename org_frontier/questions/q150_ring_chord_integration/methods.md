# q150 — methods

## Forms

Both forms have six nodes labeled A through F at ring indices 0 through 5.

Unchorded ring: `ring(6)` from `probe_scaling_zoo`. Each node is the AND of its two ring neighbors.

Chorded ring: the same ring with one chord across the opposite pair (A, D). Every node keeps its
two ring-neighbor inputs; the two chord endpoints add their partner. A reads {F, B, D} and D reads
{C, E, A}. The other four nodes are unchanged.

## Machinery (reused)

- `verdict(rules, labels)` from `org_frontier.probes.lib` returns the whole-system classifier
  verdict: `structure`, `max_phi` (max Φ_MIP over reachable states), `mip_state`, and
  `mip_partition` (the minimum-information cut at the max-Φ state).
- `major_complex(rules, labels)` from the same module returns the irreducible core and its Φ, taken
  as the maximum over reachable states.
- `shapley(rules, labels)` from `q111_shapley_value.forms` returns the per-node Shapley value of
  subsystem Φ at the all-ones integrating state, where the value of a coalition S is the Φ of the
  subsystem on S.

## Reads

H1 compares `max_phi` and the `mip_partition` of the two forms. The cut string renders as one brace
pair holding the parts, e.g. `{BC,ADEF}`; the parser splits the inside on commas to recover the
parts and tests whether A and D fall in the same part. "Cut moved off the chord" means A and D share
a part in the chorded ring but not in the unchorded ring. H1 holds only if Φ rises and the cut
shifts off the chord.

H2 sums the Shapley values over the chord endpoints (A, D) and over the far arc (B, C, E, F) for
each form. Support requires the endpoint sum to rise and the far-arc sum to fall.

## Control

The instrument control runs the faithful worker-system-counterpart triad
`[lambda x:x[1], lambda x:x[0]&x[2], lambda x:x[1]]` and checks it reads `triadic` at max Φ_MIP
2.0 before any new computation.

## Determinism

The RNG is seeded with `numpy.random.default_rng(0)`. The verdict, major-complex, and Shapley
computations are exact enumerations over reachable states, so output is byte-identical on re-run.

## Run

```
source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
python -m org_frontier.questions.q150_ring_chord_integration.probe_ring_chord_integration
```
