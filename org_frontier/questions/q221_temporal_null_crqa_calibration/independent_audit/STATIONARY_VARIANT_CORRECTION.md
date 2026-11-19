# Stationary-law correction: A_self, B_xor, and B_xor_memory

**Status:** verified numerical regression check; exploratory, not an IIT result.

The repository's `identifiability/phi_detail.py` uses `B_xor: H'=X XOR Y`, whereas earlier independent finite-sample files use `B_xor_memory: H'=H XOR X XOR Y`. All three models use `X'=X`, `Y'=Y`, and independent flip probability 0.08 at each node.

Exact 8-state transition matrices were enumerated and stationary probabilities iterated to numerical convergence. Stationary H lag-one self-match probabilities are:

| Variant | H lag-one self-match | Uniform eight-state stationary law? |
|---|---:|---|
| A_self (`H'=H`) | 0.92000000 | Yes |
| B_xor (`H'=X XOR Y`) | 0.74893568 | **No** |
| B_xor_memory (`H'=H XOR X XOR Y`) | 0.50000000 | Yes |

The B_xor stationary law has X/Y persistence and H tracking their XOR with delay; it is **not** legitimate to substitute a uniform joint state distribution when computing population recurrence profiles or conditional mutual information.

These numerical facts are pinned in `test_rule_variants.py` (two tests passed in an independent NumPy environment). They are not exact-Φ computations. The historical IIT-target exclusion remains unchanged.

**Action required:** identify the exact rule variant behind each prior analytical, finite-sample, and CMI result. Recompute any B_xor profile/CMI calculation that assumed a uniform joint stationary distribution. Do not pool results across variants or claim all-lag profile equivalence for B_xor until checked against its actual stationary law. The bounded-search report must be evaluated separately.
