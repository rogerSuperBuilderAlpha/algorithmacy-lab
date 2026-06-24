# q195 — review

What the probe shows. On the synthetic cohort the partial correlation r(Φ_coord, ACS | SE, BE) is +0.40
with a 95% CI that excludes 0, and Φ_coord tracks ACS (+0.40) more tightly than self-efficacy (+0.10),
with the bootstrap difference CI excluding 0. Both hypotheses are supported. The instrument control
passed.

What it does not show. The cohort is simulated, so the discriminant separation is planted: ACS and the
coordination latent share variance that self-efficacy does not reach. The probe demonstrates that the Φ
bridge recovers that planted structure and survives the standard nuisance controls, and that the
hierarchical regression and the dependent-correlation bootstrap behave as designed. It is not evidence
that a real cohort separates algorithmacy from generic competence; that requires fielding the survey.

Robustness notes. Self-efficacy was deliberately made to correlate with ACS at +0.45 so the H1 partial
is not a controlled-for null. Φ_coord takes two values (0.0, 2.0), so its association is a between-form
contrast; the partial and the bootstrap both respect that. The ΔR² of +0.13 confirms the partial is not
an artifact of a degenerate nuisance block. Determinism is exact: seed 0 for the cohort, seed 0 for the
bootstrap, Φ memoised on the two forms; three runs are byte-identical.

Place in the line. This is the discriminant-validity study of the survey arm, building on the study-1
bridge module. Later studies test measurement invariance, growth, and sub-competences. The shared
`phi_bridge.py` now exposes `simulate_cohort_full`, `partial_corr`, and `steiger_diff` for those.
