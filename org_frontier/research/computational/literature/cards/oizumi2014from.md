---
citekey: oizumi2014from
title: From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0
authors: Oizumi, Masafumi and Albantakis, Larissa and Tononi, Giulio
year: 2014
doi: 10.1371/journal.pcbi.1003588
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003588&type=printable
sha256: 589dcc7d2cc3c8e4f72a76a43d0daaa5fce53ab52770b8e599c826b766b963c6
pdf_path: literature/pdfs/oizumi2014from.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This paper presents Integrated Information Theory (IIT) 3.0, a revised mathematical formulation that derives the mechanisms of consciousness from the phenomenology of experience. The authors start from five self-evident phenomenological axioms about experience (existence, composition, information, integration, exclusion) and translate each into a corresponding ontological postulate that prescribes how physical mechanisms (neurons, logic gates) must be configured to generate experience. They build the formalism bottom-up, first at the level of individual mechanisms (defining cause-effect repertoires, cause-effect information, integrated information phi, and concepts) and then at the level of systems of mechanisms (conceptual structures, integrated conceptual information Phi, and complexes). The central identity proposed is that an experience is identical to a maximally irreducible conceptual structure (MICS, or "quale"), whose constellation of concepts specifies the quality of the experience and whose value Phi^Max specifies its quantity. Using small example systems of OR, AND, and XOR logic gates, they illustrate the step-by-step calculation and derive several consequences, including that simple systems can be minimally conscious, complicated systems can be unconscious, feed-forward systems can be functionally equivalent "zombies," and concepts are intrinsic and self-referential rather than about the external environment.

## Key facts it relies on
- IIT is built on five phenomenological axioms taken as self-evident truths about consciousness: existence, composition, information, integration, and exclusion; each is translated into a corresponding physical/ontological postulate.
- The paper distinguishes three formulations: IIT 1.0 (original, dealt only with stationary systems), IIT 2.0 (state-dependent, integrated information computed top-down), and the present IIT 3.0, which defines composition, information, integration, and exclusion precisely and makes them operational.
- A mechanism's cause information (ci) and effect information (ei) are quantified as the distance D between the constrained cause/effect repertoire and the unconstrained repertoire; cause-effect information cei = min(ci, ei), motivated by an "intrinsic information bottleneck principle."
- The distance measure D in IIT 3.0 is the earth mover's distance (EMD, Wasserstein distance), used both for repertoires (phi) and for constellations of concepts (Phi) in concept/qualia space.
- Worked example values for mechanism A=1 in the candidate set ABC: ci(ABC^p|A^c=1) = 0.33, ei(ABC^f|A^c=1) = 0.25, so cei = min = 0.25; the unconstrained future repertoire of A (an OR gate) gives p(A=0)=0.25 and p(A=1)=0.75.
- Integrated information phi ("small phi") is the distance D between the cause-effect repertoire of the whole mechanism and that of the partitioned mechanism across the minimum information partition (MIP); for mechanism ABC in state 100, phi^MIP_cause = 0.5, phi^MIP_effect = 0.25, so phi = min = 0.25.
- A concept is a mechanism specifying a maximally irreducible cause-effect repertoire (MICE / "quale sensu stricto"); for mechanism BC, the core cause BC^c/AB^p has phi_cause^Max = 0.33, and the concept's phi^Max(A^c) = min(0.17, ...) = 0.17 (example values from Figs 8-9).
- A conceptual structure (constellation of concepts C) is the set of all concepts a candidate set specifies; conceptual information CI is the distance D from C to the "null" concept p^uc, computed as 2.11 in the worked ABC example.
- At the system level, a set of elements is integrated only if every subset specifies both selective causes and selective effects in its complement; integrated conceptual information Phi ("big phi") is the distance between the whole constellation and the MIP-partitioned constellation. A complex is a set generating a local maximum of Phi^Max.
- In the candidate set ABC, concept space has dimension 16 (8 axes for past states, 8 for future states); of the power set of ABC's mechanisms, only AC gives phi^Max = 0 (no concept), while all others specify non-zero concepts (Figure 10).

## Critical notes from the literature
- The authors emphasize IIT inverts the usual neuroscience approach: it takes phenomenology as primary and asks how it can be physically implemented, rather than starting from neural mechanisms and asking when they give rise to consciousness; they argue the standard "neural correlates of consciousness" approach cannot by itself explain how consciousness comes about.
- The exclusion postulate enforces a "causal Occam's razor" (causes should not be multiplied beyond necessity), allowing only one maximally irreducible cause and one effect per mechanism, excluding all overlapping/superposed causes; this is a strong theoretical commitment of the framework.
- All demonstrations use small idealized systems of discrete deterministic logic gates (OR, AND, XOR) or linear threshold units; the framework is presented on toy networks of a few elements (e.g., ABCDEF), and the choice of EMD as the distance measure is acknowledged as a choice that is discussed/defended in the Supplementary Material (Text S2) rather than uniquely forced.
- The paper notes that an empirical prediction of IIT (loss/recovery of consciousness tied to breakdown of information integration) has been confirmed via transcranial magnetic stimulation with high-density EEG, but the core 3.0 formalism itself is theoretical and the article is presented independently of empirical validation.

## Key topics covered
Integrated Information Theory (IIT 3.0); phenomenological axioms (existence, composition, information, integration, exclusion); ontological postulates; cause-effect repertoire; cause-effect information (cei, ci, ei); integrated information (phi, "small phi"); minimum information partition (MIP); concept and MICE (maximally irreducible cause-effect repertoire); conceptual structure / constellation of concepts; conceptual information (CI); integrated conceptual information (Phi, "big phi"); maximally irreducible conceptual structure (MICS / quale); complexes and minor complexes; earth mover's distance / Wasserstein distance; concept space / qualia space; transition probability matrix (TPM); logic-gate networks (OR/AND/XOR); intrinsic information bottleneck; feed-forward "zombie" systems; mind-body identity.
