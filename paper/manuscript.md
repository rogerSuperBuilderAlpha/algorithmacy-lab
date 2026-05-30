# What tracks integrated information? Validating Φ proxies and candidate measures against exact IIT‑4.0 Φ

*A short empirical note. Code and data: https://github.com/rogerSuperBuilderAlpha/iit-experiments*

## Abstract

Integrated Information Theory (IIT) defines a quantity Φ that is intractable to
compute for systems of any appreciable size, so empirical and theoretical work
relies on cheaper *proxies* and *candidate measures*. These stand‑ins have rarely
been validated against the Φ they approximate, because exact Φ was out of reach
[1]. Using the IIT‑4.0 implementation in PyPhi [2,3], we compute exact Φ on
ensembles of small binary networks and ask, systematically, what tracks it. We
find: (i) empirical proxies (Lempel‑Ziv complexity, correlation) do not track Φ
and can anti‑correlate with it; (ii) theoretically‑motivated candidate measures
do better but only moderately, with whole‑minus‑sum Φ the best single measure and
improving with system size; (iii) even *exact* scalar Φ is nearly orthogonal to
the cause‑effect *structure* it summarizes, supporting a multi‑dimensional view
[1]; and (iv) a model that *combines* cheap features recovers much of Φ and
detects integrated systems with AUC 0.90, with detection — but not magnitude —
extrapolating to larger unseen systems. The unifying observation is that no
single cheap number is integrated information, but the information needed to
recover it is distributed across several cheap signals, and measures that share
IIT's "whole‑minus‑parts" structure carry the most of it.

## 1. Motivation

IIT [4] proposes that the integrated information Φ of a system characterizes its
intrinsic, irreducible cause‑effect power. Computing Φ exactly requires searching
over partitions and is super‑exponential in system size; even the most careful
empirical applications therefore compute proxies — perturbational complexity,
Lempel‑Ziv complexity, correlation‑based integration — or candidate measures
formulated to be tractable. A recent review [1] makes the sharp observation that
these quantities are *proxies that have never been validated against Φ*, and
proposes replacing the single number Φ with a multi‑dimensional suite.

Validation is possible on systems small enough that exact Φ is computable. The
IIT‑4.0 formalism is implemented in PyPhi [2,3], and 3–4 node networks are well
within reach. We use this to run six connected validation experiments.

## 2. Methods

**Systems.** Random binary networks of `n` nodes, each updating as a (possibly
noisy) Boolean gate — OR, AND, PARITY, MAJORITY, or COPY — of the nodes that
connect to it. We sweep connectivity density `{0.3, 0.5, 0.8}` and per‑node noise
`{0.0, 0.05, 0.2}`, which spans sparse↔dense and deterministic↔stochastic regimes
and yields a broad range of Φ.

**Ground truth.** Exact IIT‑4.0 system integrated information via
`pyphi.new_big_phi.sia`. Φ is state‑dependent; for a per‑network value we take the
mean over the network's reachable states. Negative system Φ denotes a reducible
system and is clamped to zero. Experiment 3 instead analyzes each
`(network, state)` pair separately.

**Measures.** Empirical proxies (Lempel‑Ziv complexity of a simulated trajectory,
mean pairwise correlation, total correlation, edge count) and candidate measures
(whole‑minus‑sum Φ [5], stochastic interaction [6], causal density [7], a
co‑information "integrated synergy", time‑delayed mutual information), all
computed exactly from the network's stationary distribution and time‑lagged
joint. Candidate measures sharing IIT's partition structure are evaluated over
the minimum‑information bipartition. Each measure is unit‑checked on known systems
(independent units → 0; XOR → zero pairwise causal density).

## 3. Results

**(1) Empirical proxies do not track Φ.** Across 270 networks, the strongest
association of any empirical proxy with Φ is total correlation at Spearman
ρ = −0.36 — the wrong sign. Lempel‑Ziv complexity is near chance at detecting
Φ > 0 (AUC 0.57). The best single detector of integration is a trivial edge count
(AUC 0.64). Relationships are non‑monotonic and even change sign between detecting
integration and grading it.

**(2) Candidate measures do better, but only moderately.** On the same networks,
whole‑minus‑sum Φ leads (ρ = 0.47, AUC 0.79) and *strengthens with system size*
(ρ 0.41 → 0.55 from n=3 to n=4); integrated synergy is second. Measures of mere
statistical dependence (total correlation, time‑delayed mutual information)
anti‑correlate. The measures that share IIT's whole‑minus‑parts structure are the
ones that track Φ, and they clearly outperform the empirical proxies (best
AUC 0.79 vs 0.64).

**(3) Scalar Φ is an impoverished summary.** Extracting the full Φ‑structure
(distinctions, relations, mechanism‑order composition) for 372 `(network, state)`
pairs, scalar Φ is nearly orthogonal to every structural dimension
(ρ = 0.07–0.21). Reducible systems (Φ = 0) nonetheless possess rich structure —
all of them have at least one distinction. The suite reduces to roughly three
independent axes — integration (Φ), structural size, and composition — of which Φ
is only one. This is concrete support for the multi‑dimensional characterization
proposed in [1].

**(4) Combined cheap features recover Φ; detection extrapolates.** On 720
networks, a random forest combining the cheap features predicts Φ with
out‑of‑fold ρ = 0.54 (vs 0.32 for the best single feature) and detects Φ > 0 with
AUC 0.90 (vs 0.69). Whole‑minus‑sum Φ dominates feature importance; the
non‑linear model beats a linear one, indicating the features relate to Φ through
interactions. Trained on `n ∈ {3,4}` and applied to a fresh unseen `n=5` set,
*detection* holds up (AUC 0.84) while *magnitude* prediction degrades (ρ 0.33).
Cheap surrogates thus appear usable for screening integration across scales, but
not yet for accurate Φ estimation — a testable caution for the surrogate program
exemplified by recent graph‑neural‑network work [8] (which targeted IIT 3.0
without exact PyPhi ground truth) and scalable estimators such as M‑information
[9].

**(5) A neighbouring framework diverges from Φ.** Comparing Hoel's effective
information and causal emergence to Φ on 180 n=3 systems (with the
coarse-graining search done exactly), causal emergence is nearly orthogonal to Φ
(ρ = 0.02), and the most integrated systems show no causal emergence at all —
emergence rewards degeneracy (a coarse-graining recovers determinism) whereas Φ
rewards irreducibility. Effective information, Φ's precursor, tracks Φ only
*among already-integrated systems* (ρ = 0.77), not whether integration occurs.

**(6) Estimating the best measure from data roughly halves its tracking.** On
real data, integration is not computed exactly from a TPM but estimated from a
finite time series via Integrated Information Decomposition (ΦID) [10]. Computing
the revised Φ_R from simulated trajectories with the `phyid` package — using the
CCS redundancy, since MMI assigns spurious synergy to independent variables — its
tracking of exact Φ falls by about half relative to the exact whole-minus-sum on
the same networks (ρ 0.28 → 0.12; AUC 0.67 → 0.56). Exact and estimated measures
agree at ρ = 0.64, so this is an estimation gap (finite samples, coarse-graining),
not a conceptual mismatch — a concrete caution for inferring integration from
data-side ΦID.

## 4. Discussion

The six results cohere into one statement: *no single cheap number is integrated
information, but the information needed to recover it is distributed across
several cheap signals, and the closer a measure's structure is to IIT's own
whole‑minus‑parts move, the more of that information it carries.* For empirical
practice this is a caution — popular proxies need not track Φ. For measure design
it is encouraging — whole‑minus‑sum measures track Φ best and improve with size,
and combinations recover much of it. For theory it supports moving beyond a single
Φ to a structural characterization.

## 5. Limitations

These are small systems (`n ≤ 5`) with a specific Boolean‑gate dynamics; the
regime where exact Φ is computable is precisely the regime that cannot directly
inform us about large or biological systems. Generalization is the open problem,
and we release the exact‑Φ feature datasets (n=3,4 and n=5) so others can probe
it. We use system‑level Φ summarized over reachable states; per‑state and
Φ‑structure‑level analyses may differ. Several candidate measures requiring
numerical optimization — geometric Φ, Φ*, decoding‑Φ, full ΦID, M‑information —
are deferred and may rank differently. Relation counts in Experiment 3 carry a
congruence caveat documented with that experiment.

## Reproducibility

All experiments are self‑contained Python packages with `run`/`build` and
`analyze` entry points, sharing one ensemble generator and the IIT‑4.0 PyPhi
line. See the repository for code, data, figures, and per‑experiment writeups.

## References

[1] A. B. Barrett et al. *Integrated information theory: the good, the bad and
the misunderstood* (2026).
[2] W. G. P. Mayner et al. *PyPhi: A toolbox for integrated information theory.*
PLOS Comput. Biol. 14(7):e1006343 (2018).
[3] L. Albantakis et al. *Integrated information theory (IIT) 4.0.* PLOS Comput.
Biol. 19(10):e1011465 (2023).
[4] G. Tononi. *An information integration theory of consciousness.* BMC
Neuroscience 5:42 (2004).
[5] D. Balduzzi & G. Tononi. *Integrated information in discrete dynamical
systems.* PLOS Comput. Biol. 4(6):e1000091 (2008).
[6] N. Ay. *Information geometry on complexity and stochastic interaction.* MPI
MIS preprint (2001); Entropy 17 (2015).
[7] A. K. Seth. *Causal density and integrated information as measures of
conscious level.* Phil. Trans. R. Soc. A (2008).
[8] T. Hosaka. *Graph neural networks for integrated information and major complex
estimation.* PLOS One 20(11):e0335966 (2025).
[9] A. Liardi et al. *A scalable estimator of high‑order information in complex
dynamical systems.* arXiv:2506.18498 (2025).
[10] P. A. M. Mediano, A. K. Seth & A. B. Barrett. *Measuring integrated
information: comparing candidate measures.* Entropy 21(5):525 (2019).

*Note: reference details are provided for orientation; verify against the
original sources before citing.*
