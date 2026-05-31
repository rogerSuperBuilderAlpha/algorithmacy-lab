# Maximum-caliber information is a complexity measure, not an integration measure: a direct test of ψ against exact IIT-4.0 Φ

**Roger Hunt**

*Preprint draft, May 2026. Code, data, figures, and the literature corpus:
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`psi_vs_phi/`).
Citations are author–year and resolve to `literature/references.bib`. This responds to Kearney (2026),
posted shortly before this work.*

---

## Abstract

The Free Energy Principle (FEP) and Integrated Information Theory (IIT) are two of the most ambitious
mathematical frameworks for, respectively, the dynamics of self-organising systems and the structure
of conscious experience. A rigorous bridge between them would be a significant result, and Kearney
(2026) proposes one. Defining an information quantity ψ as the deviation of a system's realised
dynamics from a constrained maximum-caliber (MaxCal) path ensemble, he re-derives IIT 3.0's
cause–effect repertoires from this principle and relates ψ to prediction error and the FEP. For a
stationary ergodic Markov chain the proposal reduces to a closed-form scalar, ψ(π) = log₂κ − H(π) −
h(π). However, the proposal is never directly compared against integrated information Φ, the quantity
the bridge is meant to reach, and the paper explicitly calls for that test. We perform it.

On an ensemble of small discrete networks where exact IIT-4.0 Φ is computable without approximation, we
implement ψ (validated against the paper's own worked controls to machine precision) and ask whether
it tracks exact Φ. It does not. Across 181 ergodic networks ψ is essentially uncorrelated with Φ
(Spearman ρ = 0.085, 95% CI [−0.08, +0.24]; detection AUC = 0.52), and the result is robust to how Φ
is aggregated, stable across five random seeds, and absent within every density, noise, and gate-type
stratum. We then test the objection that ψ lacks a partition step by constructing one: a MaxCal
integration measure ϕ_ψ, built on IIT's minimum-information-partition logic. It does not help. ϕ_ψ is
weakly anti-correlated with Φ (ρ = −0.28), whereas the same partition operation applied to a mutual
information (whole-minus-sum Φ) tracks exact Φ at ρ = 0.58 on the same networks. We also address the
objection that ψ might track the IIT 3.0 repertoires Kearney re-derives: ψ misses 3.0 Φ as badly as
4.0 Φ (ρ = 0.11 vs 0.10), while 3.0 and 4.0 Φ agree with each other (ρ = 0.86).

Two hand-built minimal systems at matched size (n = 3) make the dissociation concrete: a segregated,
biased system scores ψ = 2.62 with Φ = 0, while an integrated parity-coupled system scores ψ = 0.43
with Φ = 1.38, so ψ ranks them in the wrong order. We argue that this reflects a structural property of
ψ rather than an artefact of the chosen reduction. ψ is the divergence of one distribution from a
reference derived from the same dynamics, an order/disorder complexity quantity, and the analysis of
the leaderboard suggests that tracking Φ requires a whole-minus-parts comparison of cause-effect
structure across a cut, which ψ does not perform. The MaxCal–IIT–FEP bridge holds at the level at which
it is proven, a system-level duality between free energy and constrained entropy, but it does not
descend to a scalar ψ ≈ Φ relationship. The result leaves Kearney's separate repertoire-level
derivation untouched.

---

## 1. Introduction

Two research programmes dominate the mathematical study of mind. Integrated Information Theory (IIT)
identifies a conscious experience with the irreducible cause–effect structure a physical substrate
specifies for itself, and quantifies the amount of consciousness by integrated information, Φ (Tononi
2004; Oizumi, Albantakis & Tononi 2014; Albantakis et al. 2023). The Free Energy Principle (FEP)
holds that any system individuated from its environment by a Markov blanket can be described as
minimising variational free energy, a tractable upper bound on the surprise of its sensory states
(Friston 2010, 2019). The two start from opposite ends. IIT is intrinsic, synchronic, and concerned
with structure; the FEP is extrinsic, dynamical, and concerned with persistence. Whether they are two
views of one underlying fact is a long-standing conjecture, and several authors have pursued it
(Safron 2020; Lundbak Olesen et al. 2023; Mayama et al. 2025). Until recently the connection was
conceptual or correlational rather than a mapping one could compute with.

Kearney (2026) sets out to supply the mapping, using maximum caliber (MaxCal), the trajectory-space
generalisation of the maximum-entropy principle (Pressé et al. 2013; Dixit et al. 2018). Among all
distributions over a system's possible paths consistent with measured dynamical constraints, MaxCal
selects the one of greatest path entropy, the least-committal ensemble. Kearney defines an information
quantity ψ as the deviation, formally a Kullback–Leibler divergence, of a system's realised dynamics
from this reference. He then makes two distinct moves. At the level of construction, he re-derives IIT
3.0's cause and effect repertoires (the conditional distributions IIT uses to score the difference a
mechanism makes) from this single constrained-maximum-entropy principle. At the level of quantity, he
shows that ψ coincides with prediction error in appropriate asymptotic limits, which is what ties it
to the FEP. For a stationary, ergodic Markov chain the second move collapses to a cheap closed-form
scalar,

> ψ(π) = log₂κ − H(π) − h(π),

where H(π) is the entropy of the chain's stationary distribution, h(π) is its entropy rate, and κ is
a system-specific normaliser defined in §2.4.

The construction is elegant and potentially useful, but it has a self-acknowledged gap. ψ is never
compared against Φ, the integrated information it is meant to bridge toward. The paper is candid about
this: "the explanatory power of our proposal here remains unconfirmed. Experimental or theoretical
work must be conducted to … connect the metrics observed here to those in IIT." The bridge is
asserted but empirically unverified. This paper provides that verification.

We are in an unusually good position to do so, because we hold an instrument most consciousness
research lacks: an exact IIT-4.0 Φ oracle. Φ has never been computed for a brain or for any system of
biological scale; the computation is super-exponential, and what is reported on empirical data are
proxies whose relationship to canonical Φ is largely unverified (Barrett et al. 2026). For small
discrete systems, however, Φ is computable exactly using PyPhi's implementation of the IIT-4.0
formalism. This is the regime in which a candidate bridge quantity can be held against ground truth. A
companion line of work in the same repository uses this strategy to audit empirical proxies and
candidate integration measures; here we apply the same apparatus to ψ.

Our contribution is organised around four objections such a test must answer. First, the direct test:
we implement ψ exactly, validate it against the paper's own worked cases, and
correlate it with exact IIT-4.0 Φ across a 270-network ensemble, with robustness checks on Φ
aggregation, five seeds, and within-regime structure. Second, the partition objection: because the
bare scalar might be a degenerate reduction of the integration structure Kearney sketches at the
repertoire level, we build that structure as a partitioned MaxCal measure ϕ_ψ and test it on the same
footing as IIT's minimum information partition. Third, the version objection: because Kearney
re-derives IIT 3.0 while we primarily validate against 4.0, we compute 3.0 Φ where it is stable and
compare. Fourth, the mechanism: we exhibit two minimal systems on which ψ and Φ dissociate in both
directions, so that the vanishing correlation can be seen rather than only inferred from a statistic.

The thesis we defend is that the null result is structural. The reason ψ does not track Φ is visible
in the algebra of ψ before any network is generated, and the same reason limits how far the
MaxCal–FEP duality can be extended as a claim about consciousness. We state and argue that thesis in
§5.

## 2. Background

### 2.1 What Φ measures: partition and exclusion

Two operations are constitutive of Φ and absent from ψ, so we set them out first.

IIT begins from a substrate: a set of interacting units whose joint dynamics are given by a transition
probability matrix (TPM), specifying for each current state the distribution over next states. From
the TPM, IIT constructs, for every candidate subset of units (every mechanism) in a given state, a
cause repertoire and an effect repertoire, the distributions over states that could have produced and
that will be produced by the mechanism's current state. A mechanism contributes to consciousness only
if these repertoires are irreducible: if the mechanism can be partitioned into independent parts whose
repertoires reconstruct the whole's, it specifies nothing beyond its parts and is discarded. This is
the partition operation, and the degree of irreducibility across the partition that costs least to
make, the minimum information partition (MIP), is the mechanism's integrated information.

The same logic recurs at the system level. The whole substrate's cause–effect structure is scored
against the structure that survives cutting the system across its weakest bipartition, and system-level
Φ is the irreducibility of the whole across its MIP. A second operation also applies: exclusion. Among
overlapping candidate substrates, only the one of maximal integrated information, the maximal complex,
exists as an entity; the others are excluded. Φ is therefore not a property of a fixed node set but
the result of a maximisation over candidate substrates, each evaluated by an
irreducibility-across-a-partition computation.

The point to carry forward is that Φ is, by definition, a whole-minus-its-best-cut quantity selected
by a maximisation. A measure that contains neither a partition nor a maximisation is not a small or
noisy version of Φ; it measures something else.

IIT 3.0 (Oizumi et al. 2014) scored the difference a mechanism makes using the earth-mover's distance
(EMD) between repertoires and an unconstrained baseline. IIT 4.0 (Albantakis et al. 2023) replaced EMD
with a uniquely determined intrinsic difference (ID) measure and unfolded the system into a structure
of distinctions and relations whose total is the canonical Φ. The difference between 3.0 and 4.0 is
real, but for the present question it does not matter, because both retain the partition-and-exclusion
skeleton, and that skeleton is what ψ lacks. We show this empirically in §4.4.

### 2.2 The measurement problem

Because canonical Φ is uncomputable beyond toy systems, empirical consciousness science runs on
proxies: perturbational complexity, and candidate integration measures from the Mediano–Seth–Barrett
lineage (Mediano, Seth & Barrett 2019). Barrett et al. (2026) argue that these proxies must be
validated against the thing they proxy rather than assumed to track it, and note that Φ is arguably
not well-defined for continuous physical systems and has not been computed on any. The strong-versus-
weak IIT distinction (Mediano et al. 2022) and the unfolding argument (Doerig et al. 2019) further
complicate what validation should mean. Our stance is operational: where exact Φ is available, as it
is on small discrete networks, a candidate that claims a relationship to Φ should demonstrate it
there, or the claim remains unsupported. ψ makes such a claim, and we test it where it can be tested.

### 2.3 MaxCal, the path ensemble, and the proven duality

Maximum entropy selects, among distributions consistent with measured averages, the one of greatest
entropy. Maximum caliber lifts this from states to trajectories: among distributions over a system's
paths consistent with measured dynamical constraints, it selects the one of greatest path entropy
(Pressé et al. 2013; Dixit et al. 2018). The selected ensemble is a reference, the dynamics one would
predict knowing only the constraints. Kearney's ψ measures how far a system's actual dynamics depart
from this reference, which is why it takes the form of a Kullback–Leibler divergence.

The link to the FEP runs through a duality. Ramstead et al. (2023), developing Bayesian mechanics,
prove a correspondence, asymptotically and under non-equilibrium-steady-state and Markov-blanket
assumptions, between minimising variational free energy and a constrained maximum-entropy description
of a system's steady state. This is the result that makes a MaxCal–FEP bridge coherent. One feature
of it matters for §5: the proven duality is a statement about the whole system's steady-state
distribution, relating the system's free energy to its constrained entropy. It contains no partition,
no exclusion, and no maximisation over candidate substrates. The absence is not a gap to be filled
later; it is what the proof is about. The duality is a system-level fact, whereas Φ is a fact about
how the system decomposes.

### 2.4 The definition of ψ

The argument depends on what is and is not inside ψ, so we define it completely. Let the system be a
homogeneous Markov chain on N states with transition matrix P, where P(x, ·) is the distribution over
next states given current state x. All entropies are in bits.

The conditional entropy of the dynamics out of state x is Hc(x) = H(P(x, ·)), the unpredictability of
the next step given that the system is in x. The per-state perplexity PP(x) = 2^{Hc(x)} is the
effective number of next-states reachable from x. The MaxCal normaliser κ = Σ_x PP(x) sums these over
all states; it is system-specific, depending on the full transition structure rather than only on N.
The MaxCal input marginal µ(x) = PP(x)/κ is the reference distribution over states implied by the
maximum-caliber ensemble. The chain's stationary distribution π solves π = πP, and the entropy rate
h(π) = Σ_x π(x) Hc(x) is the long-run per-step uncertainty under π. The maximum-caliber information is

> ψ(π) = log₂κ − H(π) − h(π) = D_KL(π ‖ µ),   (Kearney eq. 5.10)

the right-hand equality being an algebraic identity, which we verify numerically below. The KL form
shows three things. First, ψ ≥ 0, with equality iff π = µ, that is, iff the system's realised occupancy
coincides with its MaxCal reference. Second, ψ is a property of one distribution (π) measured against
a fixed reference (µ) derived from the same dynamics. Third, ψ is therefore a self-divergence: it asks
how far a system is from its own least-committal description, a question about order, bias, and
predictability. It is a complexity quantity.

A small worked example fixes the meaning of the parts. Take a two-state chain that, from either
state, stays put with probability 0.9 and switches with probability 0.1, so the rows of P are (0.9,
0.1) from state 0 and (0.1, 0.9) from state 1. Each row has Hc(x) = H(0.9, 0.1) ≈ 0.469 bits, so the
per-state perplexity is PP(x) = 2^{0.469} ≈ 1.384 and κ = PP(0) + PP(1) ≈ 2.768, giving log₂κ ≈
1.469. The two perplexities are equal, so the MaxCal marginal is µ = (0.5, 0.5). The chain is
symmetric, so its stationary distribution is also π = (0.5, 0.5), with H(π) = 1 bit and entropy rate
h(π) ≈ 0.469 bits. Then ψ = log₂κ − H(π) − h(π) ≈ 1.469 − 1 − 0.469 = 0, matching D_KL(π ‖ µ) = 0
because π = µ. Now break the symmetry: if state 0 is sticky (row (0.95, 0.05)) while state 1 leaks
(row (0.5, 0.5)), the stationary distribution shifts toward state 0 (π ≈ (0.91, 0.09)), π departs
from µ, and ψ rises to ≈ 0.90. ψ thus measures how far a chain's long-run occupancy is pulled away
from the spread its own branching structure would imply. It registers bias in where the system spends
its time, not how its parts depend on one another.

The companion quantity i(π) = H(π) − h(π) is the mutual information between consecutive states,
I(X_{t−1}; X_t). One might expect any integration signal to appear here; we test that in §4.2.

Nowhere in ψ is there a partition of the system into parts, a comparison of the whole to its parts, or
a maximisation over candidate substrates. ψ never cuts the system. §5 argues that this absence is the
whole story.

### 2.5 Prior IIT–FEP unifications

Safron's Integrated World Modelling Theory (2020) is a conceptual synthesis rather than a mapping.
Lundbak Olesen et al. (2023) report empirically that Φ fluctuates with surprisal in a simulated agent,
an encouraging correlation but not a derivation. Mayama et al. (2025) describe a hill-shaped Φ
trajectory in living neuronal cultures as they adapt; their Φ is itself a proxy, and the relationship
they report is over learning time, a point we return to in §5.5. None of these computes a candidate
bridge quantity against exact Φ. Kearney's derivation is the most rigorous attempt so far to connect
the formalisms, which is why it warrants a direct test.

## 3. Methods

### 3.1 Design and pre-registered hypotheses

This is a within-ensemble measure-validation study. For each network we compute exact IIT-4.0 Φ
(ground truth) and the candidate ψ and its variants, then quantify how strongly ψ tracks Φ. Two
hypotheses were fixed before any ψ–Φ association was computed. H1: ψ tracks exact Φ, with a positive
monotonic association comparable to that of genuine integration measures. H0: ψ tracks order/disorder
complexity and is at best weakly and unreliably related to Φ. We regard H0 as the favoured outcome for
the structural reasons of §2.4, but the design allows H1 to win, since the same apparatus detects a
strong Φ signal when one is present (§3.7, §4.7); a null for ψ is therefore informative rather than a
failure of the test.

### 3.2 The system ensemble

Each network has n binary units. Every unit updates as a possibly-noisy Boolean function of the units
feeding into it, drawn uniformly from five gate types chosen to span the integration range: OR and AND
(low integration), COPY (near-trivial), MAJORITY (intermediate), and PARITY (the maximally integrative
case, since a node's next value depends jointly and irreducibly on all its inputs). For each network we draw
a connectivity matrix by including each directed edge independently with probability equal to the
density, guaranteeing every node at least one input; assign each node a random gate; and build the
state-by-node TPM, mixing each node's deterministic output toward 0.5 by the noise level (noise 0 gives
deterministic dynamics).

The ensemble sweeps a grid: densities ∈ {0.3, 0.5, 0.8}, noise ∈ {0.0, 0.05, 0.2}, sizes n ∈ {3, 4},
with 15 networks per (size, density, noise) cell, giving 2 × 3 × 3 × 15 = 270 networks per seed. The
size cap n ≤ 4 is dictated by the exact-Φ oracle, which is feasible at n = 3,4 and quickly becomes
infeasible beyond. We use five independent seeds (1–5). The generator is the shared
`proxy_audit.networks.generate_ensemble`, identical to the one used to audit the other candidate
measures, so ψ is tested on the same systems they were. The ensemble is a particular slice of
dynamical-systems space, small, binary, Boolean-gated. It is also the only slice on which the
comparison can be made against exact ground truth rather than a proxy, and §5.6 argues the structural
conclusion does not depend on the slice.

### 3.3 The exact-Φ oracle and three aggregations

Φ was computed with PyPhi's IIT-4.0 system-irreducibility analysis (`pyphi.new_big_phi.sia`) on the
whole substrate in a given state. Φ is state-dependent, so to obtain one number per network we
aggregate over the network's reachable states (states with at least one predecessor under the
dynamics, which PyPhi will analyse). A negative system Φ denotes a reducible system in that state,
which carries zero integrated information, so we clamp negatives to 0, matching IIT's treatment of
complexes. Because the choice of aggregation could in principle drive the result, we compute and
report three: the uniform mean over reachable states (the primary value), the maximum, and the
stationary-π-weighted mean. The π-weighted mean is the most appropriate comparator for a stationary
quantity such as ψ, since it weights each state by how often the system occupies it. For n ∈ {3,4}
every reachable state is evaluated (≤16), so the three aggregations come from the same exact per-state
Φ values.

### 3.4 The ψ implementation and the ergodicity screen

ψ is implemented directly from §2.4 (`psi_vs_phi/psi.py`). The state-by-state TPM is obtained from the
state-by-node TPM via PyPhi's converter, and the stationary distribution by power iteration. ψ is
defined only for ergodic, homogeneous chains, so each chain is screened by a practical test: power
iteration from a uniform start and from a one-hot start must converge to the same stationary
distribution. This catches reducible chains and gross periodicity, though it is not a complete
aperiodicity certificate, and we report it as a practical filter. The primary analysis is restricted to
the ergodic subset; non-ergodic networks are flagged, excluded, and counted.

### 3.5 A partitioned MaxCal integration measure (ϕ_ψ)

The objection that the bare scalar ψ is a degenerate reduction, and that the integration content of
Kearney's proposal lives in the repertoire-level construction with its partition step, is reasonable.
We therefore construct the partitioned analogue on the same footing as IIT. For a bipartition of the
nodes into parts A and B, we form the marginal sub-chain on A by projecting the stationary-weighted
joint distribution of consecutive states onto A's coordinates and row-normalising, the same
marginalisation the whole-minus-sum candidate measure uses, so that ϕ_ψ and Φ_WMS treat the partition
identically and differ only in the underlying scalar. We then define

> ϕ_ψ = ψ(whole) − min over bipartitions (A,B) of [ ψ(A) + ψ(B) ],

minimising the per-part-normalised difference and reporting the un-normalised value at that minimum
information bipartition, mirroring `phi_wms`. The construction is principled: ψ is exactly additive
over independent subsystems (if A and B evolve independently, κ, H, and h factorise and ψ(whole) =
ψ(A) + ψ(B), so ϕ_ψ = 0 on a fully separable system, which we confirm as a control), so ϕ_ψ measures
the irreducibility of the system's MaxCal deviation across its weakest cut, the operation ψ alone omits
and that Φ is built on. This is an operationalisation of the partition logic Kearney sketches at the
repertoire level (his §6.4), using the same marginalisation as Φ_WMS so that the two measures differ
only in the scalar being partitioned. If giving ψ a partition step makes it track Φ, ϕ_ψ will show it.
§4.3 reports the outcome.

### 3.6 The IIT-3.0 comparator

Because Kearney re-derives IIT 3.0 repertoires, we computed whole-system IIT-3.0 Φ on the same
networks (`psi_vs_phi/exact_phi3.py`), configured for 3.0 (IIT_VERSION 3.0, DIRECTED_BI system
partitions, EMD repertoire distance), aggregated as for 4.0. Two practical notes. First, the 3.0
concept-evaluation path routes through a parallel map-reduce requiring an optional dependency we do not
install, so we force sequential evaluation with a thin patch; results are identical, only slower.
Second, the EMD code in this 4.0-oriented checkout raises a histogram-shape error on some n = 4
repertoires, so the 3.0 comparator is computed on the n = 3 subset only, where every evaluation is
stable (0 errors across 90 ergodic networks). This is a limitation of the present run, and §4.4 shows
the n = 3 evidence settles the question on its own.

### 3.7 Comparison measures

To establish that the apparatus can detect integration, we rank ψ and ϕ_ψ against six practical
measures computed on the identical ergodic networks (`candidate_audit`): whole-minus-sum Φ (Φ_WMS;
Balduzzi & Tononi 2008; Barrett & Seth 2011), integrated synergy (a net co-information measure in the
sense of Williams & Beer 2010 and the ΦID lineage of Mediano, Seth & Barrett 2019, which avoids the
spurious-synergy pathology of MMI-based decompositions), stochastic interaction (Ay 2015), causal
density (Seth 2008), total correlation, and time-delayed mutual information. Φ_WMS is the
key positive control: it is a partition-based whole-minus-parts measure, and if the test is alive it
should track Φ.

### 3.8 Validation controls

Following the practice that has caught measure-implementation errors in the companion studies, ψ was
validated against Kearney's predictions before any ψ–Φ number was computed: ψ = 0 for circulant and
uniform-row chains (π = µ); ψ = log₂N − H(π) for deterministic permutations; ψ ≥ 0 across random
chains; and exact agreement of the entropy form and the KL form. ϕ_ψ was validated as ≈ 0 for a
separable two-node system, with the additivity identity confirmed.

### 3.9 Statistics

For each measure against Φ we report Spearman ρ (the primary statistic given the skewed Φ
distribution), Pearson r, and the area under the ROC curve for detecting Φ > 0; bootstrap 95%
confidence intervals (2000 resamples); exact Spearman p-values; the association restricted to Φ > 0;
per-size, per-(density,noise)-cell, and per-gate breakdowns to check for a pooled cancellation; and a
five-seed pooling. As a sensitivity statement we report the minimum detectable |ρ| at the analysis
sample size, the correlation whose Fisher-z 95% interval just excludes zero.

## 4. Results

### 4.1 Implementation verification

All controls passed. ψ = 0 for circulant and uniform-row chains; ψ = log₂N − H(π) for deterministic
permutations; ψ ≥ 0 across 200 random chains; and the entropy form and KL form agreed to a maximum
difference of 1.3 × 10⁻¹⁵. ψ is therefore computed exactly and as defined, and nothing below is an
implementation artefact.

### 4.2 ψ does not track exact IIT-4.0 Φ

Of the 270 seed-1 networks, 181 were ergodic (the primary analysis set), of which 55 had Φ > 0; Φ
ranged from 0 to 1.588 bits. Across the ergodic set, ψ is essentially uncorrelated with exact Φ:
Spearman ρ = 0.085 (95% bootstrap CI [−0.08, +0.24], including zero; exact p = 0.25), Pearson r =
−0.116, and the detection AUC for Φ > 0 is 0.524, at chance. Restricting to integrated systems (Φ > 0)
gives ρ = −0.318: among systems that are integrated at all, more MaxCal deviation is associated, if
anything, with less Φ. Figure 1a shows the scatter, a structureless cloud with the highest-Φ networks
at low ψ.

The result does not depend on how Φ is aggregated. Against the π-weighted mean Φ, the aggregation best
matched to ψ's own stationary character, ρ = 0.018 (p = 0.81); against max Φ, ρ = 0.125 (p = 0.09). All
three aggregations place ψ at or near zero. The absent signal is not hidden in the mutual-information
companion either: i(π) = H(π) − h(π) gives ρ = −0.135.

One point of statistical care cuts against an over-strong reading. Pooling all five seeds (906 ergodic
networks), the small positive rank association becomes statistically distinguishable from zero (ρ =
0.096, CI [+0.02, +0.17], p = 0.004). With roughly 900 samples even a trivially small effect crosses
significance, so the interpretation must turn on effect size. ρ ≈ 0.10 means ψ accounts for about 1%
of the rank variance in Φ. The genuine integration measure Φ_WMS, on the same networks, reaches ρ =
0.58, about 34% of the rank variance, a factor of thirty higher. ψ's own small association is also not
of stable sign, being positive over the full ergodic set and negative within the Φ > 0 subset, which
is the pattern of noise around zero rather than of a weak but real signal. (The partitioned ϕ_ψ has a
distinct and more stable negative association, discussed separately in §4.3; it is a different measure
and does not bear on the stability of ψ itself.) The defensible claim is therefore not that ψ is
exactly orthogonal to Φ, but that ψ carries no usable integration signal: an order of magnitude weaker
than a real proxy, of inconsistent sign, and below the threshold at which
one would call it tracking.

### 4.3 A partitioned MaxCal measure also fails to track Φ

If ψ's failure were merely the absence of a partition, then ϕ_ψ, which adds IIT's minimum-information-
partition logic, should recover the signal. It does not. Across the ergodic set, ϕ_ψ vs Φ gives ρ =
−0.276 (p < 0.001, AUC = 0.359): a significant negative association, in which higher Φ is associated
with more negative ϕ_ψ. The mean ϕ_ψ is −0.20 among the Φ > 0 networks against −0.06 among the Φ = 0
networks (Figure 1c).

The sign can be traced to the two terms of ϕ_ψ = ψ(whole) − Σ ψ(parts). Neither term tracks Φ on its
own: ρ(ψ(whole), Φ) = +0.085 and ρ(Σ ψ(parts), Φ) = +0.099, both small. The summed deviation of the
parts is the larger of the two in 71% of networks, and it grows with Φ slightly faster than the
whole's: among the Φ > 0 networks the mean ψ(whole) is 0.84 bits against a mean Σ ψ(parts) of 1.04
bits. Marginalising an integrated system onto a node subset tends to concentrate that sub-chain's
occupancy and so raise its self-divergence, so the parts typically deviate from their MaxCal reference
more than the whole does, and the difference ψ(whole) − Σ ψ(parts) is negative. The symmetric
noisy-parity system used as System B in §4.8 is an exception, with single-node marginals near uniform
and ϕ_ψ positive; it is not representative of the ensemble. The general point is that the KL
self-divergence is not subadditive across these cuts in the way a mutual information is, so a
whole-minus-parts construction built on it does not behave like Φ.

The contrast with the positive control is the point. The identical partition operation, the identical
marginalisation and MIP search and whole-minus-parts arithmetic, applied to a mutual information rather
than to ψ yields Φ_WMS, which tracks exact Φ at ρ = 0.58 (Figure 1b). The two measures differ in
exactly one respect: the scalar that is partitioned. Φ_WMS partitions a mutual information; ϕ_ψ
partitions a KL self-divergence. The partition step is therefore not the missing ingredient. The
missing ingredient is the kind of quantity being partitioned, a point we develop in §5.1.

### 4.4 ψ is orthogonal to both IIT 3.0 and IIT 4.0

Because Kearney re-derives 3.0, we computed exact IIT-3.0 Φ on the n = 3 subset (90 ergodic networks,
37 with Φ₃ > 0). The objection that ψ might track the 3.0 repertoires it was derived from, rather than
the 4.0 ID structure, does not survive the comparison: ψ vs IIT-3.0 Φ gives ρ = 0.113, practically
indistinguishable from ψ vs IIT-4.0 Φ on the same networks, ρ = 0.096. ψ misses both. The two oracles
are not measuring different things from ψ's point of view either: IIT-3.0 and IIT-4.0 Φ correlate at ρ
= 0.858 across these networks. So the version of IIT is not the confound; 3.0 and 4.0 largely agree,
and ψ is orthogonal to both. The reason is the one in §2.1: 3.0 and 4.0 differ in their distance
measure but share the partition-and-exclusion skeleton, and that skeleton is what ψ lacks. The n = 4
3.0 values are omitted owing to the EMD instability in §3.6; given that the n = 3 evidence already
shows ψ missing 3.0 by the same margin it misses 4.0, and that 3.0 ≈ 4.0, the missing n = 4 cells are
not material to the conclusion.

### 4.5 Absence of within-stratum correlation

The pooled null does not conceal a strong within-stratum association that cancels on aggregation. By
size, ρ = 0.096 (n = 3) and 0.028 (n = 4). Across the nine (density, noise) cells the per-cell ρ
ranges from +0.155 to −0.170, with no cell showing tracking of the magnitude Φ_WMS shows when pooled.
By gate composition, networks containing each gate type give ρ between +0.017 (parity) and +0.154
(AND). In every stratum ψ's association with Φ is small and of unstable sign. There is no regime in
which ψ becomes a good proxy.

### 4.6 Five-seed stability and power

The per-seed ψ–Φ correlations are 0.085, 0.052, 0.083, 0.122, 0.137 (seeds 1–5), uniformly small and
none reaching the magnitude of a genuine proxy. With n = 181 the minimum detectable |ρ| at α = 0.05 is
≈ 0.146; ψ sits below this threshold while Φ_WMS (ρ = 0.58) sits well above it. The design had ample
power to detect a useful association and did not, while detecting one for the positive control on the
same data.

### 4.7 Comparative performance of candidate measures

**Table 1.** Association with exact IIT-4.0 Φ (mean aggregation) across the 181 ergodic networks (seed
1), ranked by |ρ|. CIs are 2000-sample bootstrap; p is the exact two-sided Spearman p-value.

| measure | Spearman ρ | 95% CI | p | AUC(Φ>0) |
|---|---:|:---:|---:|---:|
| Φ whole-minus-sum (partition-based) | +0.580 | [+0.46, +0.67] | <0.001 | 0.860 |
| integrated synergy (partition-based) | +0.479 | [+0.37, +0.58] | <0.001 | 0.784 |
| total correlation (complexity) | −0.373 | [−0.50, −0.24] | <0.001 | 0.261 |
| ϕ_ψ (partitioned MaxCal) | −0.276 | [−0.42, −0.13] | <0.001 | 0.359 |
| stochastic interaction | +0.136 | [−0.02, +0.28] | 0.068 | 0.573 |
| i(π) = H − h (MaxCal companion) | −0.135 | [−0.28, +0.01] | 0.069 | 0.393 |
| time-delayed MI | −0.135 | [−0.28, +0.01] | 0.070 | 0.394 |
| ψ (maximum-caliber information) | +0.085 | [−0.08, +0.24] | 0.254 | 0.524 |
| causal density | −0.011 | [−0.16, +0.13] | 0.880 | 0.513 |

The two measures that track Φ are the two built on a whole-minus-parts comparison of time-lagged
(predictive) mutual information: Φ_WMS and integrated synergy. Total correlation has a joint-versus-
factorised form but is a static, single-time redundancy with no predictive content and no comparison
across a transition cut, and it anti-correlates. ψ and ϕ_ψ sit with the complexity quantities at the
bottom, ϕ_ψ on the negative side of zero. §5.1 develops the distinction these rankings imply.

### 4.8 Analytic dissociation

To make the mechanism concrete, consider two hand-built systems of the same size, n = 3 (Figure 2c).
System A is three independent COPY nodes, each strongly biased to stay ON: no node influences any other,
so the system is reducible and Φ = 0, yet the stationary distribution concentrates in one corner of
state space far from the MaxCal marginal, giving a large ψ = 2.623. System B is three nodes each
updating to the parity of the other two, maximally integrative since every node depends irreducibly on
the rest, giving Φ_max = 1.378 (mean 0.689), yet its broad occupancy keeps it close to its MaxCal
reference, giving a modest ψ = 0.428. ψ assigns the segregated, unintegrated system about six times the
score of the maximally integrated one, while Φ assigns the segregated system zero. The ranking is
reversed at equal state-space size, by construction. This is the aggregate null of §4.2 in analytic
form, and it shows what ψ responds to: bias and order in the occupancy distribution, which is
complexity, not irreducibility.

## 5. Discussion

### 5.1 The divergence between ψ and Φ is structural

The result of §4.3 locates the obstacle: it is not the absence of a partition but the type of quantity
being partitioned. The leaderboard makes the requirement precise. Two features must be present together
for a measure to track Φ. The measure must compare the whole's cause-effect (predictive) structure
against its parts', and it must do so across a partition. Φ_WMS and integrated synergy have both: each
is a whole-minus-parts comparison of time-lagged mutual information, I(X_{t−1}; X_t), and each tracks Φ
(ρ = 0.58 and 0.48).

Neither feature alone suffices, and the leaderboard contains the relevant controls. Total correlation
is a joint-versus-factorised divergence (Σ_i H(X_i) − H(X) = D_KL of the joint from the product of its
marginals), so it has the divergence form one might think is the key. It nonetheless anti-correlates
with Φ (ρ = −0.37), because it is static, an instantaneous redundancy among nodes with no reference to
the dynamics and no comparison across a transition cut. The divergence form is therefore not the
operative feature; the comparison of predictive structure across a cut is.

ψ has neither feature. ψ = D_KL(π ‖ µ) is the divergence of one distribution, the stationary
occupancy, from a reference derived from the same dynamics. Both arguments are properties of the single,
undivided system, so ψ compares nothing across a cut, and although it involves the transition matrix
through κ and the entropy rate, it summarises the dynamics into a scalar bias of occupancy rather than
comparing the whole's transition structure to its parts'. Partitioning ψ, as ϕ_ψ does, subtracts
self-divergences of sub-chains from the self-divergence of the whole; §4.3 showed that neither the
whole term nor the parts term tracks Φ, and their difference anti-correlates. On this analysis a
partition-free self-divergence of the stationary distribution is not positioned to track Φ, and adding
a partition to it does not change its character, because it still compares occupancy bias rather than
predictive structure. We present this as a structural argument, supported by the leaderboard and the
two analytic systems, rather than as a theorem.

The argument concerns the algebraic form of ψ, not features of the ensemble, so it is not specific to
n ≤ 4; a larger ensemble could shift the small correlations but would not give a self-divergence the
predictive whole-minus-parts structure it lacks. ψ measures how far a system's occupancy departs from
its least-committal reference, which is a form of complexity, and complexity and integration coincide
only in special cases. Systems A and B show them coming apart.

### 5.2 Why the result is not tautological

A sceptic may object that of course the measures with a partition track Φ and those without do not, so
the study only confirms that Φ has a partition. There are two replies.

First, nothing guaranteed that ψ lacked an effective partition. Kearney's central claim is that ψ
derives from the same constrained-maximum-entropy principle he uses to reconstruct IIT's repertoires.
A reasonable hypothesis, the one we pre-registered as H1, was that this shared origin would give the
scalar integration-tracking behaviour even without an explicit cut, because the MaxCal reference µ
already encodes the system's branching structure. That hypothesis was the strongest case for the
bridge, and the results reject it. Finding that a quantity derived to be close to IIT nonetheless fails
to track IIT's central number is an empirical result, not a restatement of definitions.

Second, the ϕ_ψ result answers the charge directly. We did not merely note that ψ lacks a partition
and stop; we added the partition that makes Φ_WMS work, and ψ still failed, indeed reversed. If "has a
partition implies tracks Φ" were the tautology, ϕ_ψ would track Φ. The content of the finding is
therefore not that partitions matter, which is granted, but that the base quantity must be a
mutual-information-type comparison; the MaxCal deviation is not one, so the MaxCal bridge does not
reach Φ even when given IIT's own partition machinery.

### 5.3 Robustness to the degenerate-limit objection

The strongest defence is that we tested the cheap stationary scalar rather than the repertoire-level
construction that carries Kearney's integration content, and so refuted a degenerate limit rather than
the theory. There are three replies, and together we think they are sufficient.

First, we did not test only the scalar. ϕ_ψ is a partition-level MaxCal integration measure,
constructed on the same footing as IIT's MIP, and it fails worse than the scalar. The defence that the
integration lives in the partition step is the one ϕ_ψ was built to test.

Second, the burden of proof rests with the bridge. Kearney offers ψ as the quantity that connects the
frameworks and asks for it to be tied to IIT's metrics. A bridge that connects to Φ only via a further,
unspecified construction, one its author has not exhibited and that we could not make work, is an
unvalidated bridge until that construction is produced and shown to track Φ. We have tested the two
most natural readings of the proposal, the scalar the paper gives and the partition-augmented version
one would build next, and both miss.

Third, the system-level duality, which is proven, is system-level by its nature (§2.3), so the
expectation that a system-level scalar should descend to Φ was not licensed by the mathematics in the
first place. The stationary scalar is not an impoverished shadow of an integration quantity defined
elsewhere; it is a faithful expression of a duality that is not about irreducibility.

### 5.4 The IIT version objection

We pre-empted the objection that we used 4.0 while Kearney derived 3.0 by computing 3.0 directly
(§4.4). ψ misses 3.0 (ρ = 0.11) by the same margin it misses 4.0 (ρ = 0.10), and 3.0 and 4.0 agree
with each other (ρ = 0.86). 3.0 and 4.0 differ in their distance measure, EMD versus intrinsic
difference, but share the partition-and-exclusion skeleton, and it is that skeleton, not the distance,
that ψ lacks. Changing the distance measure changes which integrated systems score how much; it does
not introduce a partition into a partition-free scalar.

### 5.5 The limits of the system-level duality and the role of learning dynamics

None of this refutes the MaxCal–FEP duality at the level Ramstead et al. (2023) prove it. The
correspondence between free energy and constrained entropy at a system's steady state stands, and
Kearney's re-expression of IIT's repertoire calculus in MaxCal terms may be correct as a piece of
construction. What the present result bounds is the reach of the duality as a claim about
consciousness. The duality yields a system-level correspondence between two scalar descriptions of the
same steady state. It does not yield Φ, because Φ is not a system-level scalar in the relevant sense;
it is the output of a partition and a maximisation over the system's decomposition, and the duality is
silent on decomposition. The proven part of the bridge is a statement about a system's steady-state
thermodynamics that does not involve decomposition, whereas Φ essentially involves it. Φ is itself a
whole-system property, but one obtained through a partition and a maximisation over the system's
decomposition, and that decomposition does not follow from a decomposition-free description of the
steady state.

One route remains open, and we regard it as the productive direction rather than a caveat. The
empirical Φ–surprise couplings that motivate this programme, in Lundbak Olesen et al. (2023) and Mayama
et al. (2025), are not observed in static stationary systems. They are observed in systems that learn,
reorganising their cause–effect structure over time as they reduce prediction error. Our test, like
Kearney's scalar, is synchronic, scoring a fixed TPM at its stationary distribution. It is consistent
with everything here that the genuine relationship is diachronic: that as a system minimises free
energy over learning time it tends to build more integrated cause–effect structure, so that ΔΦ
correlates with the trajectory of surprise even though instantaneous ψ does not correlate with
instantaneous Φ. If so, the relevant bridge quantity is not ψ(π) but something like dψ/dt against
dΦ/dt along a learning trajectory. A natural test would train simple reinforcement-learning agents, or
record adapting neuronal cultures, while tracking both ψ(t) and Φ(t) over adaptation time, and ask
whether their changes covary even though their static values do not. That is a testable proposal, and
it concedes the present point: the static scalar ψ is not the bridge to Φ.

### 5.6 Implications

Two broader points follow. The first is methodological. ψ has a strong pedigree, a variational
principle, a proven duality, and a re-derivation of IIT's own machinery, and it still does not track
the quantity it is offered to connect to. The only way to establish that was to compute exact Φ and
compare. Where exact Φ is available, proxies and bridge quantities should be required to earn their
status there (Barrett et al. 2026), and the exact-Φ apparatus used here is one way to do so routinely.

The second is conceptual. ψ joins total correlation and i(π) in the class of complexity measures,
quantities sensitive to order, bias, and predictability in a system's behaviour, and the temptation to
treat such quantities as measures of consciousness should be resisted. Systems A and B illustrate the
risk: a biased, segregated system can score high on a complexity measure while specifying no integrated
cause–effect structure, and a maximally integrated system can score low. If IIT is approximately right
about what matters, complexity and consciousness come apart exactly there, and a measure that cannot
distinguish System A from System B is not a measure of consciousness, whatever else it is useful for.
This is not a criticism of ψ as a complexity statistic, which it may be a good one, but a boundary on
its interpretation.

## 6. Limitations

The networks are small (n ∈ {3,4}), binary, and Boolean-gated. This is forced by the exact-Φ oracle and
is the cost of testing against ground truth rather than a proxy. We do not claim the numbers generalise
to large or biological systems. The structural argument of §5.1 does not depend on size or gate type,
since it depends on ψ being a self-divergence, which holds at any scale; a larger ensemble could move ρ
from 0.09 to 0.2, but it could not turn a complexity measure into an integration measure.

ψ is defined only for ergodic chains, so 89/270 networks are excluded, and the ergodicity screen is a
practical reducibility and periodicity filter rather than a complete aperiodicity certificate. Many
biological and conscious states are metastable or transient, a regime where ψ is undefined while Φ is
not, which is itself a point against ψ as a general consciousness measure but one we do not rely on.

The 3.0 comparator is n = 3 only, owing to an EMD shape error in this 4.0-oriented PyPhi checkout
(§3.6). We judge the n = 3 evidence sufficient given that it already shows ψ missing 3.0 by the 4.0
margin and that 3.0 ≈ 4.0; a complete n = 4 3.0 sweep with a 3.0-configured build is an obvious item
for a revised version. We aggregate state-dependent Φ to a single number and clamp negatives to zero;
the first is mitigated by reporting three aggregations, all null for ψ, and the clamping matches IIT's
treatment of reducible systems. Finally, our ground truth is scalar system Φ, not the full unfolded
structure of distinctions and relations. A bridge to the structure rather than to the scalar is a
different and harder question, and Kearney's repertoire-level derivation belongs to it, which is why
the present result does not touch that derivation.

## 7. Conclusion

We carried out the test Kearney (2026) called for, and the further tests its defence would require. On
systems where Φ is exactly computable, the maximum-caliber information ψ does not track integrated
information (ρ ≈ 0.09, detection at chance, stable across five seeds, robust to aggregation, absent in
every stratum). Giving ψ IIT's own partition step does not rescue it; the resulting ϕ_ψ anti-correlates
with Φ (ρ = −0.28), while the same partition on a mutual information tracks Φ at ρ = 0.58. ψ misses IIT
3.0, the version it was derived from, and IIT 4.0 alike, and the two versions agree with each other, so
the result does not hinge on which IIT is meant. Two minimal hand-built systems show ψ ranking an
unintegrated system above a maximally integrated one. We argue that this is structural rather than a
defect of the chosen reduction: ψ is a self-divergence, a complexity quantity, and complexity is not
integration, with or without a partition step. The MaxCal–FEP duality holds where it is proven, as a
decomposition-free description of a system's steady state, whereas Φ is obtained through a partition and
a maximisation over the system's decomposition, which that description does not determine. A bridge
between IIT and the FEP, if there is one, will be built from the dynamics of learning rather than from a
static scalar, which is the experiment we would do next.

## Data and code availability

All code, data, figures, the literature corpus, and per-paper notes are at
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`psi_vs_phi/`). The study reproduces
end-to-end: `python -m psi_vs_phi.psi` (ψ controls), `python -m psi_vs_phi.run 15 <seed>` (dataset,
seeds 1–5), `python -m psi_vs_phi.exact_phi3 15 1` (IIT-3.0 comparator, n = 3),
`python -m psi_vs_phi.dissociation` (analytic cases), `python -m psi_vs_phi.analyze` (statistics), and
`python -m psi_vs_phi.figures` (figures), built on the exact IIT-4.0 Φ oracle in `proxy_audit/`. For a
citable archive, the release will be deposited at a Zenodo DOI and the frozen tag cited in the final
version.

## Acknowledgments

This study was developed with AI assistance (Anthropic's Claude) for code, analysis, and drafting; all
scientific claims were checked against computed results. The exact-Φ oracle and candidate-measure
framework reused here were built in the companion `iit-experiments` study. We thank A. Kearney for
posting the motivating preprint openly; a courtesy copy of this response will be sent.

## References

Citations resolve to `literature/references.bib`. Key sources:

- Albantakis, L., Barbosa, L., Findlay, G., et al. (2023). Integrated information theory (IIT) 4.0.
  *PLOS Comput. Biol.* 19(10):e1011465. (arXiv:2212.14787)
- Ay, N. (2015). Information geometry on complexity and stochastic interaction. *Entropy*
  17(4):2432–2458.
- Balduzzi, D., & Tononi, G. (2008). Integrated information in discrete dynamical systems. *PLOS
  Comput. Biol.* 4(6):e1000091.
- Barrett, A. B., & Seth, A. K. (2011). Practical measures of integrated information for time-series
  data. *PLOS Comput. Biol.* 7(1):e1001052.
- Barrett, A. B., Milinkovic, M., Mediano, P. A. M., Rosas, F. E., Bor, D., Barnett, L., & Seth, A. K.
  (2026). Integrated information theory: the good, the bad and the misunderstood. arXiv:2604.11482.
- Dixit, P. D., et al. (2018). Maximum caliber is a general variational principle for dynamical
  systems. *J. Chem. Phys.* 148:010901. (arXiv:1711.03450)
- Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019). The unfolding argument. *Conscious.
  Cogn.* 72:49–59.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.*
  11:127–138.
- Friston, K. (2019). A free energy principle for a particular physics. arXiv:1906.10184.
- Hanson, J. R., & Walker, S. I. (2021). Formalizing falsification for theories of consciousness.
  *Neurosci. Conscious.* 2021(2):niab014. (arXiv:2006.07390)
- Kearney, A. (2026). Information as Maximum-Caliber Deviation: A bridge between Integrated Information
  Theory and the Free Energy Principle. arXiv:2605.12536.
- Lundbak Olesen, C., Waade, P. T., Albantakis, L., & Mathys, C. (2023). Phi fluctuates with surprisal.
  *PLOS Comput. Biol.* 19(10):e1011346.
- Mayama, T., et al. (2025). Bridging integrated information theory and the free-energy principle in
  living neuronal networks. arXiv:2510.04084.
- Mediano, P. A. M., Seth, A. K., & Barrett, A. B. (2019). Measuring integrated information. *Entropy*
  21(1):17.
- Mediano, P. A. M., Rosas, F. E., Bor, D., Seth, A. K., & Barrett, A. B. (2022). The strength of weak
  integrated information theory. *Trends Cogn. Sci.* 26(8):646–655.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
  consciousness: IIT 3.0. *PLOS Comput. Biol.* 10(5):e1003588.
- Pressé, S., Ghosh, K., Lee, J., & Dill, K. A. (2013). Principles of maximum entropy and maximum
  caliber in statistical physics. *Rev. Mod. Phys.* 85:1115.
- Ramstead, M. J. D., et al. (2023). On Bayesian mechanics. *Interface Focus* 13(3):20220029.
  (arXiv:2205.11543)
- Safron, A. (2020). An Integrated World Modeling Theory (IWMT) of consciousness. *Front. Artif.
  Intell.* 3:30.
- Seth, A. K. (2008). Causal networks in simulated neural systems. *Cogn. Neurodyn.* 2:49–64.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neurosci.* 5:42.
- Williams, P. L., & Beer, R. D. (2010). Nonnegative decomposition of multivariate information.
  arXiv:1004.2515.
