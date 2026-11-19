<!-- Claim register, batch A8, run rr-2026-11-k, written by a Claude (Fable 5.2) subagent on 11 Nov 2026. -->

# Claim register A8: 'When a person must be reachable', with Table 1 (S-204 to S-226)

**Scope.** I audited the 23 ledger sentences S-204 to S-226 of `manuscript/DRAFT_v6.md` and the 28 cells of Table 1, 71 rows in all. I did not open `CORRECTIONS_2026-11-11.md`, `VERIFICATION.md` or anything under `manuscript/reviews/`. I used library cards only to find saved texts.

**Ledger against draft.** The last 'As written' line of every entry matches `DRAFT_v6.md`, with one exception. Table 1, identity row, fourth cell: the ledger (S-211) has 'A staffed fallback; a reachable person if failure would refuse entry'; the draft has 'A staffed fallback that is not a downgraded route; a reachable person if failure would refuse entry'. I audited the draft's wording.

**What I read, and how much.**

- In full: Baum and Laux, the LNCS version of record (`sources/baum2026constitutive/vor/chapter.txt`, pp. 115–130; I checked that PDF page 6 is printed p. 120). Article 29 Working Party, WP251rev.01 (`sources/wp29_2018adm/wp251.txt`, pp. 5–37, the whole text and annexes). 42 U.S.C. § 2000a(a)–(e) (`sources/usc2000a/lii.txt`, and a second copy I fetched from govinfo.gov, U.S. Code 2024 edition, saved as `sources/usc2000a/govinfo_usc2024_sec2000a.htm`; the two agree on subsections (a), (b)(1) and (e), which I compared).
- The provisions only: Regulation (EU) 2016/679, arts 12 and 22 and recital 71 (`sources/gdpr2016art22/gdpr.txt`, Official Journal text from the Publications Office). Hotel Proprietors Act 1956, s. 1. Directive (EU) 2015/2302, arts 7, 13, 15, 16. Equality Act 2010, ss 20, 29. Data (Use and Access) Act 2025, s. 80. CJEU, C-634/21 *SCHUFA*, paras 51–56.
- Passages only, to test Table 1: Xiang et al. (2022), Sandoval-Strausz (2005: 62–64), Wilson-Nash et al. (2026: 977–978), Di Domenico and Lynch (2007: 322), Garcia et al. (the CESifo working paper, not the *Management Science* version), Chang et al. (2022).
- Abstract only: Ivanov and Webster (2024). ScienceDirect returned 403 and a bot page to `curl` and to WebFetch, the Elsevier API asked for a key, and Unpaywall and OpenAlex list no repository copy. The article is CC BY, so a person can download it.

**How to read the tables.**

- Classes are the brief's nine: 1 Population, 2 Setting, 3 Strength, 4 Speaker, 5 Scope, 6 Design, 7 Application, 8 Version, 9 Combination.
- Passages come from the saved text. I rejoined words split at line ends, expanded ligatures and normalised quotation marks; an ellipsis marks a cut.
- For a stipulation (a row label in Table 1), `valid` means the label keeps one sense through the batch, and `equivocal` means it does not.
- A table cell that rests on no source is typed 'Own inference (judgment)' if it grades stakes or prescribes recourse, and 'Empirical generalization (unsourced)' if it says how hotels operate. The second kind is `unverifiable` unless a saved source bears on it.
- S-ids outside the batch (S-075, S-092, S-102, S-104, S-175, S-176, S-183, S-192, S-196, S-237, S-244, S-266) point to sentences I read in the draft but did not audit.
- Legal rows: 'later treatment' is stated in each.

---

### S-204 · When a person must be reachable ¶1
> Not every touchpoint needs a person with authority standing by.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-204.1 | Some touchpoints need no person with authority present at the moment a decision is taken | Own inference | — | — | — | valid | — | None. The sentence survives a rebuilt criterion, because S-196 alone carries it. |

- Premises. P1 (earlier inference, S-196): some touchpoints decide nothing about the guest (the projected chef). P2 (stipulation, S-102): authority is the power to change a decision or the rule behind it. C: where nothing is decided, there is nothing for a person with authority to change at that moment.
- Counter-model: none. S-183 requires that some party be obliged to answer; it does not require that a person stand by.
- Terms: 'standing by' means present when the decision is taken. Quantifier: 'not every' needs one instance, and P1 gives it.
- K claim: K7 (the timing boundary).

### S-205 · ¶1
> Baum and Laux distinguish forms of human involvement in automated systems by whether intervention can come before a decision takes effect, and what matters, they write, is 'not elapsed time but whether intervention can occur before the token output becomes effective' (2026: 120).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-205.1 | Baum and Laux distinguish forms of human involvement in automated systems by whether intervention can come before a decision takes effect | Paraphrase | Baum and Laux, LNCS 17146 version of record, abstract (p. 115) and § 2.3 (p. 120) | "HITL is constitutive (a human contribution is necessary for the decision output), while HOTL is corrective … Within HOTL, we distinguish temporal modes—synchronous, asynchronous, and anticipatory" (p. 115) | 5 (their main division is causal, gate against switch; timing is a gradation inside corrective oversight only, and it separates two of the three modes: the third, anticipatory, always precedes the decision); 2 (AI systems, not automated systems at large) | partial | minor | Say 'within corrective oversight' or 'among forms of human oversight'. Their examples are vehicles, surgery, an ICU, a warehouse, parole and hiring; none is a service encounter. |
| S-205.2 | The quoted words, and that the authors say them | Quotation | same, § 2.3, p. 120 | "Where periodic review occurs before outputs take effect (e.g., decisions released only after batch review), the configuration is, in our terms, synchronous with latency: the distinguishing feature is not elapsed time but whether intervention can occur before the token output becomes effective." | none | supported | — | None on the words or the page. The clause settles how to class batch review before release; 'what matters' is a fair gloss of 'the distinguishing feature'. Version: the chapter's footer reads '© The Author(s) 2027 … LNCS 17146, pp. 115–130, 2027'; Crossref gives online publication on 13 Oct 2026. The reference list says 2026 and names no editor (B. Steffen) or series. The authors should choose the year. |

### S-206 · ¶1
> Synchronous intervention can change the decision a person is subject to, asynchronous review shapes future decisions, and for decisions too fast for any person the only human control is a limit set in advance and kept open to revision (Baum and Laux 2026: 120–122).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-206.1 | Synchronous intervention can change the decision a person is subject to | Paraphrase | Baum and Laux, version of record, pp. 120–121 | "Only synchronous HOTL can become outcome-HITL for a given deployer-runtime decision (cf. footnote 4): upon intervention, the human becomes causally necessary for the specific output." | 7, 1 ('a person is subject to' is the paper's; the human in the source is a monitor 'watching a dashboard', p. 120, and the section names no person affected by the output) | partial | minor | Write 'the decision in hand' or 'the individual decision'. The gloss prepares the move from an overseer to a guest, which is the paper's (S-207). |
| S-206.2 | Asynchronous review shapes future decisions | Paraphrase | same, pp. 120, 121 | "asynchronous HOTL intervenes after the decision has been made, shaping future iterations" (p. 121); "the intervention targets future system behavior … rather than the decision currently being made" (p. 120) | none | supported | — | None. Hold the paper to it: by this sentence a later review does not reach the decision already made (see S-209.1). |
| S-206.3 | For decisions too fast for any person, the only human control is a limit set in advance and kept open to revision | Paraphrase | same, p. 122, and p. 120 n. 5 | "The same vehicle executes emergency braking autonomously; here, the human is not meaningfully a synchronous HOTL: the intervention happens too fast for real-time correction. However, if a human can adjust parameters governing emergency braking behavior … this constitutes anticipatory HOTL." (p. 122) | 3 ('the only human control' is not in the source: asynchronous review also remains, and the general statement is hedged, 'may render reactive oversight modes insufficient while anticipatory oversight remains viable', p. 121); 6 (one example, a vehicle's brakes, stated as a rule) | partial | minor | Drop 'only', or write 'what remains at the moment is'. 'Kept open to revision' is sourced: 'A choice that is not revisitable within the system's life-cycle is design, not corrective involvement' (p. 120 n. 5). Pages 120–122 are right. |

### S-207 · ¶1
> Applied to hospitality, the distinction gives a boundary that follows the host's obligation.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-207.1 | The source's distinction, applied to hospitality, yields the boundary stated in S-208 and S-209 | Own inference | Baum and Laux, p. 116, for what the distinction is | "our taxonomy is primarily descriptive: it characterizes the causal structure of human involvement in AI systems. … Satisfying the descriptive conditions (e.g., being in a HOTL configuration) is typically necessary but not sufficient for meeting normative demands" | 7 | valid with added premise | material | The source supplies one thing: only an intervention before the output takes effect can change that output. The boundary adds four things the source does not have (listed below). Credit the source with the timing test and state the boundary as the paper's. |
| S-207.2 | The boundary follows the host's obligation | Own inference | — | — | — | valid with added premise | material | The premise is K7's P3, which v6 does not state. As v6 stands, the nearest step is S-123, and it does not carry a duty to be reachable in advance. |

- **S-207.1.** P1 (sourced, S-205.2, S-206.2): an intervention changes an output only if it can occur before the output takes effect; later review shapes later outputs. P2 (assumption): a decision 'takes effect on the guest' when the system's output takes effect. P3 (assumption): some effects can be undone before they harm the guest, and for those a later reversal serves as well as prior intervention. P4 (assumption): the human who can intervene is one the guest can reach, where the source's human monitors the system and is reached by nobody. P5 (earlier inference, K7): the guest is owed the intervention. C: the boundary of S-208 and S-209.
- Counter-model: P1 true and C false. A hotel staffs a control room whose operator can stop any output before release and takes no calls from guests. The source's synchronous oversight is complete; the paper's reachable party is absent.
- Terms: 'takes effect' (source: the output becomes operative; paper: the guest is affected); 'intervention' (source: by an overseer; paper: at the guest's instance).
- Overgeneration and undergeneration: see S-208.1.
- K claim: K7. Verdict: valid with P2–P5 added.
- **S-207.2.** P1 (earlier inference, K4, K5): the host owes the guest duties for the length of the stay. P2 (earlier inference, K8, S-123): the duties stay with the holder when a system does the work. P3 (the paper's step, K7 P3, not in v6): a duty to see that something is done includes the means to learn that it is not being done and to correct it while it can still be done. C: the need for a reachable person tracks whether performance is still possible.
- Counter-model without P3: the host performs every duty through its systems and pays compensation after each failure. The duty and the guest's claim are intact and no one was reachable.
- K claim: K7. Verdict: valid with P3 added.

### S-208 · ¶1
> Where a decision takes effect on the guest's person, access or contract during the stay and cannot be undone before the harm lands, the guest needs a reachable party with authority before it takes effect.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-208.1 | For decisions of this class the guest needs a reachable party with authority before the decision takes effect | Own inference | — | — | — | valid with added premise | material | This is the row the subsection, Table 1, Table 2 (stage 4) and S-244 rest on. State it as the paper's proposal, give K7's P3 as its ground, and make the consequent match the antecedent ('before the harm lands'). |
| S-208.2 | The class: a decision that takes effect on the guest's person, access or contract, during the stay, and cannot be undone before the harm lands | Definition or stipulation | — | — | — | equivocal | material | Three uses in another sense, listed below. |

- **S-208.1.** P1 (sourced, S-206.1, S-206.2): only intervention before an output takes effect changes it. P2 (earlier inference, K4, K5, K8): the host's duties run through the stay and stay with the holder. P3 (the paper's step, K7 P3): the holder must be able to learn of a failure and correct it while performance is possible. P4 (assumption, K7 P4, empirical): the guest's report is often the only timely signal, and correction needs a person with power over the single case. P5 (stipulation): the decision cannot be undone before the harm lands. C: the guest needs a reachable party with authority before the decision takes effect.
- Counter-model: a lock deactivates at 23:00. The guest learns of the decision by meeting its effect, so no party is reachable 'before it takes effect' unless the system waits for a human (the source's gate, or review before release). What the premises support is a party reachable before the harm lands, or a human gate on the host's side. The antecedent says 'harm'; the consequent says 'effect'. Added premise: the guest learns of the decision before it takes effect.
- Terms. *Authority*: S-102 defines it as power to change 'a decision or the rule behind it'; S-176 sets 'discretion' (the single case) against 'authority' (the rule). What S-208 needs in time is power over the single case, which S-176 calls discretion. On S-176's usage a desk clerk with discretion would meet the criterion. *Reachable*: by the guest; the source has no such relation.
- Quantifiers: P4 says 'often'; C says 'needs' of every such decision. Where a system detects its own failure, the guest's reach is not needed.
- Overgeneration: the argument proves the same of a bank that blocks a card abroad at night, an airline that denies boarding and a hospital's triage software. The paper concedes the mechanism is general at S-066 to S-070, not here.
- Undergeneration: a restaurant has no stay and no night; a guest placed and paid for by a third party has no contract, and the party with power over the case may be the placing agency (the draft's own cases, which I did not audit: Petie et al. 2025; *Crinkley* 1988: 167 n. 3); in a short-term rental the criterion applies but S-224 to S-226 then call the obligation weakest.
- K claim: K7, with K9 for decisions before reception.
- **S-208.2, uses in another sense.** (a) 'During the stay': Table 1 heads with admission at the door and 'a booking not honoured', and includes pricing; all three are usually settled before a stay begins, and K9 treats admission as a separate failure. (b) 'Takes effect' against 'harm lands', as above. (c) 'Undone': reversed in S-208, compensated in the 'later appeal' rows of Table 1 (T1.r4.c4).

### S-209 · ¶1
> Where a decision can be deferred or undone, a reachable appeal is enough, and where it is too fast for anyone, the host answers for the rule it set in advance.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-209.1 | Where a decision can be deferred or undone, a reachable appeal is enough | Own inference | Baum and Laux, p. 120, for the slot the sentence fills | "The corrective capacity exists, but is temporally displaced from individual decisions: the intervention targets future system behavior (e.g., by adjusting parameters or triggering retraining) rather than the decision currently being made." | 7 | equivocal | material | The sentence sits where the source's asynchronous mode sits, and that mode does not touch the decision already made. An appeal that reverses the guest's own outcome has no place in the taxonomy. Say that the appeal is the paper's category. |
| S-209.2 | Where a decision is too fast for anyone, the host answers for the rule it set in advance | Own inference | same, p. 122 and p. 120 n. 5 (quoted at S-206.3) | — | — | valid with added premise | minor | Added premise: the host set the rule. S-175 says authority over the rule 'drifts towards whoever designs, configures or controls it, often a vendor'. Write 'the rule under which the system ran'. The source's condition 'kept open to revision' is in S-206 and Table 1 and missing here. |

- **S-209.1.** P1 (earlier inference, S-208.1): prior reach is needed only where the effect cannot be undone in time. P2 (assumption): where it can, a later reversal repairs the guest fully. P3 (assumption): the guest knows a decision was taken. P4 (assumption): the appeal has power to reverse (S-244 adds 'with authority to reverse'; S-209 omits it). C: a reachable appeal is enough.
- Terms. *Later review / appeal*: in S-206.2 it 'shapes future decisions'; here it undoes this one. *Deferred*: a decision held until a person has reviewed it is, in the source's terms, 'synchronous with latency' (p. 120), the first class and not the second. *Undone*: reversed, or compensated after a one-night stay has ended.
- Counter-model: a deposit hold on a debit card is released in a week; it 'can be undone', and the guest is without funds for the trip. The antecedent needs 'in time', which Table 1's column head has and the sentence lacks.
- K claim: K7 (repair after the fact belongs to accountability). Verdict: equivocal.
- **S-209.2.** P1 (sourced, S-206.3): for outputs too fast for real-time correction a human can still set and revise parameters. P2 (earlier inference, K8): the holder answers for performance by others. P3 (assumption): the host set the rule. C: the host answers for it. Counter-model: a vendor's default configuration; K8 still makes the host answer, so the conclusion needs 'whoever set it'. No hospitality decision of this kind is named anywhere in the paper. K claim: K8.

### S-210 · ¶2
> Table 1 places common hospitality decisions against this boundary.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-210.1 | Table 1 follows | Signpost | — | — | — | — | — | Recorded. |
| S-210.2 | The decisions in the table are common hospitality decisions | Empirical generalization (unsourced) | none cited; nearest is Ivanov and Webster (2024), abstract only | "applied to 23 decisions in 8 hotel departments" (abstract; the list is in the closed full text) | 2 (every row is a lodging decision: check-in, room, booking; no restaurant or bar decision appears, though the section covers three formats) | unverifiable | minor | Ivanov and Webster's list of 23 decisions would settle whether hoteliers recognise these seven. Write 'hotel decisions', or add a restaurant row. The table has no row for a guest's belongings, the oldest of the duties the paper lists at S-065. |

### S-211 · Table 1
> **Table 1. Hospitality decisions by stakes, reversibility and the recourse they need**

The table cites nothing. For each row I asked three things: whether the stakes entry has a source or is the paper's judgment; whether 'Reversible in time?' is true of how hotels operate, what would settle it, and what in the library bears on it; and whether the recourse follows from S-208 and S-209.

### T1.r1 · Admission
> | Admission or refusal at the door or at check-in; a booking not honoured | High: shelter for the night | No | A reachable person with authority before refusal takes effect |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r1.c1 | Refusal at the door, refusal at check-in and a booking not honoured are one kind of decision | Definition or stipulation | — | — | — | equivocal | minor | A booking can fail days before arrival, remotely and with time to rebook; a refusal at the door cannot. The first is not 'during the stay' (S-208) and falls where S-223 says the framework explains less. Split the row or say which case it means. |
| T1.r1.c2 | The stakes are high, because shelter for the night is at stake | Own inference (judgment) | nearest: Sandoval-Strausz (2005: 64), on early American innkeeper law | "In this way the early American law of travel sought to ensure that all innkeepers fulfilled the primary purpose of the inn as a shelter for travelers." | — | valid with added premise | minor | The paper's judgment; no source grades stakes. Added premise: no other lodging is within the guest's reach that night. |
| T1.r1.c3 | A refusal cannot be reversed in time | Empirical generalization (unsourced) | Xiang et al. (2022), 'Performance pathways: managing ritual violations' (saved article text, no page numbers) | "Upon arrival, the staff couldn't let the guest check-in, and helped him to book another hotel in another district with different policies. However, the guest was still very angry and came back the next day to file complaints to the general manager and the group head office." | 3 | partial | material | The flat 'No' is contradicted twice. S-212 says only that 'some of these decisions cannot be undone in time'. And in the paper's own source the refusal stood while the harm (no shelter) was averted by rebooking; another guest in the same study 'left the hotel and went to another hotel'. Write 'Often not', and decide whether relocation counts as recourse. |
| T1.r1.c4 | The recourse needed is a reachable person with authority before refusal takes effect | Own inference | — | — | — | valid with added premise | material | Follows from S-208 once 'takes effect' is read as the guest leaving without shelter. The cell is normative; see the list. |

- **Reversibility: what would settle it.** Records of refused arrivals and relocated ('walked') guests: how many were placed elsewhere the same night, how long it took, and who authorised it. The library holds no such study. It holds three cases in Xiang et al. (one guest for whom, 'after checking with hotel management', the hotel paid for a test and arranged transport to it; one rebooked elsewhere; one who gave up after an hour and a half at reception), and a rule that limits the duty to rooms that exist: innkeepers had 'to provide any available accommodation' (Sandoval-Strausz 2005: 63).
- **T1.r1.c4.** P1 (S-208.1). P2 (earlier inference, S-075; K4): the duty to receive is in force when the traveller presents. P3 (assumption): the person reached can admit the guest, or place the guest elsewhere. C: as the cell.
- Counter-model: a full house. No one's authority can undo the refusal; what helps is relocation, which the cell omits.
- The legal register gives repair, not a hearing: 'an innkeeper's refusal to admit a guest gave that person the right to sue the innholder for any resultant damages' (Sandoval-Strausz 2005: 63). That is K7's own refuter ('remedies doctrine that is satisfied by damages afterwards').
- Undergeneration: a placed guest (the party with authority may be the agency that placed them); a restaurant (no night).
- K claim: K7, K9 (the decision precedes reception).

### T1.r2 · Safety and access
> | Safety and access on the premises (lock-out, alarm, removal) | Highest | Often not; some too fast for any person | A reachable person where one can act in time; otherwise limits set in advance by the host and kept open to revision |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r2.c1 | Lock-out, alarm and removal are decisions of one kind | Definition or stipulation | — | — | — | equivocal | minor | An alarm is a safety function and decides nothing about a particular guest (S-006 defines an algorithmic system by 'a decision about a guest'). Removal is slow and deliberate. Lock-out is a matter of access, the same stake as row 1. |
| T1.r2.c2 | The stakes are the highest in the table | Own inference (judgment) | — | — | — | valid with added premise | minor | The paper's judgment, from the duty to protect. Added premise: each listed item endangers the person. That holds of an alarm; a lock-out or a removal costs shelter, which row 1 grades 'High'. The row graded 'Highest' stands second (see S-216). |
| T1.r2.c3 | These decisions often cannot be reversed in time, and some are too fast for any person | Empirical generalization (unsourced) | Baum and Laux, p. 122, for 'too fast' only | "the human is not meaningfully a synchronous HOTL: the intervention happens too fast for real-time correction" (of a vehicle's emergency braking) | 7 (the only 'too fast' instance is a car's brakes; the paper names no hospitality decision of this kind) | unverifiable | minor | What would settle it: incident logs of key deactivations and the time to restore access, alarm events, and removals. The library holds nothing on lock-outs. On removal it holds one line, and it describes a slow, human process: 'Only when guests do not abide by the ritual after repeated communications will they be asked to leave the hotel' (Xiang et al. 2022). |
| T1.r2.c4 | The recourse is a reachable person where one can act in time; otherwise limits set in advance by the host and kept open to revision | Own inference | Baum and Laux, p. 120 n. 5, for the second limb | "it is subject to iterative refinement—the human can inspect operational behavior and revise the normative constraints accordingly" | — | valid with added premise | material | Follows from S-208 and S-209. Added premise: the host sets and can revise the limits. S-175 says the rule is 'often' the vendor's, who keeps the right to 'change, withdraw, or cancel products and services at will'. In the arrangements the paper describes, the second limb may be unavailable; say what the host owes then. K claim: K7, K8. |

### T1.r3 · Identity verification
> | Identity verification | Low as verification; high if failure blocks entry | Yes, if a staffed route exists | A staffed fallback that is not a downgraded route; a reachable person if failure would refuse entry |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r3.c1 | Identity verification is a decision distinct from admission | Definition or stipulation | — | — | — | valid | — | Consistent with S-193 ('a clerical job'). |
| T1.r3.c2 | Stakes are low as verification and high if failure blocks entry | Own inference (judgment) | — | — | — | valid | — | The paper's judgment. The second limb reduces to row 1. |
| T1.r3.c3 | A failed verification can be reversed in time if a staffed route exists | Own inference | — | — | — | valid with added premise | minor | Added premise: the staff on that route can admit on other evidence. S-198 to S-201 describe an employee who stands between guest and system without that power. Whether staffed routes exist is the open fact: Airbnb's self-check-in lets guests arrive 'without meeting anyone in person' (Bosma 2022: 605, as quoted at S-195), and Chang et al. (2022) study 'unmanned smart hotels'. Field data on failure rates and time to admission would settle it. Boo and Chua (2022) is carded at abstract depth; I did not open it. |
| T1.r3.c4 | The recourse is a staffed fallback that is not a downgraded route, and a reachable person if failure would refuse entry | Own inference | Wilson-Nash et al. (2026: 978), for 'downgraded' | "this environmental shift may occur in terms of substitution (analogue access replaced by digital), co-existence (analogue retained but downgraded and more difficult to access), liquid digital (constant updating), or a move to digital-only (systemic) access" | 2 (the source's cases are banking, e-visas and app-only offers) | valid with added premise | minor | The first limb comes from the 'real alternative' principle (S-237), which the paper states after the table; it does not follow from the timing criterion. The second limb is row 1. The draft's cell differs from the ledger's (see the note at the head of this file). |

### T1.r4 · Room assignment
> | Room assignment | Low to moderate; high where a guest's need makes a room unusable | Mostly | A later appeal by default; a reachable person where the room cannot be used |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r4.c1 | Room assignment is a decision about the guest | Definition or stipulation | — | — | — | valid | — | None. |
| T1.r4.c2 | Stakes are low to moderate, and high where a guest's need makes a room unusable | Own inference (judgment) | — | — | — | valid with added premise | minor | The paper's judgment. Added premise: apart from usability, a room is a matter of preference. A lead for the high case: in Great Britain a service-provider owes disabled persons 'such steps as it is reasonable to have to take to avoid the disadvantage' (Equality Act 2010, ss 20(3), 29(7)(a); saved). K4 lists this as a possible legal duty of adjustment. |
| T1.r4.c3 | A room assignment can mostly be reversed in time | Empirical generalization (unsourced) | — | — | — | unverifiable | minor | It turns on occupancy: with the house full there is no other room. Property-management records of room-move requests, by occupancy, would settle it. The library holds nothing; Spektor et al. (2025) concerns staff. |
| T1.r4.c4 | The recourse is a later appeal by default, and a reachable person where the room cannot be used | Own inference | — | — | — | equivocal | material | The second limb follows from S-208. The first does not follow from the third cell. If the assignment is 'mostly' reversible in time, someone must be reachable during the stay to reverse it; an appeal after a one-night stay can only compensate. 'Undone' shifts from reversed to compensated. The two-way boundary has no place for an appeal during the stay with power to reverse, which is what this row needs. K claim: K7. |

### T1.r5 · Pricing
> | Pricing | Usually moderate; significant if a price bars access | Yes | A later appeal, and rules the host can explain |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r5.c1 | Pricing is a decision about the guest | Definition or stipulation | — | — | — | valid | — | A price is usually set before arrival, where S-223 says the framework explains less. |
| T1.r5.c2 | Stakes are usually moderate, and significant if a price bars access | Paraphrase (source uncited in this subsection; cited at S-192) | Article 29 Working Party, WP251rev.01, p. 22 | "Automated decision-making that results in differential pricing based on personal data or personal characteristics could also have a significant effect if, for example, prohibitively high prices effectively bar someone from certain goods or services." | 3 ('could' dropped); 5 (the passage concerns solely automated pricing on personal data; in the paper's own case managers 'retain the final decision right' and set a price for a room and date: Garcia et al., CESifo working paper, p. 2) | partial | minor | 'Usually moderate' is the paper's grading. Restore the hedge or mark the cell as the paper's. |
| T1.r5.c3 | A price can be reversed in time | Empirical generalization (unsourced) | — | — | 3 | partial | minor | True of a charge that can be refunded. False of the case the second cell singles out: a price that bars access cannot be undone once the night has passed. The cell contradicts its neighbour. Evidence that would settle the ordinary case: how often hotels reprice or refund after booking. |
| T1.r5.c4 | The recourse is a later appeal, and rules the host can explain | Own inference | — | — | — | undergenerates | material | By S-208 a price that bars access to shelter needs a reachable person, as rows 3 and 4 provide for their high case; S-214 says pricing does need one, and the cell does not. 'Rules the host can explain' comes from predictability, not from the timing criterion, and the paper's own case found that 'neither a guest nor the staff at the desk could anticipate the operative rule' (S-192). A lead: EU consumer law already requires a trader to tell a consumer 'that the price was personalised on the basis of automated decision-making' (Directive 2011/83/EU, art. 6(1)(ea), inserted by Directive (EU) 2019/2161; saved). K claim: K7. |

### T1.r6 · Complaints and service recovery
> | Complaints and service recovery | Varies with the failure | Partly | A reachable person with authority, at a time that suits the guest |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r6.c1 | Complaints and service recovery are a decision | Definition or stipulation | — | — | — | equivocal | minor | This row is the recourse channel itself. Its 'recourse' is recourse for the handling of a complaint, which the paper does not say. |
| T1.r6.c2 | Stakes vary with the failure | Own inference (judgment) | — | — | — | valid | — | True by construction. |
| T1.r6.c3 | Recovery is partly reversible in time | Empirical generalization (unsourced) | nearest: Tang et al. (2018), abstract only, hotel scenarios | "immediate and economic recovery effectively raises the service recovery evaluations from customers with low-intensity negative emotions, whereas delayed and psychological recovery helps customers with high-intensity negative emotions" | — | unverifiable | minor | Records of time to resolution, and of the rank of the person who resolved, would settle it. Tang et al. measure evaluations in a scenario experiment, not reversal. Hewagama et al. (2019) is carded at abstract depth; I did not open it. |
| T1.r6.c4 | The recourse is a reachable person with authority, at a time that suits the guest | Own inference | — | — | — | valid with added premise | minor | The cell does not follow from the timing criterion, which for a 'partly' reversible decision gives a mixed answer. It follows from S-148 (a hearing by someone with authority). 'At a time that suits the guest' is new and unsourced. It also sits uneasily with S-244, which gives 'a later appeal' to everything that is not irreversible on site. K claim: K7. |

### T1.r7 · Routine requests and information
> | Routine requests and information | Low | Yes | Automation, under rules set in advance |

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| T1.r7.c1 | Routine requests and information form a class | Definition or stipulation | — | — | — | valid | — | These are service functions; they decide little about the guest. |
| T1.r7.c2 | Stakes are low | Own inference (judgment) | — | — | — | valid with added premise | minor | Added premise: the information bears on neither safety nor access. |
| T1.r7.c3 | These can be reversed in time | Empirical generalization (unsourced) | — | — | — | unverifiable | minor | Chatbot escalation and failure records would settle it. The library holds nothing. |
| T1.r7.c4 | The recourse is automation under rules set in advance | Own inference | — | — | — | undergenerates | minor | S-209 gives a reversible decision 'a reachable appeal'; this row gives none. It relies on a threshold of stakes that the criterion does not contain. S-209 also keeps 'rules set in advance' for decisions too fast for anyone, a different class. And the cell needs the fifth principle to hold with it (S-237: a real alternative), or a guest without the app has no route. K claim: K7. |

### S-212 · ¶3
> Admission and refusal, and safety and access on the premises, head the table, because shelter for the night is at stake and some of these decisions cannot be undone in time; the regulators give the cancellation of a contract as an example of a legal effect, which would cover a booking (Article 29 Working Party 2018: 21).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-212.1 | The first two rows head the table because shelter is at stake and some of these decisions cannot be undone in time | Own inference | — | — | — | valid with added premise | minor | Added premise: the table is ordered by stakes and irreversibility together. 'Some … cannot be undone' is right and contradicts the table's flat 'No' (T1.r1.c3). |
| S-212.2 | The regulators give the cancellation of a contract as an example of a legal effect | Paraphrase | Article 29 Working Party, WP251rev.01 (revised 6 Feb 2018), p. 21 | "A legal effect may also be something that affects a person's legal status or their rights under a contract. Examples of this type of effect include automated decisions about an individual that result in: cancellation of a contract; …" | none | supported | — | Page confirmed. Speaker: 'an independent European advisory body' (p. 1) of the data-protection authorities; the EDPB's site lists the guidelines as endorsed at its first plenary. The example is of an effect that brings a solely automated decision within Article 22. No jurisdiction is named until S-218; 'the regulators' leans on S-192. |
| S-212.3 | That example would cover a booking | Own inference | — | — | — | valid with added premise | minor | 'Would' marks it as the paper's. Added premises: the booking is a contract; a solely automated decision about the guest cancels it. A booking 'not honoured' (Table 1) is a breach, not a cancellation. |

### S-213 · ¶3
> Routine requests and information sit at the foot and can be automated under rules set in advance.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-213.1 | Routine requests and information can be automated under rules set in advance | Own inference (restates T1.r7.c4) | — | — | — | undergenerates | minor | As T1.r7.c4. The prose matches the table. |

### S-214 · ¶3
> Identity checks need a staffed fallback, room allocation and pricing a later appeal by default, and each a reachable person where failure would refuse entry or leave a room unusable.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-214.1 | Identity checks need a staffed fallback | Own inference (restates T1.r3.c4) | — | — | — | valid with added premise | minor | As T1.r3.c4. The prose drops 'that is not a downgraded route'. |
| S-214.2 | Room allocation and pricing need a later appeal by default | Own inference (restates T1.r4.c4, T1.r5.c4) | — | — | — | equivocal | minor | As T1.r4.c4: 'later' cannot reverse within a short stay. |
| S-214.3 | Each of the three needs a reachable person where failure would refuse entry or leave a room unusable | Own inference | Table 1, pricing row | — | — | contradicted (by Table 1) | minor | The pricing row gives no reachable person in any case. Either the table is right and 'each' is wrong, or the prose is right and the cell is incomplete; S-208 supports the prose. |

### S-215 · ¶3
> The placements are our own reading of the sources cited; the nearest hospitality study asks hoteliers which of 23 hotel decisions they would leave to artificial intelligence, not what recourse a guest needs (Ivanov and Webster 2024).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-215.1 | The placements are the paper's own reading of the sources cited | Own statement of sourcing | Table 1, against this subsection's citations | — | 7, in reverse (judgment presented as a reading of sources) | partial | material | 'Our own' is right. 'Reading of the sources cited' is not: of 28 cells, five draw on a source (T1.r1.c2 through S-212, T1.r2.c3, T1.r2.c4, T1.r3.c4, T1.r5.c2), and for two of the five the source is cited elsewhere (WP251 p. 22 at S-192; Wilson-Nash et al. after the table). The other 23 cells, among them the reversibility column apart from 'too fast', rest on nothing cited. S-266 repeats the claim. Say that the placements are the authors' judgments and name the cells that have a source. |
| S-215.2 | Ivanov and Webster (2024) is the nearest hospitality study | Gap claim | library cards; Consensus; OpenAlex (queries in closing list 4) | — | 3 (a superlative no logged search supports) | partial | material | I found no study that sorts hospitality decisions by the recourse a guest needs. I did find hotel experiments on the guest's side that ask whether a human must step in after an automated failure, one of them by severity of failure. They are leads (closing list 5). Give the claim in the run's form: 'I found no work that does X in [sources, queries, date]'. |
| S-215.3 | The study asks hoteliers which of 23 hotel decisions they would leave to artificial intelligence | Case description | Ivanov and Webster (2024), *Technology in Society* 76, 102430; abstract from the saved OpenAlex record | "It evaluates the preferences towards four decision-making approaches ('human only', 'human-in-the-loop', 'human-on-the-loop' and 'human-out-of-the-loop') applied to 23 decisions in 8 hotel departments. The sample includes 130 respondents from the Bulgarian hotel industry." | none at abstract depth | supported (abstract only) | minor | 'Would leave to' compresses four graded approaches into one. The sample is 130 respondents in one country. Read the full text before the sentence goes forward. |
| S-215.4 | The study does not ask what recourse a guest needs | Case description | same, abstract | "The paper investigates the attitudes of hoteliers towards the use of artificial intelligence in the decision-making process in various departments within hotels." | none at abstract depth | supported (abstract only) | minor | A statement of what a study omits needs the full text. |

### S-216 · ¶3
> The order follows the duties to receive and to protect, which is why admission and safety come first.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-216.1 | The table's order follows the duties to receive and to protect | Own inference | — | — | — | valid with added premise | minor | The two duties explain the first two rows. They do not order the other five: complaints, whose recourse is the strongest after row 1, stands sixth. The title promises an order by stakes, and the row graded 'Highest' is second. S-065 lists four duties (receive, sustain, protect, attend) in another order. K claim: K4. |

- P1 (earlier inference, S-065, K4): the host's duties are to receive, to sustain, to protect and to attend. P2 (assumption): the rows are ordered by the duty each decision touches. C: admission and safety come first. Counter-model: order the rows by P2 and room assignment (sustain) precedes safety (protect). Verdict: valid for rows 1 and 2 with the premise that only two duties order the table.

### S-217 · ¶4
> The law sets a floor beneath this boundary rather than a ceiling.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-217.1 | The law requires less than the boundary and does not cap what a host may offer | Own inference | Regulation (EU) 2016/679, art. 22; WP251rev.01, pp. 19, 21 | "Article 22(1) establishes a general prohibition for decision-making based solely on automated processing. This prohibition applies whether or not the data subject takes an action regarding the processing of their personal data." (WP251, p. 19) | 2 (one EU regulation stands for 'the law'); 5 | valid with added premise | material | Name the law: Article 22 of the GDPR, in the Union. The floor exists only where a decision is solely automated, rests on personal data, has a legal or similarly significant effect ('only serious impactful effects will be covered', WP251 p. 21) and falls within art. 22(2)(a) or (c). See the list. |

- P1 (sourced, S-218): art. 22(3) gives a right to human intervention and to contest. P2 (sourced, S-219): the reviewer must be able to change the decision. P3 (sourced in part, S-220.1): the Article fixes no moment. C: the law asks less than the boundary.
- Counter-model 1: a solely automated decision with a legal effect that is not necessary for the contract and has no explicit consent. Article 22(1) forbids it outright, however reversible. The paper's boundary would allow it with a later appeal. There the law stands above the boundary.
- Counter-model 2: room assignment, routine requests and prices set without personal data do not reach Article 22's threshold. There the law sets no floor.
- Counter-model 3: other law asks for more than a later review (S-221).
- Jurisdiction: the UK has replaced Article 22 with arts 22A–22D (Data (Use and Access) Act 2025, s. 80; saved). The United States has no counterpart in the library.
- K claim: K7 ('law that enacts the conclusion' and 'remedies … satisfied … afterwards').

### S-218 · ¶4 (two sentences since the split of 11 Nov)
> Under the General Data Protection Regulation, a person has the right not to be subject to a solely automated decision with legal or similarly significant effects (Regulation (EU) 2016/679, art. 22(1)). Where such a decision is allowed because it is necessary to a contract, among other grounds, the controller must provide 'at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision' (art. 22(2)–(3)).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-218.1 | A person has the right not to be subject to a solely automated decision with legal or similarly significant effects | Legal proposition | Regulation (EU) 2016/679, OJ L 119, 4.5.2016, art. 22(1) | "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her." | none | supported | — | Jurisdiction: EU law. 'A person' is a data subject, so the right presupposes processing of personal data. Later treatment: the CJEU reads the paragraph as 'a prohibition in principle, the infringement of which does not need to be invoked individually' (C-634/21 *SCHUFA*, 7 Dec 2023, para 52; saved). Corrigenda and later cases: not checked. |
| S-218.2 | The quoted words of art. 22(3) | Quotation | same, art. 22(3) | "the data controller shall implement suitable measures to safeguard the data subject's rights and freedoms and legitimate interests, at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision." | none | supported | — | Words exact. |
| S-218.3 | The duty to provide these rights applies where the decision is allowed as necessary to a contract, 'among other grounds' | Legal proposition | same, art. 22(2), (3) | "In the cases referred to in points (a) and (c) of paragraph 2, the data controller shall implement suitable measures …" | 5 | partial | minor | The minimum in art. 22(3) attaches to two of the three grounds: contract (a) and explicit consent (c). Under (b) the authorising law must itself lay down 'suitable measures'. Write 'or rests on explicit consent'. The contract must be one 'between the data subject and a data controller' (art. 22(2)(a)), which a guest booked by an employer may not have. |

### S-219 · ¶4
> The guidance on that article requires the reviewer to be someone 'who has the appropriate authority and capability to change the decision' (Article 29 Working Party 2018: 27).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-219.1 | The quoted words | Quotation | WP251rev.01, p. 27 | "Human intervention is a key element. Any review must be carried out by someone who has the appropriate authority and capability to change the decision." | none | supported | — | Words exact; page confirmed. The guidance calls the intervention a 'review'. |
| S-219.2 | The guidance on art. 22 requires this of the reviewer | Legal proposition | same, pp. 1, 27 | "It is an independent European advisory body on data protection and privacy." (p. 1) | none | supported | — | The guidance says 'must'. It is guidance, not legislation; the sentence says so. A second passage would serve the paper's main case: a clerk who applies a system's output 'without any actual influence on the result' leaves the decision 'based solely on automated processing' (p. 21). |

### S-220 · ¶4
> The right states no timing, and many hotel decisions may fall within that contractual exception (art. 22(2)(a)).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-220.1 | The right to human intervention states no timing | Legal proposition | Regulation (EU) 2016/679, arts 22(3), 12(3) | "The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request. That period may be extended by two further months where necessary" (art. 12(3)) | 5 (a condition in the same Regulation) | partial | minor | True of art. 22(3). The Regulation does set an outer limit for the controller's answer to a request under Article 22, and the guidance confirms it applies ('obligations under Articles 15 – 22 in the timescales provided for by the GDPR', WP251 p. 31 n. 52). Citing art. 12(3) makes the paper's point exact: the law allows a month. |
| S-220.2 | Many hotel decisions may fall within the contract exception | Own inference | WP251rev.01, p. 23, on the condition | "The controller must be able to show that this type of processing is necessary, taking into account whether a less privacy-intrusive method could be adopted. If other effective and less intrusive means to achieve the same goal exist, then it would not be 'necessary'." | — | valid with added premise | material | The paper's reading, hedged by 'may'. Added premises: the decision is within art. 22(1) at all, and solely automated processing is 'necessary' in the guidance's narrow sense. A staffed hotel has a less intrusive means to hand, a person, so 'many' is doubtful. S-221 rests on this row. |

- **S-220.2.** P1 (sourced): art. 22(2)(a) lifts the prohibition where the decision is necessary for entering into or performing a contract with the data subject. P2 (assumption): hotel decisions on bookings, check-in and price are solely automated and have legal or similarly significant effects. P3 (assumption): no less intrusive means would serve. C: many may fall within the exception. Counter-model: a hotel with a staffed desk; P3 fails. The guidance's own example of necessity is a recruiter with 'tens of thousands of applications' (p. 23). K claim: none.

### S-221 · ¶4
> The law can therefore be satisfied by a later review rather than a person at the threshold.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-221.1 | The law can be satisfied by a later review and does not require a person at the moment of decision | Own inference | WP251rev.01, p. 32 (good-practice annex), for the reading; Directive (EU) 2015/2302, art. 7(2)(d), against 'the law' | "a mechanism for human intervention in defined cases, for example providing a link to an appeals process at the point the automated decision is delivered to the data subject, with agreed timescales for the review and a named contact point for any queries" (WP251, p. 32) | 2, 5 | valid with added premise | material | The reading is the paper's, not the text's: art. 22(3) is silent. The guidance supports it (a 'review'; an appeal offered when the decision is delivered; 'contact details … to request that any declined decision is reconsidered', p. 26), and so does art. 12(3). It holds of Article 22 inside the two exceptions. It does not hold of 'the law'. Write 'Article 22 can therefore be satisfied'. |

- P1 (sourced, S-218.2). P2 (sourced in part, S-220.1). P3 (assumption, S-220.2). C: the law can be satisfied by a later review.
- Counter-model 1: outside art. 22(2), no review cures the decision; it is forbidden (WP251, p. 34: the active right 'only applies in those cases, because carrying out the processing described in Article 22(1) on other bases is prohibited').
- Counter-model 2, from the library: EU package-travel law, which covers accommodation sold in a package, requires in the contract the details of 'a contact point or of another service which enables the traveller to contact the organiser quickly and communicate with him efficiently, to request assistance when the traveller is in difficulty or to complain about any lack of conformity perceived during the performance of the package' (Directive (EU) 2015/2302, art. 7(2)(d)), and assistance 'without undue delay' (art. 16). That is a reachable party during performance, required by law. I did not read the 2026 amending directive saved beside it.
- Terms: 'the law' shifts from Article 22 (the premises) to law at large (the conclusion).
- K claim: K7. This row is where K7's 'confirms' and 'refutes' lists meet: data-protection law points to later review, package-travel law to a contact point in time.

### S-222 · ¶4
> The framework explains most where the guest is on site and the decision is high in stakes and hard to undo.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-222.1 | The framework has most explanatory force where the guest is on site and the decision is high in stakes and hard to undo | Own inference | — | — | — | equivocal | minor | 'Explains' has no object. The paper says its test 'measures neither satisfaction nor harm' (S-179) and that its cases 'illustrate the distinctions rather than test them' (S-153), so it has explained no outcome. Read as 'asks most', the sentence restates S-208. |

- P1 (earlier inference, S-208.1): a reachable person in advance is needed where the effect falls on the guest during the stay and cannot be undone in time. P2 (assumption): 'explains most' means 'makes its strongest demand'. C: as the sentence. With P2 the inference is valid and adds nothing to S-208.
- Counter-model for a monotonic reading: at the extreme of stakes and speed (decisions 'too fast for any person') the framework stops asking for a person and asks for limits set in advance. 'Most' does not rise with stakes throughout.
- Terms: 'the framework' is not defined in the section; it could be the role account, the test or Table 1.
- K claim: K7, K9.

### S-223 · ¶4
> It explains less where decisions are remote and reversible.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-223.1 | The framework has less force where decisions are remote and reversible | Own inference | — | — | — | equivocal | material | 'Remote' has two senses and the sentence is true in one only. See the list. |

- P1 (S-209.1): a reversible decision needs only an appeal. P2 (earlier inference, S-075, K9): the obligation comes into force when a traveller presents, so a decision taken before arrival precedes it. C: the framework asks less of remote, reversible decisions.
- Terms. *Remote* (a): the guest is not on site. Then C follows, and understates: by S-075 the role obligation is not yet in force, so the framework does not reach these decisions unless the booking contract carries a duty (K4). *Remote* (b): the party that decides is distant from the guest. That is the paper's subject (S-007: each technology 'places the party who decides at a distance from the guest it affects'), and in that sense the sentence denies the thesis.
- Consequence for the paper's cases: the first worked case, hotel pricing (S-190 to S-192), is remote and reversible. The case chosen to show 'the questions at work' lies where the framework is said to explain less.
- Undergeneration: remote and irreversible (a booking cancelled on the day of arrival); on site with a remote decider (a rental's door code that fails at night, S-195).
- K claim: K9.

### S-224 · ¶4
> It reaches its edge at the line between commercial and household hosting, where United States public accommodation law exempts an establishment with 'not more than five rooms for rent or hire' that is 'actually occupied by the proprietor of such establishment as his residence' (Civil Rights Act 1964, § 2000a(b)(1)).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-224.1 | The framework stops applying at the line between commercial and household hosting | Own inference | — | — | — | valid with added premise | minor | Added premise: a household host does not hold out to travellers at large. In the paper's own English source the edge is drawn by holding out, with no test of size or residence: a hotel is 'an establishment held out by the proprietor as offering food, drink and, if so required, sleeping accommodation, without special contract, to any traveller presenting himself' (Hotel Proprietors Act 1956, s. 1(3)). K claim: K3. |
| S-224.2 | United States public accommodation law exempts an establishment with not more than five rooms that its proprietor occupies as a residence | Legal proposition | 42 U.S.C. § 2000a(a), (b)(1) (Pub. L. 88-352, title II, § 201); LII text and govinfo, U.S. Code 2024 edition | "any inn, hotel, motel, or other establishment which provides lodging to transient guests, other than an establishment located within a building which contains not more than five rooms for rent or hire and which is actually occupied by the proprietor of such establishment as his residence" | 5, 3 | partial | minor | Three points. The five rooms and the occupation belong to the building, not the establishment. The carve-out is from the definition of a 'place of public accommodation' in one federal statute that forbids discrimination 'on the ground of race, color, religion, or national origin' (§ 2000a(a)); it is not an exemption from a duty to receive travellers. 'United States … law' is wider than Title II: the ADA has the same carve-out (42 U.S.C. § 12181(7)(A); saved), and state laws were not checked. Later treatment and case law: not checked. |
| S-224.3 | The two quoted phrases | Quotation | same, § 2000a(b)(1) | (as above) | none | supported | — | Words exact in both copies. |
| S-224.4 | The statutory carve-out marks the line between commercial and household hosting | Paraphrase (application) | § 2000a, read in full; Di Domenico and Lynch (2007: 322) | "there is a diverse range of owner-occupied small businesses providing accommodation where the private home dimension is significant, including bed and breakfasts, farm tourism, home stays, guesthouses, small hotels and self-catering cottages" (Di Domenico and Lynch) | 7 | not in source | material | The statute says nothing of households. The exempt establishment lets rooms 'for rent or hire' and takes 'transient guests', so it is commercial; the paper's own source calls such places businesses. Describe the line as the statute draws it (small, owner-occupied), or use the 1956 Act's test. |

### S-225 · ¶4
> A short-term rental in a host's own home can fall on the household side of that line.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-225.1 | A short-term rental in the host's own home can fall within the carve-out | Own inference | 42 U.S.C. § 2000a(b)(1) (quoted at S-224.2) | — | — | valid with added premise | minor | 'Can' is right. Added premises: the building holds no more than five rooms for rent, and the host lives in it. The sentence inherits 'household' from S-224.4. I read no case on whether Title II reaches platform rentals; none is in the library. K claim: K3 (the 'selective rental host'). |

### S-226 · ¶4
> There the role obligation we describe is at its weakest.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-226.1 | In a short-term rental in the host's own home the role obligation is at its weakest | Own inference | — | — | — | equivocal | material | 'Role obligation' means the duty to admit in the premise and the whole bundle in the conclusion. The conclusion also collides with S-092 and S-104. See the list. |

- P1 (sourced, S-224.2): one federal statute leaves small owner-occupied lodgings outside its equal-access rule. P2 (earlier inference, K3, K4): the law imposes the host's duties on whoever takes up the role by holding out. P3 (assumption): what that statute leaves out, the role obligation leaves out. C: the obligation is weakest there.
- Counter-model: a four-room, owner-occupied inn in England held out to any traveller is a hotel under the 1956 Act, with every duty of an innkeeper. P1 and P2 hold; C is false.
- Terms. *Role obligation*: in P1, a duty not to refuse on four listed grounds; in C, the duties 'to receive, to sustain, to protect and to attend' (S-065). The premise reaches the first only. Nothing shows the duties owed to a guest once received (care for safety, the contract) to be weaker in a home.
- Against the paper's own text: S-092 names 'the owner of a small commercial home' first among holders of the role, and S-104 says the single host, in whom obligation, authority and accountability 'sit together', 'fits the owner of a small commercial home'. On the paper's central concern, the path to someone with authority, the owner-occupied home is the strongest case, not the weakest.
- K3's grounds come apart here and point the other way on one: dependence is greatest for a guest inside the host's own home.
- Overgeneration: the argument would make the obligation 'weakest' in any establishment a discrimination statute exempts, for instance a private club (§ 2000a(e)).
- K claim: K3, K4 (the admission tier).

---

## Closing lists

### 1. Counts by verdict (71 rows)

| Verdict | Rows |
|---|---|
| supported | 8 |
| supported (abstract only) | 2 |
| partial | 11 |
| not in source | 1 |
| contradicted (by Table 1) | 1 |
| unverifiable | 5 |
| valid | 7 |
| valid with added premise | 22 |
| equivocal | 10 |
| undergenerates | 3 |
| overgenerates, invalid | 0 |
| signpost (no verdict) | 1 |

Severity, for the 55 rows that are neither `supported`, `valid` nor a signpost: fatal 0, material 18, minor 37. No row is fatal, on one condition: S-208.1 is material if the paper presents the criterion as its own proposal, and would be fatal if the paper insisted that the source's distinction yields it.

### 2. The fifteen rows that most endanger the paper

1. **S-208.1** The timing criterion needs K7's P3, which v6 never states, and its consequent ('before it takes effect') does not match its antecedent ('before the harm lands').
2. **S-207.1** The boundary is credited to a taxonomy its authors call 'primarily descriptive'; reversibility, harm, the guest and reachability are all the paper's additions.
3. **S-209.1** 'A reachable appeal' stands where the source's asynchronous review stands, and that review does not touch the decision already made.
4. **S-221.1** 'The law' can be satisfied by a later review only if the law is Article 22 inside its exceptions; package-travel law in the library requires a contact point the traveller can reach quickly.
5. **S-226.1** The role obligation is called weakest in the owner-occupied home, which S-092 and S-104 treat as a holder of the role and the fit case of the single host.
6. **S-224.4** The statute's carve-out is not a line between commercial and household hosting; the exempt establishment rents rooms.
7. **T1.r1.c3** 'No' for admission contradicts S-212 ('some') and the rebooked guest in Xiang et al.
8. **S-217.1** Outside the exceptions Article 22 forbids the decision, so the law there is stricter than the boundary; below the threshold it sets no floor; and it is EU law only.
9. **S-220.2** 'Many hotel decisions' within the contract exception: the guidance reads 'necessary' narrowly, and a staffed hotel has a less intrusive means.
10. **S-215.1** 'Our own reading of the sources cited': 23 of 28 cells rest on no source, and two of the other five on sources cited elsewhere.
11. **T1.r5.c4** (with **S-214.3**) The pricing row gives no reachable person even where a price bars access; the prose says it does.
12. **S-208.2** The class is defined 'during the stay', and the table's first row and its pricing row are settled before one.
13. **S-215.2** 'The nearest hospitality study' is a superlative without a logged search; guest-side experiments exist.
14. **T1.r2.c4** Limits 'set in advance by the host', where S-175 says the vendor often holds the rule.
15. **S-223.1** 'Remote' in one of its senses names the paper's own subject.

### 3. Sources I could not read in full, and the rows that wait

| Source | What I reached | Rows that wait |
|---|---|---|
| Ivanov and Webster (2024), doi 10.1016/j.techsoc.2023.102430 | Abstract (OpenAlex record). Publisher page 403 and bot page; no repository copy. CC BY, so a person can download it. | S-215.3, S-215.4, S-210.2; it could also supply a sourced list of decisions for the first column of Table 1 |
| Tang et al. (2018), doi 10.1108/jsm-04-2017-0126 | Abstract (saved OpenAlex record) | T1.r6.c3, T1.r6.c4 |
| Boo and Chua (2022); Hewagama et al. (2019); Huang and Lo (2025) | Not opened; the cards record abstract depth | T1.r3.c3; T1.r6.c3; S-215.2 |
| Garcia et al. | CESifo working paper 10849, pp. 2 and 10 only; not the *Management Science* version in the reference list | T1.r5.c2 |
| Xiang et al. (2022); Sandoval-Strausz (2005); Wilson-Nash et al. (2026); Di Domenico and Lynch (2007) | The passages quoted, read in their paragraphs; not the whole text | T1.r1.c2 to c4, T1.r2.c3, T1.r3.c4, S-224.4 |
| Regulation (EU) 2016/679; Directive (EU) 2015/2302; Equality Act 2010; C-634/21 | The provisions and paragraphs cited. Not read: GDPR corrigenda, the 2026 directive amending 2015/2302, CJEU cases after *SCHUFA* | S-217.1, S-218.1, S-220.1, S-221.1 |
| State public-accommodation laws and case law on § 2000a(b)(1) | Not searched | S-224.2, S-225.1 |

### 4. Gap claims, and the queries I ran

**S-215.2, 'the nearest hospitality study'.** All searches on 11 Nov 2026.

- Library (`grep -il` over `library/cards/*.md`, held and rejected cards included): 'human-in-the-loop' or 'on-the-loop' (3 cards: baum2026constitutive, ivanov2024automated, martinwaldman2022legitimate); 'recourse' (3, none on typology); 'which decisions' or 'typology of decisions' (2, neither in hospitality); 'robot … failure' or 'human intervention' (5, among them huanglo2025failure, a hotel experiment on human against robot agents in service failures, carded at abstract depth); 'overbook', 'lock-out', 'unstaffed' (0); 'reversib' (3, none a study of hotels).
- Consensus, three queries, 20 results each: 'which hotel decisions require human intervention versus automation: typology of hospitality decisions by stakes and reversibility for guests'; 'hotel service robot or AI failure: when do guests need human employee intervention, escalation or recovery'; 'human-in-the-loop human-on-the-loop decision-making tourism hospitality framework which decisions to automate'.
- OpenAlex (`/works?search=`): 'hotel guest contest automated decision human review appeal' (647 results, none on point in the first 12); 'hospitality contestability algorithmic decision guest recourse' (82, none on point in the first 12); 'hotel decisions human-in-the-loop reversibility stakes typology guest' (2, neither relevant).
- Result. I found no work that sorts hospitality decisions by the recourse a guest needs, in those sources with those queries. I found work nearer than a survey of managers on the guest's side of the question: Huang and Lo (2025), already carded, and three records under list 5 (Liu et al.; Liu and Wang; Choi et al.), each confirmed in Crossref and read at abstract depth only. Search summaries are leads, not sources.

No other sentence in the batch makes a gap claim. S-220.1 ('the right states no timing') is a claim about a text and is checked at its row.

### 5. Sources to drop, and leads to replace them

**Drop or re-scope.**

- *Civil Rights Act 1964, § 2000a(b)(1)*, as the marker of 'the line between commercial and household hosting' (S-224 to S-226). The statute draws another line. Replacement already in the reference list: Hotel Proprietors Act 1956, s. 1(3), whose test is holding out 'without special contract … to any traveller'.
- *Baum and Laux (2026)*: keep for the timing test (p. 120) and the three modes; do not cite for the boundary or for the 'later appeal'.
- *Ivanov and Webster (2024)*: keep only after a full read; at abstract depth it cannot carry 'nearest'.

**Leads, each from a record or text fetched or opened this session.**

- Regulation (EU) 2016/679, art. 12(3): the one-month limit on the controller's answer to an Article 22 request (saved text; read).
- WP251rev.01, p. 21 (a clerk without influence leaves the decision solely automated), p. 26 and p. 32 (the regulators picture reconsideration after delivery, with 'agreed timescales' and 'a named contact point'), p. 34 (the active right exists only inside the exceptions) (saved; read).
- CJEU, C-634/21 *SCHUFA*, paras 52–54 (saved; paragraphs read).
- Directive (EU) 2015/2302, arts 7(2)(d), 13, 15, 16: a contact point the traveller can reach quickly, and assistance without undue delay, for packages that include accommodation (saved; articles read). It bears on K7 as law that enacts the conclusion, in a neighbouring setting.
- Equality Act 2010, ss 20(3)–(5), 29(7)(a): a duty of adjustment owed by service-providers, for Table 1's room row and for K4 (saved; read).
- Directive 2011/83/EU, art. 6(1)(ea), as inserted by Directive (EU) 2019/2161: disclosure that a price was personalised by automated decision-making, for Table 1's pricing row (saved; the inserted point read).
- Data (Use and Access) Act 2025, s. 80 (UK GDPR arts 22A–22D), which lets regulations say 'how and when' the safeguards must work (saved; passages read).
- Xiang et al. (2022), already in the reference list: the rebooked guest, for Table 1's admission row.
- Liu, Zhang, Li and Wu (2026), 'Are human employees still needed? …', *Journal of Consumer Behaviour*, doi 10.1002/cb.70226 (Crossref record; abstract only): four experiments in unmanned smart hotels on severity of failure and who apologises.
- Liu and Wang (2025), 'Can service robots recover themselves? …', *International Journal of Hospitality Management* 124, 103951, doi 10.1016/j.ijhm.2024.103951 (Crossref record; abstract only).
- Choi, Mattila and Bolton, 'To err is human(-oid) …', *Journal of Service Research* 24:3, pp. 354–371, doi 10.1177/1094670520978798 (Crossref record, online 16 Dec 2020; abstract only): human intervention after an inadequate recovery by a robot.
- Ivanov, 'Automated decision-making', *foresight* 25:1, pp. 4–19, doi 10.1108/fs-09-2021-0183 (Crossref record, online 18 Apr 2022; abstract only): sorts decisions by speed, frequency and 'low negative consequences of a wrong decision', which is close to the table's stakes column.
- Haynes and Egan, 'Transient price setting in the era of automated systems …', *Journal of Revenue and Pricing Management* 23:1, pp. 28–38, doi 10.1057/s41272-023-00447-5 (Crossref record, online 7 Nov 2023; abstract only): twenty managers; the general manager keeps control of price. For the pricing row.

Crossref gave the online dates above and no print year for these three; fix the year of each from the issue before citing.
