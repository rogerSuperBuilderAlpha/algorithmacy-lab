# q173 — methods

## The bridge module

`org_frontier/field/rule_to_phi.py` exposes:

    rule_to_phi(rules, labels) -> {structure, competence, max_phi, n_irreducible}
    krippendorff_alpha(codings) -> float
    phi_ci(coder_phis, coder_codings=None, n_boot, ci, rng) -> {phi_point, ci_low, ci_high, ...}
    phi_ci_from_rules(coder_rule_sets, labels, coder_codings=None, ...) -> same dict

`rule_to_phi` encodes per-party Boolean determination rules into a deterministic state-by-node
TPM via the classifier's `tpm_from_rules`, runs the exact IIT-4.0 Φ classifier over the MIP, and
returns the verdict. Φ is not reimplemented; the module wraps `org_frontier.classifier` and
`org_frontier.probes.lib`.

`krippendorff_alpha` computes nominal Krippendorff agreement on a (n_coders, n_units) integer
coding matrix: observed pairwise disagreement over expected disagreement from the pooled label
distribution. It returns 1.0 for perfect agreement.

`phi_ci` takes a panel of per-coder Φ readings and returns a studentized bootstrap-t interval.
It resamples coders with replacement, studentizes each resample by its own standard error, and
inverts the bootstrap distribution of the t-statistic. The bootstrap-t is used because the plain
percentile bootstrap under-covers at small coder counts. When the coder readings are identical
(or one coder, or zero spread), the interval collapses to the degenerate point [phi, phi], and
the reported alpha is 1.0.

## Controls

**Instrument controls.** Two canonical forms. The decoupled rule set `[x0, x1, x2]` (each party
copies itself, no cross-party coupling) reads `dyadic`. The faithful worker-system-counterpart
triad `[x1, x0&x2, x1]` with labels `(W, S, C)` reads `triadic` with max Φ_MIP = 2.0. The probe
aborts on failure.

**Agreement control.** `phi_ci_from_rules([TRIAD, TRIAD, TRIAD])`: three identical coder readings
give alpha = 1 and a degenerate CI [2.0, 2.0].

## H1 — verdict reproducibility

The probe samples 250 random per-party rule forms (each party's rule is a random truth table over
the three current bits, frozen by closure). For each form it compares `rule_to_phi`'s structure
to `classify_rules`'s structure and counts disagreements. H1 is supported iff verdict-flips = 0
and the agreement control's CI is degenerate.

## H2 — CI coverage

A consensus account fixes a true Φ (the faithful triad, consensus Φ = 2.0). Coding which states
or bits are active is graded: each coder marks 8 active-bit cells, matching the consensus cell by
cell with probability 0.80. A mis-coded cell pushes the coder's Φ reading by a symmetric ±0.30,
so each reading is mean-zero coding noise around the consensus Φ. Each panel has 12 coders. The
active-bit matrix drives the Krippendorff alpha; the panel runs through `phi_ci`. Coverage is the
fraction of 500 panels whose CI brackets 2.0. H2 is supported iff coverage is in [0.93, 0.97];
the [0.90, 0.98] band is the non-miscalibration tolerance.

## Determinism

The probe seeds `numpy.random.default_rng` with fixed seeds (0 for rule sampling, 2 for coder
draws, 3 for the bootstrap). Output is byte-identical across re-runs; this was confirmed across
three runs.

## Scope

The rule sets and coder panels are synthetic. The study validates the bridge machinery on known
ground truth. No real coordination is measured, and the gap between coded accounts and observed
behaviour is not closed here. Later field studies import this module.
