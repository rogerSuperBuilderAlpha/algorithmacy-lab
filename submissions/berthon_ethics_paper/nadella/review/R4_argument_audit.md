# R4: audit of the argument's logic

*Run R4, 2026-10-24. Agent-drafted. The author has not reviewed it. Scope and rules: `BRIEF_R.md`; `../facets/BRIEF.md` §6.
This file reviews substance and logic only. It proposes no wording.*

## 1. Scope

- **Premises:** A1–A8, CA; B1–B3, CB (`../ARGUMENT_AND_OUTLINE.md` v2, Part 1).
- **Draft passages** (`../manuscript/DRAFT_v1.md`, read whole): opening 26–92; §1 94–140; §2 142–289; §3 291–440; §4 442–510;
  §5 512–552; footnote 554.
- **Ledger rows:** every row of `../../consolidation/CONCEPT_LEDGER.md` (K01–K15, H01–H29, N01–N17, E01–E18, D01–D10,
  O01–O08, L01–L06, M01–M10). The ledger has no "I" section; BRIEF_R's "ledger M, E, I rows" for R2 names a section that
  does not exist in the file.
- **Cards opened** (Key facts, Where the argument uses it, S2 block): every card named in the Support column of A1–A8
  and B1–B2, every card the draft cites, and the D-row cards the duties lean on (list in §2). I reopened no `local_path`
  file: the S2 blocks of all 106 new cards record a string match of every quotation against the file at `local_path`
  (`../facets/ADJUDICATION.md` §3), so the cards' quotations are the checked text and I treat them as such. Where a
  card's basis is second-hand (Saenger, Parkes) I say so.
- **Other inputs:** `../COVERAGE_PREMISES.md` v2; `../facets/ADJUDICATION.md`; `../facets/N6_counter_case_and_gap_search.md`
  §§(c)–(d); `../RESEARCH_PLAN.md` M1–M11; `../README.md` rulings; `../manuscript/DRAFT_NOTES.md`; the local capture of
  Nadella's post (P1–P21, for locator checks only).

## 2. Search log

No external search, fetch or database call was made in this run. No new source was opened, so no new card and no
`R4_argument_audit.bib` exist. Reads, in order:

| # | File | What was taken |
|---|---|---|
| 1 | `review/BRIEF_R.md`; `facets/BRIEF.md` | rules and format |
| 2 | `ARGUMENT_AND_OUTLINE.md` v2 | the premises, their Support and Sinks-it columns, calls taken by default |
| 3 | `manuscript/DRAFT_v1.md` (lines 1–774) | every passage carrying a premise, by line |
| 4 | `COVERAGE_PREMISES.md` v2; `facets/ADJUDICATION.md` | premise status after the audit; §6 rows |
| 5 | `consolidation/CONCEPT_LEDGER.md` (181 lines, all rows) | row-to-premise map |
| 6 | `manuscript/DRAFT_NOTES.md`; `README.md`; `RESEARCH_PLAN.md` M1–M11 | locators still open; rulings; move-failure pairings |
| 7 | `~/iit-playground/berthon_ethics_local/nadella/x/nadella_2026-10-10_models_as_insider_risks.txt` | P-number checks of every post quotation in the draft (26 checked; all exact) |
| 8 | `facets/N6_counter_case_and_gap_search.md` §§(c)–(d) | the counter-case ranking |
| 9 | Cards, `literature/cards/berthon_ethics_paper/`: lovett2026republicanism, hamilton2025digital, bartha2019analogy, seele2022greenwashing, ketokivi2017reasoning, vonsamson2025immanent, walzer1988interpretation, celikates2023critical, kugelberg2026practice, gowans2026moral, moffatt2024air, eu2016gdpr, eu2024productliability, luchs2026taking, diamantis2025danger, kingston2026social, lindman2023big, calo2012against, frahm2022fixing, boretius1883capitularia, statutesrealm1817vol3, starchamber1637decree, deazley2008commentary1586, commons1803journal, manuzio1564index, reusch1883index, parker1877south, lely1883judicature, israeli2022requerimiento, virginia1831acts, northcarolina1831acts, unesco2015education, cranmer1846miscellaneous, furnivall1871four, pennsylvania1851minutes, spain1805novisima, simon2005impact, microsoft2026audit, microsoft2026responsible, openai2026reasoning, anthropic2026thinking, microsoft2026copilot, anthropic2025consumer, microsoft2025multistage, anthropic2026measuring, shavit2023practices, eu2024aiact, california2025transparency, corporateeurope2025bias, europeancommission2025reply, elmergawi2026introducing, microsoft2026overview, google2026agentic, parikh2025powering, palod2026evaluating, zhang2026hansel, openai2026agent, felt2012android, chiang2022exploring, sharon2024regulating, cjeu2024publicresource | Key facts, Where the argument uses it, S2 |
| 10 | Cards, `literature/cards/berthon_ethics_course/`: microsoft2022responsible, arber1875transcript, lestrange1934graucob, upton1875tribilcock, alabama1901official, katzenbach1966south, gaston1969gaston, unesco2000dakar, spain1944reglamento, sudore2006use, uk1987noncontentious, jones1899meehan, statutesrealm1819vol5, microsoft2026application, nadella2025looking, smith2025microsoft, nadella2026models, jobin2019global, garciaruiz2026can, kolt2025governing, zong2024data, nussbaum2011creating, hoeksema2023digital | same |
| 11 | Cards, `literature/cards/dxd_foundation/`: knox1968silent, saenger1997space, parkes1992pause | same; basis noted |

## 3. Entries

### 3.1 Argument A in explicit form, and the hidden premises it needs

**What the draft says.** Lines 72–78 state the inference: the moves "pair, one by one" with failures that met one of
three internal standards; the pairing "rests on the property each historical verdict turned on"; the present wrong
"does not follow from the past one by itself" but from broken professions and from domination. Line 548 adds "It
imputes no motive to Nadella or to Microsoft". Lines 44–46 give the four questions; lines 96–135 the three steps.

**Explicit form.**

1. (A1) A medium that demands a new competence of everyone settles four questions Q1–Q4 (work of understanding, record, brake, refusal/contest).
2. (A2) Literacy's growth settled them twice; the print stage produced six failures F1–F6 (custody by an interested party; one-sided record; disclosure leaving the reading to the bound; burden of reading on the signer; competence withheld then promised; gate held by the few).
3. (A3) Each Fi failed by its era's standard Si (objection, broken profession, unmet promise).
4. (A4) Nadella's moves M1–M11 settle Q1–Q4 for the second party as the Fi did.
5. (A5) The one move resembling the correction (M6) declares its envelope to the deployer alone.
6. (A6) Each pairing (Mj, Fi) shares the property Pi on which the verdict under Si turned, with no critical disanalogy.
7. (A7) A present practice with Pi is wrong if (route 1) it breaks the actor's own professed standard, or (route 2) it places a person under uncontrolled power (domination).
8. (A8) No present condition removes Pi.
9. (CA) So, for the second party, the course is the print stage's and not the scribes'.

**Hidden premises the inference uses.** None is stated as a premise in the argument file; the draft states HP1 and
HP2 in passing and the rest not at all.

- **HP1 (transfer).** Steps 2–3 and 6 do no normative work unless step 7 holds; "wrong by the era's own lights" transfers to today only through route 1 or route 2. The draft says this (lines 76–78). It follows that A2, A3 and A6 establish the *descriptive* claim "repeats the print stage" and nothing more; wrongness rests on A7 alone. The draft's reply to the ornament objection (lines 449–455) accepts this. The argument file should say that A6 serves the classification, not the verdict.
- **HP2 (position, not intent).** The draft disclaims motive (line 548) and the ledger's L02 says the analogy compares positions. But the verdicts the paper cites for F5 and F6 turned on intent: *Katzenbach* found tests "specifically designed to prevent Negroes from voting" (`katzenbach1966south`, p. 310) and "instituted with the purpose of disenfranchising Negroes" (pp. 333–334); North Carolina's preamble gives its ground as reading's "tendency to excite dissatisfaction" (`northcarolina1831acts`); Knox's stated aim was "to establish white supremacy in this State" (`alabama1901official`, p. 8). Under Bartha's prior-association test (`bartha2019analogy`, §3.5.2) the property that connected the gate to its verdict included purpose. A present brake with no exclusionary purpose therefore lacks the verdict-bearing property, which is a critical disanalogy. HP2 is false for the gate and the withheld-competence pairings and holds for custody (Commons 1695 objected to the Company's position, not its motives), the one-sided record (Easton) and the burden of reading (Maugham L.J.'s regret concerns the rule).
- **HP3 (duty-bearer).** A7 route 1 judges Nadella's architecture by Microsoft's Responsible AI Standard. That Standard binds Microsoft's product teams as *developer* ("Applies to: All AI systems when the intended use of the generated outputs is to inform decision making by or about people", `microsoft2022responsible`, p. 9); Nadella's "we" is the *deployer* (`nadella2026models`, Relation to the argument). The draft's fourth duty hands A5.4 to "the operator" (lines 527–530) and the refund example to the deploying organisation (535–540). The chain-of-thought withholding is the *model provider's* (`openai2026reasoning`; `anthropic2026thinking`), and the standards capture is the *industry body's* (`corporateeurope2025bias`). The argument needs a premise that says which party owes which duty, and why the deployer rather than the provider or a regulator is the addressee of D02–D08. B2 ("whoever designs and runs the system") names two parties and picks neither. Ledger N06 (Young's social-connection model, "who else must act") exists for this and is unused.
- **HP4 (completeness of the frame).** The four questions omit *who carries the loss*. The corrections the draft itself counts strongest shift risk (D06 "carry the risk"; `jones1899meehan`, pp. 10–11, construes against the drafter), and the law the fourth objection concedes (PLD, Moffatt) answers that question and no other. A1 needs a fifth question or D06's second half has no slot in the frame.
- **HP5 (two courses are exhaustive).** CA's "not the scribes'" presupposes that a course is either the correction or the failure. The draft's own first moment refutes this: the scribes' correction ran under custody held by ruler and church (lines 166–172; `boretius1883capitularia`, pp. 80–81), so a course can move work onto the artifact *and* fail Q2. The clean contrast the title and abstract draw does not exist in the record as the draft presents it. What distinguishes the courses is the beneficiary of the move (README pushback 1), and CA should be stated as "takes the print-stage course on custody, record and reading for the second party, and makes no move onto the artifact that serves her", not as a dichotomy.
- **HP6 (the products implement the post).** A4 reads OpenAI's, Anthropic's and Google's documents as "the products that implement" Nadella's essay (line 296). They do not; they are vendor practice the essay neither governs nor cites. The claim they support is "industry practice gives the second party none of the four", which is a different premise from "Nadella's moves settle the questions the print-stage way".
- **HP7 (silence allocates).** The post never mentions the second party except at P20. The draft reads that silence as an allocation ("leaves her the reading", line 50). The inference holds only if some work remains for her; for the refund customer the residual work is contesting an outcome, not reading a text, which is Q4, not Q1. The draft should state the premise and confine it.
- **HP8 (ex post remedy is not control).** Route 2 answers the fourth objection by "remedies after the harm, not voice or brake before it" (A8; lines 478–479). On Lovett's procedural view, non-domination requires constraints "resilient over a wide range of possible changes" (`lovett2026republicanism`, §2.2), and Pettit's contestatory conditions are reasons open to debate, inclusiveness and impartial "courts of appeal" (§4.2). Courts of appeal are ex post. The paper needs the premise that a remedy confined in subject matter (PLD damage heads, `eu2024productliability`, Art 6(1); GDPR personal data only) and dependent on a record the person does not hold is not control in the republican sense. The draft hints at the confinement (line 478) and never connects the one-sided record to the unusability of the remedy, which is the connection that would make the premise true.

**Verdicts:** HP1 contested (rests on A7); HP2 wrong for F5/F6, holds for F1, F2, F4; HP3 contested; HP4 narrower;
HP5 wrong as a dichotomy; HP6 narrower; HP7 narrower; HP8 contested.

### 3.2 Argument B in explicit form

1. (B1) The corrections moved work or record to the artifact or to a party owed to the weaker side; the strongest checked understanding.
2. (B2) Where failures turned on positions, the duty falls on whoever designs and runs the system.
3. (B3) LLM tools reproduce those positions for the second party (= CA).
4. (CB) Designers owe six duties, each the inverse of a failure, each with a working precedent.

CB does not follow from B1–B3 without a bridge from "a correction worked" to "a correction is owed". That bridge is
A7: a duty is owed where the operator professes the standard (route 1: T1.3/A5.4 give D06) or where non-domination
requires it (route 2: contestation gives D02, D04). Nothing in B1–B3 says why D07 or D08 is *owed* rather than
available. A second missing premise is feasibility at the agent's speed and scale (N6 rank 6), which the draft's §4
does not raise. The per-duty findings are in §3.5.

### 3.3 Equivocation: eleven terms tracked across the draft

Each row gives the senses, the lines where the sense shifts, and the verdict.

| Term | Sense in the record (§2) | Sense in the present (§3–5) | Shift | Verdict |
|---|---|---|---|---|
| record | the instrument that binds the weaker party or stands for her hearing: the requerimiento's *testimonio* (lines 242–250), treaty minutes (270–274), the notarial note (268–270) | the operator's internal audit log of agent activity (339–346; `microsoft2026audit`: "which user interacted with Copilot, when ... and where") | The Purview log is not the record that binds the customer; the binding artefact is the decision (the denial). Line 346 pairs the log with the requerimiento's "record made and held by one side", but the *testimonio* was made to bind its addressee and the log is made for the tenant's security. The property the Israeli verdict turned on (the answer dropped from the record, p. 47; record as "self-legitimation", p. 62) is present only if the record in question is the record of the decision toward her | misused at 346–351; repairable by naming the decision record |
| custody | custody of the medium or its convention for a whole realm: the charter's monopoly over printing (182–189), licensing of all books (199–202), the ruler's authority over the page (166–172) | custody of one organisation's own agents' limits (301–311); custody of standards (325–335) | The Stationers' custody excluded every other printer and was judged a wrong for that reason (`commons1803journal`, reason 12: "the People compelled to buy their Freedom of Trade ... from the Company"). An organisation's control of its own agents excludes no one from the medium. The property the 1695 verdict turned on is present in the standards paragraph (JTC 21, `cjeu2024publicresource` paras 70–75) and absent from the envelope paragraph | narrower: the custody pairing holds for P6, not for P17 |
| reading | decoding a written text one is bound by (231–240, duty to read) | verifying an agent's output or interpreting its trace (353–362, 392–400) | The verifying duty in the terms falls on the *user who requested the action* ("When you request that Copilot take Actions on your behalf", `microsoft2026copilot`), a principal, not on the person acted on. The signer in *Upton* was also a principal who signed. So the pairing holds for the user and not for the second party; line 398 ("for the person at the end of the chain") carries it over without a premise | narrower; holds for the user, unsupported for the second party |
| brake | none in the record; §3.3 supplies "the gate ... and the license" (385–388) | P19's pause or shutdown of a model mid-task | A gate decides who may use the medium; a brake stops a running process. The gate's verdict turned on exclusionary design and discriminatory administration (`katzenbach1966south`, pp. 310–312), not on the voter's lack of a stop. No contemporary objected that the person acted on lacked a brake, so by A3's own rule the pairing drops out of Argument A and rests on route 2 alone. The draft does not say so (387–390) | misused |
| envelope | — (A5's term; the "convention" of §2) | (i) runtime security policy on tool calls, defined by "a security or compliance team" (`elmergawi2026introducing`); (ii) D03's outcome-level commitments toward the person (521–524); (iii) AP2's user-signed constraints (319–323) | Sense (i) is not "toward" the person in sense (ii): an email agent that "must not send messages to external recipients" protects the tenant. Line 322–323 picks AP2's wrong property: the mandate is signed by the *principal* (the user), which in Nadella's frame is the organisation; the feature that bears on D03 is the counterparty's verification, and only "constraints relevant to the closed Mandates are shared with the verifier" (`google2026agentic`, Modes). §5 (523–524) gets it right | narrower |
| second party | defined at 48–49: customer, applicant, counterparty | §3.2: "The person on whom an agent acts keeps nothing" (345–346) holds; §3.3: Copilot consumer users (392–397), expense requesters (`microsoft2025multistage`), Claude Code users (`anthropic2026measuring`) are users or employees of the deploying side | Half of §3.3's evidence concerns the agent's principal or the organisation's own staff. The thesis is stated for the outside counterparty (CA), so that evidence supports A8 (capacity of the authorised person) and not A4 | misused at 392–400; the user evidence needs relabelling |
| print stage | the moment a medium reaches everyone and institutions govern its distribution (56–61) | a type of allocation (custody, record, reading, brake, gate) | Moment 3's failures (duty to read 1875–1934; tests 1901; acts 1831; Dakar 2000) are not print-era; the draft calls them "literacy demanded of the bound". CA's "print stage" is a label for moments 2 and 3 together. The title promises a print analogy the body only half delivers | narrower |
| scribes' correction | word separation moving the reader's parsing onto the page, for readers the old script excluded (149–164) | P11–P12 moving the deployer's trust-work onto a policy engine (301–305) | The beneficiary differs (reader vs deployer), which the draft notes (305, 311). The deeper problem is HP5: the first moment itself ran under custody (166–172), so "the scribes' course" is not custody-free | narrower |
| literacy | the ability to read and write (231–266) | "AI literacy", skilling credentials (425–431) | For the second party no competence is specified: the refund customer needs standing, not skill, and the draft's own D07 says "None of the six asks her to read more" (543). F5 ("competence withheld, then promised") therefore has no object for the second party; what Nadella promised (2025 ¶4) is addressed to users of AI, not to those acted on | narrower |
| disclosure | (i) the instrument read aloud to the person it binds, before it binds (242–250); (ii) notice on a ticket (237–239) | (iii) chain-of-thought exposure to the deployer (353–357); (iv) incident disclosure after failure (411–423) | The requerimiento was read *before* the act to legitimate it; P20 informs *after* a failure and binds no one. Line 421–423 pairs them on "informed after the fact", which is not the property the Israeli verdict turned on (the dropped answer and the absent court). Sense (iii) concerns the deployer, not the second party | narrower |
| scaffold | — | (i) Nadella's "scaffolding for human potential vs a substitute" (`nadella2025looking`, ¶4), a product-design metaphor about amplification; (ii) "rich scaffolds that orchestrate multiple models" (¶5), systems architecture; (iii) D08's learning-science scaffold, contingent and withdrawn (532–533, 507–510) | Lines 425–427 and 503–505 treat sense (i) as a promise of sense (iii). Nadella promised neither owed nor withdrawn support; he named a design aim. O08 and D08 then answer a promise he did not make in that sense | misused |

### 3.4 Support: each premise against the draft passage and the cards

**A1 (lines 44–46, 96–102).** The frame is offered "as an analytic frame, not as a finding" (99). Lovett §4.2 and
Hamilton p. 5 carry Q4 only (ADJUDICATION §6). Q1–Q3 are unsourced and the draft says so. The omission of a risk
question (HP4) is the gap. **Narrower.**

**A2 (lines 149–289).** Moment 1: Parkes p. 1 and Saenger pp. x, 83, 85, 87, 100 are quoted verbatim (156–162, 166,
175). The arm's only cards for both books (`dxd_foundation/saenger1997space`, `parkes1992pause`) are marked "⚠ Not read
in full" with content "second-hand" from earlier facets; `DRAFT_NOTES.md` says the pages were confirmed on Google
Books and a lending scan in AUDIT_01 and AUDIT_06, which are outside this arm's cards. R1's call; for the argument the
first moment carries no verdict and is used only to define the correction, so the exposure is small. Boretius pp. 80–81
hold. Moment 2: Arber xxviii–xxxi, Star Chamber 9–10 and 16, 14 Car. II §§ II and X, 34 & 35 Hen. VIII p. 896,
Cranmer p. 121, Furnivall p. 64, Index p. 15, Reusch pp. 334–336, Commons reasons 3 and 12 all hold on the cards. Two
notes: the 1577–1586 printers' voices (191–198) are quoted through Deazley, whose card says "Quote these voices in the
paper only after a library check of Arber vol. 2"; the draft cites Deazley, which is honest, and the check is open.
Line 216 "not at the request of those it barred" has no source. Moment 3: *Upton* p. 50, *L'Estrange* 403 and 405,
Israeli 47–48 and 62, Alabama 8 and 11, *Katzenbach* 310 and 312, *Gaston* 293, Virginia 107, North Carolina's
preamble, Dakar 7(iv), UNESCO 2015 p. 135 hold. *Parker* p. 423 is quoted for the presumed reader (238–239), which is
exact, but the summarising sentence (239–240, "the courts treated it as done") runs against the case: Mellish L.J. held
"The plaintiff was certainly under no obligation to read the ticket" (`parker1877south`, p. 423) and Baggallay L.J.
put the onus on the company (p. 425). **Narrower:** the six failures are carried for F1–F4 and F6; F5 has no object
for the second party (§3.3, "literacy"); the dichotomy is not clean (HP5).

**A3 (lines 191–198, 204–216, 220–224, 249–250, 262–266, 270–274).** Holds for custody (Commons 1695; the printers of
1577–1586 at secondary depth), for the one-sided record (Easton 1757: Teedyuscung and four commissioners "in writing",
`pennsylvania1851minutes`, pp. 656–657), for the burden of reading (Maugham L.J., p. 405), for 1543 by the broken
profession (the Act's preamble, p. 896; Cranmer p. 121) with the *Supplication* "probable, not established"
(`furnivall1871four`), for Dakar by the unmet promise. Does not hold for Rule IV (Reusch records non-enforcement, "not
as a wrong", card), for the brake pairing (no objector; §3.3), or for M7 (`N6` Q3; the draft concedes at 453–455).
**Narrower.**

**A4 (lines 36–52, 299–440).** Custody with the organisation (P3, P5, P17; `microsoft2026overview`), record for the
organisation (P15; `microsoft2026audit`; the Unified Audit Log gap, `microsoft2026responsible` PDF p. 19), standards
by industry (P6; CEO 55 per cent; Commission pdf pp. 13, 16; CJEU paras 70–75): hold for the second party. Four
items are weaker than the premise states. (a) "Reasoning disclosed to no one outside the supplier (P9)": P9 *demands*
chain-of-thought transparency; the withholding is the providers' (`openai2026reasoning`: "we don't expose the raw
reasoning tokens"). This is a fact about vendors that contradicts the post, not a move of Nadella's; the draft
half-says so (353–357). (b) "Responsibility for actions placed on the user": true of the agent's principal
(`microsoft2026copilot`; `anthropic2025consumer`), not of the second party (§3.3, "reading"). (c) "Notice to
authorities, not standing for those affected (P20)": P20 asks for "timely disclosure to those affected"; it is the
*law* (AI Act art. 73(1); SB 53 §22757.13) that routes notice to authorities, and the draft says the post "asks more
than the law" (412). The absence of standing is the post's silence, not its choice. (d) One product move toward the
recipient is omitted: Cowork's outputs "include attribution indicating AI assistance, ensuring recipients know when
they are interacting with AIproduced content" (`microsoft2026responsible`, PDF p. 18). A4's Sinks-it column names
exactly this kind of counter-instance; the draft should concede it as notice (not standing) to the second party.
**Narrower.**

**A5 (lines 301–323).** Holds for Nadella and Microsoft on `elmergawi2026introducing` ("who defines those
boundaries" answered by "a security or compliance team") and `microsoft2026overview`. The envelope equivocation and
the AP2 property error are in §3.3. The draft also omits `openai2026agent`'s point that OpenAI's default reviewer
policy "is in the open-source Codex repository", so one vendor's envelope is readable by anyone until an enterprise
replaces it; A5 as "declared to the deploying organisation alone" is true of the replaced policy, not the default.
**Narrower.**

**A6 (lines 104–112, and each pairing in §3).** Bartha §3.5.2 and Seele and Schultz p. 1065 are quoted exactly and
used as the cards advise (method from Seele, inference from Bartha). Applying the test the draft adopts: the record
pairing (346–351) and the reading pairing (364–369) share the verdict-bearing property; the custody pairing (313–315)
shares it only for the standards half; the brake pairing (384–390) fails it (HP2); the notice pairing (420–423)
names a different property from the one Israeli's verdict turned on; the competence pairing (431–434) has no object.
Three of six pairings pass the paper's own rule. **Narrower.**

**A7 (lines 113–135).** Route 1 is sourced (Microsoft 2022 pp. 8–9; P3, P9) and the keyword search of the 2026
report (368–369) is recorded in `microsoft2026responsible`. The duty-bearer shift (HP3) is the gap. Route 2 is carried
by Lovett §4 and Hamilton p. 5 for "the tradition travels"; whether it *condemns* is the call taken against ledger
N04 ("describe, not condemn"). The draft asserts domination (77–78, 439–440) and never shows the arbitrariness
condition: on the procedural view, uncontrolled power is power not bound by resilient common-knowledge rules
(`lovett2026republicanism`, §2.2), and the fourth objection names rules that bind it in part. HP8 is needed and
unstated. Hamilton's own concession that vendor-granted controls "create antipower for users" (p. 10) is a published
republican view that cuts against the paper and is not met. **Contested.**

**A8 (lines 442–510).** Seven objections are met. Four are missing from §4 and each is in the arm's own files: speed
and scale remove the reader on whom reader-based corrections depend (N6 rank 6; Shavit p. 12, "balloon beyond a
user's ability to feasibly keep up"), which damages D06; the cost of a second track (ledger O04), which the refund
example asserts away ("at comparable speed", 536); envelopes expose method and invite gaming, and a redeclarable
envelope leaves domination (ledger O05; Lovett's resilience condition); and Johns's null contrast class (N6 Q2: "no
Protestant state before 1695 lacked a press regime"), which bears on A3's use of 1695. The fourth objection's reply
needs HP8. **Narrower.**

**CA (lines 72–78, 436–440, 550–552).** Follows from A1–A8 only with HP1–HP8, two of which are false as stated
(HP2 for the brake and competence pairings; HP5 as a dichotomy). What survives: for the people the deploying
organisation's agents act on, Nadella's post allocates custody, record and reading as the print-stage institutions
did; the brake and the notice allocations are condemned, if at all, by the republican route alone; the post makes
no move onto the artifact that serves those people, and Microsoft's products make one (attribution). **Narrower.**

**B1 (lines 268–289).** Pragmática leyes I, III, V (p. 144–145) hold for "work or record moved"; Easton holds; grade
cards hold ("associated with a 13.1 percent decrease", `simon2005impact`, p. 32). "The strongest of them checked
understanding instead of presuming it" (285–287) overstates two of its four cases: the 1883 jurat records an officer's
impression ("seemed perfectly to understand", `lely1883judicature`, p. 276; "an impression, not a test", card), and
art. 193 sets a standard for the notary's communication and attests the parties' own declaration, "No step tests
their understanding" (`spain1944reglamento`, verifier). Probate r. 13 and teach-to-goal check; the jurat and art. 193
certify. **Narrower.**

**B2 (lines 514–518; ledger D01).** Kingston and Carnovale p. 19 is quoted exactly and used as the card describes.
"Designs and runs" names two parties (HP3). *Gaston* is the ledger's precedent for position-based duty and is not
cited in §5; it would carry B2 better than Kingston, whose precedent is "ceding power to third parties", a D04
form. **Narrower.**

**B3.** Identical to CA; follows as CA is narrowed. **Holds (given CA narrowed).**

**CB (lines 514–544).** "Each with a precedent" is false for two of six (§3.5). **Narrower.**

### 3.5 The six duties: does each follow from B1–B3 and invert its failure?

| Duty | Failure inverted | Precedent the draft gives (lines) | Does it follow? | Verdict |
|---|---|---|---|---|
| D02 structural refusal | the gate (F6) | none; "so that no single reader stands where the registrar stood" (520–521) | No. The record's correction to the gate was suspension and abolition (`gaston1969gaston`; VRA), not an alternative route. CB's "each with a working precedent" is unmet here; the obvious present precedent (GDPR art. 22 right to human intervention, ledger D02; E05) is unused. Needs the feasibility and cost premise (O04) the refund example asserts (536) | narrower; precedent unsupported |
| D03 declared envelope binding toward the people acted on | custody (F1) | AP2 (522–524) | Partly. The record's correction to custody was removal of custody (1695), not a declared envelope; the precedent is present-day and partial ("Only constraints relevant to the closed Mandates are shared", `google2026agentic`; dispute use "outside the scope"). The duty's bite depends on "the organization cannot change for her case without notice" (537), whose precedent (P2B's 15 days, ledger D03) is unused, and on Lovett's resilience condition against O05, which §4 does not raise | narrower |
| D04 counter-delegation | one-sided record (F2) | Easton 1757; Pragmática copies (524–526, 537–538) | Yes. Both halves have record precedents: the party's own clerk comparing minutes (p. 656), the party's copy on demand (ley V), the recorded answer and two notaries (Israeli pp. 47–48). The "body the operator does not control" has a thin precedent in Teedyuscung's request that the refusal "be represented to the great King" (p. 657, card) | holds |
| D06 check understanding and carry the risk | disclosure (F3) | 1883 rule; art. 193; Microsoft A5.4 (527–530) | Partly. The check half follows from B1's narrowed second limb (probate r. 13, teach-to-goal). The risk half's precedent is misassigned: the 1883 certificate governs admissibility of the deponent's own evidence (card: "protects the court's record as much as the deponent"), while the risk-shifting precedents are *Jones v. Meehan* (construe "in the sense in which they would naturally be understood by the Indians", p. 1) and *non est factum*, both in the ledger (H23, H10) and absent from the draft. A5.4 binds Microsoft as developer (HP3). The speed-and-scale objection hits the check half hardest and is unmet | narrower |
| D07 change the medium | burden of reading (F4) | grade cards (530–532, 541–542) | Partly. The grade card worked because "an independent inspector does the reading and the artefact carries a one-letter verdict" (`simon2005impact`, Where used). The draft's version is an operator-made marker about the operator's own decision (541–542), which lacks the inspector. Calo's visceral notice (ledger D07) is the operator-side precedent and would fit; the grade card fits a third-party-graded marker, which overlaps D04 | narrower |
| D08 scaffold inside the system | competence withheld and promised (F5) | none; "on the four conditions of Section 4" (532–533) | No. No historical or present precedent is named; the competence the second party must acquire is unspecified (§3.3, "literacy"); the promise it inverts is Nadella's metaphor (§3.3, "scaffold"). The nearest evidence, Chiang and Yin's model-specific interactive tutorial (card: "fits the paper's duty D08"), is cited for the null result only (429–430) | unsupported as a duty of the operator toward the second party |

### 3.6 Ledger rows mapped to premises

Rows the draft uses, by premise: **A1** K10 (implicit), N04. **A2** H01, H04, H07 (via Israeli, Easton), H11, H13,
H18, H19, H22 (via `lely1883judicature`, not `moj1998practice32`), H26. **A3** N01, H01, H13, H18. **A4** E11, E13,
E14, E05 (GDPR, PLD only), O02 (law). **A5** D03 (as the term). **A6** O03 (Bartha, Seele, Ketokivi). **A7** N01,
N04, E14. **A8** K12 (via Hamilton only), E15 (via Shavit only), O01–O03, O06–O08. **B1** H10, H22, H23, N07
(implicit). **B2** D01. **CB** D02–D08, D05, E07 (one clause), N17 (O08), K11 (Lovett quotation only).

Rows unused and relevant to a premise (each would strengthen or discipline the argument):
- **H03** (Cleveland 1897 and Wilson 1917 vetoes; "No one ended them by learning to read better"): a contemporary objection for F6 that A3 lacks, and the ledger's own evidence for O03.
- **H15** (what the record does not show; bans leaked; illiterate people used notaries): the honest bound on A2's Sinks-it column.
- **H24** (four stages): the ledger's reply to O07 ("disclosure is the second of four stages") is absent from §4's fifth objection; N6 says the reply must meet Calo's outsider-reader model, which the draft does (489–490) without the stages.
- **N02** (Moody-Adams: a thin record of objection does not clear the actors): directly relevant to the 1543 "probable objector" and to M7, where the draft lets a pairing drop for want of an objector.
- **N06** (Young's social connection: who else must act): the missing duty-bearer premise (HP3).
- **N08** (right to explanation; AI Act art. 86; CJEU *Dun & Bradstreet*): the strongest present answer to O02 for the second party; `eu2024aiact` art. 86(1) is on the card and not in the draft.
- **E05** beyond GDPR and PLD (GDPR art. 22; Platform Work Directive arts. 9–11; DSA arts. 20–21): the precedents D02 and D04 need.
- **E06** (timing, independence at first instance, separation of roles): the three gaps the law leaves, which is the fourth objection's reply in the ledger's own words.
- **E16** (AI Act art. 4 literacy; the Omnibus "support" duty): the law's answer to F5, relevant to 3.4.
- **E18** (financial education effects decay; just-in-time education "may have promise"): a second null-and-exception result for 3.4 beside Chiang.
- **K09** (the medium answers back; adaptive updates): Seele and Schultz's "fluid algorithms" break (card, p. 1070) and O05 both turn on it; it is the paper's best "changed condition" for A8 and goes unmentioned.
- **O04, O05**: objections to D02 and D03 not met in §4.
- **D09, D10**: D10 ("skill alone does not discharge the duty") is the ledger's own guard for D08 against O08.

Rows used in the draft without a premise: Frahm (432–434; ledger H13/H25) is a contribution claim (84–85) that no
premise needs; Lindman (82, 479–481) and Calo (83, 483–490) serve the objections, which is fine. The "three
conversations" paragraph (80–87) stands outside the argument.

Rows unused and parked by design: K01, K04–K08, K13, K15, H02, H05, H06, H08, H09, H12, H14, H16, H17, H20, H21, H25,
H27–H29, N03, N05, N09–N16, E01–E04, E08–E10, E12, E17, L01–L06 (L02 and L03 are partly voiced at 546–552), M01–M10.
The draft does not state L01 (the cases are narrow) or L03 (one essay, one firm's documents), which the argument file's
own "What the paper does not claim" row (Part 2, §5) promised.

### 3.7 The strongest counter-argument to CA, and whether §4 answers it

**Steelman.** The architecture is correctly scoped. Design governs the deployer's relation to the model it buys;
the deployer's relation to the public is governed by law (contract, consumer protection, data protection,
anti-discrimination, product liability). The post's silence about the second party is therefore not an allocation
of work to her but a jurisdictional division the paper itself endorses when D05 says "the concentration of the means
of AI in a few firms belongs to competition law" and "Duties are worth their enforcement" (546). On that division
the second party already holds what the paper demands: an explanation right (AI Act art. 86(1)), notice and a
judicial remedy for data breaches (GDPR arts. 34, 79), compensation for defective software (PLD art. 5(1)), and the
ordinary law that refused the double-check burden in *Moffatt* (para 28). The duties the paper derives (own record,
independent dispute body, a human route at comparable speed) are institutional, not design, duties, so CB's addressee
is the legislature, and CA mislabels a sensible division of labour as a print-stage failure. The historical pairings
add nothing, because the verdicts on the gate turned on purpose (HP2), the Stationers' wrong was exclusion from a
trade, and no literacy-era contemporary asked that the person bound hold a brake.

**Does §4 answer it?** In part. The second objection (457–463) concedes the enterprise reading and relocates the
problem; the fourth (472–481) grants GDPR, PLD and *Moffatt* and replies that no regime "gives the person a voice or a
brake before the action". That reply presupposes HP8 (ex post remedy is not control), which the draft never argues,
and it ignores the AI Act's explanation right, which gives reasons before any court and is the republican
contestation condition Lovett names (§4.2). The reply the record supports and the draft does not make is this: the
remedies are confined (PLD's damage heads exclude a denied refund, a lost job or a loan; GDPR reaches personal data
only; art. 86 reaches Annex III decisions only), and every one of them requires a record of the decision that the
one-sided record denies her, so the law's remedy is usable only if D04 is met. That turns the counter-argument into
support for D04 and bounds CA to the gap the law leaves. The first objection (447–455) answers the "history adds
nothing" limb only for separability and precedents; it does not answer HP2. So §4 answers the counter-argument on the
enterprise reading, half-answers it on law, and does not answer it on intent.

## 4. Gaps and blocks

No source was blocked in this run because none was sought. Open checks the argument depends on, with where a
Bentley library user would find them:

- Saenger 1997 pp. x, 83, 85, 87, 100 and Parkes 1992 p. 1 in a library copy (Stanford UP / De Gruyter e-book;
  Scolar Press 1992 or U. California 1993): the arm's cards are second-hand; `DRAFT_NOTES.md` cites AUDIT_01/06
  confirmations outside this arm.
- Arber, *Transcript* vol. 2 pp. 770–807 (HathiTrust or a research library) for the 1577–1586 printers' voices now
  quoted through Deazley.
- Pettit 1997 pp. 52, 62, 73–74, 107, 186–187 (OUP; Bentley Library catalogue) for the arbitrariness condition HP8
  needs; the arm has Pettit only through Lovett.
- *Jones v. Meehan*, 175 U.S. 1 (open: Caselaw Access Project, carded) and *Foster v. Mackinnon* (carded) for the
  risk-shifting precedent D06 should cite in place of the 1883 rule.
- GDPR art. 22 and AI Act art. 86 (both carded, `eu2016gdpr` superseded card and `eu2024aiact`) for D02's and O02's
  missing precedents.

## 5. Verdict table

| ID | Concept / claim | Draft lines | Verdict | Evidence (card + locator) | Fix to the argument |
|---|---|---|---|---|---|
| A1 | Four questions a medium settles | 44–46, 96–102 | narrower | `lovett2026republicanism` §4.2 (Q4 only); risk question absent (`jones1899meehan` p. 1; `eu2024productliability` Art 5(1)) | Add a fifth question, who carries the loss, or move D06's risk half out of the frame |
| A2 | Print stage produced six failures | 149–289 | narrower | `boretius1883capitularia` pp. 80–81 (custody inside the correction); `parker1877south` p. 423 ("under no obligation to read"); `saenger1997space`, `parkes1992pause` second-hand | State the two courses by beneficiary, not as a dichotomy; drop F5 for the second party or name her competence; cite *Parker* for the presumed reader only |
| A3 | Each failure met an internal standard | 191–274 | narrower | `commons1803journal` reasons 3, 12; `pennsylvania1851minutes` pp. 656–657; `lestrange1934graucob` p. 405; `furnivall1871four` p. 64 (probable); `reusch1883index` p. 335 (non-enforcement, not objection) | Holds for F1, F2, F4, 1543, Dakar; drop the brake pairing and Rule IV from A3 |
| A4 | Nadella's moves settle the four questions the print-stage way for the second party | 36–52, 299–440 | narrower | `microsoft2026overview`; `microsoft2026audit`; `cjeu2024publicresource` paras 70–75 (hold); `microsoft2026copilot` (user, not second party); P20 names "those affected"; `microsoft2026responsible` PDF p. 18 (attribution to recipients) | Keep custody, record, standards; restate CoT as a vendor fact against P9; restate responsibility as the user's; restate P20 as notice the post offers and the law withholds; concede attribution |
| A5 | The correction's envelope is declared to the deployer alone | 301–323 | narrower | `elmergawi2026introducing` ("a security or compliance team"); `google2026agentic` Modes; `openai2026agent` (default policy public) | Say "Nadella and Microsoft"; name the counterparty's verification, not the principal's signature, as AP2's relevant feature |
| A6 | Each pairing shares the verdict-bearing property, no critical disanalogy | 104–112; §3 | narrower | `bartha2019analogy` §3.5.2; `katzenbach1966south` pp. 310, 333–334 (purpose) | Three pairings pass (record, reading, standards); state that the brake, notice and competence pairings rest on route 2 or on Microsoft's professions alone |
| A7 | Wrong today by two routes | 113–135 | contested | `microsoft2022responsible` p. 9 (binds developer); `lovett2026republicanism` §2.2 (arbitrariness), §4.2 (courts of appeal); `hamilton2025digital` p. 10 (vendor controls as antipower) | Add the duty-bearer premise; argue the arbitrariness condition against ex post remedies; meet Hamilton p. 10 |
| A8 | Nothing removes the property | 442–510 | narrower | `shavit2023practices` p. 12; `seele2022greenwashing` p. 1070 ("fluid algorithms"); ledger O04, O05; N6 Q2 (Johns) | Add speed and scale, cost of the second track, envelope gaming and redeclaration, and the null contrast class |
| CA | For the second party the course is the print stage's, not the scribes' | 72–78, 436–440, 550–552 | narrower | as A2, A4, A6, A7 | "Allocates custody, record and reading as the print-stage institutions did, makes no move onto the artifact that serves her, and leaves the brake and notice to be judged by non-domination" |
| B1 | Corrections moved work or record; the strongest checked understanding | 268–289 | narrower | `lely1883judicature` p. 276 ("seemed perfectly to understand"; impression); `spain1944reglamento` art. 193 (no test); `uk1987noncontentious` r. 13 and `sudore2006use` (check) | "Certified" for the jurat and art. 193; "checked" for probate r. 13 and teach-to-goal |
| B2 | Duty falls on whoever designs and runs the system | 514–518 | narrower | `kingston2026social` p. 19; `gaston1969gaston` pp. 296–297 (unused); ledger N06 (unused) | Split developer, deployer and regulator; assign each duty |
| B3 | LLM tools reproduce the positions for the second party | — (= CA) | holds | as CA | None beyond CA's restatement |
| CB | Six duties, each inverting a failure, each with a working precedent | 514–544 | narrower | §3.5 | Supply precedents for D02 and D08 or drop "each with a working precedent" |
| HP1 | Wrongness transfers only through A7 | 76–78 | contested | `vonsamson2025immanent` p. 1318; `celikates2023critical` §2.1; `gowans2026moral` §7 | State that A2–A3–A6 classify and A7 condemns |
| HP2 | Position, not intent, grounds the verdicts | 548 | wrong (for F5, F6) | `katzenbach1966south` pp. 310, 333–334; `northcarolina1831acts` preamble; `alabama1901official` p. 8 | Confine the pairings to F1, F2, F4, where position carried the verdict |
| HP3 | The deploying organisation is the duty-bearer | 527–540 | contested | `microsoft2022responsible` p. 9 ("Applies to"); `openai2026reasoning`; `corporateeurope2025bias` | Add a premise assigning D02–D08 among provider, deployer and regulator |
| HP4 | The four questions are complete | 44–46 | narrower | `jones1899meehan` pp. 10–11; `eu2024productliability` Art 6(1) | Add the risk question |
| HP5 | The two courses are exhaustive | 60–61, 72, 551 | wrong | `boretius1883capitularia` pp. 80–81 (draft 166–172) | Define the scribes' course by beneficiary; drop "not the scribes'" as a dichotomy |
| HP6 | Vendor documents implement the post | 296 | narrower | `openai2026reasoning`, `anthropic2026thinking`, `google2026agentic` (none cites the post) | "Industry practice", not "the products that implement it", for non-Microsoft documents |
| HP7 | Silence allocates the residual work | 50 | narrower | `nadella2026models` (word counts: no "user", "customer", "people") | State it; confine to Q4 (contest) for the second party |
| HP8 | An ex post remedy is not control | 478–479 | contested | `lovett2026republicanism` §2.2, §4.2; `eu2024aiact` art. 86(1); `eu2024productliability` Art 6(1) | Argue it from confinement of the remedies and from the record they require |
| record | binding instrument vs operator's audit log | 242–250, 339–351 | misused | `israeli2022requerimiento` pp. 47, 62; `microsoft2026audit` | Pair the requerimiento with the record of the decision toward her, not with Purview |
| custody | medium-wide monopoly vs one firm's agents | 182–189, 301–335 | narrower | `commons1803journal` reason 12; `cjeu2024publicresource` para 75 | Carry the custody pairing on P6 and the standards bodies |
| reading | decoding a text one is bound by vs verifying an agent | 231–240, 392–400 | narrower | `microsoft2026copilot` ("When you request that Copilot take Actions on your behalf"); `upton1875tribilcock` p. 50 | Label the verification evidence as the user's burden |
| brake | gate vs pause/shutdown | 384–390 | misused | `katzenbach1966south` pp. 310–312; P19 | Rest the brake claim on non-domination alone and say so |
| envelope | security policy vs outcome commitment; principal vs counterparty | 301–323, 521–524 | narrower | `elmergawi2026introducing` (worked example); `google2026agentic` Modes | Define the envelope as D03 does before pairing ACS with it |
| second party | outside counterparty vs user or staff | 48–49, 392–400 | misused | `shavit2023practices` p. 5 (parties); `anthropic2026measuring`; `microsoft2025multistage` | Move user and staff evidence to A8 (capacity of the authorised person) |
| print stage | period vs allocation type | 10, 56–61, 72 | narrower | draft's own moment 3 dates (1831–2015) | Call moments 2 and 3 "the institutions of distribution and binding", or justify the label |
| scribes' correction | reader's work onto the page vs deployer's trust onto a policy engine | 149–164, 301–305 | narrower | `saenger1997space` p. 85 (second-hand); `elmergawi2026introducing` | Keep the concession; define the correction by beneficiary |
| literacy | reading and writing vs AI skilling; competence of the second party | 231–266, 425–434, 543 | narrower | `chiang2022exploring` p. 159; `smith2025microsoft`; draft 543 | Name the competence the second party needs, or drop F5 for her |
| disclosure | pre-binding reading; CoT exposure; post-failure notice | 242–250, 353–357, 411–423 | narrower | `israeli2022requerimiento` pp. 47, 62; `eu2024aiact` art. 73(1) | Pair P20 with the dropped answer and the absent court, not with "after the fact" |
| scaffold | Nadella's design metaphor vs learning-science scaffold | 425–427, 503–510, 532–533 | misused | `nadella2025looking` ¶¶4–5 | Cite the phrase as a profession about product design, not a promise of in-system support |
| D02 | structural refusal | 520–521, 535–536 | narrower | `gaston1969gaston`; ledger D02 (GDPR art. 22); O04 | Supply the precedent; meet the cost objection |
| D03 | declared envelope toward the people acted on | 521–524, 536–537 | narrower | `google2026agentic` Modes, Dispute Evidence; ledger D03 (P2B 15 days); O05 | Add the no-change-without-notice precedent; meet O05 with Lovett's resilience condition |
| D04 | counter-delegation | 524–526, 537–538 | holds | `pennsylvania1851minutes` pp. 656–657; `spain1805novisima` leyes III, V; `israeli2022requerimiento` p. 48 | None; connect it to the usability of legal remedies (§3.7) |
| D06 | check understanding and carry the risk | 527–530, 539–540 | narrower | `lely1883judicature` p. 276; `jones1899meehan` p. 1; `microsoft2022responsible` p. 8 | Cite *Jones v. Meehan* for the risk half; assign A5.4 to the developer; meet speed and scale |
| D07 | change the medium | 530–532, 541–542 | narrower | `simon2005impact` p. 32 and Where used (inspector); `calo2012against` p. 1034 | Either add the third-party grader or cite visceral notice as the operator-side precedent |
| D08 | scaffold inside the system | 532–533, 542–543 | unsupported | `chiang2022exploring` (card: fits D08); `nadella2025looking` ¶4 | Name the competence and a precedent, or state D08 as a duty toward users rather than the second party |

**Counts.** 38 rows: holds 2; narrower 25; contested 4; misused 4; wrong 2; unsupported 1.
