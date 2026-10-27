# R2 — Referee report for *Business Ethics Quarterly*

**Agent-drafted review. The author has not seen it.**

*Written by Claude on 2026-10-13 as the second seat on the panel, from `../AUTHOR_DRAFT_v2.md` read
whole, the arm's records (`../AUTHOR_DRAFT_CHECK.md`, `../LITERATURE_TO_ADD.md`,
`../literature/facets/`), and Crossref records fetched this session for the business-ethics papers the
draft cites. Line numbers are those of `AUTHOR_DRAFT_v2.md`. I report; I do not rewrite.*

## 1. Verdict

The paper argues that the wrongs of the literacy transition were committed by whoever held the test,
the access and the record, not by a public that failed to learn; that platform operators now hold
those positions; and that AI-literacy and explanation remedies therefore address the wrong party. The
idea at its centre is publishable and, as far as the arm's four research rounds can tell, new in its
combination; the manuscript is not ready for BEQ, and in its present state an editor would return it
before a referee saw it. The single most serious problem is that the argument assumes what it must
show: that the platform intermediary dominates in Pettit's sense and that domination yields these
three particular duties on operators, when the paper's own framework (Muldoon and Raekstad; its
section 5.1 on divided loyalties) locates the dominator in the operator, not in a "third party", and
when the duties are announced by rhyme with the three positions rather than derived.

**Contribution in two sentences, as I read it.** The paper shifts the ethics of algorithmic mediation
from the user's competence to the institutional positions around the medium, using five documented
practices from the literacy transition to show that the gate, the access and the record were where
the historical wrongs lay. From that reading, via Pettit's non-domination and Young's social-connection
model, it proposes three operator duties: structural refusal, declared operating envelopes and
infrastructural counter-delegation.

**Recommendation: major revision**, on the understanding that the mechanical faults in findings 1 to 3
would be fixed before any resubmission. If they were not, I would recommend rejection.

## 2. Findings, most serious first

### Finding 1 — The manuscript carries machine-generated citation tokens and an uncited formal model. **Must fix.**

*Where.* Tables in §4.1 (lines 256, 262), §5 (line 350), §5.4 (line 423), §6.1 (lines 455–467), §6.2
(lines 483–492), §7.1 (lines 527–540) and §7.2 (lines 566–578) contain strings of the form
`[span_54](start_span)[span_54](end_span)`. §5.3 (lines 399–403) introduces "the Human Identity and
Autonomy Gap (HIAG) framework", a stochastic differential equation for autonomy
$dA_t = \mu(I_t) A_t dt + \sigma_A A_t dW_t^A$, with no citation and no author; §7.2 (line 577) then
cites "(HIAG)" as if it were a source.

*What is wrong.* The `span` tokens are the citation markers of a generative drafting tool, left in the
text. No reader can resolve them. The HIAG model is either the author's own, in which case a normative
paper owes a reason for introducing a Brownian-motion model of autonomy that nothing later uses, or it
is someone else's, in which case it is uncited. Either way a reader will conclude that part of the
text was generated and not checked. Cambridge requires disclosure of generative-AI assistance
(`../venue/VENUE_RECOMMENDATION.md`, "Disclosure"); the tokens would make an undisclosed use obvious.

*Fix.* Remove every `span` token. Delete the HIAG passage and the "verification tax (HIAG)" cell, or
cite the source and state what the model contributes that the prose does not. Add the AI-assistance
disclosure the journal requires.

### Finding 2 — Five reference-list entries do not match any verified record. **Must fix.**

I am not the citation checker, but a referee at BEQ would catch these in the journal's own
conversation, and they bear on the verdict. In each case the arm's bibliography (`../literature/
references.bib`, 459 verified entries) or a Crossref record fetched this session gives a different work.

| Draft entry (line) | What the record shows |
| --- | --- |
| Hsieh, N. (2008). Employment discrimination, commodification, and agency. *BEQ*, 18(4), 513–539 (line 631) | Crossref returns no such article; a bibliographic query for the title returns nothing by Hsieh in BEQ 18(4). The arm's bib has no Hsieh entry. The text (line 62) credits this paper with "deploy[ing] the republican framework to challenge arbitrary managerial power" |
| Zong, J., & Matias, J. N. (2024). Bartleby in the algorithmic age: The right to refusal in platform labor. *ACM TOCHI*, 31(2) (line 680) | Crossref has Zong and Matias (2024), "Data Refusal from Below: A Framework for Understanding, Evaluating, and Envisioning Refusal as Design", *ACM Journal on Responsible Computing* 1(1), 1–23, DOI 10.1145/3630107. No "Bartleby" title and nothing in TOCHI 31(2) |
| Kolt, N. (2025). Algorithmic agency and the law of principals. *Stanford Technology Law Review*, 28(2) (line 638) | The arm's bib: Kolt, "Governing AI Agents", *Notre Dame Law Review* 101 (2025) (`references.bib:3088`) |
| Almeida Cabrejas, B. (2019). The evolution of the Spanish notarial institution… *Journal of Legal History and Notarial Studies*, 44(1) (line 593) | The arm's bib: Almeida Cabrejas, "No firmó porque dijo no saber", *Philologia hispalensis* (`references.bib:1654`). The p. 24 quotation of the Pragmática is from that article (facet G, line 91) |
| Qadri, R., Prabhakaran, V., & Denton, E. (2026). Temporal pitfalls in sociotechnical AI critique… *Big Data & Society*, 13(1) (line 655) | The arm's bib: Qadri et al. (2026), "'AI is (not) the new ..': A Diagnostic Analogy Framework for Generative AI's Cultural Impacts" (`references.bib:2095`), a non-journal record |

Two further entries are misfiled rather than invented: Scherer, Neesham, Schoeneborn and Scholz
(2023) is the guest editors' introduction in *BEQ* 33(3), 409–439, DOI 10.1017/beq.2023.7, not an
article in *Business & Society* 62(8) (line 660); Bhargava and Young (2022) lacks its subtitle, "An
Institutional Complementarities Approach" (DOI 10.1017/beq.2021.40). Bakos et al. is 2014 in *JLS*
43(1) or the 2009 working paper, not both (line 597; `references.bib:3376, 3388`); Engerman and
Sokoloff in *JEH* 65(4) is 2005 (line 620; `references.bib:4425`).

*Fix.* Replace each entry with the verified record and re-read the sentence that cites it against the
real work. Where no real work carries the claim (Hsieh on workplace republicanism in BEQ 2008), cut the
claim or find the source that does.

### Finding 3 — Errors the first fact-check corrected have returned. **Must fix.**

`../AUTHOR_DRAFT_CHECK.md` flagged these against the first draft and §F records that they were
corrected in the Google Doc. Each is back in v2.

| Draft v2 | What the source says | Record |
| --- | --- | --- |
| Line 13 and line 167: *Marshall* ¶14 "noted that Mi'kmaq signatories had no practical opportunity to create their own written record … allowing Crown scribes to overwrite oral covenants"; "Justice Ian Binnie noted that the Mi'kmaq signatories were non-literate" | ¶14 is a remark about treaty-making in general ("The Indian parties did not, for all practical purposes, have the opportunity…"), not a finding about the Mi'kmaq signatories; and the Court held the reverse of overwriting: the lower courts "erred in concluding that the only enforceable treaty obligations were those set out in the written document" (¶40) | CHECK A8, A9; `T_adjudication.md` §2 row 3 |
| "sworn notaries" (abstract; line 23; line 330; line 411; line 588) | No source read for the arm says "sworn"; struck three times in the first pass | CHECK A3 |
| *Non est factum* among the safeguards "that historically restrained human scribes" (abstract; line 23; line 294) | In *Foster v Mackinnon* the person who misdescribed the paper was the counterparty, not a scribe; facet G scores the case "no distinct intermediary" | CHECK A4; `T_adjudication.md` §8.1 table |
| Line 169, 292, 588: notaries required to "read all legal instruments aloud" | The 1503 law says the notes are read "presentes las partes e los testigos", in the presence of the parties and witnesses; the audit removed "aloud" | CHECK C12; facet G line 91 |
| Line 203: "Junior printers … In their 1643 petition to Parliament, non-elite pressmen denounced … reducing journeymen printers to wage dependency" | The 1643 petition is the Company's own, against eleven patentees it calls "Monopolizers of Printing"; journeymen and wage dependency are not in the record | CHECK C16; facet B line 59 |
| Line 437: antitrust, public utility regulation and bans "(Berthon et al., 2019; …)" | Berthon, Pitt and Campbell write on digital addiction; a full-text search finds no "antitrust", "monopoly" or "public utility". What they supply is "public policy solutions are required" (p. 457) | CHECK D10 |
| Line 169: the 1503 law was passed "Recognizing that scribes routinely defrauded illiterate citizens" | The article "says nothing about misreading by notaries" and the purpose is not stated in the sources read | CHECK C14; facet G line 94 |

Two quotations in v2 are not in the arm's record at all. Moody-Adams (line 64) is quoted as calling
the evasion "the myth of culture as an engine of moral blindness" (p. 304); facet L3 (line 44) gives
p. 304 as "A culture—independent of agents who perpetuate culture—cannot be an 'agent' of anything."
Cleveland's 1897 veto (line 143) is quoted as "It is said that the quality of recent immigration is
undesirable…"; facet D (lines 250, 479) records different words from the veto ("to admit a hundred
thousand immigrants who, though unable to read and write…"). Milton (line 201) reads "brocards" where
facet B (line 89) reads "standards". These may be real; they are unverified.

*Fix.* Restore the corrected wording from the Google Doc for each row, and check the three quotations
against the texts before resubmission.

### Finding 4 — The paper assumes that the intermediary dominates; it does not show it, and its own framework points at a different dominator. **Must fix.**

*Where.* §2.2 (line 60) defines domination as the capacity to interfere "at will, according to their
own arbitrary discretion, without accountability to the affected party's tracked interests". §1 (line
15) then asserts that "the platform intermediary occupies the exact positions that generated illiberal
domination". §4.1 (line 230): the five practices "map with disturbing precision". §7.3 (line 586):
"reproduces these exact institutional patterns".

*What is wrong.* Three gaps.

(a) *Domination is a relation between agents.* The draft's own source places the dominator in
"company owners and managers" acting as a group agent (Muldoon and Raekstad, p. 594, as
`M4_ethical_frameworks.md` line 189 reports it; the Crossref abstract: "company owners and managers
dominate workers"). The draft instead makes "the intermediary" the dominator and the operator a
"Human Subject B" on the far side of it (diagram, line 49). In ride-hail and delivery the platform is
the counterparty, not a third party between two others (`M2_algorithm_studies.md` line 154: "The
platform is not a neutral third party like a notary; in gig work it is the counterparty"). The paper
half-concedes this in §4.4 (line 328: the platform "collapses two distinct legal roles") and §5.1
(divided loyalties), but then the triad in §2.1 is not what it says it is. The paper has to say, in
one place, who dominates whom: the operator dominates the worker and the applicant, using the
algorithm; and the rider, the employer and the lender stand where? If they are the operator's
customers rather than co-equal principals, the triad collapses into Muldoon and Raekstad's dyad with a
customer attached, and the claimed novelty of the "triadic position" needs restating.

(b) *The conditions of domination are not checked case by case.* Pettit's test requires capacity to
interfere, arbitrariness (no forced tracking of the affected party's interests) and absence of
accountability. The paper asserts all three for screening vendors, dispatch and the closed ledger but
checks none. The EU provisions the draft names in §4.4 (GDPR Art. 22, the Platform Work Directive)
are a form of accountability; the draft dismisses them in one sentence ("The human reviewer is an
employee … paid to clear backlogs under brutal performance quotas"), uncited. The narrower claim the
arm's sources support is "no independent, binding check at the point of decision"
(`LITERATURE_TO_ADD.md` §2 item 1), which the abstract and contribution 3 do use. §4.4 then reverts to
"the complete absence of independent procedural safeguards" (line 288), "Zero External Procedural
Buffers" (line 324) and "historically unique" (line 330). The paper contradicts itself between its
abstract and its §4.4.

(c) *Pettit is cited unread.* `LITERATURE_TO_ADD.md` §7 and `M4_ethical_frameworks.md` line 189 record
that neither of Pettit's books was opened. The "benevolent slaveholder" and "tracked interests"
language in §2.2 is unlocated. A BEQ referee will know the text.

*Fix.* State the dominator as an agent (operator, vendor, lender) and give the intermediary the role
of instrument and record; then say what the triad adds to Muldoon and Raekstad that survives this
restatement (my reading: the record-keeping and binding-on-both-sides property, which facet G and
`T_adjudication.md` §8.1 identify as the nearest historical match). For each of the three present
cases, show the three Pettit conditions with a locator. Replace "complete absence", "zero" and
"historically unique" with the narrowed claim already in the abstract. Read Pettit (1997) and give
page numbers.

### Finding 5 — The three duties are announced, not derived, and the paper does not say who holds the claim or what kind of duty it is. **Must fix.**

*Where.* §5 (line 342): "I derive three architectural obligations." §5.2–5.4 then open with
"platforms must", "business ethics must endorse".

*What is wrong.* The inference runs: historical institutions dominated through compulsory literacy
(§3); platforms occupy the same positions (§4, by table); therefore operators owe refusal, envelopes
and counter-delegation (§5). The missing premises are (i) that occupying the position constitutes
domination (finding 4), and (ii) that domination by X generates a duty on X to redesign, rather than a
duty on the state to constrain X. Pettit's own remedy for domination is constitutional and legal
design; Young's social-connection model gives forward-looking *shared* responsibility across all who
participate in the structure, which includes users, regulators and customers (`LITERATURE_TO_ADD.md`
§3 item 3: "McKeown notes users keep a share"). Neither delivers three specific duties on one party.
The draft's own text shows the addressee wobbling: the right to refusal is "backed by a legal
guarantee" (line 372), counter-delegation needs "statutory policy" to "carve out protected legal
standing" (line 429), and §5.5 hands monopoly to antitrust. These are prescriptions to legislators
dressed as duties of operators.

Who holds the correlative claim is never said (`LITERATURE_TO_ADD.md` §3 item 12 asked for this).
Whether the duties are duties of justice (correlative to a right), of beneficence, or design
recommendations is never said. And the three duties pair with three positions by rhyme (gate →
refusal; access → envelope; record → counter-delegation), while practices 4 and 5 get no duty: the
monopoly is deferred to antitrust and the oversold promise is answered in §7.2 by a new curriculum.

On the arm's three recorded objections (`LITERATURE_TO_ADD.md` §2 items 3–5):

- *Envelopes (item 3).* The draft answers the disclosure objection well in §5.3 (Ben-Shahar and
  Schneider; Bakos et al.): an envelope "binds the operator" rather than informing the user. It does
  not answer Lovett's point that predictability does not end domination; an operator who declares a
  pay floor and keeps unilateral power to change it next quarter still dominates. "Hard, mathematically
  guaranteed performance boundaries" (line 405) is asserted, and who enforces the guarantee is not
  said.
- *Counter-delegation (item 4).* The draft acknowledges the agency-law problem (line 429, citing
  Kolt) but not its consequence: a user's agent is the user's instrument, so it is not a notary and
  carries no duty to the other side; and it is a new third party with interests of its own (who
  builds it, who pays for it). Dubal's finding that workers' own data collection has not changed firm
  practice is not engaged, though Dubal is cited elsewhere.
- *Refusal (item 5).* The draft says refusal must carry "no penalty or loss of standing" and gives the
  example of a human interview "without downgrading the candidate's application". It does not say how
  an employer who runs two tracks can be shown not to downgrade, nor who bears the cost of the human
  track, nor what "comparable processing speeds" (line 372) would require of a lender. Hoeksema's
  point that exit and consent are the weak answers is used, but the duty on the operator "behind it"
  (item 5) is still a slogan.

*Fix.* Write the inference out as premises and conclusion. Name the duty-bearer and the claim-holder
for each duty, and classify the duty. Where the real addressee is the legislature, say so and recast
the operator's duty as the one Young's model can carry (to support, not obstruct, the public
safeguard). Answer Lovett on envelopes, Dubal on counter-records, and the two-track cost on refusal.

### Finding 6 — Sections 6, 7.1 and 7.2 dilute the argument, and 7.2 contradicts it. **Must fix.**

*Where.* §6 (lines 439–509): Martela and Steger's three meanings of life; Winner's "authoritarian
technics"; Verbeek's scripts; three of Vallor's virtues. §7.1 (lines 513–550): an "AI Context Engine"
with a provenance layer (C2PA), an interpretability layer (sparse autoencoders, circuit tracing), a
mediation-exposure layer and an autonomy layer. §7.2 (lines 552–579): "critical algorithmacy" as a
pedagogy that trains students to "interrogate, audit, and dismantle algorithmic systems".

*What is wrong.* None of this is in the earlier outline (`../AUTHOR_DRAFT.md` §6–§7, which ended on
boundary conditions and a conclusion), and none of it is needed by the argument. §6 restates the
injury in a psychological register that the paper's normative frame (domination) already covers;
Winner's nuclear-plant example is applied to "hyperscale deep learning models" by assertion (line
495: "operate as authoritarian technologies"), and Vallor's virtues address engineers' characters,
which pulls against §2.2's insistence on institutional, not individual, agency. §7.1 is an engineering
proposal whose second layer (mechanistic interpretability delivered to a gig worker) is the "unfiltered
dump of dense statistical logic" §5.3 just condemned. §7.2 recommends a curriculum after §1, §2.1, §4.2
and §5 have argued that educational remedies address the wrong party; the table at lines 560–579 then
sets "Critical Algorithmacy" against "Traditional Digital Literacy" as two pedagogies, which is the
competence framing the paper exists to reject. The two-sentence hedge (line 554: architectures "will
fail if our educational institutions continue to preach passive compliance") does not reconcile them.
The paper also stops applying its own method here: nothing in §6–§7.2 is tested against the three
internal benchmarks.

*What I would cut.* All of §6, §7.1 and §7.2, and the HIAG passage of §5.3. That returns roughly 3,000
words to a 12,000-word limit, which the paper needs for findings 4 and 5. If the author wants one
element kept, Verbeek's point that the intermediary scripts behaviour before deliberation belongs in
§4.3 as part of the plasticity divergence, in a paragraph, not a section.

### Finding 7 — The paper misreads two BEQ articles and is unfair to a third. **Should fix.**

Checked this session against Crossref abstracts (abstract depth only; I could not open full texts).

- *Kim and Routledge (2022).* The draft (line 11) uses them for "grounding a moral right to an
  explanation" and (line 272) says advocates of explainability "operate on the assumption that if an
  algorithm explains its outputs, the user's autonomy is restored (Kim & Routledge, 2022)". Their
  abstract (DOI 10.1017/beq.2021.3) grounds the right in trust: informed consent reconceived as an
  assurance of trust for incomplete transactions, supporting a right to ex post explanation. Autonomy
  restoration is not their premise. A paper that argues explanation does not cure domination can
  still be right against them, but it must argue against the trust ground, not a premise they do not
  hold. Edwards and Veale, whom the draft also cites, make the "transparency fallacy" argument the
  draft wants; attribute it there.
- *Bhargava and Young (2022).* The draft (line 62) says they "demonstrat[ed] that the employer's
  unilateral right to terminate … subjects employees to pervasive republican domination". Their
  abstract (DOI 10.1017/beq.2021.40) argues that whether employment-at-will is justified depends on a
  jurisdiction's institutional complementarities, and that critics' concerns can be addressed by public
  policy without abolishing the doctrine. That is a qualified defence, not a demonstration of
  pervasive domination. If the body of the article contains the republican claim, give the page; if
  not, the sentence reverses their position.
- *Bhargava and Assadi (2024).* The abstract (DOI 10.1017/beq.2022.41) argues from Scanlon's value of
  choice that interviews have non-instrumental value and should not be wholly replaced by algorithms.
  The draft's uses (lines 15, 266, 370, 372) are compatible, and "cf." at line 372 is the right
  marker. Their value-of-choice argument is in fact the closest thing in BEQ to the paper's "right to
  structural refusal"; the paper should build on it rather than cite it in passing.
- *Scherer et al. (2023).* Cited (line 11) for "disclosure and individual upskilling rarely alter the
  distribution of power". Their abstract defines organized immaturity as the reduction of capacities
  for public use of reason and proposes both disorganizing immaturity and organizing maturity, the
  latter a capacity-building remedy. The draft's citation is at best adjacent and may run against
  them. This is also the guest editors' introduction to the special issue most like the one the
  author is targeting; engage it as such.
- *Hsieh (2008).* See finding 2: no such article.

*Fix.* Re-read each against the full text and cite for what it says. Engage Bhargava and Assadi's
value-of-choice account in §5.2 and Scherer et al.'s organized-maturity remedy in §5, since both are
positions the paper's thesis must answer.

### Finding 8 — The method section promises selection and disconfirmation procedures the paper does not have. **Should fix.**

*Where.* §1 (line 17): "Treating this history as empirical evidence". §2.3: three benchmarks.

*What is wrong.* The paper says how a practice qualifies as a failure, not how the five practices
were chosen, how many candidates were examined, or what would have counted against the thesis. The
arm's record holds counter-cases the paper does not mention:

- A literacy franchise that *widened* the electorate: Italy's 1882 law enfranchised men who had
  passed the compulsory elementary course, and electors rose from 621,896 to 2,049,461
  (`M5_wider_cases.md` line 91; `LITERATURE_TO_ADD.md` §2 item 6). The gate was not always an
  instrument of exclusion.
- Bans that leaked: the Ems Ukaz has "a record of leakage" (`M5_wider_cases.md` line 140); "Many of
  these bans leaked" (`LITERATURE_TO_ADD.md` §3 item 8); Margo notes Williams does not test whether
  the Southern laws were effective (`T_adjudication.md` §9.5).
- Safeguards that documented more firmly than abuse: facet G "found no petition by an illiterate
  party against a notary or scrivener" and records safeguards "more firmly than it documents abuse"
  (`T_adjudication.md` §8.1), against the draft's "scribes routinely defrauded illiterate citizens".
- Workers who do gain leverage: Cameron (2024) finds covert "engagement" and "deviance" tactics
  (`M2_algorithm_studies.md` line 49). The draft cites Cameron at line 276 for the opposite ("zero
  power").
- A court that rejected the read-aloud analogue: *Hill v. Gateway* says a telephonic recitation of
  terms "would anesthetize rather than enlighten" (`M3_intermediaries_records.md` lines 15, 115). The
  draft cites *Hill* (line 330) for the proposition that nobody reads form contracts and does not
  answer the court's point, which is aimed at the paper's own remedy.

The benchmarks also fail on the paper's third practice. Benchmark 1 requires contemporaries to
condemn; for record over voice the condemnation comes from courts a century or two later ("Centuries
of judicial doctrine gradually recognized", line 167), and `T_adjudication.md` §5 notes that row 3
"rests mostly on what later courts said". The draft bridges the gap with affected ignorance (line 78:
scribes and judges "chose not to see"), but Moody-Adams's test is "choosing not to know what one can
and should know", a person's choice requiring interest and refusal to examine; the arm's reading is
that the paper "can claim plausibly … It cannot claim proof" (`T_adjudication.md` §9.4 item 3). The
draft asserts.

Note too that the paper judges the past by internal standards and says presentism forces this (line
70), while its own authority, Moody-Adams, argues against the "own day" defence (CHECK B6;
`L3_library_reads.md` line 50). The choice of internal standards is defensible; the reason given for
it is one the cited source rejects.

*Fix.* Add a paragraph on case selection (what was searched, how many candidates, which were set
aside and why), and name the counter-cases above with what they do and do not show. State the
affected-ignorance claim for scribes and judges as plausible, with the interest and the refusal to
examine shown, or drop it. Give the real reason for internal standards.

### Finding 9 — The analogy is asserted in §4, not disciplined. **Should fix.**

*Where.* Line 230 "map with disturbing precision"; line 276 "this exact dynamic"; line 586 "these
exact institutional patterns". The §4.1 table's third column is the discipline, and it is good: it
records that the present gate tests compliance not competence, that opacity rests on trade secrecy not
statute, that monopolies rest on capital not charter. But each of those is a reason the mapping is
*not* exact, and the prose around the table says the opposite.

Two further tensions. §4.2 argues that comprehension gave Douglass no power; §4.3 argues that because
text was stable, "once an excluded group learned to read, that skill could be turned against the
ruling class". Both can be true at different scales, but the paper does not say so, and a reader will
see §4.3 take back what §4.2 gave. And §4.5 (line 336) says the record "proves that whenever a
communication medium is made a compulsory condition … the institutions controlling the medium
reliably leverage it for domination": five cases from one legal family plus Italy's counter-case do
not prove "whenever" and "reliably".

*Fix.* Let the third column govern the prose: say the positions recur and the mechanisms differ.
Reconcile §4.2 and §4.3 by stating what comprehension does and does not buy (Dubal, p. 1984:
"Knowledge alone will not end or mitigate the precarities of digitalized pay", with Cameron's covert
leverage as the qualification). Replace "proves … whenever … reliably" with what the cases show.

### Finding 10 — The novelty claim is honest in the introduction and overstated in the contributions. **Should fix.**

§1 (line 11) now positions the paper against Vee and Kamperman and Graff as centring "the skill and
its overpromised returns rather than the institutional positions". That is fair and matches the arm's
gap search (`T_adjudication.md` §9.1, §10 item 2: none of Brandt, Vee, Edwards and Veale, Street or
Kamperman and Graff has the five practices or the triad). But:

- Brandt's sponsors already "regulate, suppress, or withhold literacy and gain advantage by it"
  (`LITERATURE_TO_ADD.md` §1). The draft cites Brandt (line 52) for sponsorship and then says the
  intermediary "does not merely sponsor". The distinction the arm drew, that her sponsor stands
  between a learner and literacy while the intermediary stands between two people and an outcome, is
  the paper's real difference from Brandt, and the draft does not state it.
- Contribution 1 ("replaces the diffuse charge that 'society' failed") answers a charge nobody in the
  cited literature makes; it was the author's own earlier framing (`T_adjudication.md` §3 item 1).
  Contribution 2's "shifting the ethical locus from competence to position" is the paper's genuine
  advance, but Edwards and Veale already moved the duty "to system design" and Street already
  untethered literacy from the autonomous model; the draft cites both and should say in one sentence
  what it adds (the positions, named; the historical warrant for them).
- Contribution 3's two divergences: `T_adjudication.md` §8.1 shows the historical third party also
  committed binding text, so plasticity and the self-reviewing intermediary are the surviving
  divergences, as the draft says. The "self-interested scribe who is legally permitted to review their
  own work" (line 330) is the best sentence in the paper and the arm's facets agree it is the
  strongest point (`M2_algorithm_studies.md` line 154). It deserves to be the thesis of §4.4 rather
  than its closing flourish.
- Line 54 attributes to Kamperman and Graff the view that Street's critique of the autonomous model
  "applies with equal force to modern technology". The arm's full read of their article
  (`L2_graff_kamperman.md`) records no mention of Street; their objection is to "literacy uncritically
  as a metaphor" (p. 35). Verify or re-attribute.

*Fix.* State the Brandt difference. Reframe contribution 1 as the move from a collective to an
institutional subject of blame, which is what §2.2's Moody-Adams argument does. Verify the Street
attribution.

### Finding 11 — Rhetoric outruns evidence at these points. **Should fix.**

A normative journal accepts conviction; these overstate what the paper has shown.

| Line | Phrase | Why it overclaims |
| --- | --- | --- |
| 54 | "dismantles the idea that digital equity can be achieved through user education" | §2.1 is a definition; the argument comes later |
| 78 | "They chose not to see the structural violence encoded in their scrolls" | Asserts affected ignorance as fact; see finding 8 |
| 230 | "map with disturbing precision" | The table's third column records imprecision |
| 272 | "shatters this premise" | One case (Douglass) and a misattributed premise (finding 7) |
| 276 | "zero power" | Cameron, cited in the same paragraph, finds covert leverage |
| 288, 324 | "complete absence", "Zero External Procedural Buffers" | Contradicts the abstract's narrowed claim and the EU provisions the draft itself names |
| 330 | "brutal performance quotas"; "historically unique" | Uncited; and the Stationers' wardens also reviewed their own trade |
| 336 | "proves that whenever … reliably leverage it for domination" | Five cases, one counter-case unmentioned |
| 342 | "irreconcilable ethical contradiction" | Walzer's test is applied in two sentences |
| 364 | "empty corporate rhetoric" | Khan and Pozen's point is stronger stated as they state it |
| 378 | "Decades of research … confirm" | Two sources |
| 405 | "hard, mathematically guaranteed performance boundaries" | No mechanism of guarantee is given |
| 473 | Significance "is extinguished"; "statistical training debris" | Unargued |
| 495 | "operate as authoritarian technologies" | Winner's criterion is applied by assertion |

Also "Human Subject A / B" and "Extracted Surplus" in the §2.1 diagram import a vocabulary the paper
does not otherwise use or defend.

### Finding 12 — Smaller points. **Consider.**

- Line 11: Jobin et al.'s counts are of guidelines that *name* each principle (CHECK A5); "found
  non-maleficence named in 60" is now right. The next clause, that the remedy "most frequently
  derived" from non-maleficence is to inform the person, is not Jobin et al.'s finding and needs a
  source or softening.
- Line 15: Stark and Vanden Broeck (2024) is cited for the triad definition. No facet in the arm
  records what that paper says (`grep` across `facets/` finds no entry). Confirm it supports "reads
  both and enforces an outcome binding on both".
- Line 15, 268: Rosenblat and Stark p. 3771 for template replies from a closed ledger. The arm never
  verified this locator (CHECK A12: "No citation, and none verified"). Confirm the page.
- Line 143: the Voting Rights Act of 1965 suspended tests where its formula applied; the 1970
  amendments barred them nationwide (CHECK C4). "Dismantled … through the Voting Rights Act of 1965"
  is loose.
- Line 165: "Over 500 chiefs signed" is p. 386 of the Tribunal report, not pp. 355–358 (facet G, line
  214). "The colonial administration immediately enforced the English text" is not in the pages the
  arm read. And "whose textual ambiguities served Crown expansion" states one side of a dispute the
  Tribunal reports without ruling: Belich, Moon and Fenton argue deceit; Ward, Head, McKenzie and
  Owens reject it (facet G, line 214). Report the dispute.
- Line 70: Walzer (1988) *The Company of Critics* is cited for the method of internal critique; the
  arm's quotation for that method ("The same men and women who act badly create and sustain the
  standards…", p. 42) is from the Tanner lectures, *Interpretation and Social Criticism*
  (`M4_ethical_frameworks.md` line 138). Confirm which Walzer carries the method.
- Line 211: Giesler and Veresiu's responsibilization is a consumer-culture construct; calling
  nineteenth-century literacy promotion "an early form of" it reverses the chronology of the concept.
  Say the practice is older than the name.
- Line 62: Muldoon and Raekstad's dominator is owners and managers as a group agent; "gig economy
  platforms subject workers" elides that.
- §2.1 diagram and §4.4 diagram: the second shows the operator and the intermediary as separate boxes
  feeding one black box, which is the finding-4 problem drawn.
- Line 209: "The targets were roundly missed" is right for Dakar; Jomtien's halving was a proposal
  "countries may wish" to adopt (CHECK B10). "Explicit mandates" (line 209) overstates Jomtien.

## 3. What works and should be protected

- The reversal in the first two paragraphs of §1: the wrongs were committed *with* literacy by whoever
  held the test, the access and the record. Knox, Auld and the treaty cases carry it. This is the
  paper.
- The self-reviewing scribe (§4.4, line 330) and the two-roles point (line 328). The arm's facets
  independently identify this as the strongest comparison. Make it the spine of §4.4 and of the
  record duty.
- The §4.1 table's third column, which does the disciplining the prose refuses to do.
- §5.3's answer to the disclosure objection: an envelope binds the operator, a notice burdens the
  user. Keep, and extend to Lovett.
- §5.1's use of Khan and Pozen against Balkin: divided loyalties defeat the fiduciary model. Sound and
  well placed.
- The internal-critique benchmarks of §2.3 and their application to present firms in §5 (line 342),
  which answers the asymmetry objection a philosopher would press. Extend the application.
- The Waitangi paragraph's correction from the first draft (Henry Williams named; *kawanatanga* and
  *tino rangatiratanga* distinguished).
- The restraint of §3.6 in refusing to call residential schools a failure of literacy.

## 4. What I could not check

- Full texts of Kim and Routledge, Bhargava and Young, Bhargava and Assadi, Scherer et al. and
  Muldoon and Raekstad: Crossref abstracts only. The Crossref fetch for Bhargava and Assadi was
  rate-limited once (HTTP 429) and succeeded on retry.
- Pettit (1997), Young (2006) beyond the arm's reading, Fricker (2007), Street (1984), Vallor (2016),
  Verbeek (2005), Winner (1980), Martela and Steger (2016), Yeung (2016) beyond facet X's partial
  read: not opened this session.
- Whether Hsieh has a 2008 BEQ article under any title: Crossref returned none for the title given;
  I did not search the whole BEQ 2008 volume.
- The three quotations in finding 3 (Moody-Adams "engine of moral blindness", Cleveland 1897, Milton
  "brocards"): unverified against the texts; the arm's facets record different words at the same
  locators.
- Rosenblat and Stark p. 3771; Stark and Vanden Broeck (2024); Zong and Matias's actual content
  against the draft's use of it.
- Word count against BEQ's 12,000 limit; I did not count, and I do not know whether the diagrams
  count.

## 5. Recommendation and the three changes that would most improve the paper's chances

**Major revision.** The idea is worth a BEQ paper. The manuscript is not yet that paper.

1. **Cut §6, §7.1, §7.2 and the HIAG passage, and remove every machine token.** This removes the
   contradiction with the paper's own thesis, the uncited model and the generated-text signal, and
   returns the words needed for the next two items.
2. **Write the inference out.** Name the dominator as an agent; check Pettit's three conditions for
   each present case; say who owes each duty, to whom, and of what kind; and say why domination yields
   these duties on this party rather than constraints on it from the state. Read Pettit before doing
   so.
3. **Restore the corrected facts and fix the reference list**, then re-read Kim and Routledge,
   Bhargava and Young and Scherer et al. in full and cite them for what they argue. A BEQ referee will
   read those three before anything else.
