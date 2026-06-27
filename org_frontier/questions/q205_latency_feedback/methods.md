# Q205 — Stage 4 methods

Every test reproduces from this file and `probe_latency_feedback.py`. One script runs all five hypotheses.

## Shared infrastructure
- Verdict / Φ / major complex: `classifier.classifier` (`classify`, `classify_rules`, `tpm_from_rules`,
  `cm_from_rules`), `probes/lib.py` (`verdict`, `major_complex`).
- Exact Φ: `proxy_audit/exact_phi.py` via PyPhi IIT-4.0 (`new_big_phi`), `PHI_EPS = 1e-9`.
- Python: run from the repo root with the project venv active.

Rules are little-endian: `rules[j](x)` reads `x[0], x[1], …` and returns node j's next bit.

## The forms
- **F0 (immediate triad, n=3)**, labels (W,S,C): `[x[1], x[0] & x[2], x[1]]` — W'=S, S'=W∧C, C'=S.
- **F1 (represented latency, n=4)**, labels (W,S,C,B): `[x[3], x[0] & x[2], x[3], x[1]]` — W'=B, S'=W∧C,
  C'=B, B'=S. The buffer B holds S's previous output; the parties read the mediator one step late.

## Estimation procedure (for the hidden-latency forms)
A long deterministic-plus-noise trajectory is simulated and a one-step state-by-node TPM over the chosen
units is estimated by counting, exactly as q204 estimates a TPM from a real sequence. Parameters fixed
before the run: `STEPS = 20000`, warmup `200`, output-flip noise `p = 0.05`, seed `0`. The connectivity
matrix is inferred numerically (node i feeds node j iff flipping i changes column j of the estimated TPM
by more than `1e-6`). The estimated TPM and inferred CM are passed to `classify`.

- **F2 (hidden latency, n=3):** simulate F1, record only (W,S,C), estimate the one-step TPM, classify.
- **estF0 (estimation control, n=3):** simulate F0, record (W,S,C), estimate the one-step TPM, classify.

## Instrument control (run first)
F0 must read `triadic` with Φ_MIP = 2.000000 before any other number is reported. The probe asserts this
and aborts on failure.

## H1 test
- **Form:** F0. **Measure:** `verdict(F0)`. **Decision:** structure == triadic and max_phi == 2.0.
- **Script:** `probe_latency_feedback.py`.

## H2 test
- **Form:** F1. **Measure:** `verdict(F1)`. **Control:** F0 (H1). **Decision:** F1 structure == triadic
  and max_phi > PHI_EPS confirms; dyadic refutes.

## H3 test
- **Form:** F1. **Measure:** `major_complex(F1)` core label tuple. **Decision:** "B" in the core confirms;
  a core of exactly {W,S,C} (or any core excluding B) refutes.

## H4 test
- **Form:** F2 (estimated, units (W,S,C)). **Measure:** `verdict` on the estimated TPM/CM. **Control:**
  F1 is triadic (H2). **Decision:** F2 structure == dyadic (max_phi ≤ PHI_EPS) while F1 is triadic confirms
  that unrepresented latency hides integration; F2 triadic refutes.

## H5 test
- **Form:** estF0 (estimated, units (W,S,C)). **Measure:** `verdict` on the estimated TPM/CM. **Decision:**
  estF0 structure == triadic confirms the H4 effect is specific to latency, not an artifact of estimation;
  estF0 dyadic refutes (the estimation procedure alone would then explain H4).
