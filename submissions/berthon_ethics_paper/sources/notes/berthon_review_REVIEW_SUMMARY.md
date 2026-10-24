# Review of the second draft — consolidated

*Compiled by Claude on 2026-10-13 from six agent-drafted reviews in this directory (R1–R6). The
author has not reviewed it. The reviews report; none rewrites. The manuscript is
`../AUTHOR_DRAFT_v2.md`, saved byte-for-byte from the author's paste. The reviews were not themselves
audited; where two reviewers checked the same point independently, this file says so.*

## Verdict

The paper has a real contribution: it moves the ethics of algorithmic mediation from the user's
competence to the positions around the medium, and it documents five practices from the literacy
transition to show where the historical wrongs lay. Sections 1, 3, 4.2–4.5 and 5.1–5.2 carry it and
read as the author's.

It is not ready to submit. The referee's recommendation is major revision, and rejection if the
mechanical faults are not fixed first: an editor would return this draft before review.

## Fix before anyone else reads it

1. **Uncited verbatim material.** The equation in 5.3 and its symbol definitions are Equation 1 of
   Margondai and Mouloua, arXiv 2601.13973 (20 January 2026), which credits the HIAG framework to
   Margondai, Willox and Mouloua (2025, *Proceedings of the Human Factors and Ergonomics Society*
   69(1), 1403–1408). Neither is cited. [R5; R2 and R1 flagged the missing source.] Cite both or cut
   the passage. R5 and R2 advise cutting: the model measures nothing, and the draft's account of its
   "absorbing barrier" does not match the source. Claude confirmed the arXiv record: "The
   Transparency Paradox in Explainable AI: A Theory of Autonomy Depletion Through Cognitive Load",
   Margondai and Mouloua, 20 January 2026. The phrase "transparency paradox", which the draft
   attributes to Pasquale (2015), is that paper's title; Claude did not compare the equation itself.
2. **A quotation that is not in its source.** "The myth of culture as an engine of moral blindness"
   (Moody-Adams, p. 304) does not occur in her article; neither "engine" nor "myth" appears in it.
   Her p. 304 sentence is "A culture … cannot be an 'agent' of anything." [R3 and R1, independently.]
3. **References that do not exist as given.** Eight entries, with what the record shows:

   | Draft entry | What exists |
   | --- | --- |
   | Hsieh (2008), BEQ 18(4), 513–539 | Not found. Those pages are another article. Hsieh's workplace-republicanism paper is "Rawlsian Justice and Workplace Republicanism", *Social Theory and Practice* 31(1), 2005 (record seen, text not read) |
   | Cameron (2024), *Academy of Management Annals* | Cameron, L. D. (2024), "The Making of the 'Good Bad' Job", *Administrative Science Quarterly* 69(2), 458–514 |
   | Rahman (2021), *Yale Law Journal* | Rahman, H. A. (2021), "The Invisible Cage", *Administrative Science Quarterly* 66(4), 945–988 |
   | Kolt (2025), *Stanford Technology Law Review* | Kolt, N., "Governing AI Agents", *Notre Dame Law Review* 101 |
   | Zong and Matias (2024), "Bartleby…", TOCHI | Zong and Matias (2024), "Data Refusal from Below", *ACM Journal on Responsible Computing* 1(1), 1–23 |
   | Qadri, Prabhakaran and Denton (2026), *Big Data & Society* | A workshop poster at ICML 2026, "'AI is (not) the new ..'"; abstract only |
   | Almeida Cabrejas (2019), "Journal of Legal History and Notarial Studies" | *Philologia hispalensis* 33(1), 21–41, under a Spanish title |
   | Scherer et al. (2023), *Business & Society* | A guest editors' introduction, *Business Ethics Quarterly* 33(3), 409–439 |

   Nine more have wrong details (Bakos et al.; Engerman and Sokoloff; Lake; Moser; Johansson;
   Hagedorn; Viljoen; M. Douglass; the UIS item). `R1_citations.md` gives each correction. All but
   Hsieh and Scherer et al. are in `../literature/references.bib` with verified details.
4. **Machine residue.** 94 `[span_…]` tags on 22 lines, all inside tables and diagrams; an
   unrendered LaTeX equation; `⚬` bullets; a broken table row in 6.1. [R1, R6.]
5. **Citations with no entry, and entries with no citation.** Cited but unlisted: Levin (2016), the
   Waitangi Tribunal (2014), Akrich, Mumford, the Cleveland and Wilson veto messages, about eleven
   statutes. Listed but never cited: twelve entries, among them Aristotle, Bourdieu, Clanchy, Citron
   and H. A. Williams. [R1.]

## Corrections that reverted

`../AUTHOR_DRAFT_CHECK.md` listed 60 points in the earlier draft. In this one, 13 are corrected, 25
show the old error, 14 are changed but still unsupported, and 8 passages are gone. [R1.] The ones that
matter most:

- *Marshall*, para. 14, again attributed to "non-literate" Mi'kmaq signatories; it is a general remark
  on treaty-making. "Crown scribes overwrite oral covenants" inverts the holding at para. 40.
- "Sworn notaries"; *non est factum* as a restraint on scribes; the Pragmática read "aloud".
- "Zero power" (4.2), where Cameron (2024) reports covert worker leverage.
- "Complete absence of independent procedural safeguards" and "Zero External Procedural Buffers"
  (4.4), where the narrowed claim had been accepted into the Google Doc.
- The 1643 petition as journeymen's; it was the Company's own.

## The argument

1. **The method contradicts the thesis.** [R3, R2.] Section 2.3 forbids judging the past by present
   standards; section 3 classifies 1740 and 1901 as "republican domination", a theory of 1997. The
   three numbered benchmarks are the author's, not Walzer's, and the method is stated in
   *Interpretation and Social Criticism* (1987), not *The Company of Critics* (1988). Section 5 applies
   only the hypocrisy benchmark to platforms. One standard for both periods needs choosing and
   defending. Moody-Adams, on whom 2.3 leans, argues against the "standards of their own day" defence.
2. **Domination is assumed.** [R2, R3.] The draft does not show that a platform's power is arbitrary
   in Pettit's sense, given law, contract and competition. Its own source places the dominator in
   owners and managers. Pettit is cited unread.
3. **The duties are announced, not derived.** [R2, R3, R5.] They match the three positions by rhyme.
   No claim-holder or type of duty is stated, and the addressee shifts between operator and
   legislature. Young's model is shared, non-blaming and discharged collectively, so it does not yield
   an "unavoidable, affirmative duty" on one class of actor. Objections the research recorded go
   unanswered: predictability does not end domination; an envelope may be a disclosure by another
   name; a user's agent is its user's instrument in law.
4. **The triad is not applied consistently.** [R5.] The first diagram labels one side "Employer /
   Capital" with "Extracted Surplus", which is a two-party picture. A lender's own model, a feed and a
   moderation system are two-party cases. Hiring vendors and credit bureaus are the true triads.
5. **The paper contradicts itself in sections 6–7.** [R2, R5, R6.] 7.1's interpretability layer gives
   users the data dump 4.2 and 5.3 condemn. 7.2 asks students to audit models and "deploy obfuscatory
   tactics" after section 5 says remedies aimed at the user fail.
6. **Sources stretched.** Bhargava and Young (2022) defend employment-at-will contextually; the draft
   has them demonstrating "pervasive republican domination". Kim and Routledge ground a right to
   explanation in trust. Kamperman and Graff never mention Street. "Structural testimonial injustice"
   merges two of Fricker's categories. [R3, R2, R1.]

## The history

Of 99 historical claims: 31 supported, 31 narrower in the source, 18 contradicted, 19 not in the
research record. [R4.] The ten most serious are listed in `R4_history.md`; among them Waitangi (more
than 500 signed in total; 39 signed the English text), the anti-literacy statutes (none "identical";
Virginia's act predates Turner's revolt), Jomtien and Dakar (no "mandate to eradicate"), the 1917
immigration test (enacted over the veto), Graff (three Ontario cities; no US data; the page range does
not support the claim), Milton ("statutes and standards", a pamphlet), and India (no statute).

Thirteen of thirty quotations are altered or not in the source at the locator given; eight are
verbatim. [R1.] Section 3 omits every counter-case the research recorded. [R4, R2.]

One find worth using: Knox himself records the objection that registrar discretion "perpetuates the
very form of abuse" (p. 11). [R4.]

## Structure and prose

- **Length.** 12,339 words: body 8,984, diagram text 1,195, references 1,828. BEQ's limit is 12,000.
- **Two voices.** Sections 6, 7.1, 7.2, the HIAG passage, the 7.3 conclusion and the thirteen boxes
  read as generated and unrevised: absent from the outline and the research, carrying 80 of the 94
  markers, without page numbers, and repeating one template three times. [R6.] The advice is to cut
  them, not smooth them.
- **Recommended shape** [R6, R2]: cut section 6, 7.1, 7.2 and the HIAG passage; keep three figures
  redrawn (the five practices merged with the mapping; the three duties; the scribe-versus-platform
  figure); move 3.6 into 5.2; move 4.5 to the end and grow it into a limits section; expand 4.1, now
  202 words, since it is the paper's central move. About 9,000 words result, with 2,500 to spare.
- **Epigrams.** 24 paragraph-final epigrams, none in the introduction and 15 in sections 4–6.
- **For the author and the journal.** The Douglass quotation in 3.2 reproduces a slur from the source.

## What to protect

The "test, access, record" spine. The introduction's three cases. The qualification in 2.3 that the
charge is against what was done with literacy. Section 3's named actors and dated acts where they
match the record. The narrowed safeguards claim as the Google Doc had it. Section 4.5's statement of
what the analogy cannot show.

## Not checked

The reviews were not audited against each other. Full texts of Pettit, Fricker, Young (2011), Kousser,
Burns, the BEQ articles and Bommasani et al. were not opened by any reviewer. R1 could not confirm the
Moser book, Monteiro, or Phule's publisher.
