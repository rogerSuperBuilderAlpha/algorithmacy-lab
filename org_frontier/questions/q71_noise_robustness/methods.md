# Q71 — Stage 4 methods (fixed before computation)

The read-recipient triad (E'=M, M'=E∧R, R'=M) and the broadcast (E'=M, M'=E, R'=M) are converted to
deterministic state-by-node TPMs with `classifier.tpm_from_rules`, then perturbed: each entry is flipped
with probability epsilon, giving a stochastic TPM det*(1-eps)+(1-det)*eps. Exact IIT-4.0 Φ (max over
states) is computed with `probes.lib.max_phi_float`, which accepts a stochastic state-by-node TPM and
infers the connectivity numerically. Run on `~/iit-playground/venv-4.0/bin/python`. epsilon in
{0, 0.05, 0.1, 0.2, 0.3, 0.5}. Decision rules fixed here.

## Test (`probe_noise_robustness.py`)

- **Measure:** max-Φ of the noisy triad and the noisy broadcast at each epsilon.
- **Decision rules:**
  - H1 confirmed if triad Φ > 0 at epsilon = 0.05 and 0.1.
  - H2 confirmed if triad Φ is non-increasing across the epsilon grid.
  - H3 confirmed if triad Φ < 0.1 at epsilon = 0.5.
  - H4 confirmed if broadcast Φ < 0.1 at every epsilon.
