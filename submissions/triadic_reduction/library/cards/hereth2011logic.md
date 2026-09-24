---
citekey: hereth2011logic
title: "Peircean Algebraic Logic and Peirce's Reduction Thesis"
authors: "Hereth, Joachim; Pöschel, Reinhard"
year: 2011
venue: "Semiotica 2011(186): 141–167 (special issue 'Diagrammatical reasoning and Peircean logic representations')"
doi: "10.1515/semi.2011.050"
section: "S1, S4"
status: candidate
verified: corrected
source_basis: "Author preprint PDF (30 pp., TeX, dated 28 Aug 2009) from R. Pöschel's TU Dresden page, read in full via pdftotext -layout; its abstract matches the published abstract in OpenAlex almost word for word. DOI, year, issue 186 and author forms confirmed in Crossref and OpenAlex; pages 141–167 from Semantic Scholar and the lab's references.bib; issue title from F. Dau's publications page (listing his paper in the same issue)"
access_url: "https://wwwpub.zih.tu-dresden.de/~poesch-r/poePUBLICATIONSpdf/2011_Hereth_Poe.pdf"
retrieved: 2026-09-24
sha256: "310d30e602e927b34cf3578b446ad6b8506bc47d1a57075a4a964043868d63a0"
---

## What the talk may use it for
This is the most readable complete statement and proof of both clauses in restriction-free PAL. The operations are product, join of two places, complement, permutation and the constant teridentity. The thesis is stated as: for Q the set of all unary and binary relations, ⟨Q⟩_PAL− ⊊ ⟨Q⟩_PAL "independently from the underlying set A" (|A| ≥ 2), where PAL− omits teridentity. The constructive clause is proved in PAL. Every finite relation is a union of singleton tuples built from unary relations, with teridentity nodes and negation ovals doing the union. For **infinite** relations the construction needs a bijection µ: A×A → A, whose graph is a ternary relation, and so needs the axiom of choice for arbitrary infinite A. The irreducibility clause is proved with a union-of-intersections normal form and the "Crux Lemma" on cores of binary relations.

## Loci
Page numbers of the 30-page preprint, not the Semiotica pagination.
- p. 1 (abstract) — "that all relations can be generated from the ensemble of unary, binary and ternary relations, but that at least some ternary relations cannot be reduced to relations of lower arity." — the thesis as the authors state it.
- p. 2 — "In the following we assume that A has at least two elements."
- p. 6 — "Formally, Peirce's Reduction Thesis can be stated as follows: let Q be the set of all unary and binary relations, then independently from the underlying set A the set" ⟨Q⟩_PAL− "is a strict subset of" ⟨Q⟩_PAL (the set symbols are garbled in the text layer; the words were matched).
- p. 6 — "Burch (1991) introduces an operation join2 , which allows the product of two relations if they are joined directly after" — Burch's restriction: products only as δ(ρ × σ), and free products only in a second, final step.
- p. 6 — "allows to generate graphs which could not be generated with the original PAL." — on the authors' relaxed version.
- p. 8 — "we have shown, that any finite relation can be constructed from ternary relations with PAL-operations."
- p. 8 — "However, this construction does not work for infinite relations." — continued on p. 9 with the bijection between A and A × A.
- p. 19 — "if A is finite than we can represent teridentity as the union of its tuples and each tuple can be represented as the intersection of three unary singleton relations" — why the proof is not trivial.
- p. 28 — "Therefore teridentity cannot be constructed not using teridentity itself. This was the proof of Peirce's Reduction Thesis."
- p. 28 (note 2) — "To prove that such a bijection exists for any infinite set A one uses the axiom of choice too."

## What the preliminary sources claim about it
- hp-2011-semiotica-bib (TR-S4-046) → corrected. Cite Hereth, Joachim & Pöschel, Reinhard (2011), "Peircean Algebraic Logic and Peirce's Reduction Thesis", *Semiotica* 2011(186): 141–167, doi:10.1515/semi.2011.050, not ResearchGate. The first author publishes here as "Hereth", not "Hereth Correia". The lab's references.bib has this right (hereth2011pal); koshkin2022reduction's list gives "Semiotica, 86", a typo for 186.
- prt-positive-clause (TR-S1-002, -024, -033, -044, -050) → corrected. In PAL the positive clause is a theorem here (§3). Finite relations need teridentity and complement (for union). Infinite relations need, in addition, the ternary graph of a pairing bijection A×A → A. So "universally sufficient" holds relative to PAL's operations, and on infinite domains it rests on the axiom of choice. For the pp version, see koshkin2025completeness (Theorem 2: n ≥ 4 reduces to ternaries on any domain). TR-S1-050's "n ≥ 3 vs n ≥ 4" is moot: the construction here starts from arbitrary n and first rebuilds unary and binary relations from ternary ones.
- polyads-from-subcubic-teridentity-networks (TR-S1-075, -076) → corrected. The construction builds relations from unary singletons, teridentity nodes and negation (finite case) plus a pairing graph (infinite case). "Subcubic networks of teridentities" is not the paper's term, and the construction is not "entirely" teridentities. koshkin2022reduction's Fig. 3 (hypostatic abstraction split into teridentities) is closer to that wording.
- ternary-completeness (TR-S4-192) → corrected. Cite Herzberger 1981 or Burch 1991 for the constructive clause as they set it up (herethcorreia2006teridentity p. 2), and this paper §3 for restriction-free PAL. Do not cite "PAL" generically.
- two-invariant-results (TR-S4-013) → corrected. The two clauses are separate theorems with different operation sets and domain conditions: irreducibility in PAL− for any A with |A| ≥ 2 (§6; herethcorreia2006teridentity Theorem 2), and constructibility in PAL with teridentity and negation (finite A) plus a pairing bijection (infinite A) (§3).
- peirce-generative-internal-standpoint (TR-S1-003) → unverifiable. None of the four PAL papers read contrasts a "generative, internal standpoint" with a closure view. The nearest wording is Burch's "unitary logical vision" (p. 1, quoting Burch 1991: 3).
- relational-clone-generation-question (TR-S1-004) → corrected. The fixed-universe generation question is the algebraic reformulation stated here (p. 6) and in herethcorreia2004power. dau2006instances p. 106 says the thesis "is not stated explicitly in Peirce's work". Attribute the wording to Hereth & Pöschel, not to Peirce.
- pairing-is-triadic-relation (TR-S3-021) → corrected. This paper uses the *graph* of a pairing bijection µ as a ternary relation (pp. 8–9) to reduce arity on infinite domains, so pairing enters the constructive clause as a triad. That makes pairing a ternary relation in PAL's bookkeeping. The paper does not prove that the pairing graph is irreducible.
- teridentity-diagonal-definition (TR-S1-026, -034, -041, -046) → verified: teridentity is the diagonal {(a, a, a) | a ∈ A} (herethcorreia2004power Def. 7). "Join-irreducible" (TR-S1-041, -046) occurs in none of the PAL papers.
- triads-primitives-algebra-and-info-theory (TR-S1-070) → corrected: the algebra half holds in PAL (§3 and §6 here) and, for n ≥ 4, in pp terms (koshkin2025completeness Theorem 2). No PAL source makes the information-theory half.
- polyad-synthesized-thirdness (TR-S1-082) → unverifiable: no PAL source maps polyads to "synthesized Thirdness".

## Notes
- The preprint predates publication by two years. The Semiotica typeset text was not read, so the page numbers are preprint pages.
- The abstract dates the full proof to Hereth's 2008 TU Dresden dissertation, "Relation Graphs and Contextual Logic: Towards Mathematical Foundations of Concept-Oriented Databases", which has not been read.
- The paper reports herethcorreia2006teridentity as pp. 230–247; Crossref gives 229–246.
- The claim that the positive clause on infinite domains uses a pairing function is directly relevant to the talk's Quine section. The Peircean constructive clause and the Löwenheim–Quine reduction use the same device, and here it counts as a triad.
