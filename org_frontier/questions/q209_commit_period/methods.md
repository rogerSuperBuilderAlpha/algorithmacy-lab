# Q209 — Stage 4 methods

Every test reproduces from this file and `probe_commit_period.py`. One script sweeps the commit period and
runs all five hypotheses; all forms are small (n ≤ 5) deterministic Boolean systems.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`).
- Exact Φ: PyPhi IIT-4.0, `PHI_EPS = 1e-9`.
- Python: run from the repo root with the project venv active.

Rules are little-endian: `rules[j](x)` reads `x[0], x[1], …` and returns node j's next bit.

## The period-p form F_p
Node order: W (0), S (1), C (2), then counter bits c0 (3), c1 (4) when present.
- **p = 1 (n=3):** the synchronous triad `W'=S, S'=W∧C, C'=S`.
- **p = 2 (n=4):** a 1-bit counter K with `K'=¬K`; `S' = W∧C` when K marks the reset step, else `S'=S`;
  `W'=S, C'=S`. (q207's form.)
- **p = 3, 4 (n=5):** a 2-bit counter (c0 = LSB, c1 = MSB) incrementing mod p; `S' = W∧C` when the counter
  reads zero (c0=c1=0), else `S'=S`; `W'=S, C'=S`. The mod-3 counter cycles 0→1→2→0 (the c0=c1=1 state maps
  to 0); the mod-4 counter cycles 0→1→2→3→0.

The mediator commits `W∧C` once per period and holds its value the rest of the period.

## Instrument control (run first)
F_1 must read triadic with Φ_MIP = 2.000000 before any other number is reported. The probe asserts this and
aborts on failure.

## H1 test
- **Form:** F_1. **Measure:** `verdict(F_1)`. **Decision:** triadic and max_phi = 2.0.

## H2 test
- **Forms:** F_2, F_3, F_4. **Measure:** `verdict(F_p).structure`. **Decision:** all dyadic → SUPPORTED;
  any triadic refutes and identifies a binding period > 1.

## H3 test
- **Forms:** F_2..F_4. **Measure:** `major_complex(F_p).core`. **Decision:** no triad member {W,S,C} in any
  core → SUPPORTED.

## H4 test
- **Forms:** F_2..F_4. **Measure:** `major_complex(F_p).core_phi`. **Decision:** non-decreasing over
  p = 2, 3, 4 → SUPPORTED.

## H5 test
- **Forms:** F_2..F_4. **Measure:** `verdict(F_p).max_phi` and structure. **Decision:** dyadic (the triad
  contributes no whole-system integration) at every p ≥ 2 → SUPPORTED.
