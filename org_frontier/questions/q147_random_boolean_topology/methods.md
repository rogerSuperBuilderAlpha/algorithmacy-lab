# q147 methods

## Ensemble

160 random Boolean networks: 120 at n=4 and 40 at n=5. Each node draws a random arity k in
1..kmax (kmax = 4) and a random truth table over k randomly chosen inputs. The dependency graph
is read back from the rule set with `cm_from_rules`, a flip-test: an input that the truth table
ignores adds no edge, so the graph reflects the realized dependencies. Sampling uses a single
`numpy.random.default_rng(0)`; the run reproduces byte-identically.

## Graph statistics (from the directed connectivity matrix cm)

- mean degree: mean over nodes of in-degree plus out-degree.
- clustering: average clustering coefficient on the symmetrized graph (fraction of each node's
  neighbour pairs that are connected).
- diameter: longest shortest path on the symmetrized graph by Floyd-Warshall; a disconnected
  graph returns the sentinel n.
- cycle density: per-node count of directed closed walks of length 1, 2, and 3, from the traces
  of the first three powers of cm. This is the recurrence proxy.
- core in-degree: mean in-degree of the maximal-complex nodes.

## Φ and the verdict

`verdict(rules, labels)` returns the triadic/dyadic call and max Φ over the MIP across reachable
states. `major_complex(rules, labels)` returns the maximal complex's node set and its Φ. Both
wrap the repo's exact IIT-4.0 oracle; Φ is exact at n<=5.

## Tests

H1: point-biserial correlation (Pearson with a 0/1 verdict) of each graph statistic against the
triadic indicator, ranked by absolute correlation. p-values use a Fisher-z normal approximation
so the report is deterministic.

H2: Pearson correlation of core mean in-degree against the maximal complex's Φ over the triadic
subset.

## Control

The faithful triad `[x[1], x[0]&x[2], x[1]]` must read triadic with max Φ 2.0. The graph
statistics are checked on two hand-computed structures: a directed 3-ring (mean degree 2,
clustering 1, diameter 1, cycle density 1) and a 4-node hub (cycle density 0, diameter 2,
clustering 0). The probe asserts all of these before sampling.

## Scope

Synthetic Boolean networks; exact Φ at n<=5. No field data. The correlations describe this
in-silico ensemble. The Φ-to-organizational-value bridge is open (see q122).
