---
citekey: tononi2004information
title: An Information Integration Theory of Consciousness
authors: Tononi, Giulio
year: 2004
doi: 10.1186/1471-2202-5-42
arxiv: null
journal: BMC Neuroscience
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://bmcneurosci.biomedcentral.com/counter/pdf/10.1186/1471-2202-5-42
sha256: 27a598c5c538d7c1e9a1e4e60ae081483313db298736e84645dc561cf5e83ef7
pdf_path: literature/pdfs/tononi2004information.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Tononi proposes the information integration theory of consciousness (IIT), arguing that consciousness corresponds to a system's capacity to integrate information. The theory is motivated by two phenomenological properties of subjective experience: differentiation (each conscious state is one of an enormous repertoire of possible states) and integration (each experience is a unified whole that cannot be subdivided into independent components). It introduces a quantitative measure, Φ, defined as the amount of effective information that can be exchanged across the "minimum information bipartition" (the informational weakest link) of a subset of elements; a "complex" is a subset with Φ>0 that is not included within a larger subset of higher Φ, and the complex of highest Φ is the "main complex." The theory claims that the quantity of consciousness equals the Φ of a complex, while the quality of consciousness is determined by the informational relationships among the complex's elements, captured by an "effective information matrix" that defines an abstract "qualia space." Tononi uses simplified linear (Gaussian) computer models to show that high Φ requires the joint presence of functional specialization and functional integration, mirroring thalamocortical organization, and that strongly modular architectures (like the cerebellum) yield only small low-Φ complexes. The theory is shown to account in a principled way for neurobiological observations, including why consciousness depends on the thalamocortical system but not the cerebellum, why it is lost in dreamless sleep and seizures, and why conscious experience has characteristic time requirements. Implications drawn include that consciousness is graded, present in infants and animals, a fundamental and disposition-like quantity, and in principle constructable in artifacts.

## Key facts it relies on
- Information is measured by the entropy function H = -Σp_i·log_2·p_i; the paper states a fair coin gives 1 bit and throwing a fair die yields log_2(6) ≈ 2.59 bits.
- An idealized one-megapixel binary camera could differentiate among 2^1,000,000 states (≈1,000,000 bits), yet because its photodiodes do not causally interact it integrates no information and is better described as 1,000,000 independent two-state repertoires.
- Effective information for a bipartition into parts A and B is defined as EI(A→B) = MI(A^Hmax;B), injecting maximum entropy (independent noise) into A's outputs; for a bipartition EI(A⇄B) = EI(A→B) + EI(B→A), and Φ(S) is the (non-normalized) EI across the minimum information bipartition (MIB), the bipartition where normalized EI reaches a minimum.
- A complex is defined as a subset S with Φ>0 that is not included within a larger subset having higher Φ; the complex with maximum Φ is the "main complex," and complexes are the "subjects" of experience.
- Models were implemented as stationary multivariate Gaussian processes; connection matrices were normalized so total afferent synaptic weight per element equals w<1 (w = 0.5 used), with perturbation coefficient c_p = 1 and intrinsic noise coefficient c_i = 0.00001.
- A connection matrix optimized for Φ starting from random weights yielded Φ = 74 bits and showed two features of high-Φ networks: connection patterns differ across elements (functional specialization) and all elements are reachable from all others (functional integration).
- Replacing heterogeneous with homogeneous connectivity, or forming small modules, lowered Φ to 20 bits; a strongly modular network of three modules of eight elements each gave Φ = 20 bits per module, illustrating why the cerebellum (with independently activated patches) contributes little to consciousness.
- Two four-element systems (a "divergent" and a "chain" architecture) can each form a single complex with the same Φ = 10 bits yet have different effective information matrices, showing Φ (quantity) and qualia-space structure (quality) are distinct.
- Time-course simulations indicate effective interactions among distant cortical areas require at least ~80 milliseconds to produce specific correlated firing; the paper cites microgenesis estimates of 100–200 ms for a fully formed sensory experience, single conscious moments not extending beyond 2–3 seconds, and low-intensity cortical stimuli needing up to 500 ms to produce a conscious sensation.
- Split-brain-like and disconnection simulations: a 16-element two-"hemisphere" main complex had Φ = 72 bits; cutting "callosal" connections produced two 8-element complexes of Φ = 61 bits each; afferent/efferent pathways and subcortical loops form larger complexes of only Φ = 10 bits, leaving the high-Φ main complex as the locus of consciousness.

## Critical notes from the literature
- The theory is explicitly presented as a hypothesis/framework aimed at the necessary and sufficient conditions for the quantity and quality of consciousness; the paper concedes that "a full understanding of how the brain generates human consciousness remains a formidable task" and that proper testing "requires a much better understanding of cortical neuroanatomy than is presently available."
- Φ is illustrated only with extremely simplified, idealized linear (Gaussian) model systems of a few elements; the author notes (Appendix x) that statements about, e.g., basal ganglia loops "need to be qualified due to the difficulty of evaluating the precise effects of their selective inactivation," and measuring Φ accurately in real systems "will not be easy," with approximations and informed guesses being conceivable.
- It is acknowledged as unclear whether highly selective single-element states can be achieved within a large high-Φ neural complex such as the one postulated to underlie human consciousness.
- The theory makes counterintuitive ontological claims the author flags as such: consciousness is a fundamental, graded quantity (like mass or charge), exists as a disposition/potentiality even when no elements are activated, and could in principle be built into artifacts by endowing them with high Φ.
- Several supporting simulations are cited as unpublished/in-preparation work (Hill and Tononi), so some quantitative claims about thalamocortical sleep-mode bistability rest on results not contained in this paper.

## Key topics covered
Information integration theory (IIT); Φ (phi) as a measure of integrated information; effective information; minimum information bipartition (MIB) and complexes; main complex / dynamic core; differentiation and integration of experience; qualia space and the effective information matrix; quantity vs. quality of consciousness; thalamocortical system; functional specialization and functional integration; cerebellum and modular architectures; reticular activating system, afferents, efferents, and cortico-subcortico-cortical loops; split-brain and functional disconnection; sleep, dreaming, and slow-wave bistability; time requirements of consciousness (microgenesis); Gaussian network modeling; consciousness as a graded, fundamental, disposition-like property; conscious artifacts.
