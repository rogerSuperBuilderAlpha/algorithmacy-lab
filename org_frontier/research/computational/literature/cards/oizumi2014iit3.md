---
citekey: oizumi2014iit3
title: From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0
authors: Oizumi, Masafumi and Albantakis, Larissa and Tononi, Giulio
year: 2014
doi: 10.1371/journal.pcbi.1003588
arxiv: null
journal: PLoS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003588&type=printable
sha256: 589dcc7d2cc3c8e4f72a76a43d0daaa5fce53ab52770b8e599c826b766b963c6
pdf_path: literature/pdfs/oizumi2014iit3.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
This paper presents Integrated Information Theory (IIT) 3.0, a mathematical framework that attempts to derive the physical substrate of consciousness from the phenomenology of experience rather than from neural mechanisms. The authors start from five phenomenological axioms held to be self-evident truths about consciousness (existence, composition, information, integration, exclusion), translate these into ontological postulates that prescribe how physical mechanisms (e.g., neurons or logic gates) must be configured to generate experience, and then arrive at an identity between experience and an informational/causal structure. Information is defined "intrinsically" as differences that make a difference within the system, measured over a mechanism's cause-effect repertoire; integration is measured by integrated information (small phi, irreducibility relative to the minimum information partition), and exclusion selects maximally irreducible structures. At the level of a system, the maximally irreducible conceptual structure (MICS, also called a quale) specifies the quality of an experience and the value of integrated conceptual information (big Phi, denoted Phi^Max) specifies its quantity. The framework is illustrated throughout on small systems of discrete logic gates (e.g., the candidate set ABC with OR, AND, XOR gates). Several consequences are derived: systems can condense into a major complex plus non-overlapping minor complexes; simple systems (a "minimally conscious photodiode") can be conscious; complicated feed-forward "zombie" systems are unconscious despite being functionally equivalent to conscious complexes; and inactive systems can still be conscious. The authors emphasize the approach is the opposite of the usual neuroscience strategy of starting from mechanisms and asking when they give rise to consciousness.

## Key facts it relies on
- IIT 3.0 rests on five phenomenological axioms taken as self-evident: existence, composition, information, integration, and exclusion; these are translated into corresponding postulates about physical mechanisms (mechanisms must have causal power, be irreducible, etc.).
- The framework defines a hierarchy of constructs first at the level of individual mechanisms (cause-effect information cei, integrated information small phi, concept/MICE = maximally irreducible cause-effect repertoire) and then at the level of systems of mechanisms (conceptual information CI, integrated conceptual information big Phi, complex/MICS).
- Distance between probability distributions is measured with the earth mover's distance (EMD), used as the metric of concept space for both small phi (between repertoires) and big Phi (between constellations of concepts).
- For the example mechanism A=1 over purview ABC in the candidate set ABC: cause information ci = D(p(ABC^p|A^c=1) || p^uc(ABC^p)) = 0.33, effect information ei = 0.25, and cause-effect information cei = min(ci, ei) = 0.25; the minimum is chosen because each mechanism acts as an information bottleneck from the intrinsic perspective.
- Integrated information small phi is evaluated across the minimum information partition (MIP), the partition that makes the least difference; for mechanism ABC in state 100, phi_cause^MIP = 0.5 and phi_effect^MIP = 0.25, giving small phi^MIP = min = 0.25.
- For the candidate set ABC the conceptual information CI = D(C || p^uc) = 2.11, and the integrated conceptual information of ABC's constellation under its MIP is big Phi^MIP = 1.92; ABC forms the complex (a local maximum of Phi), while subsets/supersets including D, E, or F have Phi = 0.
- A "minimally conscious photodiode" consisting of detector element D and predictor element P (DP=11) forms a complex with two concepts and a Phi^Max value of 1; a photodiode, blue detector, and thermistor with the same internal mechanisms generate the same minimal MICS.
- A strictly feed-forward "zombie" network has Phi^Max = 0 and no concepts because its input layer has no causes within the system and its output layer has no effects; such a system can be functionally equivalent (same input-output behavior over at least 4 time steps) to an integrated system that has Phi^Max = 0.79 and 17 concepts (Figure 21).
- Worked network examples contrast architectures: a modular network of COPY and AND gates decomposes into small complexes; a homogeneous all-to-all OR network forms a complex with low Phi^Max = 0.003 and 5 identical concepts; a specialized majority-gate network has high Phi^Max = 10.75 with 30 core concepts.
- An example system embedded in a larger network condenses into a major complex ABC (Phi^Max = 1.92) plus non-overlapping minor complexes DE and FG (each Phi^Max = 0.028), with overlapping ABCDE excluded (Phi = 0.021) by the exclusion postulate.

## Critical notes from the literature
- The authors explicitly state IIT 3.0 is "incomplete" and list unfinished business, including not discussing the relationship between MICS and specific phenomenology (modalities, submodalities, the "feel" of experience), and not having treated the assumed optimal "micro" spatio-temporal grain.
- They acknowledge the framework is, in its present form, defined only for small systems fully characterized by a transition probability matrix with discrete mechanisms in time and space; directly applying it to brains is "unfeasible" because it would require discretizing/extending to continuous variables and exhaustive perturbation of all system states.
- Computing Phi^Max exhaustively requires evaluating all possible partitions of every mechanism and of every system of mechanisms, leading to a combinatorial explosion; the authors state the exhaustive analysis is "unfeasible for systems of more than a dozen elements or so."
- The authors frame their approach as the opposite of standard neuroscience (starting from phenomenology rather than from neural mechanisms / neural correlates), and argue input-output behavior and reportability are not always reliable guides to consciousness (admitting "true zombies" that behave like us while lacking experience); this is a contested theoretical stance the paper itself advances rather than empirically demonstrates.
- The treatment of how meaning of concepts relates to the environment is acknowledged as "matching" rather than information processing and is deferred to future work; the relationship between integrated information and causation is stated to be treated "as one and the same thing," with many implications left to be explored.

## Key topics covered
Integrated Information Theory (IIT 3.0); phenomenological axioms (existence, composition, information, integration, exclusion); ontological postulates; cause-effect repertoire; cause-effect information (cei); intrinsic vs Shannon information; integrated information (small phi); minimum information partition (MIP); maximally irreducible cause-effect repertoire (MICE) / concept; conceptual information (CI); integrated conceptual information (big Phi, Phi^Max); maximally irreducible conceptual structure (MICS) / quale; complex; concept space / qualia space; earth mover's distance (EMD); major and minor complexes (condensation); paraconscious minor complexes; minimally conscious photodiode; feed-forward "zombie" systems; inactive-but-conscious systems; modular/homogeneous/specialized network comparison; self-generated, self-referential, holistic concepts; ports-in/ports-out; logic-gate model systems (OR, AND, XOR, COPY, majority, parity gates).
