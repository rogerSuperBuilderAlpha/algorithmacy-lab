# Q208 — Stage 4 methods

Every test reproduces from this file and `probe_latency_depth.py`. One script sweeps the buffer depth and
runs all five hypotheses.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`).
- Exact Φ: PyPhi IIT-4.0, `PHI_EPS = 1e-9`.
- Python: run from the repo root with the project venv active.

Rules are little-endian: `rules[j](x)` reads `x[0], x[1], …` and returns node j's next bit.

## The depth-k form F_k (n = 3 + k)
Node order: W (0), S (1), C (2), then buffers B1 (3), B2 (4), …, Bk (3+k−1).
- **Mediator:** `S' = W ∧ C` every step — `x[0] & x[2]`.
- **Delay line:** `B1' = S`, and `Bj' = B(j−1)` for j ≥ 2 — the buffers shift the mediator's output along.
- **Parties:** for k = 0, `W' = S`, `C' = S`; for k ≥ 1 the parties read the *last* buffer,
  `W' = Bk`, `C' = Bk` — the mediator reaches them k steps late.

F_0 is the synchronous triad. F_1 reproduces q205's single-buffer form. The sweep is k = 0, 1, 2, 3,
i.e. n = 3, 4, 5, 6. Exact Φ at n=6 is the slow point (~1 minute); the sweep stays within it.

## Instrument control (run first)
F_0 must read triadic with Φ_MIP = 2.000000 before any other number is reported. The probe asserts this
and aborts on failure.

## H1 test
- **Form:** F_0. **Measure:** `verdict(F_0)`. **Decision:** triadic and max_phi = 2.0.

## H2 test
- **Forms:** F_1, F_2, F_3. **Measure:** `verdict(F_k).structure`. **Decision:** all triadic → SUPPORTED;
  any dyadic refutes and locates the breaking depth.

## H3 test
- **Forms:** F_0..F_3. **Measure:** `verdict(F_k).max_phi`. **Decision:** strictly decreasing in k →
  SUPPORTED.

## H4 test
- **Forms:** F_1..F_3. **Measure:** `major_complex(F_k).core`. **Decision:** {B1..Bk} ⊆ core at every k →
  SUPPORTED.

## H5 test
- **Forms:** F_1..F_3. **Measure:** `major_complex(F_k).core`. **Decision:** "W" ∉ core at every k ≥ 1 →
  SUPPORTED.
