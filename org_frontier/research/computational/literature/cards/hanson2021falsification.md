---
citekey: hanson2021falsification
title: Formalizing falsification for theories of consciousness across computational hierarchies
authors: Hanson, Jake R. and Walker, Sara I.
year: 2021
doi: 10.1093/nc/niab014
arxiv: null
journal: Neuroscience of Consciousness
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2006.07390
sha256: 403515932bec193f16508ccf5879614a03ba206e741ab4d63c8549e456d97285
pdf_path: literature/pdfs/hanson2021falsification.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks at what level of computational abstraction a theory of consciousness can be scientifically tested, and uses this to make the abstract "unfolding argument" against Integrated Information Theory (IIT) concrete. The authors introduce a computational hierarchy of formal descriptions of a finite-state machine: the finite-state automaton (FSA, abstract input-output behavior), the combinatorial-state automaton (CSA, the FSA plus a specific binary encoding), and the full causal structure (the specific logic gates implementing the CSA). As a concrete, tabletop-realizable example, they construct two isomorphic digital circuits that operate a simple electronic tollbooth (lift a boom barrier after eight quarters): one "conscious" circuit with feedback (Φ > 0 for all states) and one functionally identical "unconscious" feed-forward circuit (Φ = 0 for all states), built from JK flip-flops, with Φ computed using the PyPhi package. They argue that the presence or absence of feedback, and hence the value of Φ, is a consequence of an arbitrary choice of binary labels used to encode the same functional states. They conclude that IIT is simultaneously falsified at the FSA level (an instance of the unfolding argument) and unfalsifiable at the CSA level. From this they extract a general criterion: to avoid being unfalsifiable or already falsified, a measure of consciousness must be invariant with respect to changes that leave the inference procedure (fixed at a given level of the hierarchy) unaffected. They suggest Group Complexity as a candidate measure that satisfies this invariance.

## Key facts it relies on
- Falsification is defined (after Popper) as a mismatch between a theoretical prediction and an observation; because conscious states cannot be observed directly, falsification for theories of consciousness must be a mismatch between prediction and inference, where inference rests on some other empirical observation.
- The paper defines a three-level computational hierarchy: the finite-state automaton (FSA) describing abstract input/output/internal-state relationships; the combinatorial-state automaton (CSA), which adds a specific binary labeling/encoding of subsystems; and the full causal structure, the specific logic gates (e.g., AND/OR/NOT vs universal NAND) implementing the CSA-level Boolean functions.
- IIT makes its predictions at the CSA level: feedback (bidirectional dependencies) between elements is a necessary (but not sufficient) condition for Φ > 0, motivated by the integration axiom; IIT is invariant with respect to changes below the CSA level (different gate implementations of the same CSA have the same Φ).
- The concrete example is an electronic tollbooth that lifts a boom barrier upon receipt of exactly eight quarters ($2.00), requiring the machine to cycle through eight internal memory states {A, B, ..., H}, described as a mod-8 FSA.
- The "conscious" circuit uses the random binary labeling A=000, B=110, C=010, D=101, E=111, F=011, G=001, H=100; built from JK flip-flops it contains meaningful feedback and, computed with the Python package PyPhi, yields Φ > 0 for all states (reported values 0.9775, 1.4687, 0.9775, 1.7187, 1.7187, 1.4688, 1.4688, 1.4688).
- The "unconscious" circuit uses a different (hierarchical, Krohn-Rhodes-derived) labeling A=000, B=100, C=010, D=110, E=001, F=101, G=011, H=111; this yields a strictly feed-forward causal architecture with Φ = 0 for all states.
- A JK flip-flop has two stable states (0,1), two input channels J and K, and a clock; JK input 00 latches, 01 resets to 0, 10 sets to 1, 11 toggles; for any desired state transition there are two JK input pairs that realize it (degeneracy used in circuit design).
- The feed-forward (Φ = 0) construction relies on the Krohn-Rhodes theorem and an isomorphic cascade decomposition via a "nested sequence of preserved partitions" (P1, P2, P3), where a partition is preserved if every microstate within a block transitions to a state in a single block; this guarantees unidirectional information flow and Φ = 0.
- The authors propose Group Complexity as a candidate measure of consciousness that, unlike Φ, is invariant below the FSA level because it counts the number of resets needed to complete a Krohn-Rhodes decomposition, putting all CSA representations on equal footing and remaining both non-trivial and falsifiable.

## Critical notes from the literature
- The paper builds directly on and concretizes prior abstract falsification arguments: the unfolding argument of Doerig et al. (2019), its generalization by Kleiner and Hoel (2020), and the authors' own isomorphic feed-forward philosophical zombies (Hanson and Walker, Entropy 2019).
- The authors acknowledge the conclusion is conditional: IIT being unfalsifiable at the CSA level "or" already falsified at the FSA level depends on which inference procedure one adopts; whether the result "falsifies the theory or renders it metaphysical" depends on whether one accepts the canonical inference procedure.
- The authors concede that Group Complexity, like Φ, "seems much too simple to truly quantify conscious experience": it coarse-grains sensorimotor richness into a scalar and offers no implicit explanation for "what it is like" to be something (citing Nagel).
- The paper notes a broader limitation for the field: inference of conscious states relies on first-hand phenomenal grounding (e.g., sleep, verbal report), which is hard to extend to cases like artificial intelligence where such grounding is lost; new frameworks (e.g., theories of the causal consequences of subjective experience) may be needed in addition to measures that quantify it.

## Key topics covered
Integrated Information Theory (IIT); Φ (phi); falsification and Popperian demarcation; unfolding argument; prediction vs inference; computational hierarchy (FSA / CSA / causal structure); finite-state automata; combinatorial-state automata; Chalmers' computational foundation; causal structure theories; feedback and the integration axiom; JK flip-flops and digital circuit design; Karnaugh maps; isomorphic circuits; Krohn-Rhodes decomposition / cascade decomposition; preserved partitions; PyPhi; philosophical zombies; Group Complexity; neural correlates of consciousness (NCCs).
