---
citekey: bonchi2024diagrammatic
title: "Diagrammatic Algebra of First Order Logic"
authors: "Bonchi, Filippo; Di Giorgio, Alessandro; Haydon, Nathan; Sobociński, Paweł"
year: 2024
venue: "Proceedings of the 39th Annual ACM/IEEE Symposium on Logic in Computer Science (LICS 2024, Tallinn) | ACM | article pp. 1–15"
doi: "10.1145/3661814.3662078"
section: "S4"
status: candidate
verified: verified
source_basis: "arXiv:2401.07055v1 PDF (34 pp. with appendices, posted 13 Jan 2024), read in full via pdftotext -layout and plain pdftotext for the two-column text; title, authors, venue, 2024-07-08 date and pages 1–15 confirmed in Crossref. The ACM typeset version was not read. Page numbers below are arXiv PDF pages."
access_url: "https://arxiv.org/abs/2401.07055"
retrieved: 2026-09-24
sha256: "b82af44f4c765044637d30f3d15eea46aaec73b1f7e0afd48a00feb6afdcc871"
---

## What the talk may use it for
The paper is the current high-water mark of the string-diagram programme for first-order logic. It gives a quantifier-free "calculus of neo-Peircean relations" (NPR_Σ) with the expressivity of FOL and a complete axiomatisation. The axioms combine cartesian bicategories (the existential–conjunctive fragment) with their photographic negative, cocartesian bicategories (the universal–disjunctive fragment). Linear bicategories glue the two, which yields "first order bicategories". Negation is derived rather than primitive, which is the paper's stated advance on haydon2020compositional.

**Role of the branching node.** The copier — the diagonal X → X × X read as a relation — and the discharger are two "novel fundamental constants" of the calculus. The copier with its opposite (the cocopier) forms a special Frobenius algebra, and it carries the sharing of variables across sub-terms. As a subset of X × X², the copier is {(x, (x, x))}, which is Peirce's teridentity. That gloss is ours: the body of the paper never uses the word. As in PAL, the three-way node is a generator of the syntax, not something the paper derives.

**Reduction thesis.** The paper does not mention the reduction thesis. Its Appendix A, "A tribute to Charles S. Peirce", credits Peirce with seeing that the "teri- or tri-identity relation", made by adding a branch to identity, is the key to moving from binary to arbitrary relations. That is Peirce's positive, constructive point. The negative clause, that the branch cannot be built from dyads, goes unmentioned. The appendix sends readers to haydon2020compositional for "Peirce's topological intuitions behind the Frobenius equations".

## Loci
arXiv v1 PDF pages.
- p. 1 (abstract) — "a string diagrammatic extension of the calculus of binary relations that has the same expressivity as first order logic and comes with a complete axiomatisation."
- p. 2 — "Monoids and comonoids together satisfy special Frobenius equations ((S◦),(F◦))." (on the cartesian-bicategory fragment; symbols from the text layer)
- p. 2 — "The (co)monoid structures allow one to express existential quantification".
- p. 2 — the copier "makes clear that the variable x3 is shared by two sub-terms".
- p. 4 — "identify two novel fundamental constants: the copier ◀◦X ⊆ X × X² which is the diagonal function ⟨idX, idX⟩ : X → X × X (considered as a relation)" (symbols transcribed from the text layer).
- p. 5 (Definition 4.1, item 4) — the white copier/discharger and cocopier/codischarger "form special Frobenius algebras".
- p. 12 (§10) — the cartesian-bicategory treatment of Beta in haydon2020compositional "inhibits a fully compositional treatment since, for instance, negation is not functorial."
- p. 14 (Appendix A) — "He went on to emphasize the teri- or tri-identity relation, arising from adding a 'branch' to the identity relation, as the key to moving from binary to arbitrary relations."
- p. 14 (Appendix A) — "We like to think that if Peirce had known category theory then he would have presented NPRΣ."

## What the preliminary sources claim about it
- lines-of-identity-frobenius (TR-S4-033, -061) → corrected; see haydon2020compositional. The register's "see also" bibliography for this paper is right: LICS 2024, doi:10.1145/3661814.3662078. Here the Frobenius structure belongs to the copier (the branch node) and its opposite (pp. 2, 5). It is not a claim about lines of identity in general.

## Notes
- Appendix A quotes Peirce's praise for EGs "treating triadic and higher relations as easily as dyadic relations" from *Logic of the Future* vol. 3/1, p. 173 (ref. [67], dated 2022). De Gruyter published vol. 3/1 in April 2024 (see pietarinen2019future), so the page may come from a pre-publication draft. Check it before quoting Peirce through this paper.
- Other diagrammatic treatments of Beta cited in §10 were not carded: Brady & Trimble (doctrines, ref. [14]) and Melliès & Zeilberger (chiralities, ref. [52]).
- The companion paper on conjunctive queries that D1's evidence names (Bonchi, Seeber & Sobociński, CSL 2018) was not read.
