# q152 — Methods

## Forms

Topology builders are reused verbatim from studies 1-9; none are reimplemented here:

- `chain(n)`, `pool(n)` — `org_frontier.probes.probe_topology_map`
- `ring(n)` — `org_frontier.probes.probe_scaling_zoo`
- `single_hub(n)`, `two_hub(n)` — `org_frontier.probes.probe_distributed_mediators`
- `sym_multihub(n, m)` — `org_frontier.probes.probe_multihub_law`
- `hub_chain(L, g)` — `org_frontier.questions.q148_multihub_chain_hierarchy`

Each is instantiated at every n in {5, 6} for which it is defined. `sym_multihub` is swept
over m = 1..n-2 (at least one party). `hub_chain` is taken at the (L, g) pairs that land
exactly on n = 5, 6.

## Measurements (reused machinery)

For each `(rules, labels)`:

- `verdict(rules, labels)` -> `.structure` ('triadic' / 'dyadic'), `.max_phi`
  (`org_frontier.probes.lib`)
- `major_complex(rules, labels)` -> `(core label tuple, phi)`, the maximal complex over
  reachable states (`org_frontier.probes.lib`)
- `shapley(rules, labels)` -> `({party: value}, total_phi)`, the Shapley value of subsystem
  Φ at the all-on integrating state (`org_frontier.questions.q111_shapley_value.forms`)

## Decision rules

- A topology **disagrees** when the verdict is triadic and the core omits at least one node
  (`len(core) < n`).
- **H1** is SUPPORTED iff at least one topology disagrees.
- A node is a **zero-Shapley** party when `|value| <= 1e-6`.
- **H2** is CONFIRMED iff the biconditional `disagree <=> (zero-Shapley count > 0)` holds
  for every topology and H1 holds; otherwise NOT SUPPORTED. Two counterexample classes are
  reported explicitly: triadic exclusions carrying no zero-Shapley node, and zero-Shapley
  nodes sitting inside a full triadic core.

## Determinism

`numpy.random.default_rng(0)` seeds all RNG. `verdict`, `major_complex`, and `shapley` are
exact and deterministic over the reachable-state enumeration, so output is byte-identical
on re-run.

## Instrument control

The worker-system-counterpart / read-recipient triad
`[lambda x:x[1], lambda x:x[0]&x[2], lambda x:x[1]]` is checked to read verdict 'triadic'
at max_phi 2.0 with a full-party core and no zero-Shapley party before any new computation;
the probe prints `CONTROL ... PASS`.

## Scope

Exact IIT-4.0 Φ on synthetic Boolean forms. In-silico only; no field data.
