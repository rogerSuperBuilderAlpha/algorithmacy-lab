# q175 — methods

## Machinery

The probe imports the on-disk field bridge `org_frontier.field.rule_to_phi` built by q173:
`rule_to_phi` encodes per-party coded determination rules into a TPM and reads the exact IIT-4.0 Φ
verdict over the MIP, and `phi_ci` propagates coder disagreement into a Φ interval. Φ is not
reimplemented; the bridge wraps `org_frontier.classifier`. `PHI_EPS = 1e-9` is the classifier's
irreducibility floor.

## Coded rule sets

The specific worker is the faithful worker-system-counterpart triad on nodes (W, S, R) with
S = W & R. The substitutable pool of size k is built on nodes (D1, ..., Dk, S, R) with
S = (D1 | ... | Dk) & R; each pool member is driven by S and R is driven by S. The probe reads the
specific set and the pooled sets for k = 2, 3, 4 (system sizes n = 4, 5, 6) through `rule_to_phi`
and records the structure and max_phi.

## Contested coder panels (H2)

Each contested form is a synthetic panel of 12 coders. Each coder reads the account either as
specific (Φ = 2.0) or as pooled (Φ = 0.0). The fraction of specific-readers is drawn uniformly from
the genuine-contest band [0.30, 0.70]; a panel is contested when both readings appear. The panel is
carried through `phi_ci`, and the propagated reading interval is the 2.5/97.5 percentile span of the
coder Φ readings. The interval surfaces the flip when its lower endpoint is at 0 (<= PHI_EPS) and
its upper endpoint is above 0. The probe draws 600 panels and reports the fraction of contested
forms whose interval spans [0, specific Φ].

A contested categorical reading is a split between two readings, so the interval that surfaces it is
the span of the readings, not a confidence band on their mean. The bridge's bootstrap-t CI is a band
on the mean Φ; this study reads the flip from the percentile span of the readings the bridge carries.

## Determinism

All RNG is seeded with fixed generators (`numpy.random.default_rng`). The probe output is
byte-identical across re-runs.

## Controls

Control 1 reads the specific rule set and asserts triadic at max_phi = 2.0. Control 2 runs a
unanimous-pool panel through `phi_ci` and asserts the CI is degenerate at [0, 0]. Both must pass
before the result lines print.

## Scope

The rule sets and coder panels are synthetic, with known ground truth. The study tests what a coding
choice does to the verdict and what the disagreement interval reports, not a measured coordination.
Results are on synthetic data.
