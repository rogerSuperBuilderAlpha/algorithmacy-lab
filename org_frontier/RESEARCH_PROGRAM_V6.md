# Research program v6 — questions from the v5 results

v5 left three openings. The holistic residual gave partial ground: it is one-sided (all false positives,
coupling necessary not sufficient), global dynamics closes about half, and ~5% stays holistic (#125–127).
The multi-hub core drops its peripheral parties at intermediate mediator counts (#128). The cheap
surrogate stays family-bound even with diverse training (#129). This round works each opening. Probes
continue at 130. Runs on `worktree/org-frontier`.

## P. Pinning the residual

- **P1 — attractor-condition** `[R]` — H: among the three-way-coupled wirings, a single globally
  attracting fixed point is the dyadic condition — the residual forms are exactly the ones whose dynamics
  collapses. M: from the cached residual panel, restrict to n_bidir==3 and test how well attractor-type
  features separate the verdict. Builds on #125, #127. Out: `probe_attractor_condition.py`.
- **P2 — holistic-core** `[R]` — H: the ~5% no cheap feature reaches are a scattered, near-boundary set,
  not a coherent missed structure. M: from the panel, find the forms a full-feature random forest still
  misclassifies and describe where they sit in feature space. Builds on #126. Out:
  `probe_holistic_core.py`.

## Q. The scaling-law zoo

- **Q1 — scaling-zoo** `[X]` — H: commit topologies fall into distinct Φ-vs-size law classes — constant
  (chain), linear (conjunctive hub), super-linear (pool), exponential decay (parity) — and a ring gives a
  fifth. M: build chain, ring, conjunctive hub, pool, and parity hub at n=3..6; fit the Φ(n) law class for
  each. Builds on #104, #116, #115. Out: `probe_scaling_zoo.py`.

## R. Structural and instrument fixes

- **R1 — party-peer-coupling** `[X]` — H: giving the parties peer edges keeps them in the core at the
  intermediate mediator counts where they otherwise drop (#128). M: a symmetric m-hub with added
  party-to-party coupling; check whether the full core returns at the intermediate m. Builds on #128. Out:
  `probe_party_peer_coupling.py`.
- **R2 — invariant-feature** `[X]` — H: a size-normalized coupling feature transfers across topology where
  raw mean-MI does not (#129). M: compute normalized coupling features on the archetype families and test
  their cross-topology AUC against raw mean-MI. Builds on #129, #122. Out: `probe_invariant_feature.py`.

## Waves and status

| Wave | Projects | Lane | Status |
|------|----------|------|--------|
| Z1 | P1 P2 | R | **done** (probes 130–131; P1 refuted — no attractor condition; P2 confirmed — near-boundary holistic tail) |
| Z2 | Q1 R1 R2 | X | pending |

Stop rule: all Lane-R/X projects done. Probe numbering continues from 129.
