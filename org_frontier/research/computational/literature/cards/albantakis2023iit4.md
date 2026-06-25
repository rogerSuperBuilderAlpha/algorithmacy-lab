---
citekey: albantakis2023iit4
title: Integrated information theory ({IIT}) 4.0: Formulating the properties of phenomenal existence in physical terms
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
pdf_path: literature/pdfs/albantakis2023iit4.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This paper presents Integrated Information Theory (IIT) 4.0, a theory of consciousness that aims to account for the properties of experience in physical (operational) terms. It starts from five axioms of phenomenal existence — intrinsicality, information, integration, exclusion, and composition (plus a "zeroth" axiom that experience exists) — and translates each into a corresponding postulate of physical existence that a substrate must satisfy to be conscious. "Physical" is meant operationally: to exist is to have cause-effect power, quantified from a substrate's transition probability matrix (TPM). The paper provides an updated mathematical formalism that uses an Intrinsic Difference (ID)-based measure of intrinsic information to determine a substrate's maximal cause-effect state, system integrated information (φ_s) to identify maximal substrates (complexes), and the unfolding of distinctions and relations into a Φ-structure whose structure integrated information (Φ) corresponds to the quantity of consciousness. IIT proposes an explanatory identity: an experience is identical to the cause-effect structure (Φ-structure) unfolded from a maximal substrate in its current state. The formalism is applied to small simulated binary networks to illustrate three implications: how connectivity, activity, and functional (in)equivalence affect Φ-structures — notably that purely feed-forward systems have φ_s = 0 and that functionally equivalent systems can differ in their cause-effect structures ("being is not doing").

## Key facts it relies on
- IIT identifies exactly five axioms of phenomenal existence — intrinsicality, information (specificity), integration (unitary), exclusion (definite), and composition (structured) — preceded by a zeroth axiom that experience exists; the paper claims these are complete and necessary and sufficient.
- "Physical" is defined operationally via the principle of being (Box 2): "to be is to have cause-effect power" — the power to take and make a difference, judged by a conscious observer/manipulator; the paper relates this to Plato's Eleatic principle and to the Buddhist philosopher Dharmakīrti.
- A substrate U is a stochastic system of n interacting units, assumed to update in discrete steps with finite state space, with units conditionally independent given the preceding state (Eq 2), fully described by a transition probability matrix (TPM) of size |Ω_U| under the do-operator (intervention).
- Intrinsic information (ii) is quantified in units of "intrinsic bits" or "ibits" and is the product of informativeness (deviation from chance, the log term in base 2) and selectivity (concentration of cause-effect power on a specific state); it is built on the notion of intrinsic difference (ID), which uniquely satisfies three properties — causality, intrinsicality, and specificity.
- System integrated information φ_s is evaluated over the minimum partition (MIP), defined as the directional partition that minimizes integrated information relative to its maximum possible value; the maximal possible φ_s for a partition equals Σ|S^(i)||X^(i)|, the number of pairwise connections cut.
- Exclusion is enforced by selecting the candidate substrate with maximum system integrated information (φ_s*), called a maximal substrate or complex; a recursive search "condenses" a universe into a disjoint, exhaustive set of complexes.
- A causal distinction d(m) = (m, z*, φ_d) links a mechanism M⊆S to a maximal cause-effect purview (Eq 27); a relation r(d) = (d, f(d), φ_r) binds distinctions whose purviews overlap congruently; the cause-effect structure is C(D) = D ∪ R(D), and Φ ("big Phi") is the sum of all φ values of distinctions and relations (Eq 59).
- Examples use binary units with a logistic (sigmoidal) activation function (Eq 60) with slope parameter k (k = 4.0 in figures) and normalized incoming weights summing to 1 (Eq 61); a directed 6-unit copy cycle forms a complex with φ_s = 1.74 ibits but low Φ = 7.65 because its Φ-structure is only first-order distinctions.
- Worked Φ values include: a 6-unit specialized lattice with 27 of 63 distinctions giving Φ = 11451.98 ibits (Fig 6D); a 5-unit network in state ABcdE with φ_s = 1.1, 23 of 31 distinctions, 13740 relations, and Φ = 22.26, dropping to Φ = 18.55 when E is inactive (OFF) and Φ = 3.35 (14 distinctions) when E is inactivated (Fig 7).
- The number of relations for n units is upper-bounded by 2^(2^n − 1) − 1, and the number of distinctions for an optimally connected specialized system is bounded by 2^n − 1; ΣΦ_r can be computed analytically (S3 Text).

## Critical notes from the literature
- The authors state IIT "must still be considered work in progress" and that IIT 4.0 is the first formulation striving to characterize Φ-structures completely using measures that satisfy the postulates uniquely, implying earlier versions (IIT 1.0/2.0/3.0) did not.
- The paper acknowledges exhaustive application is infeasible for realistic systems: fully characterizing a universal TPM and condensing it into complexes involves "multiple, nested combinatorial explosions" repeated across grains and maximizations, so full analysis "can only be performed on idealized systems of a few units."
- Some algorithmic choices remain open, including the proper treatment of background conditions and the resolution of ties given symmetries in TPMs (S1 Text); the authors note further validation depends on systematic back-and-forth among phenomenology, theory, and neuroscientific evidence.
- The authors explicitly flag possible failure modes: assumptions of a discrete, finite set of "atomic" units of cause-effect power may be incompatible with current physics, and they pose whether the axioms-as-postulates basis is sound/unique and whether IIT can survive empirical tests relating Φ to consciousness in the brain.
- The "being is not doing" claim — that feed-forward/digital architectures could be behaviorally indistinguishable from conscious humans yet experience nothing (φ_s = 0) — is presented as a strong and contestable implication, resting on the explanatory identity rather than independent empirical proof.

## Key topics covered
Integrated Information Theory (IIT 4.0); axioms and postulates of consciousness; intrinsicality, information, integration, exclusion, composition; cause-effect power; transition probability matrix (TPM); intrinsic information (ii) and intrinsic difference (ID); ibits; system integrated information (φ_s, small phi); minimum information partition (MIP); maximal substrate / complex; causal distinctions and relations; purviews and mechanisms; Φ-structure and structure integrated information (Φ, big Phi); explanatory identity; principle of being / maximal existence / minimal existence; macro units and grains; feed-forward vs recurrent architectures; functional vs phenomenal equivalence; PyPhi ("iit-4.0" branch); neural substrate of consciousness predictions.
