---
citekey: abramsky2011structure
title: "The sheaf-theoretic structure of non-locality and contextuality"
authors: "Abramsky, Samson; Brandenburger, Adam"
year: 2011
venue: "New Journal of Physics 13(11): 113036 (open access)"
doi: "10.1088/1367-2630/13/11/113036"
section: "S5 (peripheral)"
status: candidate
verified: corrected
source_basis: "arXiv:1102.0264v7 PDF (33 pp., 29 Nov 2011, 'Submitted to: New J. Phys.'; arXiv journal-ref 'New Journal of Physics 13 (2011) 113036'), abstract, §1, §§2–4 definitions, §6 and §8 read via pdftotext -layout, the rest searched by keyword. The IOP version of record was not reachable (the publisher PDF URL returned an HTML page). Title, volume, issue, article number, date (28 Nov 2011) and authors from Crossref"
access_url: "https://arxiv.org/abs/1102.0264v7"
retrieved: 2026-09-24
sha256: "a06560481dd4dfdd91f0d031221be1aa1152e3cd5d15300e1a08c9f8df7f1f48"
---

## What the talk may use it for
Peripheral to S5. Abramsky and Brandenburger recast non-locality and contextuality in sheaf theory. Measurements form a cover of compatible contexts, an empirical model is a compatible family of distributions over that cover, and a model is non-contextual exactly when those local distributions glue into one global section, i.e. one distribution on all measurements whose marginals are the observed ones. Their Theorem 8.1 makes this an equivalence with realisation by a "factorizable hidden-variable model". The talk may borrow the picture of a whole whose local views agree pairwise yet admit no global assignment, cited to this paper, and only as an analogy: the paper says nothing about Peirce, relational clones, PAL, PID or IIT.

## Loci
Page numbers of the arXiv v7 PDF; the NJP pagination was not seen. Quotations matched against the pdftotext layer.
- p. 1 (abstract) — "We use the mathematical language of sheaf theory to give a unified treatment of non-locality and contextuality" — the programme.
- p. 1 (abstract) — "We show that contextuality, and non-locality as a special case, correspond exactly to obstructions to the existence of global sections." — the main characterisation.
- p. 2 — "We introduce a general mathematical setting, completely independent of Hilbert space" — the setting is not restricted to quantum mechanics.
- p. 7 — "We shall define a no-signalling empirical model for M to be a compatible family for the cover M with respect to the presheaf" DR E — the definition of an empirical model.
- p. 9 — "Thus the existence of a global section for the empirical model corresponds exactly to the existence of a distribution defined on all measurements, which marginalizes to yield the empirically observed probabilities." — what a global section means.
- p. 12 — "Proposition 4.2 The Bell model has no global section." — Bell's theorem in this language; Hardy (Prop. 4.3, p. 13) and GHZ (Prop. 6.1, p. 19) follow.
- p. 19 — "Proposition 6.2 (Lal) The only strongly contextual no-signalling models of type (2, 2, 2) are the PR boxes." — the PR box is the paper's two-party example of maximal contextuality.
- pp. 23–24 (Theorem 8.1) — "(i) e has a realization by a factorizable hidden-variable model." / "(ii) e has a global section." — stated as equivalent.
- p. 25 — "This result provides a definitive justification for equating the phenomena of non-locality and contextuality with obstructions to the existence of global sections."
- p. 29 — "The C̆ech cohomology of this presheaf with respect to the measurement cover is used to define a cohomological obstruction to locality or non-contextuality" — reported from ref. [53], Abramsky, Barbosa & Mansfield, not proved here.

## What the preliminary sources claim about it
- abramsky-brandenburger-2011-bib (TR-S4-026, -052, -136) → corrected: Abramsky, S. & Brandenburger, A. (2011), "The sheaf-theoretic structure of non-locality and contextuality", New J. Phys. 13(11): 113036. TR-S4-052's title is right; TR-S4-136's "The Sheaf-Theoretic Structure of Contextuality" drops "non-locality and".
- abramsky-sheaf-program (TR-S4-173) → verified: a sheaf-theoretic treatment (p. 1) in which the event sheaf is a functor P(X)^op → Set (p. 5), so "category-theoretic" is fair. The setting is "completely independent of Hilbert space" (p. 2).
- contextuality-obstruction-global-section (TR-S4-031, -138, -175, -179, -183) → corrected: contextuality and non-locality "correspond exactly to obstructions to the existence of global sections" (p. 1; Theorem 8.1). "Topological obstruction" (TR-S4-138, -175) is not this paper's phrase; the cohomological version belongs to Abramsky, Barbosa & Mansfield (p. 29, ref. [53]). TR-S4-183's "in quantum systems" overstates it: specific models (Bell, Hardy, GHZ) lack global sections, not every quantum model.
- contextuality-definition-presheaf (TR-S4-174, -178) → corrected: -178 is right in substance, with a correction. The empirical model is a compatible family of *distributions* over the measurement cover (p. 7), not of observations. -174's "assigning global values to observables" is the deterministic reading; the paper's definition is at the level of distributions, and value-assignment failure is its *strong* contextuality (§6).
- bell-ks-nonfactorizable (TR-S4-181, -182) → corrected: Theorem 8.1 equates a global section with a "factorizable hidden-variable model" (pp. 23–24), and factorizability "corresponds to Bell locality" in Bell-type scenarios (p. 9). -182's "marginals of a global joint distribution" matches p. 9. "Independent local classical channels" (-181) is not the paper's phrase.
- abramsky-xor-bell-games (TR-S4-032, -185) → corrected: the paper treats Bell, Hardy and GHZ models, PR boxes and Kochen–Specker configurations. The strings "XOR" and "game" do not occur in it (grep: 0 hits). The game framing and an XOR step appear only later, in abramsky2024contextuality (pp. 1, 4), where XOR is classical processing in an MBQC example, not an XOR game. -185's "almost exclusively physical" is half right: the examples are physical, but the setting is "completely independent of Hilbert space" (p. 2), and maximal contextuality is recast as unsolvability of a constraint satisfaction problem (Prop. 6.4, p. 20).
- contextuality-cech-cohomology (TR-S4-180) → corrected: the Čech-cohomology treatment is Abramsky, Mansfield & Barbosa (2012), which this paper reports as ref. [53] (p. 29). It defines a cohomology class whose non-vanishing witnesses contextuality; this paper does not claim the converse. The 2012 paper was not read.
- sheaf-literature-not-linked-to-clones (TR-S4-034, -186) → corrected: this paper mentions no clones, PAL, PID, ΦID or IIT. It does link maximal contextuality to constraint satisfaction (Prop. 6.4), the setting in which co-clones live, so "not connected to relational structures" would be wrong. The wider sheaf literature was not searched.
- contextuality-mirrors-relational-irreducibility (TR-S4-139, -184) → unverifiable: no such claim appears here. The paper's "factorizable" concerns hidden-variable models (p. 23), not decomposition of a relation into dyadic relations, and it never mentions hypergraphs. Present any bridge as the talk's analogy.

## Notes
- Peripheral to S5: use only for an analogy between contextuality (locally consistent, globally unassignable) and irreducibility. Neither this paper nor abramsky2024contextuality mentions Peirce, teridentity, relational clones, PID or IIT (grep of both full texts: 0 hits for clone, Peirce, teridentity, synerg, integrated information, hypergraph).
- Page numbers are arXiv v7 pages. Cite the NJP article; check the NJP pagination before quoting a page on a slide.
