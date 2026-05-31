# Maximum-caliber information is a complexity measure, not an integration measure: a direct test of ψ against exact IIT-4.0 Φ

**Roger Hunt**

*Preprint draft, May 2026. Code, data, figures, and the full literature corpus:
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`psi_vs_phi/`).
Citations are author–year and resolve to `literature/references.bib`. This is a response to an
unrefereed preprint posted three weeks prior (Kearney 2026); it is offered in that collegial spirit.*

---

## Abstract

Integrated Information Theory (IIT) and the Free Energy Principle (FEP) are the two most ambitious
mathematical frameworks for, respectively, the structure of consciousness and the dynamics of
self-organisation, and a rigorous bridge between them would be a significant result. Kearney (2026)
proposes one: defining an information quantity ψ as the deviation of a system's realised dynamics
from a constrained maximum-caliber (MaxCal) path ensemble, he re-derives IIT 3.0's cause–effect
repertoires from this principle and links ψ to prediction error and the FEP. For a stationary ergodic
Markov chain the proposal reduces to a closed-form scalar, ψ(π) = log₂κ − H(π) − h(π). But ψ is
never compared against integrated information Φ — the quantity the bridge is supposed to reach — and
the paper explicitly calls for that test. We run it, exhaustively. On an ensemble of small discrete
networks where exact IIT-4.0 Φ is computable without approximation, we implement ψ (validated against
the paper's own worked controls to machine precision) and ask whether it tracks exact Φ. **It does
not.** Across 181 ergodic networks ψ is essentially uncorrelated with Φ (Spearman ρ = 0.085, 95% CI
[−0.08, +0.24]; detection AUC = 0.52, chance), and the result is robust to how Φ is aggregated
(π-weighted ρ = 0.02, max ρ = 0.13), stable across five random seeds, and absent within every
density, noise, and gate-type stratum we examined. We then test the obvious rescue: we give ψ the
partition step it lacks, constructing a MaxCal *integration* measure ϕ_ψ analogous to IIT's
minimum-information-partition, and show that this does not help — ϕ_ψ is, if anything, weakly
*anti*-correlated with Φ (ρ = −0.28), whereas the identical partition operation applied to a mutual
information (whole-minus-sum Φ) tracks exact Φ at ρ = 0.58 on the same networks. We further rule out
the natural objection that ψ might track the IIT *3.0* repertoires Kearney actually re-derives:
ψ misses 3.0 Φ as badly as it misses 4.0 Φ (ρ = 0.11 vs 0.10), and 3.0 and 4.0 Φ themselves agree
(ρ = 0.86), so the oracle version is not the issue. Two hand-built minimal systems make the mechanism
analytic: a segregated, biased system scores ψ = 1.75 with Φ = 0, while an integrated parity-coupled
system scores ψ = 0.43 with Φ = 1.38 — ψ ranks them backwards. We argue that this is not an empirical
accident to be patched by a better reduction but a structural fact: ψ is a self-divergence of a
single distribution from a reference, an order/disorder *complexity* quantity, and no amount of
partitioning converts a complexity measure into an irreducibility measure. The MaxCal–IIT–FEP bridge
holds at the level it is actually proven — a system-level duality between free energy and constrained
entropy — but it does not, and we contend cannot, descend to a scalar ψ ≈ Φ relationship. This leaves
Kearney's separate repertoire-level derivation untouched, and we say precisely why.

---

## 1. Introduction

Two research programmes dominate the mathematical study of mind. Integrated Information Theory (IIT)
identifies a conscious experience with the irreducible cause–effect structure that a physical
substrate specifies for itself, and quantifies the *quantity* of consciousness by integrated
information, Φ (Tononi 2004; Oizumi, Albantakis & Tononi 2014; Albantakis et al. 2023). The Free
Energy Principle (FEP) holds that any system that persists as a thing distinct from its environment —
anything individuated by a Markov blanket — can be described as minimising variational free energy,
a tractable upper bound on the surprise of its sensory states (Friston 2010, 2019). The frameworks
start from opposite ends. IIT is intrinsic, synchronic, and about structure; the FEP is extrinsic,
dynamical, and about persistence. That they might nevertheless be two views of the same underlying
fact is one of the most tantalising conjectures in theoretical neuroscience, and several authors have
pursued it (Safron 2020; Lundbak Olesen et al. 2023; Mayama et al. 2025). Until recently the
connection was conceptual or correlational, not a mapping you could compute with.

Kearney (2026) sets out to supply the mapping. The vehicle is maximum caliber (MaxCal), the
trajectory-space generalisation of the maximum-entropy principle (Pressé et al. 2013; Dixit et al.
2018): among all probability distributions over a system's possible paths that are consistent with
some measured dynamical constraints, MaxCal selects the least-committal one, the path ensemble of
maximum entropy. Kearney defines an information quantity ψ as the deviation — formally a
Kullback–Leibler divergence — of a system's *realised* dynamics from this MaxCal reference ensemble.
He then makes two distinct moves. First, at the level of *construction*, he re-derives IIT 3.0's
cause and effect repertoires (the conditional distributions IIT uses to score a mechanism's
"difference it makes") from this single constrained-maximum-entropy principle. Second, at the level
of *quantity*, he shows that ψ coincides with prediction error / Bayesian surprise in appropriate
asymptotic limits, which is what ties it to the FEP. For the special but important case of a
stationary, ergodic Markov chain, the second move collapses to a remarkably cheap closed-form scalar,

> ψ(π) = log₂κ − H(π) − h(π),

where H(π) is the entropy of the chain's stationary distribution, h(π) is its entropy rate, and κ is
a system-specific normaliser we define carefully in §2.4.

This is an elegant and genuinely useful construction. But it contains a conspicuous, self-acknowledged
hole. At no point is ψ compared against Φ — the integrated information it is meant to bridge toward.
The paper is candid about this: "the explanatory power of our proposal here remains unconfirmed.
Experimental or theoretical work must be conducted to … connect the metrics observed here to those in
IIT." The bridge, in other words, is built and asserted but not load-tested. Whether a structure can
bear weight is not a matter of how elegantly it was assembled; it is a matter of whether it stands up
when you put weight on it. The purpose of this paper is to put the weight on.

We are in an unusually good position to do so, because we hold an instrument that most consciousness
research lacks: an *exact* IIT-4.0 Φ oracle. Φ has never been computed for a real brain, or indeed
for any system of biological scale — the computation is super-exponential, and what gets reported on
empirical data are always *proxies* whose relationship to canonical Φ is mostly unverified (Barrett
et al. 2026). But for small discrete systems — networks of a handful of binary nodes — Φ *is*
computable exactly, with no approximation, using PyPhi's implementation of the IIT-4.0 formalism.
This is the regime in which a candidate bridge quantity can be held against ground truth and made to
answer for itself. A companion line of work in the same repository uses exactly this strategy to
audit empirical proxies and candidate integration measures; here we turn the same apparatus on ψ.

Our contribution is fourfold, and each part anticipates and forecloses an objection a defender of the
bridge would raise:

1. **The direct test.** We implement ψ exactly from Kearney's definition, validate it against the
   paper's own worked cases, and correlate it with exact IIT-4.0 Φ across a 270-network ensemble. ψ
   does not track Φ, and we show this is robust to the choice of Φ aggregation, stable across five
   seeds, and not an artefact of pooling heterogeneous regimes.
2. **The partition rescue, tested and refused.** The natural defence is that we tested only the
   "degenerate" stationary scalar and not the integration structure Kearney sketches at the
   repertoire level. So we build that structure: a partitioned MaxCal measure ϕ_ψ that bolts IIT's
   minimum-information-partition logic directly onto ψ. It still fails — indeed it inverts — while the
   *same* partition operation makes a mutual-information-based measure succeed.
3. **The version objection, closed.** Kearney re-derives IIT *3.0*; we primarily validate against IIT
   *4.0*. We compute 3.0 Φ on the subset where it is stable and show ψ misses both, and that 3.0 and
   4.0 agree with each other — so the result does not hinge on which IIT one means.
4. **The mechanism, made analytic.** We exhibit two tiny hand-built systems on which ψ and Φ
   dissociate in both directions, so the reader can see *why* the correlation vanishes without
   trusting an aggregate statistic.

The thesis we will defend is stronger than "the experiment came out null." It is that the null was
inevitable, for a reason that is visible in the algebra of ψ before any network is generated, and
that the same reason places a hard ceiling on how far the MaxCal–FEP duality can be pushed as a claim
about consciousness. We state that thesis sharply in §5 and argue for it rather than merely asserting
it.

## 2. Background

### 2.1 What Φ measures, and the two operations that define it

Everything in this paper turns on two operations that are constitutive of Φ and absent from ψ, so we
spell them out before anything else.

IIT begins from a substrate: a set of interacting units whose joint dynamics are given by a transition
probability matrix (TPM), specifying for each current state the probability distribution over next
states. From the TPM, IIT constructs, for every candidate subset of units (every "mechanism") in a
given state, a **cause repertoire** and an **effect repertoire** — the probability distributions over
the states that could have produced, and that will be produced by, the mechanism's current state. A
mechanism contributes to consciousness only if these repertoires are **irreducible**: if you could
partition the mechanism into independent parts and reconstruct the same repertoires from the parts'
repertoires alone, the mechanism specifies nothing over and above its parts and is discarded. This is
the **partition** operation, and the degree of irreducibility — how much information is lost under the
partition that costs the least to make, the *minimum information partition* (MIP) — is the integrated
information of that mechanism.

At the system level the same logic recurs. The whole substrate's cause–effect structure is scored
against the structure that survives cutting the system across its weakest bipartition; the system-level
Φ is the irreducibility of the whole across its MIP. And there is a second operation: **exclusion**.
Among all the overlapping candidate substrates, only the one with maximal integrated information — the
*maximal substrate*, or complex — actually exists as an entity; the others are excluded. Φ is thus
not a property of a fixed set of nodes but the outcome of a maximisation over candidate sets, each
evaluated by an irreducibility-across-a-partition computation.

Hold onto this: **Φ is, definitionally, a whole-minus-its-best-cut quantity, selected by a
maximisation.** A measure that contains neither a partition nor a maximisation is not measuring a
small or noisy version of Φ; it is measuring something else.

IIT 3.0 (Oizumi et al. 2014) scored the difference a mechanism makes using the earth-mover's distance
(EMD) between repertoires and an unconstrained baseline. IIT 4.0 (Albantakis et al. 2023) replaced
EMD with a uniquely-determined *intrinsic difference* (ID) measure, motivated axiomatically, and
unfolded the system into a structure of distinctions and relations whose total is the canonical,
computable Φ. The difference between 3.0 and 4.0 is real and matters for some questions — but, as we
will show empirically in §4.4, it does not matter for *this* question, because both 3.0 and 4.0 retain
the partition-and-exclusion skeleton, and that skeleton is what ψ lacks.

### 2.2 The measurement problem, and why exact Φ is the right adjudicator

Because canonical Φ is uncomputable beyond toy systems, empirical consciousness science runs on
proxies: perturbational complexity, candidate integration measures from the Mediano–Seth–Barrett
lineage (Mediano, Seth & Barrett 2019), and so on. Barrett et al. (2026) argue forcefully that these
proxies must be *validated* against the thing they proxy rather than assumed to track it, and note
that Φ is arguably not even well-defined for continuous physical systems. The strong-vs-weak IIT
distinction (Mediano et al. 2022) and the unfolding argument (Doerig et al. 2019) further complicate
what "validation" should even mean. Our stance is operational and, we think, unimpeachable for the
present purpose: when exact Φ *is* available — as it is on small discrete networks — a candidate that
claims a relationship to Φ must demonstrate it there, on ground truth, or the claim is unsupported.
ψ makes such a claim. We test it where it can be tested.

### 2.3 MaxCal, the path ensemble, and the duality that is actually proven

Maximum entropy (MaxEnt) selects, among distributions consistent with measured averages, the one of
greatest entropy — the least-biased distribution. Maximum caliber (MaxCal) lifts this from states to
*trajectories*: among distributions over a system's possible paths consistent with measured dynamical
constraints, it selects the one of greatest *path* entropy (Pressé et al. 2013; Dixit et al. 2018).
The selected ensemble is a reference: the dynamics you would predict knowing only the constraints and
nothing else. Kearney's ψ measures how far a system's actual dynamics depart from this reference,
which is why ψ is naturally a Kullback–Leibler divergence — a directed "distance" of the real
distribution from the MaxCal one.

The link to the FEP runs through a duality. Ramstead et al. (2023), building the programme of
Bayesian mechanics, *prove* — asymptotically, under non-equilibrium-steady-state and Markov-blanket
assumptions — a correspondence between minimising variational free energy and a constrained
maximum-entropy description of a system's steady state. This is the rigorous core that makes a
MaxCal→FEP bridge coherent. We stress a feature of it that will matter enormously in §5: the proven
duality is a statement at the level of the *whole system's* steady-state distribution. It relates the
system's free energy to the system's constrained entropy. **It contains no partition, no exclusion,
and no maximisation over candidate substrates.** Nothing in the duality, as proven, says anything
about *irreducibility across a cut*. This is not a gap in the proof to be filled later; it is what the
proof is about. The duality is a system-level fact, and Φ is not a system-level fact in the same
sense — Φ is a fact about how the system decomposes.

### 2.4 Kearney's ψ, defined completely

We now define ψ in full, because the argument of this paper depends on what is and is not inside it.
Let the system be a homogeneous Markov chain on N discrete states with transition matrix P, where
P(x, ·) is the probability distribution over next states given current state x. All entropies are in
bits.

- The **conditional entropy of the dynamics out of state x** is Hc(x) = H(P(x, ·)) = −Σ_y P(x,y)
  log₂ P(x,y). It measures how unpredictable the next step is, given that the system is in x.
- The **per-state perplexity** PP(x) = 2^{Hc(x)} is the "effective number of next-states" reachable
  from x — the antilog of the conditional entropy.
- The **MaxCal normaliser** κ = Σ_x PP(x) sums these effective branchings over all states. It is
  *system-specific*: it depends on the full transition structure, not just on N.
- The **MaxCal input marginal** µ(x) = PP(x)/κ is the reference distribution over states that the
  maximum-caliber ensemble implies — the stationary occupancy you would expect if the system simply
  reflected its branching structure with no further bias.
- The chain's actual **stationary distribution** π solves π = πP.
- The **entropy rate** h(π) = Σ_x π(x) Hc(x) is the long-run per-step uncertainty of the dynamics
  under π.
- Finally, the **maximum-caliber information** is

> ψ(π) = log₂κ − H(π) − h(π) = D_KL(π ‖ µ),   (Kearney eq. 5.10)

the equality on the right being an algebraic identity (we verify it numerically below). The KL form
makes three things transparent. (i) ψ ≥ 0 always, with equality iff π = µ — that is, iff the system's
realised occupancy coincides with its MaxCal reference. (ii) ψ is a property of a *single*
distribution (π) measured against a *fixed reference* (µ) derived from the same dynamics. (iii) ψ is
therefore a *self-divergence*: it asks "how far is this system from its own least-committal
description?" — a question about order, bias, and predictability, i.e. about complexity.

It is worth pausing on the companion quantity i(π) = H(π) − h(π), which is the mutual information
between consecutive states of the chain, I(X_{t−1}; X_t). One might hope the integration signal hides
here. We test that too; it does not (§4).

Nowhere in ψ is there a partition of the system into parts, a comparison of the whole to its parts, or
a maximisation over candidate substrates. ψ never cuts the system. This is the single most important
fact about it, and §5 argues it is dispositive.

### 2.5 Prior IIT–FEP unifications

Safron's Integrated World Modelling Theory (2020) is a conceptual synthesis rather than a mapping.
Lundbak Olesen et al. (2023) report empirically that Φ fluctuates with surprisal in a simulated agent,
an encouraging correlation but not a derivation. Mayama et al. (2025) describe a "hill-shaped"
Φ trajectory in living neuronal cultures as they adapt — and, importantly, their Φ is itself a proxy
and the relationship they find is over *learning time*, a point we return to in §5.5. None of these
computes a candidate bridge quantity against exact Φ. Kearney's derivation is the most rigorous
attempt to date to connect the formalisms, which is precisely why it deserves a rigorous test.

## 3. Methods

### 3.1 Design and pre-registered hypotheses

This is a within-ensemble measure-validation study. For each network we compute exact IIT-4.0 Φ
(ground truth) and the candidate ψ (and its variants), then quantify how strongly ψ tracks Φ. Two
hypotheses were fixed before computing any ψ–Φ association:

- **H1 (the bridge descends to the scalar):** ψ tracks exact Φ — a substantial positive monotonic
  association, comparable to that of genuine integration measures.
- **H0 (ψ is complexity, not integration):** ψ tracks order/disorder complexity and is at best weakly
  and unreliably related to Φ.

We regard H0 as the theoretically favoured outcome for the structural reasons of §2.4, but the design
is built so that H1 *could* win: the same apparatus detects a strong Φ signal when one is present
(§3.7, §4.7), so a null for ψ is informative rather than a dead detector.

### 3.2 The system ensemble, specified exactly

Each network has *n* binary units. Every unit updates as a possibly-noisy Boolean function of the
units that feed into it, drawn uniformly from five gate types chosen to span the integration spectrum:
OR and AND (low integration), COPY (near-trivial), MAJORITY (intermediate), and PARITY/XOR (maximally
integrative, since a node's next value depends jointly and irreducibly on all its inputs). For each
network we (i) draw a connectivity matrix by including each directed edge independently with
probability equal to the *density*, guaranteeing every node at least one input; (ii) assign each node
a random gate; (iii) build the state-by-node TPM, mixing each node's deterministic output toward 0.5
by the *noise* level (noise 0 gives deterministic dynamics; higher noise softens them).

The ensemble sweeps a full grid: densities ∈ {0.3, 0.5, 0.8}, noise ∈ {0.0, 0.05, 0.2}, and sizes
n ∈ {3, 4}, with 15 networks per (size, density, noise) cell, giving 2 × 3 × 3 × 15 = **270 networks**
per seed. The size cap n ≤ 4 is dictated by the exact-Φ oracle: Φ is computed over all reachable
states of all candidate substrates, which is feasible at n = 3,4 and quickly becomes infeasible
beyond. We generate five independent seeds (1–5) for stability. The generator is the shared,
version-controlled `proxy_audit.networks.generate_ensemble`, identical to the one used to audit the
other candidate measures, so ψ is tested on exactly the systems they were.

This is admittedly a particular slice of dynamical-systems space — small, binary, Boolean-gate. We
neither hide this nor apologise for it: it is the *only* slice on which the comparison can be made
against exact ground truth rather than a proxy, and §5.6 argues the structural conclusion does not
depend on the slice.

### 3.3 The exact-Φ oracle and three aggregations

Φ was computed with PyPhi's IIT-4.0 system-irreducibility analysis (`pyphi.new_big_phi.sia`) on the
whole substrate in a given state. Φ is state-dependent, so to obtain one system-level number per
network we aggregate over the network's reachable states (states with at least one predecessor under
the dynamics, which PyPhi will analyse). A negative system Φ denotes a *reducible* system in that
state — not an integrated complex — and carries zero integrated information, so we clamp negatives to
0, matching IIT's own treatment of complexes.

A reviewer-anticipated concern is that the choice of aggregation could drive the result. We therefore
compute three aggregations and report all of them: the **uniform mean** over reachable states (the
primary value), the **maximum** over reachable states, and the **stationary-π-weighted mean**, which
weights each state's Φ by how often the system actually occupies it. The π-weighted mean is the most
defensible comparator for a stationary quantity such as ψ, since ψ is itself a stationary-distribution
property. For n ∈ {3,4} every reachable state is evaluated (≤16), so the three aggregations are
computed from the same exact per-state Φ values, not from subsamples.

### 3.4 The ψ implementation and the ergodicity screen

ψ is implemented directly from the formulas of §2.4 (`psi_vs_phi/psi.py`). The chain's state-by-state
TPM is obtained from the state-by-node TPM via PyPhi's converter; the stationary distribution is found
by power iteration. ψ is defined only for ergodic, homogeneous chains (a unique stationary
distribution must exist and be independent of the start), so each chain is screened for ergodicity by
a practical test: power iteration from a uniform start and from a one-hot start must converge to the
same stationary distribution. This catches reducible chains (multiple recurrent classes) and gross
periodicity. We acknowledge in §6 that this screen detects reducibility and gross periodicity but is
not a complete aperiodicity certificate; it is reported as a practical filter. The primary analysis is
restricted to the ergodic subset; non-ergodic networks are flagged and excluded, and the count is
reported.

### 3.5 The partitioned MaxCal integration measure ϕ_ψ — giving ψ a fair shot at integration

The central methodological addition of this revision is a measure designed to give the bridge its
*best* case. The objection that the bare scalar ψ is a degenerate reduction, and that the integration
content of Kearney's proposal lives in the repertoire-level construction with its partition step, is a
fair one. So we construct the partitioned analogue explicitly and on the same footing as IIT.

For a bipartition of the nodes into parts A and B, we form the **marginal sub-chain** on A by
projecting the stationary-weighted joint distribution of consecutive states onto A's coordinates and
row-normalising — exactly the marginalisation the whole-minus-sum candidate measure already uses, so
that ϕ_ψ and Φ_WMS treat the partition identically and differ *only* in the underlying scalar. We then
define the partitioned MaxCal integration as

> ϕ_ψ = ψ(whole) − min over bipartitions (A,B) of [ ψ(A) + ψ(B) ],

minimising the per-part-normalised difference and reporting the un-normalised value at that
minimum-information bipartition, mirroring `phi_wms` precisely. The construction is principled: ψ is
*exactly additive* over independent subsystems (if A and B evolve independently, κ, H, and h all
factorise and ψ(whole) = ψ(A) + ψ(B)), so ϕ_ψ measures the irreducibility of the system's MaxCal
deviation across its weakest cut — the very operation ψ alone omits and that Φ is built upon. If giving
ψ a partition step makes it track Φ, ϕ_ψ will reveal it. This is the strongest steel-man of the bridge
we can construct, and §4.3 reports what it does.

### 3.6 The IIT-3.0 comparator

Because Kearney re-derives IIT *3.0* repertoires, we computed whole-system IIT-3.0 Φ on the same
networks (`psi_vs_phi/exact_phi3.py`), configured for 3.0 (IIT_VERSION 3.0, DIRECTED_BI system
partitions, EMD repertoire distance), aggregated identically to the 4.0 oracle. Two practical notes,
reported rather than hidden: (i) the 3.0 concept-evaluation path routes through a parallel map-reduce
that requires an optional dependency we do not install, so we force sequential evaluation via a thin
patch — results are identical, only slower; (ii) the EMD code in this 4.0-oriented checkout raises a
histogram-shape error on some n = 4 repertoires, so the 3.0 comparator is computed on the **n = 3
subset only**, where every evaluation is stable (0 errors across 90 ergodic networks). This is a real
limitation of the present run, not of the argument, and §4.4 shows the n = 3 evidence is decisive on
its own.

### 3.7 The candidate-measure leaderboard

To establish that the apparatus *can* detect integration, we rank ψ and ϕ_ψ against six practical
integration/complexity measures computed on the identical ergodic networks (`candidate_audit`):
whole-minus-sum Φ (Φ_WMS; Balduzzi & Tononi 2008; Barrett & Seth 2011), integrated synergy
(a co-information net-synergy measure that avoids the spurious-synergy pathology of MMI-based
decompositions), stochastic interaction (Ay 2001), causal density (mean pairwise transfer entropy;
Seth 2008), total correlation (instantaneous multi-information), and time-delayed mutual information.
Φ_WMS is the critical positive control: it is a partition-based whole-minus-parts measure, and if the
test is alive it should track Φ.

### 3.8 Validation controls (run before any ψ–Φ analysis)

Following the discipline that has caught measure-implementation bugs in the companion studies, ψ was
validated against Kearney's own predictions *before* any ψ–Φ number was computed: ψ = 0 for circulant
and uniform-row chains (π = µ); ψ = log₂N − H(π) for deterministic permutations; ψ ≥ 0 across random
chains; and exact agreement of the two equivalent forms (entropy form and KL form). ϕ_ψ was likewise
validated: ≈ 0 for a separable two-node system and the additivity identity confirmed.

### 3.9 Statistics

For each measure against Φ we report Spearman ρ (rank, the primary statistic given the skewed Φ
distribution), Pearson r, and the area under the ROC curve for detecting Φ > 0; bootstrap 95%
confidence intervals (2000 resamples); exact Spearman p-values; the association restricted to the
Φ > 0 subset; per-size, per-(density,noise)-cell, and per-gate-type breakdowns to rule out a
pooled cancellation (a Simpson's-paradox check); and a five-seed pooling. As a sensitivity/power
statement we compute the **minimum detectable |ρ|** at the analysis sample size — the correlation
whose Fisher-z 95% interval just excludes zero — so the null can be read against what the design could
have found.

## 4. Results

### 4.1 ψ is implemented exactly

All controls passed. ψ = 0 for circulant and uniform-row chains; ψ = log₂N − H(π) for deterministic
permutations; ψ ≥ 0 across 200 random chains; and the entropy-form and KL-form definitions agreed to a
maximum difference of 1.3 × 10⁻¹⁵ — machine precision. ψ is therefore computed exactly and as Kearney
defines it; nothing below is an implementation artefact.

### 4.2 ψ does not track exact IIT-4.0 Φ, and the result is robust

Of the 270 seed-1 networks, 181 were ergodic (the primary analysis set), of which 55 had Φ > 0; Φ
ranged from 0 to 1.588 bits. Across the ergodic set, ψ is essentially uncorrelated with exact Φ:
**Spearman ρ = 0.085** (95% bootstrap CI [−0.08, +0.24], comfortably including zero; exact p = 0.25),
Pearson r = −0.116, and the detection AUC for Φ > 0 is **0.524 — chance**. Restricting to the
integrated systems (Φ > 0) gives ρ = −0.318: if anything, among systems that are integrated at all,
*more* MaxCal deviation predicts *less* Φ. Figure 1a shows the scatter — a structureless cloud, with
the highest-Φ networks sitting at low ψ.

The result does not depend on how Φ is aggregated. Against the π-weighted mean Φ — the aggregation
best matched to ψ's own stationary character — ρ = 0.018 (p = 0.81); against max Φ, ρ = 0.125
(p = 0.09). All three aggregations put ψ at or near zero. Nor does the absent signal hide in the
mutual-information companion: i(π) = H(π) − h(π) gives ρ = −0.135.

A note on rigour, because it cuts against an over-strong reading of our own result. When we pool all
five seeds (906 ergodic networks), the small positive rank association becomes *statistically*
distinguishable from zero (ρ = 0.096, CI [+0.02, +0.17], p = 0.004). We do not hide this behind a
"correlation ≈ 0" slogan. The correct reading is the one statistics demands: with ~900 samples even a
trivially small effect crosses significance, and ρ ≈ 0.10 means ψ accounts for roughly **1% of the
rank variance** in Φ. The genuine integration measure Φ_WMS, on the *same* networks, reaches ρ = 0.58
— about **34%** of the rank variance, a factor of thirty more. Moreover ψ's tiny association is not
even of stable sign (positive overall, negative within the Φ > 0 subset, negative as ϕ_ψ; see §4.3),
which is the signature of noise around zero, not of a weak-but-real signal. The honest claim is
therefore not "ψ is exactly orthogonal to Φ" but the stronger and more defensible "**ψ carries no
usable integration signal: an order of magnitude weaker than a real proxy, of inconsistent sign, and
below the threshold at which one would call it tracking.**"

### 4.3 Giving ψ a partition step does not rescue it — it inverts it

This is the decisive new result. If ψ's failure were merely the absence of a partition operation, then
ϕ_ψ — ψ endowed with IIT's minimum-information-partition logic — should recover the signal. It does
the opposite. Across the ergodic set, **ϕ_ψ vs Φ gives ρ = −0.276** (p < 0.001, AUC = 0.359): a
*significant negative* association. The most "integrated-looking" systems under the MaxCal
whole-minus-parts construction are among the *least* integrated under Φ. Figure 1c shows the pattern:
the high-Φ networks cluster at ϕ_ψ ≈ 0, while the most negative ϕ_ψ values belong to low-Φ networks.

The contrast with the positive control is the whole point. The identical partition operation —
identical marginalisation, identical MIP search, identical whole-minus-parts arithmetic — applied to a
*mutual information* rather than to ψ yields Φ_WMS, which tracks exact Φ at ρ = 0.58 (Figure 1b). The
two measures differ in exactly one respect: the scalar that is partitioned. Φ_WMS partitions a mutual
information; ϕ_ψ partitions a KL self-divergence. The partition step is therefore demonstrably *not*
the missing ingredient. **The missing ingredient is the kind of quantity being partitioned.** A
mutual information measures shared structure *between* the parts and the whole's future, so cutting it
exposes irreducibility; a self-divergence measures one distribution's deviation from a reference, and
cutting it exposes nothing of the sort. We develop this into a general claim in §5.1.

### 4.4 ψ misses IIT 3.0 as badly as IIT 4.0, and the two agree

Because Kearney re-derives 3.0, we computed exact IIT-3.0 Φ on the n = 3 subset (90 ergodic networks,
37 with Φ₃ > 0). The objection "perhaps ψ tracks the 3.0 repertoires it was derived from, not the 4.0
ID structure" is thereby foreclosed: **ψ vs IIT-3.0 Φ gives ρ = 0.113**, statistically and practically
indistinguishable from **ψ vs IIT-4.0 Φ on the same networks, ρ = 0.096**. ψ misses both. And the two
oracles are not measuring different things from ψ's point of view: **IIT-3.0 and IIT-4.0 Φ correlate at
ρ = 0.858** across these networks. So the version of IIT is not a confound — 3.0 and 4.0 largely agree
with each other, and ψ is orthogonal to both. The n = 4 3.0 values are omitted owing to the EMD
instability noted in §3.6; given that the n = 3 evidence already shows ψ missing 3.0 by the same margin
it misses 4.0, and that 3.0 ≈ 4.0, we do not regard the missing n = 4 3.0 cells as material to the
conclusion.

### 4.5 No hidden within-regime tracking (Simpson's-paradox check)

The pooled null is not concealing a strong within-stratum association that cancels on aggregation. By
size, ρ = 0.096 (n = 3) and 0.028 (n = 4). Across the nine (density, noise) cells the per-cell ρ
ranges from +0.155 to −0.170, with no cell exhibiting tracking of the magnitude Φ_WMS shows pooled.
By gate composition, networks containing each gate type give ρ between +0.017 (parity) and +0.154
(AND). In every stratum ψ's association with Φ is small and of unstable sign. There is no regime in
which ψ becomes a good proxy.

### 4.6 Five-seed stability and a power statement

The per-seed ψ–Φ correlations are 0.085, 0.052, 0.083, 0.122, 0.137 (seeds 1–5): uniformly small and
none reaching the magnitude of a genuine proxy. With n = 181 the minimum detectable |ρ| at α = 0.05 is
≈ 0.146; ψ's correlation sits below this threshold while Φ_WMS (ρ = 0.58) sits far above it. The
design had ample power to detect a real association of useful size and did not, while detecting one for
the positive control on identical data. The null is a finding, not a failure of sensitivity.

### 4.7 Leaderboard

**Table 1.** Association with exact IIT-4.0 Φ (mean aggregation) across the 181 ergodic networks
(seed 1), ranked by |ρ|. CIs are 2000-sample bootstrap; p is the exact two-sided Spearman p-value.

| measure | Spearman ρ | 95% CI | p | AUC(Φ>0) |
|---|---:|:---:|---:|---:|
| Φ whole-minus-sum (partition-based) | **+0.580** | [+0.46, +0.67] | <0.001 | 0.860 |
| integrated synergy (partition-based) | +0.479 | [+0.37, +0.58] | <0.001 | 0.784 |
| total correlation (complexity) | −0.373 | [−0.50, −0.24] | <0.001 | 0.261 |
| **ϕ_ψ (partitioned MaxCal)** | **−0.276** | [−0.42, −0.13] | <0.001 | 0.359 |
| stochastic interaction | +0.136 | [−0.02, +0.28] | 0.068 | 0.573 |
| i(π) = H − h (MaxCal companion) | −0.135 | [−0.28, +0.01] | 0.069 | 0.393 |
| time-delayed MI | −0.135 | [−0.28, +0.01] | 0.070 | 0.394 |
| **ψ (maximum-caliber information)** | **+0.085** | [−0.08, +0.24] | 0.254 | 0.524 |
| causal density | −0.011 | [−0.16, +0.13] | 0.880 | 0.513 |

The two measures that track Φ are precisely the two that combine a mutual-information base with a
partition step. ψ and ϕ_ψ — the MaxCal scalar and its partitioned extension — sit with the
complexity quantities at the bottom, ϕ_ψ on the wrong side of zero.

### 4.8 Analytic dissociation: ψ ranks two minimal systems backwards

To make the mechanism concrete rather than statistical, consider two hand-built systems (Figure 2c).
System A is two independent COPY nodes, each strongly biased to stay ON: no node influences any other,
so the system is reducible and **Φ = 0**, yet the stationary distribution piles up in one corner of
state space far from the MaxCal marginal, giving a large **ψ = 1.749**. System B is three nodes each
updating to the parity of the other two — maximally integrative, every node depending irreducibly on
the rest — giving **Φ_max = 1.378** (mean 0.689), yet its broad, near-uniform occupancy keeps it close
to its MaxCal reference, giving a modest **ψ = 0.428**.

So ψ assigns the *segregated, unintegrated* system more than four times the score of the *maximally
integrated* one, while Φ assigns the segregated system zero. This is not a small quantitative
discrepancy; it is a sign inversion of the ranking, produced in two and three nodes, by construction.
It is the aggregate null of §4.2 in its purest analytic form, and it shows exactly what ψ responds to:
bias and order in the occupancy distribution — complexity — not irreducibility.

## 5. Discussion

We will argue four claims, in order of increasing strength: that ψ's failure is *structural* and not
fixable by reduction-choice; that the standard defences of the bridge (tautology, fair-target,
wrong-version) each fail on the evidence above; that what survives is a real but strictly bounded
duality; and that the only live route to an IIT–FEP connection runs through learning dynamics, with
consequences for how the field should treat complexity-based correlates of consciousness.

### 5.1 The failure is structural: a self-divergence cannot be made into an irreducibility measure

The cleanest way to see why ψ cannot track Φ is to notice what §4.3 established and §4.8 dramatised:
the problem is not the *absence* of a partition but the *type* of the quantity. Φ is irreducibility —
information the whole specifies that its parts cannot. Any measure of irreducibility must be, at
bottom, a comparison of a *joint* object to a *factorised* one: the whole's cause–effect structure
versus the product of its parts'. Mutual information is exactly such a comparison — I(X;Y) is the KL
divergence of a joint from the product of its marginals — which is why partitioning a mutual
information (Φ_WMS) exposes integration, and why it tracks Φ at ρ = 0.58.

ψ is not that kind of object. ψ = D_KL(π ‖ µ) is the divergence of *one* distribution from a
*reference derived from the same dynamics*. It has the mathematical form of a divergence, but both
arguments are properties of the single, undivided system; there is no second system, no parts, nothing
being held apart and compared. When you then partition ψ — when you compute ϕ_ψ — you are subtracting
self-divergences of sub-chains from the self-divergence of the whole, and there is no reason on earth
why that difference should equal the irreducibility of anything. Empirically it does not; it
anti-correlates. We therefore make the strong claim and defend it: **no partition-free scalar built
from whole-system entropies can track Φ, and bolting a partition onto the wrong kind of scalar does
not fix it — you must partition a quantity that is already a joint-versus-factorised comparison, and ψ
is not one.** This is why we titled the paper as we did. ψ is a complexity measure — a measure of how
far a system's occupancy departs from maximal noncommittal spread — and complexity is not integration.
The two coincide in special cases and dissociate in general, exactly as systems A and B show.

This is a claim about the algebra, not about our particular ensemble, which is why we are willing to
state it generally. The ensemble's role was to *demonstrate* the structural fact and to rule out the
escape hatches; it was not the source of the conclusion.

### 5.2 The tautology objection cuts the other way

A sceptic will say: "Of course the measures with a partition track Φ and the ones without it don't —
you have confirmed that Φ has a partition. This is arithmetic, not science." We take the objection
seriously and answer it directly, because answering it sharpens the contribution.

First, it is not arithmetic, because nothing guaranteed that ψ lacked an *effective* partition.
Kearney's whole point is that ψ is derived from the *same* constrained-maximum-entropy principle that
he uses to reconstruct IIT's repertoires. A reasonable and serious hypothesis — H1, which we
pre-registered — was that this shared origin would endow the scalar with integration-tracking
behaviour even without an explicit cut, because the MaxCal reference µ already encodes the system's
branching structure. That hypothesis was not silly; it was the bridge's best case. We tested it and it
lost. Discovering that a quantity which *was derived to be close to IIT* nonetheless fails to track
IIT's central number is a substantive empirical result, not a restatement of definitions.

Second, the ϕ_ψ result is precisely what defeats the tautology charge. We did not merely note that ψ
lacks a partition and stop. We *added* the partition — the identical one that makes Φ_WMS work — and
ψ still failed. If "has a partition ⇒ tracks Φ" were the tautology, ϕ_ψ would track Φ. It does the
reverse. So the real content of our finding is not "partitions matter" (granted) but "**the base
quantity must be a mutual-information-type comparison, and the MaxCal deviation is not one, so the
MaxCal bridge cannot reach Φ even when handed IIT's own partition machinery.**" That is a claim with
teeth, and it is the opposite of trivial.

### 5.3 The "you tested a degenerate limit" objection, and where the burden lies

The most sophisticated defence is that we tested the cheap stationary scalar rather than the
repertoire-level construction that carries Kearney's integration content, so we refuted a degenerate
limit, not the theory. We have three responses, and we think they are decisive together.

(i) We did not only test the scalar. ϕ_ψ *is* a repertoire/partition-level MaxCal integration measure,
constructed on the same footing as IIT's MIP, and it fails worse than the scalar. The defence that
"the integration lives in the partition step" is exactly the defence ϕ_ψ was built to test, and it
does not survive contact with the data.

(ii) The burden of proof is on the bridge, not on us. Kearney offers ψ as the quantity that connects
the frameworks and explicitly asks for it to be tied to IIT's metrics. A bridge that turns out to
connect to Φ only via some further, unspecified construction that its author has not exhibited and
that we could not make work is, until that construction is produced and shown to track Φ, an
unvalidated bridge. We have tested the two most natural cash-values of the proposal — the scalar the
paper actually gives, and the partition-augmented version one would build next — and both miss. It is
not the critic's job to keep inventing rescues; it is the proposer's job to deliver one that works.

(iii) The system-level duality, which *is* proven, is system-level *by its nature* (§2.3), so the
expectation that a system-level scalar should descend to Φ was never licensed by the mathematics in
the first place. The degenerate-limit framing has it backwards: the stationary scalar is not an
impoverished shadow of an integration quantity that lives upstairs; it is a faithful expression of a
duality that simply is not about irreducibility. There is no upstairs.

### 5.4 The version objection is empirically closed

We pre-empted the "you used 4.0, he derived 3.0" objection by computing 3.0 directly (§4.4). ψ misses
3.0 (ρ = 0.11) by the same margin it misses 4.0 (ρ = 0.10), and 3.0 and 4.0 agree with each other
(ρ = 0.86). The reason is the one from §2.1: 3.0 and 4.0 differ in their *distance* (EMD vs intrinsic
difference) but share the *partition-and-exclusion* skeleton, and it is that skeleton, not the
distance, that ψ lacks. Swapping EMD for ID changes which integrated systems score how much; it does
not conjure a partition into a partition-free scalar. The version of IIT is a red herring for this
question, and now we have shown it empirically rather than merely argued it.

### 5.5 What survives: a real duality, strictly bounded, and the learning-dynamics escape hatch

None of this refutes the MaxCal–FEP duality at the level Ramstead et al. (2023) actually prove it.
That result — free energy ↔ constrained entropy, at the system's steady state — stands, and Kearney's
re-expression of IIT's repertoire calculus in MaxCal terms may well be correct as a piece of
*construction*. What we have bounded is the *reach* of the duality as a claim about consciousness. The
duality buys you a system-level correspondence between two scalar descriptions of the same steady
state. It does not buy you Φ, because Φ is not a system-level scalar in the relevant sense — it is the
output of a partition-and-maximisation over the system's decomposition, and the duality is silent on
decomposition. We will put this provocatively: **the proven part of the bridge is real but, with
respect to consciousness, nearly vacuous, because it lives entirely on the side of the divide (whole-
system thermodynamics) that IIT says is *not* where consciousness's quantity comes from.** Integration
is about the cut; the duality is about the whole; and you cannot get the cut from the whole.

There is exactly one escape hatch we find credible, and we flag it as the productive direction rather
than a face-saving caveat. The empirical Φ–surprise couplings that motivate this whole programme —
Lundbak Olesen et al. (2023), Mayama et al. (2025) — are not observed in static stationary systems.
They are observed in systems that *learn*: cultures and agents reorganising their cause–effect
structure over time as they reduce prediction error. Our test, like Kearney's scalar, is synchronic —
it scores a fixed TPM at its stationary distribution. It is entirely possible, and consistent with
everything here, that the genuine relationship is *diachronic*: that as a system minimises free energy
*over learning time* it tends to build more integrated cause–effect structure, so that ΔΦ correlates
with the trajectory of surprise even though instantaneous ψ does not correlate with instantaneous Φ.
If so, the right bridge quantity is not ψ(π) but something like dψ/dt versus dΦ/dt along a learning
trajectory. That is a real, testable proposal, and it is the one we would pursue next. But notice it
concedes our point: the *static scalar* ψ is not the bridge to Φ. At most, its rate of change might
shadow Φ's rate of change for dynamical reasons that have nothing to do with ψ being an integration
measure — because it is not one.

### 5.6 Implications: validate proxies, and stop equating complexity with consciousness

Two broader morals. First, methodological: this is a worked example of why the field cannot accept
candidate consciousness measures on the strength of an elegant derivation. ψ has an impeccable
pedigree — a variational principle, a proven duality, a re-derivation of IIT's own machinery — and it
still does not track the thing it is offered to connect to. The only way to know that was to compute
exact Φ and look. Wherever exact Φ is available, proxies and bridge quantities should be made to earn
their status there (Barrett et al. 2026), and our exact-Φ apparatus is one way to do it routinely.

Second, conceptual, and we will take the position squarely: ψ joins total correlation and i(π) in the
class of *complexity* measures — quantities sensitive to order, bias, and predictability in a system's
behaviour — and the persistent temptation to treat such quantities as measures of consciousness should
be resisted. Systems A and B of §4.8 are the cautionary tale in miniature: a biased, segregated,
"complex-looking" system can score high on a complexity measure while specifying *no* integrated
cause–effect structure at all, and a maximally integrated system can look bland to the same measure.
If IIT is even approximately right about what matters, then complexity and consciousness come apart
exactly where it counts, and a measure that cannot tell System A from System B is not a measure of
consciousness whatever else it may be good for. This is not a knock on ψ as a *complexity* statistic —
it may be an excellent one, and the MaxCal framework is valuable on its own terms. It is a boundary
line, drawn where the evidence draws it.

## 6. Limitations

We are candid about what the study does not show, and about why the limitations do not rescue H1.

**Scope of the systems.** The networks are small (n ∈ {3,4}), binary, and Boolean-gated. This is
forced by the exact-Φ oracle and is the price of testing against ground truth rather than a proxy. We
do not claim the *numbers* generalise to large or biological systems. But the *structural* argument of
§5.1 does not depend on size or gate type: it depends on ψ being a self-divergence, which it is at any
scale. A larger ensemble could move ρ from 0.09 to 0.2; it could not turn a complexity measure into an
integration measure.

**Ergodicity.** ψ is defined only for ergodic chains, so 89/270 networks are excluded, and our
ergodicity screen is a practical reducibility/periodicity filter rather than a complete aperiodicity
certificate. Many biological and conscious states are metastable or transient, a regime where ψ is
simply undefined while Φ is not — itself a point against ψ as a general consciousness measure, but one
we do not lean on.

**The 3.0 comparator is n = 3 only**, owing to an EMD shape error in this 4.0-oriented PyPhi checkout
(§3.6). We judge the n = 3 evidence sufficient given that it already shows ψ missing 3.0 by the 4.0
margin, and that 3.0 ≈ 4.0; a complete n = 4 3.0 sweep is nonetheless an obvious tidy-up for a revised
version with a 3.0-configured PyPhi build.

**Aggregation and clamping.** We aggregate state-dependent Φ to a single number and clamp negatives to
zero. We mitigated the first by reporting three aggregations (all null for ψ); the clamping matches
IIT's treatment of reducible systems and compresses a tail rather than creating the null.

**We tested ψ, not the full Φ-structure.** Our ground truth is scalar system Φ, not the complete
unfolded structure of distinctions and relations. A bridge to the *structure* (rather than to the
scalar) is a different and harder question that our apparatus does not yet address, and Kearney's
repertoire-level derivation properly belongs to that question — which is why we have been careful to
say our result does not touch it.

## 7. Conclusion

We ran the test Kearney (2026) called for and did not run, and then we ran the tests his defenders
would call for next. On systems where Φ is exactly computable, the maximum-caliber information ψ does
not track integrated information (ρ ≈ 0.09, detection at chance, stable across five seeds, robust to
aggregation, absent in every stratum). Giving ψ IIT's own partition step does not rescue it — the
resulting ϕ_ψ anti-correlates with Φ (ρ = −0.28) while the identical partition on a mutual information
tracks Φ at ρ = 0.58. ψ misses IIT 3.0 (the version it was derived from) and IIT 4.0 alike, and the
two versions agree with each other, so the result does not hinge on which IIT one means. Two minimal
hand-built systems show ψ ranking an unintegrated system above a maximally integrated one. We have
argued that this is not a defect to be patched by a cleverer reduction but a structural fact: ψ is a
self-divergence — a complexity quantity — and complexity is not integration, partition step or no
partition step. The MaxCal–FEP duality is real where it is proven, at the level of whole-system
thermodynamics, and that is exactly the level at which IIT says the quantity of consciousness does
*not* live. The honest bridge between IIT and the FEP, if there is one, will be built not from a
static scalar but from the dynamics of learning — and that is the experiment we would do next.

## Data and code availability

All code, data, figures, the literature corpus, and per-paper notes are at
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`psi_vs_phi/`). Reproduce end-to-end:
`python -m psi_vs_phi.psi` (ψ controls), `python -m psi_vs_phi.run 15 <seed>` (dataset, seeds 1–5),
`python -m psi_vs_phi.exact_phi3 15 1` (IIT-3.0 comparator, n=3), `python -m psi_vs_phi.dissociation`
(analytic cases), `python -m psi_vs_phi.analyze` (all statistics), `python -m psi_vs_phi.figures`
(figures), built on the exact IIT-4.0 Φ oracle in `proxy_audit/`. For a citable archive, the release
will be deposited at a Zenodo DOI and the frozen tag cited in the final version.

## Acknowledgments

This study was developed with AI assistance (Anthropic's Claude) for code, analysis, and drafting; all
scientific claims were checked against computed results, and the exact-Φ oracle and candidate-measure
framework reused here were built in the companion `iit-experiments` study. We thank A. Kearney for
posting the motivating preprint openly; this response is offered collegially and a courtesy copy will
be sent.

## References

Citations resolve to `literature/references.bib`. Key sources:

- Albantakis, L., Barbosa, L., Findlay, G., et al. (2023). Integrated information theory (IIT) 4.0.
  *PLOS Comput. Biol.* 19(10):e1011465. (arXiv:2212.14787)
- Ay, N. (2001/2015). Information geometry on complexity and stochastic interaction. *Entropy*
  17(4):2432–2458.
- Balduzzi, D., & Tononi, G. (2008). Integrated information in discrete dynamical systems. *PLOS
  Comput. Biol.* 4(6):e1000091.
- Barrett, A. B., & Seth, A. K. (2011). Practical measures of integrated information for
  time-series data. *PLOS Comput. Biol.* 7(1):e1001052.
- Barrett, A. B., Milinkovic, M., Mediano, P. A. M., Rosas, F. E., Bor, D., Barnett, L., & Seth, A. K.
  (2026). Integrated information theory: the good, the bad and the misunderstood. arXiv:2604.11482.
- Dixit, P. D., et al. (2018). Maximum caliber is a general variational principle for dynamical
  systems. *J. Chem. Phys.* 148:010901. (arXiv:1711.03450)
- Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019). The unfolding argument. *Conscious.
  Cogn.* 72:49–59.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.*
  11:127–138.
- Friston, K., et al. (2019). A free energy principle for a particular physics. arXiv:1906.10184.
- Hanson, J. R., & Walker, S. I. (2021). Formalizing falsification for theories of consciousness.
  *Neurosci. Conscious.* 2021(2):niab014. (arXiv:2006.07390)
- Kearney, A. (2026). Information as Maximum-Caliber Deviation: A bridge between Integrated Information
  Theory and the Free Energy Principle. arXiv:2605.12536.
- Lundbak Olesen, C., Waade, P. T., Albantakis, L., & Mathys, C. (2023). Phi fluctuates with
  surprisal. *PLOS Comput. Biol.* 19(10):e1011346.
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
