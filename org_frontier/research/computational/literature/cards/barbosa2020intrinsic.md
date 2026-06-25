---
citekey: barbosa2020intrinsic
title: A measure for intrinsic information
authors: Barbosa, Leonardo S. and Marshall, William and Streipert, Sabrina and Albantakis, Larissa and Tononi, Giulio
year: 2020
doi: 10.1038/s41598-020-75943-4
arxiv: null
journal: Scientific Reports
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41598-020-75943-4.pdf
sha256: d05770af15e50b492f81a647907a743e75232bcf8ed0a76821dc3f9bc76c44fe
pdf_path: literature/pdfs/barbosa2020intrinsic.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper asks how to measure information from the *intrinsic perspective* of a receiver or sender of a single symbol who has no access to the communication channel, its source, or its target (e.g., a neuron in a network), as opposed to the extrinsic perspective of a channel designer who can agree on codes and use error correction. The authors formalize three desired properties—causality, specificity, and intrinsicality—and prove that a unique measure (up to a positive multiplicative constant) satisfies all three: the *intrinsic difference* (ID), D(Pn, Qn) = max_α { p_α log(p_α / q_α) }. They contrast ID with the Kullback–Leibler (KL) divergence, showing KL is a probability-weighted sum over all states (total "mass") while ID picks the single optimal state with highest "density" (informativeness log(p_α/q_α) times selectivity p_α). Through worked enclosure examples (one-wire bit channels vs. eight-wire byte channels with noise), they show ID captures the intuition that a noisy byte-size channel conveys near-zero intrinsic information while KL still assigns it 1 bit. They demonstrate that ID, unlike KL, mandates a balance between expansion (adding noiseless signal, additivity) and dilution (adding noise, sub-additivity), so intrinsic information peaks at an optimal channel/fan-out size. Applied to a network of simplified sigmoidal neurons, ID peaks at an intermediate number of outputs (e.g., N=8 for noise level t=1), whereas KL grows indefinitely with the number of target neurons.

## Key facts it relies on
- The measure satisfies three properties—causality (D=0 only when source has no causal connection, i.e., Pn ≡ Qn), specificity (D reflects the single most informative symbol via D(Pn,Qn) = max_α f(p_α,q_α)), and intrinsicality (additive for noiseless expansion, sub-additive for noisy dilution)—and is shown to be unique.
- The unique resulting measure (up to a multiplicative constant k > 0, set to k=1) is the intrinsic difference: D(Pn, Qn) = k max_α { p_α log(p_α / q_α) }; the full theorem and proof are in the Supplementary Materials.
- Intrinsicality formalizes that extending a noiseless channel Vn1 by a noiseless channel Vm2 (Kronecker product) is additive: D(Vn1∗Vm2, Qn1∗Qm2) = D(Vn1,Qn1) + D(Vm2,Qm2); extending by a fully noisy channel Um is sub-additive: D(Pn∗Um, Qn∗Um) = [D(Pn,Qn) + D(Um,Um)] / m.
- ID is interpreted as informativeness log(p_α/q_α) times selectivity p_α at the optimal state; by analogy to mass, KL computes total mass while ID finds the point of highest density. KL is defined as KL(Pn,Qn) = Σ_α p_α log(p_α/q_α).
- In the enclosure example, ID and KL both assign 1 bit/ibit to the noiseless bit-size (one-wire) channel and 8 bits/8 ibits to the noiseless byte-size (eight-wire) channel; but for the noisy byte-size channel (one noiseless wire + seven fully noisy wires, signal probability 1/2), KL assigns 1 bit while ID assigns close to zero ibits (~0.01).
- A new unit, the intrinsic bit ("ibit"), is defined to name the quantity returned by the ID function, because KL (bits) and ID outputs are not commensurable.
- For a byte-size channel with one noiseless wire and seven wires of variable noise s ∈ [1, 1/2], a noise level of s ≈ 0.78 yields 1 ibit; the noisy byte channel's output then displays one correct byte-size character on a typical run of eight transmissions.
- For fixed per-wire correctness r = 0.88, informativeness log(p_α/q_α) = N log(r/2) grows linearly and selectivity p_α = r^N decreases exponentially; their product ID peaks at N=8 wires (2.41 ibits), versus ~0.72 ibits at N=1 and 1.77 ibits at N=16.
- For a network of simplified neurons with sigmoidal firing P(Yj=1|X=x_α) = 1 / (1 + exp[−2t^{-1}(h(x_α)+b)]), bias b = 1−N, at noise level t=1 ID peaks at N=8 outputs (2.90 ibits), versus 0.72 ibits at N=1 and 2.10 ibits at N=16; KL grows indefinitely with the number of target neurons.
- The KL measure is uniquely characterized by monotonicity, continuity, and additivity; it satisfies the authors' Causality property but not Specificity or Intrinsicality.

## Critical notes from the literature
- Scope/idealization: the network application uses *simplified* neurons; the authors state future work must address more realistic elements, the influence of connection patterns, correlated signals, signal composition and integration, and the effects of learning.
- The neuron example makes specific simplifying assumptions: iid noise, bias chosen as b = 1−N to manipulate noise only through slope t, and uniform chance distribution P(X=x_α)=1/n; output neurons are conditionally independent given inputs but not independent in the joint distribution (they share inputs and carry redundant information).
- The choice of one noiseless wire and seven noisy wires is described as arbitrary, serving only to match the motivating example; other arrangements (e.g., two noiseless, six noisy) are said not to change the qualitative behavior (Supplementary Figure S2), and a correlated-noise example is deferred to Supplementary Figure S1.
- The authors frame ID as an alternative to the extrinsic approach where, lacking optimal encoding, one selects a channel by maximizing KL subject to a *subjective* maximum acceptable error rate (one-shot/real-time communication); ID instead yields a principled error rate without that subjective constraint.
- Positioning vs. prior measures: unlike generalized measures (e.g., Daróczy, Havrda–Charvát, Tsallis) that are sub-additive for *all* independent distributions, ID is sub-additive only for some independent distributions (any p_α < 1) and additive for others (any p_α = 1); the Rényi entropy can satisfy specificity in a limit but is always additive and thus lacks dilution.

## Key topics covered
- Intrinsic vs. extrinsic perspective on information; intrinsic information measure
- Intrinsic difference (ID) measure; uniqueness theorem
- Causality, specificity, intrinsicality properties (axiomatic characterization)
- Expansion (additivity) vs. dilution (sub-additivity) trade-off
- Informativeness vs. selectivity decomposition
- Kullback–Leibler divergence comparison; channel capacity and error-correcting codes
- Intrinsic bit (ibit) unit
- Noiseless/noisy bit- and byte-size channels; enclosure thought experiment
- Optimal channel/fan-out size selection
- Simplified sigmoidal neuron networks; neural fan-out optimization
- Rényi entropy, Tsallis / Havrda–Charvát / Daróczy generalized entropies (comparison)
- Connection to IIT-style intrinsic-perspective modeling of neurons
