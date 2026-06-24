# q173 — hypotheses

A field bridge encodes per-party coded determination rules into a TPM, reads the exact-Φ
verdict, and propagates coder disagreement into a Φ confidence interval. Both hypotheses are
fixed before the computation.

**H1 (verdict reproducibility + zero-anchored CI).** `rule_to_phi` reproduces the classifier's
dyadic/triadic verdict exactly, with 0 verdict-flips against `classify_rules` over at least 200
sampled per-party rule forms, and under perfect coder agreement (alpha = 1.0) `phi_ci` returns a
degenerate interval [phi, phi].

- H1-null: the bridge disagrees with `classify_rules` on at least one form, or returns a
  non-degenerate CI under perfect agreement.

**H2 (CI coverage).** When coders disagree on which bits are active, the coder-weighted bootstrap
Φ CI covers the consensus-rule Φ at its nominal 95% rate, with empirical coverage in [0.93, 0.97]
over 500 synthetic coder-panel draws.

- H2-null: empirical coverage falls outside [0.90, 0.98], so the CI is miscalibrated.

The rule sets and coder panels are synthetic. The construct validated is the machinery, not a
measured coordination.
