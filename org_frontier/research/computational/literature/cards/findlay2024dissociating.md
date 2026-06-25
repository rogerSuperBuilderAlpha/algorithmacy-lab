---
citekey: findlay2024dissociating
title: Dissociating Artificial Intelligence from Artificial Consciousness
authors: Findlay, Graham and Marshall, William and Albantakis, Larissa and David, Isaac and Mayner, William G. P. and Koch, Christof and Tononi, Giulio
year: 2024
doi: 10.48550/arXiv.2412.04571
arxiv: 2412.04571
journal: arXiv preprint
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2412.04571
sha256: 592bfcbf6d38a8a04e315b30b60845f66f1fcde367ed531b9dc269a72dc2e8d6
pdf_path: literature/pdfs/findlay2024dissociating.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper asks whether a computer that is functionally equivalent to a conscious system (e.g. could do all a human does) would thereby be phenomenally equivalent — i.e. actually experience anything. The authors address this through Integrated Information Theory (IIT), which grounds consciousness in a system's intrinsic cause–effect structure rather than its functions. Their method is to construct explicit pairs of Boolean-unit systems: a small target system (a four-unit "simulandum," PQRS) and a stored-program digital computer ("simulans") that is functionally equivalent to it, then apply IIT's mathematical machinery to both. They demonstrate that the two systems can be functionally equivalent without being phenomenally equivalent: the target specifies a single rich cause–effect structure, whereas the computer fragments into many tiny complexes specifying trivial structures. They further show this dissociation does not depend on what function is simulated (it holds for a Turing-complete Rule 110 implementation too) and extends by induction to arbitrarily large computers simulating arbitrarily complex behaviors. The conclusion, per IIT, is that a digital computer could simulate human behavior — even simulate the brain neuron by neuron — without replicating experience, sharply contrasting with computational functionalism.

## Key facts it relies on
- IIT formulates five axioms of phenomenal existence (intrinsic, specific, unitary, definite, structured) into five corresponding postulates of physical existence (intrinsicality, information, integration, exclusion, composition), assessed algorithmically on a system's transition probability matrix (TPM).
- A substrate supports consciousness — is a "complex" — iff it maximizes system integrated information (φs) relative to overlapping candidate systems and grains; its quality of experience is given by its unfolded cause–effect structure (Φ-structure).
- The target system PQRS is four binary Boolean units; in state 0101 (pQrS) it has φs = 1.51 ibits (intrinsic bits) and is a complex.
- The cause–effect structure of pQrS is composed of 13 distinctions and 8184 relations, with Φ = 391.25 ibits.
- The simulating computer is a Harvard-like stored-program four-bit machine constituted of 117 micro units (clock/frequency dividers, program/instruction register, multiplexer/processing unit, four data registers); the 4-unit simulandum and 117-unit simulans are functionally equivalent modulo eight updates.
- Applied to the whole computer, φs = 0 ibits because it contains purely feedforward modules; the computer fragments into 24 disjoint complexes, each with Φ ≤ 6 ibits (and feedback-connected versions add small complexes with Φ ≤ 2 ibits).
- The computer's failure to replicate PQRS's cause–effect structure cannot be rescued by macroing its units into functionally meaningful macro units (e.g. multiplexer, registers), because such macroings violate IIT's postulates (e.g. they are reducible, not maximally irreducible, or borrow extrinsic causal power).
- The result is function-independent: WXYZ, a four-unit cellular automaton implementing Wolfram's Rule 110 (Turing-complete), specifies a cause–effect structure with Φ = 2.8 ibits and 0.6 ibits complexes, markedly different from pQrS's Φ = 391.25, yet the computer fragments into the same ~24 trivial complexes when simulating it.
- By induction, an n-bit computer requires 2^n program instructions, n data registers, a 2^n-input multiplexer, and a buffer of 2n−5 units; it has 2^n + n + k + 1 complexes with the largest having Φ ≤ 3n/2 ibits, growing only linearly, while a rich target's Φ can reach O(2^(2^n)) ibits — a potentially double-exponential dissociation.

## Critical notes from the literature
- The authors explicitly state their conclusions hold "only to the extent that IIT itself can be considered valid"; future experiments could show consciousness is not associated with maximal intrinsic cause–effect power, which would invalidate IIT and these machine-consciousness results.
- The analysis does not rule out artificial consciousness altogether: neuromorphic computers mimicking the brain's physical organization, or quantum computers with entangled qubits, might achieve both functional and phenomenal equivalence — open questions the paper flags.
- Findings depend on computational bottlenecks (the processor/multiplexer forcing simulated constituents to overlap on the same physical substrate); the authors note the approach extends to CPUs/GPUs and brain–machine interfaces but acknowledge generalization to arbitrary computer architectures is conjectured, not proven (one worked example plus a conjecture that it generalizes).
- The work directly opposes computational functionalism and substrate-independence views; the authors cite counterarguments (e.g. that consciousness may require biological attributes, embodiment, or specific functions like global broadcasting or predictive processing) while arguing "consciousness is about being, not doing."

## Key topics covered
Integrated Information Theory (IIT 4.0); artificial consciousness vs. artificial intelligence; computational functionalism; functional vs. phenomenal equivalence; cause–effect structure and Φ (structure integrated information); system integrated information (φs); complexes, distinctions, relations; macroing / macro units / intrinsic units; Boolean unit causal models and TPMs; stored-program (Harvard) computer architecture; Turing completeness and Rule 110 cellular automaton; Church–Turing thesis; double-exponential dissociation; double dissociation of intelligence and consciousness; neuromorphic and quantum computing.
