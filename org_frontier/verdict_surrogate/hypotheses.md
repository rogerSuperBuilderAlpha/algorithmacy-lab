# Pre-registration — a learned surrogate for the coordination verdict past the size ceiling

Committed before any result is computed, per the lab protocol. The claims below are fixed here so the
run cannot be steered to fit them. Dataset seeds and sample sizes are named in `build_dataset.py`;
the analysis scripts are `train.py`, `extrapolate.py`, and `boundary.py`.

## The gap this study fills

Two priors bracket an open cell and neither closes it.

- `proxy_bridge/` asked whether a *single cheap proxy* estimated from a coordination form's trajectory
  recovers the literacy/algorithmacy verdict that exact Φ gives. It does not: rank-AUC 0.56 (Φ_R) to
  0.63 (Φ_WMS). The named failure mode is the back-channel — a dyadic form with a direct worker–counterpart
  edge (`hierarchy_backchannel`, exact Φ = 0) draws a high proxy because a single dynamical measure reads
  statistical dependence as integration.
- `foundations/learned_surrogate/` asked whether a *learned combination* of cheap features predicts
  *generic* Φ on *random Boolean networks*, and whether it extrapolates in size. Detection of Φ > 0
  extrapolated from n ∈ {3,4} to an unseen n = 5 (AUC 0.84); magnitude prediction did not (ρ 0.54 → 0.33).
  It never touched the coordination verdict and never left random networks.

The unclaimed cell: a *learned* combination of cheap features, targeting the *coordination verdict*
(triadic vs dyadic over the MIP) on *coordination-structured forms*, tested for *size extrapolation*
toward the exact-Φ ceiling. The mechanism that makes it plausible: the back-channel that defeats a single
dynamical proxy is a *structural* fact, visible in the connectivity matrix without computing Φ. A model
given cheap structural features may learn the discount that exact Φ makes over the MIP, where a single
dynamical proxy cannot. And the verdict is a detection-style target, the kind of task that extrapolated
in size for generic Φ even when magnitude collapsed.

## The instrument and the ground truth

The verdict is exact IIT-4.0 Φ over the minimum-information partition, from
`org_frontier.classifier.classify_rules` (which wraps `foundations.proxy_audit.exact_phi`). A form is
**triadic** if Φ_MIP > 1e-9 in at least one reachable state, else **dyadic**. This is the same oracle the
rest of the lab uses; the surrogate is judged only against it.

**The feasible ceiling.** A timing probe (committed as `results/timing.csv`) measures exact-Φ cost per
form as n grows: on mediator chains it runs 0.06 s at n = 3, 0.38 s at n = 4, 3.0 s at n = 5, and 25 s at
n = 6, roughly ×8 per element, and random dense forms are slower because they reach more states. Population
studies are therefore feasible to n = 6, a sample is feasible at n = 7, and n = 8 admits only landmark
forms computed one at a time. The general OVERVIEW figure of a ~10–12-element exact ceiling holds for a
single hand-built form, not for a population. That gap is the point: a screen that runs where the
population oracle cannot is worth having even at n = 7.

## Design

**Training pool — n ∈ {3, 4, 5}.** Cheap to label exactly. Both classes must appear, so the pool mixes
random strict-mediation forms (which are triadic 9.4 % at n = 3, 2.3 % at n = 4, ~0 % at n = 5, per the
`multiparty` arm) with named triadic constructions that survive at every n: mediator chains, all-required
conjunctions (S′ = W ∧ C₁ ∧ … ∧ C_{k}), and layered mediation. Back-channel variants of triadic forms are
included so the training set contains the exact adversarial case that defeated the single proxy.

**Held-out size-extrapolation test — n ∈ {6, 7, 8}.** Never seen in training. n = 6 is a class-enriched
population; n = 7 is a smaller sample plus landmark triadic forms; n = 8 is landmark forms only. Every test
form is labeled by the same exact oracle.

**Features (all cheap; none uses exact Φ).**
- *Structural*, from the connectivity matrix (flip-test, O(n·2ⁿ), no Φ): party count, edge count, density,
  max in/out degree (hub-ness), hub fan-in (does the mediator read many parties), count of reciprocal
  non-hub edges (**the back-channel signal**), strict-star indicator, longest mediation chain.
- *Dynamical*, from `proxy_audit.all_proxies` and `candidate_audit.all_measures`: Φ_WMS, TDMI,
  total correlation, stochastic interaction, causal density, integrated synergy, LZ complexity,
  mean absolute correlation.

**Model.** Gradient-boosted / random-forest classifier on the union of features, five-fold
cross-validated within the training pool, compared against two baselines: (1) the best single dynamical
proxy at its best threshold — the `proxy_bridge` comparator; (2) a structural-only rule
(strict-mediation ∧ mediator-reads-both), the corpus arm's heuristic.

## Hypotheses

**H1 — rescue.** The learned classifier recovers the triadic/dyadic verdict within the n ∈ {3,4,5} pool
with cross-validated AUC materially above the single-proxy ceiling (proxy_bridge's 0.63) and above the
structural-only heuristic. *Pre-registered success line: AUC ≥ 0.85.* The gain comes specifically from
discounting the back-channel: on held-out back-channel forms the learned model calls dyadic where the best
single proxy calls triadic, at a rate reported explicitly.

**H2 — extrapolation (the payoff).** Trained only on n ≤ 5, the classifier recovers the verdict at
n ∈ {6,7,8} with AUC that degrades gracefully rather than collapsing to chance. *Pre-registered success
line: held-out AUC ≥ 0.75 at n = 6, and above chance (0.5, with a class-balanced test) at n = 7.* The
verdict is expected to extrapolate where magnitude did not, mirroring learned_surrogate's detection result
on the lab's own object. Because triads are rare at large n, the operative metric is recall on the rare
triadic class at a fixed screening budget (the fraction of true triads a top-k% screen catches), reported
alongside AUC.

**H3 — an honest boundary.** Residual errors concentrate in a nameable structural region rather than
scattering. *Pre-registered candidate region: near-threshold coupling and ambiguous back-channel forms
(a reciprocal non-hub edge present but weak in the dynamics).* The boundary is reported as the region
where the screen must defer to exact Φ.

**H4 — altitude guard.** Above the feasible oracle (here n > 8), no exact ground truth exists, so no
correctness claim is made. The surrogate is reported as a **screen that flags forms for exact Φ**, never a
replacement for it. Self-consistency across seeds is the only quantity reported past the oracle. Exact Φ
is not demoted: the contribution is a cheap pre-filter that widens the range the exact instrument can be
pointed at, not a substitute for the exact computation.

## What would falsify each

- H1 fails if the learned AUC does not clear 0.85, or clears it without beating the structural-only
  heuristic (then the dynamical features add nothing and the structural rule already suffices).
- H2 fails if held-out AUC at n = 6 falls below 0.75, or drops to chance at n = 7 — the verdict would then
  extrapolate no better than magnitude, and the screen would not survive the ceiling.
- H3 fails if errors are spread uniformly across the feature space with no nameable region — then the
  screen has no honest deferral rule.
- H4 is a discipline, not a testable claim; it fixes the altitude so a strong H2 cannot be overread into
  "Φ is unnecessary."
