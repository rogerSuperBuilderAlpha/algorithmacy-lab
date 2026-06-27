# Q210 — Stage 4 methods

Every test reproduces from this file and `probe_shared_counterpart.py`. One script runs all five
hypotheses; the merged forms are n=5 deterministic Boolean systems.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`).
- Exact Φ: PyPhi IIT-4.0, `PHI_EPS = 1e-9`.
- Python: run from the repo root with the project venv active.

Rules are little-endian: `rules[j](x)` reads `x[0], x[1], …` and returns node j's next bit.

## The forms
- **F0 (single triad, n=3)**, labels (W,S,C): `[x[1], x[0]&x[2], x[1]]`.
- **Shared-counterpart forms (n=5)**, labels (W1, S1, W2, S2, C), node order x[0..4]:
  - `W1' = x[1]` (S1)
  - `S1' = x[0] & x[4]` (W1 ∧ C)
  - `W2' = x[3]` (S2)
  - `S2' = x[2] & x[4]` (W2 ∧ C)
  - `C' = bridge(x[1], x[3])` — **none**: `x[1]`; **AND**: `x[1] & x[3]`; **OR**: `x[1] | x[3]`.

## Instrument control (run first)
F0 must read triadic with Φ_MIP = 2.000000 before any other number is reported. The probe asserts this and
aborts on failure.

## H1 test
- **Form:** F0. **Measure:** `verdict(F0)`. **Decision:** triadic and max_phi = 2.0.

## H2 test
- **Form:** AND bridge. **Measure:** `major_complex(AND).core`. **Decision:** {S1, S2} ⊆ core (both
  mediators in one complex) → SUPPORTED; a single-triad core refutes.

## H3 test
- **Form:** AND bridge. **Measure:** `major_complex(AND).core`. **Decision:** "C" ∈ core → SUPPORTED.

## H4 test
- **Form:** AND bridge. **Measure:** `major_complex(AND).core_phi`. **Decision:** core_phi > 2.0 →
  SUPPORTED (merging is super-additive).

## H5 test
- **Forms:** AND bridge, OR bridge. **Measure:** `major_complex(.).core_phi` for each. **Decision:**
  AND core_phi > OR core_phi → SUPPORTED (the combination rule changes the merge). The **none** bridge is
  reported as a third reference point.
