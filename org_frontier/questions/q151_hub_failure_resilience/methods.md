# q151 — Methods

Forms. Three n = 6 topologies, each with a designated spanning hub at node 0.

- single_hub: hub = AND of all five parties; every party reads the hub. No cycle runs through the non-hub
  nodes.
- two_hub_backup: two independent spanning hubs (nodes 0 and 1), each = AND of all four parties; every party
  reads (hub0 OR hub1). Hub 1 is a backup that does not depend on hub 0. No cycle runs through the non-hub
  nodes.
- ring_hub: the five non-hub nodes form a directed copy-ring, each reading its predecessor; the hub reads
  two opposite ring nodes, so it observes the whole ring while the ring does not read it back. One
  independent cycle runs through the non-hub ring.

Ablation. Node 0 is replaced by the constant 0: the hub fires for nothing. In single_hub the parties then
read a dead hub. In two_hub_backup the surviving hub still gates the parties through the OR. In ring_hub the
ring does not read the hub, so the copy-ring is untouched.

Measurements. For each topology, before and after ablation:

- major_complex(rules, labels) -> (core, Φ): the maximal complex and its Φ over reachable states. The
  structural verdict is triadic iff this Φ exceeds 1e-6, matching the classifier (a form is triadic iff it is
  irreducible at its best reachable state). A form with no irreducible complex reports Φ = 0 and reads
  dyadic.
- non-hub cycle count: the cyclomatic number (E - V + C) of the undirected subgraph induced by the non-hub
  nodes of the connectivity matrix, read from cm_from_rules. This is single_hub 0, two_hub_backup 0,
  ring_hub 1.
- retained Φ: the major-complex Φ after ablation.

Control. The unablated form of each topology must read triadic, or the resilience contrast is undefined. The
probe checks this and prints the result.

Reuse. verdict and major_complex from org_frontier.probes.lib; cm_from_rules from the classifier; the same
exact IIT-4.0 Φ oracle used across the program. No reimplementation of Φ.

Determinism. numpy seeded with 0; the Φ library seeds its state search with numpy.random.default_rng(0). The
probe opens with an instrument control on the faithful triad, which must read triadic at max Φ 2.0 with a
spanning core. Re-runs are byte-identical.

Scope. Synthetic Boolean coordination forms under exact Φ. "Hub", "backup", "ring", "ablation", and
"resilience" name graph-and-Φ quantities, not measured field constructs. The Φ-to-organization bridge is
open, so the empirical reading is a baseline on synthetic data.
