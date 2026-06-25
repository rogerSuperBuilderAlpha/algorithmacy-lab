---
citekey: kleiner2020mathematical
title: The Mathematical Structure of Integrated Information Theory
authors: Kleiner, Johannes and Tull, Sean
year: 2020
doi: 10.48550/arXiv.2002.07655
arxiv: null
journal: arXiv preprint
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2002.07655
sha256: c2c6e51751280c44d618150f4d8264d54cb0a888d902705de67fb25e400a3571
pdf_path: literature/pdfs/kleiner2020mathematical.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper asks what the essential mathematical structure of Integrated Information Theory (IIT) is, once the algorithm is separated from the auxiliary formal tools used in its standard presentation. The authors propound an axiomatic, generalized definition of IIT in which the theory is a map Sys → Exp from a class of physical systems (with states) into a class of experience spaces, sending each system S to its space of possible experiences E(S) and each state s to the actual experience E(S,s). They build this from minimal ingredients: a system class, experience spaces (a set with an intensity function, a distance function, and a scalar multiplication), and cause-effect repertoires expressed as "decompositions" of experiences. The IIT algorithm is then re-expressed concisely in terms of integration levels, integration scalings, and "cores." They prove the framework recovers classical IIT 3.0 of Tononi et al. and the Quantum IIT of Zanardi, Tomka and Campos Venuti as special cases, and show the generalization frees IIT from simplifying assumptions (discrete time, Markovian dynamics, discrete/compact state spaces) identified in the literature. The quantity of experience is Φ(S,s) = ‖E(S,s)‖ and the quality is the normalized experience; the experience is located in the "major complex," a subsystem of S.

## Key facts it relies on
- An IIT is formalized as a map Sys → Exp, sending each system S to its space of possible experiences E(S) and each state s ∈ St(S) to the actual experience E(S,s) ∈ E(S) (Figure 1; Definition 11; Eqs. 15-16).
- An experience space E is defined (Definition 2) as a set with: an intensity function ‖·‖: E → ℝ⁺; a distance function d: E × E → ℝ⁺; and a scalar multiplication ℝ⁺ × E → E satisfying ‖r·e‖ = r‖e‖, r·(s·e) = (rs)·e, and 1·e = e. The distance need not satisfy the axioms of a metric.
- The integration level of an element e with a decomposition over D is φ(e) := min over 1≠z∈D of d(e, ē(z)) (Eq. 5); the integration scaling is ι(e) := φ(e)·ê where ê is the normalization of e (Eq. 6).
- The quantity of a system's experience is Φ(S,s) := ‖E(S,s)‖ and the quality is the normalized experience Ê(S,s); the experience is located in the "major complex," a subsystem of S (Definition 11; Definition 10, Eq. 14).
- The framework recovers IIT 3.0 of Tononi et al. (classical IIT, Section 9) and Quantum IIT of Zanardi, Tomka and Campos Venuti [ZTV18] (Section 10) as special cases by supplying appropriate system classes and cause-effect repertoires.
- In classical IIT the space of proto-experiences is built from probability distributions P(S) over states with the first Wasserstein metric ("Earth Mover's Distance"); PE(S) := closure of P(S) (Eq. 24, Section 9.4).
- In quantum IIT, states are density matrices (positive semidefinite Hermitian operators of unit trace) on a Hilbert space H_S = ⊗ᵢ Hᵢ, and the proto-experience metric is the trace distance d(ρ,σ) = ½ tr_S(√((ρ−σ)²)) (Section 10).
- IIT 3.0 may only be applied to physical systems that have discrete time-evolution, satisfy Markovian dynamics, and exhibit a discrete set of states [BM19]; the paper shows in Section 11 how to redefine the maps (26) and (28) to cope with continuous time, non-Markovian dynamics, and non-compact state spaces while leaving the remaining structure intact.
- A companion article [TK20] (Tull and Kleiner, "Integrated Information in Process Theories") gives a categorical formulation in the language of symmetric monoidal categories that yields both classical and quantum IIT as special cases.
- The paper assumes each set of subsystems Sub_s(S) is finite (with the infinite case deferred to Section 12), and requires the number of subsystems to remain constant under cuts and changes of state.

## Critical notes from the literature
- The authors acknowledge (Section 12.2, with a dedicated footnote) that the IIT algorithm relies on a series of maximization and minimization operations unified as "core" subsystems, and that in general there is no guarantee these operations yield unique results in either classical or quantum IIT; using different cores has major impact on the output including the Φ value, which they describe as a case of "ill-definedness."
- They cite [BM19] (Barrett and Mediano, "The Phi measure of integrated information is not well-defined for general physical systems") as the source of the criticisms their extensions are designed to address, including the non-canonical-metrics critique that different metric choices imply different algorithm results.
- The authors state the non-canonical-metrics problem is not technical but conceptual/philosophical: resolving it requires justifying why a particular metric should be used, ideally by defining the distance d in terms of the phenomenological structure of similarity of conscious experiences (Section 11.3).
- They note their formalization (and the contemporary definition) relies on there being a finite number of subsystems per system, which "might not be the case in reality," and that a fully phenomenologically grounded understanding of how experience-space structure corresponds to the phenomenology of experience (e.g., qualia) remains an open task (Section 12.2).
- The paper positions itself as a contribution to ongoing critical discussion of IIT, citing critiques and analyses including [Bay18], [MSB19], [MRCH+19], and [TK15].

## Key topics covered
Integrated Information Theory (IIT 3.0); axiomatic/generalized IIT; experience spaces (intensity, distance, scalar multiplication); cause-effect repertoires and structure; decompositions; integration level (φ); integration scaling; cores and core integration scaling; concepts and concept space; Q-shape; major complex; Φ value (quantity) and quality of experience; classical IIT system class; transition probability matrices; conditioning, marginalizing, conditional independence; cuts and minimum information partition (MIP); Earth Mover's Distance / Wasserstein metric; Quantum IIT; density matrices and trace distance; extensions to continuous time, non-Markovian dynamics, and non-compact state spaces; non-canonical metrics; category-theoretic/process-theory formulation; qualia space and constellation of concepts.
