# Research program v3 — the edges program v2 left

Program v2 closed at Probe 112. It left three sharp edges, and this round works them. Numbering
continues: v3 probes start at 113. Same loop — write a script, run on the IIT-4.0 venv, log to
`probes/PROBES.md`, update the status table, commit, push. This round runs on the `worktree/org-frontier`
worktree of the IIT repo.

The three edges:

- **The parity blind spot.** The 8 pure-higher-order (parity) determinations (#56) are the universal hard
  case: Φ_AR under-ranks them (#101) and every cheap CES predicate misses exactly them (#102). What are
  they, and is there any cheap signal that catches them?
- **The all-required scaling law.** A single conjunctive hub stays triadic with the full group in its core
  and Φ = n−1 from n=4 to n=7 (#105); distributing the mediation fragments the core (#103). Is Φ = n−1 a
  law, which commits scale, and was the fragmentation an artifact of an asymmetric design?
- **The holistic residual.** The 7% of the n=3 verdict the graph cannot decide is holistic (#106, #13).
  (Parked for this round; noted as the next edge.)

## G. The parity blind spot

- **G1 — parity-characterization** `[R]` — H: the cheap-measure blind spot is exactly the XOR-family
  (parity) determinations. M: over the 24 triadic corpus forms, label each commit as conjunctive vs
  parity; cross-tab with Φ (2.0 vs 0.5), CES counts, and whether each cheap measure flags it. Builds on
  #56, #101, #102. Out: `probe_parity_characterization.py`.
- **G2 — parity-detector** `[R]` — H: a synergy-targeted feature separates parity-triadic from dyadic
  where Φ_AR and relation counts do not. M: for each cheap feature, compute its AUC restricted to
  parity-triadic vs dyadic; identify the feature the surrogate (#85) must be using to catch parity. Builds
  on #85, #102, #46. Out: `probe_parity_detector.py`.
- **G3 — parity-scaling** `[R]` — H: the parity family stays pure-higher-order and scales differently from
  the conjunctive hub. M: build the all-parity commit (S = XOR of all parties, parties read S) at n=3,4,5;
  read Φ and the core. Builds on #56, #105. Out: `probe_parity_scaling.py`.

## H. The all-required scaling law

- **H1 — conjunctive-law** `[X]` — H: Φ = n−1 exactly for the conjunctive hub, and it is the form that
  scales. M: verify Φ = n−1 up to n=8; compare AND-all vs OR-all at the floor for the full-core property.
  Builds on #105, #30. Out: `probe_conjunctive_law.py`.
- **H2 — threshold-commits** `[X]` — H: only extreme thresholds (AND, OR) keep the full core as the group
  grows; intermediate thresholds (majority) factor. M: k-of-n threshold commits at n=4,5; report which
  keep all parties in the core. Builds on #10, #67. Out: `probe_threshold_scaling.py`.
- **H3 — symmetric-multihub** `[X]` — H: the two-hub fragmentation (#103) was an artifact of an asymmetric
  build; a symmetric two-hub keeps the full core. M: build a symmetric two-hub (both hubs read all parties
  and each other) at n=6,7; compare the core to the single hub. Builds on #103. Out:
  `probe_symmetric_multihub.py`.

## Waves and status

| Wave | Projects | Lane | Status |
|------|----------|------|--------|
| W1 | G1 G2 G3 | R | **done** (probes 113–115; all confirmed — blind spot = XOR family, caught by MI[W;C], scales as Φ=2^(2−n)) |
| W2 | H1 H2 H3 | X | pending |

Stop rule: all Lane-R/X projects done. Probe numbering continues from 112.
