# What does — and doesn't — track integrated information? Six experiments against exact IIT‑4.0 Φ

*A synthesis of the six experiments in this repository.*

## Summary

Integrated Information Theory (IIT) defines a quantity, Φ, that is intractable to
compute on systems of any appreciable size. In practice researchers compute
*proxies* and *candidate measures* instead — and, as
[Barrett et al. (2026)](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/)
point out, these have rarely (if ever) been validated against the Φ they stand
in for, because exact Φ was out of reach. On systems small enough to compute
exact **IIT‑4.0** Φ with [PyPhi](https://github.com/wmayner/pyphi), we can do that
validation. Six experiments give a connected answer:

1. **Empirical proxies don't track Φ.** Lempel‑Ziv complexity, correlation, and
   the like are uninformative or *anti*‑correlated.
2. **Theoretically‑motivated candidate measures do better — but only
   moderately.** Whole‑minus‑sum Φ leads, and tracks Φ better the larger the
   system.
3. **Even exact scalar Φ is an impoverished summary.** It is nearly orthogonal to
   the cause‑effect *structure* it comes from.
4. **Yet integration is recoverable.** A model that *combines* cheap features
   predicts Φ well — and detects integrated systems with AUC 0.90, with
   detection (though not magnitude) still holding up on larger unseen systems.
5. **A neighbouring framework diverges too.** Hoel's causal emergence is nearly
   orthogonal to Φ; the most integrated systems show no emergence at all.
6. **And it's worse on data than in principle.** Estimating the best measure the
   realistic way — ΦID on a finite time series — roughly halves how well it
   tracks Φ.

The throughline: *no single cheap number is integrated information, but the
information needed to recover it is distributed across several cheap signals —
and the closer a measure's structure is to IIT's own "whole‑minus‑parts" move,
the more of that information it carries.*

## Setup common to all six

- **Systems:** random binary networks, `n ∈ {3,4}` nodes, with noisy Boolean‑gate
  dynamics, swept across connectivity density and noise to span a wide range of Φ.
- **Ground truth:** exact IIT‑4.0 Φ via `pyphi.new_big_phi`, summarized per
  network as the mean over reachable states (negative system Φ = reducible,
  clamped to 0). Experiment 3 instead works per `(network, state)`.
- Cross‑experiment numbers come from different ensembles/seeds, so comparisons
  *between* experiments are qualitative; the comparisons that carry weight
  (best‑single‑measure vs. alternative, *within* an experiment) are like‑for‑like.

## The six results

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

Crucially, we also test **size extrapolation** — the make‑or‑break property for a
cheap surrogate. Trained on `n ∈ {3,4}` and applied to a fresh **unseen `n=5`**
set, *detection* holds up (AUC 0.84, vs 0.90 in‑distribution) while *magnitude*
prediction degrades (ρ 0.54 → 0.33). Screening for integration may transfer
across scales; estimating its amount does not — yet.

### 5 · Causal emergence vs Φ — [`emergence_vs_phi/`](emergence_vs_phi/)
Beyond proxies and candidate measures, we compare a *neighbouring framework* —
Hoel's effective information and causal emergence — against Φ on 180 n=3 systems,
with the emergence search done exactly (all state coarse‑grainings). Causal
emergence is nearly orthogonal to Φ (Spearman 0.02), and the most integrated
systems show **no** emergence: emergence rewards degeneracy (a coarse‑graining
recovers determinism), while Φ rewards irreducibility, so they pick out different
systems. Effective information — Φ's precursor — does track Φ, but only *among
already‑integrated systems* (ρ 0.77), not whether integration occurs.

### 6 · ΦID-based Φ from data vs exact Φ — [`phiid_vs_phi/`](phiid_vs_phi/)
The candidate audit computed measures exactly from the TPM; on real data they are
estimated from finite time series via ΦID. Computing the revised Φ_R (with CCS
redundancy — MMI assigns spurious synergy to independent variables) from
trajectories via the `phyid` package, the tracking of exact Φ roughly halves: on
the same networks, exact Φ_WMS gives ρ = 0.28 (AUC 0.67) while the data-style
Φ_R gives ρ = 0.12 (AUC 0.56). Exact and estimated agree at ρ = 0.64 — the same
quantity, degraded by finite-sample estimation and coarse-graining. A concrete
caution for inferring integration from data-side ΦID.

### Philosophical companion — [`consciousness_range/`](consciousness_range/)
The six experiments ask *what tracks Φ*. A seventh flips the question: *assume IIT
is true* (the Φ-structure is the experience) and build a bestiary of minds. Three
systems with identical Φ = 0.415 have structures spanning 59–32 764 relations
(555×); across the bestiary Φ and structural richness *anti*-correlate; and the
composition differs in kind. On IIT's own terms, scalar Φ radically
underdetermines the mind — a concrete, by-example case for the field's move from
a single number to the full Φ-structure.

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
