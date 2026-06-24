# q149 — methods

## Machinery

The probe reuses existing code and does not reimplement Φ.

- `shapley(rules, labels)` from `q111_shapley_value.forms` returns `({party: value}, total_phi)`. The
  coalition value v(S) is the IIT-4.0 Φ of the subsystem on S at the all-ones integrating state,
  computed with `pyphi.new_big_phi.sia`. The Shapley value is the exact average marginal contribution
  over all orderings (no sampling).
- `verdict(rules, labels)` from `org_frontier.probes.lib` supplies the whole-system classifier reading
  used in the instrument control.
- Topology forms are imported from the probes that define them: `single_hub`, `two_hub`
  (`probe_distributed_mediators`), `sym_multihub` (`probe_multihub_law`), `ring` (`probe_scaling_zoo`),
  and `pool` (`probe_topology_map`).

## Instrument control

Two known cases run before any new computation.

1. The faithful worker-system-counterpart triad `[x[1], x[0]&x[2], x[1]]` reads `triadic` at
   `max_phi` 2.0.
2. The read-recipient triad splits its Φ so the mediator M captures about two-thirds of the total
   (M share within 1e-3 of 2/3) and the two outer parties take equal value. The run prints
   `CONTROL ... PASS`.

## Procedure

For each n in {5, 6}:

- Hub topologies. Build `single_hub`, `two_hub`, and `sym_multihub(n, m)` for m = 1 .. n-2. The hub
  set is node 0 for the single hub, nodes 0 and 1 for the two-hub, and nodes 0 .. m-1 for the m-hub.
  Compute the Shapley split, then report the hub sum, the party sum, the hub fraction of the total,
  and the per-hub share.
- Symmetric topologies. Build `ring` and `pool`. Compute the spread (max minus min) of the per-node
  Shapley values and flag whether it is at or below tolerance.

Determinism. The Shapley computation is exact. The RNG is seeded with `numpy.random.default_rng(0)`
so any incidental randomness reproduces. Two runs produce byte-identical output.

## Verdicts

- H1 is supported only if, at both n, the per-hub share ordered by hub count is non-increasing and
  strictly lower at the most-distributed end than at the single hub.
- H2 is supported only if every ring and pool spread is at or below tolerance.

## Scope

In-silico, synthetic Boolean forms. No empirical data.
