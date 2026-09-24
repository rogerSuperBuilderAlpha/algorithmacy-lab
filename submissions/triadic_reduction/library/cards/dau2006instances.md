---
citekey: dau2006instances
title: "Two Instances of Peirce's Reduction Thesis"
authors: "Dau, Frithjof; Hereth Correia, Joachim"
year: 2006
venue: "Missaoui, R.; Schmid, J. (eds.), Formal Concept Analysis (ICFCA 2006, Dresden) | Springer | LNAI 3874 (LNCS series), 105–118"
doi: "10.1007/11671404_7"
section: "S1, S4"
status: candidate
verified: corrected
source_basis: "Published-version PDF (14 A4 pages, one per LNAI page, with LNAI running heads 105–118 and the footer 'ICFCA 2006, LNAI 3874, pp. 105–118'), posted on F. Dau's own publications page, read in full via pdftotext -layout; DOI and pages confirmed in Crossref and OpenAlex"
access_url: "http://www.dr-dau.net/Papers/pal.pdf"
retrieved: 2026-09-24
sha256: "c1ff933e90144c6b72e453079eae8c7999c4c887df1024cd666c5509e0ced0a5"
---

## What the talk may use it for
The paper proves the irreducibility clause in unrestricted PAL for two special cases only: infinite domains (Corollary 1, a counting argument on a DNF-like normal form) and two-element domains (Corollary 2, a class-inheritance argument). It calls these "the first steps toward the proof". It also states outright that teridentity is **constructible in ordinary relational algebra** from the binary identity, =3 = ∆(ζ(= × =)), where ∆ identifies two coordinates and ζ is cyclic shift. On this reading the teridentity is "hidden" in coordinate identification, and the thesis is a claim about PAL's operations, not about pp-definability. This is the clearest published sentence for the talk's point that FOL's repeated variables smuggle in teridentity.

## Loci
LNAI page numbers, read from the running heads of the published PDF.
- p. 105 (abstract) — "This representation is then used to prove the thesis for infinite and two-element domains."
- p. 106 — "His description of Existential Graphs is too vague to suit the requirements of contemporary mathematics."
- p. 106 — "He uses this logic system to prove Peirce's reduction thesis, namely, that ternary relations suffice to construct arbitrary relations, but that not all relations can be constructed from unary and binary relations alone." — on Burch 1991.
- p. 106 — "While this thesis is not stated explicitly in Peirce's work [Pei35b], this idea appears repeatedly."
- p. 106 — "the juxtaposition of disjoint graphs is only allowed as last or second-last operation. While Burch proves that the expressivity is still the same, this restriction is a major difference to the original system of Existential Graphs."
- p. 106 — "In this paper we provide the first steps toward the proof, concentrating on the special cases of a domain with only two elements and of domains with infinitely many elements."
- p. 106 — "we define representations of the constructed relations similar to the disjunctive normal form (DNF) known from first-order propositional logic."
- p. 107 — "This means that the teridentity would be somehow hidden in the operations from relational algebra." — continued: "this is at least difficult for the identification of the first two coordinates … Proving the Peircean Reduction Thesis will show that this is not only difficult but impossible."
- p. 108 — "In relational algebra, we can construct the teridentity in relational algebra using product, cyclic shift ζ (the tuples are rotated: see [HCP04], Def. 2,R2a) and identification of the first two coordinates from the binary identity" — followed by the formula =3 = ∆(ζ(= × =)) (symbols transcribed from the text layer).
- p. 114 (Corollary 1) — "Particularly, for an infinite set A, there exists no PG which evaluates to the teridentity on A." — the corollary's first sentence gives the finite bound: if |A| > n(G), the graph G does not evaluate to =3.
- p. 114 — "But this argument does not apply to finite domains."
- p. 117 (§6) — "The methods and ideas presented in this paper will be continued to a complete proof of Peirce's Reduction Thesis."

## What the preliminary sources claim about it
- dau-hc-2006-bib (TR-S4-021, -105) → corrected. The pages are **105–118**, not 215–229. The rest (LNAI 3874; Dau, F. & Hereth Correia, J.; 2006) is right. The author order on the paper, in Crossref and on Dau's page is Dau first; koshkin2022reduction lists "Hereth Correia and Dau", which reverses it.
- dau-hc-2006-result (TR-S4-110, -111, -116) → verified. The paper uses PAL with juxtaposition, cut (negation) and join and no ordering restriction, introduces a relational normal form "similar to the disjunctive normal form", and proves the thesis for infinite and two-element domains.
- dau-hc-2006-finite-gap (TR-S4-117) → verified for this paper: finite domains with more than two elements are left open (pp. 106, 114, 117). herethcorreia2006teridentity, published later in 2006, closed the gap for every |A| ≥ 2.
- existential-graphs-too-vague (TR-S4-112) → verified: p. 106, quoted above. The paper says this about Peirce's *description* of EGs, as a reason why their equivalence with FOL cannot be proved from his text.
- pal-rigorous-foundation-eg (TR-S4-113) → verified in substance. Burch's PAL is described as reconstructing Peirce's system "in an algebraic precise manner" (abstract).
- prt-lacked-proof-before-2006 (TR-S4-114) → corrected. Burch 1991 did prove the thesis, "but" under the juxtaposition restriction (p. 106). What was missing before 2006 was a proof *without* the restriction. This paper supplies it for infinite and two-element domains, and herethcorreia2006teridentity for all |A| ≥ 2.
- pal-relational-normal-form (TR-S4-115) → verified (abstract; Theorem 1, p. 110).
- hp-2004-closure-coordinate-identification (TR-S4-158) → corrected. The construction is from this paper, p. 108: =3 = ∆(ζ(= × =)), with ∆ identification of the first two coordinates. It shows that =3 *is* in the relational-algebra (pp) closure of the binary identity.
- fol-variable-sharing-hides-teridentity (TR-S1-010) → verified with a correction. The paper says the teridentity is "hidden in the operations from relational algebra", specifically in identification of coordinates (p. 107). Two occurrences of a variable are a plain two-hook join; teridentity is needed when one variable fills three or more places.
- prt-both-clauses (TR-S1-047) → verified as a paraphrase of p. 106, which gives Burch's statement: ternary relations suffice, and not all relations can be constructed from unary and binary relations alone. The paper adds that the thesis "is not stated explicitly in Peirce's work".
- dyadic-pp-clone-excludes-teridentity (TR-S4-109, which cites this paper) → refuted as a pp claim. This paper constructs =3 in relational algebra (p. 108). The non-constructibility holds only in PAL.
- prt-both-clauses (TR-S1-014, -078), beside TR-S1-047 above → corrected: the two-clause statement is Burch's, in PAL (p. 106). TR-S1-078's "dyads can never generate triads" is false under relational-algebra (pp) closure, where =3 = ∆(ζ(= × =)) (p. 108), and needs the scope "in PAL without teridentity".

## Notes
- The PDF on Dau's page carries the Springer running heads and copyright line, so it appears to be the published version; the page numbers above are LNAI pages.
- Dau's publications page lists the paper under "Lecture Notes in Computer Science, Vol. 3874"; the paper's own footer says LNAI 3874 (LNAI is a subseries of LNCS).
- The paper's ∆ is herethcorreia2004power's (R3), identification of the first two coordinates. Its projection and renaming are "technical operations which do not belong to PAL (but they can be constructed within PAL)" (p. 108).
