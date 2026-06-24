# q148 — Methods

Form. A length-L hub chain at fixed group size g = 1. Node layout per hub k: one hub node H{k} followed by
its g party nodes p{k}_{j}. Rules:

- hub_0 = AND(its group),
- hub_k = hub_{k-1} AND its group, for k >= 1,
- each party reads its own hub.

This is the directed generalization of the mutually-coupled two-hub: the two-hub couples H0 and H1 both ways,
while the chain feeds H0 -> H1 -> ... -> H{L-1} one way. Total size n = L(1+g). For g = 1 the tested chains are
L = 2, 3, 4 at n = 4, 6, 8.

Measurements. For each chain:

- major_complex(rules, labels) -> (core, Φ): the maximal complex and its Φ, taken over reachable states.
- the number of distinct groups represented in the core (a group counts if its hub or any of its parties is
  in the core).
- the whole-system Φ and minimum-information-partition cut at the all-ones integrating state, via
  pyphi.new_big_phi.sia.

Control. A single all-spanning hub of the same n: one hub = AND of all parties, every party reads the hub. By
construction this binds every party into one complex, so its core spans all n nodes. It fixes the reading of
"spans all groups" against a topology built to span. The all-spanning hub is fully integrated, so its maximal
complex grows costly fast; the control is read at the tractable size n = 4 (where it spans all 4 nodes,
Φ = 3.000), and n >= 6 is skipped to keep the probe deterministic and re-runnable.

Reuse. verdict and major_complex from org_frontier.probes.lib; tpm_from_rules and cm_from_rules from the
classifier. Φ is exact IIT-4.0; no reimplementation.

Determinism. numpy seeded with 0; the Φ library seeds its search with numpy.random.default_rng(0). The probe
opens with an instrument control on the faithful triad, which must read 'triadic' at max Φ 2.0 with a spanning
core. Re-runs are byte-identical.

Scope. Synthetic Boolean coordination forms under exact Φ. "Core", "span", and "seam" are graph-and-Φ
quantities, not measured field constructs. The Φ-to-organization bridge is open.
