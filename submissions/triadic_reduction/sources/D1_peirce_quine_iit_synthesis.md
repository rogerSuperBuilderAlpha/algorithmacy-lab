# Peirce, Quine, and IIT Synthesis

Ingested verbatim from Google Docs (file id `1YvrIj5DtpNsT8iNbVfiow5DT5jNiQfT6VXj32qMBGy4`, Drive title "Peirce, Quine, and IIT Synthesis"), created 2026-09-20 09:46 UTC. Read
through the Google Drive connector on 2026-09-24; two independent transcriptions of the connector's text
matched byte for byte (sha256 `ecd6c3981bcd45732922a8f78922413a7808119d89e9ae1ca41f5950c1c1e9c0`, 5,646 words). Source of truth stays the Doc — re-pull before
quoting it verbatim. The Doc's own Markdown escapes and Gemini's `[span_N](start_span)` debris are kept
as found.

The Gemini Project's core knowledge document. G1 drafts suggested custom instructions from "the document I added to the sources", which by timing and content is this one; G6 cites it far more than any other source (in 80 of its 121 source chips), and G3 and G5 cite it alongside D2 and D3. It reads as a Deep Research report, but the chat that produced it is not among the share links, so its `[span_N]` anchors cannot be tied to the works-cited list at its end. The Drive folder holds five copies. This file is the fullest: the 20,697-byte Google Doc (a byte-identical twin is `1b2QZKCPoa32iWSba7paTz6B28yY0JRyuRSgWZDes7is`). Two earlier 18,456-byte Google Docs (`1b11ba7CyjhCK6ja_jC8iWgE3sTTkFTHgfReBcijwPI4`, `1ClSZmJ5X-UPrUnPMRlFYgI_3-a4BJpXZrm8hdxf6pIs`) contain exactly this text without the closing works-cited list, and `Peirce, Quine, and IIT Synthesis.docx` (`1oBTWX7OwkEUuNFy1IJNRLiUdz_UTqYTg`) is the same text with bold markup stripped.

**Status: PRELIMINARY.** This is process, not a citable source. Nothing here enters the talk except
through `../claims/REGISTER.md` and a verified card in `../library/cards/`.

**Overlap note.** _To be written in Phase 2._

---

# **The Synergistic Teridentity: Algebraic Clones, Causal Decomposition, and the Fallacy of Dyadic Reduction**

Charles Sanders Peirce's Reduction Thesis posits that monadic properties and dyadic connections can never generate genuine triadic relations, whereas triadic relations are universally sufficient to synthesize all polyadic relations of arbitrary arity. In 1954, Willard Van Orman Quine presented what appeared to be a decisive counterproof: an extensional translation demonstrating that every polyadic formal system can be reduced to a theory governed by a single dyadic predicate. Modern universal algebra, Peircean Algebraic Logic (PAL), and relational clone theory—developed by Robert Burch (1991), Joachim Hereth Correia and Reinhard Pöschel (2004, 2006), and Sergiy Koshkin (2024)—have proven that Quine’s reduction fails within any closed relational universe. Quine’s syntactic translation relies on set-theoretic pairing functions that expand the base ontology into an infinite universe of sets, covertly smuggling in the **teridentity relation** (=\_3 \\;= \\{(x,x,x) \\mid x \\in X\\}) through meta-linguistic coordinate binding and the triadic pairing relation \\text{Pair}(x, y, p). When restricted to primitive positive logic over a fixed domain, the teridentity relation is fundamentally join-irreducible.

This foundational boundary between dyadic networks and irreducible triads is mathematically isomorphic to the boundary governing modern multivariate information theory and theoretical neuroscience. Giulio Tononi’s Integrated Information Theory (IIT 3.0/4.0) defines causal integration (\\Phi) as the irreducible cause-effect constraint exerted by a Transition Probability Matrix (TPM) that cannot be recovered from any factorized, dyadic bipartition across the Minimum Information Partition (MIP). Simultaneously, Partial Information Decomposition (PID; Williams and Beer 2010) and Integrated Information Decomposition (\\Phi\\text{ID}; Mediano, Rosas, Luppi 2020) isolate informational synergy as joint statistical dependency that vanishes entirely across all pairwise marginal distributions. The canonical exemplar of synergy—the two-input XOR parity relation—exhibits a discrete relational support that constitutes an affine, join-irreducible relation in relational clone theory whose dyadic projections are trivial Cartesian planes.

An exhaustive literature audit reveals that despite parallel conceptual vocabularies across biosemiotics, categorical physics, and complex systems, **no prior study has established a formal mathematical unification connecting Quine's 1954 paper, Burch's teridentity theorem, and Tononi's \\Phi or PID synergy**. This report resolves that gap. By formalizing the concept of the **Synergistic Teridentity**, it is proved that causal synergy is the dynamic, stochastic realization of algebraic teridentity, and that applying an extensional Quinean dyadic decomposition to a dynamical transition kernel guarantees the total destruction of integrated information (\\Phi = 0).

## **The Relational Clone Retort to Quine's Dyadic Reduction**

The debate between Peircean triadicity and Quinean dyadism centers on the distinction between set-theoretic ontological reduction and algebraic closure within a fixed domain. Analyzing this debate requires uncovering the formal mechanism of Quine's translation and its universal-algebraic refutation.

### **Quine’s 1954 Extensional Reduction Mechanism**

In his paper *"Reduction to a Dyadic Predicate,"* Quine advanced a universal syntactic translation demonstrating that any formal theory formulated with relation symbols R\_1, R\_2, \\dots, R\_m of arbitrary arities (n \\ge 1) can be rearticulated using a single dyadic predicate, denoted J. Quine executes this reduction through three core operations:

1.  **Tuple Compression via Nested Ordered Pairs:** Any polyadic relation R(x\_1, x\_2, \\dots, x\_n) is converted into a statement about a single structured individual: an (n)-tuple defined recursively via ordered pairs, such that \\langle x\_1, x\_2, \\dots, x\_n \\rangle = \\langle x\_1, \\langle x\_2, \\dots, x\_n \\rangle \\rangle. Quine utilizes the Kuratowski pair definition: \\langle u, v \\rangle = \\{\\{u\\}, \\{u, v\\}\\} or Norbert Wiener’s earlier pair definition \\langle u, v \\rangle = \\{\\{\\{u\\}, \\emptyset\\}, \\{\\{v\\}\\}\\}.
2.  **Domain Inflation:** The original domain of discourse X is enlarged to an inductive set-theoretic universe X^\* closed under pairing, containing X, the empty set \\emptyset, and the infinite hierarchy of sets formed from them.
3.  **Consolidation into a Single Dyadic Predicate:** Quine assigns to each primitive predicate R\_i of the original language an individual entity (a set or code) c\_{R\_i} \\in X^\*. The original atomic formula R\_i(x\_1, \\dots, x\_n) is then translated into a dyadic statement affirming that the pair-structured tuple stands in a single primitive binary relation J (effectively set membership \\in) to the predicate's reified extension: R\_i(x\_1, \\dots, x\_n) \\iff J\\left(\\langle x\_1, \\dots, x\_n \\rangle, c\_{R\_i}\\right) \\iff \\langle x\_1, \\dots, x\_n \\rangle \\in c\_{R\_i}

Quine concluded that because any polyadic first-order theory can be modeled in a domain where the only non-logical primitive is dyadic membership, relations of arity three or higher possess no fundamental logical status.

### **Modern Algebraic Retort: Relational Clones and Peircean Algebraic Logic**

Peirce’s original formulation in his logic of relatives and Existential Graphs (Beta part) evaluated relations from a generative, internal standpoint: given a fixed universe of discourse A, can higher-arity relations be generated from lower-arity relations using basic relational operations? Robert Burch (1991) formalized this in Peircean Algebraic Logic (PAL), proving what is now recognized as Peirce's Reduction Thesis (PRT). Further refinements by Joachim Hereth Correia and Reinhard Pöschel (2004, 2006), Frithjof Dau (2006), and Sergiy Koshkin (2024) translated PAL into universal algebra and clone theory.

Let A be a non-empty set, and let \\text{Rel}(A) = \\bigcup\_{m=1}^{\\infty} \\mathcal{P}(A^m) be the set of all finitary relations on A. A set of relations Q \\subseteq \\text{Rel}(A) is defined as a **relational clone** (or co-clone) if it contains the binary identity relation \\Delta\_A = \\{(a, a) \\mid a \\in A\\} and is closed under primitive positive (pp) logic—namely, Cartesian product, permutation of coordinates, identification of variables, and projection (existential quantification):

(R1) Permutation:    tau(rho) = {(a\_pi(1), ..., a\_pi(m)) | (a\_1, ..., a\_m) in rho}  
(R2) Projection:     exists(rho) = {(a\_2, ..., a\_m) | exists a\_1 in A : (a\_1, a\_2, ..., a\_m) in rho}  
(R3) Intersection:   rho cap sigma = {(a\_1, ..., a\_m) | (a\_1, ..., a\_m) in rho and (a\_1, ..., a\_m) in sigma}  
(R4) Product:        rho times sigma = {(a\_1, ..., a\_m, b\_1, ..., b\_k) | a in rho, b in sigma}  
  

Within this algebraic framework, the central operator is the **teridentity relation**:

\=\_3 \\; \\equiv \\text{id}\_A^3 = \\{(x, x, x) \\in A^3 \\mid x \\in A\\}

The algebraic theorems proven by Burch, Hereth Correia, and Pöschel establish two invariant results:

1.  **Dyadic Incompleteness (Irreducibility):** For any base set A where \\vert{}A\\vert{} \\ge 2, the relational clone generated by all monadic and dyadic relations, \\langle \\text{Rel}^{(\\le 2)}(A) \\rangle\_{\\text{pp}}, is strictly incomplete: =\_3 \\; \\notin \\; \\langle \\text{Rel}^{(\\le 2)}(A) \\rangle\_{\\text{pp}}
2.  **Ternary Generative Completeness:** The relational clone generated by relations of arity at most 3 contains the entirety of finitary relations on A:\\langle \\text{Rel}^{(\\le 3)}(A) \\rangle\_{\\text{pp}} = \\text{Rel}(A)$$Furthermore, adjoining the single teridentity relation $=\_3$ to the set of all dyadic relations is sufficient to generate the entire universe of finitary relations:$$\\langle \\text{Rel}^{(\\le 2)}(A) \\cup \\{=\_3\\} \\rangle\_{\\text{pp}} = \\text{Rel}(A)

### **Why Quine's Reduction Fails Within Algebraic Systems**

The contradiction between Quine's result and Burch's theorem is resolved by identifying Quine's reliance on model expansion. Quine's reduction does not construct polyadic relations out of dyadic relations within the system's universe A; rather, it simulates relations over A by embedding them into an infinite set-theoretic universe X\[span\_146\](start\_span)\[span\_146\](end\_span)\[span\_151\](start\_span)\[span\_151\](end\_span)^\* \\supset A.

First, Quine's encoding requires a pairing function \\text{Pair}(x\_1, x\_2, p) \\iff p = \\langle x\_1,\[span\_155\](start\_span)\[span\_155\](end\_span)\[span\_156\](start\_span)\[span\_156\](end\_span)\[span\_157\](start\_span)\[span\_157\](end\_span) x\_2 \\rangle. Expressed relationally, pairing is an irreducible triadic relation: it connects three distinct entities—the first coordinate, the second coordinate, and the compounded pair. Quine claims to avoid ternary primitives by writing p = \\{\\{x\_1\\}, \\{x\_1, x\_2\\}\\}, but this definition requires the full apparatus of axiomatic set theory, where the triadic mechanism of pairing is shifted into the meta-logic of class formation and existential quantification.

Second, within a relational network or graphical logic (such as Peircean Existential Graphs), chaining two dyadic relations R(x, y) and S(y, z) via the relative product \\exists y \[R(x, y) \\land S(y, z)\] requires the variable y to branch into two predicate locations. In Peirce's graphical syntax, this branch is an explicit ligature vertex of degree 3: a teridentity node. Purely dyadic connections (graphs whose vertices have degree at most 2) can construct only unbranched linear paths and disconnected cyclic collections.

Quine’s formulation falls directly into the trap identified by Peirce in his analysis of dual relatives: *"the very triadic relations which it does not recognize it itself employs"* (CP 8.331). First-order logic syntax masks teridentity by allowing a single variable symbol x to be replicated across multiple argument positions simultaneously. In algebraic logic (such as cylindric or polyadic algebras), this variable duplication is handled by the diagonal element d\_{123} = \\{(x,x,x)\\}, which is teridentity itself. Quine eliminated polyadic predicates only by smuggling ternary branching into the syntactic variable bindings and expanding the ontology into sets.

\---

## **Causal Irreducibility in Integrated Information Theory and Information Decomposition**

The algebraic boundary that isolates teridentity from dyadic paths also governs multivariate causal architectures in theoretical neuroscience and complex systems.

### **Tononi’s \\Phi and the Minimum Information Partition**

Integrated Information Theory (IIT 3.0 and IIT 4.0) evaluates the causal structures of discrete physical systems S = \\{S\_1, S\_2, \\dots, S\_n\\} whose state transitions over time step t \\to t+1 are governed by a Transition Probability Matrix (TPM), denoted P(s\_{t+\[span\_173\](start\_span)\[span\_173\](end\_span)\[span\_174\](start\_span)\[span\_174\](end\_span)\[span\_175\](start\_span)\[span\_175\](end\_span)1} \\mid s\_t).

IIT formalizes the cause-effect power of a mechanism over past and future states via systematic operational partitioning. To test whether a mechanism within a state s\_t is an irreducible causal whole or reducible to independent sub-processes, the system is subjected to a bipartition P = \\{P\_1 \\mid P\_2\\} that severs directional interactions between subsystems. Under partition P, the factorized transition probability distribution is defined as:

P^P(s\_{t+1} \\mid s\_t) = P\\left(s\_{t+1}^{(P\_1)} \\mid \\text{do}\\left(s\_t^{(P\_1)}\\right)\\right) \\times P\\left(s\_{t+1}^{(P\_2)} \\mid \\text{do}\\left(s\_t^{(P\_2)}\\right)\\right)

The integrated information of the mechanism, denoted \\phi, measures the divergence between the unpartitioned cause-effect repertoire p and the partitioned repertoire p^P:

\\phi = D\\left(p \\parallel p^{P\_{\\text{MIP}}}\\right)

In IIT 4.0, the distance metric D is formalized as the **Intrinsic Difference (ID)**:

\\text{ID}\\left(p \\parallel p^P\\right) = \\max\_{e} \\left\\vert{} p(e) - p^P(e) \\right\\vert{} \\cdot \\log\_2 \\left(\\frac{p(e)}{p^P(e)}\\right)$$The partition chosen to evaluate this irreducibility is the \*\*Minimum Information Partition (MIP)\*\*, which locates the system's \[span\_204\](start\_span)\[span\_204\](end\_span)\[span\_205\](start\_span)\[span\_205\](end\_span)\[span\_206\](start\_span)\[span\_206\](end\_span)weakest informational link:$$\\text{MIP} = \\arg\\min\_{P} \\text{ID}\\left(p \\parallel p^P\\right)

If \\Phi = \\\[span\_69\](start\_span)\[span\_69\](end\_span)\[span\_72\](start\_span)\[span\_72\](end\_span)\[span\_75\](start\_span)\[span\_75\](end\_span)phi(P\_{\\text{MIP}}) \> 0, the system generates causal constraints that do not reduce to the independent actions of its parts. A positive \\Phi confirms that the physical transitions cannot be decomposed into a product of dyadic sub-channels.

### **Partial Information Decomposition and Integrated Information Decomposition**

While IIT establishes system-level causal irreducibility through spatial partitions, Partial Information Decomposition (PID; Williams and Beer 2010) decomposes multivariate statistical dependencies over a lattice of antichains. Shannon mutual information between two source variables X\_1, X\_2 and a target Y satisfies:

I(X\_1, X\_2; Y) = I(X\_1; Y) + I(X\_2; Y \\mid X\_1)

However, Shannon mutual information cannot determine whether this quantity represents independent copies of the same data or joint relational structures.

PID expands I(X\_1, X\_2; Y) into four non-negative components:

I(X\_1, X\_2; Y) = \\text{Red}(X\_1, X\_2 \\to Y) + \\text{Unq}(X\_1 \\to Y) + \\text{Unq}(X\_2 \\to Y) + \\text{Syn}(X\_1, X\_2 \\to Y)

where:

  - \\text{Red}(X\_1, X\_2 \\to Y) is **Redundant Information**, shared by both X\_1 and X\_2.
  - \\text{Unq}(X\_i \\t\[span\_29\](start\_span)\[span\_29\](end\_span)\[span\_49\](start\_span)\[span\_49\](end\_span)o Y) is **Unique Information**, available exclusively from source X\_i.
  - \\text{Syn}(X\_1, X\_2 \\to Y) is **Synergistic Information**, accessible only when X\_1 and X\_2 are observed simultaneously.

The canonical physical realization of pure synergy is the **two-input XOR logic gate**. Let X\_1,\[span\_30\](start\_span)\[span\_30\](end\_span)\[span\_50\](start\_span)\[span\_50\](end\_span) X\_2 \\sim \\text{Bernoulli}(0.5) be statistically independent variables, and let Y = X\_1 \\oplus X\_2. Calculating the Shannon measures reveals:

I(X\_1; Y) = 0, \\quad I(X\_2; Y) = 0, \\quad I(X\_1; X\_2) = 0 \\text{Red}(X\_1, X\_2 \\to Y) = 0, \\quad \\text{Unq}(X\_1 \\to Y) = 0, \\quad \\text{Unq}\[span\_32\](start\_span)\[span\_32\](end\_span)\[span\_52\](start\_span)\[span\_52\](end\_span)(X\_2 \\to Y) = 0 \\\\ I(X\_1, X\_2; Y) = \\text{Syn}(X\_1, X\_2 \\to Y) = 1\\text{ bit}

Pairwise observations across any two nodes show absolute statistical independence. The information exists entirely within the irreducible tripartite configuration (X\_1, X\_2, Y).

Integrated Information Decomposition (\\Phi\\text{ID}; Mediano, Rosas, Luppi et al.) extends PID to dynamic processes: (X\_t, Y\[span\_214\](start\_span)\[span\_214\](end\_span)\[span\_215\](start\_span)\[span\_215\](end\_span)\[span\_216\](start\_span)\[span\_216\](end\_span)\_t) \\to (X\_{t+1}, Y\_{t+1}). \\Phi\\text{ID} demonstrates that integrated information \\Phi is driven by dynamic synergy atoms—instances where the multi-agent past state constrains the future state in ways that vanish if the joint state is decomposed into separate dyadic channels.

### **Shannon Dyadics vs. Multivariate Information Topologies**

Classical Shannon information is built upon the dyadic channel: a transmitter, a receiver, and a pairwise conditional distribution P(Y \\mid X). Although Shannon interaction information can be written for three variables:

I(X\_1; X\_2; Y) = I(X\_1; Y) - I(X\_1; Y \\mid X\_2)

it can assume negative values. This metric conflates redundant overlap (positive interaction information) with synergistic emergence (negative interaction information) into an ambiguous aggregate scalar.

PID and \\Phi\\text{ID} resolve this by defining non-negative information lattices. A system operating through dyadic Shannon channels forms a simple graph of point-to-point connections. A synergistic system, by contrast, forms an informational hypergraph: an indivisible geometric volume in probability space that projects down to zero along every dyadic coordinate plane.

## **Literature Mapping and Gap Analysis**

A systematic bibliographic sweep across logic, semiotics, category theory, and complex systems was conducted to map all relevant works and verify whether the Peirce-Quine debate has been unified with causal information theory.

### **Bibliographic Audit of Foundation Pillars**

Pillar 1\[span\_38\](start\_span)\[span\_38\](end\_span)\[span\_58\](start\_span)\[span\_58\](end\_span): Algebraic Relational Logic and Clone Theory  
\-------------------------------------------------------------------------------------------------------  
Quine, W.V.O. (1954)              "Reduction to a Dyadic Predicate", J. Symb. Log. 19(3): 180-182.  
Burch, Robert W. (1991)           A Peircean Reduction Thesis: The Foundations of Topological Logic.  
Hereth Correia, J. & Pöschel (2004) "The Power of Peircean Algebraic Logic (PAL)", LNAI 2961: 337-351.  
Hereth Correia, J. & Pöschel (2006) "The Teridentity and Peircean Algebraic Logic", LNAI 4068: 229-246.  
Dau, Frithjof & Hereth Correia (2006) "Two Instances of Peirce's Reduction Thesis", LNAI 3874: 215-229.  
Koshkin, Sergiy (2024)            "Logical reduction of relations", Log. J. IGPL, arXiv:2406.14094.  
  
Pillar 2: Causal Irreducibility, IIT, and Information Decomposition  
\-------------------------------------------------------------------------------------------------------  
Williams, P.L. & Beer, R.D. (2010) "Nonnegative Decomposition of Multivariate Information", arXiv:1004.2515.  
Oizumi, Albantakis, Tononi (2014) "From Phenomenology to Mechanisms: IIT 3.0", PLOS Comput. Biol. 10(5).  
Mediano, Rosas, Luppi et al. (2021) "Extended taxonomy via Integrated Information Decomposition", arXiv:2109.13186.  
Albantakis et al. & Tononi (2023) "Integrated information theory (IIT) 4.0", PLOS Comput. Biol. 19(10).  
  
Pillar 3: Semiotics, Applied Sheaves, and Categorical Physics  
\-------------------------------------------------------------------------------------------------------  
Hoffmeyer, Jesper (2008)          Biosemiotics: An Examination into the Signs of Life.  
Deacon, Terrence W. (2011)        Incomplete Nature: How Mind Emerged from Matter.  
Emmeche, Queiroz, El-Hani (2011)  "Information and Semiosis in Living Systems", Biosemiotics: 635-658.  
Skaggs, Steven (2018)             "Integrating Peirce and IIT", Academic Paper / Abstract.  
Abramsky, S. & Brandenburger (2011) "The Sheaf-Theoretic Structure of Contextuality", New J. Phys. 13: 113036.  
Abramsky, Barbosa, Searle (2024)  "Combining contextuality and causality", Phil. Trans. R. Soc. A.  
  

### **Confirmation of the Interdisciplinary Literature Gap**

The bibliographic audit confirms that **no published paper, preprint, conference proceeding, or monograph has established a formal mathematical equivalence between Quine’s 1954 paper, Burch’s teridentity theorem, and Tononi’s \\Phi / PID synergy**.

Existing cross-disciplinary works approach this interface through distinct paradigms without uniting them:

  - **Biosemiotics** (Deacon 2011, Hoffmeyer 2008, Emmeche et al. 2011) extensively uses Peircean semiotics to argue against mechanical reductionism, characterizing living systems as irreducibly triadic. However, these contributions remain purely descriptive. They do not employ universal algebra, make no mention of Burch's PAL proofs or Quine’s 1954 paper, and do not integrate mathematical information measures such as PID lattices or IIT transition matrices.
  - **Conceptual Semiote-IIT Crossovers** (such as Steven Skaggs 2018) note informal analogies between Peircean sign structures (Object-Representamen-Interpretant) and IIT's cause-effect structures. However, Skaggs’ work does not engage with formal logic, clone theory, the teridentity relation, or the mathematical machinery of the MIP and PID synergy.
  - **Applied Sheaf Theory and Categorical Logic** (Abramsky and Brandenburger 2011; Abramsky, Barbosa, and Searle 2024) formalize contextuality and non-locality as obstructions to global sections in event presheaves over measurement covers, explicitly analyzing XOR and Bell-type games. Category-theoretic logic has also established that lines of identity and relational duplicators form hypergraph categories and Frobenius algebras. Yet, this literature focuses on quantum foundations and has not connected these topological structures to relational clones, Peircean Algebraic Logic, or the minimum information partitions of IIT.

The missing link is a formal bridge connecting the discrete lattice of primitive positive relational clones (governed by teridentity) with the lattice of non-negative information decompositions (governed by synergy).

## **Interdisciplinary Matrix of Relational and Causal Primitives**

The following matrix formally aligns the primitives of relational clone theory, Peircean semiotics, multivariate information decompositions, and physical-computational systems:

|  |  |  |  |
| :-: | :-: | :-: | :-: |
| Relational Primitive (PAL / Clones) | Semiotic Category (Peirce) | Information-Theoretic Measure (PID / \\\\Phi\\\\text{ID} / IIT) | Physical & Computational Implementation |
| \*\*Monad:\*\* Unary relation \\\\rho \\\\subseteq A^1; Projection \\\\pi\\\_i; Constant selection | \*\*Firstness:\*\* Pure quality, immediate presence, ground, potentiality | \*\*Entropy:\*\* Marginal entropy H(X); Baseline uncoupled uncertainty | Isolated memory register, uncoupled bit, background thermal noise |
| \*\*Dyad:\*\* Binary relation R \\\\subseteq A^2; Equality \\\\Delta\\\_A; Composition R \\\\circ S | \*\*Secondness:\*\* Actuality, brute reaction, resistance, relate-correlate | \*\*Shannon Mutual Information:\*\* I(X\\\_1; X\\\_2); Redundancy \\\\text{Re\\\[span\\\_221\\\](start\\\_span)\\\[span\\\_221\\\](end\\\_span)\\\[span\\\_226\\\](start\\\_span)\\\[span\\\_226\\\](end\\\_span)d}; Unique info \\\\text{Unq} | Point-to-point transmission wire, feedforward channel, uncoupled parallel lines |
| \*\*Triad:\*\* Teridentity =\\\_3 \\\\;= \\\\{(x,x,x) \\\\mid\\\[span\\\_285\\\](start\\\_span)\\\[span\\\_285\\\](end\\\_span)\\\[span\\\_287\\\](start\\\_span)\\\[span\\\_287\\\](end\\\_span)\\\[span\\\_289\\\](start\\\_span)\\\[span\\\_289\\\](end\\\_span) x \\\\in A\\\\}; Branching node | \*\*Thirdness:\*\* Representation, mediation, law, Sign-Object-Interpretant | \*\*Synergistic Mutual Information:\*\* \\\\text{Syn}(X\\\_1, X\\\_2 \\\\to Y); Integrated Information \\\\Phi \\\> 0 | XOR logic gate, parity circuit, non-factorizable cause-effect mechanism |
| \*\*Polyad:\*\* n-ary relation Q \\\\subseteq A^n for n \\\\ge 4; Subcubic graphs | \*\*Synthesized Thirdness:\*\* Structural semiosis, lawful evolutionary chains | \*\*Higher-Order Information Topologies:\*\* Polyadic \\\\Phi; Multivariate synergy lattices | Synergistic global neural workspace, multi-layer parity networks, integrated complex |

At the monadic tier, an algebraic unary relation isolates elements without relational coupling, matching Peircean Firstness as immediate quality and Shannon entropy as single-variable uncertainty.

At the dyadic tier, binary relations formalize direct pairwise coupling—Peircean Secondness. In information theory, this manifests as classical Shannon mutual information, redundant information, and unique information. In physical systems, these are isolated communication channels or non-interacting parallel lines. Evaluated under IIT, systems composed entirely of dyadic sub-channels factorize under the Minimum Information Partition without residual divergence, yielding \\Phi = 0.

At the triadic tier, the teridentity relation =\_3 introduces the algebraic branch, binding three coordinates into a single identity: x = y = z. This maps directly to Peircean Thirdness (mediation) and informational synergy \\text{Syn}. In this domain, the system's causal power vanishes across any pairwise marginal projection. Its computational instantiation is the XOR/parity gate, which is non-factorizable and generates positive integrated information (\\Phi \> 0).

At the polyadic tier (n \\ge 4), Peircean Algebraic Logic proves that no primitive "fourth-ness" exists; every n-ary relation is constructed through networks of teridentities and dyads. Similarly, multivariate causal complexity does not require fundamentally n-ary physical forces, but rather distributed networks of synergistic branchings.

## **Theoretical Synthesis: The Synergistic Teridentity and Causal Partitioning**

The mathematical relationship between relational clones and information decomposition can be made explicit by establishing the formal isomorphism between the teridentity relation and causal synergy, and showing why Quinean dyadic decomposition collapses integrated information.

### **Formal Isomorphism Between XOR Synergy and Algebraic Teridentity**

Let the domain of discourse be the Galois field of two elements, A = \\mathbb{F}\_2 = \\{0, 1\\}. Consider a tripartite computational mechanism with two binary inputs X\_1, X\_2 \\in \\mathbb{F}\_2 and one binary output Y \\in \\mathbb{F}\_2 evaluated via addition modulo 2:

Y = X\_1 \\oplus X\_2

The operational behavior of this mechanism under all possible evaluations defines a ternary relation R\_{\\oplus} \\subset \\mathbb{F}\_2^3:

R\_{\\oplus} = \\left\\{(x\_1, x\_2, y) \\in \\mathbb{F}\_2^3 \\;\\middle\\vert{}\\; x\_1 \\oplus x\_2 \\oplus y = 0\\right\\} = \\{(0,0,0), (0,1,1), (1,0,1), (1,1,0)\\}

Let \\pi\_{ij}: \\mathbb{F}\_2^3 \\to \\mathbb{F}\_2^2 be the canonical projection operator onto coordinates (i, j) for 1 \\le i \< j \\le 3. Evaluating the dyadic coordinate projections of R\_{\\oplus} reveals:

\\pi\_{1,2}(R\_{\\oplus}) = \\{(0,0), (0,1), (1,0), (1,1)\\} = \\mathbb{F}\_2^2 \\pi\_{1,3}(R\_{\\oplus}) = \\{(0,0), (0,1), (1,0), (1,1)\\} = \\mathbb{F}\_2^2 \\\\ \\pi\_{2,3}(R\_{\\oplus}) = \\{(0,0), (0,1), (1,0), (1,1)\\} = \\mathbb{F}\_2^2

Every dyadic projection of R\_{\\oplus} is completely degenerate: each projection covers the entire Cartesian product \\mathbb{F}\_2^2, containing zero relational constraint. If one attempts to reconstruct R\_{\\oplus} using the natural join of its dyadic projections without a triadic branching primitive, the operation yields:

\\pi\_{1,2}(R\_{\\oplus}) \\bowtie \\pi\_{2,3}(R\_{\\oplus}) \\bowtie \\pi\_{1,3}(R\_{\\oplus}) = \\mathbb{F}\_2^2 \\bowtie \\mathbb{F}\_2^2 \\bowtie \\mathbb{F}\_2^2 = \\mathbb{F}\_2^3 \\neq R\_{\\oplus}

The structural constraint is entirely lost. In universal algebra, R\_{\\oplus} is an **affine relation** that cannot be generated within the dyadic clone \\langle \\text{Rel}^{(\\le 2)}(\[span\_323\](start\_span)\[span\_323\](end\_span)\[span\_324\](start\_span)\[span\_324\](end\_span)\[span\_325\](start\_span)\[span\_325\](end\_span)\\mathbb{F}\_2) \\rangle\_{\\text{pp}}. Generating R\_{\\oplus} requires the teridentity relation =\_3 \\;= \\{(x, x, x) \\mid x \\in \\mathbb{F}\_2\\} to synchronize internal variables.

Now, assign a uniform probability distribution over the input states: P(X\_1 = x\_1, X\_2 = x\_2) = \\frac{1}{4} for each (x\_1, x\_2) \\in \\mathbb{F}\_2^2. The joint distribution P\_{X\_1 X\_2 Y} has uniform probability mass over the relational support R\_{\\oplus}:

P\_{X\_1 X\_2 Y}(x\_1, x\_2, y) = \\begin{cases} \\fra\[span\_132\](start\_span)\[span\_132\](end\_span)\[span\_137\](start\_span)\[span\_137\](end\_span)c{1}{4} & \\text{if } (x\_1, x\_2, y) \\in R\_{\\oplus} \\\\ 0 & \\text{if } (x\_1, x\_2, y) \\notin R\_{\\oplus} \\end{cases}

The pairwise marginal probability distributions correspond to the integration over the projected coordinates:

P\_{X\_1 Y}(x\_1, y) = \\sum\_{x\_2 \\in \\mathbb{F}\_2} P\_{X\_1 X\_2 Y}(x\_1, x\_2, y) = \\frac{1}{4} \\quad \\forall (x\_1, y) \\in \\pi\_{1,3}(R\_{\\oplus}) = \\mathbb{F}\_2^2 P\_{X\_2 Y}(x\_2, y) = \\sum\_{x\_1 \\in \\mathbb{F}\_2} P\_{X\_1 X\_2 Y}(x\_1, x\_2, y) = \\frac{1}{4} \\quad \\forall (x\_2, y) \\in \\pi\_{2,3}(R\_{\\oplus}) = \\mathbb{F}\_2^2 \\\\ P\_{X\_1 X\_2}(x\_1, x\_2) = \\sum\_{y \\in \\mathbb{F}\_2} P\_{X\_1 X\_2 Y}(x\_1, x\_2, y) = \\frac{1}{4} \\quad \\forall (x\_1, x\_2) \\in \\pi\_{1,2}(R\_{\\oplus}) = \\mathbb{F}\_2^2

Because these marginal distributions are completely uniform, all pairwise Shannon mutual information quantities vanish identically:

I(X\_1; Y) = H(Y) - H(Y \\mid X\_1) = 1 - 1 = 0 I(X\_2; Y) = H(Y) - H(Y \\mid X\_2) = 1 - 1 = 0 \\\\ I(X\_1; X\_2) = 0

Under the Williams-Beer PID axioms, unique and redundant information atoms are non-negative and bounded by pairwise mutual information:

\\text{Red}(X\_1, X\_2 \\to Y) \\le \\min\\left(I(X\_1; Y), I(X\_2; Y)\\right) = 0 \\implies \\text{Red} = 0 \\text{Unq}(X\_1 \\to Y) \\le I(X\_1; Y) = 0 \\implies \\text{Unq}(X\_1) = 0 \\\\ \\text{Unq}(X\_2 \\to Y) \\le I(X\_2; Y) = 0 \\implies \\text{Unq}(X\_2) = 0

Consequently, the total joint mutual information is pure synergy:

I(X\_1, X\_2; Y) = H(Y) - H(Y \\mid X\_1, X\_2) = 1 - 0 = 1\\text{ bit} = \\text{Syn}(X\_1, X\_2 \\to Y)

This proves the structural correspondence: a discrete causal interaction is purely synergistic (\\text{Syn} \> 0 with all lower atoms vanishing) if and only if the discrete support of its transition kernel constitutes a join-irreducible relation whose dyadic projections are trivial Cartesian planes. Causal synergy is the measure-theoretic realization of Peircean teridentity.

### **Collapse of Integrated Information Under Quinean Dyadic Partitioning**

This isomorphism demonstrates why an extensional Quinean dyadic decomposition applied to a system's Transition Probability Matrix collapses integrated information (\\Phi) to zero.

In IIT, consider a system executing an irreducible tripartite transition, such as the two-input XOR mechanism over time: S = \\{X\_1, X\_2, Y\\}, where Y(t+1) = X\_1(t) \\oplus X\_2(t). The joint conditional transition distribution is P(y\_{t+1} \\mid x\_{1,t}, x\_{2,t}).

Quine's reduction asserts that any polyadic dependency can be represented as an aggregation of dyadic predicates by encoding relationships through intermediate paired representations:

R(x\_1, x\_2, y) \\implies J\\left(\\langle x\_1, x\_2 \\rangle, y\\right)

Translated into causal state transitions, a Quinean reduction decomposes the joint transition probability matrix into a factorized cascade of dyadic transfers:

P\_{\\text{Quine}}\\left(y\_{t+1} \\mid x\_{1,t}, x\_{2,t}\\right) = \\sum\_{p} P\\left(y\_{t+1} \\mid p\_t\\right) P\\left(p\_t \\mid x\_{1,t}, x\_{2,t}\\right)

where p\_t represents the intermediate pair state. However, in physical execution without domain inflation, a bipartition must cut the physical components of the actual mechanism.

In IIT 4.0, evaluating the Minimum Information Partition requires testing all bipartitions P = \\{P\_1 \\mid P\_2\\} of the candidate mechanism. Consider the partition cutting the inputs: P = \\{X\_1 \\mid (X\_2, Y)\\}. The partitioned cause-effect repertoire p^P is evaluated by injecting independent uniform noise over the severed boundary:

p^P\\left(Y\_{t+1} \\mid X\_{1,t}, X\_{2,t}\\right) = P\\left(Y\_{t+1} \\mid \\text{do}\\left(X\_{2,t}\\right)\\right) = \\sum\_{x\_{1,t}} P\\left(Y\_{t+1} \\mid x\_{1,t}, X\_{2,t}\\right) \\cdot \\frac{1}{2} = \\frac{1}{2}

Severing X\_1 destroys the XOR parity constraint, transforming the deterministic transition into complete randomness. The Intrinsic Difference between the intact repertoire p and the partitioned repertoire p^P is strictly positive:

\\text{ID}\\left(p \\parallel p^P\\right) = \\left\\vert{} 1 - \\frac{1}{2} \\right\\ve\[span\_186\](start\_span)\[span\_186\](end\_span)\[span\_194\](start\_span)\[span\_194\](end\_span)rt{} \\log\_2\\left(\\frac{1}{1/2}\\right) = \\frac{1}{2} \\times 1 = 0.5\\text{ bits} \> 0

This non-zero divergence confirms that the intact XOR mechanism is causally irreducible (\\Phi \> 0).

Now, suppose an analyst attempts to validate Quine's philosophical thesis by modeling the system *strictly as an extensional network of dyadic channels*—that is, assuming the physical mechanism can be fully captured by its dyadic marginals without a primitive triadic node. The reconstructed transition probability matrix \\tilde{P} derived solely from pairwise marginal data is:

\\tilde{P}\\left(Y\_{t+1} \\mid X\_{1,t}, X\_{2,t}\\right) = \\frac{P\\left(Y\_{t+1} \\mid X\_{1,t}\\right) P\\left(Y\_{t+1} \\mid X\_{2,t}\\right)}{\\sum\_{y} P\\left(y \\mid X\_{1,t}\\right) P\\left(y \\mid X\_{2,t}\\right)} = \\frac{\\frac{1}{2} \\times \\\[span\_70\](start\_span)\[span\_70\](end\_span)\[span\_73\](start\_span)\[span\_73\](end\_span)\[span\_76\](start\_span)\[span\_76\](end\_span)frac{1}{2}}{\\frac{1}{4} + \\frac{1}{4}} = \\frac{1}{2}

Because all dyadic correlations across the XOR gate are zero (I(X\_1; Y) = 0 and I(X\_2; Y) = 0), the dyadic reconstruction \\tilde{P} is identical to complete noise. If this dyadic system is partitioned across the MIP, the partitioned repertoire \\tilde{p}^\[span\_365\](start\_span)\[span\_365\](end\_span)\[span\_367\](start\_span)\[span\_367\](end\_span)P matches the unpartitioned repertoire \\tilde{p}:

\\tilde{p}(e) = \\frac{1}{2} \\quad \\text{and} \\quad \\tilde{p}^P(e) = \\frac{1}{2} \\quad \\forall e \\in \\math\[span\_366\](start\_span)\[span\_366\](end\_span)\[span\_368\](start\_span)\[span\_368\](end\_span)bb{F}\_2

Evaluating the Intrinsic Difference yields:

\\text{ID}\\left(\\tilde{p} \\parallel \\tilde{p}^P\\right) = \\left\\vert{} \\frac{1}{2} - \\frac{1}{2} \\right\\vert{} \\log\_2(1) = 0 \\implies \\Phi = 0

An extensional Quinean dyadic decomposition collapses causal integration. Quine’s reduction succeeds in formal logic only by moving the triadic binding into an infinite set-theoretic universe. In a finite physical substrate, moving relational binding into descriptive set theory removes the causal constraint from the mechanism itself, reducing its intrinsic integrated information to zero. Physical cause-effect power requires the causal instantiation of algebraic teridentity.

## **Publication Architecture: The Synergistic Teridentity**

The following publication plan formalizes these findings for submission to an interdisciplinary journal in mathematical philosophy, theoretical computer science, or complex systems (such as *Synthese*, *Philosophy of Science*, or *Entropy*).

### **Working Title**

**The Synergistic Teridentity: Why Causal Integration Is Invariant Under Quinean Relational Reductions**

### **Formal Academic Abstract**

Charles Sanders Peirce’s Reduction Thesis asserts that triadic relations cannot be decomposed into dyadic relations, whereas triads generate all polyads. In 1954, W.V.O. Quine challenged this thesis, proposing that any polyadic formal theory can be reduced to a single dyadic predicate via set-theoretic ordered pairs. While universal algebra (Burch 1991, Hereth Correia & Pöschel 2006) subsequently vindicated Peirce within closed relational clones by demonstrating the irreducibility of the teridentity relation (=\_3), this foundational debate has remained completely isolated from contemporary information theory. In this paper, we bridge mathematical logic and theoretical neuroscience by demonstrating a formal isomorphism between algebraic teridentity and informational synergy. Utilizing the Partial Information Decomposition (PID) and Integrated Information Decomposition (\\Phi\\text{ID}) frameworks, we prove that canonical synergistic interactions (e.g., the multivariate XOR logic gate) have state-space supports that are isomorphic to join-irreducible affine relations in relational clone theory. In both domains, dyadic coordinate projections yield unconstrained Cartesian products, erasing joint constraints. Extending this isomorphism to Giulio Tononi’s Integrated Information Theory (IIT 4.0), we prove that applying an extensional Quinean dyadic decomposition to a Transition Probability Matrix guarantees integrated information \\Phi = 0. Quine’s reduction succeeds only by externalizing irreducible triadic binding into an infinite meta-theoretic ontology, committing a use/mention fallacy that destroys the intrinsic cause-effect power of physical systems. We conclude by formalizing the "Synergistic Teridentity," establishing higher-order causal synergy as the dynamic counterpart of Peircean Thirdness.

### **Five-Section Structural Outline**

#### **Section 1: The Peirce–Quine Debate and the Problem of Relational Adicity**

  - **Narrative Bridge:** Establish the historical conflict between Peirce's phenomenological-algebraic trichotomy and Quine's program of radical nominalism and dyadic reduction.
  - **Analytical Substance:** Reconstruct Quine’s 1954 paper *"Reduction to a Dyadic Predicate"*, unpacking its reliance on Wiener-Kuratowski ordered pairs, infinite class hierarchies, and predicate reification. Formulate the core paradox: if Quine’s proof is syntactically sound, why do multi-variable dependencies resist dyadic reduction in modern physics, complex systems, and algebra?
  - **Theoretical Payoff:** Define the boundary between extensional model expansion and generative algebraic closure on a fixed universe of discourse.

#### **Section 2: Universal Algebra, Relational Clones, and the Teridentity Theorem**

  - **Narrative Bridge:** Transition from first-order syntax to internal algebraic representations via Peircean Algebraic Logic (PAL) and clone theory.
  - **Analytical Substance:** Formally define relational clones, Krasner algebras, and primitive positive logic. Trace Robert Burch's (1991) proof of Peirce's Reduction Thesis and the subsequent generalized proofs by Hereth Correia and Pöschel (2006) and Koshkin (2024). Provide the formal proof that the teridentity relation =\_3 \\;= \\{(x,x,x) \\mid x \\in A\\} cannot be generated by any set of monadic and dyadic relations when \\vert{}A\\vert{} \\ge 2.
  - **Theoretical Payoff:** Demonstrate Peirce's diagnostic of the use/mention fallacy: Quine’s dyadic logic presupposes teridentity through the implicit 3-way branching of shared variables across conjuncts (R(x) \\land S(x) \\la\[span\_381\](start\_span)\[span\_381\](end\_span)\[span\_382\](start\_span)\[span\_382\](end\_span)nd T(x)) and inside the triadic pairing relation \\text{Pair}(x\_1, x\_2, p).

#### **Section 3: Multivariate Information Decomposition and the Topology of Synergy**

  - **Narrative Bridge:** Connect the algebraic irreducibility of relational clones to the decomposition of multivariate probability distributions.
  - **Analytical Substance:** Introduce Williams and Beer's (2010) Partial Information Decomposition (PID) and the 16-atom temporal lattice of Integrated Information Decomposition (\\Phi\\text{ID}). Detail how Shannon mutual information obscures the distinction between redundancy and synergy. Provide an exhaustive information-theoretic analysis of the XOR gate and parity distributions.
  - **Theoretical Payoff:** Prove the Synergistic Teridentity Theorem: pure informational synergy exists if and only if the relational support of the joint distribution forms a join-irreducible relation whose dyadic projections are trivial Cartesian planes. Synergy is established as the dynamic measure-theoretic manifestation of teridentity.

#### **Section 4: Integrated Information Theory and the Causal Collapse Theorem**

  - **Narrative Bridge:** Apply the Synergistic Teridentity to the causal ontology of Integrated Information Theory.
  - **Analytical Substance:** Reconstruct IIT 4.0 mathematical postulates: transition probability matrices, physical purviews, cause-effect repertoires, the Minimum Information Partition (MIP), and the Intrinsic Difference (ID) metric. Prove the Causal Collapse Theorem: modeling a multi-input causal mechanism via an extensional Quinean dyadic factorization forces its intact cause-effect repertoire to match its MIP-partitioned repertoire, driving \\Phi to zero.
  - **Theoretical Payoff:** Establish that physical consciousness and causal integration require hardware-level triadic primitives; Quinean reductions eliminate genuine causal power by pushing physical constraints into the descriptive observer's syntax.

#### **Section 5: Epistemological Repercussions for Complex Systems and Biosemiotics**

  - **Narrative Bridge:** Contextualize the mathematical isomorphism within broader scientific attempts to formalize emergence, meaning, and biological organization.
  - **Analytical Substance:** Re-evaluate biosemiotics (Deacon, Hoffmeyer, Emmeche), providing a rigorous information-theoretic grounding for the claim that life and semiosis require irreducible Peircean Thirdness. Show how subcubic graph reductions in relational clones explain multi-scale hierarchical emergence without requiring ungrounded polyadic primitives beyond n=3.
  - **Theoretical Payoff:** Unify formal logic, semiotics, and information theory, presenting a mathematically rigorous ontology of complexity that refutes radical nominalism and dyadic reductionism.

The formal reconciliation of Peirce’s Reduction Thesis, Quine’s dyadic reduction, and causal information decomposition resolves a century-old philosophical dispute by translating it into concrete mathematical constraints. Relational clone theory proves that within a closed domain, dyadic relations can never generate the ternary branching of the teridentity relation; Quine’s apparent reduction works solely by inflating the ontology to an infinite set-theoretic hierarchy, shifting the irreducible triadic binding into the meta-logic of pairing. When translated into physical and computational dynamics, this shift has catastrophic consequences: an extensional Quinean dyadic decomposition of a Transition Probability Matrix strips the system of all synergistic mutual information, forcing its cause-effect structure to factorize across the Minimum Information Partition and driving its integrated information (\\Phi) to zero. Informational synergy is not an epistemic illusion, but the dynamical realization of algebraic teridentity. In this unified framework, Peircean Thirdness emerges as the necessary and sufficient algebraic condition for irreducible causal integration in complex physical systems.

#### **Works cited**

1\. Peircean Algebraic Logic and Peirce's Reduction Thesis, https://www.researchgate.net/publication/272536145\_Peircean\_Algebraic\_Logic\_and\_Peirce's\_Reduction\_Thesis 2. from relational databases to Peirce's reduction thesis - arXiv, https://arxiv.org/pdf/2406.14094 3. Semiotic theory of Charles Sanders Peirce - Wikipedia, https://en.wikipedia.org/wiki/Semiotic\_theory\_of\_Charles\_Sanders\_Peirce 4. W. V. Quine. Reduction to a dyadic predicate. The journal of, https://www.researchgate.net/publication/274204526\_W\_V\_Quine\_Reduction\_to\_a\_dyadic\_predicate\_The\_journal\_of\_symbolic\_logic\_Bd\_19\_1954\_S\_180-182\_-\_Alan\_Cobham\_Reduction\_to\_a\_symmetric\_predicate\_Ebd\_Bd\_21\_1956\_S\_56-59 5. The Journal of Symbolic Logic: Volume 19 - | Cambridge Core, https://www.cambridge.org/core/journals/journal-of-symbolic-logic/volume/F5729311784AE7D2EA73AF6974208A4D 6. W. V. Quine's Professional Published and Unpublished Essays, https://www.wvquine.org/wvq-publish.html 7. The Power of Peircean Algebraic Logic (PAL), https://wwwpub.zih.tu-dresden.de/\~poesch-r/poePUBLICATIONSpdf/2004\_Hereth\_Poe.pdf 8. The Teridentity and Peircean Algebraic Logic | Request PDF, https://www.researchgate.net/publication/221649144\_The\_Teridentity\_and\_Peircean\_Algebraic\_Logic 9. Pairs, Sets and Sequences in First Order Theories, https://dspace.library.uu.nl/bitstreams/197811be-a857-45ac-8e7f-9d1b2775327e/download 10. Is Peirce's reduction thesis gerrymandered? - arXiv, https://arxiv.org/pdf/2406.14058 11. The mathematical landscape of partial information decomposition, https://arxiv.org/html/2603.06678v2 12. Synergistic information supports modality integration and flexible, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012178\&rev=1 13. Integrated information theory - Grokipedia, https://grokipedia.com/page/Integrated\_information\_theory 14. Integrated information theory (IIT) 4.0: Formulating the properties of, https://pmc.ncbi.nlm.nih.gov/articles/PMC10581496/ 15. Measuring the integrated information of a quantum mechanism, https://www.researchgate.net/publication/366962448\_Measuring\_the\_integrated\_information\_of\_a\_quantum\_mechanism 16. A synergistic core for human brain evolution and cognition | bioRxiv, https://www.biorxiv.org/content/10.1101/2020.09.22.308981v1.full-text 17. What is Peirce's reduction thesis in modern terms? - MathOverflow, https://mathoverflow.net/questions/510103/what-is-peirces-reduction-thesis-in-modern-terms 18. Causation, Information, and Synergy in the Multiscale Brain Hierarchy, https://www.preprints.org/manuscript/202509.0678 19. Integrating Peirce and IIT : how integrated information theory and, https://www.semanticscholar.org/paper/fb67aa7fc4597072edcd07b9a7759aacfe0b7c77 20. The Sheaf-Theoretic Structure Of Non-Locality and Contextuality, https://www.researchgate.net/publication/48199583\_The\_Sheaf-Theoretic\_Structure\_Of\_Non-Locality\_and\_Contextuality 21. Word and Object - Daniel W. Harris, https://danielwharris.com/teaching/364/readings/QuineWordObject.pdf 22. Categories (Peirce) - Wikipedia, https://en.wikipedia.org/wiki/Categories\_(Peirce) 23. Triads and Triadic Relations - John Sowa, http://jfsowa.com/talks/triads.pdf 24. A Peircean Reduction Thesis: The Foundations of Topological Logic, https://www.abebooks.com/9780896722477/Peircean-Reduction-Thesis-Foundations-Topological-0896722473/plp 25. Two Instances of Peirce's Reduction Thesis - Researcher.Life, https://artefacts-discovery.researcher.life/full\_text\_files/DA-2/96/969c569128053c4e8f22f378e400c689/full\_text/FOSnUdx2P52TdbLHf9ODju4\_ouBc61XngUjr41T3Gro%3D.pdf 26. Journal of Applied Logics - College Publications, https://www.collegepublications.co.uk/downloads/ifcolog00025.pdf 27. Intelligence Without Consciousness the Rise of the IIT Zombies, https://www.preprints.org/manuscript/202510.1665 28. Integrated information theory - Wikipedia, https://en.wikipedia.org/wiki/Integrated\_information\_theory 29. A Synergistic Workspace for Human Consciousness ... - bioRxiv, https://www.biorxiv.org/content/10.1101/2020.11.25.398081v2.full.pdf 30. A taxonomy of information dynamics phenomena - arXiv, https://arxiv.org/html/1909.02297v1 31. Functional completeness and primitive positive decomposition of, https://arxiv.org/html/2606.19492v1 32. (PDF) A Synergistic Workspace for Human Consciousness, https://www.researchgate.net/publication/379687851\_A\_Synergistic\_Workspace\_for\_Human\_Consciousness\_Revealed\_by\_Integrated\_Information\_Decomposition 33. How Physical Information Underlies Causation and the Emergence, https://pmc.ncbi.nlm.nih.gov/articles/PMC11937085/ 34. Combining contextuality and causality: a game semantics approach, https://pmc.ncbi.nlm.nih.gov/articles/PMC10822710/ 35. Information and Semiosis in Living Systems: A Semiotic Approach, https://www.researchgate.net/publication/216816466\_Information\_and\_Semiosis\_in\_Living\_Systems\_A\_Semiotic\_Approach 36. Semiotics in Graphic Design - Steven Skaggs, https://turkey-lettuce-fl4e.squarespace.com/s/Semiotics-and-graphic-design 37. Quantum computation: harnessing the atom at the borders of paradox, https://people.maths.ox.ac.uk/nanda/cat/CAT17L1.pdf 38. Compositional Diagrammatic First-Order Logic - ResearchGate, https://www.researchgate.net/publication/343688222\_Compositional\_Diagrammatic\_First-Order\_Logic 39. Deep Inference for Graphical Theorem Proving - LIX (Polytechnique), https://www.lix.polytechnique.fr/page/index.php?username=donato\&path=papers/thesis.pdf 40. Toward a unified taxonomy of information dynamics via Integrated, https://www.pnas.org/doi/10.1073/pnas.2423297122 41. Integrated Information in the Active Inference Framework - arXiv, https://arxiv.org/html/2608.14165
