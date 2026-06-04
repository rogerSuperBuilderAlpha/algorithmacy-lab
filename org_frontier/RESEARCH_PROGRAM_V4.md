# Research program v4 — new hypotheses from the v1–v3 results

This round reads the 118-probe logbook and turns its results into the next hypotheses. Each project below
names the prior result it grows from. Numbering continues: v4 probes start at 119. Same loop — script,
run, log to `probes/PROBES.md`, update the status table, commit, push. Runs on `worktree/org-frontier`.

The freshest results, and the questions they raise:

- **Symmetric multi-hub beats a single hub (#118).** Two symmetric hubs hold the full core at higher Φ
  than one. How does Φ move with the number of mediators, and where is the ceiling?
- **Two scaling laws (#115, #116).** Conjunctive Φ = n−1 (grows), parity Φ = 2^(2−n) (fades), both full
  core. Does the parity hub ever go numerically dyadic, and what do real control structures look like?
- **A transferable, cheap surrogate (#99, #100, #114).** It transfers across size and the signal is party
  coupling. Does it transfer to topology families it never trained on, and is the single coupling feature
  enough? Can a hybrid CES+coupling predicate be exact where neither part alone is (#102)?

## J. The geometry of the scaling laws

- **J1 — multihub-law** `[X]` — H: Φ rises with the number of symmetric mediators, approaching the
  all-to-all pool as every node becomes a mediator. M: a symmetric m-hub at fixed n; sweep m and read Φ
  and the core. Builds on #118, #104. Out: `probe_multihub_law.py`.
- **J3 — parity-dissolution** `[R]` — H: the parity hub's Φ = 2^(2−n) stays positive but crosses below a
  detectable floor at a computable size, so XOR coordination effectively dissolves at scale. M: verify
  Φ = 2^(2−n) at n=6,7 and extrapolate the size where Φ < 1e−6. Builds on #115. Out:
  `probe_parity_dissolution.py`.
- **L1 — org-control-structures** `[R]` — H: most real control structures (dual authorization, separation
  of duties) are conjunctive and so scale robustly; genuine parity (XOR) structures are rare, which is why
  the parity blind spot seldom bites in practice. M: model named control structures, classify each
  commit's type and verdict. Builds on #115, #50, #68. Out: `probe_control_structures.py`.

## K. The cheap instrument, hardened

- **K1 — coupling-transfer** `[R]` — H: the single coupling feature (mean pairwise MI) transfers across
  size like the full surrogate. M: train a one-feature model on n=3, test on n=4,5. Builds on #99, #114.
  Out: `probe_coupling_transfer.py`.
- **K2 — ood-surrogate** `[X]` — H: the n=3 strict-mediation surrogate classifies topology families it
  never saw (multi-hub, parity, threshold, chain, tree). M: score the trained surrogate on labelled forms
  from the new families. Builds on #99, #118, #115. Out: `probe_ood_surrogate.py`.
- **K3 — hybrid-predicate** `[X]` — H: a CES-count OR party-coupling predicate is exact where neither part
  alone is (#102 missed only the parity forms; coupling catches them). M: search hybrid predicates over the
  corpus for zero error. Builds on #102, #114. Out: `probe_hybrid_predicate.py`.

## Waves and status

| Wave | Projects | Lane | Status |
|------|----------|------|--------|
| X1 | J1 J3 L1 | R/X | **done** (probes 119–121; all confirmed — Φ rises with hubs toward the pool, parity dissolves at n=22, everyday controls are conjunctive) |
| X2 | K1 K2 K3 | R/X | **done** (probes 122–124; K1 confirmed, K2/K3 refuted — instrument is family-specific and a screen, not exact) |

**Program v4 complete.** Probes 119–124 close both waves. The scaling laws gained a geometry (Φ rises
with symmetric mediators toward the pool; parity dissolves near n=22) and a real-world reading (everyday
controls are conjunctive, parity is exotic). The cheap instrument reduces to party coupling and transfers
across size, but not across topology, and no hard threshold makes it exact — it is a family-specific
ranked screen. The logbook stands at 124 probes.

Stop rule: all Lane-R/X projects done. Probe numbering continues from 118.
