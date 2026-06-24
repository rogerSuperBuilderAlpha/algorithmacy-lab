# Methods — q160

## Machinery reused
- `org_frontier.recurrence.crqa.trajectory` — runs a Boolean form as a stochastic dynamical system
  (flip noise 0.08, 600 steps after a 20-step warmup).
- `org_frontier.recurrence.crqa.coupling_centrality` — each node's summed prominent lead-lag
  coupling, the behavioral centrality.
- `org_frontier.recurrence.bridge_four.major_complex` — the max-Φ maximal complex over reachable
  states, via `complex_over_states` (exact IIT-4.0 Φ).
- `org_frontier.recurrence.bridge_four.separates` — the full-separation predicate: True when every
  core member out-couples every non-member, None when the core is everyone or no one.
- `org_frontier.recurrence.bridge_four.rand_form5` — the random five-node form generator added for
  this study (the n=5 counterpart of `rand_form4`).

## Forms
- Named five-node forms from `org_frontier.multiparty.forms`: `deep_pool_all`, `deep_substitutable`.
- Three inline five-node peers placing the excluded party at different indices to rule out a
  positional artifact: `relay_chain5`, `central_hub5`, `pool_with_spectator5`.
- A `rand_form5` ensemble of 40 draws (form-draw seed 1; trajectory seeds 7000+k).

## Structural ground truth
The major complex of each form, the node set carrying the maximal Φ over reachable states. The core
is a strict, non-empty subset for the separation test to be a real question; forms whose core is
everyone or no one are marked n/a.

## Behavioral ranking
`coupling_centrality` from one sampled trajectory per form. A form fully separates when the lowest
core-member centrality exceeds the highest non-member centrality.

## Control
The four-node published full-separation rate, 36% (`org_frontier/recurrence/BRIDGE_FOUR.md`), is the
baseline H1 tests against. The instrument control validates the faithful triad: major complex {W,S,C}
at Φ=2.0 with the mediator S top-coupled.

## H2 read
On `deep_pool_all`, across 20 trajectory seeds, the worker's (node 0) coupling rank and how often it
out-couples the weakest core member.

## Determinism
Every trajectory uses `random.Random(seed)` with a fixed seed; the Φ library seeds its reachable-state
search internally; `numpy.random.default_rng(0)` is set once. Output is byte-identical across re-runs.

## Validation gap / scope
Exact IIT-4.0 Φ on small Boolean coordination forms. "worker", "spectator", "core", "relay", and
"coupling centrality" name graph-and-Φ quantities, not measured organizations. In-silico scope; the
Φ-to-organization bridge is open. The CRQA arm runs on synthetic trajectories, so every separation
fraction is a baseline on synthetic data.
