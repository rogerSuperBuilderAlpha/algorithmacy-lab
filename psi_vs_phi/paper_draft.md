# Does maximum-caliber information track integrated information? A direct test of ψ against exact IIT-4.0 Φ

**Roger Hunt**
*Preprint draft. Code and data: https://github.com/rogerSuperBuilderAlpha/iit-experiments (psi_vs_phi/).
Citations are author–year and resolve to `literature/references.bib`.*

---

## Abstract

Integrated Information Theory (IIT) and the Free Energy Principle (FEP) are the two most ambitious
mathematical frameworks for, respectively, the structure of consciousness and the dynamics of
self-organization. Kearney (2026) recently proposed a rigorous bridge between them: defining
information ψ as the deviation of a system's realized dynamics from a constrained maximum-caliber
(MaxCal) path ensemble, he re-derives IIT 3.0's cause-effect repertoires from this principle and
links ψ to prediction error and the FEP. Crucially, ψ is never compared against integrated
information Φ — the quantity it purports to bridge — and the paper explicitly calls for that test.
We perform it. On an ensemble of small discrete networks where exact IIT-4.0 Φ is computable, we
implement the system-level scalar ψ(π) = log₂κ − H(π) − h(π) (validated against the paper's own
worked cases), and correlate it with exact Φ. **ψ does not track Φ:** across 181 ergodic networks,
Spearman ρ = 0.085 (95% CI [−0.08, +0.24], including zero; detection AUC = 0.52, chance), stable
across two seeds. ψ ranks near the bottom of a leaderboard of candidate measures, while the
whole-minus-sum Φ — which contains a partition step — tracks Φ at ρ = 0.58 on the *same* networks.
The result is the theoretically anticipated one: ψ is built from whole-system entropies with no
partition or exclusion operation, and the proven FEP↔constrained-MaxEnt duality that underwrites
the bridge operates only at the system level, with no analogue of Φ's partition/exclusion
structure. We conclude that the MaxCal–IIT bridge holds at the level it is proven (free energy ↔
constrained entropy) but does not descend to a scalar ψ ≈ Φ relationship. This does not bear on the
separate repertoire-level derivation, which we leave to future work.

---

## 1. Introduction

IIT identifies a conscious system with the irreducible cause-effect structure it specifies,
quantified by integrated information Φ (Tononi 2004; Oizumi, Albantakis & Tononi 2014; Albantakis et
al. 2023). The FEP holds that any system individuated from its environment by a Markov blanket
minimizes variational free energy, an upper bound on surprise (Friston 2010, 2019). The two have
been linked conceptually and empirically (Safron 2020; Olesen & Waade 2023; Mayama et al. 2025), but
a rigorous mathematical mapping was missing — limiting, as Kearney (2026) notes, the precision and
testability of the connection.

Kearney supplies such a mapping through maximum caliber (MaxCal), the dynamical generalization of
maximum entropy (Pressé et al. 2013; Dixit et al. 2018): he defines information **ψ** as the
deviation of a system's realized dynamics from a constrained MaxCal path ensemble, re-derives IIT
3.0's cause-effect repertoires from this constrained-maximum-entropy principle, and shows ψ equals
prediction error in appropriate limits. For a stationary ergodic Markov chain the proposal reduces
to a cheap scalar, ψ(π) = log₂κ − H(π) − h(π). However, **ψ is never compared to integrated
information Φ itself**, and the paper explicitly calls for that work: "the explanatory power of our
proposal here remains unconfirmed. Experimental or theoretical work must be conducted to … connect
the metrics observed here to those in IIT."

We close that gap. Building on a validation framework in which exact IIT-4.0 Φ is computed for small
systems, we add ψ as a candidate measure and ask directly whether it tracks exact Φ. Our
contribution is (i) the first direct numerical test of ψ against exact IIT-4.0 Φ, with ψ
implemented exactly from the paper's definition and validated on its own controls; and (ii) a clear,
robust answer — ψ does not track Φ — situated against a leaderboard of candidate measures on
identical systems and explained by the structural mismatch between ψ and Φ.

## 2. Background

**IIT and its measurement problem.** IIT 3.0 (Oizumi et al. 2014) operationalizes Φ via cause/effect
repertoires scored against an unconstrained baseline by earth-mover's distance, with system-level Φ
over the minimum information partition (MIP). IIT 4.0 (Albantakis et al. 2023) replaces the
difference measure with a unique intrinsic difference and unfolds the structure into distinctions
and relations, yielding the canonical, computable Φ. Yet Φ has never been computed on a real
physical system; what is computed on data are *proxies* (Barrett et al. 2026), and whether those
proxies track Φ has rarely been checked. Prior work in this repository found, on small systems where
exact Φ *is* computable, that empirical proxies do not track Φ and that candidate measures
(Mediano, Seth & Barrett 2019) track it only moderately. The validation target is itself contested:
the strong-vs-weak-IIT distinction (Mediano et al. 2022), the unfolding argument (Doerig et al.
2019), and formal falsifiability analyses (Hanson & Walker 2021) all bear on what a measure should
be validated against.

**FEP, MaxCal, and the bridge.** The FEP can be cast as a path-integral principle over trajectories
(Friston 2019), the natural meeting point with path-ensemble methods. MaxCal maximizes path entropy
over trajectories subject to dynamical constraints (Dixit et al. 2018). Ramstead et al. (2023)
*prove* a duality between the FEP and the constrained maximum-entropy principle — asymptotically,
under non-equilibrium-steady-state / Markov-blanket assumptions — which makes a MaxCal→FEP bridge
coherent at the system level. Notably, this proven duality relates free energy to constrained
entropy and contains no analogue of Φ's partition, exclusion, or maximization structure.

**Prior IIT–FEP unifications.** Safron's IWMT (2020) is conceptual; Olesen & Waade (2023) report
that Φ fluctuates with surprisal; Mayama et al. (2025) describe a "hill-shaped Φ trajectory" in
adapting neuronal cultures. None supplies a rigorous mapping, and none computes a candidate bridge
quantity against exact Φ — the gap Kearney's derivation targets and that we test.

## 3. Methods

**Design.** A within-ensemble measure-validation study: for each network we compute exact IIT-4.0 Φ
(ground truth) and the candidate maximum-caliber information ψ, then quantify how well ψ tracks Φ.
Hypotheses were fixed in advance: **H1**, ψ tracks Φ; **H0**, ψ tracks order/disorder complexity but
not integration.

**System ensemble.** Networks of *n* binary units, each updating as a (possibly noisy) Boolean gate
(OR, AND, PARITY, MAJORITY, COPY) of its inputs, giving a state-by-node transition probability
matrix (TPM). We swept connectivity density and per-node noise and used *n* ∈ {3,4} with 15 networks
per (density, noise) cell (270 networks), under fixed seeds, reusing the generator
`proxy_audit.networks.generate_ensemble`. ψ is defined only for ergodic, homogeneous Markov chains,
so each chain's state-by-state TPM was tested for ergodicity (agreement of power-iteration
stationary distributions from a uniform and a one-hot start) and the primary analysis restricted to
the ergodic subset.

**Ground truth.** Φ was computed exactly with PyPhi's IIT-4.0 implementation
(`pyphi.new_big_phi.sia`), summarizing each network by the mean exact Φ over its reachable states
(negative system Φ, denoting a reducible system, clamped to 0), via the oracle
`proxy_audit.exact_phi`.

**Measure under test.** Transcribed exactly from Kearney §5.1–5.2: the per-state perplexity
PP(x) = 2^{H(P(x,·))}, the partition constant κ = Σₓ PP(x), the MaxCal input marginal µ(x) = PP(x)/κ,
and ψ(π) = log₂κ − H(π) − h(π) = D_KL(π ‖ µ) (Kearney eq. 5.10), where H(π) is the marginal entropy
of the stationary distribution and h(π) = Σₓ π(x)·H(P(x,·)) the entropy rate. We also computed the
companion mutual information i(π) = H(π) − h(π) for ablation. ψ was added to the `candidate_audit`
harness so it is computed and analyzed identically to previously-audited measures.

**Implementation validation (before any ψ–Φ analysis).** We verified ψ ≡ 0 for circulant/uniform
chains (π = µ); ψ = log₂N − H(π) for deterministic permutations; ψ ≥ 0 and exact agreement of the
two equivalent forms (ψ = log₂κ − H − h and the KL form) across random chains (maximum difference
1.3×10⁻¹⁵).

**Analysis.** Spearman ρ, Pearson r, and detection AUC for Φ > 0, of ψ (and i) against exact Φ;
bootstrap 95% confidence intervals; the association restricted to Φ > 0; a per-size split; an
independent second seed; and a leaderboard ranking ψ against the candidate measures (Φ whole-minus-
sum, total correlation, stochastic interaction, causal density, integrated synergy, time-delayed MI)
computed on the identical ergodic networks.

## 4. Results

**ψ is well-defined and behaves as specified.** All controls passed: ψ = 0 for circulant/uniform
chains, ψ = log₂N − H(π) for permutations, ψ ≥ 0 across random chains, and the entropy-form and
KL-form definitions agreed to machine precision. ψ is therefore computed exactly and as defined.

**ψ does not track exact IIT-4.0 Φ.** Of 270 networks, 181 were ergodic (55 with Φ > 0). Across
these, ψ is essentially uncorrelated with Φ: Spearman ρ = 0.085 (95% bootstrap CI [−0.08, +0.24],
not distinguishable from zero), Pearson r = −0.116, and detection AUC = 0.524 (chance). Restricting
to Φ > 0 gives ρ = −0.318. The result is stable: an independent second ensemble gave ρ = 0.052,
AUC = 0.516. The companion i(π) likewise fails (ρ = −0.135), so the absent signal is not hidden in
the mutual-information term. By size, ρ = 0.096 (n=3) and 0.028 (n=4).

**The failure is specific to ψ, not the test (Table 1).** On the identical ergodic networks, the
whole-minus-sum Φ correlates strongly with exact Φ (ρ = 0.580, AUC = 0.860) and integrated synergy
moderately (ρ = 0.479); ψ ranks near the bottom, clustering with the dependence/complexity measures
— total correlation (ρ = −0.373) and i(π) (ρ = −0.135) — that are known not to track Φ. The measures
that succeed are precisely those built on a whole-minus-parts (partition) operation.

**Table 1.** Association with exact IIT-4.0 Φ across the 181 ergodic networks (seed 1).

| measure | Spearman ρ | AUC(Φ>0) |
|---|---:|---:|
| Φ whole-minus-sum | 0.580 | 0.860 |
| integrated synergy | 0.479 | 0.784 |
| total correlation | −0.373 | 0.261 |
| stochastic interaction | 0.136 | 0.573 |
| i(π) = H − h | −0.135 | 0.393 |
| **ψ (maximum-caliber information)** | **0.085** | **0.524** |
| causal density | −0.011 | 0.513 |

## 5. Discussion

**The negative result is the predicted one.** ψ is constructed entirely from whole-system entropies
— the stationary distribution's marginal entropy and entropy rate, measured against a
maximum-caliber reference. It contains no partition and no exclusion. Exact IIT Φ is, by
construction, the irreducibility of the cause-effect structure *across the minimum information
partition*, after an exclusion step selects the maximal substrate. There is therefore no structural
reason for a partition-free scalar to track a partition-defined one, and our data show it does not.
The point is sharpened by the leaderboard: the measures that *do* track Φ here — whole-minus-sum Φ
and the co-information "integrated synergy" — are exactly those that contain a whole-minus-parts
operation. ψ behaves, instead, like the order/disorder complexity quantities (total correlation,
i(π)) that a partition-free construction would be expected to resemble. In short, ψ is a complexity
measure, not an integration measure.

**What this means for the MaxCal–IIT–FEP bridge.** The result does not undermine the bridge at the
level at which it is actually proven. Ramstead et al. (2023) establish a duality between free energy
and constrained entropy at the *system* level; Kearney's contribution is to re-express IIT's
repertoire machinery in MaxCal terms and to relate ψ to surprise. Our finding bounds the bridge: the
system-level maximum-caliber information is not a proxy for integrated information. The two
frameworks may still be deeply related — IIT and the FEP can co-vary, and Olesen & Waade (2023) and
Mayama et al. (2025) report empirical Φ–surprise coupling in dynamic, learning systems — but that
coupling, if real, is not captured by a static, system-level MaxCal scalar on these ensembles. A
natural reconciliation is that Φ–surprise relationships observed empirically are mediated by the
*dynamics of learning* (a system reorganizing its cause-effect structure as it reduces surprise),
which a single stationary ψ does not encode.

**Relation to the measurement-validation literature.** Our result extends a consistent pattern: on
small systems where exact Φ is computable, measures that lack IIT's partition structure — empirical
proxies, total correlation, and now ψ — fail to track Φ, while partition-based candidate measures
track it moderately. This both supports the case (Barrett et al. 2026) that proxies must be
validated rather than assumed, and provides a concrete, falsifiable use of the exact-Φ framework:
it can adjudicate a live theoretical proposal. It also illustrates the strong-vs-weak IIT
distinction (Mediano et al. 2022) in action — ψ might still serve weak-IIT, correlational purposes
in some regimes even though it does not track the strong-IIT canonical Φ.

**What the result does and does not establish.** It answers, negatively, the specific empirical
question Kearney raised about the system-level scalar ψ. It does *not* refute his repertoire-level
derivation — the claim that IIT 3.0's cause/effect repertoire calculus can be re-expressed via
constrained maximum entropy — which is a structural statement about the construction, distinct from
whether the resulting scalar proxies Φ. Testing that derivation directly, and against IIT 4.0's
intrinsic-difference repertoires, is the natural next study.

## 6. Limitations

ψ is defined only for ergodic, homogeneous Markov chains; our primary analysis is the 181/270
ergodic networks, with non-ergodic networks flagged and excluded. The systems are small (n ∈ {3,4})
and drawn from a specific Boolean-gate ensemble; generalization to large or biological systems is
not claimed (and is precisely the regime where exact Φ is unavailable). Kearney re-derives IIT
**3.0** repertoires (earth-mover's distance), whereas we validate against canonical IIT **4.0** Φ
(intrinsic difference); the near-zero correlation is, however, not a subtle measure-choice effect —
ψ is near-orthogonal to Φ and to the broad integration signal regardless of measure details. We
tested the **system-level stationary** ψ — the cheap scalar the paper provides — not the full
constrained-maximum-entropy repertoire construction, and we compared against scalar system Φ rather
than the full Φ-structure (distinctions and relations).

## 7. Conclusion

We performed the test that Kearney (2026) called for and did not run: a direct numerical comparison
of the maximum-caliber information ψ against exact IIT-4.0 Φ. On systems where Φ is exactly
computable, ψ does not track Φ (ρ ≈ 0.05–0.09, detection at chance, stable across seeds), ranking
near the bottom of a candidate-measure leaderboard while partition-based measures succeed. The
maximum-caliber information is a complexity-type quantity, not an integration measure — the outcome
anticipated by the fact that the FEP↔maximum-entropy duality underwriting the bridge operates at the
system level with no analogue of Φ's partition-and-exclusion structure. The MaxCal–IIT–FEP bridge
holds where it is proven, but does not descend to ψ ≈ Φ. Whether the repertoire-level derivation
fares differently, and whether learning dynamics (rather than a static scalar) mediate the empirical
Φ–surprise coupling, are the questions we leave open.

## Data and code availability

All code, data, figures, the literature corpus, and per-paper notes are available at
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`psi_vs_phi/`). The study is reproducible
end-to-end: `python -m psi_vs_phi.psi` (controls), `python -m psi_vs_phi.run 15 1` (dataset),
`python -m psi_vs_phi.analyze` (analysis), built on the exact IIT-4.0 Φ oracle in `proxy_audit/`.

## Acknowledgments

This study was developed with AI assistance (Claude). The exact-Φ oracle and candidate-measure
framework reused here were built in the companion `iit-experiments` study.

## References

Citations resolve to `literature/references.bib`. Key sources:

- Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLOS Comput. Biol.*
  19(10):e1011465. doi:10.1371/journal.pcbi.1011465. (arXiv:2212.14787)
- Barrett, A. B., et al. (2026). Integrated information theory: the good, the bad and the
  misunderstood. arXiv:2604.11482.
- Dixit, P. D., et al. (2018). Maximum caliber is a general variational principle for dynamical
  systems. *J. Chem. Phys.* 148:010901. arXiv:1711.03450.
- Doerig, A., et al. (2019). The unfolding argument. *Conscious. Cogn.* 72:49–59.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.*
  11:127–138.
- Friston, K. (2019). A free energy principle for a particular physics. arXiv:1906.10184.
- Hanson, J. R., & Walker, S. I. (2021). Formalizing falsification for theories of consciousness.
  *Neurosci. Conscious.* 2021(2):niab014. arXiv:2006.07390.
- Kearney, A. (2026). Information as Maximum-Caliber Deviation: A bridge between IIT and the FEP.
  arXiv:2605.12536.
- Mayama, T., et al. (2025). Bridging integrated information theory and the free-energy principle in
  living neuronal networks. arXiv:2510.04084.
- Mediano, P. A. M., Seth, A. K., & Barrett, A. B. (2019). Measuring Integrated Information.
  *Entropy* 21(1):17.
- Mediano, P. A. M., et al. (2022). The strength of weak integrated information theory. *Trends Cogn.
  Sci.* 26(8):646–655.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
  consciousness: IIT 3.0. *PLOS Comput. Biol.* 10(5):e1003588.
- Olesen, C. L., Waade, P. T., Albantakis, L., & Mathys, C. (2023). Phi fluctuates with surprisal.
  *PLOS Comput. Biol.* doi:10.1371/journal.pcbi.1011346.
- Pressé, S., et al. (2013). Principles of maximum entropy and maximum caliber in statistical
  physics. *Rev. Mod. Phys.* 85:1115.
- Ramstead, M. J. D., et al. (2023). On Bayesian Mechanics. *Interface Focus* 13(3):20220029.
  arXiv:2205.11543.
- Safron, A. (2020). An Integrated World Modeling Theory (IWMT) of Consciousness. *Front. Artif.
  Intell.* 3. doi:10.3389/frai.2020.00030.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neurosci.* 5:42.
