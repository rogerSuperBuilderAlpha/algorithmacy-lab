---
citekey: albantakis2023information
title: "Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms"
authors: "Albantakis, Larissa; Barbosa, Leonardo; Findlay, Graham; Grasso, Matteo; Haun, Andrew M.; Marshall, William; Mayner, William G. P.; Zaeemzadeh, Alireza; Boly, Melanie; Juel, Bjørn E.; Sasai, Shuntaro; Fujii, Keiko; David, Isaac; Hendren, Jeremiah; Lang, Jonathan P.; Tononi, Giulio"
year: 2023
venue: "PLOS Computational Biology 19(10): e1011465"
doi: "10.1371/journal.pcbi.1011465"
section: "S5"
status: candidate
verified: corrected
source_basis: "Publisher PDF (open access, 45 pp.), read in full via pdftotext; PMC10581496 confirmed as this DOI through the NCBI ID converter"
access_url: "https://doi.org/10.1371/journal.pcbi.1011465"
retrieved: 2026-09-24
sha256: "96129cb9589703e30663969cb0f0f329f706778b88b6b5f4b967a19f994783db"
---

## What the talk may use it for
Albantakis and fifteen co-authors (Tononi last) give the reference formalism of IIT 4.0. The talk needs three of its definitions exactly. First, intrinsic information is selectivity times informativeness, ii_e(s, s̄) = p_e(s̄|s) · log2[p_e(s̄|s) / p_e(s̄)] (Eq 5), which the authors say is formally the intrinsic difference (ID) of Barbosa et al. 2020 on the effect side. Second, system integrated information φ_s is the minimum of cause and effect irreducibility (Eq 21). Each side has the same product form with the partitioned probability in place of the unconstrained one and a positive-part operator (Eqs 19–20). The minimum partition (MIP) is the directional partition, into k ≥ 2 parts, that minimises φ_s *normalised* by its maximum possible value over all TPMs (Eq 23). Third, structure integrated information Φ ("big Phi") is the sum of the φ values of a complex's distinctions and relations (Eq 59). The authors state that Φ "is not computed based on a partition". A partitioned TPM does not factor as "P(s_P1 | do(s_P1)) × P(s_P2 | do(s_P2))". Cut connections are causally marginalised, meaning replaced by uniform noise, unit by unit (Eqs 17–18).

## Loci
Page numbers are the journal's (x / 45). Quotations were matched against the pdftotext layer of the publisher PDF.
- p. 3 — "The existence of experience is IIT’s zeroth axiom." — the zeroth axiom; the five axioms follow (intrinsicality, information, integration, exclusion, composition).
- p. 2 — "in physical terms, to be is to have cause–effect power." — existence as cause–effect power.
- p. 5 — "Irreducibility is measured by integrated information (φ) over the substrate’s minimum partition." — the integration postulate.
- p. 15 — "Intrinsic information is formulated as a product of selectivity and informativeness based on the notion of intrinsic difference (ID) [14]." — ID is the basis of ii; [14] is Barbosa et al. 2020 (barbosa2020measure).
- p. 16 — "Note that, on the effect side, iie is formally equivalent to the ID between the constrained effect repertoire" — on the cause side ii_c is "not strictly equivalent" to an ID.
- p. 16 — "either the part’s inputs, outputs, or both are replaced by independent “noise”" — system partitions are directional; Eq 14 allows k ≥ 2 parts.
- p. 17 — "This means that all connections to unit Sj that are affected by the partition are causally marginalized (replaced by independent noise)." — the partitioned TPM (Eqs 17–18).
- p. 18 — "Accordingly, the system is reducible if at least one partition θ 2 ΘS makes no difference to the cause or effect probability." — φ_s = 0 condition ("2" is the text layer's rendering of ∈).
- p. 18 — "overlapping substrates with lower φs are thus excluded from existence." — exclusion: the complex is the maximum of φ_s among overlapping candidates.
- p. 23 — "a disintegrating partition θ 2 Θ(M, Z) either “cuts” the mechanism into at least two independent parts if |M| > 1, or it severs all connections between M and Z" — mechanism-level partitions (Eq 38), distinct from system partitions.
- p. 29 — "Note that Φ is not computed based on a partition (as system phi), but rather a sum of the integrated information within the structure" — Φ versus φ_s.
- p. 30 — "its Φ-structure corresponds to the quality of the experience of S in state s, while its Φ value corresponds to its quantity" — the explanatory identity.
- p. 37 — "a purely feed-forward system necessarily has φs = 0." — the feed-forward claim, stated for system φ_s.
- p. 39 — "it is not possible in practice to exhaustively apply the postulates to unfold the cause–effect power of realistic systems" — IIT 4.0 itself concedes intractability.

## What the preliminary sources claim about it
- iit-phi-definition (TR-S5-003): Φ is the irreducible constraint of a TPM not recoverable from any factorized dyadic bipartition across the MIP → corrected: IIT 4.0 separates φ_s, computed over the MIP of directional partitions into k ≥ 2 parts, from Φ, a sum over the Φ-structure that uses no partition. "Dyadic bipartition" is Gemini's phrase, not the paper's.
- iit-discrete-system-setup (TR-S5-014, -015) → verified: discrete updates, a finite state space, units conditionally independent given the prior state (Eq 2), and the TPM T_U (Eq 1).
- iit-partition-test (TR-S5-016, -017) → corrected: partitions test irreducibility, but system partitions are directional and may have more than two parts (Eq 14). "Bipartition" is IIT 3.0 usage.
- iit-partitioned-tpm-formula (TR-S5-018) → refuted as rendered: the partitioned probability of each unit averages uniformly over the states of the units whose inputs the partition cuts (Eq 18). No factor of the form P(s_P | do(s_P)) appears.
- iit-mechanism-phi-definition (TR-S5-019) → corrected: φ_e(m, Z, θ) = π_e(z′|m) · |log(π_e(z′|m) / π^θ_e(z′|m))|₊ at the maximal state z′ (Eq 41), not a divergence D between whole distributions. The MIP is the normalised argmin (Eq 43), and φ_d = min(φ_c, φ_e) after maximising over purviews (Eqs 46–47).
- iit4-intrinsic-difference (TR-S5-020) → corrected: ii rests on the ID (p. 15). The effect-side ii_e is formally the ID between the constrained and unconstrained repertoires, and ii_c is not strictly an ID (p. 16).
- iit4-intrinsic-difference-formula (TR-S5-021) → refuted: ID(p, q) = max_α p_α log(p_α/q_α) (barbosa2020measure, Eq 1). IIT 4.0's φ keeps that product form. No |p − p^P| factor appears anywhere in the paper.
- iit-mip-definition (TR-S5-022, -494) → corrected: the MIP minimises φ_s(θ) divided by its maximum over all TPMs (Eq 23), not raw ID. The paper's gloss is "the partition that makes the least difference" (p. 10), and it bears on the system's maximal cause–effect state, not on the Φ-structure.
- iit-phi-positive-irreducible (TR-S5-023) → verified as a gloss, with φ_s in place of "Φ(MIP)".
- iit-partition-cuts-components (TR-S5-095) → unverifiable: too vague to check. Partitions cut causal connections between parts, directionally (p. 16).
- iit4-mechanism-partitions (TR-S5-096) → corrected: mechanisms are tested over disintegrating partitions of mechanism × purview into k ∈ {2, 3, 4, …} parts (Eq 38), not over bipartitions of the mechanism alone.
- xor-cut-repertoire (TR-S5-097, -098) → corrected: the arithmetic holds under Eqs 28 and 39, but the paper prints no XOR repertoire; the 1/2 is the carder's calculation. Marginalising the cut input uniformly leaves π^θ(y|x1) = 1/2 for an XOR output. This is mechanism-level (φ_d), not system Φ.
- xor-mechanism-id-value and xor-repertoire-arithmetic (TR-S5-099, -617–619, -624–626) → refuted: with p = 1 and p^θ = 1/2, Eq 41 gives φ_e = 1 · log2(2) = 1 ibit, not 0.5. The 0.5 comes from Gemini's |p − q| factor. TR-S5-617 is right only on the effect side, since the cause repertoire of Y has two preimages. The "dyadic reconstruction" rows (-624–626) give 0 under either formula, but the reconstruction is a max-ent statistical model, not an IIT substrate. The 1-ibit figure is my arithmetic on Eq 41, not a value the paper reports; a full φ_d also needs the cause side.
- iit4-postulates (TR-S5-122) → refuted: the postulates are existence (the zeroth) plus intrinsicality, information, integration, exclusion and composition (pp. 4–5). TPMs, purviews, repertoires, the MIP and ID are formal machinery.
- iit4-axioms-postulates (TR-S5-271, -283, -432, -492) → corrected: TR-S5-283 leaves out exclusion and composition. The others are right. The authors "formulate" the axioms as postulates by "inference to a good explanation" (p. 2); they do not deduce them.
- iit4-zeroth-axiom-existence (TR-S5-433, -491) → verified (p. 3).
- iit4-axioms-to-postulates (TR-S5-435) and iit4-phi-structure-from-tpm (TR-S5-436) → verified (abstract; p. 38).
- iit4-explanatory-identity (TR-S5-437) → corrected: quality is the Φ-structure and quantity is Φ (p. 30). "Φ^Max" is IIT 3.0's symbol.
- iit-computational-intractability (TR-S5-438) → corrected: IIT 4.0 itself says exhaustive application is impossible in practice and full analysis is limited to "idealized systems of a few units" (p. 39). The register note calling this a critics' claim is wrong. The authors add that approximations make IIT "eminently testable".
- iit4-existence-cause-effect-power (TR-S5-415, -434, -459, -487) → corrected: -434 and -487 are verified. "Evaluated over a MIP" (-415, -459) mixes existence with integration.
- iit4-tpm-operational (TR-S5-260) → corrected: "a substrate U … is operationally defined by its potential interactions, assessed in terms of conditional probabilities" (p. 8). Purviews belong to mechanisms, not to the system TPM.
- iit4-phi-s-intrinsic-difference (TR-S5-261, -489) → corrected: φ_s measures how much the partition reduces the intrinsic information of the maximal cause–effect state, taking the minimum of the cause and effect sides (p. 10; Eqs 19–22). Its product form comes from the ID. The paper writes φ*_s only for the maximum over candidate systems.
- iit4-phi-s-definition (TR-S5-490) → corrected along the same lines.
- iit-mip-search (TR-S5-493) → verified for φ_s and φ_d (Eqs 23, 43). Φ itself needs no partition search.
- phi-zero-iff-lossless-partition (TR-S5-495) → corrected: φ_s = 0 if some partition "makes no difference" (p. 18), and also whenever the system is not strongly connected. "Feed-forward" adds nothing.
- phi-zero-aggregate (TR-S5-496) → corrected: a reducible system is not a complex and "condenses" into smaller complexes, as with the third system of Fig 8, which "splits into three smaller complexes". "Aggregate of independent variables" is not the paper's term.
- iit4-unitary-irreducible-whole (TR-S5-488), iit-irreducible-whole-definition (TR-S5-328), iit4-apparatus (TR-S5-485) → verified as glosses.
- feedforward-phi-zero (TR-S5-265, -270, -280, -282, -445) → corrected: IIT 4.0 claims φ_s = 0 for any purely feed-forward system (p. 37), so the universal claim is IIT's own. The paper says such machines "would experience nothing (or nearly nothing)" (p. 39), because feed-forward systems can still condense into small complexes (Fig 8). TR-S5-445 cites IIT 3.0; see oizumi2014phenomenology.
- iit-functional-equivalence (TR-S5-281) → refuted as a theorem name: the section is "Consciousness and functional equivalence: Being is not doing" (Fig 8). The cited result that any discrete recurrent function has a feed-forward implementation is Krohn & Rhodes [54], not an IIT theorem.
- iit4-exclusion-postulate (TR-S5-273, -279, -299) → corrected: -273 and -299 are close. The complex is the maximum of φ_s among overlapping candidates (Eq 26). -279 is refuted: exclusion removes overlapping substrates from existence as complexes. It does not set their φ_s to zero.
- iit4-exclusion-grain (TR-S5-284) → verified (p. 19): the grain is the one that maximises φ*_s.
- iit-isolated-feedback-system (TR-S5-285) → corrected: the paper says the Φ-structure "depends on the causal interactions between system subsets, not on the system’s interaction with its environment" (p. 36), and that a system in a fixed point "may be phenomenally quite “alive,”" (p. 38). The row's "keeps generating" wording is not the paper's.
- iit4-current-state-ces (TR-S5-288) → verified (pp. 5–6, 36).
- iit4-complex-ports (TR-S5-278) → refuted for IIT 4.0, which defines no complex by ports. "Ports-in" and "ports-out" are IIT 3.0's names for interface elements (oizumi2014phenomenology, p. 16).
- iit4-current-standard (TR-S5-407) → corrected: IIT 4.0 "incorporates" the ID introduced by Barbosa et al. 2020 [12, 14] (p. 3).
- iit-spatial-partitions (TR-S5-643) → corrected: IIT partitions divide units and cut their causal connections directionally. They are not spatial.
- modern-proofs-triadic-irreducibility (TR-S5-558) → refuted: IIT 4.0 proves nothing about Peirce's reduction thesis. It never mentions Peirce, relations of adicity three, or teridentity.
- iit4-albantakis-2023 and albantakis-2023-iit4-citation (TR-S5-053, -136, -231, -259, -406, -412, -486) → corrected: the bibliographic data are right: PLOS Comput Biol 19(10): e1011465, and PMC10581496 resolves to this DOI. "Albantakis et al. & Tononi" is malformed. The title ends "in physical terms", not "in physical systems" (TR-S5-412).
- dyadic-decomposition-phi-zero (TR-S5-305) → refuted: no "Causal Collapse Theorem" appears in this paper. A web search for the phrase in the IIT literature on 2026-09-24 found nothing.
- dyadic-decomposition-strips-synergy (TR-S5-312) → refuted: IIT 4.0 never mentions PID synergy (grep: 0 hits for "synerg"), and no source found makes the claim.
- wholeness-definition (TR-S5-603) → corrected: φ_s > 0 over the MIP is IIT 4.0's criterion for a system's irreducibility. "Dynamical return" is not sufficient. Choosing the MIP by Eq 23 "ensures that φs … = 0 if the system is not strongly connected in graph-theoretic terms" (p. 18), and the paper nowhere says that strong connectivity guarantees φ_s > 0.

## Notes
- NOT FOR SLIDES: carder's own arithmetic. The XOR values on this card (partitioned repertoire π^θ = 1/2; φ_e = 1 · log2 2 = 1 ibit under Eq 41) are computed by the carder from the paper's equations. The paper prints neither number. A slide may state the formula (Eq 41) and the refutation of the |p − q| factor, but not "IIT 4.0 gives 1 ibit for XOR".
- The lab's Φ numbers use PyPhi's GID repertoire distance, not this paper's ID. A slide that quotes an ID-based formula must not present lab numbers as its output.
- The text layer renders ∈ as "2" and drops subscripts ("φs" = φ_s). The loci above keep those renderings so they match character for character.
- Supplementary S1–S3 (ties, comparison with IIT 1.0–3.0, relation theorems) were not read.
