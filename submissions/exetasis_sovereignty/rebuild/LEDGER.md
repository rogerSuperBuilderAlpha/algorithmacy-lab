# LEDGER: one entry per written sentence

[Claude, 24 Oct 2026. Entries are keyed to outline ids: 23 sentences, plus one outline entry (O8) cut. Marks: ✅ passes; ⚠️ passes with a departure written; ❌ rewritten, with both attempts kept.
- **form:** the counterpart move, and weight within ±40%.
- **construction:** sentence shape, and every pronoun with exactly one antecedent.
- **register:** the words checked against the model.
- **value:** what the sentence owes the question or the thesis.
- **counterpart:** the model entry answered.
- **truth:** the claim is in the draft; the credit is the same; any number matches.

**Section gate: 494 words by `wc -w`, inside the call's 300–500.** Attempt 1 was 597 words and failed the gate. It is kept at `scratchpad/ms_attempt1.txt`, and the cuts are recorded at O3, O5, O8, O16 and O22.]

---

**O1** Democratic theory has tied popular sovereignty to a civic competence that citizens must acquire.
- form ✅: field-claim, 14 words against A1's 13.
- construction ✅: no pronouns.
- register ✅: "has tied" is the present perfect of A1's "have changed"; "civic competence" is a plain noun phrase.
- value ✅: the domain.
- counterpart: A1, I1.
- truth ✅: DRAFT ¶1.1 "links popular sovereignty to acquiring civic competence".

**O2** In fifth-century Greece most free citizens "could apparently read the laws," and democracy was "from the beginning associated with widespread literacy" (Goody and Watt, 1963: 332).
- form ✅: concrete evidence, 27 words against I4's 22 (+23%).
- construction ✅: I4's shape ("In the UK, the number … doubled … (Huws 2020: 4)").
- register ✅: the citation form "(Author, year: page)" is the model's.
- value ✅: anchors the premise.
- truth ✅: both quotations are verbatim, p. 332. "Most free citizens" paraphrases "a majority of the free citizens", same page. The credit is the same as the draft's.

**O3** Recent discussions of artificial intelligence keep this premise: Son (2022: 13, 16) treats literacy as "the necessary condition for democracy" and asks for "technology literacy," and Coeckelbergh (2023) looks to education to protect epistemic agency.
- form ⚠️: I9's move at 37 words against 40. The model's "have contributed to calls for" clause was cut for budget (attempt 1 had it).
- construction ✅: the colon introduces the two examples, as the model's colons introduce lists.
- register ✅: "Recent discussions of" is I9's frame; "keep", "treats", "asks for" and "looks to" are plain verbs.
- value ✅: the rival premise and its remedy.
- truth ✅: Son p. 13 ("the necessary condition"), p. 16 ("technology literacy"); Coeckelbergh p. 1348 ("protect or even enhance epistemic and political agency"; "by means of education").

**O4** Political philosophers have paid less attention to whether a reading competence can secure sovereignty once algorithms coordinate people rather than inform them.
- form ✅: gap, 22 words against I10's 25.
- construction ✅: the agent is named ("Political philosophers"), as the house style requires.
- register ✅: "have paid less attention to" is I10's frame. "Reading competence" is plain.
- value ✅: the research question, stated once.
- truth ⚠️: the claim that algorithms coordinate rather than inform is DRAFT ¶1.5. **The gap claim is not in the draft.** It rests on `research/LITERACY_SEARCH.md` ("I found no work that…"), whose search is incomplete (OpenAlex, Consensus, Semantic Scholar and PhilPapers are still pending). It is held to the model's soft frame. **Roger:** keep it, or cut it before submission.

**O5** In this paper, I develop the concept of algorithmacy to address this question.
- form ⚠️: concept-offer, 13 words against I11's 32 (−59%). Warrant: budget. I11's second clause ("provide an account of …") is carried by O19.
- construction ✅: "this question" has one antecedent, O4's whether-clause.
- register ✅: "In this article, we develop the concept of … to address …" is I11's frame, in the first-person singular (precedence note 1).
- value ✅: names the concept.
- truth ✅: algorithmacy is the draft's term (¶4.1).

**O6** I argue that literacy was necessary for democratic sovereignty but never sufficient, and that algorithmacy stands in the same relation to sovereignty under algorithmic coordination.
- form ✅: thesis, 26 words against A4's 28.
- construction ✅: "the same relation" refers back to "necessary … but never sufficient", in the same sentence.
- register ✅: "I argue that" is A4's frame. "Stands in the same relation" is plain.
- value ✅: the whole thesis.
- truth ✅: DRAFT ¶2.1 ("necessity … but also its insufficiency") and ¶4.2 ("relates to platform governance as literacy did to the state").

**O7** Algorithmacy is the competence to infer how an intermediary evaluates transactions, to encode intent into signals the intermediary accepts, and to adapt as the intermediary's models change.
- Attempt 1 ❌: "…into signals **it** accepts, and to adapt as **its** models change." "It" could be the competence or the intermediary, so it has two candidate antecedents.
- Attempt 2:
  - form ✅: definition, 28 words against I22's 24.
  - construction ✅: the noun is repeated instead of a pronoun.
  - register ✅: the model repeats its key term rather than vary it (9 times in the introduction).
  - value ✅: the concept defined.
  - truth ✅: DRAFT ¶4.1, with the three capacities in order.

**O8** (outline: "Consider the history of literacy.", the counterpart of I13)
- **Cut** for budget in the third cutting pass (attempt 1 → 516 → 496).
- The paragraph now opens on O9's narrative citation, "Goody and Watt (1963: 333) observe", whose subject names the history in question.

**O9** Goody and Watt (1963: 333) observe that the "dream of an 'educated democracy'" was never realized, and public schooling emerged and mostly expanded under nondemocratic regimes that used it to teach obedience (Paglayan, 2022: 1242).
- form ✅: two examples compressed into one sentence (I14–I15), 36 words against 44.
- construction ✅: "it" has one antecedent, "public schooling" ("regimes" is plural).
- register ✅: "observe" (cf. "Rosenblat and Stark (2016) found that"); "emerged and mostly expanded" follows Paglayan's own "emergence and most of their expansion".
- value ✅: the evidence that literacy was insufficient.
- truth ✅: Goody & Watt p. 333 ("has never been realized in practice"); Paglayan p. 1242, abstract ("designed to teach obedience"). The credit is the same as the draft's.

**O10** The literate subjects of those regimes lacked standing, not qualification.
- Attempt 1 ❌: "…lacked standing, not **competence**." That changed the draft's opposition: the draft says "qualification", the term that sets up Mill.
- Attempt 2:
  - form ⚠️: 10 words against I17's 30. I17's pseudo-cleft frame ("What these examples have begun to point to is") was dropped for budget.
  - construction ✅: "those regimes" names O9's nondemocratic regimes.
  - register ✅: plain.
  - value ✅: the hinge from evidence to standing.
  - truth ✅: DRAFT ¶2.3.

**O11** This calls into question Mill's rule that "universal teaching must precede universal enfranchisement" (1861: ch. VIII).
- form ✅: 15 words.
- construction ✅: a bare "This" opener refers to O10's claim. The model opens on "This" twice (I5, I20) and the venue range allows it.
- register ✅: "has called into question" is I7's verb phrase.
- value ✅: answers Mill's rival position.
- truth ✅: Mill ch. VIII, verbatim (Gutenberg #5669). DRAFT ¶2.4 "challenges Mill's assertion".

**O12** Only where codified law, a free press and the franchise existed could literate citizens hold authorities to account.
- Attempt 1 ❌: "…held authorities to account only where … allowed **them** to." "Them" could be the citizens or the authorities.
- Attempt 2:
  - form ✅: the closer, 18 words.
  - construction ✅: no pronoun; the inversion keeps the condition first.
  - register ✅: "hold … to account" is plain.
  - value ✅: the condition the next paragraph removes, and the sentence ends on it (end-focus).
  - truth ✅: DRAFT ¶2.5.

**O13a** Algorithmic coordination provides none of these institutions.
- form ✅: 7 words; the opener of I18's move.
- construction ✅: "these institutions" refers to law, press and franchise, the end of O12 (tail-head link).
- register ✅: plain.
- value ✅: the turn.
- truth ✅: DRAFT ¶3.1 ("fails to reproduce the institutional infrastructure").

**O13b** Platforms operate through "a triangular structure" with the operator at the apex (Stark and Vanden Broeck, 2024: 14).
- form ✅: mechanism, 16 words.
- construction ✅: "the operator" is the platform's, named by "Platforms".
- register ✅: "operate through" is plain.
- truth ✅: p. 14, verbatim fragment.

**O14** Machine-learning opacity resists the remedies of code literacy (Burrell, 2016), and operators co-opt participants by enrolling "users and providers in a system of ratings" (Stark and Vanden Broeck, 2024: 14).
- Attempt 1 ❌: "operators co-opt **the parties** when **they** 'enroll …'". "They" could be the operators or the parties, and "the parties" had no prior referent.
- Attempt 2:
  - form ✅: mechanism continued, 29 words.
  - construction ✅: no pronoun.
  - register ✅: "resists" and "co-opt" are plain. "Co-opt" is Stark & Vanden Broeck's term (p. 5).
  - truth ✅: Burrell, the three forms of opacity (pp. 1–2). Stark & Vanden Broeck p. 14, "platform operators enroll users and providers in a system of ratings"; the quoted fragment is verbatim. DRAFT ¶3.3.

**O15** Authority issues no public decree, and algorithmic governmentality "produces no subjectivation" (Rouvroy and Berns, 2013: 173–174, my translation), so a literate public has nothing stable to read.
- form ✅: appearance (I19), 28 words against 24.
- construction ✅: no pronoun.
- register ✅: plain verbs ("issues", "produces", "has").
- value ✅: the reason literacy fails, ending on "read".
- truth ✅: "ne produit aucune subjectivation", pp. 173–174, in Claude's translation, which is marked. DRAFT ¶3.3–5.

**O16** Algorithmacy meets the same limit that literacy met.
- form ⚠️: the concession (I28) at 8 words against 30. Attempt 1's "This is not a new problem but the problem of literacy in a new medium", which used I28's "not … but" frame, was cut for budget.
- construction ✅: "the same limit" refers to O6's "never sufficient".
- register ✅: plain.
- truth ✅: DRAFT ¶4.2 ("indispensable yet politically inert in isolation").

**O17** Gagrčin et al. (2026: 442) find algorithm literacy to be "but one facet of competences needed to improve working conditions."
- form ✅: evidence, 18 words.
- construction ✅.
- register ✅: "find", as in the model's "found that".
- truth ✅: p. 442, verbatim. "Review of 169 studies" was cut for budget.

**O18** Because platforms rank participants against each other, individual algorithmacy yields only advantage over peers.
- form ✅: 14 words; the plain answer to I26.
- construction ✅.
- register ✅: "rank" and "yields" are plain. The model's "beneath … lies" figure was not taken.
- truth ✅: DRAFT ¶4.4.

**O19** Algorithmacy becomes sovereignty only through institutional standing, which I call coordinative sovereignty: the collective capacity to contest and co-govern a mediation that participants cannot bypass.
- form ✅: distinctive and definition, 28 words.
- construction ⚠️: a colon introduces a definition. The model's colons introduce lists and quotations, and the house style allows a gloss welded onto its term. Attempt 1 opened on "It", which was ambiguous after O18, so the subject is now the repeated key term.
- register ✅: "which I call" is plain.
- value ✅: the institutional half of the thesis.
- truth ✅: DRAFT ¶4.5. "Bypass" replaces the draft's "avoid", because "bypass" is the draft's own term in ¶5.4 ("bypass test").

**O20** In such a mediation exit fails, since "a choice between awful regimes cannot confer authority on either" (Lazar, 2025: 163), and collective voice remains.
- form ✅: 26 words.
- construction ✅: "such a mediation" refers to O19's.
- register ✅: plain.
- truth ✅: Lazar p. 163, verbatim. DRAFT ¶4.6–7. "Only collective voice remains" is softened to "collective voice remains", because Lazar argues that exit fails, not that voice is the only remedy.

**O21a** Verhulst and Gonzalez Otero (2026: 1) locate digital sovereignty in "who has the power to shape, govern, and challenge these systems" and answer with a European "stewardship architecture."
- form ⚠️: the rival claim (I31) at 29 words against 10. Warrant: the rival needs its quotation.
- construction ✅.
- register ✅: "locate" and "answer with" are plain.
- truth ✅: p. 1 (abstract), both quotations verbatim. DRAFT ¶5.2. The draft's "criticize … for focusing primarily on dependency" was dropped for budget (OUR_BRIEF).

**O21b** If I am right, that power lies with the workers, sellers and citizens inside mediations they cannot exit.
- form ✅: "if we are right" (I32), 18 words against 13.
- construction ✅: "that power" refers to O21a's quoted power; "they" refers to workers, sellers and citizens.
- register ✅: I32's frame. The model's "However," is dropped because no contrast marker is needed after O21a.
- truth ✅: DRAFT ¶5.1, ¶5.3.

**O22** In the full paper I trace the genealogy from literacy to algorithmacy, specify a bypass test for compulsory mediation, and examine data trusts and collective bargaining as institutions that could turn competence into standing.
- form ⚠️: the roadmap (I37–I42) compressed into one sentence. "This article proceeds as follows" and "First / We then / Finally" were cut for budget.
- construction ✅.
- register ✅: "trace", "specify" and "examine" (I42 "examine"); "could" follows I42's "could potentially".
- truth ✅: DRAFT ¶5.4.

---

## Open for Roger
1. **O4, the gap claim.** It comes from an incomplete search, not from your draft. Keep it or cut it.
2. **Departures marked ⚠️** at O3, O5, O10, O16, O21a and O22. In each, the budget cut a model frame.
3. **The read-aloud** is the last gate.
