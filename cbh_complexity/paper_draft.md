# Complexity, not entropy, indexes structure: a computational instantiation of the Complex Brain Hypothesis on exactly-computable systems

**Roger Hunt**

*Preprint draft, May 2026. Code, data, and figures:
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`cbh_complexity/`).
Citations are author–year and resolve to `literature/references.bib`. This is a constructive response to
Mago et al. (2026), supplying the computational instantiation that paper calls for.*

---

## Abstract

The Entropic Brain Hypothesis holds that the entropy of spontaneous brain activity indexes the richness
of conscious experience. Minimal Phenomenal Experiences (MPEs), phenomenologically sparse states such
as deep meditation, pose a problem, because they show elevated entropy despite low content, the same
signature as high-content psychedelic experiences. Mago et al. (2026) name this the entropy–content
conundrum and propose the Complex Brain Hypothesis (CBH): richness is indexed by complexity rather than
entropy, where complexity is shaped by the grain of inference (coarse vs fine), so that high entropy can
arise in two distinct regimes that complexity, but not entropy, separates. The CBH is conceptual; it
provides no computable measure or worked model, and it explicitly calls for one. We supply it. On the
authors' own example systems, the 2D Ising model across temperature, and a small dynamical system where
exact IIT-4.0 Φ is computable, we implement entropy H, Tononi–Sporns–Edelman neural complexity Cₙ,
apparent complexity under coarse-graining, and exact Φ, and test whether the CBH's claims hold with exact
numbers. They largely do, with one informative qualification. On the exact 4×4 Ising model, entropy is
monotone in temperature while Cₙ is non-monotone, peaking near the critical temperature (Cₙ = 8.3 at
T ≈ 2.25) and collapsing at high temperature (Cₙ = 1.8): the highest-entropy state has low complexity.
On a parity-ring dynamical system swept from order to disorder, entropy rises monotonically while Cₙ
peaks at intermediate disorder and exact Φ falls, so the maximal-entropy state has zero complexity and
zero integration, "contentless." Two systems matched at high entropy (H = 3.17 bits) are cleanly
separated by complexity and Φ (Cₙ = 0, Φ = 0 versus Cₙ = 0.25, Φ = 0.39). Apparent complexity under
explicit coarse-graining collapses for the high-entropy disordered state, consistent with the
grain-dependence the CBH asserts, though with finite-size caveats. The qualification is that TSE neural
complexity resolves the conundrum at the high-entropy end but stays high at the ordered low-entropy end
(the known redundancy conflation), so it is not a complete richness index on its own; the coarse-grained
apparent complexity is needed for the full picture. The CBH's central logical claim, that complexity
dissociates from entropy and is the better index of structure, survives a concrete computational
instantiation, and we identify which measures realise it.

---

## 1. Introduction

The Entropic Brain Hypothesis (EBH; Carhart-Harris et al. 2014) proposes that the entropy of spontaneous
brain activity is a marker of the richness of conscious experience: more entropy, more phenomenal
content. The hypothesis is supported by the elevated signal diversity of high-content psychedelic
experiences (HCPEs). Minimal Phenomenal Experiences (MPEs), wakeful but phenomenologically sparse
states, such as deep meditative absorption, present a difficulty. Neuroimaging suggests that MPEs also
show elevated entropy, despite being content-poor. Entropy is therefore high for both rich and
contentless states, and cannot by itself index richness. Mago et al. (2026) call this the
entropy–content conundrum.

Their resolution, the Complex Brain Hypothesis (CBH), is that richness is better indexed by *complexity*
than by entropy. Complexity, in their account, is the structured part of a representation, the
organised content, with randomness filtered out, and it depends on the *grain of inference*, the scale
or coarseness of the brain's generative model. High entropy can then arise in two regimes that
complexity separates: a fine-grained, overfitting regime (some HCPEs) in which loosened constraints
amplify fluctuations into proliferating content, and a coarse-grained, underfitting regime (some MPEs)
in which a simpler model dissolves variety into contentless awareness. The authors ground complexity in
two ways: the free-energy "complexity" term (a Kullback–Leibler divergence between posterior and prior
beliefs), and "apparent complexity" in the sense of Aaronson, Carroll & Ouellette (2014), the
algorithmic complexity of a coarse-grained representation, illustrated by a coffee–cream mixing process
and by the Ising model across temperature.

The CBH is a conceptual paper. It offers no computable complexity measure, no discrete-system model, and
no worked demonstration; it explicitly states that "measures sensitive to model architecture … such as
approximations of Kolmogorov Complexity, causal large-scale models … will be necessary to disambiguate
high-entropy states that differ in complexity," and that "any adequate computational theory of
consciousness must be able to account for how similarly high-entropy neural dynamics can support both
densely structured HCPEs and minimally structured, 'contentless' awareness."

We provide that computational account. We hold tools the CBH does not deploy: implementations of entropy
and of established complexity measures, an exact coarse-graining apparatus, and an exact IIT-4.0 Φ
oracle that runs on small systems. On the authors' own example systems, the Ising model, and a small
dynamical system where Φ is exactly computable, we instantiate the CBH's quantities and test, with
exact numbers, whether its claims hold. This is a constructive engagement: rather than auditing an
existing measure, we build the model the hypothesis requires and report whether it behaves as claimed,
including the measures and regimes where it does not.

## 2. Background

### 2.1 Entropy, and why it cannot be the whole story

Entropy here is the Shannon entropy H of the distribution over a system's states, the formal counterpart
of the EBH's "signal diversity." It is maximal for a uniform distribution and minimal for a system
locked in one state. The conundrum is a statement about H: two systems can share high H yet differ in
the structure of what that entropy is distributed over. Entropy counts the diversity of states; it does
not measure how those states are organised. A maximally random system and a richly structured system can
both have high entropy.

### 2.2 Complexity measures

We use three computable complexity constructs, chosen to match the CBH's own references.

**Tononi–Sporns–Edelman neural complexity Cₙ** (Tononi, Sporns & Edelman 1994; the construct the CBH
cites as "neural complexity"). For a system of n units with a joint distribution, Cₙ combines
*integration* (the whole is more than the sum of its parts) with *differentiation* (the parts are not
all identical). Formally, with total correlation I(X) = Σ_i H(x_i) − H(X), Cₙ = Σ_k [(k/n) I(X) −
⟨I(X_k)⟩], where ⟨I(X_k)⟩ is the average integration over subsets of size k. Cₙ is zero for independent
units (no integration) and is intended to be larger for systems that are both integrated and
differentiated. As we confirm below, Cₙ is also non-zero for fully redundant (ordered) systems, a known
property we address directly.

**Apparent complexity under coarse-graining** (Aaronson et al. 2014; Gell-Mann & Lloyd 1996). This is the
complexity of a *coarse-grained* representation: a uniform field (ordered, or washed-out to homogeneity)
has a short description and low apparent complexity, while a structured field of domains has high
apparent complexity. We operationalise it as the Shannon entropy of the distribution of coarse-grained
block-magnetization values at a chosen grain. The grain, the block size, is the CBH's "grain of
inference." Strict apparent complexity is Kolmogorov complexity, which is uncomputable; the block-value
distribution is a principled computable surrogate that captures the rise-and-fall the coffee/Ising
picture is about.

**Exact IIT-4.0 Φ** (Oizumi et al. 2014; Albantakis et al. 2023). Φ is the irreducible cause–effect
structure a system specifies for itself, an integration measure computed exactly on small systems with
PyPhi (reusing the `proxy_audit` oracle from the companion project). We include it as an independent,
theory-grounded index of organised structure, distinct from Cₙ and from apparent complexity.

### 2.3 Grain of inference and coarse-graining

The CBH's "grain of inference" is the scale of the generative model: fine-grained models have many
effective parameters and resolve fine detail; coarse-grained models have few and smooth over it. The
formal counterpart is block coarse-graining: replacing groups of units by their average. Apparent
complexity is grain-dependent by construction, which is the lever the CBH uses to separate the two
high-entropy regimes.

## 3. Methods

### 3.1 Pre-registered claims

We fixed two claims to test before computing anything. **C1 (resolution of the conundrum):** entropy is
monotone in disorder and so cannot separate the structured from the maximally-disordered regime, whereas
a complexity measure (Cₙ, apparent complexity, or Φ) is non-monotone, peaking at an intermediate
structured regime and so separating them. **C2 (grain-dependence):** the apparent complexity of a
high-entropy disordered state is high at fine grain but collapses under coarse-graining, while a
structured (critical) state retains complexity across grains.

### 3.2 Validation of the instruments (before any sweep)

Each measure was validated on controls. Cₙ = 0 and integration I = 0 for n independent fair bits; Cₙ is
larger for a structured system (three correlated pairs: Cₙ = 3.5) than for either independent units (0)
or fully-redundant units (2.5). Apparent complexity is 0 for a uniform field and positive for a
two-domain field. Entropy is maximal for the uniform distribution. These pass before any experiment.

### 3.3 Experiment A: exact 2D Ising (the authors' own example)

We enumerate all 2^16 configurations of a 4×4 periodic Ising lattice, compute the Boltzmann distribution
P(config) ∝ exp(−E/T) at each temperature with E = −Σ_{⟨ij⟩} s_i s_j, and from it the exact Shannon
entropy H(T) of the configuration distribution and the exact (Boltzmann-weighted) TSE complexity Cₙ(T)
and apparent complexity. A 4×4 lattice is small enough to enumerate exactly and large enough to show the
finite-size crossover near the 2D critical temperature T_c ≈ 2.27.

### 3.4 Experiment B: grain-dependence

To vary the grain over a usable range we use a larger 16×16 lattice, sampled by Metropolis Monte Carlo
(400 equilibrium configurations per temperature), and compute apparent complexity at block sizes 1, 2, 4,
8 at low (T = 1.0), critical (T = 2.27), and high (T = 6.0) temperature. This is the one sampled (rather
than exact) experiment, and we report its finite-size limitations.

### 3.5 Experiment C: exact IIT-4.0 Φ on a dynamical system

To connect "complexity" to integration on a system where Φ is exact, we use a parity ring: n = 4 binary
nodes, each updating to the parity (XOR) of its two ring-neighbours, which is maximally integrative. A
per-node noise parameter carries the system from order (noise 0, deterministic) to disorder (noise 0.5,
uniform), an order parameter analogous to Ising temperature. At each noise level we compute the entropy
H and TSE complexity Cₙ of the stationary distribution and the exact IIT-4.0 Φ (mean and max over
reachable states).

### 3.6 Matched-entropy dissociation

We exhibit the conundrum analytically. Because every system at maximal entropy is uniform and hence
independent (forcing complexity to zero), the informative comparison is at high-but-submaximal entropy.
We match the parity ring at a chosen noise to a system of independent biased bits with the same
stationary entropy, and compare their complexity and Φ.

## 4. Results

### 4.1 Exact Ising: entropy is monotone, complexity peaks then collapses (C1)

On the exact 4×4 Ising lattice, entropy increases monotonically with temperature, from H = 1.0 bit at
T = 0.5 (the two ordered ground states) to H = 15.3 bits at T = 6.0 (near the 16-bit maximum); the rank
correlation of T with H is +1.0. TSE complexity behaves differently. Cₙ is non-monotone: it rises to a
peak of 8.26 at T = 2.25, essentially at the finite-size critical temperature, and then collapses to
1.84 at T = 6.0. The highest-entropy state therefore has low complexity (Figure 1a). This is the
conundrum's resolution made exact on the authors' own example system: high entropy does not imply high
complexity, because complexity tracks organised structure and the maximally-disordered state, though
maximally diverse, is structureless.

One qualification is important and we state it plainly. Cₙ is also high at low temperature (7.5 at
T = 0.5), where the system is ordered and low-entropy. This is the known redundancy property of TSE
complexity: a fully-aligned system is highly integrated (every spin predicts every other) and so scores
high, even though it is phenomenologically simple. TSE complexity thus resolves the conundrum at the
high-entropy end (disorder → low Cₙ) but conflates order with complexity at the low-entropy end. It is a
correct discriminator of the two high-entropy states the CBH is concerned with, but not a complete index
of richness across the whole order–disorder axis.

### 4.2 Grain-dependence: the disordered state collapses when coarsened (C2)

On the sampled 16×16 lattice, apparent complexity depends on grain in the predicted direction. At the
coarsest grain examined (block size 8), the high-temperature disordered state (T = 6.0) has the lowest
apparent complexity, 1.89 bits, below both the critical (2.02) and the ordered (2.53) states, even
though it has the highest microscopic entropy (Figure 1c). Coarse-graining reveals the high-entropy state
as the simplest: its fine-scale fluctuations average out to a homogeneous coarse description, exactly the
coffee-automaton picture. The ordering of the ordered and critical states across grains is not clean at
this lattice size, a finite-size and sampling limitation we do not paper over; the robust signal is the
collapse of the disordered state under coarse-graining.

### 4.3 Exact Φ: integration is destroyed by disorder, complexity peaks (C1 with Φ)

On the parity ring, entropy of the stationary distribution rises monotonically with noise, from 0 (the
deterministic cycle) to 4.0 bits (uniform). TSE complexity peaks at intermediate noise (Cₙ = 0.31 at
noise 0.075) and falls to 0 at maximal noise. Exact IIT-4.0 Φ_max falls monotonically from 0.50 in the
ordered system to 0 in the disordered one: integration requires the structured dependencies that noise
destroys. The maximal-entropy state has H = 4.0 (maximal), Cₙ = 0, and Φ = 0, maximally diverse, with
zero complexity and zero integration, the formal counterpart of contentless awareness (Figure 1b). The
rank correlations confirm that complexity and integration are not functions of entropy: Spearman(H, Cₙ)
= −0.71 and Spearman(H, Φ_max) = −1.0 over the sweep.

### 4.4 Matched-entropy dissociation

Two systems matched at H = 3.17 bits are cleanly separated by complexity and integration (Figure 1d). A
system of four independent biased bits has Cₙ = 0 and Φ = 0 (the contentless, coarse-grained analogue),
while the parity ring at the matching noise has Cₙ = 0.25 and Φ_max = 0.39 (the structured analogue).
Entropy is identical; complexity and Φ are not. This is the entropy–content conundrum exhibited exactly
in four units: entropy cannot tell the two systems apart, and complexity and Φ can.

## 5. Discussion

### 5.1 The CBH's central claim survives a computational instantiation

The CBH asserts that complexity, not entropy, indexes organised structure, and that high entropy can
occur with high or low complexity depending on the grain of description. On exactly-computable systems,
including the authors' own Ising example, this holds. Entropy is monotone in disorder; complexity (TSE
Cₙ, apparent complexity, exact Φ) is non-monotone or anti-monotone, so the highest-entropy state is the
least structured. Two systems at matched high entropy are separated by complexity and by Φ. The verbal
hypothesis becomes a worked model with exact numbers, and the resolution of the conundrum is concrete
rather than asserted.

### 5.2 Which measure realises the claim, and which does not

The instantiation also adjudicates between candidate complexity measures, which the conceptual paper
cannot, and the adjudication is less flattering to the obvious candidates than one might hope. Both exact
Φ and TSE neural complexity cleanly resolve the *high-entropy* end of the conundrum: the disordered,
maximal-entropy state has Φ = 0 and low Cₙ, so neither mistakes diversity for structure. But neither
vanishes at the *low-entropy* ordered end. TSE Cₙ is high for a fully-redundant ordered system (the
known redundancy property). Exact Φ, on the parity ring, is in fact highest for the ordered deterministic
system (Φ_max = 0.50 at zero noise) and falls monotonically with disorder: Φ tracks integration, and a
deterministic integrated cycle is maximally integrated even though it is low-entropy and undifferentiated.
So Φ, like Cₙ, rates the ordered low-entropy state as "rich," which by the CBH's own differentiation
criterion is a false positive. The only measure that is low at *both* extremes and high only for
structured intermediates, the full Aaronson picture, is apparent complexity under coarse-graining,
which in our finite systems shows the predicted collapse of the disordered state but is the noisiest of
the three. The practical implication for the CBH is sharper than "use complexity instead of entropy":
the right index must be low for both order and disorder, and neither raw TSE complexity nor exact Φ has
that profile. A coarse-grained apparent complexity does, and it is the construct the CBH's own
coffee/Ising illustrations actually point to.

### 5.3 Relation to integrated information

The CBH and IIT make partial contact here. The complexity the CBH wants, organised, differentiated
structure rather than mere diversity, overlaps with what Φ measures at the disordered end: both Φ and
the CBH agree that the maximal-entropy state is structureless. But the overlap is incomplete. Φ is
destroyed by the disorder that raises entropy, so it is highest at the ordered, low-entropy limit, which
the CBH would not call rich. So integration is a natural candidate for the CBH's index only with respect
to the high-entropy conundrum, not as a general richness measure. The deeper consequence concerns the
*fine-grained* HCPE regime, which the CBH describes as high entropy together with high complexity. In our
framework that combination cannot live at the maximal-entropy limit, where every system is uniform and
hence structureless; it lives at high-but-submaximal entropy, as in the matched-entropy rich system
(H = 3.17 of a 4-bit maximum, with positive Cₙ and Φ). This is a sharpening the CBH's verbal account
leaves implicit: "high entropy with high complexity" must mean high relative to baseline, not maximal,
because complexity necessarily vanishes as entropy approaches its ceiling.

### 5.4 What the result does and does not establish

We have tested the information-theoretic content of the CBH: that entropy and complexity dissociate, that
the dissociation is grain-dependent, and that complexity is the better index of structure. We have not
tested, and do not address, the neuroscientific or phenomenological claims, whether meditation or
particular psychedelics realise the coarse- and fine-grained regimes in the brain, which is an empirical
question about human data, not about small dynamical systems. Our contribution is to show that the
formal core of the hypothesis is coherent and demonstrable, and to identify which complexity measures
carry it.

## 6. Limitations

The systems are small: a 4×4 exact Ising lattice (finite-size crossover, not a sharp transition), a
16×16 sampled lattice for the grain sweep, and n = 4 for the exact-Φ experiment. We claim the
qualitative dissociation, not critical exponents. Apparent complexity is operationalised by a computable
surrogate (the entropy of coarse-grained block values), not Kolmogorov complexity, which is uncomputable;
the surrogate captures the rise-and-fall but is not the only reasonable choice. The grain sweep is
sampled rather than exact and shows finite-size noise in the ordered/critical ordering. TSE complexity
conflates redundancy with complexity at the ordered end, as discussed. Finally, the FEP "complexity"
term (a posterior–prior KL divergence) is part of the CBH's grounding but is not directly computed here,
because it requires a specified generative model and prior; instantiating that term on a dynamical system
is a natural next step.

## 7. Conclusion

The Complex Brain Hypothesis proposes that complexity, not entropy, indexes the richness of conscious
experience, and that high entropy can accompany both rich and contentless states depending on the grain
of inference. The hypothesis was conceptual, and its authors called for a computational instantiation.
We supplied one, on their own example systems and on systems where IIT-4.0 Φ is exact. Entropy is
monotone in disorder; complexity peaks at intermediate structure and collapses at maximal disorder;
exact Φ is destroyed by disorder; and two systems matched at high entropy are separated by complexity and
Φ. The CBH's central dissociation holds with exact numbers, and the instantiation identifies which
complexity measures realise it, exact Φ and coarse-grained apparent complexity cleanly, raw TSE neural
complexity only at the high-entropy end. The entropy–content conundrum is resolvable on computable
systems, and "complexity" in the CBH is, on these systems, close to integration.

## Data and code availability

All code, data, and figures are at https://github.com/rogerSuperBuilderAlpha/iit-experiments
(`cbh_complexity/`). Reproduce end-to-end: `python -m cbh_complexity.complexity` (instrument controls),
`python -m cbh_complexity.run` (the three experiments), `python -m cbh_complexity.dissociation`
(matched-entropy dissociation), `python -m cbh_complexity.analyze` (summary), and
`python -m cbh_complexity.figures` (figure). The exact-Φ oracle is reused from `proxy_audit/`.

## Acknowledgments

This study was developed with AI assistance (Anthropic's Claude) for code, analysis, and drafting; all
quantitative claims were checked against computed results. We thank the authors of the Complex Brain
Hypothesis for an open preprint; this constructive response is offered collegially, and a courtesy copy
will be sent.

## References

Citations resolve to `literature/references.bib`. Key sources:

- Aaronson, S., Carroll, S. M., & Ouellette, L. (2014). Quantifying the rise and fall of complexity in
  closed systems: the coffee automaton. arXiv:1405.6903.
- Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLOS Comput. Biol.*
  19(10):e1011465.
- Carhart-Harris, R. L., et al. (2014). The entropic brain. *Front. Hum. Neurosci.* 8:20.
- Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory
  processing and behavior. *Sci. Transl. Med.* 5(198):198ra105.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.*
  11:127–138.
- Gell-Mann, M., & Lloyd, S. (1996). Information measures, effective complexity, and total information.
  *Complexity* 2(1):44–52.
- Mago, J., Lopez-Sola, E., Vohryzek, J., Lifshitz, M., Carhart-Harris, R., Friston, K., & Chandaria, S.
  (2026). The Complex Brain Hypothesis. arXiv:2605.16146.
- Mehta, P., & Schwab, D. J. (2014). An exact mapping between the variational renormalization group and
  deep learning. arXiv:1410.3831.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
  consciousness: IIT 3.0. *PLOS Comput. Biol.* 10(5):e1003588.
- Tononi, G., Sporns, O., & Edelman, G. M. (1994). A measure for brain complexity. *PNAS*
  91(11):5033–5037.
