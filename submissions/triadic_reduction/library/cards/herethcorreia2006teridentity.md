---
citekey: herethcorreia2006teridentity
title: "The Teridentity and Peircean Algebraic Logic"
authors: "Hereth Correia, Joachim; Pöschel, Reinhard"
year: 2006
venue: "Schärfe, H.; Hitzler, P.; Øhrstrøm, P. (eds.), Conceptual Structures: Inspiration and Application (ICCS 2006, Aalborg) | Springer | LNAI 4068 (LNCS series), 229–246"
doi: "10.1007/11787181_17"
section: "S1, S4"
status: candidate
verified: corrected
source_basis: "Author preprint PDF (23 pp., A4, dvips/Ghostscript) from R. Pöschel's TU Dresden page (https://wwwpub.zih.tu-dresden.de/~poesch-r/poePUBLICATIONSpdf/2006_Hereth_Poe_Teridentity.pdf), read in full via pdftotext -layout; a fresh download from that URL on 2026-09-24 has the same sha256 as the local copy. DOI, pages 229–246 (Crossref) and editors confirmed in Crossref and OpenAlex; volume 4068 confirmed by a web-search listing of the proceedings (ISBN 3-540-35893-5, Crossref ISBN 9783540358930) and by hereth2011logic's reference list"
access_url: "https://wwwpub.zih.tu-dresden.de/~poesch-r/poePUBLICATIONSpdf/2006_Hereth_Poe_Teridentity.pdf"
retrieved: 2026-09-24
sha256: "bfe73461549666d7b019403591fcdfb19e2d44a96df7e86c996a42651d181bd7"
---

## What the talk may use it for
This paper proves the hard clause of the thesis in its strongest PAL form. PAL here means product, join of two places (δ^{i,j}), complement and permutation, with teridentity id3 as the only built-in constant. Burch's rule on when a product may be taken is dropped. Theorem 2: for **any** set A with |A| ≥ 2 and Σ = Rel^(1)(A) ∪ Rel^(2)(A), ⟨Σ⟩_PAL∖{id3} ⊊ ⟨Σ⟩_PAL, and the missing relation is id3 itself. Negation is allowed and A may be infinite. The key invariant is Lemma 1: in a term built from unary and binary relations without id3, no set of more than two places is connected. The proof uses a union-of-intersections normal form (∪∩-representation) and a "crux lemma" on cores of binary relations. The paper does not prove the constructive clause and points to Herzberger 1981, Burch 1991 and Hereth Correia & Pöschel 2004 for it.

## Loci
Page numbers of the 23-page preprint, not the LNAI pagination.
- p. 1 (abstract) — "Using a restriction on the allowed constructions, he is able to prove the Peircean Reduction Thesis, that in PAL all relations can be constructed from ternary relations, but not from unary and binary relations alone." — what Burch 1991 proved, and on what condition.
- p. 1 (abstract) — "This is a mathematical version of Peirce's central claim that the category of thirdness cannot be decomposed into the categories of firstness and secondness." — the authors' own framing: a mathematical *version* of the category claim, not an identity with it.
- p. 2 — "The triad is the lowest form of relative from which all others can be derived." — Peirce, MS 482, quoted from the Robin catalogue [PR67]. This is one transcription, not checked against the manuscript; the peirce cluster owns it.
- p. 2 — "According to Herzberger in [Her81] Peirce mentioned he found a proof, but no corresponding publication has been found."
- p. 2 — "provides a first approach for an algebraic proof" — on Herzberger 1981.
- p. 2 — "The juxtaposition of graphs (this corresponds to the product Def. 1(1)) is only allowed as last or before last operation." — Burch's restriction, stated exactly.
- p. 2 — "Many attempts have failed for non-obvious reasons."
- p. 2 — "we present the complete mathematical proof of the difficult part of the reduction thesis."
- p. 2 — "we will not show the part that any relation can be constructed (in PAL) from ternary relations. For this, we refer to [Her81], [Bur91] or [HCP04]."
- p. 6 (Lemma 1) — "Then |X| ≤ 2." — for Σ = Rel^(1) ∪ Rel^(2), a ⟨Σ⟩_PAL∖{id3}-term t, and a t-connected set X of places.
- p. 12 (§1.4) — "They correspond to disjunctive-conjunctive (normal) forms of first-order predicate logic formulas." — the ∪∩-representations.
- p. 21 (§3) — "therefore at least one ternary relation is needed besides unary and binary relations to generate all relations."
- p. 21 (Theorem 2) — "Let |A| ≥ 2 and Σ := Rel(1) (A) ∪ Rel(2) (A). Then" ⟨Σ⟩_PAL∖{id3} ⊊ ⟨Σ⟩_PAL (the inclusion symbol is garbled in the text layer; the words were matched).
- p. 22 (end of proof) — "Therefore the teridentity is not representable in PAL without teridentity."

## What the preliminary sources claim about it
- hp-2006-teridentity-bib (TR-S4-020, -104) → verified: LNAI 4068, 229–246. hereth2011logic cites it as "230–247", and koshkin2022reduction's list gives "v. 4069". Use 4068, 229–246.
- hp-2004-2006-bib (TR-S4-098) → verified.
- hp-2006-teridentity-nonconstructible (TR-S4-135, -163, -164, -170) → verified. The proof removes Burch's restriction, allows complement and unrestricted products, and holds for any A with |A| ≥ 2 (Theorem 2). It covers "the difficult part" only.
- hp-2006-connectivity-bound (TR-S4-166, -169) → corrected. Lemma 1 bounds the size of *t-connected sets of places of a term* (|X| ≤ 2). It is not a bound on "connected components of a relation". The terms may use product, join, complement and permutation, but not id3.
- hp-2006-normal-form (TR-S4-165) → verified: ∪∩-representations, which the authors liken to disjunctive-conjunctive normal forms.
- hp-2006-normal-form (TR-S4-167) → corrected. Theorem 1 gives, for each term, a ∪∩-representation whose member relations have at most two essential places (i), are pairwise comparable or inverted-comparable when their essential places overlap (ii), and are themselves generable without id3 (iii). "E(σ) preserve pairwise comparability" garbles (ii).
- hp-2006-fixed-base-set (TR-S4-168, -171) → verified. All relations live on one fixed set A (Def. 1–2), and no domain extension or encoding is used. "Relies heavily" is the source's framing; the theorem simply has no step that changes A.
- teridentity-degree-3 (TR-S1-055) → corrected. The paper shows that all three places of id3 are essential (Lemma 3(ii)) and that without id3 no t-connected set has more than two places (Lemma 1). "Connectivity degree 3" is a paraphrase of that pair.
- teridentity-not-generated-from-dyads (TR-S4-042, -045, -088) → corrected. True in PAL without id3 for |A| ≥ 2 (Theorem 2). It is not a theorem of "clone theory": in pp/co-clone closure =3 is x=y ∧ y=z (dau2006instances p. 108). TR-S4-090's attribution to Burch 1991 holds only under his juxtaposition restriction.
- teridentity-join-irreducible (TR-S4-003, -093, -099, -204) → refuted. None of the three PAL papers uses "join-irreducible" (grep of the full texts: 0 hits). In the lattice of relational clones, ⟨{=3}⟩_RA = ⟨∅⟩_RA = D_A (herethcorreia2004power §3) is the bottom element, so the lattice term does not apply. The likely source of the phrase is PAL's operation called "join" (δ^{i,j}): the theorem says id3 cannot be *built by PAL joins* from unary and binary relations.
- pal-vindicated-peirce (TR-S4-036, -037, -194) → corrected. The results are PAL theorems (Burch with his restriction; this paper and hereth2011logic without it), not proofs "within closed relational clones". The clause about teridentity's irreducibility is right.
- burch-terminal-juxtaposition-restriction (TR-S4-142, -145, -200) → verified in substance: juxtaposition only "as last or before last operation" (p. 2). hereth2011logic p. 6 gives the mechanism, Burch's join2 = δ(ρ × σ) followed by a final product step.
- burch-restriction-undermines-universality (TR-S4-147, -148, -149) → corrected. Removing the restriction breaks Burch's *proof*, not his expressivity: dau2006instances p. 106 says "Burch proves that the expressivity is still the same". TR-S4-149's "unrestricted relational algebra could synthesize =3" is trivially true (=3 is a diagonal). The open question was unrestricted PAL *without teridentity*.
- prt-negative-clause (TR-S1-001, -020, -022, -023, -031, -051, -054) → corrected. The safe statement is this paper's Theorem 2: in PAL without teridentity, unary and binary relations on any set with at least two elements do not generate id3. "Never" and "proves" need that scope. The authors call it "a mathematical version" of the Thirdness claim, so TR-S1-054's "non-reducibility of Thirdness" goes beyond them.
- monadic-dyadic-basis-no-branch (TR-S1-053) → corrected: the formal content is Lemma 1 and Theorem 2. "3-star node" is not the source's term.
- hp-2004-predecessor-of-2006 (TR-S4-133) → verified: the paper refers to [HCP04] for the constructive part (p. 2) and builds on its restriction-free PAL.
- thirdness-is-teridentity (TR-S1-019, -074) → refuted: the authors call the theorem "a mathematical version" of the Thirdness claim (abstract). They do not identify Thirdness with id3.
- thirdness-triad-tier (TR-S1-039) and teridentity-necessary-for-integration (TR-S1-060) → unverifiable: interpretive alignments with no PAL source. In PAL, teridentity is needed to identify one variable across three or more places (herethcorreia2004power Fig. 4); "synchronizing variables across a complex system" has no source.
- teridentity-and-synergy-not-from-dyads (TR-S1-058) → corrected: the teridentity half holds only in PAL without id3 (Theorem 2). The synergy half has no support in the PAL papers (see williams2010decomposition). Do not join them under one citation.
- degree-2-graphs-paths-and-cycles (TR-S1-007, -028, -036) → verified as graph theory (a graph of maximum degree 2 is a disjoint union of paths and cycles). No source read states that sentence; the formal counterparts are Lemma 1 here and herethcorreia2004power Remark 14.

## Notes
- This is a preprint whose text matches the published abstract. The LNAI typeset text (Crossref: pp. 229–246, doi 10.1007/11787181_17) was not read, so page numbers are preprint pages. Cite the LNAI chapter; the TU Dresden URL is the access copy.
- The hard direction is proved for any A with |A| ≥ 2. The earlier-in-2006 ICFCA paper, dau2006instances, covered only infinite and two-element domains.
- The paper uses one join operator where Burch used two (p. 2).
