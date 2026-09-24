# Prepared questions and answers

Seeded by a red-team pass over ARGUMENT.md: for every premise and for the conclusion, the strongest objection an expert would raise, and an honest answer of under a minute with its evidence. Rows marked **backup** need a backup slide. These are working answers for the author to rewrite in the author's own voice, not a script.

## Q1. Your four regimes are a taxonomy you built so Peirce wins somewhere. Logicians settled on standard first-order definability long ago, and there triads reduce.

*Target:* D1 (composition regimes)

I didn't build it. Herzberger proved both sides in one 1981 chapter: the thesis holds for valency-regular processes (T9) and collapses under standard definability (T11). Burch, PAL's author, says the issue 'entirely depends on exactly what constructive resources are to be allowed'. I pick no winner among regimes. I claim only that they split at the three-way junction.

*Evidence:* herzberger1981theorem T9, T11 (snippet; cite by theorem number only). burch2021sep §14 (verified verbatim).

## Q2. A Peircean dyadic relation is a static set of pairs, not a Boolean transition rule. You've changed the object of study and kept its name.

*Target:* D2 (the lab's rendering: dyad = one-input rule)  **backup**

I changed it on purpose, and I say so. As a set of pairs, a relation has no direction, which is exactly why definability can't settle the junction. A one-input rule is the causal counterpart: B's next state answers to A alone. I call the result a change of question, from definability to causal determination, not a verdict on Peirce's logic.

*Evidence:* ARGUMENT C5, C7. peirce/forms.py genuine_adicity l.101–135. Register TR-S5-191 ('located', not 'resolves').

## Q3. You fixed the criterion today, after the probes ran. That's drawing the target around the arrows.

*Target:* D3 (triad criterion, locked 2026-09-24)  **backup**

Yes, the criterion came after the results, and I disclose it. The pre-registered H1 came out REFUTED, and that word is on slide 13. The criterion tightens our old Φ > 0 rule, which counted a mutual dyad as triadic. The honest remedy is a confirmatory run: fix the criterion, apply it to a one-input family nobody has examined, and register the result before October.

*Evidence:* README 'Triad criterion (fixed 2026-09-24)'. CI thinkers-peirce-h1-irreducibility: 'H1 (no complexus of dyads reaches adicity 3): REFUTED'. CI thinkers-simmel-h1-superindividual: 'dyad_mutual ... Φ_MIP=2.000000  core=('A', 'B') coreΦ=2.000'.

## Q4. Cause-side adicity 3 also counts a two-element mechanism with a one-element purview, like two copies read backward. And 'whole' is ambiguous: your own two_input_00 has system Φ > 0 but a two-element core.

*Target:* D3 (operational form: 'whole' and 'cause-side 3')

Both points are right, which is why the operational form asks for more: one party as mechanism, two others in its irreducible cause purview, and all three in the major complex. That rules out the backward copies and settles 'whole' as the core. Every registered exemplar passes either way, because in each one the core equals the whole system.

*Evidence:* CI thinkers-peirce-h5-polyads: 'two_input_00           Φ_MIP=0.830075  core=('B', 'C') ...'. CI thinkers-simmel-h4-nonpartisan: 'mediator_eliminated    dyadic   Φ_MIP=0.000000  core=('A', 'B') coreΦ=2.000'.

## Q5. Your lab defines literacy teleologically: a medium with no objective of its own. Now you define it by input count. You've redefined literacy until the result falls out.

*Target:* D4 (structural definitions of literacy and algorithmacy)

The two definitions part company at one point, and I name it. A scoreboard, a vote tally or a posted price has no objective of its own, but both parties set it and both read it: the control's shape. The teleological test calls that literacy; the structural test calls it algorithmacy. I use the structural test because it is the one a model can check.

*Evidence:* ARGUMENT P39. concepts.md L7–17 (paraphrase only; lab text takes no quotation marks).

## Q6. You rewrote the conditional. In Quine's sense triads reduce, so by your own first horn algorithmacy is pointless.

*Target:* D5 (the author's conditional, restated)

In the Peirce–Quine sense, both horns fire: triads reduce under pairing and don't under bonding. A dilemma that fires both ways settles nothing, so I have to fix 'reduce'. I fix it as causal composition among the same parties, and I defend that choice by what coordination is: two parties who can each act, and be acted on, separately.

*Evidence:* ARGUMENT C3, C4, P36-grain. quine1954reduction p.180; herethcorreia2006teridentity Thm 2.

## Q7. The 1870 sentence is bare assertion. Peirce admits he studied it 'but little'. Why call that the origin of a thesis?

*Target:* P1 (1870 origin)

It is the origin of the claim, not of the argument, and I quote his concession on the slide myself. The argument arrives later, as valency arithmetic in CP 1.363 and the 1897 Monist. The date matters because much of the secondary literature starts the story in 1897, and the page image shows both clauses already in one 1870 sentence.

*Evidence:* peirce1870description p.374 = CP 3.144 (page image); p.317 'Communicated January 26, 1870.' Register TR-S1-067 (corrected).

## Q8. μ+ν−2λ is a fact about Peirce's graph notation, not about relations. You've mistaken bookkeeping for metaphysics.

*Target:* P2 (valency arithmetic)

Agreed that it is conditional, and S1 presents it that way. The arithmetic holds only if bonds join two places and a three-way junction counts as a relation. Peirce knew the second premise needed defending and defended it three times, in 1897, 1903 and 1904. I present the negative clause as a theorem conditional on that premise, not as metaphysics.

*Evidence:* peirce1897logic p.183 and pp.170–171 ('every node of bonds is equivalent to a relative'). peirce1931papers CP 1.346. peirce1904letter CP 8.331.

## Q9. A graph of maximum degree 2 is a union of paths and cycles. Every undergraduate knows it. Why is this interesting?

*Target:* P3 (parity: dyads make only paths and cycles)

Because nobody disputes it. With the arithmetic beyond dispute, the whole quarrel moves to one premise: is a degree-3 vertex a relation or free wiring? Hereth Correia and Pöschel state the same bound, every vertex of valency at most 2. The triviality is what makes the junction the only thing left to argue about.

*Evidence:* herethcorreia2004power Remark 14 p.12 (preprint). herzberger1981theorem valency rule. Register TR-S1-007, TR-S1-028 (verified as graph theory).

## Q10. Teridentity is just identity. Peirce's 'node is a relative' is special pleading, and he anticipated the objection himself.

*Target:* P4 (a node is a relative)

He did anticipate it, and I quote both sentences so the negation survives: 'You may think that a node connecting three lines of identity Y is not a triadic idea. But analysis will show that it is so.' I don't settle that dispute in logic. I argue that the extensional junction is ambiguous between copy and merge, and the lab splits the two.

*Evidence:* peirce1931papers CP 1.346, vol.1 p.176 (page image). haydon2020compositional p.10.

## Q11. You're tidying 1892. Peirce says Kempe's analysis 'causes me somewhat to modify my position'. That's a retreat, not your neat split.

*Target:* P5 (Kempe exchange: expressibility conceded, composition denied)

He modified his position 'but not to surrender it'. He conceded that Kempe shows his algebra adequate to expressing that A gives B to C, got 'by adding to the universe of concrete things the abstraction 'this action.''. He denied that the diagram represents how that abstraction is derived. The split into expressibility and composition is my gloss, and I label it as mine.

*Evidence:* peirce1892critic CP 3.423–424 (verified). kempe1886memoir §330 p.57 (page image). Keep the three act-relations of CP 3.424 off until carded.

## Q12. The '[my]' in CP 8.331 is an editorial insertion. You may be pinning a criticism of Schröder on Peirce himself.

*Target:* P6 (1904: 'the very triadic relations which it does not recognize')

Fair. CP's editors print '[my]', while Hardwick and Wiener print 'that algebra'. My point doesn't depend on whose algebra it is. It rests on the next sentence: 'every combination of relatives to make a new relative is a triadic relation irreducible to dyadic relations.' The combining step itself is the junction.

*Evidence:* peirce1904letter CP 8.331 (transcription: CP 8 scan, Hardwick, Wiener). Register TR-S1-009 (corrected).

## Q13. Genuine giving is triadic because of Law, Peirce's Thirdness as habit and institution. Your Boolean 'genuine giving' has no law in it, so it models nothing Peirce meant.

*Target:* P7 (giving as the type case)

Agreed: Peirce's giving runs 'according to Law', and a Boolean rule is no law. What the model captures is the structural mark Peirce also names: the three 'welded into one fact' versus 'merely one dyadic relation followed by another'. The model shows that the structural difference is detectable. It does not show that the difference is law.

*Evidence:* peirce1904letter CP 8.331. peirce1890guess CP 1.363. peirce1931papers CP 1.345. CI thinkers-peirce-h3-giving: giving_genuine adicity=3 (cause 3, effect 3); giving_degenerate adicity=2 (cause 2, effect 2).

## Q14. Peirce's sign is triadic, so reading is triadic, so literacy is triadic. Your literacy/algorithmacy line collapses on Peirce's own semiotics.

*Target:* P8 / P41 (the sign is genuinely triadic)  **backup**

Granted: every sign is triadic, bound 'in a way that does not consist in any complexus of dyadic relations'. But that triad binds a text, its object and one reader's interpretant. Literacy between two humans runs writer, text, reader, and while I read, my interpretant determines nothing on your side. The triad lives in the reader. The coordination is a chain.

*Evidence:* peirce1931papers CP 2.274 and CP 5.484 (page images). CI thinkers-peirce-h2-degeneracy: 'dyadic_degenerate      Φ_MIP=0.000000  core=('A',)  adicity=2 (cause 2, effect 2)'. CI thinkers-peirce-h4-sign: sign_exogenous Φ_MIP=0.000000. Register TR-S1-062.

## Q15. Small's 1902 translation is unreliable. You're building on an English Simmel.

*Target:* P9 (Simmel: superindividual energy, the broken line)

Small is unreliable in places. On this very page he prints 'immediate' twice where the German has 'die mittelbare'. I quote only two sentences, both checked against the 1908 German: 'keine überindividuelle Kraft' and 'durch eine gebrochene verbunden'. For anything longer I'd use Wolff 1950.

*Evidence:* simmel1902number1 p.45 (page image). simmel1908soziologie p.93.

## Q16. Small's 'only through the addition of the third' renders 'immer schon'. Simmel never claimed that three is a threshold.

*Target:* P10 (the step to three changes the form)

Right: 'only' is Small's word. I rest on the full II:165–66 clause, which includes 'are either likewise excluded, or are merely extended quantitatively'. That is a claim about form, not about a number threshold. The lab agrees that magnitude doesn't single out three: Φ over cliques grows by +4, +6, +8.

*Evidence:* simmel1902number2 pp.165–66; simmel1908soziologie p.102. CI thinkers-simmel-h2-number: 'ΔΦ(2→3) = +4.000000', 'ΔΦ(3→4) = +6.000000', 'ΔΦ(4→5) = +8.000000'.

## Q17. Simmel himself says a distant third yields only 'configurations of twos'. By your own source, three parties don't make a triad.

*Target:* P11 (Simmel's distant third)  **backup**

Exactly, and I put it on slide 7. Three parties are necessary, not sufficient. Our majority triad has three parties and binds nothing: Φ_MIP = 0.000000, empty core. What makes the triad is a third set by both others that acts back on both. Simmel's broken line has exactly the control's rules and binds all three.

*Evidence:* simmel1902number2 p.166; simmel1908soziologie p.103 ('Zweierkonfigurationen'). CI thinkers-simmel-h3-majority: 'majority_triad ... Φ_MIP=0.000000  core=() coreΦ=0.000'. CI thinkers-simmel-h1: 'triad_broken_line ... Φ_MIP=2.000000  core=('A', 'B', 'C')'.

## Q18. 'Dyad' and 'triad' are American sociology's words. Simmel wasn't doing Peirce's logic, so pairing them is a pun.

*Target:* P12 (translators' words; form, not logic)

They are translators' words, though Small, not Wolff, already used both in 1902. And Simmel argues from social form, not logic. I don't make him a logician. I use him for the social shape of the step and for his own caveat, the distant third. The link to Peirce is structural, and the lab shows it: the same rule set.

*Evidence:* simmel1950sociology Notes; simmel1902number1 I:44, simmel1902number2 II:182. ARGUMENT P14.

## Q19. The mutual triad reads 6, the dyad 2. You're smuggling magnitude back in as 'more triadic'.

*Target:* P13 (Simmel probes: 2.0 vs 6.0)

No. The lab withdrew graded Φ claims. The mutual dyad and the broken-line triad both read Φ_MIP = 2.000000, so magnitude cannot mark the triad. I use Φ only for the whole clause: does the system factor or not.

*Evidence:* CI thinkers-simmel-h1-superindividual: dyad_mutual and triad_broken_line both 'Φ_MIP=2.000000'. concepts.md 'The honest limits' item 1 (binary, not graded; paraphrase).

## Q20. Your 'Simmel broken line' is just your control renamed. You picked AND and dressed it in Simmel.

*Target:* P14 (broken line = control = arbitrator)

It is the control, and I say so. AND is our choice, since Simmel specifies no rule, and it is the simplest one in which the third answers to both. The convergence is a coincidence of coding, so I claim no support from it. What matters is the structure Simmel describes: a second route between each pair through a third.

*Evidence:* simmel/forms.py l.30, l.37, l.56; peirce/forms.py l.37. CI thinkers-simmel-h4-nonpartisan: 'arbitrator ... Φ_MIP=2.000000  core=('A', 'M', 'B')'.

## Q21. Your own CI prints 'H2 ... REFUTED' against Simmel. You're hiding a failed prediction.

*Target:* C2 (H2 'REFUTED')

H2 tested a magnitude reading built on the p.161 passage, which concerns duality, the step from one ally to two, not two to three. It refutes our rendering, not Simmel. Putting a REFUTED on the slide that Simmel never earned would mislead. I'll show it on request.

*Evidence:* CI thinkers-simmel-h2-number: 'H2 (2→3 is the decisive step; increments diminish): REFUTED'. simmel1902number2 Notes (C2 correction on p.161).

## Q22. Löwenheim proved a result about satisfiability of relative equations. You're conflating it with decomposing relations.

*Target:* P15 (Löwenheim 1915)

Satz 6 is equivalence in satisfaction status, which is why I say 'coded' and never 'decomposed'. The mechanism is my point: a new domain whose elements are the pairs of old elements. For n individuals that is n² elements, with no infinity and no set theory. The minted object is right there in 1915.

*Evidence:* lowenheim1915moglichkeiten §4 Satz 6, pp.463–464 (page images). Register TR-S3-040 (refuted: no infinite embedding needed).

## Q23. Herbrand proved Löwenheim's theorem. Why route the lineage through Kalmár?

*Target:* P16 (Kalmár lineage)

Because Kalmár opens by sharpening 'eines Löwenheimschen Satzes', credits Herbrand's proof, and cites Löwenheim 1915 'insb. § 4'. Quine's footnote then cites Kalmár. The chain Löwenheim, Herbrand, Kalmár, Quine is on the pages.

*Evidence:* kalmar1936zurueckfuehrung p.137 and n.1 (verified). quine1954reduction n.1.

## Q24. Quine's reduction is a theorem. Irreducibility is just a restriction on operations: gerrymandering.

*Target:* P17 (Quine 1954)  **backup**

Quine's theorem is correct, and I don't contest it. It assumes 'a fragment of set theory' and a pair-closed universe. Irreducibility is equally a theorem, under two-place bonds. Each result restricts something. Koshkin argues that the invariant version is 'a deep fact about the fine structure of relations'. I take a different exit: causal determination among fixed parties.

*Evidence:* quine1954reduction p.180 (publisher transcription). herethcorreia2006teridentity Thm 2. koshkin2022reduction p.20. burch2021sep §14.

## Q25. Quine never aimed at Peirce. You're staging a debate that never happened.

*Target:* P18 (Quine's readers set him against Peirce)

Agreed. Quine doesn't name Peirce on p.180 or in the notes, the parts I've read. The debate is real in the reception. Burch writes that the thesis was 'doubted by many, especially after the publication of a proof by Willard Van Orman Quine'. Christopherson and Johnstone pressed it by 1981 at the latest.

*Evidence:* quine1954reduction p.180, n.1 (pp.181–182 unread). burch2021sep §14. christopherson1981triadicity (metadata-only; via Koshkin 2022 n.1). Register TR-S3-096 (refuted).

## Q26. A pair-closed universe is the standard mathematical universe. Your bonding regime is the exotic one.

*Target:* C3 (a theorem's scope is its stated resources)

In mathematics, yes. In coordination, no. The parties are fixed, and you cannot add an entity that stands for the pair of two workers without adding someone. Pairing is harmless in set theory and substantive in a coordination form. That asymmetry, not a preference for bonding, is why I restrict the question.

*Evidence:* quine1954reduction p.180 (the universe comprises {x, y}). ARGUMENT C3b, P36-grain.

## Q27. Cute, but vacuous. A set {x, y} isn't a party, and sets aren't agents.

*Target:* C3b (every reduction mints a third)  **backup**

Sets aren't agents. My claim is smaller, and it is mine, not a source's. Render pairing causally and the pair-node is set jointly by A and B: a cause-side joint determination. Recovering A and B from it needs a fan-out. So causal pairing uses both junctions. Koshkin makes the logical version: the pair-element 'conceals triadicity'.

*Evidence:* koshkin2022reduction p.2, p.7 (formula 5). Register TR-S5-094 note (pair-state node is itself an adicity-3 mechanism). Label slide 9 as the talk's argument.

## Q28. You're quoting Herzberger from search snippets with no page numbers.

*Target:* P19 (Herzberger 1981)

Correct: snippet status, matched across two OCR scans. So I cite by theorem number only, T7 to T9 and T11, and quote only phrases visible in both scans. If anyone here has the volume, I'd be glad of the pages.

*Evidence:* herzberger1981theorem card (snippet; page numbers mostly not visible).

## Q29. Burch's own 1991 proof needed a restriction on juxtaposition. That's the gerrymander.

*Target:* P20 (Burch's resource-relative verdict)

Koshkin says as much: 'the shadow of gerrymander still looms over it.' Hereth Correia and Pöschel removed the restriction in 2006. I cite Burch only through the SEP and the PAL authors' reports, because I haven't read the book.

*Evidence:* koshkin2022reduction p.8. herethcorreia2006teridentity p.2. burch1991reduction metadata-only.

## Q30. 'PAL without teridentity' is a regime designed to make id₃ irreducible. Of course it can't build it.

*Target:* P21 (PAL without teridentity)

It is the regime in which every bond joins exactly two places, Peirce's own convention. The theorem shows that the convention does the work, and that is my point: the verdict turns on the junction. One caution: Hereth and Pöschel's domain-independence covers irreducibility only. Their constructive clause uses a bijection A×A→A and choice.

*Evidence:* herethcorreia2006teridentity Thm 2, Lemma 1, pp.21–22. hereth2011logic p.6, pp.8–9, p.28 n.2.

## Q31. Relational algebra gets teridentity from binary identity. So teridentity is reducible, full stop.

*Target:* P22 (relational algebra builds teridentity)

Only by identifying coordinates. Dau and Hereth Correia say it directly: 'the teridentity would be somehow hidden in the operations from relational algebra.' The pattern repeats. The reduction doesn't remove the junction; it moves the junction into the machinery.

*Evidence:* dau2006instances pp.107–108 (published pagination).

## Q32. Koshkin 2025: on |D| ≥ 3, pp composition reduces ternaries to binaries. Your Boolean models sit in the one degenerate case where it fails.

*Target:* P23 (Koshkin's domain qualifiers)

True, and I flag it. Our models are Boolean, where ¬I₃ is 'irreducible to binary relations on Boolean domains'. I don't rest the argument on that. The causal claim is about one-input rules, and a one-input rule gives each element one cause whatever the alphabet. We have computed only binary alphabets, though.

*Evidence:* koshkin2025completeness Thm 3 p.13, Thm 4 p.14, Thm 6 p.17 (preprint).

## Q33. Koshkin already settled it: PRT isn't gerrymandered. What does IIT add?

*Target:* P24 (Koshkin vs Burch)  **backup**

Koshkin's invariant version explicates branch points as teridentities, so his explication counts a junction as a triad. Burch reads the same theorems the other way. Both accept the theorems and disagree over which regime is privileged. Neither framework gives the junction a direction, and that is what IIT adds.

*Evidence:* koshkin2022reduction p.2, p.20. burch2021sep §14. Caution: the p.4 'It cannot simply be...' sentences are not yet a card locus; add them before slide 10 quotes them, otherwise use p.20.

## Q34. Koshkin proposed information integration and called it tentative. You're just running his suggestion and calling it your move.

*Target:* P25 (Koshkin's information-integration pointer)

He pointed at the minimum mutual information across bipartitions of a relation's places, a static measure, and cited Tegmark. Tegmark defines his measures on Markov dynamics and rejects one-time mutual information across a cut. Koshkin never names IIT. So I don't claim to implement Koshkin. Φ is at most a causal member of the family he gestured at.

*Evidence:* koshkin2022reduction pp.14–15, n.18 p.22. tegmark2016improved p.3, p.19. Register TR-S5-164 (corrected), TR-S5-470 (refuted).

## Q35. Relational algebra has converse, and string diagrams have separate copy and merge generators. The direction is already there. 'A formalism cannot adjudicate a distinction it does not draw' is convenient.

*Target:* P26 / C5 (the junction has no direction)

String diagrams draw it syntactically, but in Rel the copier and its opposite together form 'the canonical Frobenius structure'. The same set of tuples reads as copy one way and merge the other. The definability debate ran on tuples. A transition rule has a direction: M′ = A ∧ B is fan-in, and A′ = M with B′ = M is fan-out.

*Evidence:* haydon2020compositional p.10. bonchi2024diagrammatic p.4. herethcorreia2004power p.8.

## Q36. Φ is a consciousness measure. IIT's zeroth axiom is the existence of experience, and critics call IIT pseudoscience. Why use it for coordination?

*Target:* P27 / D2 (why Φ at all)

IIT built Φ for consciousness, and I leave that claim at the door. I borrow the partition test, which is mathematically well-defined whatever you think of experience. I need it because one principle gives both clauses: φ over mechanism partitions for the triad, Φ over system partitions for the whole. No platform here is conscious.

*Evidence:* albantakis2023information p.3 (zeroth axiom), p.5, p.23. tegmark2016improved p.3 ('focused only on integration, not on consciousness'). essays/literacy_or_algorithmacy.md (borrowing for formal content; paraphrase only).

## Q37. M′ = A ∧ B was chosen to make adicity 3. The PASS is circular.

*Target:* P27 (the control passes)

The control is a control: it exists to check that the instrument recognizes joint determination when we build it in. The PASS condition requires M's cause purview to be {A, B} and all three in the core. It is not evidence that triads exist in the world. It is evidence that the reader reads correctly.

*Evidence:* CI thinkers-peirce-h1-irreducibility: 'control conjunctive triad: Φ=2.000000 core=('A', 'M', 'B') adicity=3 PASS'. peirce/forms.py run_control l.155–159.

## Q38. You changed your classifier. Your published lab claims that Φ > 0 means triadic are now wrong.

*Target:* P28 (tightening the classifier)

Some are, and I say so on slide 12. The classifier called any Φ > 0 form triadic, which counted a mutual dyad. We've flagged the concept map, the structural findings and the essay for revision. The CI still prints the old labels, so I show only names and numbers.

*Evidence:* concepts.md L37–40. CI thinkers-simmel-h1: 'dyad_mutual            triadic  Φ_MIP=2.000000'. Register TR-S5-174, TR-S5-638.

## Q39. Your pre-registered prediction failed, and then you invented a cause/effect split to rescue Peirce.

*Target:* P29 (89 wirings, pre-registered H1 REFUTED)  **backup**

The pre-registered measure came out REFUTED, and the slide says so. The split came afterward. It doesn't rescue Peirce. It locates where the excess adicity sits: always on the effect side, at branch points. The branches reached 3 because our rendering left out Peirce's own premise that a node is a relative. Our register says 'located', never 'resolves'.

*Evidence:* CI thinkers-peirce-h1: 'wirings=89 ... adicity counts={2: 11, 3: 66, 4: 12}'; 'H1 ... REFUTED'; '... max cause-side adicity over all=2'. Register TR-S5-191, -196, -198.

## Q40. The cause-side ceiling is true by construction. A one-input rule has one cause, so of course nothing is jointly determined. You discovered your definition.

*Target:* P30 (cause-side ceiling)  **backup**

Yes, and I say it is close to definitional. That's why I call the 89-wiring panel a calibration, not a discovery. Fed Peirce's rendering, IIT's partition test returns his arithmetic, 2 + 2 − 2, and adds a direction. The non-trivial results lie elsewhere: joint determination inside a whole exists, and a whole's clause rejects three-party forms.

*Evidence:* CI thinkers-peirce-h1: 'max cause-side adicity over all=2'; 'branched wirings=78, min adicity=3, Φ>0 in 0'. albantakis2023information p.23 (disintegrating partition). peirce1897logic p.183.

## Q41. 'Branched wirings are never wholes' is also forced, and you only enumerated up to four nodes.

*Target:* P30 (branched never wholes; n ≤ 4)

Both true. In a one-input family each node is read n times in total, so a branch leaves some node unread, and a node that affects nothing can't be in a complex. The enumeration stops at four nodes. The same counting extends further, but that is an argument, not a computation.

*Evidence:* CI thinkers-peirce-h1: 'branched wirings=78, min adicity=3, Φ>0 in 0'. peirce/forms.py one_input_wirings. FINDINGS.md caveat.

## Q42. A ring of copies is Φ = 2. So why isn't a chain of letters, a correspondence, algorithmacy?

*Target:* P31 (Φ alone is not the test)  **backup**

Because wholeness is only half the test. The copy ring reads Φ_MIP = 2.000000 at adicity 2: a whole in which no party is set by two others. A letter exchange loops a chain into a ring, so at most it is that, a whole of one-input handoffs. We haven't modelled correspondence. Algorithmacy needs a third set by both parties, inside the whole.

*Evidence:* CI thinkers-peirce-h1: 'copy_BCA               Φ_MIP=2.000000  core=('A', 'B', 'C')        adicity=2 (cause 2, effect 2)'. CI thinkers-peirce-h3: giving_degenerate Φ_MIP=2.000000 adicity=2. Register TR-S5-012, TR-S5-381.

## Q43. In your exogenous sign, the interpretant is jointly determined by object and sign, yet Φ = 0. Your criterion misses Peirce's paradigm triad.

*Target:* P32 (three-term facts without a whole)  **backup**

IIT files the reader's joint determination on the effect side of {O, S}, because nothing reads I, and a party that affects nothing can't be a cause-side mechanism. Once interpretation acts back on the object, as in the pragmatic sign, I is jointly determined by O and S and the form binds all three.

*Evidence:* CI thinkers-peirce-h4-sign: 'sign_exogenous ... Φ_MIP=0.000000  core=('O',) ... OS -> cause O effect SI'; 'sign_pragmatic ... Φ_MIP=2.000000  core=('O', 'S', 'I') ... I -> cause OS effect O'. Concede: no registered case of 'jointly determined, system factors'.

## Q44. Two motifs. That's an anecdote, not an evidential base.

*Target:* P33 (joint determination in a whole exists)

Two motifs, and I count them on the slide: the control family and the pragmatic sign. The ontological claim needs only existence: one registered form with joint determination inside a whole. Breadth is the next job. We've listed which cause purviews to register next: the majority triad, the mutual triad, the mediator, and a two-input form.

*Evidence:* CI thinkers-peirce-h3: 'giving_genuine ... adicity=3 (cause 3, effect 3)  R -> cause GT effect GT (φ=2.000)'. CI thinkers-peirce-h4: sign_pragmatic line.

## Q45. If the two humans can also talk directly, the third isn't mediating anything. Your criterion is incoherent about mediation.

*Target:* P34 (direct ties allowed)

The criterion doesn't need the direct channel cut. The mutual triad ties every pair and reads Φ_MIP = 6.000000 with all three in the core. Our essay once claimed that suppressing the direct channel flips the verdict. Under this criterion it doesn't, so I've dropped that claim. Only the triad's Φ and core are registered, not its cause purviews.

*Evidence:* CI thinkers-simmel-h1: 'triad_mutual           triadic  Φ_MIP=6.000000  core=('A', 'B', 'C') coreΦ=6.000'.

## Q46. Quine's pair-element isn't a causal node at all. Your 'causal pairing' is a straw man.

*Target:* P35-bridge (causal renderings of pairing)

Then tell me the rendering. If the new node reads A and B, it is jointly determined: the first case. If it reads one pre-paired variable, A and B were already merged into one unit: the second. Among fixed parties I see no third option. This is an argument, and the lab hasn't modelled Quine's construction.

*Evidence:* Register TR-S5-094 note; TR-S5-012 note ('The lab hasn't modeled Quine's set-theoretic pairing construction'). koshkin2022reduction p.7.

## Q47. You've moved the gerrymander from operations to units. Fuse A and B into one element and your control's M is a one-input copy: a mutual dyad.

*Target:* P36-grain (parties are the units)  **backup**

That is the strongest objection. My defence is interventionist: coordination presupposes that each party can act, and be intervened on, separately, and fusing them erases that. IIT has its own test, where exclusion picks the grain that maximizes φ, and we haven't run it on a paired re-encoding of the control. That is the open, decisive test.

*Evidence:* albantakis2023information p.18–19; register TR-S5-284 (verified). concepts.md 'The honest limits' item 2 (model-relative; paraphrase).

## Q48. Logicians didn't 'run together' fan-in and fan-out. Category theorists have separate copy and merge generators.

*Target:* C6 (IIT separates fan-out, fan-in, wholeness)

Fair. String diagrams distinguish copier and cocopier syntactically. My claim is narrower: the definability debate, run on relations as sets of tuples, treated the junction as one undirected thing. IIT separates what that debate ran together. It doesn't separate what logicians can't tell apart.

*Evidence:* bonchi2024diagrammatic p.4. haydon2020compositional p.10. Register TR-S5-191.

## Q49. So you changed the subject from definability to causation. That says nothing about Peirce versus Quine.

*Target:* C7 (change of question)

It doesn't refute Quine, and I say so. It answers the question the talk needs: can coordination among fixed parties that requires a jointly determined third be rebuilt from one-input mediation? That is the only sense of 'reduce' in which algorithmacy's target is at stake, and it is causal.

*Evidence:* ARGUMENT C7, D5.

## Q50. Any parent count gives 2 + 2 − 2. IIT adds nothing a graph count doesn't.

*Target:* P37 (what IIT adds; calibration)

A parent count gets the cause side. It doesn't get the whole clause. The majority triad and the exogenous sign both have nodes that read two parties, and both read Φ_MIP = 0.000000. A count would call them triads. IIT also puts the branch's excess on the effect side, and it derives both clauses from one partition principle.

*Evidence:* CI thinkers-simmel-h3: majority_triad Φ_MIP=0.000000 core=(). CI thinkers-peirce-h4: sign_exogenous Φ_MIP=0.000000. CI thinkers-simmel-h1: triad_mutual Φ_MIP=6.000000.

## Q51. Your definitions are stipulations. You can't extract an ontological result from stipulated definitions.

*Target:* P38 (the lab's definitions are stipulated)

The definitions stipulate what each competence targets. The results aren't stipulated. Whether joint determination can sit inside a whole, and whether one-input mediation can compose it, are checked on models. The link from target to competence is the one premise I state openly as a premise.

*Evidence:* concepts.md L7–17 (paraphrase). Register TR-S6-003, TR-S6-064, TR-S6-033 (stipulation).

## Q52. By your structural test, a vote tally is algorithmacy. Then algorithmacy is everywhere and trivial.

*Target:* P39 (scoreboard, tally, posted price)

On the structural test, a tally both parties set and both read has the control's shape, and I accept that cost rather than hide it. It follows that the target is triadic coordination as such, which is older than AI. What changes with AI is scale, opacity and a rule that shifts.

*Evidence:* ARGUMENT P39, P43. CI thinkers-simmel-h4: arbitrator Φ_MIP=2.000000 core=('A', 'M', 'B').

## Q53. The writer anticipates the reader, and readers write back. Literacy lives in an interpretive community. It isn't a chain.

*Target:* P40 (literacy's coordination is a chain)  **backup**

Anticipation sits in the writer's head, not in the medium: the text doesn't change while it is read. Our chain reads Φ_MIP = 0.000000 at adicity 2. A reply loops the chain into a ring: a whole, still adicity 2. Broadcast is a branch, copy_CCA's shape, effect-side only. The chain is an analogy, and Peirce never called reading degenerate.

*Evidence:* CI thinkers-peirce-h2: 'dyadic_degenerate ... Φ_MIP=0.000000 ... adicity=2 (cause 2, effect 2)'. CI thinkers-peirce-h1: copy_BCA; 'copy_CCA ... adicity=3 (cause 2, effect 3)'. Register TR-S6-180, TR-S6-014.

## Q54. Your exogenous-sign model has one human. You can't use it to say anything about literacy between two.

*Target:* P41 (reading as a triad inside a dyadic coordination)

Agreed. In that model the object isn't the second human, so it models one reader. I use it only to show a three-term fact in a system that factors. The two-human claim rests on the chain alone, and I keep the two on separate lines. The model carries no thought or meaning either.

*Evidence:* CI thinkers-peirce-h4: sign_exogenous line. Register TR-S6-016 (corrected: not evidence about Peirce's text). peirce1931papers CP 1.345.

## Q55. Every platform has an active algorithm in the middle. So every platform is algorithmacy, and your claim is unfalsifiable.

*Target:* P42 (the algorithmacy form is the control)

The opposite. An active third is necessary, not sufficient. In the majority triad every node reads the others, and it reads Φ_MIP = 0.000000 with an empty core. A platform counts only once its rule is modelled and the model passes. That makes the claim falsifiable one form at a time.

*Evidence:* CI thinkers-simmel-h3: majority_triad line. CI thinkers-peirce-h1: control PASS. Register TR-S6-002, TR-S6-252 (lab_contradicted).

## Q56. Simmel's arbitrator passes your test with no algorithm. And 'whatever the book was to literacy, AI is to algorithmacy' makes AI the medium, while your argument makes it a party.

*Target:* P43 (the target is older than AI)  **backup**

Both conceded. The arbitrator reads Φ_MIP = 2.000000 with all three in the core, so the target is triadic coordination as such. AI's role is a historical premise, not a lab result: the third is now mass, opaque and shifting. The book analogy holds at that historical level and fails at the level of roles, so I use it only historically.

*Evidence:* CI thinkers-simmel-h4-nonpartisan: 'arbitrator             triadic  Φ_MIP=2.000000  core=('A', 'M', 'B') coreΦ=2.000' (show without label column). Simmel 1902 on mediator, arbitrator, tertius gaudens: simmel1902number2 pp.166–174.

## Q57. 'When A = 1, M follows B' is just AND. You need to infer the other side in any strategic game. Nothing here is special.

*Target:* P44 (the rule makes a demand)

In any game with hidden information, yes. The difference is where the dependence sits. Here the third's next determination, which both parties act through, isn't fixed by either party's act. The demand comes from the rule, not from stipulation. I don't claim it is unique to algorithms. I claim this form creates it.

*Evidence:* Control rule M′ = A ∧ B (peirce/forms.py l.37). concepts.md L7–17: first component, inferring the hidden other side (paraphrase).

## Q58. An irreducible target doesn't make the skill distinct. Someone good at one-input coordination might just be good at this too.

*Target:* P45 (the competence bridge)

Right: target irreducibility doesn't entail skill distinctness. I state the bridge as a premise: coordinating through M requires anticipating M's determinations. That is weaker than the lab's old claim that competence follows form, which our register marks as a stipulation. Whether the skill separates in people is a question for data, not models.

*Evidence:* Register TR-S6-033 (stipulation). essays/literacy_or_algorithmacy.md l.136 (paraphrase only).

## Q59. Boolean toy models of three or four binary elements say nothing about platforms.

*Target:* P46 (scope)

They don't measure platforms, and I say 'Boolean models, not people' on the last slide. What they do show is that the kind exists and that one-input mediation can't compose it. Whether a given dispatch or hiring system is of that kind is a per-form question: model its rule, then run the test.

*Evidence:* peirce/paper.md l.339–341. Register TR-S6-276, TR-S6-280 (lab_contradicted: triadicity is a per-form verdict).

## Q60. A shared spreadsheet both parties edit, whose cells combine their entries, is 'reading and writing'. By your definition it's algorithmacy. Absurd.

*Target:* C8 (literacy forms compose one-input mediations)

Not absurd; intended. If a cell is set jointly by both parties' entries and both act on it, it has the control's shape, and coordinating through it is algorithmacy in my sense. The line runs at joint determination, not at paper versus screen.

*Evidence:* ARGUMENT D4, P39. CI thinkers-peirce-h1: control PASS string.

## Q61. Non-empty in models isn't non-empty in the world. Your modus ponens runs on a toy.

*Target:* C9 (the target class is non-empty and non-composable)

C9 is stated in models. It shows the kind exists as structure and can't be composed from literacy's forms among fixed parties. Whether a given platform instantiates it is a separate, per-form question. The argument secures a target, not a population.

*Evidence:* ARGUMENT C9 limits. Register TR-S6-276.

## Q62. 'The ontological argument for the necessity of algorithmacy' overclaims. You've shown a property of Boolean models.

*Target:* C10 / Conclusion ('ontological argument for necessity')  **backup**

It would overclaim if I meant that triads are primitives or that everyone needs algorithmacy. I mean conditional necessity: wherever coordination takes this form, the competence it demands isn't a composition of competences for one-input mediation. The ontology concerns the target kind's existence and non-composability, shown on Boolean models, among fixed parties.

*Evidence:* Register TR-S6-280, TR-S6-276 (lab_contradicted: 'triads as irreducible primitives'). ARGUMENT C10.

## Q63. You define literacy as one-input mediation and algorithmacy as joint determination, then 'prove' one-input doesn't compose joint determination. That's circular.

*Target:* Conclusion (circularity)  **backup**

The definitions are mine, and the ceiling nearly follows from them. I said so. Two parts don't follow. First, joint determination can sit inside a whole at all, which is a lab result. Second, the Quinean route of pairing doesn't escape it among fixed parties, which is an argument. The circular part is the calibration. The rest is the claim.

*Evidence:* CI thinkers-peirce-h1 control PASS; thinkers-peirce-h3 giving_genuine; thinkers-peirce-h4 sign_pragmatic. Register TR-S5-094. ARGUMENT P30.
