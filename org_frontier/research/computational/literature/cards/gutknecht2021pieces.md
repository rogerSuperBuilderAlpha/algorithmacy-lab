---
citekey: gutknecht2021pieces
title: Bits and pieces: understanding information decomposition from part-whole relationships and formal logic
authors: Gutknecht, A. J. and Wibral, M. and Makkeh, A.
year: 2021
doi: 10.1098/rspa.2021.0110
arxiv: null
journal: Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2008.09535
sha256: dc65320690c85aa9617a0af469692200f991f24784aac5d7399fa2c6854533d3
pdf_path: literature/pdfs/gutknecht2021pieces.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Partial information decomposition (PID) aims to split the joint mutual information that a set of source variables carries about a target into "atoms" representing unique, redundant, and synergistic contributions. This paper re-derives the entire structure of PID from two elementary relations: part-whole (mereological) relations between information contributions, and logical implication between statements about source realizations. Each atom is characterized by a "parthood distribution," a monotonic Boolean function over collections of sources indicating whether the atom is part of the information each collection provides; the authors show the resulting structure is equivalent to the Williams-Beer redundancy lattice but approached directly from the atoms rather than indirectly via redundancy. Going to the pointwise level, they identify the pointwise redundancy of collections of source realizations with the information provided by the disjunction of the corresponding conjunctions of basic statements, recovering the shared-exclusions measure i_∩^sx of Makkeh et al. They prove that parthood distributions, antichains, and logical statements ordered by implication form three isomorphic lattices, giving a "logical" view of PID as a hierarchy of access constraints. Finally they use the parthood framework to systematically test whether PIDs can be built from quantities other than redundancy, showing this works for "restricted information," "weak synergy," and "moderate synergy" but fails for "strong synergy" and is trivial for unique information.

## Key facts it relies on
- A parthood distribution is a Boolean function f: P({1,...,n}) → {0,1} satisfying three constraints: f({}) = 0 (no information in the empty set), f({1,...,n}) = 1 (all information in the full set), and monotonicity (b ⊇ a and f(a)=1 implies f(b)=1) (Definition 1).
- The number of atoms equals the number of monotonic Boolean functions minus two (the two constant functions are ruled out); these counts are the Dedekind numbers, which for 2 ≤ n ≤ 6 are 6, 20, 168, 7581, 7828354. For two sources there are 4 atoms (synergy, two unique, shared); for three sources 18 atoms with 11 missing equations / 11 "proper" redundancies; for four sources 166 atoms.
- Core Principle 2 ("wholes are sums of their atomic parts") gives for two sources: I(T:S1,S2) = Π_red + Π_unq1 + Π_unq2 + Π_syn, I(T:S1) = Π_red + Π_unq1, I(T:S2) = Π_red + Π_unq2 (Eqs. 2.2-2.4); the four-unknown three-equation system is underdetermined.
- Redundant information I_∩ associated with a parthood distribution is the sum of atoms below and including it on the lattice (Eq. 2.10), so the atoms are recovered by Moebius inversion, which guarantees a unique solution for any real- or complex-valued I_∩ placed on the lattice.
- Any redundancy measure I_∩ implied by the parthood criterion automatically satisfies the Williams-Beer axioms: symmetry, idempotency, invariance under superset removal/addition, and self-redundancy I_∩(T:a) = I(T:a); these imply redundancy can be restricted to antichains.
- Pointwise mutual information i(t:s) = log(P(t|s)/P(t)) can be positive or negative; variable-level atoms are averages of pointwise atoms, Π(f) = Σ_{s1,...,sn,t} P(s1,...,sn,t) π(f) (Eq. 3.3).
- Core Principle 4: the redundancy of statements A1,...,Am is the information provided by their disjunction; this yields the measure i_∩^sx(t:a1,...,am) = i(t : ⋁_j ⋀_{i∈aj} Si=si) (Eq. 3.7), which is identical to the shared-exclusions measure of reference [12] and is implemented in the IDTxl toolbox [28].
- Theorem 1: for all n, the lattice of logical statements (L_n, ⊨̄) is isomorphic to the antichain lattice (A_n, ⪯) and the parthood-distribution lattice (B_n, ⊑); statements in L correspond exactly to propositional statements with monotonic truth-tables (Proposition 1).
- Using the parthood scheme, consistent non-redundancy-based PIDs are obtained from restricted information, weak synergy, and moderate synergy; strong synergy fails because it produces linearly dependent equations (e.g., for three sources Isyn(T:{1}{2}{3}) = Π({1,2,3}) = Isyn(T:{1,2}{1,3}{2,3})), and unique information only trivially defines each atom Iunq(T:α) = Π(α).

## Critical notes from the literature
- The authors note the measure i_∩^sx as well as the pointwise atoms π^sx can be negative and i_∩^sx can violate monotonicity; they argue these violations are fully attributable to "misinformative" contributions, since i_∩^sx splits uniquely into a non-negative informative part i_∩^sx+ and misinformative part i_∩^sx- (Eq. 6.1), each monotonic with non-negative induced atoms.
- The paper situates PID as a long-contested problem with "heated disputes over possible solutions," "simple but incomplete answers," and even claims "that the question should not be asked," and explicitly notes one quantitative monotonicity Williams-Beer axiom that the authors reject (§6).
- The synergy-centered decomposition using the "extended constraint lattice" (reference [15], resembling the authors' weak synergy) yields the same number of atoms but its "synergy atoms" S_∂ do not satisfy the consistency equation (2.5) except for the full set of sources, so they are not directly comparable to standard PID atoms and represent different types of information.
- The framework derives the structure of PID but still requires choosing a particular redundancy (or alternative) measure; the specific measure i_∩^sx is one proposal (motivated independently via logic and via shared exclusions), not a forced consequence, and the super-exponential growth of Dedekind numbers makes computing all atoms infeasible for large n.

## Key topics covered
Partial information decomposition (PID); mereology / part-whole relations; parthood distributions; monotonic Boolean functions; Dedekind numbers; redundant, unique, and synergistic information; Williams-Beer redundancy lattice and axioms; Moebius inversion; pointwise information theory; shared-exclusions redundancy measure i_∩^sx; logical statements / propositional logic lattice; antichain lattice isomorphism; restricted information, weak/moderate/strong synergy PIDs; constraint lattice; IDTxl toolbox; XOR example; misinformation and negativity of pointwise atoms.
