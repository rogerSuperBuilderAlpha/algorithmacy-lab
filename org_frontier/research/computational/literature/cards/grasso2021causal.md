---
citekey: grasso2021causal
title: Causal reductionism and causal structures
authors: Grasso, Matteo and Albantakis, Larissa and Lang, Jonathan P. and Tononi, Giulio
year: 2021
doi: 10.1038/s41593-021-00911-8
arxiv: null
journal: Nature Neuroscience
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://static-content.springer.com/esm/art%3A10.1038%2Fs41593-021-00911-8/MediaObjects/41593_2021_911_MOESM1_ESM.pdf
sha256: 22654d30ad9c0ad9f68d34ffde543bf2bcb53813b5b70ef88a08e3e1459b3676
pdf_path: literature/pdfs/grasso2021causal.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
This paper argues against "causal reductionism" — the assumption that the causal workings of a system are fully captured by the causes and effects of its individual micro-level mechanisms — and proposes instead that causation should be characterized in terms of full causal structures that include higher-order and macro-level mechanisms. (Note: the acquired PDF is the Supplementary Information only, which documents the methods and worked examples backing the main text.) Using the formal framework of actual causation (Albantakis et al., 2019), the authors causally analyze three kinds of in-silico artificial organisms ("frogs") that live in a 2D grid world and react to "bugs," each frog implemented as a network of probabilistic binary sensor, central, and motor units described by a state transition probability matrix (TPM). The causal analysis identifies which subsets of central units form irreducible mechanisms and what their actual causes (sensor states at t-1) and effects (motor states at t+1) are, scored by a causal strength measure α formalized as an Intrinsic Difference. The central demonstration is that frogs behaviorally indistinguishable in some respects differ in their causal structure: F3 and F2 frogs contain irreducible higher-order mechanisms (e.g., a second-order mechanism over central units whose actual cause is the super-bug pattern), whereas a pair of F1 frogs is causally reducible into two independent first-order structures with no higher-order mechanism and no relations between objects and actions. A separate worked example shows, as a proof of principle, that macro-level causes/effects (black-boxed functional units) can have higher causal strength α than their underlying micro-level causes/effects.

## Key facts it relies on
- The grid world contains three bug types: left-bugs and right-bugs ("small-bugs," two horizontally adjacent squares, head + tail) which are prey, and super-bugs (three horizontally adjacent squares, two heads + central body) which are predators that prey on frogs and all other bugs.
- Frogs are built from three kinds of probabilistic binary units — sensors (S), central units (C), and motors (M); causal analysis focuses only on central units because only they have both causes and effects within the frog's nervous system.
- Unit firing probability uses a Gaussian activation function with parameters µ = 1 and σ = 0.3; e.g., in F2 frogs unit M_L's input weights sum to 1 when its inputs CLCR = 11, giving firing probability 1.
- Causal strength α is computed from interventional probabilities from the system's TPM and is formalized (per Barbosa et al., 2020) as an Intrinsic Difference of the form α = p · log2(p/q), weighting the log-ratio by the unpartitioned purview probability to balance expansion and dilution; the actual cause/effect is the purview with the highest α (exclusion principle).
- F3 frogs specify 6 irreducible mechanisms; mechanism CC = 1 has actual cause SLSCSR = 101 (detecting a super-bug) and actual effect MLMR = 11 (jumping over); the figure reports αcause = 0.3·log2(0.3/0.12) = 0.39 and αeffect = 0.27·log2(0.27/0.21) = 0.09 for CC.
- The actual cause of CC = 1 equals the union of the actual causes of CL = 1 and CR = 1: (SLSCSR = 101) = (SLSC = 10) ∪ (SCSR = 01), reflecting that super-bugs are composed of a left-bug and a right-bug fused at the tail.
- In F2 frogs all 3 possible mechanisms (CL, CR first-order and CLCR second-order) are irreducible; for the CLCR mechanism the figure reports αcause = 0.8·log2(0.8/0.56) = 0.41 and αeffect = 1·log2(1/0.81) = 0.3.
- For a pair of F1 frogs the second-order mechanism CLCR is reducible (αcause = 0 and αeffect = 0 in Fig. B2C): no irreducible cause purview over SLSRSLSR exists, so the joint structure decomposes into two independent first-order causal structures and no object–action relations appear.
- The macro/micro example uses nine micro elements grouped into three functional units (A, B, C), each with two binary input units (X, Y) and one ternary output O (states {0,1,2}); X/Y use a sigmoid activation with bias h = −1.8 and indeterminism τ = 0.4, O uses a softmax with z weights [[3.5,2.5,2.0],[2.0,3.0,3.0],[1.0,2.0,5.0]]; black boxes are evaluated over two micro time steps (per Marshall et al., 2018).

## Critical notes from the literature
- Scope of acquired file: the supplied PDF is explicitly the Supplementary Information ("In the format provided by the authors and unedited"), containing Supplementary Notes 1–3 and Figures A1, B1–B3; the main-text arguments, Box 2, and main figures are referenced but not present, so quantitative claims here are limited to the supplement.
- The analysis is entirely in silico on small hand-designed model organisms with known TPMs; the paper presents the macro-over-micro result explicitly as a "proof of principle" rather than a general theorem, and demonstrates it for a single worked example system.
- The causal framework is the authors' own actual-causation / IIT-derived formalism (Albantakis et al., 2019; Barbosa et al., 2020; Marshall et al., 2018), so conclusions about "irreducible higher-order/macro mechanisms" are framework-dependent (they hinge on the chosen α measure, the integration and exclusion principles, and the partition scheme).
- The frog comparison is constructed so that causal structure, not behavior alone, distinguishes the systems (e.g., a pair of F1 frogs is reducible by design); this is illustrative of the thesis rather than an empirical sampling of natural systems.

## Key topics covered
Causal reductionism; causal structure; actual causation; integrated information theory (IIT); irreducible mechanisms; higher-order and second-order mechanisms; macro vs. micro causation; black-boxing of functional units; causal strength (α) / Intrinsic Difference; cause and effect purviews; exclusion and integration principles; transition probability matrices (TPMs); in-silico artificial organisms (frogs/bugs); cause–effect relations and overlapping purviews.
