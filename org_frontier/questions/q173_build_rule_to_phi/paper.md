# q173 — A rule-to-Φ field bridge with a coder-disagreement confidence interval

A coded account of a coordination names, for each party, a determination rule: that party's next
state as a Boolean function of the current states of all parties. This study builds the bridge
that turns such an account into an exact-Φ verdict and, when coders disagree on the coding,
turns that disagreement into a Φ confidence interval. The bridge is `org_frontier/field/
rule_to_phi.py`, study 1 of the field line; later field studies import it.

## What the bridge does

`rule_to_phi(rules, labels)` encodes the per-party rules into a deterministic state-by-node TPM
and runs the exact IIT-4.0 Φ classifier over the minimum-information partition, returning the
dyadic or triadic verdict and the max Φ_MIP. Φ is not reimplemented; the module wraps the repo's
classifier and probe library.

Coding is done by people, who disagree. Each coder supplies a reading of the same account: which
states and bits are active. `krippendorff_alpha` scores their agreement on the active-bit matrix.
`phi_ci` takes the panel of per-coder Φ readings and returns a studentized bootstrap-t interval.
Identical readings collapse the interval to a point.

## Two claims, two checks

The first claim is reproducibility. Encoding rules into a TPM and reading the verdict must agree
with running the classifier on the rules directly. Across 250 random per-party rule forms the
bridge produced 0 verdict-flips against `classify_rules`. Under perfect coder agreement the CI
collapses to the degenerate point [phi, phi].

The second claim is calibration. A consensus account fixes a true Φ of 2.0. Twelve coders each
mark eight active-bit cells, matching the consensus with probability 0.80; a mis-coded cell
shifts the coder's Φ reading by a symmetric ±0.30. Over 500 such panels the bootstrap-t CI
brackets the consensus Φ on 94.4% of draws, inside the nominal 95% band [0.93, 0.97].

| arm                         | value    | criterion        | verdict   |
|-----------------------------|----------|------------------|-----------|
| H1 verdict-flips / 250      | 0        | = 0              | SUPPORTED |
| H1 alpha=1 CI degenerate    | True     | degenerate       | SUPPORTED |
| H2 coverage / 500 panels    | 0.9440   | in [0.93, 0.97]  | SUPPORTED |

## Scope

The rule sets and coder panels are synthetic, with known ground truth. The study validates the
machinery, not a measured coordination. The bridge reads coded accounts; whether a coded account
matches observed behaviour is a separate question this study does not address. Results are on
synthetic data.

## Run

    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
      python -m org_frontier.questions.q173_build_rule_to_phi.probe_build_rule_to_phi
