# Pairs, triads and the target of algorithmacy: the argument

*Evidence document, not the script. Synthesized 2026-09-24 from three independent reconstructions (logic-first, Peirce-text-first, lab-results-first) after critique for validity, textual fidelity and lab consistency. Every premise names its support: a library card and locus, a CI check and expect string, or a register id.*

*This is the evidence document for the ALGOCON talk (Port of Spain, 28–31 October 2026, 20-minute slot). It is not the script. Each quotation carries its card and locus. Each lab number carries its CI check and the exact expect substring from `ci/reproduce.json`.*

*Status tiers follow the cards:*
- ***page image***: matched on the printed page.
- ***transcription***: matched in two or more editions or transcriptions, with no page image.
- ***preprint***: read in full, cited by arXiv or author-copy pagination.
- ***snippet***: seen only through search-inside.
- ***metadata-only***: not read.

*Register ids (TR-…) point to `submissions/triadic_reduction/claims/register.json`. Card citekeys point to `submissions/triadic_reduction/library/cards/`.*

## The argument in one paragraph

Peirce claimed in 1870 that no triad can be built from pairs. He defended the claim with valency arithmetic, and that arithmetic holds only if a junction of three lines counts as a relation. Simmel found the same step in social form: a third opens a second route between each pair. He also saw that three parties can remain "configurations of twos". Löwenheim (1915) and Quine (1954) coded every relation with one dyadic predicate. Each did it by minting an object that stands for the tuple, just as Kempe minted his unit λ and Peirce his "this action". The logicians who came after proved that the answer depends on the operations allowed. Burch says both sides were right; Koshkin says they cannot both be. The regimes split on one point, the status of the three-way junction, and definability cannot settle it because an extensional junction has no direction. The lab gives the junction a direction. IIT 4.0's partition test separates three things the logical debate ran together:
- fan-out, an effect-side branch;
- fan-in, a party jointly determined by two others;
- wholeness, a system that does not factor.

Among fixed parties, one-input determination never composes into joint determination. Joint determination inside a whole exists. Literacy coordinates through one-input mediation and algorithmacy through joint determination in a whole, so algorithmacy has a target that literacy's structure cannot compose. The argument shows this on Boolean models. It does not show it on people.

## Terms

**D1 (definition). Composition regime.** A relation R is reducible to a stock Σ of lower-adicity relations under operations O when R lies in the closure of Σ under O. The literature uses four regimes:
- (a) bonding, or PAL without teridentity, where each bond joins exactly two places;
- (b) primitive-positive (pp) or relational-algebra closure, where a variable may be shared by any number of factors and coordinates may be identified;
- (c) pp plus projection with domain extension (hypostatic abstraction);
- (d) set-theoretic pairing over a pair-closed universe.

*Support:* burch2021sep §14 (verified): "the issue entirely depends on exactly what constructive resources are to be allowed to be used in building relations out of other relations". Also koshkin2024reduction p.3, p.12, Thm 13 p.20 (preprint), and herzberger1981theorem T9, T11 (snippet).

**D2 (definition). The lab's rendering.** The lab renders a *dyad* as a one-input rule (node_i′ = node_j) and a *relation* as an irreducible distinction (φ > 0) in the system's IIT 4.0 cause–effect structure. A distinction's *adicity* is |mechanism ∪ purview|, read separately for the cause side and the effect side. *Φ_MIP* is system integrated information over the minimum-information partition. The *major complex* (core) is the maximal irreducible subset.

*Support:* org_frontier/thinkers/peirce/paper.md ("From claims to forms"; Methods). peirce/forms.py `genuine_adicity` (l.101–135: ad_c = |m ∪ cause purview|, ad_e = |m ∪ effect purview|). albantakis2023information p.5 ("Irreducibility is measured by integrated information (φ) over the substrate's minimum partition."), p.23 (mechanism partitions).

**D3 (stipulation, locked by the author). The triad criterion.** An irreducible triad is joint determination in a whole: a party jointly determined by two others (cause-side adicity 3) inside a system that does not factor (Φ > 0). Φ > 0 alone is not the test.

*Operational form, which builds on the lock and does not change it:* there is a first-order distinction whose mechanism is one party X, whose irreducible cause purview contains two other parties Y and Z, and X, Y and Z all lie in the major complex.

This operational wording closes two gaps in the bare gloss:
- **Cause-side adicity 3 is broader than joint determination.** A two-element mechanism with a one-element cause purview also scores 3. Two copies of one source, read backward, are an example.
- **"Whole" is ambiguous.** It can mean whole-system Φ_MIP or the major complex. In `two_input_00` the whole system reads Φ_MIP = 0.830075, yet the core is {B, C}. In `mediator_eliminated` the whole system reads Φ_MIP = 0 while a core {A, B} sits inside it at coreΦ = 2.000.

Every registered exemplar passes on either reading, because each exemplar's core equals its whole system.

*Support:*
- README.md "Triad criterion (fixed 2026-09-24)".
- STRUCTURAL_FINDINGS.md L65–68, of which only "The number of parties is not the variable" may be quoted. The rest of that law was written under the superseded Φ-only rule.
- peirce/paper.md l.135–137, which rejects Φ > 0 as the mark of genuineness.
- CI thinkers-peirce-h5-polyads: `two_input_00           Φ_MIP=0.830075  core=('B', 'C')             adicity=4 (cause 4, effect 4)  BD -> cause AC effect C (φ=1.000)`.
- CI thinkers-simmel-h4-nonpartisan: `mediator_eliminated    dyadic   Φ_MIP=0.000000  core=('A', 'B') coreΦ=2.000`.

*Disclosure:* the author fixed the criterion on 2026-09-24, after the probes had run. It tightens the lab's own classifier rule (P28).

**D4 (definition, the talk's). The two competences, stated structurally.**
- *Literacy* is the competence for coordinating through one-input mediation: a medium whose next state answers to one party at a time, however it is chained or looped.
- *Algorithmacy* is the competence for coordinating through joint determination in a whole: a third that both parties determine and that acts back on both.

These structural definitions sharpen the lab's teleological wording (P35). They depart from that wording at one point, noted in P36.

**D5 (stipulation, the author's conditional, restated in the sense the talk argues).**
- If every coordination form in which a party is jointly determined by two others could be rebuilt from one-input mediations among the same parties, algorithmacy would have no target distinct from literacy's. It would be literacy applied link by link.
- If some such form cannot be rebuilt that way, algorithmacy has a target of its own.

*Why restate it:* stated as "if triads reduce to dyads", the conditional uses the Peirce–Quine sense of definability. In Quine's regime, triads do reduce (C3), so both horns would fire and the dilemma would settle nothing. The talk fixes "reduce" as causal composition among the same parties, and P34 defends that choice.

*Support:* author's thesis statement (task brief); README paragraph 2.

---

## S1. Peirce's logical argument

**P1 (textual).** Peirce first stated both clauses in one sentence of a memoir communicated on 26 January 1870:

> "A relative term cannot possibly be reduced to any combination of absolute terms, nor can a conjugative term be reduced to any combination of simple relatives; but a conjugative having more than two correlates can always be reduced to a combination of conjugatives of two correlates."

A conjugative of two correlates is a triadic term. The sentence therefore holds both clauses: no triad from dyads, and every higher term from triads. Peirce argued for neither clause. He illustrated only the positive one (p.374; generalized at the top of p.375), and he conceded: "I have, however, studied this part of my notation but little." The origin is 1870, not 1897.

*Support:* peirce1870description p.374 = CP 3.144 (page image; card status corrected); p.317 "Communicated January 26, 1870."; p.375. The volume is Memoirs AAAS 9, dated 1873, and the SEP cites it as "1873 [1870]". Register TR-S1-067 (corrected: 1897 is not the origin).

**P2 (textual).** Peirce's argument for the negative clause is valency arithmetic, and he gave it three times.
- *In words* (CP 1.363): two triads joined at one blank "will form a whole having four blank places". With two dyads, "we find we only have two blank places in the combination, just as we had in either of the relatives taken by itself."
- *As a formula* (Monist 1897): "In general, the union of a μ-ad and a ν-ad gives a (μ+ν−2λ)-ad, where λ is the number of bonds of union. This formula shows that artiads, or even-ads, can produce only artiads."
- *As an image* (CP 1.363): "A road with only three-way forkings may have any number of termini, but no number of straight roads put end on end will give more than two termini."

*Support:* peirce1890guess CP 1.363, vol.1 p.188 (page image; dated 1887–88 in W6, c.1890 in CP). peirce1897logic p.183 §5 (page image).

**P3 (logical).** If every bond joins exactly two places, any composition of dyads has adicity 2 + 2 − 2λ. That number is even, so it is never 3. Triads are odd, and their compositions reach every adicity. Under bonding, dyads never yield a triad and triads yield everything. In graph terms, a graph of maximum degree 2 is a disjoint union of paths and cycles.

*Support:*
- peirce1897logic p.183 ("any perissid, or odd-ad (except a monad), can by repetition produce a relative of any adinity").
- herzberger1981theorem, valency rule p.52 (via Conarroe p.138).
- herethcorreia2004power Remark 14, p.12 ("such that every vertex has valency at most 2"; preprint).
- Register TR-S1-007 and TR-S1-028 (verified as graph theory).

**P4 (textual).** The formula holds only if a junction where three lines meet counts as a relation and not as free wiring. Peirce argued for that condition in three places:
- Monist 1897, pp.170–71: "every node of bonds is equivalent to a relative".
- Lowell Lectures 1903: "You may think that a node connecting three lines of identity Y is not a triadic idea. But analysis will show that it is so." Quote both sentences, because splicing them drops the negation.
- Letter to Lady Welby, 1904: "no branching of a line can result from putting one line on the end of another."

*Support:* peirce1897logic pp.170–171 (page image of p.171). peirce1931papers CP 1.346, vol.1 p.176 (page image). peirce1904letter CP 8.331 (transcription: CP 8 scan, Hardwick, Wiener).

**P5 (textual).** Kempe (1886) drew every relationship with units and two-ended links. §330 draws an isolated triad as an auxiliary unit λ with three links. "Isolated" is Kempe's technical term (§328): each unit is unique with respect to the other two.

Peirce answered in 1892:
- He called it "a formidable objection to my views".
- He conceded that Kempe "virtually shows that my algebra is perfectly adequate to expressing that A gives B to C", and noted that "This is accomplished by adding to the universe of concrete things the abstraction 'this action.'"
- He replied that "the diagram fails to afford any formal representation of the manner in which this abstract idea is derived from the concrete ideas", and that mediation lies in "the attachment of lines to spots".
- He modified his position "but not to surrender it."

So Peirce conceded expressibility through a minted object and denied composition.

Two hazards:
- Between the two concession sentences, Peirce lists three dyadic relations to an act D ("In a certain act, D, something is given by A; …"). That list is matched only in local CP 3 scan OCR. Add it to peirce1892critic before any slide quotes it.
- The CP excerpt of the Welby letter (CP 8.327–341) does not mention Kempe, so the branching aphorism is not a reply to Kempe.

*Support:* kempe1886memoir §68 pp.12–13, §328 and §330 p.57 (page images). peirce1892critic CP 3.423–424, Open Court 6: 3417–3418 (verified). peirce1897logic p.168 (Peirce's charge against Kempe). peirce1904letter Notes.

**P6 (textual).** In 1904 Peirce turned the same point on his own algebra: "The criticism which I make on [my] algebra of dyadic relations … is that the very triadic relations which it does not recognize, it does itself employ. For every combination of relatives to make a new relative is a triadic relation irreducible to dyadic relations." The bracketed "[my]" is the CP editors' substitution; Hardwick and Wiener print "that algebra".

*Support:* peirce1904letter CP 8.331 (transcription). Register TR-S1-009 (corrected wording).

**P7 (textual).** Giving is Peirce's type case of a genuine triad.
- *Genuine giving* "consists in A's making C the possessor according to Law" (CP 8.331).
- *The imitation*, "A's laying down the B which C subsequently picks up", is "a degenerate form of Thirdness in which the thirdness is externally appended" (CP 8.331).
- *Throwing B so that it happens to hit C* would be "merely one dyadic relation followed by another" (CP 1.345).
- The three dual relations must "be welded into one fact" (CP 1.363).

Peirce's test is whether the three are welded. How many parties there are does not decide it.

*Support:* peirce1904letter CP 8.331 (transcription). peirce1931papers CP 1.345, vol.1 p.176 (page image). peirce1890guess CP 1.363 p.188 (page image). Peirce's grades of degeneracy (CP 1.473) are matched only in OCR; keep them off slides until someone checks them on the vol.1 page image.

**P8 (textual).** Peirce made the sign genuinely triadic.
- CP 2.274: "The triadic relation is genuine, that is its three members are bound together by it in a way that does not consist in any complexus of dyadic relations."
- CP 5.484: semiosis is "a coöperation of three subjects, such as a sign, its object, and its interpretant, this tri-relative influence not being in any way resolvable into actions between pairs."
- CP 8.332: "In its genuine form, Thirdness is the triadic relation existing between a sign, its object, and the interpreting thought".
- CP 1.345: "every genuine triadic relation involves thought or meaning".

On Peirce's account, reading is irreducibly triadic, and S6 must face this.

*Support:* peirce1931papers CP 2.274, vol.2 p.156 and CP 5.484, vol.5 p.332 (page images). peirce1904letter CP 8.332 (transcription). Register TR-S1-062 (verified).

**C1 (inference from P2–P6).** Peirce's negative clause is a valency theorem, and it is conditional on counting every three-way junction as a relation. Dyads laid end to end make chains and rings; a triad appears only where a line branches. Peirce answered every dyadic construction the same way:
- Kempe's λ: the attachment carries mediation.
- The minted "this action": its derivation is not represented.
- His own algebra: the combining step is itself triadic.

From its first round, then, the dispute concerns the status of the junction. *Rule:* parity arithmetic of μ + ν − 2λ with two-place bonds, plus Peirce's premise that a node is a relative.

**C1b (inference from P7).** Peirce separates genuine giving (possession fixed under one law) from its imitation (two dyads in sequence) by whether the three are welded into one fact. Headcount does not decide it.

---

## S2. Simmel's triads

**P9 (textual).** Simmel located what the dyad lacks. When one member refuses, "only the other remains, without any superindividual energy such as, even in the case of a combination of only three, is in some measure present." With three, "each pair of elements are now joined by a broken line": A reaches B directly and also through C.

*Support:* simmel1902number1 p.45, trans. Small (page image). simmel1908soziologie p.93 (German: "keine überindividuelle Kraft"; "durch eine gebrochene verbunden"). On the same page, Small prints "immediate" twice where the German has "die mittelbare", so quote the A–B–C sentence with [sic] or use Wolff 1950: 135.

**P10 (textual).** Simmel made the step from two to three a change of form, in two passages.
- II:165, with its subject kept: "This mediation itself, however, the decisive modification of the configuration from within, occurs only through the addition of the *third* party."
- II:165–66, the full clause: "The tri-unity as such appears to me to produce three sorts of typical group-forms, which on the one hand are not possible with two elements, on the other hand, in case of a number greater than three, are either likewise excluded, or are merely extended quantitatively without changing their form-type."

Two cautions. Small's "only" renders the German "immer schon" ("always already"; 1908 p.102). Quote the whole clause, since dropping "either likewise excluded" makes Simmel claim more than he does.

*Support:* simmel1902number2 p.165, pp.165–66 (page images). simmel1908soziologie p.102 (page image).

**P11 (textual).** Simmel granted that three parties need not make a triad. When the third stands so far from the other two that no reciprocity embraces all three, "We have rather configurations of twos" (Small 1902, II:166). The German is "Zweierkonfigurationen" (1908, p.103); Wolff renders it "Rather, there are configurations of two." (1950, p.145).

*Support:* simmel1902number2 p.166. simmel1908soziologie p.103 (page image). simmel1950sociology p.145 (page image).

**P12 (textual cautions).**
- *The translators' words.* "Dyad" and "triad" are the translators' words. Small already uses both in 1902 (I:44, II:182), so Wolff did not coin them.
- *Form, not logic.* Simmel argues from sociological form. He does not argue logical irreducibility.
- *The p.161 passage.* The "so decisive" passage on p.161 concerns duality, the step from one ally to two, so it cannot warrant 2→3.
- *The proposal's paraphrase.* The line "not an increase in number but a change in kind" in the author's proposal is a paraphrase. It must not appear in quotation marks as Simmel's.

*Support:* simmel1950sociology Notes. simmel1902number2 Notes (C2 correction).

**P13 (lab_result).** The lab's Simmel probes, on Boolean models:
- *Mutual dyad* (A′ = B, B′ = A): a whole at Φ_MIP = 2.000000.
- *Broken-line triad* (A′ = C, B′ = C, C′ = A ∧ B): a whole at Φ_MIP = 2.000000 with all three in the core, although A and B have no direct tie.
- *Cut dyad*: 0.000000.
- *Mutual triad*, with every pair tied: Φ_MIP = 6.000000 with all three in the core.
- *Majority triad*, where every node follows the majority: Φ_MIP = 0.000000 with an empty core.
- *Mutual cliques*: Φ grows by +4, +6, +8 as members are added.

*CI:*
- thinkers-simmel-h1-superindividual: `Φ_MIP=2.000000  core=('A', 'B') coreΦ=2.000` (dyad_mutual); `triad_broken_line      triadic  Φ_MIP=2.000000  core=('A', 'B', 'C') coreΦ=2.000`; `dyad_cut               dyadic   Φ_MIP=0.000000`; `triad_mutual           triadic  Φ_MIP=6.000000  core=('A', 'B', 'C') coreΦ=6.000`.
- thinkers-simmel-h3-majority: `majority_triad         dyadic   Φ_MIP=0.000000  core=() coreΦ=0.000`.
- thinkers-simmel-h2-number: `ΔΦ(2→3) = +4.000000`, `ΔΦ(3→4) = +6.000000`, `ΔΦ(4→5) = +8.000000`.

*Slide rule:* the CI label column (`triadic`, `dyadic`) carries the superseded Φ > 0 sense. Show only the name, Φ_MIP, core and adicity fields.

**P14 (lab fact from source code).** The broken-line triad has exactly the rules of the lab's instrument control (A′ = M, M′ = A ∧ B, B′ = M), with C in the role of M. Simmel's arbitrator has the same rules as well.

*Support:* simmel/forms.py l.30, l.37, l.56. peirce/forms.py l.37. CI thinkers-simmel-h4-nonpartisan: `arbitrator             triadic  Φ_MIP=2.000000  core=('A', 'M', 'B') coreΦ=2.000`.

**C2 (inference from P9–P14).** Simmel's change of form is not the number three, and it is not a larger Φ.
- Three parties are necessary by count, because cause-side adicity 3 needs three elements.
- They are not sufficient: the majority triad does not bind.
- Φ does not single out the step: the mutual dyad and the broken line read the same 2.000000, and Φ over cliques grows smoothly.

What the broken line adds is the control's joint determination: the third is set by both others and acts back on both. The lab's H2 verdict ("2→3 decisive … REFUTED") tests a magnitude reading built on the p.161 misreading. It refutes that rendering, not Simmel, and stays off the slides.

---

## S3. Löwenheim, Kalmár, Quine

**P15 (textual).** Löwenheim reduced the higher relative calculus to the binary one 39 years before Quine. The reduction is §4, "Zurückführung des höheren Relativkalküls auf binären", Satz 6. Every relative equation is equivalent in satisfaction status to a binary one. He built the binary one over a new domain whose elements are pairs of old elements ("Wir betrachten einen neuen Denkbereich, dessen Elemente die Elementenpaare des alten … sind"). For n individuals the new domain has n² elements, so the reduction needs no infinity and no set theory. He cites Schröder, not Peirce.

*Support:* lowenheim1915moglichkeiten pp.463–464 (page images; verified). Register TR-S3-040 (refuted: no infinite embedding is needed).

**P16 (textual).** Kalmár (1936) opens by sharpening "eines Löwenheimschen Satzes", which Herbrand had proved. He cites Löwenheim 1915, "insb. § 4". The line of descent runs Löwenheim → Herbrand → Kalmár → Quine.

*Support:* kalmar1936zurueckfuehrung p.137 and n.1 (scan; verified).

**P17 (textual).** Quine (1954) proves a translation theorem about interpreted theories. It is not a decomposition of relations.
- *The theorem:* any interpreted theory Θ "is translatable into a theory … in which there is only one predicate letter, and it a dyadic one", 'F'.
- *What it assumes:* "a fragment of set theory" guaranteeing {x, y}, and Kuratowski pairs.
- *The universe:* the universe of Θ′ comprises Θ's universe and {x, y} for every x and y in Θ′'s universe. Quine adds "(Of course the universe of Θ may happen already to comprise all this.)", so enlargement is typical, not guaranteed.
- *His frame:* n.1 sets the result beside Kalmár and beside Church, Craig and Quine.
- *Peirce:* Quine does not name him on p.180 or in the notes, and those are the only parts read (pp.181–182 are unread). Koshkin (2022, n.1) reports that Quine never related the result to Peirce. That report is Koshkin's paraphrase and is not a card locus, so it takes no quotation marks.

*Support:* quine1954reduction p.180 and n.1 (publisher transcription; card status corrected). koshkin2022reduction n.1 (arXiv v1 p.21). Register TR-S3-001 and TR-S3-096 (refuted: Quine did not aim the paper at Peirce).

**P18 (textual).** Quine's readers, not Quine, set the result against Peirce. Burch writes that the thesis "was for over a century doubted by many, especially after the publication of a proof by Willard Van Orman Quine that all relations could be constructed exclusively from dyadic ones". Koshkin names Christopherson and Johnstone (1981) as one reader who pressed pairing against the thesis. That card is metadata-only, so the talk can say "by 1981 at the latest" and cannot say "first".

*Support:* burch2021sep §14 (verified). christopherson1981triadicity (metadata-only; content reached through Koshkin 2022 n.1).

**C3 (inference from P15–P17).** Once pairing and domain extension are allowed, every relation reduces to dyads. That refutes the negative clause only in that regime. It says nothing about bonding among the same elements. *Rule:* a theorem's scope is its stated resources.

**C3b (the talk's own argument; no source makes it).** Every definability reduction adds an object that stands for the tuple:
- Kempe's λ (§330);
- Peirce's "this action" (CP 3.424);
- Löwenheim's pair-elements (p.464);
- Quine's {x, y} (p.180).

What they show is expressibility with one dyadic predicate over a larger or pair-closed universe. They do not compose a triad from pairs among the same elements. Peirce had conceded the first and denied the second by 1892 (P5). Koshkin puts the same point in logical terms: "the pairing construction, as formalized in set theory, relies on the very FOL devices that are explicated as using triads" (p.2), and the pair-element "conceals triadicity in the same way as (4)" (p.7, formula 5).

In coordination, the minted object is a third party. The reduction therefore moves the third; it does not remove it.

*Support:* koshkin2022reduction pp.2, 7 (preprint). Do not cite Koshkin p.12 ("it is not the original relation that is reduced but some other … on a larger domain") for pairing, because that sentence concerns hypostatic abstraction on finite domains.

---

## S4. How the thesis fared in modern logic

**P19 (textual).** Herzberger (1981) proved both sides in one chapter.
- T7: "In bonding algebra, lower polyads (n ≤ 3) are absolutely irreducible."
- T8: the thesis holds "within any sufficiently large domain".
- T9: "The reduction thesis holds within any system of valency-regular definitional processes rich enough to permit the formation of relative products."
- T11: the counterargument "holds within standard notions of definability", and so "the reduction thesis collapses under standard notions of definability."

*Support:* herzberger1981theorem T7–T9, T11 (snippet: search-inside, matched across two OCR scans; most page numbers not visible). Cite by theorem number only. Keep Skidmore, whom Herzberger mentions, off the slides; that card is metadata-only.

**P20 (textual).** Burch, the author of PAL, gave the resource-relative verdict: "As it turns out, both Peirce and Quine were correct: the issue entirely depends on exactly what constructive resources are to be allowed to be used in building relations out of other relations." His proof, dated 1988 and published 1991, needed juxtaposition "only allowed as last or before last operation". That wording belongs to Hereth Correia and Pöschel, reporting Burch.

*Support:* burch2021sep §14 (verified). herethcorreia2006teridentity p.2 (preprint). burch1991reduction is metadata-only, so cite Burch through the SEP or through the PAL authors' reports.

**P21 (textual).** Hereth Correia and Pöschel (2006, Thm 2) removed Burch's restriction. For any A with |A| ≥ 2, PAL without teridentity, with negation allowed, does not generate id₃ from all unary and binary relations. No term connects more than two places (Lemma 1: "Then |X| ≤ 2."), and "Therefore the teridentity is not representable in PAL without teridentity."

Hereth and Pöschel (2011) state the strict inclusion "independently from the underlying set A". That phrase attaches to the irreducibility clause only. The constructive clause on infinite domains uses a bijection A × A → A, whose graph is ternary, and the axiom of choice.

*Support:* herethcorreia2006teridentity p.6, pp.21–22 (preprint). hereth2011logic p.6, pp.8–9, p.28 n.2 (preprint).

**P22 (textual).** Relational algebra builds teridentity from binary identity by identifying coordinates: =₃ = ∆(ζ(= × =)). Dau and Hereth Correia (2006) put it this way: "the teridentity would be somehow hidden in the operations from relational algebra."

*Support:* dau2006instances pp.107–108 (published pagination; card status corrected). Author order: Dau, then Hereth Correia.

**P23 (textual).** Koshkin's projoin results carry domain qualifiers, and the talk should keep them.
- On infinite domains every n ≥ 3 relation reduces to a bond of unaries, binaries and teridentities (2024, Thm 14). Every relation reduces to binaries by hypostatic abstraction, through 1-keys, which are equivalent to choice.
- On finite domains every n ≥ 4 relation reduces to ternaries (2025, Thm 2).
- With |D| ≥ 3, every cofinite relation reduces to binary relations (2025, Thm 3, p.13: "we can now reduce any cofinite relation to binary ones as long as |D| ≥ 3").
- On Boolean domains, ¬I₃ is "irreducible to binary relations on Boolean domains" (Thm 4).
- "I3 is bond irreducible on any domain with at least two elements." (Thm 6)

The lab's domain is Boolean. There, pp composition without domain extension does not reduce every ternary.

*Support:* koshkin2024reduction p.14, Thm 14 p.21 (preprint). koshkin2025completeness Thm 2 p.8, Thm 3 p.13, Thm 4 p.14, Thm 6 p.17 (preprint).

**P24 (textual).** Koshkin (2022) rejects the verdict that both were right:

> "It cannot simply be that Peirce and Quine are both right. For Peirce to be right Quine has to be wrong in a deeper conceptual sense, despite being correct in a technical algebraic sense."

He argues that pairing hides a triple junction (pp.2, 7) and concludes: "PRT is not gerrymandered, it is a deep fact about the fine structure of relations that can be neither manufactured nor undone by manipulating algebraic conventions."

*Support:* koshkin2022reduction p.20 (preprint, arXiv v1 pagination; the journal is TCSPS 58(4)). The p.4 sentences are verified verbatim in `/Users/ludwitt/iit-playground/triadic_reduction_local/fulltext/koshkin_2406.14058.txt` l.169–171, but they are **not yet a card locus**. Add them to koshkin2022reduction.md at p.4 before a slide quotes them. Register TR-S3-085. The register's label "Koshkin (2024)" for arXiv 2406.14058 is wrong; that paper is the 2022 one.

**P25 (textual).** Koshkin also points toward information integration, and he does so tentatively. He suggests that the minimum mutual information over bipartitions of a relation's places, the "cruelest cut", would give "a finer measure of how close the relation comes to being degenerate", and he adds: "Such measures of “information integration” are studied in biology (Tegmark, 2016)." Note 18 calls this extensional notion a "tentative means of quantifying it". His 2024 paper leaves an information-theoretic reading of ternarity open (Problem 5).

Tegmark defines his measures on Markov dynamics and rejects one-time mutual information across a cut as an integration measure (p.19). Koshkin names neither IIT's Φ nor any IIT 4.0 quantity. So the talk must not call Φ "the quantity Koshkin pointed to". Φ is at most a causal, dynamical member of that family.

*Support:* koshkin2022reduction pp.14–15, n.18 p.22. koshkin2024reduction p.30. tegmark2016improved p.3, p.5, p.19 (verified). Register TR-S5-470 and TR-S5-558 (refuted: neither IIT nor PID proves Peirce's thesis); TR-S5-164 (corrected).

**P26 (textual).** Today's string-diagram logicians build the branch in. Haydon and Sobociński (2020) show that Peirce's "lines of identity obey the laws of special Frobenius algebras". In Rel_X the copy generator is the diagonal relation {(x, xx)}, and it forms, with its opposite, "the canonical Frobenius structure of RelX" (p.10). Bonchi and colleagues (2024) take the copier as a fundamental constant (p.4). Hereth Correia and Pöschel (2004, p.8) had written that teridentity "just "splits" one edge into three "directions"". In the extensional setting, the copy node and its converse are one structure.

*Support:* haydon2020compositional p.1, p.8, p.10 (preprint). bonchi2024diagrammatic p.4 (preprint). herethcorreia2004power p.8 (preprint).

**C4 (inference from C1, C3, P19–P24, D1).** The formal answer depends on the regime, and the regimes split on the three-way junction.
- *Where a branch counts as a relation* (bonding; PAL without id₃; Koshkin's explication), the negative clause is a theorem.
- *Where a shared variable is free glue* (pp or relational algebra with coordinate identification, on |D| ≥ 3; pairing over a pair-closed universe), triads reduce.
- *On Boolean domains,* pp without extension leaves some ternaries irreducible.

Burch and Koshkin accept the same theorems and disagree about which regime is privileged. *Rule:* case analysis over D1's regimes.

**C5 (inference from P26 and C4).** Definability cannot settle the junction's status. A relation given as a set of tuples has no direction: the same extensional junction is at once copy (one to many) and merge (many to one). A setting where the junction has a direction is needed. *Rule:* a formalism cannot adjudicate a distinction it does not draw.

---

## S5. The lab's move: IIT 4.0 and exact Φ

**P27 (lab_result). The instrument control is a triad by D3.** A′ = M, M′ = A ∧ B, B′ = M. The PASS condition requires Φ_MIP = 2.0, core {A, M, B}, adicity 3, and a maximal distinction that begins "M -> cause AB". The PASS string therefore certifies that M's cause purview is {A, B}: the mediator is jointly determined by both outer parties, and the whole binds all three. The φ of that distinction is not an expect string and must not appear on a slide.

*CI:* thinkers-peirce-h1-irreducibility: `control conjunctive triad: Φ=2.000000 core=('A', 'M', 'B') adicity=3 PASS`. *Code:* peirce/forms.py `run_control` (l.155–159).

**P28 (lab fact). The talk tightens the lab's earlier rule.** The lab's classifier used Φ_MIP > 0 ⟺ triadic ⟺ algorithmacy. So did STRUCTURAL_FINDINGS L5–6 and the essay's Part four. Under that rule the mutual dyad counted as triadic, and CI still prints "dyad_mutual triadic".

The talk says once, plainly: "Our classifier used to call any form with Φ > 0 triadic. By that rule a mutual dyad counted. We now require joint determination as well." Flag concepts.md, STRUCTURAL_FINDINGS L5–6 and L65–70, and literacy_or_algorithmacy.md Part four for revision.

*Support:* concepts.md L37–40. Register TR-S5-174 (caution) and TR-S5-638.

**P29 (lab_result). Composing dyads: the pre-registered test failed.** The lab enumerated every wiring in which each node copies exactly one other node, at n = 3 (2³ = 8) and n = 4 (3⁴ = 81). That is 89 wirings, with no negation and no self-reads.

The pre-registered measure took the larger side's adicity. On it, H1 ("no complexus of dyads reaches adicity 3") came out REFUTED: 66 wirings reach 3 and 12 reach 4. The rendering had left out Peirce's own premise that a node is a relative.

The lab then split cause from effect, post hoc, and found:
- the 11 unbranched wirings stay at adicity ≤ 2, and 8 of them are wholes;
- the 78 branched wirings all reach 3 or more, and none is a whole;
- the maximum cause-side adicity over all 89 is 2.

Every adicity above 2 therefore sits on the effect side, at a branch point where one node is read by two or three others (copy_CCA: cause 2, effect 3; copy_DDDA: cause 2, effect 4).

*CI (thinkers-peirce-h1-irreducibility):*
- `wirings=89  max genuine adicity=4  adicity counts={2: 11, 3: 66, 4: 12}  whole-irreducible (Φ>0)=8`
- `H1 (no complexus of dyads reaches adicity 3): REFUTED`
- `unbranched wirings (pure cycles and their products)=11, max adicity=2, Φ>0 in 8; branched wirings=78, min adicity=3, Φ>0 in 0; max cause-side adicity over all=2`
- `copy_CCA               Φ_MIP=0.000000  core=('A', 'C')             adicity=3 (cause 2, effect 3)`
- `copy_DDDA              Φ_MIP=0.000000  core=('A', 'D')             adicity=4 (cause 2, effect 4)  D -> cause A effect ABC (φ=1.000)`

*Register:* TR-S5-191, TR-S5-196, TR-S5-198 (post hoc; "located", not "resolves"). *Paper:* peirce/paper.md l.220–233, l.331–335.

*Not registered, so keep off slides:*
- "the eight wholes are the pure cycles";
- "all eight at Φ = 2.0";
- "every branched wiring contains a core at coreΦ 2.0" (78/78 in the JSON).

Say instead: "eight of the eleven unbranched wirings are wholes, e.g. copy_BCA at Φ_MIP = 2.000000".

**P30 (logical). Both H1 facts follow from how the family is defined, so they are near-definitional.**
- *The cause-side ceiling.* A one-input rule gives each element one cause. A mechanism whose members read separate single sources falls apart under IIT's disintegrating partition ("cuts the mechanism into at least two independent parts", albantakis2023information p.23). No mechanism, single or compound, then carries an irreducible joint cause over three elements. The registered bound `max cause-side adicity over all=2` covers both readings.
- *Branched wirings are never wholes.* In a one-input family each node is read n times in total. If one node is read twice, some other node is read by none. A node that affects nothing cannot belong to a complex, so cutting its outputs loses nothing and the whole system factors. The branch's three-term fact hangs off a whole (a cycle) rather than lying inside one.

So IIT's partition test reproduces Peirce's arithmetic: without branches the adicity is 2, and with branches it is 3 or more. It adds a direction: every excess sits on the effect side. That makes the 89-wiring panel a calibration of the instrument against Peirce, not evidence for him.

The enumeration covers only n ≤ 4. For larger n the ceiling follows by the same counting, which is an argument and not a computation.

*Support:* peirce1897logic p.183. peirce/forms.py `one_input_wirings`. FINDINGS.md caveat (post hoc split).

**P31 (lab_result). Φ > 0 alone does not mark a triad.** Three forms are wholes at Φ_MIP = 2.000000 with adicity 2 and no party jointly determined:
- the mutual dyad;
- the copy ring;
- Peirce's degenerate giving (G′ = ¬R, T′ = G, R′ = T), a ring.

The imitation of giving gets its wholeness from the return, not from any three-term relation.

*CI:*
- thinkers-simmel-h1-superindividual: `Φ_MIP=2.000000  core=('A', 'B') coreΦ=2.000`.
- thinkers-peirce-h1-irreducibility: `copy_BCA               Φ_MIP=2.000000  core=('A', 'B', 'C')        adicity=2 (cause 2, effect 2)`.
- thinkers-peirce-h3-giving: `giving_degenerate      Φ_MIP=2.000000  core=('G', 'T', 'R')        adicity=2 (cause 2, effect 2)`.

*Register:* TR-S5-012 and TR-S5-381 (lab_contradicted: dyadic forms are not Φ = 0).

**P32 (lab_result). Three-term facts without a whole exist, and every registered case is on the effect side.**
- All 78 branched wirings (P29).
- The sign with an exogenous object (O′ = O, S′ = O, I′ = S↔O) has the three-term fact {O,S} → {S,I}, and it reads Φ_MIP = 0 with the object alone in the core. Nothing reads I, so I affects nothing and forms no distinction of its own. IIT files the reader's joint determination on the effect side of {O, S}. IIT counts a cause-side joint determination only when the determined party acts on something.

The cell "party jointly determined, system factors" has **no registered case**. `two_input_06` (C → cause AD, Φ_MIP 0) appears only in `results/probe_peirce_polyads_n12_s0.json`. The claim that joint determination and wholeness cross in both directions therefore rests on unregistered numbers. The slides say only that the crossing runs one way in the registered results.

*CI:* thinkers-peirce-h4-sign: `sign_exogenous         Φ_MIP=0.000000  core=('O',)                 adicity=3 (cause 2, effect 3)  OS -> cause O effect SI (φ=1.000)`.

**P33 (lab_result). Joint determination in a whole exists, in two motifs.**
- *The control star* (P27). Simmel's broken line and arbitrator have the same rules (P14).
- *Genuine giving* (G′ = ¬R, T′ = ¬R, R′ = G ∧ T). This is the control's graph with negated returns: R ← {G, T} at φ = 2.000, cause 3, core {G, T, R}.
- *The pragmatic sign* (O′ = I, S′ = O, I′ = S↔O). When interpretation acts back on the object, the interpretant is jointly determined by object and sign (I ← {O, S}, cause 3), and the form binds all three.

Counted by motif rather than by name, the base is narrow: the control family and the pragmatic sign.

*CI:*
- thinkers-peirce-h3-giving: `giving_genuine         Φ_MIP=2.000000  core=('G', 'T', 'R')        adicity=3 (cause 3, effect 3)  R -> cause GT effect GT (φ=2.000)`.
- thinkers-peirce-h4-sign: `sign_pragmatic         Φ_MIP=2.000000  core=('O', 'S', 'I')        adicity=3 (cause 3, effect 2)  I -> cause OS effect O (φ=0.500)`.

**P34 (lab_result). The criterion does not exclude direct ties between the humans.** The mutual triad, in which every pair is tied and every party is set by the other two, reads Φ_MIP = 6.000000 with all three in the core. The essay's claim that suppressing the direct channel flips the verdict therefore does not hold under the talk's criterion, and S6 drops it. The mutual triad's single-mechanism cause purviews are not registered. Only its Φ and core are.

*CI:* thinkers-simmel-h1-superindividual: `triad_mutual           triadic  Φ_MIP=6.000000  core=('A', 'B', 'C') coreΦ=6.000`.

**P35-bridge (bridge; argument, not a run). Pairing has two causal renderings, and neither removes the triad.**
1. *A pair-state node P′ = (A, B).* A node set jointly by two inputs is itself a cause-side joint determination. Recovering A and B from it needs a fan-out, so causal pairing uses both kinds of junction that the extensional junction ran together.
2. *Merging two parties into one unit.* This changes who the parties are.

*Support:* register TR-S5-094 note ("A pair-state node p_t determined jointly by X1 and X2 would itself be a joint (adicity-3) mechanism"). TR-S5-012 note ("The lab hasn't modeled Quine's set-theoretic pairing construction"). koshkin2022reduction p.7.

**P36-grain (stipulation, with its defence). In a coordination form the units are the parties.**
- *Defence (the talk's interventionist premise; no card):* a coordination between A and B presupposes that A and B can each act, and be intervened on, separately. A rendering that fuses them into one unit no longer represents that coordination.
- *What IIT 4.0 would say:* IIT picks the grain by maximal φ (exclusion; TR-S5-284, verified). The lab has never run that test on these forms, and concepts.md ("The honest limits", item 2) calls the verdict model-relative to "the state-individuation rule".

**C6 (inference from P29–P33, C5). IIT separates what the logical debate ran together.** The logic had one undirected junction. IIT's directed partition test separates three properties:
- *fan-out*: one element read by many. This is an effect-side three-or-four-term fact, the shape of Peirce's node and of PAL's teridentity-as-branch, and one-input wirings produce it everywhere.
- *fan-in*: one element determined by two. This is cause-side joint determination, and one-input wirings never produce it. Herzberger's valency rule holds there.
- *wholeness*: Φ.

The split is post hoc. It locates the disagreement and does not resolve it (TR-S5-191).

**C7 (inference from C6, P33, P35-bridge, P36-grain).** Take the parties as units and determination as directed dependence. Then one-input determination never yields joint determination, and joint determination inside a whole exists. Pairing, rendered causally, either adds a jointly determined node or merges the parties. This result is a change of question from definability to causal determination. It does not refute Quine. It is also not the static information measure Koshkin pointed to.

**What IIT adds, stated affirmatively (P37, bridge).**
1. *It gives the junction a direction:* fan-out on the effect side, fan-in on the cause side.
2. *One partition principle yields both clauses of D3:* φ over mechanism partitions for the triad, Φ over system partitions for the whole.
3. *The whole clause discriminates,* on registered cases. The exogenous sign and the majority triad are three-party forms that read Φ_MIP = 0.000000, while the mutual triad reads 6.000000.
4. *A branch can sit inside a whole once the branched party is jointly determined.* M is read by both A and B in the control, and R by both G and T in genuine giving.
5. *Calibration:* IIT, built for another purpose, returns Peirce's 2 + 2 − 2 when fed his rendering.

---

## S6. The point: algorithmacy

**P38 (stipulation). The lab's definitions.** The lab defines literacy as a dyadic competency: a person stands on one side of a medium that conveys, scores or interprets but pursues no objective of its own across two different humans. It defines algorithmacy as a triadic competency: a worker coordinates with another human through an algorithmic third party that interprets both sides and commits determinations neither side controls. Its first component is "inferring the hidden other side from observed outcomes".

*Support:* concepts.md L7–17 (the line range is L7–17, not L8–15). Register TR-S6-003 and TR-S6-064 (stipulation). These are lab text, not card loci, so the slides paraphrase them without quotation marks.

**P39 (bridge). Where the structural definitions (D4) depart from the lab's wording.** Take a scoreboard, a vote tally or a posted price. Each is set jointly by both parties, read by both, and pursues no objective of its own. Each has the control's shape. The lab's teleological test ("no objective of its own") and the structural test (input count) therefore come apart. The talk uses the structural test and says so.

**P40 (bridge). Literacy's coordination between two humans is a chain.** The writer fixes the text, the text later informs the reader, and the text is inert while it is read. The lab's Boolean chain (A′ = A, B′ = A, C′ = B) reads Φ_MIP = 0.000000 at adicity 2. This mirrors Peirce's imitation of giving ("merely one dyadic relation followed by another", CP 1.345), but only as an analogy. Peirce never classes reading as degenerate: he makes the sign genuine (P8).

Two variants keep the chain's verdict:
- *A letter exchange* loops the chain into a ring. That makes a whole, but still at adicity 2, like copy_BCA or the mutual dyad. This is the talk's analogy; the lab modelled no correspondence.
- *Broadcast* (one text, many readers) is a branch: the copy_CCA shape, effect-side 3. Peirce would count that node as a relation, but under D3 no party is jointly determined.

*CI:* thinkers-peirce-h2-degeneracy: `dyadic_degenerate      Φ_MIP=0.000000  core=('A',)                 adicity=2 (cause 2, effect 2)`. *Register:* TR-S6-180 and TR-S6-014 (stipulation).

**P41 (bridge). Reading is a triad inside a dyadic coordination.** Every sign is triadic for Peirce (P8), but the sign triad binds a text, its object and one reader's interpretant. During reading, that interpretant determines nothing on the other human's side. The exogenous-sign model shows the structure: a genuine three-term fact in a system that factors, with the reader's joint determination filed on the effect side because nothing reads it (P32). The model illustrates the structure. It is not evidence about Peirce's text (TR-S6-016, corrected), and it carries no "thought or meaning" (CP 1.345).

In this model the object O is not the second human. The model therefore has one human, and literacy as coordination between two humans uses the chain (P40). The two claims stay on separate lines.

**P42 (bridge). The algorithmacy form is the control.** The algorithmic third M is re-determined at each step from both humans (M′ = A ∧ B), and each human reads M. That is the control and Simmel's broken line: Φ = 2.000000, adicity 3, core {A, M, B}. The humans may also talk directly (P34). An active third is necessary but not sufficient, so the verdict is per form, and a platform counts only once its rule is modelled.

*Register:* TR-S6-002 and TR-S6-252 (lab_contradicted: mediation does not entail an irreducible triad).

**P43 (lab_result, a concession). The target is older than AI.** Simmel's arbitrator has the control's rules and reads Φ_MIP = 2.000000 with core {A, M, B} (P14). A human third meets the criterion with no algorithm present. The ontological argument therefore secures a target for triadic coordination as such. That the modern mass instance of that target is algorithmic (opaque, rule-shifting, present in every transaction) is a historical premise. It is not a lab result.

The author's analogy ("Whatever the book was to literacy, AI is to algorithmacy") has to be read at that historical level: the book made literacy a mass competence, and AI makes coordination through a jointly determined third a daily condition. Read at the level of roles, the analogy fails. It would make AI the medium, while the argument makes AI a party, "the mediating third".

**P44 (logical, from the control's rule). Why the form makes a demand.** Under M′ = A ∧ B, A's own state fixes M′ only when A = 0. When A = 1, M′ follows B. A party who acts through M cannot predict M's next determination from her own act and the rule alone; she must infer the unseen other side. That is the first component of algorithmacy (P38). The inference comes from the rule and needs no stipulation.

**P45 (stipulation). The remaining bridge.** Coordinating through M requires anticipating M's determinations. This is much weaker than "competence follows form" (essay l.136), which the register records as the lab's definitional identification (TR-S6-033). The talk states P45 openly as a premise.

**P46 (stipulation). Scope.** The forms are Boolean models of three and four binary elements. They are not people. No worker, platform or rule from the field is measured. Whether a form is triadic is a verdict on that form. It is not an ontological premise about mediation as such.

*Register:* TR-S6-276 and TR-S6-280 (lab_contradicted: "triads as irreducible primitives"). peirce/paper.md l.339–341.

**C8 (from D4, P40–P42).** Literacy forms are compositions of one-input mediations, and algorithmacy forms contain joint determination in a whole.

**C9 (from C8 and C7, by modus ponens on the second horn of D5).** Among fixed parties, the target class of algorithmacy is non-empty (in models) and cannot be composed from literacy's forms. Literacy's forms stay chains and rings, adicity 2 on the cause side, however they are wired or looped. So algorithmacy has a well-defined target kind of its own.

Two limits on this inference:
- It shows that the kind exists as structure and is not composable. Whether any platform instantiates it is a separate, per-form question.
- The Quinean reply does not defeat the first horn in this sense. Pairing either adds a jointly determined node or merges the parties (P35-bridge), and every definability reduction mints a third (C3b). The talk does not claim a modus tollens on the first horn.

**C10 (from C9, P44, P45, P46). Conditional necessity.** Wherever coordination takes this form, the competence it demands is not a composition of competences for one-input mediation. The argument is ontological about the target: the kind exists and cannot be composed from literacy's kind. It is not an argument that triads are primitives, and it does not claim that any worker faces the kind today.

## Conclusion (for the author)

Peirce's thesis, stated in 1870 and argued by valency arithmetic, turns on whether a junction of three lines is itself a relation. Simmel found the same step in social form and saw that three parties can stay "configurations of twos". Löwenheim and Quine showed that every relation can be expressed with one dyadic predicate once pairs are available. Each of their reductions mints the object that stands for the tuple, as Kempe's λ and Peirce's "this action" had done. Herzberger, Burch, Hereth Correia and Pöschel, Dau, and Koshkin showed that the verdict depends on the operations allowed, and the regimes split on an undirected junction.

The lab gives that junction a direction. Fan-out is everywhere in one-input wirings and never makes a whole there. Fan-in is never composed from one-input determinations. Joint determination inside a whole exists. Literacy coordinates by one-input mediation and algorithmacy by joint determination in a whole, so algorithmacy's target exists as a structure that literacy's forms cannot compose. That is the sense in which the argument is ontological. It is shown on Boolean models, and it is conditional on fixing the parties as units.

## Weakest links and how the talk handles each

1. **Grain: "you have moved the gerrymander from operations to units."** Merge two parties into one element and the control's M becomes a one-input element, cause-side adicity 2. The form then looks like the mutual dyad. The causal verdict is as regime-relative as Burch says the logical one is.
   - *Handling:* state C7 conditionally, defend the units by the interventionist premise (P36-grain), and give the pair-node argument (P35-bridge) as an argument, not a result.
   - *Open test:* the decisive next test is IIT 4.0's own exclusion (grain) test run on a paired re-encoding of the control. It has not been run.
   - *Where:* say this aloud on slide 16.
2. **The competence bridge.** "The target is irreducible" does not entail "the skill is distinct".
   - *Handling:* P44 derives the demand from the rule. P45 is stated as the one remaining premise. The talk says "conditional necessity" and never "algorithmacy rests on triads as primitives" (TR-S6-280).
3. **Algorithmic specificity.** Arbitrators, tallies and markets meet the criterion.
   - *Handling:* concede on slide 15 (P43). The target is triadic coordination, and AI's role is a historical premise, the likeliest line of attack in Q&A. Prepared answer: Simmel wrote about the mediator, the arbitrator and the tertius gaudens in 1902; what is new is the third's mass algorithmic instantiation.
4. **Post hoc criterion.** The cause/effect split and the locked criterion both came after the results.
   - *Handling:* show "REFUTED" on slide 13 and explain it.
   - *Confirmatory option:* before October, fix the criterion and run the adicity reader on a family nobody has examined, such as n = 5 one-input wirings (4⁵ = 1,024) or the unrun two-input forms. Register the result.
5. **Narrow positive base.** There are two motifs, and the "both ways" crossing is unregistered.
   - *Handling:* count motifs on the slide.
   - *Registration options:* register the single-mechanism cause purviews of majority_triad (a candidate for "jointly determined, yet no whole"), triad_mutual, mediator and two_input_08, plus the two_input_06 line.
6. **Reading is triadic.**
   - *Handling:* P41. The triad lives in the reader and the coordination runs in a chain. The talk never says literacy is degenerate "in Peirce's sense".
7. **Scope.**
   - *Handling:* say once, "Boolean models, not people".

## Pre-build actions (the deck checker `talk/check_talk.py` enforces the first two)

- Add Koshkin 2022 p.4 ("It cannot simply be that Peirce and Quine are both right. For Peirce to be right Quine has to be wrong in a deeper conceptual sense, despite being correct in a technical algebraic sense.") as a locus on koshkin2022reduction.md. I verified both sentences against the arXiv v1 text layer, l.169–171. Without the locus, slide 10 fails the quotation check. The fallback is p.20.
- Declare every numeral on slides and in the script in `talk/NUMBERS.md`: lab results with check and expect, and years and loci as plain rows.
- Do not quote lab text (concepts.md, the essay, the proposal) inside quotation marks on slides or in the script. The checker admits only card loci.
- Before CP 1.473 appears anywhere, recheck it on the vol.1 page image. Before the three act-relations of CP 3.424 appear, add them to peirce1892critic.
- Read Quine pp.181–182 if possible.
