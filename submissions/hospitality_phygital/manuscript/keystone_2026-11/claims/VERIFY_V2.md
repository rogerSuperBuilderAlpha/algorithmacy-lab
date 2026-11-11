<!-- Independent verification of claim registers A8, A9, A10, run rr-2026-11-k, written by a Claude (Fable 5.2) subagent on 11 Nov 2026. -->

# VERIFY_V2: claim registers A8, A9 and A10

*Drafted by Claude (verifier V2). None of this is the authors' wording. I wrote this file and no other; I edited no register, card, ledger or manuscript file, and I committed nothing.*

## Before the registers

**What I did.** I read `AUDIT_BRIEF.md`, the Guards in `RUN_BRIEF_K.md`, `CLAIMS_FIXED.md` and `DRAFT_v6.md` in full, then the three registers. For each selected row I opened the source text myself, found the passage, ran the brief's tests, and only then compared my result with the auditor's row. Line numbers (l. 99 and so on) are lines of `DRAFT_v6.md`.

**Selection.** 54 rows: 19 in A8, 19 in A9, 16 in A10. A script read the register tables in file order and applied the rules.

- Rule 1: every row whose severity cell contains 'fatal'.
- Rule 2: **returned nothing.** None of the three registers has a 'check hardest' list or any note addressed to a second reader (`grep -i "check hardest\|second reader"` finds no hit in A8, A9 or A10; their closing sections are the five lists the brief asks for). I took the lead's three named disputes as the stand-in and mark those rows **D**.
- Rule 3: pool = rows whose verdict is not `supported`, not `valid`, and not a signpost or label, less the rule 1 rows; every fourth, starting with the first. I counted `supported (abstract only)` and `valid with added premise` in this pool, since neither is `supported` or `valid`.
- Rule 4: pool = rows with verdict exactly `supported` or `valid`; every sixth, starting with the first.
- One parsing note: A9's closing leads table has a line that begins `| S-241.3 |`; I dropped it from the pool. It did not change the picks.

**Verdict words.** AGREE: I reach the auditor's verdict and severity, and the action is sound. AGREE-WITH-NOTE: the fault and the severity stand, but the label, the locator, the reasoning or the action needs the note given. DISAGREE: my verdict or severity differs in a way that changes what the lead should do with the row.

**Passages.** I rejoined words split at line ends, expanded ligatures and normalised quotation marks. Every passage the auditors pasted for a selected row sits at the locator given and reads as quoted, with three exceptions recorded at S-243.1 (A9), S-259.5 and S-278.2 (A10).

**Conflicts flagged.** (1) The repo `CLAUDE.md` and the arm's `AGENTS.md` say to branch, commit and push; the task and guard 11 say not to commit. I followed the task. (2) The arm's `AGENTS.md` asks for no first person in arm documents; the global style file and the registers use 'I' for the writer's own moves. I did the same. (3) My standing instructions discourage report files; the task names this file as the deliverable, so I wrote it and nothing else.

**Sources I opened** (all under `manuscript/revision_2026-11/research/sources/`).

| Source | File | What I read |
|---|---|---|
| Bovens 2007 (version of record) | `bovens2007accountability/user_pdf/fulltext.txt` | pp. 450–455 in full; every hit for ex ante, ex post, veto, retrospective, proactive, control, clients on pp. 447–468 |
| Baum and Laux (LNCS version of record) | `baum2026constitutive/vor/chapter.txt` | pp. 115–116, 120–122, 125–126 in full; term search of the rest |
| Regulation (EU) 2016/679 | `gdpr2016art22/gdpr.txt` | arts 12 and 22 in full |
| WP251rev.01 | `wp29_2018adm/wp251.txt` | pp. 21, 22, 26, 27, 31, 32, 34 |
| 42 U.S.C. § 2000a | `usc2000a/lii.txt`, `govinfo_usc2024_sec2000a.htm` | subsections (a)–(e), both copies |
| 42 U.S.C. § 12181(7)(A) | `ada1990title3/usc42_12181_lii.txt` | the paragraph |
| Regulation (EU) 2024/1689 (OJ text) | `eu2024aiact/aiact.txt` | arts 8, 14, 16, 26, 85, 86, 113; chapter and section headings; Annex III |
| Regulation (EU) 2026/1744 (OJ text) | `eu2024aiact/reg_2026_1744_omnibus.txt` | recital 40; art. 1(39), (40); art. 4; searched for any change to art. 14 (none) |
| Kong 2026 (version of record) | `kong2026delegation/user_pdf/fulltext.txt` | pp. 3–5, 9–10, 12–13; every use of 'address' and 'addressee' |
| Cobbe et al. 2023 (version of record) | `cobbe2023understanding_vor/vor.txt` | p. 1193 |
| Woodland [2013] UKSC 66 | `woodland2013uksc/woodland.txt` | paras 5–7, 22–25 in full |
| Morgan 2015 (accepted manuscript) | `morgan2015liability/morgan.txt` | abstract; AM pp. 7–9, 12, 22 |
| Occupiers' Liability Act 1957; Hotel Proprietors Act 1956; Equality Act 2010 ss 20, 29; Payment Accounts Regulations 2015 reg. 18 | `ola1957/`, `hpa1956/`, `eqa2010s20/`, `eqa2010s29/`, `pareg2015/` | the provisions named |
| Xiang et al. 2022 | `xiang2022covid/paper.txt` | Methods; Stage II findings |
| Mosca and La Rosa 2019; Mosca 2026 | `moscalarosa2019/symphonya.txt`; `mosca2026ai/fup.txt` | term search of the whole text; pp. 82, 84, 90–92; pp. 3–6 |
| Wilson-Nash et al. 2026 | `wilsonnash2025captivity/user_pdf/fulltext.txt` | pp. 974, 976, 978, 979, 981 |
| Lind et al. 1990 | `lind1990voice/user_pdf/fulltext.txt` | pp. 954–958 |
| Pigac et al. 2026 | `pigac2026transparency/user_pdf/fulltext.txt` | pp. 284, 287, 291 |
| Martin and Waldman 2023 | `martinwaldman2022legitimate/verifier2/mw.txt` | Study Design; Results on governance |
| Chalmers and Galani 2004 (Glasgow eprint) | `chalmers2004seamful/gla_eprint.txt` | abstract; eprint p. 10 |
| Garcia et al. (CESifo WP 10849, not the *Management Science* version) | `garcia2026strategic/text.txt` | abstract; pp. 2, 48 |
| Chang et al. 2022 (accepted manuscript) | `chang2022unmanned/paged.txt` | abstract |
| Di Domenico and Lynch 2007 | `didomenico2007host/user_pdf/fulltext.txt` | p. 322 |
| Ivanov and Webster 2024 | `ivanov2024automated/openalex.json` | abstract only |

**Fetched this session, 11 Nov 2026** (saved in my scratchpad, not in `sources/`). EUR-Lex, `http://data.europa.eu/eli/reg/2026/1744/oj`, HTTP 200 with no bot check: the page carries Regulation (EU) 2026/1744 and its art. 1(40) reads as the saved copy does. Crossref, Unpaywall and OpenAlex for doi 10.1016/j.techsoc.2023.102430: *Technology in Society* 76, 102430, March 2024; the only open location is the publisher, which the auditor reports behind a bot check, so I did not press. OpenAlex for doi 10.1080/10447318.2025.2558022 (Kim et al.): abstract as the A9 auditor quotes it.

**Not done.** I checked later treatment of no case or statute. I read no full text of Ivanov and Webster (2024), Kim et al. (2025), Hirschman (1970) or Star and Ruhleder (1996). I verified the out-of-batch sentence ids S-102, S-148, S-183 and S-196 in the ledger and took the other S-ids on the auditors' word.

---

## Register A8 ('When a person must be reachable', Table 1)

### Rows taken

- Rule 1: none (the register grades no row fatal).
- Rule 2: none in the file. **D** rows: S-220.1, S-224.2 (and S-224.4, which rule 3 also picks).
- Rule 3 (14 of 55): S-205.1, S-207.2, S-209.2, T1.r1.c3, T1.r2.c3, T1.r4.c2, T1.r5.c3, T1.r6.c4, S-212.1, S-214.2, S-215.3, S-218.3, S-222.1, S-224.4.
- Rule 4 (3 of 15): S-204.1, T1.r5.c1, S-219.1.

### The two disputes, settled

**Is GDPR art. 12(3) relevant to 'The right states no timing'?** Yes. Art. 22(3) itself names no time. Art. 12(3) covers every 'request under Articles 15 to 22', so a request for human intervention must be answered 'without undue delay and in any event within one month', extendable by two months. The sentence is true of the paragraph and incomplete for the Regulation. The cap helps the draft: it shows that the law tolerates a review weeks after the decision.

**What does 42 U.S.C. § 2000a(b)(1) cover?** It defines which lodgings are 'places of public accommodation' for Title II's rule against 'discrimination or segregation on the ground of race, color, religion, or national origin' (§ 2000a(a)). It leaves out an establishment 'located within a building which contains not more than five rooms for rent or hire and which is actually occupied by the proprietor of such establishment as his residence'. The excluded establishment still lets rooms to transient guests for money. The clause exempts it from one federal anti-discrimination rule; it does not exempt it from an innkeeper's duties and it draws no line between commercial and household hosting.

### Entries

**S-205.1** · rule 3 · auditor: partial, minor
- Passage: 'HITL is constitutive (a human contribution is necessary for the decision output), while HOTL is corrective … Within HOTL, we distinguish temporal modes—synchronous, asynchronous, and anticipatory' (Baum and Laux, p. 115). 'We distinguish three temporal modes, the first two of which share a common logic, while the third is structurally different' (p. 120).
- Mine: partial (class 5: timing is a gradation inside corrective oversight; class 2: AI systems), minor.
- **AGREE.** The authors' first division is causal. Their examples are a vehicle, surgery, an ICU, a warehouse, parole and hiring, as the auditor says; the chapter never mentions a person affected by the output.

**S-207.2** · rule 3 · auditor: valid with added premise, material
- Passage: none in a source. Draft l. 60: 'If the duty stays with the holder, the holder is the party the guest must be able to reach.' K7's P3 is in `CLAIMS_FIXED.md` and nowhere in v6 (the draft's only 'learn' is at l. 66, on competence).
- Tests. Premises: the duties run through the stay; they stay with the holder. Counter-model: a host that lets every failure happen and compensates afterwards has kept the duty and the guest's claim, and no one was reachable. Terms hold. The boundary follows only with P3.
- Mine: valid with added premise (K7 P3), material.
- **AGREE.**

**S-209.2** · rule 3 · auditor: valid with added premise, minor
- Passage: 'the human is not meaningfully a synchronous HOTL: the intervention happens too fast for real-time correction. However, if a human can adjust parameters governing emergency braking behavior … this constitutes anticipatory HOTL' (p. 122). 'A choice that is not revisitable within the system's life-cycle is design, not corrective involvement' (p. 120 n. 5).
- Tests. Counter-model: the vendor's default configuration; 'the rule it set' then has no referent, though K8 would still make the host answer. The premise 'the host set the rule' is missing, and l. 82 says the rule is 'often' the vendor's.
- Mine: valid with added premise, minor.
- **AGREE.** The sentence also drops 'kept open to revision', which the source makes the mark of this mode.

**T1.r1.c3** · rule 3 · auditor: partial, material
- Passage: 'after checking with hotel management, the hotel was willing to cover the cost of the nucleic acid test' and 'Upon arrival, the staff couldn't let the guest check-in, and helped him to book another hotel in another district' (Xiang et al. 2022, 'Performance pathways: managing ritual violations'). Draft l. 121: 'some of these decisions cannot be undone in time'.
- Mine: partial (class 3), material.
- **AGREE-WITH-NOTE.** The flat 'No' contradicts l. 121 and the paper's own source. The auditor leans on the rebooked guest; the first incident is the stronger counter-instance, because there a refusal at the desk was averted within the evening by someone with authority, and the draft itself reports it at l. 68.

**T1.r2.c3** · rule 3 · auditor: unverifiable, minor
- Passage: 'the intervention happens too fast for real-time correction' (Baum and Laux, p. 122, of a vehicle's brakes). 'Only when guests do not abide by the ritual after repeated communications will they be asked to leave the hotel' (Xiang et al. 2022).
- Mine: unverifiable, minor. No saved source speaks to lock-outs or alarms in hotels, and the paper names no hospitality decision that is too fast for a person.
- **AGREE.**

**T1.r4.c2** · rule 3 · auditor: valid with added premise, minor
- Passage: none for the grading. For the lead the auditor offers: 'to take such steps as it is reasonable to have to take to avoid the disadvantage' (Equality Act 2010, s. 20(3)); 'A duty to make reasonable adjustments applies to— (a) a service-provider' (s. 29(7)(a)). Both read as quoted.
- Mine: valid with added premise (apart from usability a room is a matter of preference), minor.
- **AGREE.**

**T1.r5.c3** · rule 3 · auditor: partial, minor
- Passage: none; the cell cites nothing. Its neighbour rests on 'prohibitively high prices effectively bar someone from certain goods or services' (WP251rev.01, p. 22).
- Mine: the flat 'Yes' is unsourced and conflicts with the neighbouring cell: a price that bars access to a night's room cannot be undone once the night has passed. Minor.
- **AGREE-WITH-NOTE.** The fault is real. The label departs from the register's own convention, under which an unsourced statement of how hotels operate is `unverifiable`; what the auditor found is an inconsistency between two cells, and the row should say so.

**T1.r6.c4** · rule 3 · auditor: valid with added premise, minor
- Passage: draft l. 68: 'What a guest can expect from the host's obligation is therefore a hearing by someone with authority, not the exception itself'.
- Tests. The hearing follows from l. 68. 'At a time that suits the guest' follows from nothing, and l. 105 gives reversible decisions only 'a reachable appeal'.
- Mine: valid with added premise, minor.
- **AGREE.**

**S-212.1** · rule 3 · auditor: valid with added premise, minor
- Passage: Table 1 grades row 1 'High' and row 2 'Highest', and row 1 stands first.
- Tests. The reason given, shelter, fits admission, lock-out and removal, and does not fit an alarm. The order needs the premise that stakes and irreversibility together rank the rows.
- Mine: valid with added premise, minor.
- **AGREE.**

**S-214.2** · rule 3 · auditor: equivocal, minor
- Passage: draft l. 105: 'Where a decision can be deferred or undone, a reachable appeal is enough'; Table 1, room row: 'Mostly' reversible in time, 'A later appeal by default'.
- Tests. Counter-model: a one-night guest in an unusable room while other rooms stand free; the decision is reversible in time and a later appeal can only compensate. 'Reachable' in l. 105 becomes 'later' here.
- Mine: equivocal, minor.
- **AGREE.**

**S-215.3** · rule 3 · auditor: supported (abstract only), minor
- Passage: 'It evaluates the preferences towards four decision-making approaches ("human only", "human-in-the-loop", "human-on-the-loop" and "human-out-of-the-loop") applied to 23 decisions in 8 hotel departments. The sample includes 130 respondents from the Bulgarian hotel industry' (abstract, OpenAlex record).
- Mine: supported (abstract only), minor.
- **AGREE.** I found no open copy either: Unpaywall and OpenAlex list the publisher alone.

**S-218.3** · rule 3 · auditor: partial, minor
- Passage: 'In the cases referred to in points (a) and (c) of paragraph 2, the data controller shall implement suitable measures …' (art. 22(3)); point (b) is a law 'which also lays down suitable measures' (art. 22(2)(b)).
- Mine: partial (class 5), minor. 'Among other grounds' covers one other ground, explicit consent.
- **AGREE.**

**S-222.1** · rule 3 · auditor: equivocal, minor
- Passage: draft l. 86: 'it measures neither satisfaction nor harm'; l. 72: 'cases that illustrate the distinctions rather than test them'.
- Tests. 'Explains' has no outcome to explain; read as 'asks most', the sentence repeats l. 105. The auditor's counter-model holds: at the extreme of speed the framework stops asking for a person.
- Mine: equivocal, minor.
- **AGREE.**

**S-224.4** · rule 3, **D** · auditor: not in source, material
- Passage: § 2000a(b)(1), quoted above; 'a diverse range of owner-occupied small businesses providing accommodation where the private home dimension is significant' (Di Domenico and Lynch 2007: 322).
- Mine: not in source, material. The statute never speaks of households, and the establishment it leaves out is a business.
- **AGREE.**

**S-204.1** · rule 4 · auditor: valid
- Passage: draft l. 99: 'the projection decides nothing about the guest, and the touchpoint passes'; l. 54 for the stipulated sense of authority.
- Tests. 'Not every' needs one instance and l. 99 gives it. I found no counter-model: l. 86 requires that some party be obliged to answer and does not require that a person stand by. Terms hold. Classes 1–9 do not bite on an unsourced inference of this form.
- Mine: valid.
- **AGREE.**

**T1.r5.c1** · rule 4 · auditor: valid
- Passage: draft l. 18: 'We call software that takes or shapes a decision about a guest an algorithmic system'. 'the price for the room type r in hotel h is being changed for arrival date a in month m' (Garcia et al., CESifo WP 10849, p. 48). 'differential pricing based on personal data or personal characteristics' (WP251rev.01, p. 22).
- Tests. The label carries two senses. In the paper's own case a price belongs to a room and a date and is quoted to whoever books. In the cell beside it the price is set on a person. The price is also settled before the stay, where l. 123 says the framework 'explains less'.
- Mine: equivocal, minor.
- **DISAGREE.** The auditor graded T1.r1.c1 equivocal because a booking fails before the stay and T1.r2.c1 equivocal because an alarm decides nothing about a particular guest. Both grounds apply here. The auditor wrote the first as a caution in the action cell and the second at T1.r5.c2, and then passed the row; the brief says a caution is not a pass.

**S-219.1** · rule 4 · auditor: supported
- Passage: 'Human intervention is a key element. Any review must be carried out by someone who has the appropriate authority and capability to change the decision' (WP251rev.01, p. 27, under 'Establishing appropriate safeguards').
- Nine classes. 1 and 2: the reviewer is the controller's, in EU guidance, and the sentence says 'guidance'. 3: 'must' becomes 'requires'. 4: the Working Party speaks. 5: the passage concerns review under art. 22(3), which is the sentence's subject. 6, 7: clean. 8: printed p. 27 of the version in the reference list. 9: joined to art. 22(3), and the roles line up.
- Mine: supported.
- **AGREE.**

**S-220.1** · **D** · auditor: partial, minor
- Passage: 'The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request. That period may be extended by two further months where necessary' (art. 12(3)). 'obligations under Articles 15 – 22 in the timescales provided for by the GDPR' (WP251rev.01, p. 31 n. 52).
- Mine: partial (class 5), minor.
- **AGREE.** Strictly, art. 12(3) times the controller's report of the action taken, not the intervention; the auditor's phrase 'an outer limit for the controller's answer' is exact.

**S-224.2** · **D** · auditor: partial, minor
- Passage: § 2000a(a) and (b)(1), quoted above, identical in the LII and govinfo copies. The ADA repeats the carve-out: 'except for an establishment located within a building that contains not more than five rooms for rent or hire and that is actually occupied by the proprietor' (42 U.S.C. § 12181(7)(A)).
- Mine: partial (classes 5, 3), minor. The rooms and the residence belong to the building; the clause is a definition inside one statute; 'United States public accommodation law' is wider than Title II.
- **AGREE.** The material fault sits in S-224.4.

### Summary, A8

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 (fatal) | 0 | – | – | – |
| 2 (named in the file) | 0 | – | – | – |
| 3 (every fourth, not passed) | 14 | 12 | 2 | 0 |
| 4 (every sixth, passed) | 3 | 2 | 0 | 1 |
| D (disputes, outside the rules) | 2 | 2 | 0 | 0 |

| Row | Auditor | Mine | Why |
|---|---|---|---|
| T1.r5.c1 | valid | equivocal, minor | 'Pricing' is a rule for a room and a date in the paper's case and a decision about a person in the next cell, and it is settled before the stay; the auditor faulted two other labels on the same grounds |

Faults I found that the auditor missed:

1. T1.r5.c1, as above.
2. T1.r1.c3: the better evidence against the flat 'No' is the guest for whom management paid for the test (Xiang et al.; draft l. 68), not the rebooked guest.
3. T1.r5.c3: the verdict label breaks the register's own convention for unsourced cells.

---

## Register A9 ('Designing for interruptible hospitality', Table 2)

### Rows taken

- Rule 1 (2): S-250.3, T2.r4.c2. Both are also the **D** rows.
- Rule 2: none in the file.
- Rule 3 (14 of 53): S-227.1, S-230.1, S-231.5, S-233.2, S-236.1, S-238.1, S-241.1, S-243.1, S-245.2, S-248.1, T2.title.1, T2.r2.c3, T2.r3.c4, T2.r5.c4.
- Rule 4 (3 of 17): S-228.2, S-234.2, S-250.2.

### The dispute, settled

**Is accountability in Bovens' account only retrospective, and does 'fatal' stand?** No to both. Bovens writes that 'accountability, as defined here, is in nature retrospective. Actors are to account to a forum after the fact' (p. 453). The auditor quotes that sentence correctly. Three passages qualify it, and the register weighs only two of them and calls them narrow.

- 'The consequences can also consist of the use of veto powers by the forum. It can block or amend decisions made by the actor' (p. 452).
- 'Moreover, accountability is not only about ex post scrutiny, it is also about prevention and anticipation' (p. 453). The register does not quote this sentence.
- 'actors, such as ministers on the eve of council meetings, may be obliged … to explain and justify their stances before going to Brussels and may be forced to adjust them if their account is not convincing. However, for analytical purposes, policy making and accountability should be treated as distinctive concepts' (p. 453).

Bovens excludes two things. The first is consultation and participation, which 'lack the element of justification, judgement and consequences' (p. 453). The second is control that does not work through account-giving: such mechanisms 'do not in themselves operate through procedures in which actors are to explain and justify their conduct to forums. Accountability is a form of control, but not all forms of control are accountability mechanisms' (p. 454). Neither exclusion reaches stage 4 as the draft describes it, where an actor must explain and justify a decision the system has already taken, to a guest who has asked, before the refusal lands. That account comes after the conduct it answers for. It is fast, and Bovens sets no speed.

The auditor also maps the draft onto Bovens' 'control' the wrong way round. Bovens' control is a principal's or forum's power over the actor (p. 454). The power the draft needs sits with the actor: the manager who can change the hotel's own decision.

What does fail is the label, and the A9 auditor found that fault already at S-233.2. By l. 105 the thing that must be in place before a decision takes effect is authority to change it. Stage 4 calls that 'accountability'. The term has moved from account-giving to reachable authority. The correction is to say that the account must be prompt and that the power to reverse is the paper's addition; the auditor's own action says 'the demand survives; its label does not'. A row whose demand survives is not fatal under the brief's definition.

### Entries

**S-250.3** · rule 1, **D** · auditor: contradicted, fatal
- Passage: the five Bovens passages above (pp. 452–454), and 'the focus is more on ex post facto processes in governance than on ex ante inputs' (p. 467).
- Tests. Premises: Bovens' definition (p. 450); the paper's boundary (l. 105). Counter-model in both directions: a manager who must explain within minutes and cannot change the outcome gives Bovens' account in real time and fails l. 105; a night manager who silently reverses a lock-out meets l. 105 and gives no account. What must work in real time is authority.
- Mine: equivocal ('accountability': account-giving in the premise, reachable authority in the conclusion), material.
- **DISAGREE** on verdict and severity. Bovens does not deny that an account can be demanded before a decision takes effect; he gives a case of it and lists a veto among a forum's consequences. I agree with the action in part: keep Bovens for the account, with all seven elements, and name the power to reverse as the paper's own.

**T2.r4.c2** · rule 1, **D** · auditor: contradicted, fatal
- Passage: as S-250.3. Cell: 'Establishes a forum before which an accountable actor with authority to change outcomes must answer, in real time where Table 1 requires it'.
- Mine: equivocal, material. The cell carries the faults of S-248.1 (consequences dropped, authority added) and S-249.1 (forum as a place), and it defines accountability by an 'accountable actor', as the auditor notes.
- **DISAGREE** on verdict and severity, for the reasons at S-250.3.

**S-227.1** · rule 3 · auditor: not in source, material
- Passage: 'This paper investigates the implementation of Industry 4.0 systems within the production of fashion luxury goods' (Mosca and La Rosa 2019: 82). 'Such frameworks are imposing tough new obligations: transparency, accountability, and stringent human oversight, especially for high-risk systems' (Mosca 2026: 6). Neither text contains 'guest', 'hotel' or 'hospitality'.
- Mine: not in source (classes 1, 2, 5), material. Two works with one first author do not show researchers disagreeing, and neither concerns guests.
- **AGREE.** The lead the auditor offers is where it says: 'Some studies suggest that over-disclosure may trigger guest discomfort or distrust' (Pigac et al. 2026: 284).

**S-230.1** · rule 3 · auditor: equivocal, minor
- Passage: draft l. 86: 'predictability from terms held steady enough to be negotiated'; l. 99: 'neither a guest nor the staff at the desk could anticipate the operative rule … so the touchpoint fails on predictability'.
- Tests. Counter-model: the paper's own pricing case, where no display at the desk makes the rule predictable. Predictability is a property of terms at l. 86 and a notice of change here.
- Mine: equivocal, minor.
- **AGREE.**

**S-231.5** · rule 3 · auditor: invalid, minor
- Passage: the six questions (ll. 90–95) and the three conditions (l. 86). None asks whether the guest can adjust anything.
- Tests. The sentence gives its own premise: 'a path the system alone has chosen is not the guest's choice'. With the further premise that the guest's choice is something the arrangement must protect, the principle follows. That premise appears only in the Conclusion, as 'guest agency' (l. 149).
- Mine: valid with added premise, minor.
- **AGREE-WITH-NOTE.** The gap is as the auditor says, and so is the action. The label should match the one the auditor gave principles 1 and 4, which also need a premise the test does not supply.

**S-233.2** · rule 3 · auditor: equivocal, material
- Passage: Bovens, p. 450, the definition. Draft l. 97: 'The fourth and fifth separate the power over the single case from the duty to answer for the rule'.
- Tests. Counter-models hold: a clerk who overrides and explains nothing; an unstaffed second route. The paper's own questions keep override and answering apart.
- Mine: equivocal, material.
- **AGREE.**

**S-236.1** · rule 3 · auditor: invalid, material
- Passage: 'by having human front-line employees on hand to provide support, guidance, or reassurance … struggling consumers find the experience more manageable' (Wilson-Nash et al. 2026: 981). 'the symbolic voice effect is at least as strong as the instrumental voice effect' (Lind et al. 1990: 957). 'Digital Skeptics | Minimal | Human-mediated check-in' (Pigac et al. 2026: 291, Table 4). Kim et al., abstract: stress rises with job demand and forced use, 'with the negative impact of employee's support'.
- Tests. 'Not a human presence as such' reads two ways. As insufficiency (a person without power does not meet the need) it follows from the paper's own argument. As non-necessity it does not follow, the four passages speak against it, and the Conclusion takes it that way ('neither necessary nor sufficient', l. 149). 'Need' also moves from perceived legitimacy among online raters to what guests require.
- Mine: equivocal, material.
- **AGREE-WITH-NOTE.** The fault and the fix ('not only a human presence') stand. 'Invalid' is too strong for a sentence that is sound on one of its two readings.

**S-238.1** · rule 3 · auditor: partial, minor
- Passage: 'This may include neglecting, abandoning, and distancing oneself from the service category altogether (Keeling et al. 2019), which may carry a personal cost and loss (e.g., avoiding GP surgery because bookings are mandated to be online)' (p. 979).
- Mine: partial (classes 3, 5, 7), minor. 'Pays' is categorical; the source speaks of people who give up a whole kind of service, and a guest has not.
- **AGREE.** Class 6 applies as well: the paper is conceptual and 'has yet to be empirically tested' (p. 981). The auditor lists that class at S-237.3 and S-237.4 and not here.

**S-241.1** · rule 3 · auditor: valid with added premise, minor
- Passage: none; the premise rests on Star and Ruhleder, which no one in the run has read.
- Tests. With 'can', one coherent scenario suffices. The added premise is that what a guest cannot see offers no point at which to stop it. The auditor's counter-model (a help button on every screen) shows that the premise is needed.
- Mine: valid with added premise, minor.
- **AGREE.**

**S-243.1** · rule 3 · auditor: partial, minor
- Passage: 'Lastly, we suggest that designers may consider selectively and carefully revealing differences and limitations of systems, in ways that support social interaction i.e. seamful design' (Chalmers and Galani 2004, Glasgow eprint, p. 10).
- Mine: partial (classes 3, 5), minor.
- **AGREE-WITH-NOTE.** The words are exact. The auditor places them in the Conclusion; in the eprint they close the design section, and the heading 'Conclusion' follows them on the same page.

**S-245.2** · rule 3 · auditor: partial, minor
- Passage: 'One hundred eighty male undergraduate students participated' (p. 954); the goal 'would not be changed regardless of what the subject said' (p. 954); 'The voice conditions produced higher ratings of procedural and outcome fairness than did the no-voice condition' (p. 955); 'all pairwise comparisons among the voice conditions were significant' (p. 955 n. 3); procedural fairness means 2.43, 3.15, 3.70 (Table 1, p. 956).
- Mine: partial (classes 1, 6), minor. The result is in the results section and is reported accurately; the sentence names neither the design nor the subjects.
- **AGREE.**

**S-248.1** · rule 3 · auditor: partial, material
- Passage: the definition (p. 450); 'the possibility of sanctions of some kind is a constitutive element of narrow accountability and … should be included in the definition' (p. 451); Box 1, item 7 (p. 452); 'organisations or officials, exercising public authority' (p. 448).
- Mine: partial (classes 3, 5, 7), material. The paraphrase drops the element Bovens calls constitutive and adds 'authority to change outcomes'.
- **AGREE.**

**T2.title.1** · rule 3 · auditor: equivocal, minor
- Passage: Table 2, rows 1–3: an audit, a specification, a design stage.
- Mine: equivocal, minor.
- **AGREE-WITH-NOTE.** The title also says 'answerability' where the column says 'Accountability'; the brief lists both among the terms to track.

**T2.r2.c3** · rule 3 · auditor: equivocal, material
- Passage: draft l. 86: the test 'tells whether the conditions under which a guest can exercise standing survive'; l. 133: 'then specify what guests and employees can understand, adjust and challenge'.
- Tests. A specification gives the guest nothing yet; 'secures' holds only of the organization's plan. 'Challenge' belongs to stage 4 and 'adjust' to no condition.
- Mine: equivocal, material.
- **AGREE.**

**T2.r3.c4** · rule 3 · auditor: valid with added premise, minor
- Passage: none; the cell names a kind of cost.
- Mine: valid with added premise (the capabilities include staff skills, hence 'training'), minor.
- **AGREE-WITH-NOTE.** The brief asks that an added premise be stated. The auditor writes 'A label; unsourced' and states none, here and at T2.r2.c4 and T2.r5.c4.

**T2.r5.c4** · rule 3 · auditor: valid with added premise, minor
- Passage: digital-only access is 'often positioned as a route to greater efficiency, economic productivity, and connectivity, while simultaneously reducing labor costs' (Wilson-Nash et al. 2026: 974).
- Mine: valid with added premise (a second route needs staff for as long as it runs), minor.
- **AGREE-WITH-NOTE.** As T2.r3.c4. The passage is where the auditor says and ranks nothing against stage 4.

**S-228.2** · rule 4 · auditor: supported
- Passage: 'We came to the conclusion that it would be best to avoid disclosing the use of such technologies to customers, who may perceive the product as having an inferior quality because technology was used in its creation' (p. 91; the abstract, p. 82, says the same).
- Nine classes. 1, 2, 5, 6: the 'customers' are 200 questionnaire respondents and the technology is manufacturing plant; the auditor carries those faults at S-228.1 and S-227.1, where they belong. 3: 'it would be best' becomes 'advised'. 4: the authors conclude it. 7: clean. 8: no page is cited; the article's own citation line reads '2, 82-94', against the reference list's 103–116. 9: carried at S-228.4.
- Mine: supported.
- **AGREE.** The remark on p. 90 ('a prejudice that could be easily countered by explaining, if necessary') does not change what the study advised.

**S-234.2** · rule 4 · auditor: supported
- Passage: 'A human who must click "approve" for every decision (HITL) but rubber-stamps without genuine judgment does not thereby become an overseer' (p. 126).
- Nine classes. 1–4: the authors speak, of a deployer's own staff. 5, 7: the use of the words as a reason for reachability is a separate row (S-234.3), rightly. 6: a conceptual chapter; the sentence claims no finding. 8: p. 126 of the chapter in the reference list; the chapter prints 2027. 9: n/a.
- Mine: supported.
- **AGREE.**

**S-250.2** · rule 4 · auditor: valid
- Passage: Table 1, 'Recourse it needs': 'A reachable person with authority before refusal takes effect'; 'A later appeal by default'; 'limits set in advance by the host'; 'A staffed fallback'; 'at a time that suits the guest'; 'Automation, under rules set in advance'.
- Tests. The table does say where a person must be reachable in time and where a later appeal will do, so the cross-reference holds. It also holds three other answers that the sentence leaves out. The sentence does not say 'the rest', which is the word the auditor faulted at S-244.2.
- Mine: valid.
- **AGREE-WITH-NOTE.** A borderline pass: a reader of l. 133 takes Table 1 for a two-way sorter, and it is not one.

### Summary, A9

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 (fatal), also D | 2 | 0 | 0 | 2 |
| 2 (named in the file) | 0 | – | – | – |
| 3 (every fourth, not passed) | 14 | 8 | 6 | 0 |
| 4 (every sixth, passed) | 3 | 2 | 1 | 0 |

| Row | Auditor | Mine | Why |
|---|---|---|---|
| S-250.3 | contradicted, fatal | equivocal, material | Bovens allows a forum's veto (p. 452), says accountability 'is not only about ex post scrutiny' and describes an account given before the act (p. 453); the fault is that 'accountability' has come to mean reachable authority |
| T2.r4.c2 | contradicted, fatal | equivocal, material | the same proposition in the table |

Faults I found that the auditor missed:

1. The register does not quote 'Moreover, accountability is not only about ex post scrutiny, it is also about prevention and anticipation' (p. 453) or 'Accountability is a form of control' (p. 454). Both bear against 'contradicted'.
2. The register says a person who can stop a decision 'is, in Bovens' terms, control'. Bovens' control is power over the actor; the draft's power belongs to the actor.
3. S-243.1: the locator. The passage precedes the Conclusion.
4. T2.r2.c4, T2.r3.c4, T2.r5.c4: 'valid with added premise' with no premise stated.
5. T2.title.1: 'answerability' in the title against 'Accountability' in the column.
6. S-238.1: class 6 omitted.

No selected row that the auditor passed should have failed.

---

## Register A10 (the Conclusion)

### Rows taken

- Rule 1 (1): S-257.1.
- Rule 2: none in the file. **D** rows: S-261.2 (and S-261.3 and S-278.2, which rule 3 also picks).
- Rule 3 (11 of 42): S-253.1, S-255.1, S-257.3, S-258.2, S-259.5, S-261.3, S-263.3, S-268.1, S-272.2, S-275.1, S-278.2.
- Rule 4 (3 of 17): S-256.1, S-265.1, S-268.2.

### The disputes, settled

**To whom are the art. 14 duties owed?** To no named person. Art. 14 states requirements of the system: 'High-risk AI systems shall be designed and developed in such a way … that they can be effectively overseen by natural persons' (14(1)), and the system 'shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate' (14(4)). The provider must 'ensure that their high-risk AI systems are compliant with the requirements set out in Section 2' (16(a)). The deployer 'shall assign human oversight to natural persons who have the necessary competence, training and authority' (26(2)). The overseer is the person the article equips. Its aim is 'to prevent or minimise the risks to health, safety or fundamental rights' (14(2)), which protects people exposed to the system without naming them as holders of anything. Affected persons get a complaint to a market surveillance authority (art. 85) and an explanation (art. 86(1)); neither lets them stop a system. 'Owed to overseers' is not in the text. 'Not guests' is right in effect.

**From what date?** From 2 December 2027 for systems that are high-risk under art. 6(2) and Annex III, and from 2 August 2028 for those under art. 6(1) and Annex I. Art. 14 sits in Chapter III, Section 2. The 2024 text applied the Regulation 'from 2 August 2026' (art. 113). Regulation (EU) 2026/1744 (OJ L, 24.7.2026), art. 1(40)(b), replaced point (c) of art. 113: 'Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I'. It entered into force on the third day after publication (art. 4) and does not amend art. 14. I confirmed the wording on EUR-Lex today.

**What page of Kong (2026) uses 'address'?** Pages 3 (twice), 4 and 10. Page 3: 'the apt address for a demand for justification' and 'the correct address for the question "why did this happen, and what have you to say for it?"'. Page 4: 'being the apt address for a certain demand'. Page 10: 'It is a smaller quantity with an address.' 'Addressee' is on pp. 10 and 13. The draft's p. 3 is a correct page for the word; the phrase nearest 'has an address' is on p. 10.

### Entries

**S-257.1** · rule 1 · auditor: overgenerates, fatal as worded
- Passage: 'The work required to perform such a duty may well be delegable, and usually is. But the duty itself remains the defendant's' (Woodland, para 7). 'Non-delegable duties of care are inconsistent with the fault-based principles on which the law of negligence is based, and are therefore exceptional' (para 22). 'No duty of care can be delegated, but its performance may well be' (Morgan 2015, accepted manuscript, p. 7). 'Delegating performance to an apparently competent, carefully selected contractor ordinarily discharges a duty of care by performing it' (Morgan, AM p. 22).
- Tests. Read with Morgan, 'its duty cannot [be delegated]' is true of every duty of care and proves little, since careful delegation discharges an ordinary one. Read as Woodland's category, it gives the paper what it needs, that the holder answers for the delegate, and holds only for an exceptional class, for contract, for goods and for employees. The sentence trades on both readings. The auditor's counter-model holds on the second reading: s. 2(4)(b) of the 1957 Act reads as quoted.
- Mine: equivocal ('duty … cannot': Morgan's truism against Woodland's category), fatal as worded.
- **AGREE-WITH-NOTE.** The grade stands: the thesis sentence is unsupported in the sense the argument uses, and the same Conclusion calls the question open (l. 151). Three notes. (a) The better label is 'equivocal'; the brief keeps 'overgenerates' for an argument that proves the same of a bank or an airline. (b) The auditor did not open Morgan, which the reference list holds and which gives both the truism and its limit; Morgan's abstract adds that A 'will normally be able to recover' in contract 'But not in tort', and criticises Woodland's analogy between the two. (c) Section 2(4)(b) covers 'work of construction, maintenance or repair'; the step to 'a system vendor … of the same kind' is the auditor's analogy, and Woodland para 5 carries it better.

**S-253.1** · rule 3 · auditor: valid with added premise, minor
- Passage: draft l. 22: 'keep hospitality studies' account of what a host owes'; l. 34: 'An account built on motive cannot follow the obligation under delegation'; l. 52: 'Hospitality scholars have been right about what a host owes'.
- Tests. 'Account' names the content of the duty (kept) and its source in motive (rejected). The sentence is valid if it means the first.
- Mine: valid with added premise, minor.
- **AGREE.**

**S-255.1** · rule 3 · auditor: valid with added premise, minor
- Passage: draft l. 56: 'the party which holds itself out as host answers to the guest, alongside the party that controls the operation'.
- Tests. Counter-model: the division of the work dissolves the obligation, so no one holds it; the two sentences before are true and this one false. 'Therefore' needs K8. 'Its holder' is singular and l. 56 names two.
- Mine: valid with added premise, minor.
- **AGREE.**

**S-257.3** · rule 3 · auditor: partial, material
- Passage: draft l. 80: 'the path from the guest to graded authority, which an algorithmic system can lengthen, obscure or remove'; l. 82: 'Three things that need not travel together come apart along it'; l. 99: 'if a code failed at night no one with authority might be reachable'.
- Mine: partial (class 3), material. The body supports 'can' and shows no case in which a system removed a guest's path.
- **AGREE-WITH-NOTE.** The auditor counts knowledge, discretion and the occasion for a claim as further things mediation takes. At l. 82 knowledge and discretion come apart 'along' the chain; they are how the path breaks, and the guest does not lose them separately. The exclusivity fails for two other reasons: the system that decides admission (the auditor's own S-257.2) and the loss of an alternative route (l. 129).

**S-258.2** · rule 3 · auditor: not in source, material
- Passage: the sentence: 'The argument catches an arrangement that works exactly as designed and harms no one, yet leaves the guest with no one to address.' Draft l. 99: 'On our reading, neither a guest nor the staff at the desk could anticipate the operative rule or reach the managers who held it, so the touchpoint fails on predictability and on accountability.'
- Mine: the sentence states what the argument reaches. It does not say that such an arrangement is among the paper's cases, so there is no proposition here to mark 'not in source'. The body does offer one instance on its own reading, the pricing case, where the system works as built, no harm is shown and the touchpoint fails. What remains is a note for S-258.1: the claim has thin illustration. Minor.
- **DISAGREE** on verdict and severity. The brief splits a sentence into the things it asserts; this row audits a thing it does not assert. The auditor's side note is sound and worth keeping: Kong writes 'The pricing agent worked exactly as designed' (p. 12) of a case in which harm occurred.

**S-259.5** · rule 3 · auditor: partial (class 9), material
- Passage: 'the agent's answerability for the foreseeable types of outcome within that domain is neither divided nor diminished by the autonomy of the process' (Kong, p. 5). 'The conservation principle distributes answerability to each party for the foreseeable risks of its own contribution: the model developer for the foreseeable dispositions of the base model, the deployer for the foreseeable risks of the objective and domain into which it is released' (Kong, p. 9). 'Neither will actors who are in some way responsible be equally responsible … Nor will they be responsible for the whole supply chain' (Cobbe et al., p. 1193).
- Tests for class 9. The row shortens Kong's p. 5 to 'neither divided nor diminished' and reads it as 'undivided' among parties. Kong's sentence says the machine's autonomy takes no share. Among human parties he distributes answerability on p. 9, and the auditor says as much at S-259.3. Kong and Cobbe et al. differ in term (answerability; responsibility) and in emphasis, and the draft keeps the two terms in separate clauses. Read together, each still says what it says alone.
- Mine: partial (class 9: two concepts under one 'finding'), minor.
- **DISAGREE** on severity and action. 'Set the two against each other' would misstate Kong. The material fault in the sentence is the one at S-259.3: a single conceptual argument reported as a field's finding.

**S-261.3** · rule 3, **D** · auditor: partial, material
- Passage: arts 14(1), 14(2), 14(4), 16(a) and 26(2), quoted above; 'Any affected person … shall have the right to obtain from the deployer clear and meaningful explanations' (art. 86(1)).
- Mine: partial (class 5), material. The text names no party to whom the requirement is owed, and 'owed to' is the paper's own word for a directed duty.
- **AGREE.** The auditor's rewording is accurate: the requirement equips the deployer's overseers and gives the person affected no means to stop the system.

**S-263.3** · rule 3 · auditor: invalid as stated for 'any of the three', material
- Passage: draft l. 105: 'Not every touchpoint needs a person with authority standing by.' 'Guest agency', 'relational judgement' and 'human-centricity' occur at l. 149 and nowhere else in the draft.
- Tests. The body argues non-necessity for the guest alone. For employee discretion and relational judgement it offers no premise.
- Mine: invalid as stated; valid with added premise for the guest's arm; material.
- **AGREE.**

**S-268.1** · rule 3 · auditor: contradicted (by the body), material
- Passage: draft l. 99: 'one that weighed the guest's history to decide how they would be received, a case we construct'.
- Mine: contradicted by the body, material.
- **AGREE.**

**S-272.2** · rule 3 · auditor: partial, material
- Passage: 'The purpose of this research was to determine if unmanned smart hotels create more positive outcomes such as enhanced experiential satisfaction and loyalty … An online survey was conducted with 364 guests' (Chang et al. 2022, accepted manuscript, abstract). The search note the sentence rests on: 'All of them measure acceptance, satisfaction or forgiveness' (`WS_H3_multi_actor.md`, l. 57).
- Mine: partial (classes 3, 6), material. The sentence cites no study, drops 'forgiveness' and 'loyalty', and rests on abstracts for all but one.
- **AGREE.**

**S-275.1** · rule 3 · auditor: valid with added premise, minor
- Passage: none in a source. Draft l. 105: 'Where a decision can be deferred or undone, a reachable appeal is enough'.
- Tests. Counter-model: a later appeal, a chargeback or a consumer authority answers the claim, and the cost is not borne alone. The added premise is that no other channel answers.
- Mine: valid with added premise, minor.
- **AGREE.**

**S-278.2** · rule 3, **D** · auditor: partial, minor
- Passage: the four uses of 'address' and two of 'addressee' listed above (Kong, pp. 3, 4, 10, 13).
- Mine: partial (classes 5, 7), minor. Kong's address belongs to a demand for an account of an outcome; the draft gives an address to an obligation.
- **AGREE-WITH-NOTE.** The register lists one use on p. 3 and the uses on pp. 10 and 13. It omits the second use on p. 3 and the use on p. 4. Its three quotations are exact.

**S-256.1** · rule 4 · auditor: valid
- Passage: draft l. 34: 'We argue instead that the commercial host's obligation is a role obligation'.
- Tests. The row claims only that the article argued this, and it did.
- Mine: valid.
- **AGREE.**

**S-265.1** · rule 4 · auditor: supported
- Passage: 'This Act shall not extend to Northern Ireland' (Hotel Proprietors Act 1956, s. 3(3)). I checked every entry under Cases and Legislation (ll. 325–349): Calye, Lane v. Cotton and Woodland are English; Crinkley, the Civil Rights Act and EMTALA are United States; the 1956 Act and the Equality Act are Great Britain; the two Regulations are European Union law.
- Nine classes. 5: the Payment Accounts Regulations protect 'consumers legally resident in the United Kingdom' (reg. 18(1)), so 'British' has to be read loosely. The other classes are clean for a description of the paper's own sources.
- Mine: supported.
- **AGREE.**

**S-268.2** · rule 4 · auditor: valid
- Passage: none needed. 'Them' refers to the published studies and judgments.
- Tests. No study or judgment in the reference list was gathered for the paper's question. The constructed case (l. 99) bears on S-268.1, not on this clause: it was invented, not gathered.
- Mine: valid.
- **AGREE.**

**S-261.2** · **D** · auditor: partial, material
- Passage: art. 14(4), chapeau and point (e): 'to intervene in the operation of the high-risk AI system or interrupt the system through a "stop" button or a similar procedure that allows the system to come to a halt in a safe state'. Regulation (EU) 2026/1744, art. 1(40)(b), quoted above.
- Mine: partial (class 3: 'as appropriate and proportionate' and 'or a similar procedure' dropped; class 8: the reference list holds the 2024 text alone), material.
- **AGREE-WITH-NOTE.** The auditor gives one date. The amended art. 113 gives two; 2 August 2028 governs systems that are high-risk under art. 6(1) and Annex I.

### Summary, A10

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 (fatal) | 1 | 0 | 1 | 0 |
| 2 (named in the file) | 0 | – | – | – |
| 3 (every fourth, not passed) | 11 | 7 | 2 | 2 |
| 4 (every sixth, passed) | 3 | 3 | 0 | 0 |
| D (dispute, outside the rules) | 1 | 0 | 1 | 0 |

| Row | Auditor | Mine | Why |
|---|---|---|---|
| S-258.2 | not in source, material | no such proposition in the sentence; a note on S-258.1; minor | the sentence says what the argument reaches, not that the paper holds such a case; the pricing case at l. 99 is offered as one on the paper's reading |
| S-259.5 | partial (class 9), material | partial, minor; drop the proposed action | the row truncates Kong's p. 5 and reads it as 'undivided'; Kong distributes answerability among parties on p. 9, which the auditor's own S-259.3 records |

Faults I found that the auditor missed:

1. S-257.1: Morgan 2015, already in the reference list, states that 'No duty of care can be delegated' and that careful delegation 'ordinarily discharges a duty of care'. The first makes the thesis sentence a truism on one reading; the second defeats it on the other more directly than the 1957 Act does. Morgan also criticises the analogy from contract that the body draws from Woodland para 25(5).
2. S-257.1: s. 2(4)(b) is confined to 'work of construction, maintenance or repair'.
3. S-259.5 against S-259.3: the register reads Kong as undivided in one row and as distributed in the other.
4. S-258.2: a row for a proposition the sentence does not make.
5. S-261.2: the second application date, 2 August 2028.
6. S-278.2: two further uses of 'address' (pp. 3 and 4).
7. S-257.3: knowledge and discretion are parts of the path at l. 82, not rivals to it.

No selected row that the auditor passed should have failed.

---

## All registers

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 (fatal) | 3 | 0 | 1 | 2 |
| 2 (named in the file) | 0 | – | – | – |
| 3 (every fourth, not passed) | 39 | 27 | 10 | 2 |
| 4 (every sixth, passed) | 9 | 7 | 1 | 1 |
| D (disputes, outside the rules) | 3 | 2 | 1 | 0 |
| **All** | **54** | **36** | **13** | **5** |

## Overall judgment

The registers can be relied on for what the sources say and for ordinary rows: every passage I checked sits at its locator, and on 49 of 54 rows I reached the auditor's verdict and severity, with a note on 13. They cannot be relied on, without a second reading, for their gravest grades and for rows that set one text against a sentence or against another text: both 'contradicted, fatal' rows in A9 fail on Bovens' own pages, one clash in A10 rests on a shortened quotation (S-259.5), and one A10 row audits a proposition its sentence does not make (S-258.2). The passes are sound, with one minor miss in nine (T1.r5.c1), so the lead should re-read every `fatal`, `contradicted` and class 9 row before acting on it and can take the rest largely as written.
