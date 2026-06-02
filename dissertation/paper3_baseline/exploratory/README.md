# Exploratory — NOT part of the dissertation's claims

These scripts are retained for provenance and as a template for future empirical work. **They are
deliberately excluded from Paper 3 and from every claim the dissertation makes.**

## Why they are here and not in the paper

`anchor_chicago.py` and `robustness_anchor.py` were an attempt to "calibrate" the Φ scale against an
observed coordination outcome, using the City of Chicago Transportation Network Providers — Trips dataset
(rideshare pooling). The attempt was cut from the dissertation for one decisive reason:

> In the pooling model, Φ = k + 1 for a pool of *k* riders. So Φ is a linear function of party count, and
> the headline correlations (friction r ≈ +0.98, achievement share r ≈ −0.91 across the four pool sizes)
> only show that **bigger pools are harder and costlier — i.e. they validate the party-count axis of Φ,
> the one axis you do not need Φ (or any of this machinery) to see.** They do not validate the scale's
> novel content: that determination *structure* separates forms at a *fixed* party count. The anchor was,
> at best, a near-tautological check on the trivial axis, dressed up as calibration.

The dissertation was recast as a **formal-model** contribution (see the dissertation plan and Paper 2):
it characterizes what the model yields and is explicit that it does **not** validate the model against the
world. Keeping a weak, party-count-only "calibration" would contradict that honesty. So the anchor is
removed from the spine and demoted here.

## What they could still be good for

The right empirical test of the scale's *structure* axis needs a dataset that **varies determination
structure at a fixed party count** — not pool size. These scripts are a worked template for how an
outcome-anchor would be built (bounded Socrata queries, per-form aggregation, a robustness battery) once
such a dataset is found. That search is named as future work, not done here.

## Files

- `anchor_chicago.py` — per-pool-size Φ vs friction / achievement on Chicago TNP Trips (resource `m6dm-c72p`).
- `robustness_anchor.py` — temporal split, within-stratum (Simpson's) check, alternative aggregations,
  trip-level effect size on the full pooling-era sample.

Reproducible against the public dataset, but **do not cite their numbers anywhere in the dissertation.**
