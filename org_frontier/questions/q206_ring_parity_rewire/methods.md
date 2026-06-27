# Q206 — Stage 4 methods

Every test reproduces from this file and `probe_ring_parity_rewire.py`. The probe reuses q146's rewiring
machinery (in-degree-2 Watts-Strogatz endpoint rewiring on a six-node ring) and adds a coupling-family
switch and a finer p-grid.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`).
- Exact Φ: PyPhi IIT-4.0, `PHI_EPS = 1e-9`.
- Python: run from the repo root with the project venv active.

## The forms
- **Ring (n=6)**: node i reads its two ring neighbours (i−1, i+1) mod 6.
- **Conjunctive coupling**: node = AND of its current input sources.
- **Parity coupling**: node = XOR of its current input sources.
- **Rewiring**: for each input edge, with probability p replace its source with a uniform random source
  that is not the node itself and not already an input (in-degree 2 preserved). Identical to q146's
  `rewire`.

## Sweep (as run)
- **Conjunctive grid**: p ∈ {0.0, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 1.0}, five seeds per stochastic point.
  The added points fill the interior of q146's unresolved (0.25, 0.5).
- **Parity grid**: p ∈ {0.0, 0.35, 1.0}, one seed per stochastic point. p=0.35 is the conjunctive collapse
  point, chosen for the decisive coupling comparison; p=1.0 is the disorder extreme.
- p=0 is the single deterministic lattice; every p>0 draws a seeded rewiring (BASE_SEED + a per-(coupling,
  p, seed) offset so each draws an independent stream). Per network: whole-system verdict and max Φ_MIP.

**Deviation from pre-registration (compute-driven, documented).** The Stage-3 methods specified a nine-point
grid and three seeds for *both* couplings, and the whole-system major complex per network. Two costs forced
a reduction discovered only at run time: a parity (XOR) ring at n=6 costs ≈ 416 s per exact-Φ evaluation
(vs ≈ 26 s conjunctive), so a full parity sweep is infeasible in this environment; and `major_complex` is
not needed by any hypothesis here, so it is dropped. The conjunctive arm therefore runs the fuller grid at
five seeds, and the parity arm runs three diagnostic points at one seed. The hypotheses are unchanged; the
parity arm's coarseness is itself a reported result (the cost asymmetry) and the finer parity grid is left
as an open edge.

## Instrument control (run first)
The faithful triad `[x1, x0&x2, x1]` must read triadic at Φ_MIP = 2.000000 before any sweep number is
reported. The probe asserts this and aborts on failure.

## H1 test
- **Measure:** `verdict(triad)`. **Decision:** triadic and max_phi = 2.0.

## H2 test
- **Form:** conjunctive grid. **Measure:** per-p mean Φ_MIP and the seed verdicts. **Decision:** a dyadic
  seed appears at some p in (0.25, 0.5) and the mean-Φ sequence is non-increasing → SUPPORTED.

## H3 test
- **Form:** parity ring at p=0. **Measure:** whole-system Φ_MIP. **Decision:** |Φ − 4.0| > PHI_EPS →
  SUPPORTED.

## H4 test
- **Form:** parity grid. **Measure:** per-p mean Φ_MIP. **Decision:** mean Φ at p=1 < mean Φ at p=0 with a
  non-increasing trend → SUPPORTED.

## H5 test
- **Forms:** both grids. **Measure:** the smallest p with any dyadic seed, per coupling. **Decision:**
  parity's first-dyadic p > conjunctive's → SUPPORTED.
