# Methods (summary — full version in paper_draft.md §3)

A constructive instantiation of the Complex Brain Hypothesis (Mago et al. 2026) on exactly-computable
systems. We implement entropy H, TSE neural complexity Cₙ, apparent complexity under coarse-graining,
and exact IIT-4.0 Φ, validate each on controls, then run three experiments plus a matched-entropy
dissociation.

- **Measures** (`complexity.py`): `entropy_bits` (Shannon H); `integration` (total correlation);
  `tse_complexity` (Tononi–Sporns–Edelman 1994, integration-based, subset-sampled for large n);
  `apparent_complexity` (entropy of coarse-grained block-magnetization distribution at a grain). Exact Φ
  reused from `proxy_audit.exact_phi`.
- **Validation** (run before any sweep): Cₙ = I = 0 for independent bits; Cₙ larger for a structured
  system than for independent or fully-redundant; apparent complexity 0 for uniform, positive for
  structured; entropy maximal for uniform.
- **Experiment A** (`ising.py`): exact 4×4 periodic 2D Ising; enumerate 2^16 configs; Boltzmann
  distribution per temperature; exact H(T), Cₙ(T), apparent complexity.
- **Experiment B**: Metropolis-sampled 16×16 lattice; apparent complexity at grains 1,2,4,8 at low,
  critical, high temperature.
- **Experiment C** (`run.py`): parity-ring dynamical system (n=4, each node = XOR of ring-neighbours);
  noise sweep order→disorder; exact IIT-4.0 Φ, Cₙ and H of the stationary distribution.
- **Dissociation** (`dissociation.py`): parity ring vs independent biased bits matched on entropy.

Pre-registered claims: **C1** entropy monotone, complexity non-monotone (peaks at structure);
**C2** apparent complexity grain-dependent (disordered state collapses under coarse-graining).
