# What does — and doesn't — track integrated information? Four experiments against exact IIT‑4.0 Φ

*A synthesis of the four experiments in this repository.*

## Summary

Integrated Information Theory (IIT) defines a quantity, Φ, that is intractable to
compute on systems of any appreciable size. In practice researchers compute
*proxies* and *candidate measures* instead — and, as
[Barrett et al. (2026)](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/)
point out, these have rarely (if ever) been validated against the Φ they stand
in for, because exact Φ was out of reach. On systems small enough to compute
exact **IIT‑4.0** Φ with [PyPhi](https://github.com/wmayner/pyphi), we can do that
validation. Four experiments give a connected answer:

1. **Empirical proxies don't track Φ.** Lempel‑Ziv complexity, correlation, and
   the like are uninformative or *anti*‑correlated.
2. **Theoretically‑motivated candidate measures do better — but only
   moderately.** Whole‑minus‑sum Φ leads, and tracks Φ better the larger the
   system.
3. **Even exact scalar Φ is an impoverished summary.** It is nearly orthogonal to
   the cause‑effect *structure* it comes from.
4. **Yet integration is recoverable.** A model that *combines* cheap features
   predicts Φ well — and detects integrated systems with AUC 0.90.

The throughline: *no single cheap number is integrated information, but the
information needed to recover it is distributed across several cheap signals —
and the closer a measure's structure is to IIT's own "whole‑minus‑parts" move,
the more of that information it carries.*

## Setup common to all four

- **Systems:** random binary networks, `n ∈ {3,4}` nodes, with noisy Boolean‑gate
  dynamics, swept across connectivity density and noise to span a wide range of Φ.
- **Ground truth:** exact IIT‑4.0 Φ via `pyphi.new_big_phi`, summarized per
  network as the mean over reachable states (negative system Φ = reducible,
  clamped to 0). Experiment 3 instead works per `(network, state)`.
- Cross‑experiment numbers come from different ensembles/seeds, so comparisons
  *between* experiments are qualitative; the comparisons that carry weight
  (best‑single‑measure vs. alternative, *within* an experiment) are like‑for‑like.

## The four results

### 1 · Empirical proxies — [`proxy_audit/`](proxy_audit/)
270 networks. The strongest association of any empirical proxy with Φ is total
correlation at Spearman ρ = **−0.36** — the wrong sign. Lempel‑Ziv complexity is
near chance at even detecting Φ > 0 (AUC 0.57); the best Φ > 0 detector is a
trivial **edge count** (AUC 0.64). Relationships are non‑monotonic and *sign‑flip*
between detecting integration and grading it.

### 2 · Candidate Φ measures — [`candidate_audit/`](candidate_audit/)
Same 270 networks, now testing the Barrett–Seth / Mediano–Rosas candidate
measures. **Φ whole‑minus‑sum** leads (ρ = **0.47**, AUC **0.79**) and
*strengthens with system size* (ρ 0.41 → 0.55 from n=3 to n=4); integrated
synergy is second. Pure statistical‑dependence measures (total correlation,
time‑delayed MI) anti‑correlate. The measures that share IIT's whole‑minus‑parts
structure are the ones that track it — and they clearly beat the empirical
proxies (best AUC 0.79 vs 0.64).

### 3 · Is scalar Φ enough? — [`structure_suite/`](structure_suite/)
372 `(network, state)` points, extracting the full Φ‑structure (distinctions,
relations, mechanism‑order composition). Scalar Φ is **nearly orthogonal** to
every structural dimension (ρ = 0.07–0.21). Reducible systems (Φ = 0) still have
rich structure — *all* of them have ≥ 1 distinction (mean 2.8). The suite has ~3
independent axes — Φ, structural *size*, and *composition* — and Φ is only one.
Concrete support for replacing scalar Φ with a multi‑dimensional characterization.

### 4 · Can cheap features *together* predict Φ? — [`learned_surrogate/`](learned_surrogate/)
720 networks; a published exact‑IIT‑4.0 feature dataset. Out‑of‑fold (5‑fold CV),
a random forest combining the cheap features lifts Φ‑prediction from ρ = 0.32
(best single feature) to **0.54**, and detection of Φ > 0 from AUC 0.69 to
**0.90**. Φ_WMS carries most of the signal; the non‑linear model beats the linear
one. So integration, invisible to any single cheap measure, is substantially
recoverable from a combination — and *whether* a system is integrated is quite
predictable, even if *how much* remains moderate.

## What this adds up to

- For **empirical practice** (Experiment 1): the proxies routinely used as stand‑ins
  for integration do not, on these systems, track IIT Φ — a caution worth
  heeding, and a concrete instance of Barrett et al.'s critique.
- For **measure design** (Experiments 2, 4): structure matters. The whole‑minus‑sum
  family tracks Φ best and improves with size, and combining cheap features
  recovers much of Φ — pointing at cheap surrogates (e.g. the GNN direction of
  [Hosaka et al. 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335966),
  here grounded in exact 4.0 Φ and a reusable dataset).
- For **theory** (Experiment 3): scalar Φ is genuinely lossy relative to the
  Φ‑structure, supporting the move to a multi‑dimensional account.

## Limitations (shared)

These are small systems (`n ∈ {3,4}`) with a specific dynamics. The regime where
exact Φ is computable is exactly the regime that *can't* tell us about large or
real systems — generalization is the open problem, and the published dataset is
offered so others can probe it. All experiments use system‑level Φ summarized
over reachable states; per‑state or Φ‑structure‑level analyses may differ. See
each experiment's `FINDINGS.md` for measure‑specific caveats (e.g. the relation
congruence note in Experiment 3).

## Reproduce

Each experiment is a self‑contained package with a `run`/`build` + `analyze`
entry point; see the per‑experiment READMEs. All share the IIT‑4.0 PyPhi line
and a single ensemble generator.
