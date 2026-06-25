---
citekey: albantakis2023iit40
title: Integrated Information Theory (IIT) 4.0: Formulating the Properties of Phenomenal Existence in Physical Terms
authors: Albantakis, Larissa and Barbosa, Leonardo and Findlay, Graham and Grasso, Matteo and Haun, Andrew M. and Marshall, William and Mayner, William G. P. and Zaeemzadeh, Alireza and Boly, Melanie and Juel, Bj{\o}rn E. and Sasai, Shuntaro and Fujii, Keiko and David, Isaac and Hendren, Jeremiah and Lang, Jonathan P. and Tononi, Giulio
year: 2023
doi: 10.1371/journal.pcbi.1011465
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1011465&type=printable
sha256: 96129cb9589703e30663969cb0f0f329f706778b88b6b5f4b967a19f994783db
pdf_path: literature/pdfs/albantakis2023iit40.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
This paper presents Integrated Information Theory (IIT) 4.0, a theory of consciousness that aims to account for the properties of experience in physical (operational) terms. Its method is to identify five essential, immediate and irrefutable properties of experience ("axioms": intrinsicality, information, integration, exclusion, composition, preceded by the "zeroth" axiom of existence), and to infer the necessary and sufficient properties their physical substrate must satisfy ("postulates"), then express those postulates in a mathematical framework applied to systems modeled by a transition probability matrix (TPM). The central explanatory move is an identity: an experience is identical to the cause-effect structure (Φ-structure) "unfolded" from a maximal substrate (a complex) in its current state. The paper provides explicit mathematical formulations, including a measure of intrinsic information (ii) built on the notion of intrinsic difference (ID), system integrated information (φ_s, "small phi"), and structure integrated information (Φ, "big Phi"), and demonstrates internal consistency by applying the formalism to small idealized binary networks (Figs 1, 2, 6, 7, 8). Worked examples illustrate three implications: connectivity/specialization determines whether a substrate supports high Φ; changing a single unit's state can reshape the entire Φ-structure; and functionally equivalent systems can differ in their Φ-structures, so that "being is not doing" (e.g., a feed-forward system has φ_s = 0 and cannot be conscious). IIT 4.0 incorporates a more accurate axioms-to-postulates formulation, the intrinsic-difference-based information measure, and explicit assessment of causal relations relative to IIT 1.0, 2.0, and 3.0.

## Key facts it relies on
- IIT lists five axioms of phenomenal existence — intrinsicality, information (specificity), integration (unitary/irreducible), exclusion (definiteness), and composition (structure) — preceded by a "zeroth" axiom: the existence of experience, which the paper calls immediate and irrefutable.
- Physical existence is operationalized as cause-effect power ("to be is to have cause-effect power," the principle of being / Eleatic principle), and a substrate is defined operationally by its transition probability matrix (TPM) T_U ≡ p(ū | u), assuming discrete updates, finite state space, and conditional independence of units given the preceding state.
- Intrinsic information ii(s,s̄) is defined as the product of informativeness (a logarithmic term, base 2, "ibits") and selectivity; on the effect side ii_e(s,s̄) = p_e(s̄|s) log(p_e(s̄|s)/p_e(s̄)) (Eq 5), and it is built on the notion of intrinsic difference (ID) which uniquely satisfies three properties: causality, intrinsicality, and specificity.
- System integrated information φ_s is the irreducibility of a system's maximal cause-effect state over its minimum partition (MIP), evaluated using directional system partitions; the maximal substrate (complex) is the candidate system that maximizes φ_s (φ_s*) over all overlapping candidates (Eqs 19–26).
- The MIP is the partition minimizing relative integrated information φ_s(θ)/max φ_s(θ), where the maximal normalization value for a partition θ equals Σ|S^(i)||X^(i)|, the maximal number of pairwise interactions ("connections") affected by θ.
- A complex is "unfolded" into a Φ-structure of causal distinctions d(m)=(m, z*, φ_d) (mechanisms specifying maximally irreducible cause-effect states over purviews) and causal relations r(d)=(d, f(d), φ_r) (congruent overlaps among distinctions); Φ = Σφ (sum of distinction and relation φ values, Eq 59) is the structure integrated information corresponding to the quantity of consciousness.
- Examples use binary units with state space {−1, 1} and a logistic activation p(U_i,t=1|u_{t−1}) = 1/(1+exp(−k Σ w_{j,i} u_{j,t−1})) (Eq 60) with k controlling determinism; all worked examples use k = 4.
- A purely feed-forward (recurrent-free) system necessarily has φ_s = 0 and cannot constitute a complex or support consciousness; in Fig 8 three functionally equivalent "8-counter" systems yield different structure integrated information (Φ = 21.01, 3.64, and a reducible third system that splits into three small complexes).
- For an optimally connected specialized system the number of distinctions is bounded above by 2^n − 1 and the number of relations by 2^(2^n−1) − 1; for the n=6 specialized lattice in Fig 6D the Φ value reported is 11451.98 ibits.
- All examples were computed using the "iit-4.0" feature branch of PyPhi; the paper states there is no primary data and code is available at the cited GitHub repository.

## Critical notes from the literature
- The authors explicitly state that an exhaustive calculation of the relevant quantities for realistic systems is infeasible: characterizing a universal TPM and condensing it into complexes/Φ-structures involves "multiple, nested combinatorial explosions," so a full analysis can only be done on idealized systems of a few units; tight, bounded approximations of φ_s and Φ are flagged as ongoing research.
- The paper acknowledges open methodological choices that "remain open to further evaluation," including the proper treatment of background conditions and the resolution of ties given symmetries in TPMs (S1 Text), and notes IIT "must still be considered work in progress."
- The authors raise foundational vulnerabilities themselves in the conclusions: the assumption of a discrete, finite set of "atomic" units of cause-effect power may be incompatible with current physics; whether the axiomatic basis and the formulation of axioms as postulates is sound and unique is questioned; and they ask whether IIT can survive empirical tests relating consciousness and its brain substrate.
- IIT 4.0 makes strong, controversial functionalism-rejecting claims — that digital computers / feed-forward hardware implementing AGI "would experience nothing (or nearly nothing)" and that "being is not doing" — which the paper presents as a consequence of the postulates rather than an independently demonstrated empirical result.
- Competing interests are disclosed: author G. Tononi holds an executive position and has a financial interest in Intrinsic Powers, Inc., a company developing a clinical device to assess presence/absence of consciousness.

## Key topics covered
Integrated Information Theory (IIT 4.0); axioms and postulates of consciousness; intrinsicality, information, integration, exclusion, composition; existence as cause-effect power; transition probability matrix (TPM); intrinsic information (ii) and intrinsic difference (ID); informativeness and selectivity; expansion vs dilution; system integrated information (φ_s / "small phi"); minimum information partition (MIP); maximal substrate / complex; causal distinctions and purviews; causal relations and faces; cause-effect structure / Φ-structure; structure integrated information (Φ / "big Phi"); principle of being, maximal existence, minimal existence; causal marginalization and background conditions; macro vs micro units (grain); feed-forward vs recurrent systems; functional equivalence vs phenomenal equivalence ("being is not doing"); PyPhi; neural substrate of consciousness (cortex vs cerebellum, directed cycles, specialized lattices).
