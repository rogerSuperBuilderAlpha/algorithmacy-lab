---
citekey: haydon2020compositional
title: "Compositional Diagrammatic First-Order Logic"
authors: "Haydon, Nathan; Sobociński, Paweł"
year: 2020
venue: "Pietarinen, A.-V.; Chapman, P.; Bosveld-de Smet, L.; Giardino, V.; Corter, J.; Linker, S. (eds.), Diagrammatic Representation and Inference: 11th International Conference, Diagrams 2020, Tallinn | Springer | Lecture Notes in Computer Science (vol. 12169 per the brief, unconfirmed), 402–418"
doi: "10.1007/978-3-030-54249-8_32"
section: "S4"
status: candidate
verified: corrected
source_basis: "Author's version PDF (16 pp., LaTeX, created 15 May 2020, title footnoted 'Compositional Diagrammatic First-Order Logic?'), formerly at ioc.ee/~pawel/papers/peirce.pdf (now 404) and retrieved from the Wayback Machine capture of 29 Jul 2024, whose content digest matches every capture from Apr 2021 to Feb 2026; read in full via pdftotext -layout. Title, authors, pages 402–418 and DOI confirmed in Crossref (book-chapter, Diagrammatic Representation and Inference, LNCS). The Springer typeset text was not read, so page numbers below are the author's version's."
access_url: "https://web.archive.org/web/20240729020552/https://www.ioc.ee/~pawel/papers/peirce.pdf"
retrieved: 2026-09-24
sha256: "4ade52aa0c95f4385fb29a8d73ef35a8047e517ddff524b2c9b3c5710f5913c8"
---

## What the talk may use it for
This is the paper behind the register's claim that lines of identity are Frobenius algebras, and it is the most Peirce-facing of the modern category-theoretic treatments. Haydon and Sobociński present the syntax of Peirce's Beta existential graphs as string diagrams, the arrows of a free symmetric monoidal category. Lines of identity become the generators of a monoid–comonoid pair: the copy node, the merge node and their units. These satisfy the laws of a special commutative Frobenius bimonoid, and the negation-free inference rules are the axioms of Carboni–Walters cartesian bicategories of relations. Models are structure-preserving functors into Rel_X, which send the generators to its "canonical Frobenius structure": the diagonal {(x, xx)} and its opposite.

**Role of the branching node.** The three-wire copy/merge node *is* Peirce's teridentity, and the paper says so. Adding a branch to a line of identity is the unit law. Two teridentities joined by two wires give a plain line of identity, which is the special law. Two joined by one wire give the Frobenius equations, which is Peirce's own remark that a four-way point is composed of two teridentities. The node is a primitive generator of the syntax. The paper derives it from nothing and never asks whether it could be.

**Reduction thesis.** The paper names teridentity and quotes Peirce on it (p. 8), but it does not state or discuss the reduction thesis. It cites Burch's *A Peircean Reduction Thesis* (ref. 4) only as an account of EGs and of free and bound variables (p. 2). The talk can say that modern categorical logic formalizes Peirce's teridentity as the Frobenius copy node without engaging his claim that the node is irreducible.

## Loci
Author's-version page numbers.
- p. 1 (abstract) — "we show the implied algebraic structure of EGs sans negation is that of cartesian bicategories of relations: for example, lines of identity obey the laws of special Frobenius algebras."
- p. 1 — "Throughout, we argue that Peirce's seminal studies led him to intuitions that suggest that he — at least implicitly — identified the very same algebraic structures."
- p. 2 — "Treatment of free and bound variables in modified versions of EG (see [4], [10]) equip EGs with additional structure." [4] is Burch 1991 and [10] Hereth Correia & Pöschel 2004. These, with "Further accounts can be found in [4], [9], [18]", are the paper's only uses of the PAL literature.
- p. 3 — "We represent lines of identity with the generators … of a monoid-comonoid pair." (the generator glyphs are images, lost in the text layer)
- p. 8 — "(unl) and (counl) are equivalent to being able to add a branch to any line of identity. Peirce called this triadic identity element, where a branch forms a point with three extending wires, the teridentity relation."
- p. 8 — Peirce to Lady Welby, as quoted: "every line of identity ought to be considered as bristling with microscopic points of teridentity" (cited to MS L463 via Commens; not checked against Peirce here).
- p. 8 — "Two teridentity relations brought together by connecting two of each of the three wires is equivalent to a single (dyadic) line of identity. This yields the (sp) equation."
- p. 9 — "Clearly, Peirce had the topological intuitions conveyed by the Frobenius structure." Footnote 5 quotes Peirce: "There is no need of a point from which four lines of identity proceed; for two triple points answer the same purpose" (cited as [16, p. 357], a draft of *Logic of the Future* vol. 2/3; not checked).
- p. 10 — in Rel_X the copy generator "is the diagonal relation {(x, xx) | x ∈ X}", and the four generator relations are "the canonical Frobenius structure of RelX" (symbols transcribed from the text layer).
- p. 15 (Conclusion) — "Seen through contemporary string diagrams, Peirce's lines of identity obey the rules of special Frobenius algebras, while Peirce's inference rules for lines of identity are the axioms of cartesian bicategories of relations."

## What the preliminary sources claim about it
- lines-of-identity-frobenius (TR-S4-033) → corrected. The Frobenius half is right and this paper is its source: lines of identity, drawn as string diagrams, obey the laws of special Frobenius algebras (pp. 1, 8, 15), and the copy node is the teridentity (p. 8). Three points need correcting. (1) The claim that they "form hypergraph categories" is not in this paper. It is Fong & Spivak's framing (fong2018graphical, Prop. 3.15), where Rel of a regular category is a hypergraph category whose Frobenius maps are the diagonal x ⊆ x × x × x. (2) "Shown" needs care. The Frobenius laws are axioms the authors impose on the generators that draw lines of identity. What the paper argues is that Peirce's EG rules match those axioms, and it cites as "well-known" that Rel_X satisfies them (p. 10). (3) Neither this paper nor bonchi2024diagrammatic nor fong2018graphical engages Peirce's reduction thesis. All three take the three-way node as a primitive.
- lines-of-identity-frobenius (TR-S4-061) → verified. D1's works-cited item 38 is this paper: Haydon & Sobociński 2020, LNCS 12169, 402–418, doi:10.1007/978-3-030-54249-8_32. Cite the DOI, not D1's ResearchGate link.

## Notes
- The LNCS volume number 12169 comes from the brief. Crossref and OpenAlex give the series, editors, ISBNs (print 978-3-030-54248-1, electronic 978-3-030-54249-8) and pages but no volume number, so check 12169 against the Springer front matter before print.
- bonchi2024diagrammatic §10 (p. 12) is the authors' own later assessment. It says this paper's primitive cut "inhibits a fully compositional treatment since, for instance, negation is not functorial". The 2024 paper fixes this by deriving negation.
- Another string-diagram calculus for Beta, by Brady & Trimble (2000), is cited as refs. 2–3 and was not carded.
