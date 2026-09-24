# Review findings — 2026-09-24

Pinned at `7634c1c` (first deck and script). Six seats and a mechanical auditor, blind to each other, correctness only; prose-style findings were out of scope. 107 findings: blocking 15, should_fix 55, minor 37.

### [blocking] algocon-audience — deck slide 14 (deck.md:97) / script slide 14 (script.md:138-141)

*number, confidence high.* The talk claims the crossing runs both ways: 'Simmel's majority has members jointly determined by the other two while the system as a whole factors… We wrote that prediction down and published it before we ran it. So wholeness and joint determination come apart in both directions.' At the pinned commit nothing registers this. ci/reproduce.json has only `majority_triad … Φ_MIP=0.000000 core=()` and `H3 (majority triad binds all three): REFUTED`, and NUMBERS.md:12 backs only the Φ = 0. The joint-determination result (C ← {A,B}, φ = 0.5) exists only as fast results on the unmerged branch probe/peirce-joint-determination. The script also says 'members' in the plural, but the addendum reports C only. And 'published' overstates a pre-registration sitting on an open branch.

**Proposed:** Keep deck line 97 and the 'both directions' sentence out until the JD addendum is merged and its expect strings (the majority C ← AB distinction and its φ) are in ci/reproduce.json and NUMBERS.md. Once merged, say 'one member, C, is jointly determined by the other two' (or register all three purviews), and say 'pre-registered' instead of 'published'. Until then the script should read: 'In our registered results wholeness without joint determination is common; the reverse case, joint determination in a system that factors, is the subject of a pre-registered addendum now running.'

*Evidence:* CLAIM.md:74 lists as do-not-claim 'That joint determination and wholeness cross "both ways" on registered evidence'. CLAIM.md:101 (Decision 6): 'If they are not registered, slide 14 claims the crossing in one direction only.' ARGUMENT.md:381: 'The cell "party jointly determined, system factors" has no registered case.' ci/reproduce.json:35-41. `git branch -a` shows probe/peirce-joint-determination unmerged.

### [blocking] algocon-audience — script slides 8, 12, 14 (script.md:80, 116-122, 137-139); deck slides 8, 12, 14

*audience_comprehension, confidence high.* The script never says what Φ measures, what 'the whole is irreducible' or 'does not factor' means, what the numbers 2.0 and 0 are on, or what a 'core' is. It glosses IIT only as 'the instrument'. The whole second half of the talk (slides 8 and 12–16) runs on Φ, 'whole' and 'core'. An organization scholar hears 'Φ equal to 2.0, with all three in the core' and cannot tell whether 2.0 is large, small, a probability or a count.

**Proposed:** At slide 12, add two spoken sentences plus a one-line slide gloss, e.g.: 'IIT asks a simple question of a system: if you cut it into independent parts, what do you lose? Φ is how much the system's cause-and-effect structure loses under the least damaging cut. Φ = 0 means some cut loses nothing, so the system factors into independent pieces. Φ > 0 means every cut loses something, so it is one whole. The core is the largest set of parts that forms such a whole.' Say plainly that Φ is in bits and that only zero versus non-zero matters for the argument.

*Evidence:* script.md:116-117 ('using integrated information theory, IIT 4.0, as the instrument') is the only introduction. 'Core' first appears at script.md:80 and deck.md:59 with no gloss. ARGUMENT.md:35 (D2) has the definitions the talk needs.

### [blocking] hostile-referee — deck slide 14 (deck.md:97); script slide 14 (script.md:137-142)

*number, confidence high.* The talk says Simmel's majority has 'members jointly determined by the other two while the system as a whole factors', and concludes 'wholeness and joint determination come apart in both directions'. At commit 7634c1c no registered expect string supports joint determination in majority_triad. ci/reproduce.json:38 registers only 'majority_triad dyadic Φ_MIP=0.000000 core=() coreΦ=0.000'. The JD2 result (C ← AB, φ=0.5) exists only as a fast result on the unmerged branch probe/peirce-joint-determination (c7535bc holds the pre-registration and no CI string). CLAIM.md:74 forbids the claim that joint determination and wholeness cross 'both ways' on registered evidence. Decision 6 (CLAIM.md:101) says that until the result is registered, slide 14 may claim the crossing in one direction only. The fast result also names one member (C). The script's plural 'members' goes beyond it.

**Proposed:** Gate the line and the 'both directions' sentence on merging the JD addendum into ci/reproduce.json with an expect string that shows the majority's single-mechanism cause purview (e.g. 'C -> cause AB'). Add that string to NUMBERS.md. Say 'a member (C) is jointly determined by the other two' unless the registered output shows all three. If the addendum is not merged before October, delete deck line 97 and say only: 'Wholes without a triad exist. The registered record has no case yet of joint determination outside a whole. We have pre-registered that test.'

*Evidence:* ci/reproduce.json:35-41; CLAIM.md:74, :101; ARGUMENT.md:381 ('The slides say only that the crossing runs one way in the registered results'); talk/NUMBERS.md:12 (row '0' certifies only Φ=0, not joint determination); git show c7535bc (pre-registration only)

### [blocking] hostile-referee — script slide 2 (script.md:16-21) and slide 16 (script.md:162); deck slide 2 (deck.md:13-16)

*logic, confidence high.* The talk's central conditional equivocates on 'reduce'. Slide 2 states the antecedent in definability terms: 'If every relation among three can be rebuilt out of relations between two … algorithmacy is literacy applied twice.' Slide 9 then concedes that Löwenheim and Quine do exactly this ('you can code any relation as a relation between two things'). As spoken, the antecedent is therefore true by the talk's own account, and the conditional fires against algorithmacy. The script promises to fix 'reduce' (l.21) and later claims to have done so (l.162). It never states the fixed sense: rebuilt, among the same parties, from links in which each element answers to one other. A hostile listener can say the talk moved from 'reduce' = definability (slide 2) to 'reduce' = causal composition (slide 16) without announcing the change. ARGUMENT D5 flags exactly this: stated as 'if triads reduce to dyads', both horns fire.

**Proposed:** At the end of slide 10 or the start of slide 12, add one sentence that fixes the sense: 'From here on, "reduce" means this: rebuild the form among the same parties out of links in which each element's next state answers to just one other element. In Quine's sense, triads reduce. In this sense, the question is still open.' Restate slide 2's conditional in this sense (e.g. 'If every coordination through a jointly determined third could be rebuilt from one-at-a-time links among the same people …'). Deck slide 16 can then carry 'reduce = compose among the same parties'.

*Evidence:* ARGUMENT.md:64-68 (D5 'Why restate it'); CLAIM.md:12, :19; script.md:84-86 vs :16-17

### [blocking] hostile-referee — deck slide 16 (deck.md:108); script slide 13 (script.md:125-126), slide 12 (script.md:119-120), slide 15 (script.md:149-151), slide 16 (script.md:162-164)

*logic, confidence medium.* The talk equivocates between 'one-input mediation', where the medium answers to one party at a time (slides 2, 15, 16), and one-input wirings, where every element, the people included, copies exactly one other (slide 13, the only evidence for premise 1). The slide-12 criterion counts any party jointly determined by two others. It does not require that party to be the third between the coordinating parties. Two consequences follow, and a hostile referee will press both. (a) A reader who combines two one-input texts, or a text and her own situation, is herself jointly determined. With her action fed back, she meets the slide-12 criterion inside a literacy chain. (b) The lab's own positive case, the pragmatic sign (I ← {O, S}, S′ = O), is exactly a one-input text read by a reader who acts on the world, and slide 14 counts it as a triad. As worded, deck slide 16 ('one-input mediation never composes joint determination') is false when only the medium is one-input. It holds only when every element is. What separates literacy from algorithmacy in the thesis is where the joint determination sits: in the third between the two parties, or inside one reader.

**Proposed:** Use the locked wording on deck slide 16: 'Among fixed parties, one-input determination never composes joint determination.' In the script at slide 13 say: 'in these models every element, the people included, answers to one other.' State the coordination criterion as 'the third between the two parties is jointly determined by both'. At slide 15, add: 'A reader who combines what she reads is jointly determined too. That triad sits inside one person, as in the working sign. It is not a third between two people. A person who takes input from both parties and acts back on both is the arbitrator, and I concede that case below.'

*Evidence:* CLAIM.md:16-19 (thesis uses 'one-input determination' for the composition claim; 'a medium whose next state answers to one party' for literacy); ARGUMENT.md:326 (89 wirings: 'each node copies exactly one other node'), :388 (pragmatic sign), :441-446 (P41: sign triad inside one reader); ci/reproduce.json:119 (sign_pragmatic I -> cause OS)

### [blocking] hostile-referee — script slide 15 (script.md:153-155) and slide 16 (script.md:166-169)

*logic, confidence high.* The script smuggles in the competence bridge. It moves from 'the form cannot be composed from literacy's forms' (ontology of the target) to 'the competence it demands is not literacy twice' (competence) and never states the premise that licenses the step. ARGUMENT names that premise P45: coordinating through M requires anticipating M's determinations. It says the talk 'states P45 openly as a premise', and weakest link 2 says a structural irreducibility does not entail a distinct skill. The demand as spoken is also mis-specified: 'what the third does next turns on the other party she cannot see. That is the demand a literate reader never faces.' A correspondent faces that too, because the reply turns on an unseen other. P44's actual demand is narrower. Under M′ = A ∧ B, her own act fixes M only when A = 0, so she cannot read her own effect off M without inferring the other side.

**Proposed:** At slide 15 replace the demand sentence with P44's: 'Under this rule her own act settles the outcome only some of the time. Otherwise it turns on the other party's act, so she has to infer the other side from what M does.' Drop 'never faces', or restrict it to 'a reader of a one-party text'. At slide 16 state the bridge as a premise before the conclusion: 'One premise joins the form to the skill: to coordinate through a third, you must anticipate what it will do. Grant that, and the competence this form demands is not literacy twice.'

*Evidence:* ARGUMENT.md:456-458 (P44, P45), :486-487 (weakest link 2); CLAIM.md:23 (necessity is conditional)

### [blocking] iit-specialist — Slide 14 (deck.md:97) and script slide 14 (script.md:138-141)

*citation, confidence high.* The talk says Simmel's majority has members jointly determined by the other two while Φ = 0, and concludes that 'wholeness and joint determination come apart in both directions.' At the pinned commit no ci/reproduce.json string registers the majority triad's cause purviews. The only registered majority line is 'majority_triad dyadic Φ_MIP=0.000000 core=() coreΦ=0.000'. The JD addendum (c7535bc, branch probe/peirce-joint-determination) is not an ancestor of HEAD. CLAIM.md bans exactly this claim, and ARGUMENT.md says the slides assert only one direction.

**Proposed:** Two options. (a) Before the talk, merge the addendum with a fast-run CI expect string for the majority's joint-determination line and its JD2 verdict, then add a NUMBERS.md row. (b) Otherwise cut deck line 97 and script 138-139 and say instead: 'In the registered results they come apart in one direction: wholes without joint determination.' Whichever you choose, the tie problem in the next finding also has to be fixed.

*Evidence:* CLAIM.md:74 ('That joint determination and wholeness cross "both ways" on registered evidence'); CLAIM.md:101 ('If they are not registered, slide 14 claims the crossing in one direction only'); ARGUMENT.md:381 ('The slides say only that the crossing runs one way in the registered results'); ci/reproduce.json:38; `git merge-base --is-ancestor c7535bc HEAD` gives NOT_IN_HEAD; NUMBERS.md has no row for a majority cause purview.

### [blocking] iit-specialist — Slide 14 (deck.md:97), script slide 14 (script.md:138-139) and the addendum's JD2 reading

*logic, confidence high.* The majority triad's 'joint determination' comes from a tie-break, not from a unique IIT result. Each single-element mechanism's cause φ is exactly 0.5 on all three two-element purviews (AB, AC, BC). PyPhi resolves the tie by index order and reports AB for every mechanism. A's purview AB and B's purview AB each include the mechanism itself, so under the JD criterion ('two or more elements other than X') only C qualifies. If the labels were permuted, a different member would qualify. The script's plural 'members jointly determined by the other two' is not what the instrument outputs, and even C's reading is only one of three tied purviews. The other two tied readings are 'determined by itself and one other', which is not joint determination. The positive exemplars do not have this problem: control M←AB (2.0 against 1.0 for A or B alone), giving R←GT and sign I←OS are strict maxima.

**Proposed:** Do not present the majority as a case of joint determination without a whole. If the crossing has to be shown, use a JD3(b) two-input form that factors (Φ_MIP = 0) and has a strictly maximal cause purview of two other elements, and check it for ties. Label that check post hoc, because the pre-registered JD2 rule does not treat ties. If the majority stays, say 'C's strongest cause purview ties between the other two and pairs that include C itself', and drop 'members jointly determined by the other two'.

*Evidence:* Reproduced with the repo's instrument (venv-4.0, pyphi new_big_phi, MAJORITY_TRIAD from simmel/forms.py:51) at state (1,1,1). find_mice(CAUSE) for each single mechanism gives: A/B/C purviews A,B,C = 0.4387; AB, AC, BC = 0.5000; ABC = 0.2500. phi_structure reports 'cause AB' for A, B and C alike. The same check on CONTROL gives M: AB 2.000, A 1.000, B 1.000, all others 0. The forms.py:30 header filters PyPhi's 'resolve_congruence' warnings, which concern tie resolution.

### [blocking] logician — Slide 10 (deck.md:67-70) and script slide 10 (script.md:95-102)

*logic, confidence high.* The universal claim 'Every reduction mints a third', and the contrast 'Expressible over a larger universe ≠ composed from pairs among the same parties', are false as stated, and the talk's own evidence document says so. Primitive-positive (relational-algebra) composition reduces triads to dyads on a fixed domain and adds no new object. The simplest case: teridentity is (x=y) ∧ (y=z), built from binary identity among the same three places. Koshkin proves that on any finite domain with |D| ≥ 3 every relation pp-reduces to binary relations with no domain extension. None of these reductions mints an object. What they keep is a variable shared by three places, a three-way junction. So 'larger universe' vs 'same parties' is the wrong line to draw. The line that holds is 'with a three-way junction (as a minted object OR as a shared variable)' vs 'without one'. The phrasing also equivocates between 'universe' (the domain of individuals) and 'parties' (the places or relata). A pp reduction keeps the same domain but adds hidden places.

**Proposed:** Retitle the slide 'Every reduction keeps the junction' (or 'hides a third'). Replace the second line with: 'Dyads build a triad only with a three-way junction — a minted object (Kempe, Löwenheim, Quine) or a variable shared three ways (x=y ∧ y=z). Without one, never (Hereth Correia & Pöschel 2006, Thm 2; Koshkin 2025, Thm 6).' Rewrite script l.97-100 to match. Say that pairing reductions mint an object, and that fixed-domain reductions carry the junction as a shared variable instead. That also makes slide 11's closing line ('the constructions split … on the three-way junction') follow from slide 10 instead of contradicting it. Revise C3b in ARGUMENT.md the same way.

*Evidence:* ARGUMENT.md C4 (l.303-306): 'Where a shared variable is free glue (pp or relational algebra with coordinate identification, on |D| ≥ 3 …), triads reduce'. ARGUMENT.md P22 (l.270): '=₃ = ∆(ζ(= × =))'. ARGUMENT.md P23 (l.278). koshkin2025completeness Thm 3 p.13 ('we can now reduce any cofinite relation to binary ones as long as |D| ≥ 3'). Card l.38: 'on |D| ≥ 3 pp-reduction to binaries succeeds without any extension (Theorem 3)'. herethcorreia2004power §3 p.11: ⟨∅⟩_RA already contains every diagonal relation. The author's own QA Q31 (QA.md:245-249) concedes the point: 'The reduction doesn't remove the junction; it moves the junction into the machinery'. C3b's 'Every definability reduction adds an object' (ARGUMENT.md:230) conflicts with P22/P23 in the same document.

### [blocking] mechanical — script slide 3 (script.md:30-31)

*factual, confidence high.* The script says "Notice what he did not do. He did not prove it. … The proof came later, and it came as arithmetic." That says Peirce proved the thesis, which CLAIM.md forbids. It is also false: the valency arithmetic is an argument, and the first complete proof of the hard clause is Hereth Correia & Pöschel 2006.

**Proposed:** Replace with: "The argument came later, and it came as arithmetic." Or: "He argued it later, by arithmetic; a full proof took until 2006."

*Evidence:* CLAIM.md:38 (do not claim that Peirce "proved" the thesis; he argued it). herethcorreia2006teridentity p.2 ("Peirce mentioned he found a proof, but no corresponding publication has been found"; "we present the complete mathematical proof of the difficult part").

### [blocking] mechanical — script slide 14 (script.md:137-142); deck slide 14 (deck.md:97)

*number, confidence high.* The talk claims that Simmel's majority "has members jointly determined by the other two while the system as a whole factors", and concludes that "wholeness and joint determination come apart in both directions". Only the Φ=0 half is registered. The joint-determination half (the fast JD2 result: C jointly determined by A and B, φ=0.5) is in no ci/reproduce.json check at this commit. The addendum sits on the unmerged branch probe/peirce-joint-determination (c7535bc).

**Proposed:** Before the talk, land the JD PR with a CI expect string for majority_triad's cause purview (e.g. 'C -> cause AB … φ=0.500'), then add NUMBERS.md rows. Otherwise cut deck line 97 and script lines 138-141 to one direction: "Wholes can lack joint determination." Also say "a member" or "C", not "members", unless all three are registered.

*Evidence:* ci/reproduce.json, thinkers-simmel-h3-majority, which registers only Φ_MIP=0.000000 core=() and H3 REFUTED. CLAIM.md:74 (do not claim that joint determination and wholeness cross both ways on registered evidence). CLAIM.md:101 (if the majority cell is not registered, slide 14 claims the crossing in one direction only). git merge-base shows the JD branch is not merged.

### [blocking] peirce-scholar — script slide 3 (script.md:31); leads into slide 4

*factual, confidence high.* "The proof came later, and it came as arithmetic" says Peirce proved the thesis. CLAIM.md lists this under Do-not-claim: "That Peirce 'proved' the thesis (TR-S1-031). He argued it." The valency arithmetic is an argument, and it depends on a premise (a node is a relative) that the talk itself says on slide 5 is contestable. Calling it a proof also works against the talk's own C1 reading, which treats it as a conditional theorem.

**Proposed:** "The argument came later, and it came as arithmetic." If a date is wanted: the arithmetic first appears in words in 1887-88 (CP 1.363) and as a formula in the 1897 Monist. On deck slide 4, the CP 1.363 attribution could read "Peirce, 1887-88 (CP 1.363)" so the audience sees that it came before the 1897 formula.

*Evidence:* CLAIM.md:38; ARGUMENT.md:84 (P2: "Peirce's argument for the negative clause is valency arithmetic"); peirce1890guess CP 1.363 (the words version, dated 1887-88 in W6 and c. 1890 in CP); peirce1897logic p.183 (the formula)

### [blocking] peirce-scholar — script slide 5 (script.md:53-55)

*citation, confidence high.* "Kempe's extra unit, he said, is itself the triad" puts in Peirce's mouth a claim he did not make in 1892. In The Open Court, Peirce answers Kempe in three ways. (1) Kempe's diagram leaves out representation, the diagram's connection with nature. (2) Kempe "has, and must have, three kinds of elements" (spots, lines, and the absence of lines), and "the attachment of lines to spots" carries mediation. (3) The diagram "fails to afford any formal representation of the manner in which this abstract idea ['this action'] is derived." Peirce never says the auxiliary unit is the triad. The peirce1892critic card corrects exactly this reading where the lab paper made it (paper.md l.272-274). The node-as-relative argument belongs to 1897 (Monist pp.170-171), not to the 1892 reply. So the next sentence, "from its very first round the dispute has been about one thing — the status of the junction", overstates things. The 1892 round was also about representation and hypostatic abstraction.

**Proposed:** Replace with the supported version: "His answer was that Kempe's picture still has mediation in it, in 'the attachment of lines to spots', and that the unit is minted by an abstraction, 'this action', whose derivation the diagram never shows." Then: "So from the first round the dispute concerned the junction and the minted unit." If the talk wants "the unit is the triad", say it in the speaker's own voice as the talk's reading, not as "he said".

*Evidence:* peirce1892critic.md Loci (CP 3.423 attachment/mediation; CP 3.424 'this action' and the non-representation of its derivation) and Notes l.34 ("A version the sources support: ... the spot and its three attachments are themselves the mediation, minted by an abstraction the diagram does not represent"); Open Court 6:3418 text (triadic_reduction_local/fulltext/opencourt_1892-10-13_v6n268_djvu.txt l.570-640); ARGUMENT.md P5 l.108-114

### [blocking] peirce-scholar — deck slide 14 (deck.md:97); script slide 14 (script.md:138-142); script slide 8 (script.md:80-81)

*number, confidence high.* The slide and script claim that Simmel's majority has "members jointly determined by the other two while the system as a whole factors", and conclude that "wholeness and joint determination come apart in both directions". At the pinned commit, reproduce.json registers only the majority's Φ_MIP=0 and core=(). The majority's cause purview (C jointly determined, φ=0.5) is on the unmerged JD addendum branch, so it is a fast result, not a registered one. CLAIM.md forbids claiming the crossing "both ways" on registered evidence, and decision 6 says slide 14 claims the crossing in one direction only unless the majority cell is registered. NUMBERS.md declares no φ=0.5. Separately, slide 8 says of the same model "Three parties, and nothing binds them". Slide 14 then says each member is jointly determined by the other two, and the audience will hear a contradiction. The addendum also reports a single party (C), where the script says "members" in the plural.

**Proposed:** Before the talk, land the JD addendum and add its majority purview line to reproduce.json and NUMBERS.md. Until then, cut the third line of slide 14 and the matching sentence and say "in the registered results the crossing runs one way". Once it is registered, change slide 8's "nothing binds them" to "the whole does not bind them", and say "one member is jointly determined by the other two (φ = 0.5)" to match the result.

*Evidence:* ci/reproduce.json:35-41 (thinkers-simmel-h3-majority: only Φ_MIP and core); CLAIM.md:74, 101; ARGUMENT.md:381 ("no registered case" for the cell); talk/NUMBERS.md:12

### [blocking] simmel-sociologist — Slide 8 (deck.md:56-59) and script slide 8 (script.md:74-81)

*factual, confidence high.* The talk uses the majority result as an example of Simmel's own point, when it is the lab's refutation of its reading of Simmel. The slide sets 'configurations of twos' (Simmel's distant third) directly above 'Lab, Simmel's majority of three: Φ = 0, no core'. The script says 'Simmel also saw that three people are not automatically a triad… Our lab tested a version of this.' Both claims are wrong. (a) The lab never modelled a distant third; H3 tested whether a majority binds all three. (b) For Simmel the majority is one of the things a third makes possible: 'occasion for such a majority is given so soon as a single unit is added' (II:158). The lab pre-registered that reading as H3 ('the majority is a binding whole'). The model came out REFUTED, and the Simmel paper calls this 'the sharpest result of the five'. So the talk takes a result the lab scored against Simmel and presents it as Simmel's own insight. The CLAIM lock bars saying 'Simmel was refuted', and this move breaks the same rule from the other side. A Simmel specialist in the room will catch it.

**Proposed:** Separate the two points. Keep 'configurations of twos' as Simmel's textual concession: not every arrangement of three makes a group. Move the majority result off Simmel's authority. On slide 8, write 'Lab: a majority-of-three rule, Φ = 0, no core' (or move it to slide 14 only). In the script, replace 'Our lab tested a version of this' with something like: 'Simmel expected the majority to be what the third makes possible. We modelled it and predicted it would bind all three. It did not: Φ is zero. On our rendering, three parties with a majority rule still do not make a whole.' Do not say Simmel 'saw' this.

*Evidence:* simmel1902number2.md:24 (p.158 majority locus); org_frontier/thinkers/simmel/hypotheses.md:32-40 (H3 = Simmel's reading: majority binds); FINDINGS.md:17 (H3 REFUTED); simmel/paper.md:238-248 ('What he named as the change in kind was the possibility of a majority… C3 is refuted'); forms.py:51 (no distant-third form exists); CLAIM.md:73; simmel1902number1.md:25 (p.45: superindividual energy 'even in the case of a combination of only three… in some measure present').

### [should_fix] algocon-audience — deck slide 8 (deck.md:59) / script slide 8 (script.md:79-81)

*audience_comprehension, confidence high.* Φ and 'core' appear on slide 8, four slides before IIT is introduced on slide 12. The audience gets a lab number from an instrument they have not heard of, in the middle of the Simmel section.

**Proposed:** Either move the majority result to slide 14, where it lands in any case, or say on slide 8: 'Our lab has a test for whether a system of parts is one whole, which I'll explain shortly; the majority of three fails it.' Keep the Φ symbol off slide 8.

*Evidence:* deck.md:59 'Lab, Simmel's majority of three: Φ = 0, no core.' IIT first appears at script.md:116-117.

### [should_fix] algocon-audience — script slide 6 (script.md:58-59); deck slide 6 (deck.md:45)

*citation, confidence high.* The script puts CP 1.345's phrase 'merely one dyadic relation followed by another' on the wrong example. In CP 1.345 the phrase describes A throwing B away so that it accidentally hits C. The book-put-down, picked-up-later example is CP 8.331, where Peirce calls it 'a degenerate form of Thirdness in which the thirdness is externally appended'. The script says 'If A puts a book down and C later picks it up, you have, in his words, "merely one dyadic relation followed by another"', which is a misattributed quotation.

**Proposed:** Either keep CP 1.345 and use its own example: 'If A throws B away and it happens to hit C, that is, in his words, "merely one dyadic relation followed by another"'. Or keep the put-down/pick-up example and quote CP 8.331: 'a degenerate form of Thirdness in which the thirdness is externally appended'. In that case, change the deck line to cite CP 8.331.

*Evidence:* peirce1931papers.md:21-22 (CP 1.345: 'A's throwing B away and its accidentally hitting C … merely one dyadic relation followed by another'). peirce1904letter.md:25 (CP 8.331: 'A's laying down the B which C subsequently picks up … externally appended'). ARGUMENT.md:128-129 keeps the two apart.

### [should_fix] algocon-audience — script slide 3 (script.md:30-31)

*factual, confidence high.* 'The proof came later, and it came as arithmetic' says Peirce proved the thesis. The locked claim forbids this.

**Proposed:** 'The argument came later, and it came as arithmetic.' (Deck slide 4 already says 'The argument is arithmetic'.)

*Evidence:* CLAIM.md:38: do not claim 'That Peirce "proved" the thesis (TR-S1-031). He argued it.' ARGUMENT.md:84 calls it an 'argument… valency arithmetic'.

### [should_fix] algocon-audience — deck slide 8 (deck.md:58-59) / script slide 8 (script.md:75-81)

*logic, confidence high.* The script presents the majority triad as 'a version of' Simmel's distant third who leaves 'configurations of twos'. The model does not fit that description. In it every member reads all three (A′ = B′ = C′ = maj(A,B,C)), so no one is distant. Simmel himself treats majority as the new form that the third makes possible. The talk's own slide 14 then says the majority's members are jointly determined by the other two, which is the opposite of 'configurations of twos'. The link on slide 8 is an equivocation, and a listener who holds onto it, as the script asks, will be confused on slide 14.

**Proposed:** Separate the two points. Quote 'configurations of twos' for the distant third, which the lab did not model. Then introduce the majority on its own terms: 'Simmel noted that majority arrives with the third. Our model of it, where each member follows the majority, comes out not binding as a whole: three parties who each depend on the others, yet the system factors.' State the joint-determination part only once it is registered (see the slide 14 finding).

*Evidence:* org_frontier/thinkers/simmel/forms.py:51 (MAJORITY_TRIAD = maj(*x) for all three). simmel1902number2.md:24 (p.158: 'in a combination of two there is no majority… occasion for such a majority is given so soon as a single unit is added'). script.md:138-139.

### [should_fix] algocon-audience — script slide 12 (script.md:119) vs script slide 13 (script.md:132)

*logic, confidence high.* 'The criterion, fixed before our confirmatory runs' implies the criterion came first and the control result was confirmatory. The control and every registered exemplar ran before the author fixed the criterion on 2026-09-24. The only run made under the fixed criterion is the unmerged JD addendum. Slide 13 then says 'that split came after the result'. A listener cannot tell what was pre-registered and what was post hoc.

**Proposed:** Say: 'We fixed this criterion after our first probes, and then tested it in a pre-registered run on all ten registered models; it reads every one correctly.' Say that only once the addendum is merged and registered. Otherwise say: 'We fixed this criterion after the probes; a pre-registered check is running.'

*Evidence:* ARGUMENT.md:56 (D3 disclosure: 'the author fixed the criterion on 2026-09-24, after the probes had run'). CLAIM.md:102 (Decision 7). The JD addendum is not in ci/reproduce.json at 7634c1c.

### [should_fix] algocon-audience — script slide 9 (script.md:84, 90-92)

*factual, confidence high.* Three overclaims. (1) 'the reply that made most philosophers stop believing Peirce': Burch says only that the thesis was 'doubted by many'. Löwenheim 1915 cites Schröder, not Peirce, and Quine did not aim at Peirce, so neither was a 'reply'. (2) 'a two-page paper': JSL 19(3) runs pp. 180–182, three pages. (3) 'Quine himself never said so': the team read only p.180 and the notes. This is Koshkin's report and should be attributed to him.

**Proposed:** 'Now the result that led many to doubt Peirce.' 'a short paper' (or 'a three-page paper'). 'Koshkin reports that Quine never connected the result to Peirce; others did.'

*Evidence:* burch2021sep.md:23 ('doubted by many'). quine1954reduction.md:6 (pp. 180–182), :11 (pp. 181–182 unread), :18 (Koshkin n.1 reports Quine never related it to Peirce). ARGUMENT.md:213 (Löwenheim cites Schröder). CLAIM.md:39.

### [should_fix] algocon-audience — script slide 15 (script.md:153-155); script slide 2 (script.md:14)

*scope, confidence high.* 'The platform's next state is fixed by both parties at once, and both read it' asserts that a real platform has the control's form. The lab has modelled no platform rule. On slide 2 the driver–rider platform is only an illustration, but on slide 15 it becomes a factual claim that carries the argument.

**Proposed:** 'Algorithmacy's form is the control: a third whose next state is fixed by both parties at once, and which both read. A matching platform plausibly has this form, but whether a given platform does depends on its rule, which no one has modelled yet.'

*Evidence:* CLAIM.md:90: do not claim 'That the lab shows any worker, platform or real rule is triadic. No such case is modelled.' ARGUMENT.md:448 (P42: 'a platform counts only once its rule is modelled').

### [should_fix] algocon-audience — script slide 2 (script.md:12-13) vs slides 15–16

*logic, confidence medium.* The script's examples of literacy media, 'a text, a form, a ledger', include one that fails the talk's own test. A ledger or form that both parties write into and both read is set jointly and acts back on both, which is the control's shape. The ARGUMENT concedes this for tallies, scoreboards and posted prices. The talk concedes only Simmel's arbitrator. An ALGOCON audience, many of them accounting and IS scholars, will raise the shared ledger first.

**Proposed:** Drop 'a ledger' from slide 2 or replace it with 'a letter'. On slide 15, extend the concession by one clause: 'The same holds for a shared tally or a price both sides set: the criterion is about form, not about algorithms or about paper.'

*Evidence:* ARGUMENT.md:434 (P39: scoreboard, tally and posted price 'Each has the control's shape'). CLAIM.md:104 (Decision 5: talk uses the structural definitions).

### [should_fix] algocon-audience — script slide 16 (script.md:162-169); script slide 2 (script.md:21); deck slide 16 (deck.md:108)

*audience_comprehension, confidence high.* Slide 2 promises 'by the end I'll have fixed' a precise meaning of 'reduce', and slide 16 says 'in the sense of "reduce" I promised to fix', but the definition is never stated. The deck's 'Among fixed parties' is never glossed. The link back to slide 10's 'composed from pairs among the same parties' is never made, and neither is the link from slide 2's 'answers to one party at a time' to slide 13's 'copies one other element' and slide 16's 'one-input mediation'. A listener hears three different phrasings of what should be one idea.

**Proposed:** Say the definition once, on slide 16 or on slide 12 where the lab's move begins: 'Here is the sense of reduce: can you build a party that two others jointly determine by chaining links in which each party responds to just one other, without adding or merging parties? That is what I mean by "among fixed parties" — no new object minted, as on slide 10.' Then use one term (one-input mediation) on slides 2, 13 and 16.

*Evidence:* ARGUMENT.md:68 (D5: 'The talk fixes "reduce" as causal composition among the same parties'). deck.md:14, 70, 89, 108.

### [should_fix] algocon-audience — deck slide 13 (deck.md:88-91) / script slide 13 (script.md:130-133)

*audience_comprehension, confidence high.* The slide says 'cause side never above 2' and 'every excess on the effect side' without saying what the 2 counts or what the two sides are. The script says 'the cause side never goes above 2' without saying 2 of what. 'Located' in the headline is jargon for 'placed on one side'.

**Proposed:** Add one spoken gloss: 'For each element, IIT asks two things: which parties fix its state — its causes — and which parties its state fixes — its effects. Count the parties in each fact. On the cause side the count never exceeds 2, the element plus its one source. All the three-party facts are an element fanning out to several readers.' On the slide: 'parties fixing any one element: never more than 2'.

*Evidence:* deck.md:90-91. The term the lab uses is adicity (ARGUMENT.md:35), which the talk avoids naming.

### [should_fix] algocon-audience — deck slide 14 (deck.md:95-96) / script slide 14 (script.md:137)

*audience_comprehension, confidence high.* Three names on slide 14 were never introduced. (1) 'The control': slide 12 calls the A → M ← B system 'the smallest case' and never names it 'the control', yet slides 14 and 15 lean on that name. (2) 'The pragmatic sign' on the slide versus 'Peirce's sign with a working interpreter' in speech, with no description of the model (interpretation acts back on the object). (3) 'Copy ring', never shown.

**Proposed:** On slide 12, say 'We call this the control.' On slide 14, use one name for the sign in both places and gloss it: 'the sign whose interpretation acts back on its object'. Gloss the copy ring as 'A copies C, B copies A, C copies B'.

*Evidence:* script.md:120 ('Here is the smallest case'), deck.md:95-96, script.md:137, 153. ARGUMENT.md:388 (pragmatic sign: O′ = I, so interpretation acts back on the object).

### [should_fix] algocon-audience — script slide 6 (script.md:62) → deck/script slide 14 (deck.md:95; script.md:136-137); slide 15 (script.md:145-147)

*audience_comprehension, confidence high.* Slide 6 presents the imitation of giving as 'one dyadic relation followed by another', which is a chain, and slide 15 says a chain is literacy's form. But slide 14 lists the imitation of giving as a whole at Φ = 2.0. The script never explains why a chain-like imitation comes out as one whole. The lab's model closes the loop (G′ = ¬R, T′ = G, R′ = T), so it is a ring, and the wholeness comes from the return. Without that, the promised 'we will meet both again' lands as a contradiction.

**Proposed:** On slide 14, add: 'Our model of the imitation closes the loop — what the receiver does feeds back to the giver — so it is a ring. That return makes it one whole, but no party in it is fixed by two others.'

*Evidence:* ARGUMENT.md:366-368 (P31: 'Peirce's degenerate giving … a ring. The imitation of giving gets its wholeness from the return, not from any three-term relation'). ci/reproduce.json:107.

### [should_fix] algocon-audience — script slides 15–16 (script.md:153-155, 166-169)

*logic, confidence medium.* The move from 'the target cannot be composed from one-input forms' to 'the competence it demands is not literacy twice' rests on an unstated premise: coordinating through M requires anticipating M's determinations. The ARGUMENT says the talk states this premise openly. The script gives the demand from the rule (slide 15, 'turns on the other party she cannot see') but never names the bridge premise. Organization scholars will notice that a distinct structure does not by itself imply a distinct skill.

**Proposed:** Add one sentence on slide 16 before the conditional-necessity gloss: 'One premise carries us from form to competence: to coordinate through such a third you must anticipate what it will do, and here that means inferring the party you cannot see.'

*Evidence:* ARGUMENT.md:456-458 (P44, and P45 'The talk states P45 openly as a premise'); ARGUMENT.md:486-487 (weakest link 2).

### [should_fix] algocon-audience — deck slides 10 and 12 (deck.md:69-70, 83) / script slides 9–10, 12

*audience_comprehension, confidence high.* The two places where one concrete example would rescue the talk have none. (1) Slides 9–10: 'expressible over a larger universe ≠ composed from pairs among the same parties' stays abstract. The audience never sees a triad turned into pairs by minting an object. (2) Slide 12: 'M′ = A and B' reads to a non-logician as 'M becomes both A and B'. Nothing tells them it is a logical AND (M turns on only if both do).

**Proposed:** (1) On slide 10: 'Take "A gives B to C". Mint an object, g, the giving. Now write three pairs: g's giver is A, g's gift is B, g's recipient is C. Every relation is two-place, but g is a new party that holds the three together. That is Kempe's unit and Peirce's "this action".' (2) On slide 12: 'M turns on only if both A and B are on, like a deal that closes only when both sides accept, and each side then sees whether it closed.'

*Evidence:* deck.md:70, 83; script.md:95-100, 120-121. P5/C3b (ARGUMENT.md:236-244) supply the gift example.

### [should_fix] hostile-referee — script slide 2 (script.md:12-13); script slide 15 concession (script.md:157-159); deck slide 15 (deck.md:104)

*logic, confidence high.* Slide 2 lists 'a text, a form, a ledger' as literacy's media, which classes literacy by the kind of medium. A ledger or form that both parties write to and both read, like a tally, a scoreboard or a posted price, has the control's shape: M′ = f(A, B), read by both. Under the structural definitions the talk uses (Decision 5), it is algorithmacy's form. ARGUMENT P39 says the talk 'uses the structural test and says so'. The script never says so. The slide-15 concession covers only a human third (the arbitrator). The unconceded case is the dangerous one: a non-algorithmic, non-agent medium that people have long handled with literacy alone. Left implicit, it lets a critic say either that literacy already covers jointly determined thirds (which undercuts the conclusion) or that the talk defines literacy in two incompatible ways.

**Proposed:** On slide 2 replace 'a ledger' (and 'a form') with media one party fixes and another reads (e.g. 'a letter, a notice, a manual'). Extend the slide-15 concession by one sentence: 'Nor does it need a machine or a person. A tally or a shared ledger that both sides write and both read has this form too. What counts is how many parties the third answers to, not what it is made of.' That keeps the structural definition consistent from slide 2 to slide 16.

*Evidence:* ARGUMENT.md:434 (P39), :488-489 (weakest link 3: 'Arbitrators, tallies and markets meet the criterion'); CLAIM.md:100 (Decision 5)

### [should_fix] hostile-referee — script slide 10 (script.md:99-101) and slide 16 (script.md:171-174); deck slide 10 (deck.md:70)

*logic, confidence medium.* The 'same parties' restriction does all the work against Quine, and the script only asserts it: 'That second claim is the one coordination needs.' The script omits the defence ARGUMENT supplies (P36-grain, the interventionist premise that coordinating parties must be separately actable and intervenable). It also omits the talk's strongest counter (P35-bridge): Quine's pair-object, rendered causally, is itself a node jointly determined by both, so the reduction reproduces algorithmacy's form rather than literacy's. The closing objection is also misstated. The script says the choice is 'whether M counts as one party'. ARGUMENT's weakest link 1 is about merging A and B (or re-encoding the pair) so that M becomes a one-input element.

**Proposed:** After 'the one coordination needs', add the reason: 'A coordination between two people presupposes that each can act separately. Fuse them into one unit and you no longer have the coordination. And if you build Quine's pair as a thing that changes, it is set by both at once: the third comes back.' At slide 16, restate the objection as 'whether A and B count as two units rather than one is a choice', and keep the existing next-test sentence.

*Evidence:* ARGUMENT.md:400-408 (P35-bridge, P36-grain), :482-485 (weakest link 1: 'Merge two parties into one element and the control's M becomes a one-input element')

### [should_fix] hostile-referee — script slide 8 (script.md:75-81); deck slide 8 (deck.md:58-59)

*factual, confidence high.* The talk presents the majority-triad result as the lab testing 'a version of' Simmel's distant third ('configurations of twos'), and so as support for Simmel. The lab's H3 rendered Simmel's opposite claim, that a majority binds all three, and that prediction was REFUTED (ci/reproduce.json:41). The majority form is not a distant third either: every member reads all three. On slide 14 the same model is said to have members jointly determined by the other two, which is the opposite of 'configurations of twos'. 'Three parties, and nothing binds them' (slide 8) then conflicts with slide 14's joint determination. A listener will ask whether the members are bound or not.

**Proposed:** Keep Simmel's distant-third quotation as Simmel's point. Introduce the lab line as a separate form: 'A different three-party form, the majority of three, where each follows the majority, reads Φ = 0 with no core: the system as a whole factors.' Replace 'nothing binds them' with 'the whole factors'. Do not say the lab tested the distant third, and do not present the result as confirming Simmel.

*Evidence:* ci/reproduce.json:38, :41 ('H3 (majority triad binds all three): REFUTED'); org_frontier/thinkers/simmel/hypotheses.md:32-41; simmel1902number2 card p.166 (distant third: no reciprocity embracing all three)

### [should_fix] hostile-referee — script slide 6 (script.md:58-60); deck slide 6 (deck.md:45)

*citation, confidence high.* The script misattributes a quotation. It attaches CP 1.345's 'merely one dyadic relation followed by another' to the example of A putting a book down and C later picking it up. In CP 1.345 that phrase describes A throwing B away and B accidentally hitting C. For the put-down/pick-up case (CP 8.331), Peirce says something different: it is 'a degenerate form of Thirdness in which the thirdness is externally appended', which is still Thirdness, degenerate, not merely two dyads.

**Proposed:** Either use Peirce's CP 1.345 example ('If A throws a book away and it happens to hit C, you have, in his words, "merely one dyadic relation followed by another"'), or keep the put-down example with its own CP 8.331 wording ('a degenerate form of Thirdness in which the thirdness is externally appended'). Keep the deck's CP 1.345 label only with the throwing example.

*Evidence:* peirce1931papers card, CP 1.345 loci (vol.1 p.176: 'This does not consist in A's throwing B away and its accidentally hitting C … merely one dyadic relation followed by another'); peirce1904letter card, CP 8.331 ('A's laying down the B which C subsequently picks up. That would be a degenerate form of Thirdness in which the thirdness is externally appended'); ARGUMENT.md:127-129

### [should_fix] hostile-referee — deck slide 14 (deck.md:95); script slide 14 (script.md:137)

*audience_comprehension, confidence high.* Slide 6 introduces the 'imitation of giving' as a one-way handoff (put down, picked up later), and slide 15 treats a one-way chain as Φ = 0. Slide 14 then says the imitation of giving is a whole at Φ = 2.0. The lab's model (G′ = ¬R, T′ = G, R′ = T) is a ring with a return from receiver to giver. Its wholeness comes from that return, not from any three-term fact. Without that explanation the audience hears a contradiction (a chain that is a whole), and a hostile listener can use it against the slide-15 claim that chains do not bind.

**Proposed:** In the slide-14 script add: 'Our model of the imitation closes the loop, since what the receiver holds feeds back to the giver. That return makes it a whole, like a ring of copies. No three-term fact does.'

*Evidence:* org_frontier/thinkers/peirce/forms.py:45 (GIVING_DEGENERATE); ci/reproduce.json (giving_degenerate Φ_MIP=2.000000, adicity 2); ARGUMENT.md:363-368 (P31: 'gets its wholeness from the return')

### [should_fix] hostile-referee — script slide 3 (script.md:30-31)

*factual, confidence high.* 'He did not prove it … The proof came later, and it came as arithmetic' says Peirce later proved the thesis. CLAIM.md forbids saying Peirce 'proved' the thesis: he argued it. The 1897 valency arithmetic is an argument, conditional on counting a node as a relation, which slide 5 itself calls a 'hidden premise'.

**Proposed:** 'Notice what he did not do: he gave no argument for it here … The argument came later, and it came as arithmetic.'

*Evidence:* CLAIM.md:38 ('That Peirce "proved" the thesis (TR-S1-031). He argued it.'); CLAIM.md:26

### [should_fix] hostile-referee — script slide 12 (script.md:119)

*logic, confidence high.* 'The criterion, fixed before our confirmatory runs' implies the criterion came before the results shown. The author fixed it on 2026-09-24, after every probe on slides 12-14 had run (ARGUMENT D3 disclosure). The only runs made after it are the JD addendum, whose results are unregistered at this commit, and no slide presents them apart from the unregistered majority line. The audience will take the control, the 89 wirings and slide 14's classes as a test of a criterion fixed in advance.

**Proposed:** 'I fixed this criterion after the probes you will see had run. We then pre-registered it and ran it forward.' If the JD addendum is registered, add: 'It reads all ten registered exemplars as predicted', citing the registered JD1 expect string. If it is not, say 'post hoc' plainly here.

*Evidence:* ARGUMENT.md:56 ('the author fixed the criterion on 2026-09-24, after the probes had run'); CLAIM.md:102 (Decision 7: otherwise disclose 'post hoc'); ARGUMENT.md:490-492

### [should_fix] hostile-referee — script slide 2 (script.md:14) and slide 15 (script.md:153-154)

*scope, confidence medium.* The script asserts that 'The platform's next state is fixed by both parties at once, and both read it' as a fact about platforms, and calls ride-hailing 'the obvious case'. No platform rule is modelled. A real matcher answers to many riders, drivers and prices, so whether it instantiates the control form with these two parties inside a whole is exactly the per-form question the argument leaves open. The slide-16 limits sentence mentions only workers ('no worker has been measured'), not platforms.

**Proposed:** Slide 15: 'Algorithmacy's form is the control. A platform has it when its next state is set by both parties at once and both read it. Whether a given platform does is a question about its rule, which we have not modelled.' Slide 16 limits: 'no worker has been measured and no platform's rule modelled.'

*Evidence:* CLAIM.md:90 ('That the lab shows any worker, platform or real rule is triadic. No such case is modelled.'); ARGUMENT.md:448 ('a platform counts only once its rule is modelled'), :469

### [should_fix] hostile-referee — script slide 15 concession (script.md:157-159); script slide 16 (script.md:163-164)

*logic, confidence medium.* After conceding that Simmel's arbitrator meets the criterion with no algorithm, the script says 'What is new is that this form now runs through ordinary work and ordinary life at scale.' That is stated as a finding, but it is a historical premise the lab does not show. Slide 16 then concludes 'algorithmacy has a target', not 'triadic coordination has a target'. A hostile listener can read the concession as removing the algorithm-specific content of the conclusion while the conclusion still names algorithmacy.

**Proposed:** Mark the premise: 'My historical premise, not a lab result, is that this form now runs through ordinary life at scale, and mostly through algorithms. That is why I use the name.' On slide 16 say: 'So coordination through a jointly determined third has a target of its own, and algorithmacy is the competence for it.'

*Evidence:* ARGUMENT.md:452 (P43: 'a historical premise. It is not a lab result'); CLAIM.md:33, :99 (Decision 4: 'the ontological argument covers triadic coordination')

### [should_fix] hostile-referee — deck slide 12 (deck.md:83), deck slide 15 (deck.md:102); script slide 12 (script.md:120-122)

*audience_comprehension, confidence medium.* The diagram 'A → M ← B' shows two arrows, and a non-specialist will read it as two pairs (A–M and B–M), which is exactly a composition of dyads. What makes it a triad is M's update rule, which takes both at once and cannot be split into a part answering to A and a part answering to B. The diagram also omits the return arrows (A′ = M, B′ = M) that make the system a whole, so the slide shows the fan-in and hides the 'whole' half of the criterion.

**Proposed:** Draw A ⇄ M ⇄ B (or add 'M → A, M → B'). In the script add: 'The two arrows into M are not two pairs. M's rule takes A and B together, and you cannot split it into a part that answers to A and a part that answers to B. That is what IIT's test checks.'

*Evidence:* org_frontier/thinkers/peirce/forms.py:37 (CONTROL); ARGUMENT.md:316 (P27)

### [should_fix] iit-specialist — Slide 14 (deck.md:97 'Joint determination without a whole'), script slide 13 (script.md:127-128 'Branches produced three-party facts')

*factual, confidence high.* The adicity/JD reader runs phi_structure on the full candidate system (pyphi.Subsystem over all units), whether or not that system is a complex. The majority triad has no complex at any reachable state, and all 78 branched one-input wirings have Φ = 0. Under IIT 4.0, distinctions belong to the Φ-structure of a complex, and a reducible candidate is not granted existence as one. An IIT specialist will therefore object that 'joint determination without a whole' and the branched 'three-party facts' are distinctions IIT does not count as existing. They are the lab's reading, not IIT's ontology. For scale, the same whole-system unfolding gives the majority a larger structure sum than the control, although the majority has no complex.

**Proposed:** When a Φ = 0 case is used, say how its distinctions were read, for example: 'reading the three units as a candidate system, which IIT itself would not count as a complex'. In script slide 13, say that the branched three-party facts all occur in systems with Φ = 0, i.e. in systems that are not wholes, which is also why the branch does not threaten slide 16.

*Evidence:* peirce/forms.py:100-104 (distinctions_at uses pyphi.Subsystem(net, state) on the whole system); ci/reproduce.json:83 ('branched wirings=78 ... Φ>0 in 0'); ci/reproduce.json:38 (core=()); albantakis2023information card, p. 18 ('overlapping substrates with lower φs are thus excluded from existence') and p. 29 (Φ is a sum within the structure of a complex); my run: maximal_complex for majority is NullPhiStructure at both 000 and 111.

### [should_fix] iit-specialist — Slide 12 (deck.md:84 'Φ = 2.0'), slides 8, 14; script slides 8, 12, 14

*factual, confidence high.* In IIT 4.0 notation, Φ ('big Phi') is structure integrated information: the sum of the φ of a complex's distinctions and relations. System irreducibility over the MIP is φ_s. The lab's number is φ_s (major_complex returns maximal_complex(...).phi, and ARGUMENT D2 calls it 'system integrated information over the minimum-information partition'). An IIT specialist reading 'Φ = 2.0' will take it as structure Φ, which for the control at state 111 is a different number. The talk also names 'IIT 4.0' as the instrument, while the numbers come from PyPhi's implementation, which uses the generalized intrinsic difference.

**Proposed:** Add one line under slide 12: 'Φ here = system integrated information φ_s (IIT 4.0), computed with PyPhi.' Alternatively write φ_s on slides 8, 12 and 14 and in the script. The expect strings do not change.

*Evidence:* albantakis2023information card: φ_s is Eq 21, Φ is Eq 59; p. 29 'Note that Φ is not computed based on a partition (as system phi)'; the card's Notes say the lab's numbers use PyPhi's GID. org_frontier/probes/lib.py:46-61; ARGUMENT.md:35. My run: control at (1,1,1) has φ_s = 2.000 but a PyPhi structure sum of 12.0 (unregistered; do not put it on a slide). pyphi.config.REPERTOIRE_DISTANCE = GENERALIZED_INTRINSIC_DIFFERENCE.

### [should_fix] iit-specialist — Slide 8 (deck.md:58-59), script slide 8 (script.md:79-81)

*logic, confidence high.* The script says 'Our lab tested a version of this' right after Simmel's distant third ('configurations of twos'). The majority triad is not a distant-third model: every member reads all three, so it is maximally coupled. It was built to test a different passage (the majority that overrides the individual), and the lab pre-registered Simmel's prediction that it would bind all three. That hypothesis was REFUTED. The talk turns a refuted Simmel prediction into support for Simmel's point. 'Three parties, and nothing binds them' also contradicts slide 14, which says the same form has a member jointly determined by the other two.

**Proposed:** Keep the Simmel quotation and the lab result, but do not call the model 'a version of' the distant third. Suggested wording: 'Simmel expected a majority of three to bind all three. We tested that, and the whole factors, at Φ = 0 with no core. Three parties are not enough even when every member reads every other.' Replace 'nothing binds them' with 'the three do not form a whole'.

*Evidence:* simmel/probe_simmel_majority.py:3-7 (question from Simmel 1902 II on the majority; 'Hypothesis. H3 (Simmel): majority_triad triadic, core {A,B,C}'); simmel/forms.py:51 (every rule maj(A,B,C)); simmel/FINDINGS.md:17 ('H3 | majority binds all three | REFUTED'); ci/reproduce.json:41; simmel1902number2 card p. 166 (distant third).

### [should_fix] iit-specialist — Slide 13 (deck.md:90), script slide 13 (script.md:130-131)

*audience_comprehension, confidence high.* 'Cause side never above 2' is followed by 'No element is ever jointly determined by two others.' The 2 counts the determined element plus its cause (|mechanism ∪ cause purview|). A non-specialist will hear 'never more than two causes', which would allow joint determination by two others. Joint determination is cause-side 3. As delivered, the number looks as if it contradicts the conclusion it supports.

**Proposed:** Say it outright, e.g. 'the cause-side count, which includes the element itself, never goes above 2: every element has one cause'. On the slide: 'cause side never above 2 (the element + one cause)'.

*Evidence:* peirce/forms.py:115-118 (adicity = |mechanism ∪ purview|); ci/reproduce.json:83 ('max cause-side adicity over all=2'); jd_methods.md in c7535bc (the cause-side count includes the mechanism).

### [should_fix] iit-specialist — Script slide 12 (script.md:119) and script slide 14 (script.md:139)

*scope, confidence high.* 'The criterion, fixed before our confirmatory runs' suggests the criterion was set before any results. The addendum says the criterion was chosen after the H1 results and fixed only on 2026-09-24. Its confirmatory run (the full JD3 run) has not finished; only fast JD1/JD2 results exist. 'We wrote that prediction down and published it before we ran it' refers to a pre-registration commit on an unmerged branch.

**Proposed:** Script 119: 'The criterion, which we chose after our first results and then fixed in a pre-registered addendum before testing it...'. Script 139: 'We pre-registered that prediction before running it' (and merge c7535bc before the talk). Do not call the addendum confirmatory until the full JD3 verdict is in.

*Evidence:* jd_hypotheses.md (c7535bc): 'First, the criterion was chosen after the results'; jd_methods.md: 'The JD3 verdict is printed by the full run alone'; `git merge-base --is-ancestor c7535bc HEAD` gives NOT_IN_HEAD.

### [should_fix] logician — Script slide 10 (script.md:101-102): 'Sergiy Koshkin makes the same point about pairing: it conceals the triad; it does not remove it.'

*citation, confidence high.* Koshkin's point is not the speaker's 'minting a new object / larger universe' point. His mechanism is the FOL devices themselves: an existentially quantified pair-element joined by three dyads, a triple junction that explicates to a teridentity. That mechanism is present even on a fixed domain, which is why his point supports the junction formulation and not the universe formulation. The evidence document also forbids resting the pairing point on Koshkin p.12, the domain-enlargement sentence. So calling it 'the same point' misattributes the talk's claim to Koshkin.

**Proposed:** 'Sergiy Koshkin makes a related point in logical terms: the pairing construction hides a three-way junction, which is to say a triad (2022, pp. 2, 7).' Do not say 'the same point'.

*Evidence:* koshkin2022reduction p.2: 'the pairing construction, as formalized in set theory, relies on the very FOL devices that are explicated as using triads'. p.7: the pair-element 'conceals triadicity in the same way as (4)', formula (5), a triple junction ∃t[R(1)(t,x1) ∧ R(2)(t,x2) ∧ R̂(t,x3)] (quine1954reduction card l.55). ARGUMENT.md:246: 'Do not cite Koshkin p.12 … for pairing'.

### [should_fix] logician — Script slide 11 (script.md:111-112): 'They disagree about which constructions are legitimate'

*logic, confidence high.* This line misdescribes Koshkin's side. Koshkin does not argue that some constructions are illegitimate. His 'invariant' formulation admits any first-order operation and explicates its branch points as pluridentities (teridentity). He argues that, under that explication, the verdict does not depend on which operations are allowed. The 'depends on which constructions are allowed' framing is Burch's side, and it is the gerrymandering charge Koshkin sets out to rebut. Putting both men inside Burch's frame misstates what the disagreement is about. The real dispute is whether the answer is resource-relative at all, and it turns on whether a junction counts as a triad.

**Proposed:** 'Burch says the answer depends on which constructions you allow. Koshkin says it does not: allow any construction, count each three-way junction as a triad, and the thesis comes out true. The split is over the status of the three-way junction.' Make the same fix in QA Q33 and ARGUMENT C4 ('disagree about which regime is privileged').

*Evidence:* koshkin2022reduction p.1 (abstract): traditional formulations 'that tie it to privileged relational operations … invite the charge of gerrymandering'. p.20: 'PRT is not gerrymandered, it is a deep fact … that can be neither manufactured nor undone by manipulating algebraic conventions.' Card l.18: 'Any first-order operation may be used, but its branch points and quantified places are explicated as bonding with pluridentities'. Card l.48: the register's reading of Koshkin as holding that the thesis is setting-dependent 'inverts its conclusion'.

### [should_fix] logician — Script slide 9 (script.md:84): 'Now the reply that made most philosophers stop believing Peirce.'

*factual, confidence high.* The line makes two overclaims. (1) 'Most philosophers' goes beyond the only source. Burch says the thesis was 'doubted by many'. (2) Calling Löwenheim/Kalmár/Quine 'the reply' casts them as answering Peirce. Löwenheim cites Schröder, not Peirce. Kalmár works on the decision problem. Quine frames his result against Kalmár and Church–Craig–Quine and does not name Peirce. The script itself says so eight lines later ('The reading of Quine as a refutation of Peirce came from others'), and CLAIM.md forbids saying Quine aimed the paper at Peirce. The opening sentence contradicts both.

**Proposed:** 'Now the result that led many philosophers to doubt Peirce, though none of its authors aimed it at him.'

*Evidence:* burch2021sep §14: 'was for over a century doubted by many, especially after the publication of a proof by Willard Van Orman Quine'. lowenheim1915moglichkeiten card l.25-26 ('does not mention Peirce … cites Schröder'). quine1954reduction n.1. CLAIM.md:39.

### [should_fix] logician — Slide 9 headline (deck.md:62-63) 'One dyadic predicate for everything' over 'Löwenheim 1915 · Kalmár 1936 · Quine 1954'; script slide 9 (script.md:86-87) 'any theory'

*factual, confidence high.* 'One dyadic predicate' is Quine's result, and Kalmár's in the satisfiability sense. It is not Löwenheim's. Löwenheim reduces the higher calculus to the binary calculus using several binary relatives: the coded relative A plus V and H, which pick out a pair's members. Herbrand then sharpened this to three binary predicates, and Kalmár to one. 'For everything' and 'any theory' also drop Quine's scope: an interpreted theory 'formulated in the notation of quantification theory', i.e. first-order. Kalmár's result is equisatisfiability for the decision problem. It is not a translation of theories, and Quine draws exactly that distinction in his n.1.

**Proposed:** Headline: 'Dyadic predicates suffice'. Or keep 'one dyadic predicate' and attribute it to Kalmár and Quine only: 'Löwenheim 1915: binary relatives suffice · Kalmár 1936: one, for satisfiability · Quine 1954: one, for any first-order theory'. In the script, say 'any first-order theory'.

*Evidence:* lowenheim1915moglichkeiten card l.22-24 (A, V, H). kalmar1936zurueckfuehrung p.137 (Herbrand: 'drei binäre … Funktionsvariable'), p.138 III and n.7 ('gleichwertig' = both satisfiable or both unsatisfiable). quine1954reduction p.180 opening.

### [should_fix] logician — Script slide 3 (script.md:30-31): 'He did not prove it. … The proof came later, and it came as arithmetic.'

*factual, confidence high.* These lines present Peirce's valency arithmetic (1890s) as the proof of the thesis. CLAIM.md forbids saying Peirce proved it. The arithmetic is an argument that holds only if a three-way junction counts as a relation, which is what slides 4-5 go on to say. It is not a proof, and Herzberger shows it collapses under standard definability. The proofs came from Herzberger 1981, Burch 1991 and Hereth Correia & Pöschel 2006, under stated conditions. Hereth Correia & Pöschel note that no published proof by Peirce has been found.

**Proposed:** 'The argument came later, and it came as arithmetic. The proofs came a century after that.'

*Evidence:* CLAIM.md:38 ('That Peirce "proved" the thesis … He argued it.'). herethcorreia2006teridentity p.2: 'According to Herzberger … Peirce mentioned he found a proof, but no corresponding publication has been found' and 'Many attempts have failed for non-obvious reasons.' herzberger1981theorem T11.

### [should_fix] logician — Script slide 3 (script.md:27-28): 'every relation among more than two, he said, can be built from relations among three'

*factual, confidence high.* This misstates the positive clause by one. Peirce says a conjugative with more than two correlates, i.e. a relation with more than three places, reduces to conjugatives of two correlates, i.e. triads. 'Among more than two' includes triads themselves, which makes the clause trivial. It also clashes with the script's own gloss one line earlier, which correctly calls a conjugative 'a relation among three or more'.

**Proposed:** 'And every relation among more than three, he said, can be built from relations among three.'

*Evidence:* peirce1870description p.374 (CP 3.144): 'a conjugative having more than two correlates can always be reduced to a combination of conjugatives of two correlates'. Card l.18 (conjugative of two correlates = triadic relative).

### [should_fix] logician — Script slide 11 (script.md:105-106): 'Robert Burch built a whole algebra in which it holds.'

*citation, confidence high.* The line leaves out the restriction that matters on a slide about constructive resources. Burch's proof worked only with juxtaposition allowed 'only as last or before last operation'. Hereth Correia & Pöschel say his proofs 'do not hold anymore' once the restriction is dropped. Koshkin says 'the shadow of gerrymander still looms over it'. The book is also metadata-only, so the talk has not read it and cannot state its contents on its own authority. ARGUMENT P20 and QA Q29 already carry the restriction; the spoken line drops it.

**Proposed:** 'Robert Burch built an algebra, PAL, and proved the thesis in it, but only with a restriction on when products may be formed. Hereth Correia and Pöschel removed that restriction and gave the strongest proofs.' 'Strongest' is fair for the 2006 Theorem 2: no restriction, negation allowed, any |A| ≥ 2.

*Evidence:* herethcorreia2006teridentity p.2. herethcorreia2004power p.2 ('the proofs Burch is providing for Peirce's thesis do not hold anymore'). koshkin2022reduction p.8. burch1991reduction card (verified: metadata-only). ARGUMENT.md P20 (l.260).

### [should_fix] mechanical — script slide 14 (script.md:139); script slide 12 (script.md:119)

*logic, confidence high.* "We wrote that prediction down and published it before we ran it" overstates the record: the pre-registration is a commit on an unmerged branch. "The criterion, fixed before our confirmatory runs" will be heard as covering the evidence on slides 12–14. The criterion was in fact chosen after all the registered results, and the addendum itself says so. The confirmatory JD3 runs are not registered.

**Proposed:** Slide 12: "We chose this criterion after the results you'll see, and then pre-registered a test of it on new cases." Slide 14: "We pre-registered that prediction before running it", and only once the addendum is merged and registered.

*Evidence:* jd_hypotheses.md on probe/peirce-joint-determination: "the criterion was chosen after the results"; JD1 is "a consistency check … not a test of a new claim". The branch is NOT_MERGED.

### [should_fix] mechanical — script slide 5 (script.md:53-54)

*citation, confidence high.* "Kempe's extra unit, he said, is itself the triad" attributes to Peirce 1892 a claim the card identifies as the lab's gloss. In 1892 Peirce put mediation in "the attachment of lines to spots". He said the diagram fails to represent how the abstraction 'this action' is derived. He did not say the unit is the triad.

**Proposed:** "Kempe's extra unit and its three attachments, he replied, are themselves the mediation, and the diagram cannot show how that unit was minted."

*Evidence:* peirce1892critic.md Notes l.34 (corrects paper.md's "the junction is the triad" and gives the supported version). Loci CP 3.423 ("the attachment of lines to spots, that of mediation") and CP 3.424.

### [should_fix] mechanical — script slide 6 (script.md:58-59)

*citation, confidence high.* The book-down, picked-up example is CP 8.331 (1904), where Peirce calls it "a degenerate form of Thirdness in which the thirdness is externally appended". The quoted phrase "merely one dyadic relation followed by another" is from CP 1.345 (1903), whose example is A throwing B away and it accidentally hitting C. "In his words" joins one text's phrase to the other's example.

**Proposed:** Either use CP 1.345's own example ("If A throws B away and it happens to hit C, that is, in his words, 'merely one dyadic relation followed by another'"), or keep the book example and quote 8.331: "a degenerate form of Thirdness in which the thirdness is externally appended".

*Evidence:* peirce1931papers CP 1.345 (vol.1 p.176). peirce1904letter CP 8.331 loci ("A's laying down the B which C subsequently picks up … externally appended").

### [should_fix] mechanical — deck slide 2 (deck.md:15); script slide 2 (script.md:13-14)

*logic, confidence medium.* Algorithmacy is defined as "a third that both parties determine", without the locked clause "which acts back on both, in a system that does not factor". On that definition Simmel's majority qualifies (a member jointly determined by two others), yet slide 14 says the majority is not a triad. The opening definition is looser than the criterion on slide 12, so the conclusion on slide 16 ('joint determination in a whole') is not what slide 2 set up.

**Proposed:** Deck: "Algorithmacy: a third that both parties determine, and that acts back on both." Script: add "…and which acts back on both, so the three form one system."

*Evidence:* CLAIM.md:17. Deck slide 12 (deck.md:81) and slide 14 (deck.md:97).

### [should_fix] mechanical — script slide 8 (script.md:79-81) vs script slide 14 (script.md:138-139)

*audience_comprehension, confidence high.* Slide 8 says of the majority: "Three parties, and nothing binds them", and calls this "the clue to what a genuine triad is". Slide 14 then says the majority's members are jointly determined by the other two. A listener will hear a contradiction, because 'binds' is used in the lab's wholeness sense and never glossed.

**Proposed:** Slide 8: "Three parties, and they do not form one system: Φ is zero." Slide 14: tie back explicitly: "the majority we met earlier, which is not one system, still has a member fixed by the other two."

*Evidence:* ci/reproduce.json thinkers-simmel-h3-majority: "H3 (majority triad binds all three): REFUTED" (wholeness). JD2 fast result: C jointly determined.

### [should_fix] mechanical — script slide 8 (script.md:79-80); deck slide 8 (deck.md:59)

*audience_comprehension, confidence high.* Φ and "core" are used for the lab result on slide 8, but IIT is not introduced until slide 12. A non-specialist cannot read "Φ = 0, no core" at that point.

**Proposed:** Add one clause on slide 8: "using a measure, Φ, of whether a system is one thing or splits into parts, which I'll explain shortly: Φ is zero." Or move the lab line to slide 14.

*Evidence:* script.md:116-117 is the first mention of integrated information theory.

### [should_fix] mechanical — script slide 13 (script.md:131-132); deck slide 13 (deck.md:90)

*audience_comprehension, confidence medium.* "The cause side never goes above 2. No element is ever jointly determined by two others" reads as a contradiction unless the listener knows that adicity counts the element itself. Two is the element plus one cause, but it sounds like 'up to two causes'.

**Proposed:** "On the cause side a fact never spans more than two parties, the element and its one source, so no element is ever jointly determined by two others."

*Evidence:* forms.py genuine_adicity: ad_c = |mechanism ∪ cause purview|.

### [should_fix] mechanical — script slide 5 (script.md:46-50); deck slide 5 (deck.md:37-39)

*logic, confidence medium.* The script presents the node premise with its 1897 quotation, then says "In 1886 Alfred Kempe attacked exactly there". Kempe cannot have attacked a premise Peirce put in print eleven years later, partly in reply to him. The order implies a sequence that did not happen.

**Proposed:** "In 1886 Alfred Kempe challenged the negative clause… Peirce's answer, stated fully in 1897, is that the junction is itself a relation: 'every node of bonds is equivalent to a relative'."

*Evidence:* peirce1897logic pp.170-171 (node passage) and p.168 (Peirce's charge against Kempe, same §4). kempe1886memoir: "first serious challenge to Peirce's negative clause".

### [should_fix] peirce-scholar — script slide 6 (script.md:58-60)

*citation, confidence high.* The script joins an example from one text to a verdict from another. The book put down and picked up is CP 8.331 (1904 Welby letter: "A's laying down the B which C subsequently picks up"). There Peirce calls it "a degenerate form of Thirdness in which the thirdness is externally appended", and in the same paragraph he says even the most degenerate Thirdness contains "something ... which is not mere secondness". The phrase "merely one dyadic relation followed by another" is CP 1.345 (1903), where it describes a different case: A throwing B away and B accidentally hitting C. "In his words" therefore attaches to the lay-down case a verdict that Peirce's own text for that case contradicts.

**Proposed:** Keep each example with its own source. Either: "If A throws the book away and it happens to hit C, you have, in his words, 'merely one dyadic relation followed by another' (CP 1.345)." Or keep the book put down and picked up and quote CP 8.331: "a degenerate form of Thirdness in which the thirdness is externally appended." Deck slide 6 can stay as it is, because it cites CP 1.345 for the phrase without the lay-down example.

*Evidence:* peirce1904letter.md Loci l.24-25, l.28 (CP 8.331); peirce1931papers.md l.21-22 (CP 1.345, vol.1 p.176); ARGUMENT.md P7 l.126-132, which keeps the two cases apart correctly

### [should_fix] peirce-scholar — script slide 3 (script.md:27-28)

*factual, confidence high.* "And every relation among more than two, he said, can be built from relations among three" mistranslates the positive clause. Peirce's words are "a conjugative having more than two correlates". A relative's correlates do not include its relate, so a conjugative with more than two correlates has four or more places. Read literally, "a relation among more than two" includes triads, which makes the clause trivial and garbles the positive half of the thesis the slide claims to state.

**Proposed:** "And every relation among four or more, he said, can be built from relations among three."

*Evidence:* peirce1870description.md l.18 ("every relative of more than three places reduces to triads") and Locus p.374 (CP 3.144); 1870 text, jstor-25058006 p.374

### [should_fix] peirce-scholar — deck slide 3 (deck.md:22); script slide 3 (script.md:30-31)

*logic, confidence medium.* The script offers "I have, however, studied this part of my notation but little" as Peirce admitting that he had not proved the thesis. On the page, the sentence comes before the thesis sentence and concerns the notation for conjugative terms. The full text is "The treatment of conjugative terms presents considerable difficulty, and would no doubt be greatly facilitated by algebraic devices. I have, however, studied this part of my notation but little." It concedes that the notation is underdeveloped. It concedes nothing about the reduction claim. That the claim goes without argument is true, but it is an observation about the memoir, not something Peirce admits.

**Proposed:** Keep the two points apart: "He gave no argument for it. The section opens by conceding that his notation for these terms is undeveloped: 'I have, however, studied this part of my notation but little.'" Or drop the quotation and say "he asserted it without argument."

*Evidence:* peirce1870description.md Locus l.24; 1870 page image text p.374 (jstor-25058006.txt: the 'Conjugative Terms' heading, then the difficulty and 'studied ... but little' sentences, then 'A relative term cannot possibly be reduced ...')

### [should_fix] peirce-scholar — deck slide 14 (deck.md:95); script slide 14 (script.md:137); set up at script slide 6 (script.md:62)

*audience_comprehension, confidence high.* Slide 6 tells the audience that the imitation of giving is "one dyadic relation followed by another", which is a chain, and that "we will meet both again as models". Slide 14 then says the imitation of giving is a whole at Φ = 2.0. In the lab's framing a chain factors (the Boolean chain reads Φ_MIP = 0, ARGUMENT P40), so the audience will hear a contradiction. The registered model giving_degenerate (G′=¬R, T′=G, R′=T) is a ring. It gets its wholeness from the return, not from anything in Peirce's example, and neither of Peirce's two imitation cases has that return.

**Proposed:** On slide 14, say "our model of the imitation closes the handings into a ring, and the ring, not any three-party fact, makes it a whole." On slide 6, soften "we will meet both again" to "we will meet a model of each".

*Evidence:* ARGUMENT.md P31 l.362-373 ("a ring ... The imitation of giving gets its wholeness from the return"); reproduce.json thinkers-peirce-h3-giving (giving_degenerate Φ_MIP=2.000000, adicity 2); ARGUMENT.md P40 l.436

### [should_fix] peirce-scholar — script slide 15 (script.md:149-151); deck slide 15 (deck.md:103)

*factual, confidence medium.* "The sign triad sits inside one reader" misdescribes Peirce's sign. On Peirce's account the triad is a relation among a sign (here the text, outside the reader), its object (outside the reader) and an interpretant. Semiosis is "a coöperation of three subjects" (CP 5.484), and the Sign is "a First" standing to "a Second, called its Object" (CP 2.274). Only the interpretant is on the reader's side (CP 2.228: "creates in the mind of that person an equivalent sign"). A Peirce scholar will object that the triad is not located in a mind. The locked point (the triad closes in one reader's interpretant and determines nothing on the other party's side) does not need the "inside" wording. The next sentence, "It binds the text, what the text is about and one reader's interpretation", already states it correctly.

**Proposed:** "But the sign triad closes in one reader. It binds the text, what the text is about and one reader's interpretant, and it determines nothing on the other person's side." This keeps the locked claim and matches ARGUMENT P41.

*Evidence:* peirce1931papers.md l.28, l.30, l.33 (CP 2.274, 2.228, 5.484, page images); ARGUMENT.md P41 l.444 ("binds a text, its object and one reader's interpretant"); CLAIM.md:32

### [should_fix] peirce-scholar — script slide 14 (script.md:137) → script slide 15 (script.md:149-151)

*audience_comprehension, confidence medium.* Slide 14 names "Peirce's sign with a working interpreter" as a case of joint determination in a whole, which is a triad by the talk's own criterion. One slide later the talk grants that every sign is triadic and says reading is nonetheless a chain. A listener will ask: if your model of Peirce's sign passes the triad test, why doesn't reading? The missing link is that the passing model (sign_pragmatic) has interpretation act back on the object (O′ = I), while the model that fits reading is the exogenous-object sign, which factors (Φ_MIP = 0). Calling sign_pragmatic "Peirce's sign" also presents the lab's rendering as Peirce's. ARGUMENT P41 warns that the models illustrate and are not evidence about Peirce's text.

**Proposed:** On slide 14, say "our model of a sign whose interpretation acts back on its object" and not "Peirce's sign with a working interpreter". On slide 15, add one sentence: "When the reading acts back on nothing, as with a finished text, our model of the sign factors. The triad is real, but it is the reader's."

*Evidence:* ARGUMENT.md P32 l.379-383 (sign_exogenous Φ_MIP=0), P33 l.388 and l.394 (sign_pragmatic, O′ = I), P41 l.444; reproduce.json thinkers-peirce-h4-sign

### [should_fix] simmel-sociologist — Script slide 8 (script.md:80) vs slide 14 (deck.md:97; script.md:138-141)

*logic, confidence high.* Slide 8 says the same model has 'nothing' binding it, and slide 14 says it has joint determination. The script tells the audience that in the majority triad 'Three parties, and nothing binds them' and that it is the clue to what a triad is. Slide 14 then says 'Simmel's majority has members jointly determined by the other two', which is the first clause of the talk's own triad criterion (JD2: C's cause purview is {A, B}, φ = 0.5). The audience gets two incompatible descriptions of one model. Slide 8 says the lesson is that three is not enough. Slide 14 says the lesson is that joint determination without a whole is not enough.

**Proposed:** Replace 'nothing binds them' with 'the whole does not bind: Φ is zero, and no subset forms a core'. Slide 14 then says 'each member is still jointly determined by the other two, so what the majority lacks is the whole, not the three-way fact'. Or drop the majority from slide 8 entirely and introduce it only on slide 14.

*Evidence:* deck.md:59, 97; script.md:79-81, 138-139; probe/peirce-joint-determination:org_frontier/thinkers/peirce/jd_hypotheses.md:38-48 (JD2); task brief fast result (C jointly determined by A and B, Φ_MIP = 0).

### [should_fix] simmel-sociologist — Slide 8 line 1 (deck.md:58) and script slide 8 (script.md:75-77)

*audience_comprehension, confidence high.* The gloss 'a third who stays distant from the other two leaves configurations of twos' drops what Simmel's distant third is. The talk's own card locus opens with 'This society-constructing mediation of a third element is… to be treated in a later connection. For the third element has here such a distance…'. The distant third is an outside power that unifies the two, as in the 1908 examples: an alliance against a common enemy, believers joined by one God. It does not leave them unbound. The 'configurations of two' are (i) the relation among those who join and (ii) the relation between the joined pair, taken as a unit, and that centre of interest. The talk implies an aloof third who adds nothing, and the script's next line ('nothing binds them') reinforces that. Both invert Simmel's case.

**Proposed:** Say: 'Simmel set aside a third so distant that it unites the two only as a pair facing it; there he finds "configurations of twos", not a group of three.' If the author wants the examples (common enemy, one God), card the sentence before the p.166 locus (Small II:166 / 1908 p.103) first. The case also fits the talk's taxonomy well: a common reference point that both parties relate to but do not jointly determine.

*Evidence:* simmel1902number2.md:29 (p.166 locus begins 'This society-constructing mediation'); simmel1908soziologie.md:23-24 (p.103, 'gesellschaftsbildende Vermittlung'); the full p.103 German with the common-enemy and one-God examples is at submissions/slacker_thirds/old/archive/v4/verification/couch/results_p1_simmel_deferred.md:27-31 (not yet on a triadic_reduction card).

### [should_fix] simmel-sociologist — Slide 7 diagram (deck.md:51-53)

*factual, confidence high.* The diagram 'A — C — B' draws only the broken line and leaves out the straight one. Simmel's point is that the broken line is added 'apart from the bond by the straight and shortest line' (and 'added to the immediate relationship'), and that 'each pair of elements' gains one, not only A–B. As drawn, Simmel's triad is a chain, which is the form slide 15 assigns to literacy ('writer → text → reader — a chain'). The script (l.68, 'connected directly and also through C') is right, so slide and speech disagree. The same slip, a broken line with the direct tie cut, sits behind QA.md Q17 ('Simmel's broken line has exactly the control's rules') and ARGUMENT P14. The lab's triad_broken_line model removes the A–B tie that Simmel keeps.

**Proposed:** Draw a triangle, with the straight line A — B above and the route A — C — B below. Or add the caption 'A — B directly, and also A — C — B, for every pair'. In QA Q17 and ARGUMENT P14, say that the lab's broken-line model is the control with the direct tie removed, not Simmel's broken line.

*Evidence:* simmel1902number1.md:26-27 (p.45); simmel/forms.py:37 (TRIAD_BROKEN_LINE: A′=C, B′=C, no A–B term); talk/QA.md:137; ARGUMENT.md:198.

### [should_fix] simmel-sociologist — Slide 15 line 4 (deck.md:104) and script slide 15 (script.md:153-159)

*logic, confidence high.* The arbitrator concession overclaims, for three reasons. First, 'Simmel's arbitrator has exactly this form' is true only by construction. The lab wrote its arbitrator model with the control's rules (forms.py l.56 is identical to l.30), so this is a modelling choice, not a finding about Simmel. Second, the lab's mediator has the same M rule (M′ = A ∧ B), reads Φ = 2.0 with core {A, M, B}, and is pre-registered in JD2 to show joint determination in a whole. So on the lab's own models Simmel's mediator meets the criterion too, and FINDINGS says the model does not reproduce Simmel's mediator/arbitrator distinction (H4 PARTIAL: 'the mediator binds exactly as much as the arbitrator'). Third, the concession follows the line 'turns on the other party she cannot see'. Simmel's arbitration parties are 'colliding' elements who face each other, since the straight line stays in every triad. The claim fits the criterion, not the full form the script has just described.

**Proposed:** Slide: 'The target is older than AI: Simmel's arbitrator meets the same criterion.' Script: 'Simmel's arbitrator, and on our Boolean rendering his mediator too, meets this criterion: a third fixed by both parties that both then follow. There is no algorithm in it.' Drop 'exactly'. Be ready for the Q&A point that the criterion does not separate Simmel's mediator from his arbitrator.

*Evidence:* simmel/forms.py:30, 56-57; ci/reproduce.json thinkers-simmel-h4-nonpartisan (arbitrator and mediator both 'Φ_MIP=2.000000  core=('A', 'M', 'B')'); FINDINGS.md:7, 18; jd_hypotheses.md:41-43 (branch); simmel1902number2.md:31-32 (pp.167-69: mediator vs arbitrator 'takes a decided position on one side'); CLAIM.md:33 (licenses 'meets the same criterion', not 'exactly this form').

### [should_fix] simmel-sociologist — Slide 14 line 3 (deck.md:97) and script slide 14 (script.md:138-141)

*number, confidence high.* At the pinned commit, the claim that the majority has members jointly determined in a system that factors, and so 'come apart in both directions', is not in ci/reproduce.json or NUMBERS.md. Only 'majority_triad … Φ_MIP=0.000000 core=()' is registered. The JD addendum is pre-registered (commit c7535bc on origin/probe/peirce-joint-determination, 2026-09-24) and its fast results support JD2, but it has not landed. CLAIM.md bars the 'both ways' crossing on unregistered evidence, and decision 6 says slide 14 claims one direction only until it is registered. 'We wrote that prediction down and published it before we ran it' holds only if c7535bc was pushed before the run. It should cite the pre-registration.

**Proposed:** Before the talk, merge the JD addendum and register its JD2 expect lines (majority: jd true, Φ_MIP = 0) in ci/reproduce.json and NUMBERS.md. Until then, cut slide 14 line 3 and the 'both directions' sentence, or say 'pre-registered; result pending registration'. Keep the published-before-run sentence only once the push timestamp is confirmed to predate the run.

*Evidence:* ci/reproduce.json:35-45 (no cause-purview line for majority_triad); talk/NUMBERS.md:12; CLAIM.md:74, 101; git show probe/peirce-joint-determination:org_frontier/thinkers/peirce/jd_hypotheses.md:38-48.

### [minor] algocon-audience — deck slide 3 (deck.md:18-22) / script slide 3 (script.md:24-28)

*audience_comprehension, confidence high.* The headline reads 'Peirce states both clauses in 1870', but the slide quotes only the negative clause, and the script leads into it with a third clause ('A relative term cannot be reduced to absolute terms'). A listener cannot tell which two clauses are meant. The positive clause (every higher relation from triads) is only spoken.

**Proposed:** Put both clauses on the slide as two labelled lines, e.g. 'No: triads from pairs' and 'Yes: every larger relation from triads', with the 3.144 quotation beneath. Or change the headline to 'Peirce states the thesis in 1870'.

*Evidence:* deck.md:20; peirce1870description.md:18 (the sentence holds three reductions: monads→dyads, dyads→triads, and the positive clause).

### [minor] algocon-audience — script slide 12 (script.md:115-116)

*logic, confidence high.* 'A tuple doesn't say whether one thing fans out to three, or three things fix one' miscounts the junction. At a three-way junction, one party fans out to two, or two parties fix one. 'Fans out to three' describes a four-way node and blurs the fan-in point (two determine one) that the criterion rests on.

**Proposed:** 'A tuple doesn't say whether one thing fans out to the other two, or two things jointly fix the third.'

*Evidence:* deck.md:83 (A → M ← B: two fix one); ARGUMENT.md:411-412 (fan-in: 'one element determined by two').

### [minor] algocon-audience — script slide 16 (script.md:172-173)

*logic, confidence medium.* The script states the grain objection as 'whether M counts as one party is a choice'. The documented objection and the open test concern the other units. Merge A and B, or re-encode the parties as a pair, and M becomes a one-input element. As phrased, the audience hears an objection about the mediator's unity, which is not what the exclusion test would examine.

**Proposed:** '…you have moved the argument from operations to units: treat A and B as one unit, and M answers to a single input again. Whether they count as two is a choice. IIT's exclusion test is designed to make that choice, and running it on this form is our next step.'

*Evidence:* ARGUMENT.md:482-484 (weakest link 1: 'Merge two parties into one element and the control's M becomes a one-input element'; open test on 'a paired re-encoding of the control'); CLAIM.md:103 (Decision 8).

### [minor] algocon-audience — script slide 11 (script.md:105)

*citation, confidence high.* 'I am relying on Koshkin's account of that paper' misdescribes the source. The Herzberger card rests on search-inside snippets of Herzberger's own text, matched across two scans, plus Conarroe, not on Koshkin.

**Proposed:** 'I have read that chapter only in excerpts.'

*Evidence:* herzberger1981theorem.md source_basis and Loci (T7–T11 matched in two OCR scans); ARGUMENT.md:258.

### [minor] algocon-audience — script slide 14 (script.md:136)

*audience_comprehension, confidence high.* While slide 14 is on screen, the script says 'The next slide is where the instrument earns its keep', which points the audience to a slide that is not coming.

**Proposed:** 'This slide is where…' or 'Here is where…'.

*Evidence:* script.md:136, section heading 'Slide 14'.

### [minor] algocon-audience — script slides 10–11 (script.md:101-112)

*audience_comprehension, confidence medium.* Slide 10 ends on the speaker's own verdict ('This slide is my argument, not a consensus'). Slide 11 then returns to the history ('The logicians after Quine…'). The audience hears the resolution before the debate it resolves, then the debate, then the lab's move. Slide 11's closing point, that the constructions split on the three-way junction, is the setup slide 10 needs.

**Proposed:** Swap slides 10 and 11: debate (Burch vs Koshkin, splitting on the junction), then 'every reduction mints a third' as the speaker's reading, then slide 12's 'give the junction a direction'. Alternatively, open slide 11 with a backward hook: 'Logicians who accept every one of these theorems still disagree, and here is why.'

*Evidence:* script.md:101-102, 105.

### [minor] algocon-audience — deck slide 2 (deck.md:14-15)

*logic, confidence medium.* The slide equates each competence with its object: 'Literacy: a medium that answers to one party at a time. Algorithmacy: a third that both parties determine.' The locked thesis and the script say the competences answer to different forms of coordination. Read alone, the slide says literacy is a medium.

**Proposed:** 'Literacy answers to a medium that answers to one party at a time.' / 'Algorithmacy answers to a third that both parties determine.'

*Evidence:* CLAIM.md:15-17; script.md:12-13 ('Literacy is a competence for working with a medium…').

### [minor] algocon-audience — script slide 13 (script.md:132-133) and slide 16 (script.md:162-163)

*logic, confidence medium.* Slide 13 calls the cause-side ceiling 'close to true by construction… a calibration, not a discovery'. Slide 16 then uses the same ceiling as the first premise of the conclusion. A careful listener will ask what the lab contributed to that premise. The talk should say where the evidential weight actually falls. The ceiling was enumerated only for n ≤ 4, only for copies without negation or self-reads, and was argued beyond that.

**Proposed:** On slide 16, add: 'The first premise holds by construction: a one-input link has one cause. The lab's evidence is for the second premise, that joint determination inside a whole exists, and for the split that shows where the old argument's branch went.'

*Evidence:* ARGUMENT.md:353-359 (P30: near-definitional; 'The enumeration covers only n ≤ 4… an argument and not a computation'); ARGUMENT.md:326 ('no negation and no self-reads').

### [minor] algocon-audience — deck slide 7 (deck.md:51-53) / script slide 7 (script.md:67-68)

*audience_comprehension, confidence high.* The script says 'A and B are now connected directly and also through C', but the slide's diagram 'A — C — B' shows only the indirect route and has no direct A–B tie. Viewers see a chain, which is the form the talk later assigns to literacy.

**Proposed:** Draw a triangle, or two routes: 'A ——— B' above 'A — C — B'.

*Evidence:* deck.md:52; ARGUMENT.md:159 (P9: 'A reaches B directly and also through C').

### [minor] hostile-referee — script slide 9 (script.md:84)

*citation, confidence high.* 'Now the reply that made most philosophers stop believing Peirce. In 1915 Leopold Löwenheim …' has two problems. It casts Löwenheim as replying to Peirce, but Löwenheim cites Schröder, not Peirce. It also overstates the source: Burch says the thesis was 'doubted by many, especially after' Quine's proof, not that 'most philosophers' stopped believing it.

**Proposed:** 'Now the line of results that led many to doubt Peirce, as Burch puts it. In 1915 Leopold Löwenheim, working in Schröder's algebra, showed …'

*Evidence:* ARGUMENT.md:213 (P15: 'He cites Schröder, not Peirce'); burch2021sep card §14 ('was for over a century doubted by many, especially after the publication of a proof by … Quine')

### [minor] hostile-referee — script slide 11 (script.md:105)

*citation, confidence high.* 'I am relying on Koshkin's account of that paper' gives the wrong provenance for Herzberger. The card's T7-T11 wording was matched in search-inside snippets from two scans, with page numbers from Conarroe 2020. It was not taken from Koshkin, whom the card uses only for the end page and the 'triple junction' term.

**Proposed:** 'I have read that chapter only in fragments, through search of two scans and Conarroe's citations.' Or drop the hedge and cite by theorem number, T9 and T11.

*Evidence:* herzberger1981theorem card, source_basis and Loci

### [minor] hostile-referee — script slide 5 (script.md:50, :53-54)

*citation, confidence medium.* 'In 1886 Alfred Kempe attacked exactly there' gives Kempe an aim the card does not record. It was Peirce who read the memoir as 'a formidable objection to my views'. 'Kempe's extra unit, he said, is itself the triad' puts an unquoted gloss in Peirce's mouth. His recorded rejoinder is that mediation lies in 'the attachment of lines to spots', and that the diagram does not show how the abstraction 'this action' is derived.

**Proposed:** 'In 1886 Alfred Kempe published a construction that Peirce called "a formidable objection to my views".' And: 'His reply was that the unit and its three attachments are themselves the mediation, minted by an abstraction the diagram does not represent.'

*Evidence:* peirce1892critic card CP 3.423-424 loci and Notes ('A version the sources support: … the spot and its three attachments are themselves the mediation'); kempe1886memoir card

### [minor] hostile-referee — script slide 15 (script.md:146-147)

*scope, confidence high.* 'Even a long correspondence only loops that chain into a ring, and a ring is a whole with no triad in it' states as a lab fact what ARGUMENT marks as an analogy. The lab modelled no correspondence. The claim holds for the lab's copy ring (copy_BCA) and the mutual dyad.

**Proposed:** 'Even a long correspondence only loops that chain into a ring, the shape of our ring of copies, which is a whole with no triad in it.'

*Evidence:* ARGUMENT.md:439 ('This is the talk's analogy; the lab modelled no correspondence'); ci/reproduce.json:78 (copy_BCA)

### [minor] iit-specialist — Script slide 12 (script.md:117-122)

*audience_comprehension, confidence medium.* The talk never says what Φ or 'core' mean, or what 2.0 is on. A non-specialist cannot tell why 2.0 means 'whole' or why the imitation of giving also scores 2.0 on slide 14. Nothing overclaims about consciousness. But much of the audience knows IIT only as a theory of consciousness, and the talk never says it uses only IIT's causal mathematics.

**Proposed:** Add a one-sentence gloss: 'Φ measures how much the least damaging cut through the system destroys its causal power; zero means it falls apart into independent pieces. The core is the largest set of units that holds together this way.' Also add: 'IIT is a theory of consciousness; we use only its causal calculus and claim nothing about experience.'

*Evidence:* script.md:116-122 (first use of Φ and 'core', no gloss); ARGUMENT.md:35 (D2 has the definitions but the script does not voice them).

### [minor] iit-specialist — Slide 14 (deck.md:95) and NUMBERS.md row '2.0'

*number, confidence high.* All three numbers on slide 14 are correct and registered (mutual dyad, copy ring and imitation of giving at Φ = 2.0). NUMBERS.md, however, ties '2.0' only to the control's expect string, so check_talk.py passes slide 14's 2.0 by coincidence. It does not check the forms the slide names.

**Proposed:** Add NUMBERS.md rows mapping slide 14's 2.0 to thinkers-simmel-h1-superindividual (dyad_mutual), thinkers-peirce-h1-irreducibility (copy_BCA) and thinkers-peirce-h3-giving (giving_degenerate).

*Evidence:* ci/reproduce.json:9 (dyad_mutual Φ_MIP=2.000000), :78 (copy_BCA Φ_MIP=2.000000), :107 (giving_degenerate Φ_MIP=2.000000); NUMBERS.md row 1.

### [minor] logician — Script slide 11 (script.md:111): 'Both sides accept the same theorems.'

*logic, confidence medium.* This is fair only in a narrow sense. Burch and Koshkin both accept Quine's theorem as technically correct and both accept the PAL irreducibility theorems. Beyond that, the talk has no evidence. The SEP entry (wording unchanged since 2014) predates Koshkin 2022/2024/2025, and the talk has no source for Burch's view of Koshkin's results. The literature also holds one unresolved theorem-level conflict: Hereth Correia & Pöschel 2004 Thm 13(b) (positive PAL = Rel(A) for finite A) fails for |A| = 2 by Koshkin 2025 Thm 4, and neither side flags it. 'The same theorems' is therefore broader than the evidence.

**Proposed:** 'Neither disputes the other's mathematics: both grant that Quine's construction works and that the PAL proofs hold.'

*Evidence:* burch2021sep §14 ('both Peirce and Quine were correct'). koshkin2022reduction p.4 (Quine 'correct in a technical algebraic sense'). burch2021sep card l.11 (the wording already stood in 2014). herethcorreia2004power card l.53, l.61 (Thm 13(b) conflict with koshkin2025completeness Thm 4).

### [minor] logician — Script slide 11 (script.md:105): 'I am relying on Koshkin's account of that paper.'

*citation, confidence high.* This misstates the evidential basis. The Herzberger card quotes T7–T9 and T11 matched in two independent OCR scans of the chapter itself. It does not rest on Koshkin. ARGUMENT P19 and QA Q28 cite Herzberger directly, by theorem number. The disclaimer understates the evidence and sends a questioner to the wrong source.

**Proposed:** 'I have read that chapter only in search snippets, so I cite it by theorem number.' Optionally add the domain condition: the thesis holds 'within any sufficiently large domain' (T8).

*Evidence:* herzberger1981theorem source_basis and loci (l.11, l.27-30). QA.md Q28. ARGUMENT.md P19.

### [minor] logician — Slide 10 (deck.md:69) 'Kempe: a unit · Peirce: "this action" · …'; script slide 10 (script.md:95-97)

*logic, confidence high.* This line counts one construction twice. 'This action' is Peirce's name for what Kempe's §330 construction adds to the universe. It is not a separate reduction of Peirce's. Listing 'Peirce' among the reductions that 'mint a third' suggests that Peirce offered a dyadic reduction. The script also says each minted object 'stands for the whole tuple'. That fails for Löwenheim, whose new elements are pairs of old elements. A quaternary tuple becomes a binary relation between two pair-elements, and ternaries are handled as a special case of quaternaries.

**Proposed:** 'Kempe: a unit (Peirce: "this action") · Löwenheim: pair-elements · Quine: {x, y}'. In the script, say 'a new object that stands for a pair or a tuple'.

*Evidence:* peirce1892critic CP 3.424: Kempe's construction 'is accomplished by adding to the universe of concrete things the abstraction "this action."'. lowenheim1915moglichkeiten p.464 ('Elemente die Elementenpaare des alten'; a quaternary a → binary A over 𝔈).

### [minor] logician — Script slide 10 (script.md:96) 'Quine added sets of the form x, y'; slide 10 line 2 'larger universe'

*factual, confidence high.* Quine does not always enlarge the universe. He notes that Θ's universe 'may happen already to comprise all this', and in that case the reduction runs over the same universe. The 'larger universe' contrast therefore does not cover Quine's own stated case. This is another reason to draw the line at the junction rather than the universe (see the first finding).

**Proposed:** 'Quine used pairs {x, y}, which he adds to the universe when they are not already there.'

*Evidence:* quine1954reduction p.180: '(Of course the universe of Θ may happen already to comprise all this.)'. ARGUMENT.md P17 ('enlargement is typical, not guaranteed').

### [minor] logician — Script slide 9 (script.md:86-87): 'a two-page paper'

*number, confidence high.* Quine 1954 runs to pp. 180–182, three pages. The numeral is also absent from NUMBERS.md, though it is spelled out in words.

**Proposed:** 'a three-page paper', or 'a short paper'.

*Evidence:* quine1954reduction venue: 'The Journal of Symbolic Logic 19(3): 180–182'.

### [minor] logician — Script slide 9 (script.md:92): 'Quine himself never said so.'

*citation, confidence high.* The talk has read only p.180 and the notes of Quine 1954. The broader claim, never then or later, is Koshkin's report (2022, n.1), and ARGUMENT P17 says it must be attributed to him as a paraphrase. Quine's 1935 review and his 1995 'Peirce's Logic' are metadata-only.

**Proposed:** 'And Koshkin reports that Quine never connected the result to Peirce, then or later.'

*Evidence:* ARGUMENT.md P17 (l.226). quine1954reduction card l.25, l.68.

### [minor] logician — Slide 10 (deck.md:67-70)

*audience_comprehension, confidence high.* Only the script says 'This slide is my argument, not a consensus'. The slide itself carries no label. Placed between two slides of attributed quotations, a bare headline 'Every reduction mints a third' will read to the audience as an established result. The author's QA Q27 evidence line already asks for the label.

**Proposed:** Add a line on the slide: 'The speaker's argument'.

*Evidence:* script.md:102. deck.md:67-70 (no label). QA.md Q27 evidence line ('Label slide 9 as the talk's argument').

### [minor] logician — Script slide 5 (script.md:50, 53-54): 'Kempe attacked exactly there' and 'Kempe's extra unit, he said, is itself the triad.'

*citation, confidence medium.* The quoted-sounding paraphrase is stronger than the 1892 text. Peirce put the mediation in 'the attachment of lines to spots'. He objected that the diagram does not represent how the abstraction 'this action' is derived. He did not say the unit is itself the triad. CLAIM decision 9 flags this same Kempe attribution in the lab paper. 'Attacked' also frames Kempe's memoir as aimed at Peirce. The label 'formidable objection' is Peirce's own, and the cards do not show that Kempe addressed Peirce.

**Proposed:** 'In 1886 Alfred Kempe's memoir struck exactly there; Peirce called it "a formidable objection to my views." … What he denied was that this builds the triad out of pairs: the unit and its three attachments are themselves the mediation, and the diagram does not show where that unit comes from.'

*Evidence:* peirce1892critic CP 3.423 ('the attachment of lines to spots, that of mediation'), CP 3.424 ('the diagram fails to afford any formal representation of the manner in which this abstract idea is derived'). Card Notes: 'A version the sources support: … the spot and its three attachments are themselves the mediation'. CLAIM.md:104.

### [minor] mechanical — script slide 9 (script.md:84)

*factual, confidence high.* "The reply that made most philosophers stop believing Peirce": the source says "doubted by many", not most.

**Proposed:** "The reply after which many philosophers doubted Peirce."

*Evidence:* burch2021sep §14 ("was for over a century doubted by many, especially after the publication of a proof by … Quine").

### [minor] mechanical — script slide 9 (script.md:86)

*factual, confidence high.* "Quine published a two-page paper" is wrong: the paper runs to pp. 180–182. The script also says "any theory". Quine's scope is any interpreted theory in the notation of quantification theory.

**Proposed:** "a three-page paper" (or "a short paper") "showing that any interpreted first-order theory can be rewritten with…"

*Evidence:* quine1954reduction (JSL 19(3): 180–182; p.180 "Consider any interpreted theory Θ, formulated in the notation of quantification theory").

### [minor] mechanical — script slide 9 (script.md:92)

*citation, confidence high.* "Quine himself never said so" is a universal claim. The talk's own reading covers only p.180 and the notes. The support is Koshkin's n.1, so it needs attribution.

**Proposed:** "As Sergiy Koshkin notes, Quine himself never said so."

*Evidence:* quine1954reduction.md (pp.181–182 unread; Koshkin 2022 n.1: "he never did say so himself").

### [minor] mechanical — script slide 11 (script.md:105-106)

*citation, confidence medium.* The script mis-describes three sources. (a) "I am relying on Koshkin's account of that paper": the Herzberger card rests on Herzberger's own text (T9, T11, matched in two scans), not on Koshkin. (b) "Burch built a whole algebra in which it holds" leaves out that his proof needs a restriction on juxtaposition, and that restriction is the gerrymandering point of slide 11. (c) "Hereth Correia and Pöschel gave the strongest proofs": they proved only the hard (negative) clause.

**Proposed:** (a) "…collapses under another; I have read his theorems in snippets only." (b) "Burch proved it in an algebra that restricts one construction." (c) "Hereth Correia and Pöschel proved the hard half without that restriction."

*Evidence:* herzberger1981theorem source_basis and loci T9/T11. herethcorreia2006teridentity p.1 abstract ("Using a restriction on the allowed constructions") and p.2 ("we will not show the part that any relation can be constructed"). koshkin2022reduction p.8.

### [minor] mechanical — script slide 14 (script.md:136)

*audience_comprehension, confidence high.* Slide 14's own notes open with "The next slide is where the instrument earns its keep", but they describe slide 14's content. The speaker cue contradicts the slide on screen.

**Proposed:** "This slide is where the instrument earns its keep…"

*Evidence:* script.md:135-137 vs deck.md:93-97.

### [minor] mechanical — script slide 2 (script.md:14); script slide 15 (script.md:158-159)

*scope, confidence medium.* "The platform that matches a driver and a rider is the obvious case" presents a real platform as an instance of the criterion. No platform is modelled. "This form now runs through ordinary work and ordinary life at scale" is stated as fact, but CLAIM makes it a historical premise.

**Proposed:** Slide 2: "The platform that matches a driver and a rider is the case I have in mind." Slide 15: "What is new, I take it, is…" Slide 16's limit: "no worker or platform has been modelled."

*Evidence:* CLAIM.md:90 (do not claim that the lab shows any worker, platform or real rule is triadic). CLAIM.md:33 (mass algorithmic instance is a historical premise).

### [minor] mechanical — NUMBERS.md:9-11; check_talk.py:171, 192, 201-203

*number, confidence high.* The checker's 0 problems overstates coverage. (a) Deck blockquotes (slides 3, 4, 5, 11) carry no quote marks, so no deck quotation there is tested. They match by hand. (b) BANNED.txt is absent, so check 6 is skipped. (c) Numbers are checked as a set. The '2.0' row cites only the control, but slide 14's 2.0s are three other strings (dyad_mutual simmel-h1, copy_BCA peirce-h1, giving_degenerate peirce-h3). The arithmetic 2s on slide 4 pass on the lab-result row. All values happen to be correct.

**Proposed:** Add NUMBERS.md rows for dyad_mutual, copy_BCA and giving_degenerate at Φ_MIP=2.000000, and an arithmetic row for 2. Make check_quotes also read '> ' lines in deck.md. Add BANNED.txt, or make its absence a FAIL.

*Evidence:* check_talk.py:192 regex requires quote characters; deck.md:20-33, 37, 74-76 use '> ' only. ls talk/ shows no BANNED.txt. ci/reproduce.json strings listed.

### [minor] mechanical — script.md:4 header; OUTLINE.md:1, 196; per-slide timing

*scope, confidence high.* The script header says about 2,300 words and eighteen minutes. The actual length is 1,994 words: 15.3 min at the checker's 130 wpm, 16.0 min at the outline's 125, against the outline's 2,375. The deck no longer follows OUTLINE.md's slide map. Outline slide 11 is dropped, so S4 gets 128 words (~61 s) against a planned 170 s, while S1 (deck slides 1–6) runs about 305 s against 225. The biggest single overrun is deck slides 1+2: 181 words against the outline's 62.

**Proposed:** Update the script header to the real count and renumber OUTLINE.md to the 16 deck slides. Either restore the outline slide 11 material (Hereth Correia & Pöschel's Theorem 2; copy = merge) into slide 11's ~3 free minutes, or record the cut and the new section times.

*Evidence:* check_talk.py per-slide counts. OUTLINE.md section times (S1 225 · S2 145 · S3 140 · S4 170 · S5 230 · S6 230).

### [minor] peirce-scholar — script slide 5 (script.md:50)

*factual, confidence medium.* "In 1886 Alfred Kempe attacked exactly there" says Kempe aimed his memoir at Peirce's premise. The memoir is a general theory of mathematical form. The objection is Peirce's reading of it ("an analysis which amounts to a formidable objection to my views"), and Kempe's text as held does not mention Peirce. The node-as-relative premise that Kempe supposedly "attacked" was also stated in that form only in 1897, eleven years after the memoir. This is the same kind of error CLAIM.md forbids for Quine (aiming the 1954 paper at Peirce).

**Proposed:** "In 1886 Alfred Kempe published a memoir that Peirce called 'a formidable objection to my views'. Kempe redrew a triad as ..."

*Evidence:* peirce1892critic.md Locus CP 3.423 ("amounts to a formidable objection"); kempe1886memoir.md (no Peirce locus); grep of triadic_reduction_local/fulltext/kempe1886.txt finds no 'Peirce' (OCR, so medium confidence); peirce1897logic pp.170-171

### [minor] peirce-scholar — deck slide 10 (deck.md:69); script slide 10 (script.md:95-97)

*logic, confidence high.* The deck lists "Kempe: a unit · Peirce: 'this action'" as two separate reductions that each mint a third. "This action" is Peirce's name for the abstraction that Kempe's §330 unit adds to the universe. It is one minted object, described by the objector's target, and Peirce was not offering a reduction of his own. On the slide, the list reads as if Peirce had reduced triads to dyads himself. The script's wording, "Peirce, answering him, pointed to 'this action'", is accurate. The deck's is not.

**Proposed:** Deck: "Kempe: a unit λ (Peirce: 'this action') · Löwenheim: pairs · Quine: {x, y}". If the talk wants a Peirce minting of its own, use the transaction E of CP 1.363, which mints a term for the positive clause. Note that the CP sale example needs [sic] or the W6 letters.

*Evidence:* peirce1892critic.md Locus CP 3.424 ("This is accomplished by adding to the universe of concrete things the abstraction 'this action.'"); kempe1886memoir.md §330

### [minor] peirce-scholar — script slide 9 (script.md:84)

*citation, confidence high.* "The reply that made most philosophers stop believing Peirce" goes beyond the source. The only carded evidence is Burch's SEP sentence: the thesis "was for over a century doubted by many, especially after the publication of a proof by ... Quine". "Many" is not "most", and "stop believing" assumes they believed it first.

**Proposed:** "Now the reply after which, as Burch puts it, the thesis was 'doubted by many'."

*Evidence:* burch2021sep.md l.23 (§14)

### [minor] peirce-scholar — script slide 3 (script.md:25)

*factual, confidence medium.* "a memoir he read in 1870": the only carded date is that the memoir was "Communicated January 26, 1870" to the American Academy. The printed volume is dated 1873. Nothing on the card says Peirce read it himself.

**Proposed:** "a memoir communicated to the American Academy in January 1870"

*Evidence:* peirce1870description.md l.6, l.26, l.32

### [minor] simmel-sociologist — Slide 14 line 3 (deck.md:97), script slides 8 and 14 (script.md:79, 138): the label 'Simmel's majority'

*scope, confidence medium.* 'Simmel's majority' presents one Boolean rendering as Simmel's. Simmel's majority (1902 II:158; 1908 p.95) is a group decision that overrides a dissenting individual, with voluntariness in play. The model is three synchronous copies of maj(A, B, C), with no separate decision and no individual response. The lab's own table says the rendering drops 'voluntariness; the individual's response'. The lab's earlier mediated-majority form (probe 10) also factored, and FINDINGS notes that the alternatives in Limitations were not run.

**Proposed:** Label it 'a majority rule (our rendering of Simmel's majority, 1902 II:158)' on first mention and 'the majority rule' after that.

*Evidence:* simmel/paper.md:106 (C3 row: 'keeps the outvoting mechanism; drops voluntariness; the individual's response'); hypotheses.md:41-43; FINDINGS.md:25; simmel1902number2.md:24-25.

### [minor] simmel-sociologist — Slide 8 attribution (deck.md:58)

*citation, confidence high.* 'configurations of twos' (Simmel, 1902; 1908) puts two dates on an English wording that exists only in Small's 1902 translation (II:166). The 1908 text is the German 'Zweierkonfigurationen' (p.103), and Wolff has 'configurations of two'. The card rule is one edition per slide, naming the translator.

**Proposed:** 'configurations of twos' (Simmel 1902, trans. Small, II:166; German 'Zweierkonfigurationen', 1908: 103).

*Evidence:* simmel1902number2.md:20, 29, 57; simmel1908soziologie.md:37.
