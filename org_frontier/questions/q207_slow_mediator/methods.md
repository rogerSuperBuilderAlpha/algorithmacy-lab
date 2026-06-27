# Q207 — Stage 4 methods

Every test reproduces from this file and `probe_slow_mediator.py`. One script runs all five hypotheses; all
forms are small (n ≤ 4) deterministic Boolean systems read with the existing instrument.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`).
- Exact Φ: PyPhi IIT-4.0, `PHI_EPS = 1e-9`.
- Python: run from the repo root with the project venv active.

Rules are little-endian: `rules[j](x)` reads `x[0], x[1], …` and returns node j's next bit.

## The forms
- **F0 (synchronous triad, n=3)**, labels (W,S,C): `[x[1], x[0]&x[2], x[1]]`.
- **F_slow (half-rate mediator, n=4)**, labels (W,S,C,K): `W'=x[1]`, `S' = (x[0]&x[2]) if x[3] else x[1]`,
  `C'=x[1]`, `K'=1-x[3]`. The clock K toggles every step; the mediator recomputes W∧C only when K=1 and
  holds its value otherwise, so it commits at half the parties' rate.
- **F_held (zero-rate control, n=4)**, labels (W,S,C,K): `W'=x[1]`, `S'=x[1]` (the mediator holds its own
  value, `S'=S`, never recomputing W∧C), `C'=x[1]`, `K'=1-x[3]`. The mediator is frozen and the parties
  copy it, so nothing reads W or C — the form should factor.

## Instrument control (run first)
F0 must read triadic with Φ_MIP = 2.000000 before any other number is reported. The probe asserts this and
aborts on failure.

## H1 test
- **Form:** F0. **Measure:** `verdict(F0)`. **Decision:** triadic and max_phi = 2.0.

## H2 test
- **Form:** F_slow. **Measure:** `major_complex(F_slow)` core, and `verdict(F_slow)`. **Decision:**
  {W,S,C} ⊆ core and verdict triadic → SUPPORTED; the core dropping any of W, S, C refutes.

## H3 test
- **Form:** F_slow. **Measure:** `major_complex(F_slow)` core. **Decision:** "K" ∉ core → SUPPORTED.

## H4 test
- **Form:** F_slow. **Measure:** `major_complex(F_slow).core_phi`. **Decision:** core_phi < 2.0 − PHI_EPS
  → SUPPORTED.

## H5 test
- **Form:** F_held. **Measure:** `verdict(F_held)` and `major_complex(F_held)` core. **Decision:** dyadic,
  or {W,S,C} ⊄ core → SUPPORTED (a never-committing mediator cannot bind the triad).
