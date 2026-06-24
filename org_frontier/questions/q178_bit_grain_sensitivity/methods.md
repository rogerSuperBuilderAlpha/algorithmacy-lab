# q178 — methods

## The graded-to-binary calibration

Each synthetic account fixes a graded counterpart-action level `g` in `{0, 1, 2}` over labels
`(W, S, C)` = (Worker, System, Counterpart). A coder reads the account with a threshold `t` in
`{1, 2}` and collapses the grade to a bit:

    b = 1 if g >= t else 0

The bit drives the system rule. `b = 1` wires the counterpart C into the loop and gives the
worker-system-counterpart triad `[x1, x0 & x2, x1]`. `b = 0` drops C and gives the dyad
`[x1, x0, x1]`. `rule_to_phi` from the q173 bridge reads each collapsed rule set to its exact
IIT-4.0 Φ verdict. Φ is not reimplemented.

The grade-by-threshold map fixes which accounts are threshold-sensitive:

- `g = 0`: off at both cuts -> always dyadic.
- `g = 1`: on at `t = 1`, off at `t = 2` -> verdict flips with the cut.
- `g = 2`: on at both cuts -> always triadic.

## H1: verdict-flip rate

A seeded panel of 200 accounts draws graded levels uniformly over `{0, 1, 2}` with
`numpy.random.default_rng(0)`. For each grade the probe reads the verdict at both thresholds and
records whether it flips. The flip rate is the share of panel accounts whose grade is
threshold-sensitive. H1 is supported when the flip rate exceeds 0.20; the null holds below 0.05.

## H2: CI width under threshold disagreement

One threshold-sensitive account (`g = 1`) is read by two coder panels of eight coders. Each coder
carries a small seeded reading jitter (`sd = 0.02`) on the Φ read, drawn from the same generator.

- Split panel: four coders cut at `t = 1` (reading Φ ≈ 2.0), four cut at `t = 2` (Φ ≈ 0.0). The
  active-bit coding matrix records the split, `[1,1,1,1,0,0,0,0]`.
- Same-threshold panel: all eight coders cut at `t = 1` (Φ ≈ 2.0). The coding matrix is all ones.

`phi_ci` from the q173 bridge propagates each panel to a bootstrap-t Φ confidence interval and
reports its Krippendorff alpha. The width ratio is `split_width / same_width`. H2 is supported when
the ratio exceeds 2; the null holds at or below 1.2.

## Controls

**Instrument control.** The faithful triad `[x1, x0 & x2, x1]` with labels `(W, S, C)` reads
`triadic` with max Φ_MIP = 2.0. The probe aborts on failure.

**Threshold-invariance control.** Monotone accounts (`g` in `{0, 2}`) must read the same verdict at
both thresholds. The probe checks each and reports PASS.

**Single-cut CI control.** The same-threshold panel uses one cut for every coder, so its CI width
is the ordinary single-cut (reading-noise) baseline against which the split panel is compared.

## Determinism

The probe seeds `numpy.random.default_rng(0)` for the account panel and the jitter, and fixed
generators (`default_rng(1)`, `default_rng(2)`) for the two bootstrap CIs. Output is byte-identical
on re-run; confirmed across three runs.

## Scope

Accounts are synthetic, coder-supplied grade levels and rule sets, not measured worker states. The
empirical arms are on synthetic data. The gap between a coded grade and an observed action is not
closed here.
