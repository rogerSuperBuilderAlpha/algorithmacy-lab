# Q6 — Commit noise: phase transition or smooth decay? (FINDINGS)

Form: triadic conjunctive mediated chain, n=3, W'=S, S'=W∧C, C'=S (#26/#33/#27). Commit noise p as
output noise on the mediator column: P(S'=1) = (1−p)·s_clean + p·(1−s_clean). Single 51-point grid
p=0.00…0.50, step 0.01, reused by every test. Probes #140–#144.

**Instrument control PASSED** (every test): clean p=0 reads triadic, max_phi=2.000000 (1e-6),
MIP `2 parts: {W,SC}`, and max_phi_float(noisy_tpm(0.0))=2.000000.

**Headline.** Φ_MIP decays smoothly and monotonically 2.0 → 0 with no interior critical point; the
susceptibility has no interior peak (steepest at p=0); the only sharp object is the verdict, which
snaps triadic→dyadic at the degenerate endpoint p=0.5 on a smooth-ramping Φ.

| H | Claim | Verdict | Key numbers | Data |
|---|---|---|---|---|
| H1 | Φ_MIP(p) smooth, no kink/discontinuity | **partial** | exp fit a=2.232008, b=4.405975, c=−0.244293 (SSE 2.78e-04 vs quad 3.57e-02); max interior \|resid\|=0.007867 ≤0.02 ✓; resid ratio 4.06× (>3× ✗); \|Δ²Φ\| ratio 3.68× (<5× ✓, no localized spike); Φ 2.0→0; injected-corner control spikes 9.18× at p=0.25 | `results/q6_smoothness_sweep.csv` |
| H2 | susceptibility dΦ/dp peaks at interior p | **REFUTED** | \|χ\| strictly monotone-decreasing; global max at endpoint p=0.00 (\|χ\|=10.062552), falling to 1.109346 at p=0.50; no interior peak (is_interior_peak=0 everywhere) | `results/q6_susceptibility.csv` |
| H3 | verdict flips only at p=0.5, no interior p* | **confirmed** | triadic at all 49 interior pts + p=0; dyadic only at p=0.50; 0/49 interior dyadic; major complex {W,S,C} throughout; Φ_MIP 2.0→...→0.011093 (p=0.49)→0 | `results/q6_verdict_interior.csv` |
| H4 | sharp verdict on smooth Φ (decoupling) | **confirmed** | exactly 1 label-change interval [0.49,0.50] width 0.01, constant before/after; max single-interval \|ΔΦ\|=0.100626 at [0.00,0.01]=5.03% of the 2.0 fall (<25%); drops monotone-decreasing | `results/h4_decoupling.csv` |
| H5 | Φ_MIP strictly monotone, no interior max | **confirmed** | 50 δ_k all negative (min −0.1006255, max −0.01109346); rises>tol(1e-6)=0; interior peaks=0; #81 U-shape control flags 25 rises | `results/q6_monotonicity_sweep.csv`, `results/q6_monotonicity_control_u_shape.csv` |

Reference Φ values (shared sweep): Φ(0)=2.000000, Φ(0.10)=1.188722, Φ(0.25)=0.500000,
Φ(0.40)=0.138346, Φ(0.49)=0.011093, Φ(0.50)=0.000000.

**Reading.** Smooth-decay precedent [mediano2019measuring] matches; the susceptibility-peak expectation
[niizato2020continuity; popiel2020emergence] fails to transfer to this form. H1's partial is the
auxiliary 3×-median gate only (no refutation condition met, no kink). The verdict carries the sharp
transition mean Φ lacks [niizato2020continuity], here as a step in the binary label while Φ magnitude stays smooth.

Probes: `probe_q6_smoothness.py`, `probe_q6_susceptibility.py`, `probe_q6_verdict_interior.py`,
`probe_q6_decoupling.py`, `probe_q6_monotonicity.py`.
