# Q7: party noise vs mediator noise findings

Form: triadic conjunctive mediated chain, W' = S, S' = W∧C, C' = S, labels (W,S,C).
Noise: output flip-noise on a TPM column, P(out=1) = (1−p)·clean + p·(1−clean), grid p = 0.00…0.50 step 0.01.
Sites: mediator S (col 1), party W (col 0), party C (col 2), joint WC (cols 0,2).
Instrument (all sites, p=0): triadic, Φ=2.0, MIP {W,SC}. PASS.
Measure: Φ_MIP via `max_phi_float`; verdict/MIP via `classify`; PHI_EPS=1e-9, TOL=1e-6.

| H | Claim | Verdict | Key numbers | Source |
|---|---|---|---|---|
| H1 | party (W) and mediator (S) trace different Φ(p) curves | confirmed | g_max=0.9237 @ p=0.01; Φ_W(0.10)=0.7632 vs Φ_S(0.10)=1.1887 (g=−0.4255); self-ctrl=0.0 | results/h1_party_vs_mediator.csv, probe_party_vs_mediator.py |
| H2 | W-noise and C-noise are the same curve | confirmed | 0/51 points \|d\|>1e-6, max\|d\|=0.0; flip_W=flip_C=0.5; pos-control 49/51 \|W−S\|>TOL, max=0.9237 | results/wc_symmetry.csv, probe_wc_symmetry.py |
| H3 | party verdict flips at interior p < 0.5 | refuted | p_v(S)=p_v(W)=0.5; p_eff(S)=p_eff(W)=0.5; both triadic at every interior p, dyadic only at 0.5 | results/q7_verdict_flip.csv, probe_verdict_flip.py |
| H4 | party noise steeper and below across interior | refuted | m_W=102.44 > m_S=10.06 (slope half holds) BUT Φ_W<Φ_S at only 32/49 interior; crosses, first reversal p=0.33; ordering fails | results/q7_slope_asymmetry.csv, probe_slope_asymmetry.py |
| H5 | joint parties non-separable AND collapse advances | partial | non-sep CONFIRMED: r_max=1.4558 @ p=0.01, Φ_WC(0.10)=1.3738 > Φ_pred=0.2912 > single Φ_W=0.7632, residual >0 everywhere; advance REFUTED: p_eff(WC)=p_eff(W)=0.5; self-ctrl r_max=0.0 | results/h5_joint_party.csv, probe_joint_party.py |

## Reading across (probes #145–#149)

The seat that carries the flip sets the curve. Party noise and mediator noise are two distinct Φ(p) curves (H1, gap 0.92 near the clean corner, party below). The two parties are one seat: W and C overlay exactly and flip together (H2). The asymmetry is a Φ phenomenon, not a verdict one: both sites hold triadic at every interior p and snap to dyadic only at p=0.5 (H3), so the verdict instrument cannot separate them. Party noise drops about 10× steeper near the clean corner, then the curves cross at p≈0.33 and the party curve rises back above the mediator in the noisy regime, so the fixed-sign ordering fails (H4). Joint-party noise is strongly non-separable and runs opposite to the prior: it preserves more integration than the multiplicative null and than a single party, and leaves the collapse at p=0.5 (H5). Locus of the flip is a real degree of freedom for Φ and a confined one for the verdict.
