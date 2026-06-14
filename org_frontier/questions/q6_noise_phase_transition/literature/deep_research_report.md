# Does Φ undergo a phase transition as commit noise rises, or only smooth decay?

Deep-research run, June 2026. Five search angles across the IIT-criticality, coordination-dynamics,
and IIT-measurement literatures. 21 primary sources fetched, claims extracted, 15 verified by 3-vote
adversarial check. Every load-bearing source is peer-reviewed (PLOS, Nature/Scientific Reports, MDPI
Entropy, American Journal of Physiology) or a primary thesis. No blog or forum source is load-bearing.

The question: for a triadic conjunctive mediated form, is the dyadic/triadic verdict transition in
Φ_MIP sharp (a threshold/phase transition in Φ or its derivative) or gradual as the mediator's commit
flips with probability p? And what does the literature establish about Φ versus a noise-like control
parameter more generally?

The short answer the literature supports: both behaviors exist, and which one shows up is conditional.
Φ decays smoothly and monotonically toward zero when noise washes out a coupling in continuous linear
models, but Φ and its susceptibility show sharp critical signatures at noise-driven phase transitions
in discrete and self-propelled-particle models. No source computes Φ_MIP for a triadic conjunctive
TPM with a commit-flip probability p. The specific question is open. The literature constrains what to
expect and tells you where to look (the susceptibility, not Φ itself), but it does not answer it.

---

## 1. The smooth-decay precedent: Φ-type measures fall off monotonically when noise erases a coupling

In the canonical cross-measure comparison, a minimal two-node coupled Gaussian autoregressive system
swept over coupling strength and noise correlation shows the well-behaved measures (ψ, Φ*, CD)
decreasing monotonically toward zero as noise correlation c rises and the coupling can no longer be
distinguished from the noise [Mediano 2019]. Raw Φ also decreases monotonically but goes negative for
large c. No threshold, discontinuity, or phase transition appears in any measure versus noise in this
model; the trends are smooth and continuous, increasing with coupling and decreasing with noise
[Mediano 2019]. This is the strongest direct precedent for the "smooth decay" reading that the
reliability sweeps (Probes 27, 38) found.

Two limits matter. First, this is a continuous linear AR model with a noise-correlation parameter c,
not a discrete triadic conjunctive TPM with a commit-flip probability p, so the result is analogical,
not a direct instance. Second, the measures disagree strongly: no two of the six candidate measures
agree across all analyses, so the smoothness of Φ-vs-noise is itself measure-dependent. Tilde-Φ and
Sigma-bar grow monotonically and tilde-Φ diverges to infinity as c→1, while ψ, Φ*, and CD decrease
[Mediano 2019]. Smooth monotonic decay is one measure's behavior, not a universal property of "Φ."

**Confidence: high.** Single primary source, but peer-reviewed, canonical, open-access, and the
relevant claims are unanimous (3-0) and verbatim-confirmed.

## 2. The sharp-transition precedent: Φ and its susceptibility show critical signatures at noise-driven transitions

A separate body of work establishes that Φ can exhibit sharp critical behavior as a noise-like or
disorder control parameter varies.

In a Vicsek-type self-propelled-particle model — the closest model class to a coordination system in
this set — Φ_MIP peaks exactly at the noise-driven phase transition point. Φ_MIP is non-monotonic in
the noise parameter: it rises to a maximum at the critical noise value rather than decaying smoothly
[Niizato 2024]. This is the single most relevant result for the research question, because the control
parameter is noise and the measure is Φ_MIP.

In generalized Ising models fitted to brain functional connectivity, integrated information undergoes
a phase transition at the critical temperature Tc, with temperature acting as the disorder control
parameter [Popiel 2020; Khajehabdollahi thesis]. The susceptibility of Φ (χ_Φ) peaks at Tc=1.8 in a
random 5-node ensemble [Popiel 2020]. In coupled-oscillator networks, Φ peaks in the narrow critical
region poised between order and disorder, coinciding with peaks in metastability and coalition entropy
[Mediano 2016; Mediano 2022].

The critical caveat, which reshapes how to read all of this: in these systems it is typically the
**susceptibility** of Φ — a derivative-like response — that peaks at the critical point, not the mean
value of Φ itself. Φ in IIT 3.0 "does not necessarily peak at the critical point (the susceptibility
of Φ peaks at the critical point)" [Niizato 2020]. Popiel et al. report that the variations in mean Φ
are negligible except near criticality, where Φ has both large values and large fluctuations [Popiel
2020]. The sharp feature lives in χ_Φ or the variance of Φ. This directly answers a sub-question of the
research question: if a transition is sought, look at the derivative/susceptibility of Φ, not Φ alone.

**Confidence: high** for the existence of noise-driven Φ criticality across multiple model classes
(SPP, Ising, oscillators), with multiple primary sources. **Medium** for any single quantitative
detail (e.g., Tc=1.8), which is ensemble-specific and not universal.

## 3. The signature is metric- and assumption-dependent

Whether Φ shows a sharp signature at all depends on the unfolding distance and on IIT's noise
assumptions.

With the Wasserstein distance, φ in finite systems tends toward diverging (sharp) behavior around the
critical point; with the Kullback-Leibler divergence, φ does not diverge in finite systems and
diverges only in the mean-field infinite-size limit [Aguilera 2019]. The choice of metric decides
whether a finite system shows a sharp signature.

Standard IIT 3.0 assumptions can also erase the signature. Under an initial noise injection, φ goes to
zero at the critical point and is maximal on the ordered side, so that formulation cannot characterize
the phase transition at all; the diverging signature reappears only under continuous noise injection
[Aguilera 2019]. The sharpness of Φ's critical behavior is conditional on modeling choices that the
triadic-TPM experiment would have to fix explicitly.

**Confidence: high.** Single primary source, but peer-reviewed, open-access, claims unanimous (3-0),
and corroborated by related work on IIT divergence at criticality.

## 4. A precedent for a discrete discontinuity in Φ specifically

The fish-school IIT analysis is the one result in this set that reports a genuine discontinuity in Φ
as a discrete structural parameter crosses a threshold. The change in ⟨Φ⟩ is discontinuous and
qualitative as group size crosses from three to four fish, and this discontinuity appears in Φ but not
in mutual information or transfer entropy [Niizato 2020]. A measure built on IIT can mark a sharp
structural transition that simpler information measures miss. The parameter here is group size, not
commit noise, and the result is on one dataset without independent replication, so it is a precedent
for the *kind* of discontinuity a Φ analysis can find, not evidence about commit noise.

**Confidence: high** for the reported finding (primary, open-access, verbatim, 3-0); the generality is
limited by single-dataset, small-N computation.

## 5. Coordination theory establishes that coordination systems can switch sharply

Coordination dynamics supplies the theoretical reason to take a sharp transition seriously. In human
bimanual coordination, increasing movement-cycling frequency produces an abrupt, discontinuous phase
transition: the out-of-phase mode shifts suddenly to in-phase at a critical point via bifurcation
[Kelso 1984]. Continuous scaling of a control parameter destabilizes the existing mode, and the
qualitative switch happens only when a critical threshold is crossed [Kelso 1984]. This is the
canonical coordination-theory mechanism for sharp threshold transitions, formalized by the
Haken-Kelso-Bunz model and among the most replicated findings in the field.

The bifurcation parameter in HKB is movement frequency, a deterministic drive, not commit noise, and
the order parameter is relative phase, not Φ. The relevance is structural: coordination forms can and
do exhibit sharp threshold transitions in an order parameter, which makes a sharp Φ verdict transition
a reasonable hypothesis to test rather than a long shot.

**Confidence: high.** Foundational primary source, ~1500 citations, repeatedly replicated; the
existence of the abrupt coordination transition is uncontested.

## 6. Φ in IIT 3.0 is not robust to noise

A direct caution for any commit-noise sweep: Φ as defined in IIT 3.0 is not resilient to noise. Adding
a Poisson noise source treated as an internal mechanism can either increase or decrease Φ depending on
network parameters, with no clear pattern (though decreases were more frequent) [Danilczuk 2026]. The
response of Φ to an internal stochastic component is not guaranteed monotonic, so a commit-flip
probability p that the model treats as part of the mechanism could move Φ in either direction. This
both motivates the experiment and warns that a clean monotone p→Φ curve is not guaranteed by theory.

**Confidence: high.** Primary, peer-reviewed, current, unanimous (3-0), corroborated by independent
noise critiques of IIT.

---

## The open gap

No source in the verified set computes Φ_MIP for a triadic conjunctive mediated form as a function of
a mediator's commit-flip probability p, and none reports the dyadic/triadic verdict as a function of
that p. The specific question — sharp threshold versus gradual in Φ_MIP and in the verdict for this
construct — is unanswered in the literature. The closest results are analogies: smooth monotonic decay
in a two-node linear AR model [Mediano 2019], a Φ_MIP peak at the noise transition in a Vicsek SPP
model [Niizato 2024], a discrete Φ discontinuity at fish group-size four [Niizato 2020], and Φ
criticality in Ising and oscillator systems [Popiel 2020; Mediano 2016]. None uses a discrete triadic
conjunctive TPM with a commit-flip probability, and none reports a dyadic-versus-triadic
irreducibility verdict. This is the white space the probe occupies.

What the literature does contribute to the experiment design:

1. Expect the signature, if there is one, in the susceptibility or variance of Φ, not in mean Φ
   [Niizato 2020; Popiel 2020].
2. Fix the noise-injection assumption explicitly; initial-injection IIT 3.0 can zero out the signature
   [Aguilera 2019].
3. Do not assume monotonicity; internal noise can move Φ either way [Danilczuk 2026], and the verdict
   transition could be sharp even if Φ itself moves smoothly [Niizato 2020].
4. A sharp verdict transition is plausible on coordination-theory grounds [Kelso 1984].

---

## Caveats

- **Model mismatch is the central caveat.** The two strongest precedents pull in opposite directions
  and neither matches the target model. The smooth-decay result is a continuous linear AR system with a
  noise-correlation parameter; the sharp-transition results are Ising, oscillator, and SPP systems with
  temperature- or Vicsek-noise control parameters. The triadic conjunctive discrete TPM with a
  commit-flip probability p is none of these. Every cited result is analogical to the target question.
- **Measure dependence.** "Φ" is not one quantity. Six candidate measures disagree, with some decaying
  and some diverging on the same sweep [Mediano 2019]. Results for IIT 2.0 φ (order parameter), IIT 3.0
  Φ (susceptibility peaks, not Φ), and IIT 4.0 (Intrinsic Difference) need not coincide. The probe must
  state which Φ it computes.
- **Sharp-vs-smooth is partly about where you look.** Several "phase transition" results are sharp in a
  derivative (susceptibility, variance) while mean Φ moves smoothly. A finding of "smooth Φ" and "sharp
  verdict" is consistent with this literature, not a contradiction.
- **Single-source findings.** Sections 1, 3, 4, and 6 each rest on one primary source (well-supported
  and unanimous, but not independently replicated within this set). The fish-school discontinuity and
  the Tc=1.8 value are single-dataset / single-ensemble.
- **Finite-size honesty.** Several authors note that true phase transitions require the large-N limit
  and question whether 5-node ensembles license critical claims [Popiel 2020]. Exact PyPhi caps at
  ~10-12 elements, so any triadic-TPM result is inherently finite and small.
- **Refuted overreaches.** Adversarial verification killed ten stronger claims, including that Φ's
  susceptibility and the magnetic susceptibility peak at the same Tc, that the Ising Φ transition is
  unambiguously second-order, and that the SPP noise transition is a "genuine" critical transition.
  The surviving claims are the hedged versions: susceptibility peaks at criticality, Φ behavior is
  metric- and assumption-dependent, and noise-driven Φ criticality exists in some model classes.

---

## Open questions carried forward

1. For a triadic conjunctive TPM with a commit-flip probability p, is the transition sharp in Φ_MIP,
   sharp only in its derivative/susceptibility, or gradual in both? No source answers this.
2. Does the dyadic/triadic verdict (the irreducibility classification) flip at a threshold p* even when
   Φ_MIP itself moves smoothly? The fish-school result suggests verdict-level discontinuities can exist
   where the underlying measure looks continuous, but this is untested for commit noise.
3. Which Φ — IIT 3.0 Φ, IIT 4.0 Intrinsic-Difference Φ, or a tractable proxy — gives the most stable
   p-sweep, and do they agree on the verdict transition given the documented six-measure disagreement?
4. How does the noise-injection assumption (initial versus continuous) change the answer for a discrete
   commit-flip TPM, given that it flips the Ising result entirely?

---

## Sources

Open-access status in brackets. All are primary peer-reviewed or a primary thesis.

1. Mediano PAM, Seth AK, Barrett AB (2019). Measuring Integrated Information: Comparison of Candidate
   Measures in Theory and Simulation. *Entropy* 21(1):17. doi:10.3390/e21010017. arXiv:1806.09373.
   [OA, PMC7514120]
2. Aguilera M (2019). Scaling Behaviour and Critical Phase Transitions in Integrated Information
   Theory. *Entropy* 21(12):1198. doi:10.3390/e21121198. [OA, PMC7514544]
3. Popiel NJM, Khajehabdollahi S, Abeyasinghe PM, Riganello F, Nichols ES, Owen AM, Soddu A (2020).
   The Emergence of Integrated Information, Complexity, and 'Consciousness' at Criticality. *Entropy*
   22(3):339. doi:10.3390/e22030339. [OA, PMC7516800]
4. Khajehabdollahi S (2018). Phase Transitions of Integrated Information in the Generalized Ising Model
   of the Brain. MSc thesis, University of Western Ontario. ETD 5241.
   https://ir.lib.uwo.ca/etd/5241/ [OA]
5. Mediano PAM, Farah JC, Shanahan M (2016). Integrated Information and Metastability in Systems of
   Coupled Oscillators. arXiv:1606.08313. [OA]
6. Mediano PAM, Rosas FE, Farah JC, Shanahan M, Bor D, Barrett AB (2022). Integrated information as a
   common signature of dynamical and information-processing complexity. *Chaos* 32:013115.
   doi:10.1063/5.0063384. arXiv:2106.10211. [OA]
7. Niizato T, Sakamoto K, Mototake Y, Murakami H, Tomaru T, Hoshika T, Fukushima T (2020). Finding
   continuity and discontinuity in fish schools via integrated information theory. *PLOS ONE*
   15(2):e0229573. doi:10.1371/journal.pone.0229573. arXiv:1812.00718. [OA, PMC7046263]
8. Niizato T, Sakamoto K, Mototake Y, Murakami H, Tomaru T (2024). Information structure of
   heterogeneous criticality in a fish school. *Scientific Reports* 14:28934.
   doi:10.1038/s41598-024-79232-2. bioRxiv:10.1101/2024.02.18.578833. [OA]
9. Kelso JAS (1984). Phase transitions and critical behavior in human bimanual coordination.
   *American Journal of Physiology* 246(6):R1000-R1004. doi:10.1152/ajpregu.1984.246.6.r1000.
   PMID:6742155.
10. Danilczuk M, Pokropski M, Suffczynski P (2026). The integrated information Φ of an integrate and
    fire network. *PLOS Computational Biology* 22(3):e1014085. doi:10.1371/journal.pcbi.1014085.
    [OA, CC-BY]

### Supporting / context sources

11. Haken H, Kelso JAS, Bunz H (1985). A theoretical model of phase transitions in human hand
    movements. *Biological Cybernetics* 51:347-356. doi:10.1007/BF00336922. — the HKB model
    formalizing the coordination transition.
12. Amari S, Tsuchiya N, Oizumi M (2018). Geometry of information integration. In *Information
    Geometry and its Applications*. arXiv:1709.10219. — Wasserstein/KL relationship in IIT. [OA]
13. Aguilera M, Di Paolo EA (2018). Integrated information in the thermodynamic limit.
    arXiv:1805.00393. — IIT divergence at criticality, thermodynamic limit. [OA]
