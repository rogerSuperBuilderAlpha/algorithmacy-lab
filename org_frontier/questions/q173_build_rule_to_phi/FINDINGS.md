# q173 — findings

The field bridge `org_frontier/field/rule_to_phi.py` encodes per-party coded determination rules
into a TPM, reads the exact-Φ verdict, and propagates coder disagreement into a Φ confidence
interval. Both validation hypotheses hold on synthetic controls.

## Controls

The decoupled rule set `[x0, x1, x2]` reads `dyadic`. The faithful triad `[x1, x0&x2, x1]` reads
`triadic` with max Φ_MIP = 2.000000. Three identical coder readings give alpha = 1 and a
degenerate CI [2.000000, 2.000000]. PASS.

## Results

| arm                         | quantity                  | value    | criterion        |
|-----------------------------|---------------------------|----------|------------------|
| H1 verdict reproducibility  | verdict-flips / 250 forms | 0        | = 0              |
| H1 zero anchor              | alpha=1 CI degenerate     | True     | degenerate       |
| H2 CI coverage              | coverage / 500 panels     | 0.9440   | in [0.93, 0.97]  |

The bridge never disagrees with `classify_rules` across 250 sampled rule forms, so encoding the
rules into a TPM and reading the verdict reproduces the classifier exactly. Under perfect coder
agreement the CI collapses to the point [2.0, 2.0]. When 12 coders disagree on which active-bit
cells are set, the studentized bootstrap-t CI brackets the consensus Φ of 2.0 on 94.4% of panels,
inside the nominal 95% band.

## Verdicts

- **H1 (verdict reproducibility + degenerate CI under agreement): SUPPORTED.** 0 verdict-flips
  over 250 forms; degenerate CI at alpha = 1.
- **H2 (coder-weighted CI brackets the consensus Φ at nominal 95%): SUPPORTED.** Coverage 0.944,
  inside [0.93, 0.97].

## Scope

The rule sets and coder panels are synthetic, with known ground truth. The study validates the
machinery, not a measured coordination. The coded-account-to-observation gap is not closed here.
Results are on synthetic data.
