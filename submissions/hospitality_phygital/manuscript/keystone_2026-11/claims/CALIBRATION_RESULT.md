<!-- Calibration run of the claim audit, written by a Claude (Fable 5.2) subagent on 11 Nov 2026. -->

# Calibration result: claim audit of X-01 to X-24

**Scope.** I audited the 24 sentences in `CALIBRATION_SET.md` against the saved texts named for them and against nothing else. I opened no library card, nothing under `rewrite_2026-11/` or `reviews/`, neither `DECISIONS_K.md` nor `LEADS.md`, not `DRAFT_v6.md`, not `CLAIMS_FIXED.md`, and no git history. I did not use the web.

**How to read the tables.**

- Classes are the brief's eight: 1 Population, 2 Setting, 3 Strength, 4 Speaker, 5 Scope, 6 Design, 7 Application, 8 Version.
- Passages come from the saved text. I rejoined words hyphenated at line ends, expanded ligatures and normalised apostrophes; bracketed numbers are the source's footnote marks; an ellipsis marks a cut. Nothing else is changed.
- The brief has no verdict for a proposition that a readable source neither states nor denies. I record it as `partial (no passage)`, name the class that fails, and give the nearest text, marked 'nearest'.
- 'Advisory' under 'Classes failed' means the classes are clean but a second reader should know of a risk.
- The K column is empty throughout: K1–K9 sit in a file outside this test's limits. For the same reason I could not resolve terms that point outside a sentence ('that article', 'such arrangers', 'the first three questions', 'the touchpoint passes'), and an own inference whose premises lie outside the set is marked `not tested`.
- Every legal row carries 'later treatment: not checked'; the web was closed.
- Sentence verdicts in the summary: `sound` when every sourced row is `supported`; `faulted` when any sourced row is `partial` or `contradicted`; `unverifiable` when no sourced row could be checked.
- How much of each text I read is stated near the end, under 'Reading coverage'.

---

### X-01
> The UK Supreme Court put the structure plainly in Woodland: the work required to perform certain duties 'may well be delegable, and usually is. But the duty itself remains the defendant's' (2013: para 7).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-01.1 | Woodland is a decision of the UK Supreme Court | Legal proposition | *Woodland v Essex County Council* [2013] UKSC 66, saved judgment text, title page and p. 2 | "[2013] UKSC 66 On appeal from: [2012] EWCA Civ 239 … LORD SUMPTION: (with whom Lord Clarke, Lord Wilson and Lord Toulson agree)" | none | supported | | None. Court: UKSC, on appeal from the Court of Appeal of England and Wales. Lady Hale concurs (para 28: 'the judgment of Lord Sumption, with which of course I agree'), so the passage speaks for the whole court. |
| X-01.2 | The quoted words | Quotation | same, para 7 (printed p. 4) | "The work required to perform such a duty may well be delegable, and usually is. But the duty itself remains the defendant's. Its delegation makes no difference to his legal responsibility for the proper performance of a duty which is in law his own." | none | supported | | None. Words exact; speaker Lord Sumption; paragraph number confirmed. |
| X-01.3 | The work of performing certain duties can be delegated while the duty stays with the defendant | Legal proposition | same, paras 7 and 23 | "It comprises cases where the common law imposes a duty upon the defendant which has three critical characteristics. First, it arises not from the negligent character of the act itself but because of an antecedent relationship between the defendant and the claimant." | none | supported | | None. 'Certain duties' carries the condition: 'such a duty' is the second category of non-delegable duty (three characteristics, para 7; five defining features, para 23). A statement of principle in the leading judgment, applied to reach the holding. Later treatment: not checked. |

### X-02
> Neither guest nor staff could anticipate the operative rule and no one at the desk could explain the price, so the touchpoint fails on predictability and on accountability, although its legal weight is moderate unless the price bars a guest from the service (Article 29 Working Party 2018: 22).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-02.1 | Neither guest nor staff could anticipate the operative rule | Case description | Garcia, Tolvanen and Wagner, CESifo Working Paper 10849 (Dec 2023; 'accepted for publication in Management Science'), pp. 2, 10 | nearest: "The hotel manager decides every day whether to use the revenue management system to update prices. If she logs into the system, the dashboard displays for each room the current recommended price and the actual price. She then decides which price to update and by how much." (p. 10) | 7; 1 (the study has managers only; no guest and no desk staff appear) | partial (no passage) | | The scenario is the paper's own. For staff the text points the other way: the algorithm advises 'human managers who retain the final decision right' (p. 2). Present the scenario as the paper's, or find a source that observed a desk. |
| X-02.2 | No one at the desk could explain the price | Case description | same, p. 10 | nearest: "According to private communication with the revenue management service, hotels are family-run and thus managing prices takes only a small fraction of a hotel manager's weekly workload." | 7 | partial (no passage) | | As above. In the nine hotels studied a manager of a family-run house set each price. |
| X-02.3 | so the touchpoint fails on predictability and on accountability | Own inference | — | — | — | valid with added premise; unsound as it stands | | See the list below. |
| X-02.4 | Its legal weight is moderate unless the price bars a guest from the service | Legal proposition | Article 29 Working Party, Guidelines on Automated individual decision-making and Profiling, WP251rev.01 (revised 6 Feb 2018), p. 22; read at the path named for X-24 | "Automated decision-making that results in differential pricing based on personal data or personal characteristics could also have a significant effect if, for example, prohibitively high prices effectively bar someone from certain goods or services." | 3 ('could also … if, for example' becomes 'unless'); 5 (the passage covers solely automated decisions and pricing on personal data; in Garcia a manager sets 'an index price' for a room and date, p. 9); 7 ('moderate' is the paper's grading) | partial | | Printed p. 22 confirmed. Body: 'an independent European advisory body' (title page), not a court; guidance on Article 22 GDPR, not binding. State the two conditions, or take the citation off the grading. The citation sits where a reader takes it to cover the whole sentence; WP29 says nothing of hotels or desks. |

- **X-02.3.** P1 = X-02.1 (assumption). P2 = X-02.2 (assumption). P3, P4 = the test's definitions of predictability and accountability (stipulations, outside this set). C: the touchpoint fails on both.
- Counter-model: a family-run hotel where the manager who accepted or changed the recommended price stands at the desk. P3 and P4 hold and C is false. That is the setting Garcia describes.
- Quantifiers: 'neither' and 'no one' are universal; nothing sourced supports them.
- Overgeneration, undergeneration, K: not tested (outside the set).
- Verdict: valid with added premise (P3, P4); unsound as it stands, because P1 and P2 are assumptions.

### X-03
> The translation is fragile, because when a system quietly revises its rules the knowledge it rests on loses its value overnight and no one tells the employee or the guest (Hatherley 2025).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-03.1 | The translation is fragile | Own inference | — | — | — | valid with added premise | | See the list below. |
| X-03.2 | When a system quietly revises its rules, the knowledge the translation rests on loses its value overnight | Paraphrase | Hatherley, Ethics and Information Technology 27:20 (2025), pp. 1, 5, 7 of 14 | "Once the model is updated, however, these expectations may be undermined, and the user's mental model may become outdated." (p. 7) | 1 (expert users of decision-support models; the doctor is the running case); 2 ('healthcare, finance, and warfare', p. 1); 3 ('may … may' becomes 'loses … overnight', and p. 5 adds that team performance 'eventually returns to its pre-update levels'); 5 (retrained ML models, not 'rules'; 'quietly' has no counterpart); 6 (conceptual argument resting on one cited experiment, Bansal et al. 2019) | partial | | Restore the hedge, name the setting, and say that the step to hotel staff is the paper's. |
| X-03.3 | No one tells the employee or the guest | Paraphrase | same, pp. 9, 10 of 14 | nearest: "Developers often neglect to revise their documentation as models are updated over time (Wang et al., 2022), and even where such documentation is updated, the revisions may not be detailed enough" (p. 9) | 7; 1 (no employee and no guest; nothing on whether people subject to the decisions are told) | partial (no passage) | | Hatherley's problem is that users cannot understand why an update changed the outputs, not that nobody announces it. He lists 'dynamic model reporting, in which users are informed about changes' (p. 10) as a possible remedy. Mark the clause as the paper's own. |

- **X-03.1.** P1 = X-03.2. P2 = X-03.3. P3 (assumption): hospitality systems are updated as Hatherley's models are, and staff knowledge of them is a mental model in his sense. C: the translation is fragile.
- Counter-model: a rule engine whose changes are announced to staff. P1 can hold of ML models and C fail.
- Terms: 'translation' is the paper's term; its sense is fixed outside this set.
- Overgeneration: the argument covers any staffed service that runs updated software (a bank, an airline). Whether the paper concedes this I could not check.
- Verdict: valid with added premise (P3).

### X-04
> In the classical law of hospitality the host commands: 'It is always the host who ordains, the guest who complies' (Pitt-Rivers 2012: 513).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-04.1 | The quoted words | Quotation | Pitt-Rivers, 'The law of hospitality', HAU 2(1): 501–517 (2012 reprint of the 1977 text), p. 513 | "But this reciprocity does not obscure the distinction between the roles. It is always the host who ordains, the guest who complies. The guest must be granted the place of precedence and he must eat first, but precedence is defined in relation to the host" | none | supported | | None. Words exact; speaker Pitt-Rivers; page confirmed from the running head. The sentences around it (mutual honour, then the roles) leave the meaning intact. |
| X-04.2 | In the classical law of hospitality the host commands | Paraphrase | same, pp. 513, 515 | "it is the host's privilege to ordain" (p. 515) | none; advisory: 'classical' is the paper's label. Pitt-Rivers writes of 'the law of hospitality in the abstract' and a 'natural law' of hospitality (p. 515) | supported | | None needed. Reword if 'classical' could be read as 'of classical antiquity'. |

### X-05
> Guests, Shryock writes, 'depend on their hosts for protection and respect' (2012: S23).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-05.1 | Guests 'depend on their hosts for protection and respect' | Quotation | Shryock, 'Breaking hospitality apart', Journal of the Royal Anthropological Institute (N.S.) S20–S33 (2012), p. S23 | "'The guest', Jordanians tell me, 'is prisoner of the host'. Visitors are treated well, but their mobility is limited. They cannot move freely about the house or help themselves to food and drink; they depend on their hosts for protection and respect." | none; advisory on 2: the quoted sentence describes visitors in Jordanian (Balga Bedouin) houses | supported | | Words exact; speaker Shryock in his own voice, glossing a Jordanian proverb; page confirmed from the page marker and running head. Shryock extends the point himself ('Like any guest, I was a prisoner of my hosts', p. S24), so I pass class 2. 'Among the Balga Bedouin' would remove the risk. |

### X-06
> The deploying organization is best placed to reverse a decision (Lyons et al. 2021), algorithmic governance in services calls for routes of escalation and human oversight (Shabnam et al. 2026), and of five governance mechanisms only appeal raised the perceived legitimacy of an adverse algorithmic decision (Martin and Waldman 2023).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-06.1 | The deploying organization is best placed to reverse a decision | Paraphrase | Lyons, Velloso and Miller, arXiv:2103.01774v1 (preprint of Proc. ACM HCI 5, CSCW1, art. 106), p. 12, §5.1.4 | "Internal review processes are seen as practical because the entity deploying a system is likely to be in the best position to reverse that decision or provide redress." | 4 (the view of those who sent submissions to Australia's AI Ethics Framework consultation, reported by the authors); 3 ('is likely to be' becomes 'is'); 6 (thematic analysis of 65 submissions) | partial | | Attribute and hedge: submissions to the Australian consultation saw the deployer as likely to be best placed. I read the arXiv preprint; no page is cited. |
| X-06.2 | Algorithmic governance in services calls for routes of escalation and human oversight | Paraphrase | Shabnam et al., Journal of Services Marketing (EarlyCite, accepted 13 May 2026, DOI 10.1108/JSM-09-2025-0679), §7.2, unpaginated | "Secondly, algorithmic governance must remain contestable. Digitally enforced rules should incorporate escalation pathways and human oversight to prevent rigid exclusion." | none; advisory: a managerial recommendation in a conceptual paper on phygital services, which 'calls for' renders fairly | supported | | None. |
| X-06.3 | Of five governance mechanisms only appeal raised the perceived legitimacy of an adverse algorithmic decision | Empirical generalization | Martin and Waldman, Journal of Business Ethics 183: 653–670 (2023; online 10 Feb 2022), HTML full text, sections 'Governance', 'Outcomes and Governance', 'Discussion' | "The only form of procedural governance that carries a legitimacy dividend is the most robust that we studied: a formal appeal to a human decision maker." | none; advisory on 6 and 1: factorial vignette surveys of U.S. respondents on Amazon Mechanical Turk, who rated hypothetical decisions about third persons | supported | | The five are notice, impact assessment, audit, human in the loop and appeal. For bad outcomes 'the use of an appeal process does provide a legitimacy dividend (t = − 12.53; p < 0.0001)'; the dividend 'did not 'make up' for the penalty of the bad outcome'. Adding 'in a vignette study' would state the design. |

### X-07
> and hotels ask guests to leave who will not follow the stay's rules after repeated communications (Xiang et al. 2022)

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-07.1 | Hotels ask guests to leave who will not follow the stay's rules after repeated communications | Empirical generalization | Xiang, Huang, Gao and Lai, Annals of Tourism Research, art. 103376 (2022), PubMed Central full text, unpaginated; section 'Performance pathways: managing ritual violations' | "Only when guests do not abide by the ritual after repeated communications will they be asked to leave the hotel." | 2 and 6 ('Data was collected from an upscale hotel in a city in southeastern China', during COVID-19); 5 (the 'ritual' is government-mandated COVID-19 prevention: real-name registration, health codes, travel history; not 'the stay's rules'); 3 ('Only when … will' marks a last resort; the sentence makes it a general practice of 'hotels') | partial | | The authors limit the claim themselves: the findings 'might not be generalizable to other countries' and 'might not apply to midscale and economy hotels'. Name the case and keep 'only'. |

### X-08
> The second is a real alternative: digital captivity is 'coerced participation in systems that have become unavoidable' (Wilson-Nash et al. 2026: 976), an analogue route that is kept but downgraded is one of its triggers rather than a remedy (2026: 978), and letting consumers 'choose modes of access' is one way to prevent it (2026: 981).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-08.0 | The second is a real alternative | Own inference | — | — | — | valid | | See the list below. |
| X-08.1 | Digital captivity is 'coerced participation in systems that have become unavoidable' | Quotation | Wilson-Nash et al., Psychology & Marketing 43: 974–985 (2026), p. 976 | "Where digital exclusion typically captures non-access and unengagement reflects withdrawal or resistance, DTC centers on coerced participation in systems that have become unavoidable." | none; advisory: the source says 'centers on', not 'is' | supported | | None. Words exact (split across a line in the saved text); page confirmed from the footer. |
| X-08.2 | An analogue route that is kept but downgraded is one of its triggers rather than a remedy | Paraphrase | same, p. 978 | "CP1: DTC is initially triggered by changes in service access, such as when substitution, co-existence, liquid digital, or digital-only formats are introduced." Co-existence is glossed on the same page as "analogue retained but downgraded and more difficult to access". | none; advisory: 'rather than a remedy' is the paper's contrast, entailed by the trigger status and not stated; CP1 is a conceptual proposition ('we propose') | supported | | None needed. 'Wilson-Nash et al. propose' would mark the design. |
| X-08.3 | Letting consumers 'choose modes of access' is one way to prevent it | Quotation | same, p. 981 | "preserving autonomy, even in minor ways, can prevent DTC and then maladaptive coping strategies (e.g., neglect, distancing) by allowing consumers to choose modes of access (e.g., digital, analogue), control the pacing of adoption, and better understand the reasons for the change" | none; advisory on 6: the framework 'has yet to be empirically tested' (p. 981) | supported | | None. |

- **X-08.0.** P1–P3 = X-08.1 to X-08.3 (sourced). C: a kept-but-downgraded analogue route does not meet the requirement; the alternative must be real.
- Counter-model: none found. If a downgraded route triggers captivity (P2) and choice of mode prevents it (P3), the choice must lie among routes that are not downgraded.
- Terms: 'the second' points outside the set.
- Verdict: valid.

### X-09
> Baum and Laux distinguish forms of human involvement in automated systems by whether intervention can come before a decision takes effect, and what matters, they write, is 'not elapsed time but whether intervention can occur before the token output becomes effective' (2026: 120).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-09.1 | Baum and Laux distinguish forms of human involvement by whether intervention can come before a decision takes effect | Paraphrase | Baum and Laux, in Steffen (ed.), AISoLA 2026, LNCS 17146, pp. 115–130 (version of record), p. 120 | "Where periodic review occurs before outputs take effect (e.g., decisions released only after batch review), the configuration is, in our terms, synchronous with latency: the distinguishing feature is not elapsed time but whether intervention can occur before the token output becomes effective." | none; advisory on 5: this criterion separates synchronous from asynchronous on-the-loop involvement only. The taxonomy's first cut is causal: 'HITL is constitutive … while HOTL is corrective' (abstract, p. 115) | supported | | 'Among corrective forms of involvement' would state the scope. |
| X-09.2 | The quoted words | Quotation | same, p. 120 | as above | none; 8 to check: the version of record carries '© The Author(s) 2027' and 'LNCS 17146, pp. 115–130, 2027' | supported | | Words exact; speakers the authors; page confirmed from the running head. Check the year in the reference list against the 2027 imprint. |

### X-10
> When a restaurant projects an animated chef onto the table while staff go on hosting the meal, the technology adds to an encounter whose rules stay steady and whose staff keep their discretion (Batat 2021), and the touchpoint passes.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-10.1 | A restaurant projects an animated chef onto the table | Case description | Batat, Technological Forecasting & Social Change 172: 121013 (2021), p. 4 | "The video animation, created by using a motion capture process projected onto customers' tables, presents a "little chef" who cooks in front of diners' eyes and on their plates." | none | supported | | None. |
| X-10.2 | while staff go on hosting the meal | Case description | same, pp. 7, 8, 11 | "it was perceived as an ice-breaker activity that facilitated social interactions among customers dining with one another [sic] well as their interactions with other customers and staff." (p. 7) | none; advisory on 6: this rests on diners' recollections ('the service was customer oriented', P15, p. 8); the author 'did not follow and observe them in the restaurants' (p. 11) | supported | | None needed. |
| X-10.3 | The technology adds to the encounter | Paraphrase | same, p. 8 | "they were not totally disconnected from the real environment. Instead, they lived the dining experience in between real and virtual settings." | none | supported | | None. |
| X-10.4 | The encounter's rules stay steady | Case description | same, whole text searched; findings and discussion read | nearest: none. The text does not discuss the rules of the encounter; the word 'rule' does not occur. | 7 | partial (no passage) | | The paper's own characterization. Place the citation so that it covers only the projection and the diners' experience. |
| X-10.5 | The staff keep their discretion | Case description | same | nearest: none. 'Discretion' does not occur; the study interviewed 20 diners and 15 restaurateurs and no serving staff. | 7; 1 | partial (no passage) | | As above. |
| X-10.6 | and the touchpoint passes | Own inference | — | — | — | valid with added premise; unsound as it stands | | See the list below. |

- **X-10.6.** P1 = X-10.4 (assumption). P2 = X-10.5 (assumption). P3 = the test's pass conditions (stipulation, outside this set). C: the touchpoint passes.
- Counter-model: a dinner run to a fixed script timed to the projection, where staff cannot vary the service. P3 holds and C fails. Batat gives no evidence either way.
- Verdict: valid with added premise (P3); unsound as it stands, because P1 and P2 are assumptions.

### X-11
> In a short-term rental with self-check-in the app may answer the first three questions well, yet when a code fails at night no one with authority may be reachable (Bosma 2022: 605).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-11.1 | Short-term rentals offer self-check-in, with no one met in person | Case description | Bosma, Environment and Planning A 54(4): 595–610 (2022), p. 605 | "the Host Assist program[13] allows smart lock providers and other companies to integrate their services on the Airbnb platform, allowing guests to enter their holiday apartments without meeting anyone in person. … Such changes help property owners to run an STR without having to be physically present, ultimately transforming hosting into ghosting." | none | supported | | None. Page confirmed. |
| X-11.2 | The app may answer the first three questions well | Own inference | — | — | — | not tested | | The 'first three questions' are defined outside this set. Bosma says nothing on what the app tells a guest. |
| X-11.3 | When a code fails at night no one with authority may be reachable | Case description | same, whole text searched | nearest: the passage above. The text has no failed code, no night arrival and nothing on whether a guest can reach anyone. | 7; 1 (a study of Airbnb hosts in Berlin, not of guests) | partial (no passage) | | The paper's own scenario, hedged by 'may' but carried by Bosma's citation. Cite Bosma for the absent host only and mark the scenario as the paper's. |

### X-12
> Phygital arrangements multiply such arrangers, chiefly the vendors of systems that price, verify and allocate, and Cobbe et al. find that in such supply chains there is 'typically no one actor in overall control' (2023: 1192).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-12.1 | Phygital arrangements multiply such arrangers, chiefly the vendors of systems that price, verify and allocate | Own inference | — | — | — | not tested | | No source is cited and 'such arrangers' points outside this set. |
| X-12.2 | The quoted words | Quotation | Cobbe, Veale and Singh, arXiv:2304.14749v2 (22 May 2023; preprint of the FAccT '23 paper), p. 7, §4.1 | "Responsibility for the workings and outcomes of supply chains is thus distributed among several actors who may not be straightforward to identify nor consistent across instances. Even when some actors are influential, there is therefore typically no one actor in overall control of a supply chain." | none; 8 not confirmed: the saved text is the arXiv version, paged 1–13, and the words fall on its p. 7. I could not confirm '1192' | supported | | Words exact; 'typically' kept. Confirm 1192 against the proceedings. |
| X-12.3 | Cobbe et al. find this of such supply chains | Paraphrase | same, p. 1 (abstract) and p. 7 | "We argue that algorithmic accountability discussions must consider supply chains and the difficult implications they raise for the governance and accountability of algorithmic systems." | none; advisory on 6: the paper argues from analysis and reports no study, so 'find' overstates; advisory on 7: reading hospitality vendors as an algorithmic supply chain is the paper's step | supported | | 'Argue' or 'observe' for 'find'. |

### X-13
> The duty narrowed over time until it attached 'only to common carriers by land and water (including ferrymen) and innkeepers' (Burdick 1911: 523), while the shopkeeper remained free to refuse (Wyman 1904: 159).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-13.1 | The duty narrowed over time until it attached 'only to common carriers by land and water (including ferrymen) and innkeepers' | Quotation | Burdick 1911: 523. Named texts: `1110340.txt` (Part II, Columbia Law Review pp. 616–638) and `1110915.txt` (Part III, pp. 743–764) | none. Neither named text contains p. 523 or the words; 'ferrymen' occurs in neither. | — | unverifiable | | Part II, n. 1: 'The first part of this article … is to be found at page 514 of the present volume'. So p. 523 lies in Part I. A third file, `1110590.txt`, sits in the same folder and may be Part I; the set does not name it and I did not open it. That text would settle the row. |
| X-13.2 | The shopkeeper remained free to refuse | Paraphrase | Wyman 1904: 159. No text supplied. | none | — | unverifiable | | Wyman's article would settle it. Burdick's Parts II and III mention Wyman only to dispute his monopoly theory (Part II, p. 620; Part III, p. 764 n. 87) and say nothing of shopkeepers. A lead from a named text: Bogen (1996: 51 n. 3) cites the article as 17 Harv. L. Rev. 156 and dates it 1903; check the year. |

### X-14
> since guests prefer little disclosure at check-in and fuller explanation later in the stay (Pigac et al. 2026: 286)

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-14.1 | Guests prefer little disclosure at check-in | Empirical generalization | Pigac, Lee and Huang, Cornell Hospitality Quarterly 67(3): 283–297 (2026), pp. 286, 291 | p. 286: "Situational sensitivity: Varies in transparency based on the service stage. For example, minimal disclosure during check-in; richer, retrospective transparency in loyalty apps." p. 291: "At check-in, respondents preferred minimal interruption and trusted hotel staff to mediate technology." | 8 (p. 286 states a mechanism the framework proposes; the finding is on p. 291); 1 and 2 (50 luxury-hotel guests); 3 (preferences differ by segment: 'Digital Enthusiasts demanded opt-in personalization with full data traceability', p. 291); 6 (interviews) | partial | | Cite p. 291, say 'luxury-hotel guests interviewed', and keep the variation by segment. The authors note that the sample 'may limit generalizability to other regions or mid-market contexts' (p. 294). |
| X-14.2 | and fuller explanation later in the stay | Empirical generalization | same, pp. 286, 291 | "During in-room use, the desire for control increased. Post-stay feedback and loyalty apps were seen as appropriate venues for deeper algorithmic explanations." (p. 291) | 5 (the source puts deeper explanation after the stay, 'retrospective', in loyalty apps; during the stay guests wanted control); 8 | partial | | 'After the stay' is what the source says. One guest's 'Tell me later when I'm curious' (p. 291) fixes no time. |

### X-15
> Thompson's forms of directed duty, 'X has a duty to Y to do A' and 'X has a right against Y' (2004: 335), fix who owes what to whom without mentioning answering.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-15.1 | The two quoted forms | Quotation | Thompson, 'What is it to Wrong Someone? A Puzzle about Justice' (chapter 14; pp. 333–384 in the saved text), p. 335 | Table: "X has a duty to Y to do A … X has a right against Y —that he do A … —to do A". Then: "The propositions in the first row express forms of Aristotle's 'X adikei Y'; those in the last two rows express Hohfeldian 'claim' and 'privilege' respectively." | none | supported | | Words exact; page confirmed from the running head. The saved text does not show the year. |
| X-15.2 | These are Thompson's forms of directed duty, and they fix who owes what to whom | Paraphrase | same, pp. 334, 335, 344 | "These forms of judgement express what we might call forms of bipolar normativity, or forms of relation of right." (p. 335) "You 'owe' it to her not to kill her." (p. 334) | none; advisory: Thompson's word on p. 335 is 'bipolar'; he writes 'directed or bipolar duties and rights' on p. 344. The right-forms are claim and privilege, so 'forms of directed duty' is loose for the second quotation | supported | | None needed. |
| X-15.3 | They do so without mentioning answering | Own inference | same, p. 335 | — | — | valid | | See the list below. |

- **X-15.3.** P1 (sourced, p. 335): each tabulated form has places for two agents and an act. C: none has a place for answering.
- This is an observation of absence, and the table bears it out.
- Caution: Thompson ties the forms to complaint in private law. In recognizing grounds of complaint, institutions "implicitly generate a collection of directed or bipolar duties and rights. The violation of such a duty or right is the plaintiff's theme" (p. 344). The sentence is true of the forms; it should not be read as Thompson's view that directed duty stands apart from complaint.
- Terms: 'answering' has no counterpart in Thompson's text.
- Verdict: valid.

### X-16
> The innkeeper's duties were, in Maese's words, 'fixed by law rather than by contract' (2015: 501).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-16.1 | The innkeeper's duties were 'fixed by law rather than by contract' | Quotation | Maese, Texas A&M Journal of Property Law 2(3): 481 (2015; student article), p. 501 | "If the guest thus "presents himself" and is accepted, the relationship "is instantly established between them" and the rights and duties of both parties are at once fixed by law rather than by contract.[191]" | none; advisory on 4: the words are Maese's, the authority is Beale (n. 191: 'Id. at 75, 78–79'); advisory on 5: the source has 'the rights and duties of both parties', once the guest is accepted | supported | | Words exact; page confirmed from the running head. As a legal proposition the row rests on a student article reporting a treatise; no primary authority is in the set. The repository's suggested citation gives (2014), the running head 2015. |

### X-17
> Kong grounds that responsibility in the deployer's control over the act of delegating and concludes that 'one who elects a delegate that cannot answer thereby elects to answer for it' (2026: 4–5, 10).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-17.1 | Kong grounds that responsibility in the deployer's control over the act of delegating | Paraphrase | Kong, AI and Ethics 6:518 (2026), pp. 4–5 of 14 | "In the deployment case, the deployer's standing to answer for what an agent does is grounded in her guidance control over the act of delegation [12]" (p. 4). "the deployer's responsibility for a downstream outcome is derivative, traced back to an earlier exercise of guidance control — the act of delegation" (p. 5) | none; advisory on terms: Kong's claim is about answerability, which he separates from liability ('Answerability is not the same as liability for compensation', p. 10), and it covers 'foreseeable types of outcome' | supported | | None, if 'that responsibility' in the draft means answerability. |
| X-17.2 | The quoted words | Quotation | same, p. 10 of 14 | "concentrates answerability more firmly on the human who chose to delegate to a non-answerable process. One who elects a delegate that cannot answer thereby elects to answer for it." | none | supported | | Words exact (split across a line in the saved text). The sentence closes the reply to Objection 3, so 'concludes' is fair. Pages confirmed from the running heads. |

### X-18
> Facial-recognition systems verify identity at check-in (Xu et al. 2021), and service robots greet, direct and serve guests, who hold the firm responsible when the robots fail (Belanche et al. 2020).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-18.1 | Facial-recognition systems verify identity at check-in | Empirical generalization | Xu et al. 2021. No text supplied. | none | — | unverifiable | | The article would settle it. |
| X-18.2 | Service robots greet, direct and serve guests | Empirical generalization | Belanche, Casaló, Flavián and Schepers, Journal of Service Management 31(2): 267–289 (2020), pp. 273, 283 | "robots are starting to be implemented to attend customers at several hotels worldwide. For example, Connie is a robot concierge introduced by Hilton, able to inform guests about nearby places of interest or give information about the hotel." (p. 273) | 6 and 3: the robot that greets, directs and serves is the study's scenario, and "The scenarios extended the robots' abilities compared to the current market situation of these robots" (p. 283) | partial | | 'Are starting to' is the source's strength. |
| X-18.3 | Guests hold the firm responsible when the robots fail | Empirical generalization | same, pp. 267, 275 | "[the customer's attribution of the hotel's responsibility] is greater when the service is conducted by a robot (M = 4.35; S.D. = 0.90) than by an employee (M = 4.12; S.D. = 1.03). The difference is significant (F = 4.68; p < 0.05), hence supporting H2." (p. 275; the saved text prints '5' for '=') | 1 (U.S. survey participants, not guests); 6 ('Two vignette-based experimental studies', p. 267); 5 (the effect is a difference from the human-employee condition and is not tied to failure: 'the interaction effect between agent and service outcome is not significant toward attribution of responsibility to the firm so that H4b is not supported', p. 275) | partial | | State the design and the comparison: in vignette experiments respondents attributed more responsibility to the hotel when a robot rather than an employee served them. |

### X-19
> Discretion splits, because staff keep some freedom to act while more of their day goes to reading decisions made elsewhere and working around categories set elsewhere (Pedersen and Pors 2023; Spektor et al. 2025).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-19.1 | Discretion splits | Own inference | — | — | — | valid with added premise | | See the list below. |
| X-19.2 | Staff keep some freedom to act | Empirical generalization | Pedersen and Pors, Journal of Public Administration Research and Theory 33(1): 80–93 (2023), p. 80; Spektor et al., DIS '25, pp. 3221–3234 (HTML text without page breaks), §§4.2, 5.1 | Pedersen and Pors: "rather than eclipsing discretion, the technologies meant to standardize and optimize decision making in public service delivery introduce rough categorizations and scripts for action that make new types of discretionary responses and workarounds necessary." Spektor: "Hotel WCM configured UpKeep in two ways that provide more autonomy to human workers" | 1 and 2 (doctors, midwives and citizen-service staff in three Danish public bureaucracies; housekeeping at one unionized U.S. hotel); 6 (two field studies; Spektor: 'our findings may not be generalizable to the hotel industry as a whole'); 3 (the hotel's freedom is the exception: 'In most implementations of UpKeep, rooms are algorithmically assigned and enforced', and the union contract secured it) | partial | | Name the two settings and say that the hotel's latitude was contract-won and unusual. |
| X-19.3 | More of their day goes to reading decisions made elsewhere | Empirical generalization | Pedersen and Pors p. 89; Spektor §5.3 | Pedersen and Pors: "the introduced standardizing technologies created invisible work (such as preparation, acknowledging citizens' effort, increased documentation)". Spektor: "Increased visibility comes at a cost to workers, who must perform additional labor to update their progress and remain responsive within the app." | 3 (neither study measures time; 'more of their day' is the paper's quantity); 5 (the added work is documenting and updating as much as reading decisions); 2 and 6 as above | partial | | 'Added documentation and coordination work' is what both report. |
| X-19.4 | and to working around categories set elsewhere | Empirical generalization | Pedersen and Pors p. 91; Spektor §5.3.2 | Pedersen and Pors: "the frontline practitioners' professional capacities and ethical dispositions to casuistically adapt, work around, or compensate for standards and rough categories when needed". Spektor: "GRAs will try workarounds like calling their managers or going off to look for supplies on their own, instead of sorting through all of the categories in UpKeep." | 2 and 6 as above | partial | | Supported for the two settings; the only fault is the unmarked generalization. |

- **X-19.1.** P1–P3 = X-19.2 to X-19.4. P4 (assumption): the two field sites stand for hospitality staff at large. C: discretion splits.
- Counter-model: a hotel running the default configuration Spektor describes, with tasks 'algorithmically assigned and enforced'. P2 and P3 hold, P1 fails, and discretion shrinks instead of splitting.
- Quantifiers: the bare 'staff' reads as general; the sources give two sites.
- Terms: 'discretion' in Pedersen and Pors is professional judgment in an office; Spektor writes of 'autonomy' and 'agency' over the order of tasks. The senses are close, not the same.
- Verdict: valid with added premise (P4).

### X-20
> But why was the innkeeper bound at all? The legal history does not settle the question, and Bogen calls the explanation from holding out 'not so much a theory as a tautology' (1996: 52).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-20.1 | But why was the innkeeper bound at all? | Signpost | — | — | — | — | | No check. |
| X-20.2 | The legal history does not settle the question | Own inference | Bogen, 1996 Utah Law Review 51, pp. 51–53 | — | — | valid with added premise | | See the list below. |
| X-20.3 | Bogen calls the explanation from holding out 'not so much a theory as a tautology' | Quotation | same, p. 52 | "According to another theory, offering services to the public was an undertaking to serve all members of the public.[7] But that is not so much a theory as a tautology. Innkeepers made no express promise to serve all comers" | none | supported | | Words exact; speaker Bogen; page confirmed from the running head and the HeinOnline footer. 'Holding out' matches the public undertaking theory, which Bogen attributes to Burdick (n. 7). |

- **X-20.2.** P1 (sourced, p. 51): "The commonly accepted explanations for the development of the public right of access to inns are untenable." P2 (sourced, p. 53): Bogen then answers the question himself: "It was, however, concern for criminal activity in the inn, rather than any monopoly or innkeeper promise, that led to the obligation to serve the public." P3 (assumption, to be sourced): no account, Bogen's included, commands agreement. C: the legal history does not settle the question.
- Counter-model: P1 true and Bogen's account accepted. Then the history does settle it.
- Without P3 the sentence leans on a source that claims the opposite. Bogen's "Why the court imposed the obligation in the first place remains a question" (p. 52) is a charge against the undertaking theory, and he answers it a page later.
- Verdict: valid with added premise (P3). Action: acknowledge Bogen's crime-control answer, or a reader will take him to leave the question open.

### X-21
> The most persuasive account we have found rests on the traveller's exposure: people on a journey, 'away from their home communities and in unfamiliar surroundings', were held to deserve a special legal status (Sandoval-Strausz 2005: 62–63).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-21.1 | The most persuasive account we have found rests on the traveller's exposure | Paraphrase | Sandoval-Strausz, Law and History Review 23(1): 53–94 (2005), p. 62 and n. 15 | "the main idea is that these common law rules existed for the benefit of travelers, a group that enjoyed special privileges in Atlantic and Mediterranean societies." (p. 62) | none; advisory: the account is of American travel law, and the author says it is contested: 'My contention … puts me into disagreement with Joseph William Singer' (n. 15, p. 63) | supported | | None needed. 'Most persuasive … we have found' is the authors' judgment and is marked as theirs. |
| X-21.2 | People on a journey, 'away from their home communities and in unfamiliar surroundings', were held to deserve a special legal status | Quotation | same, pp. 62–63 | "Underlying all common law protections of travelers was a basic assumption: people who were on a journey, away from their home communities and in unfamiliar surroundings, were particularly vulnerable and therefore deserved a special legal status.[15]" | none | supported | | Words exact. The sentence runs over the page break, so '62–63' is right. |

### X-22
> since commercial hosts 'must meet the desires and demands of the paying guest' (Di Domenico and Lynch 2007: 335)

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-22.1 | Commercial hosts 'must meet the desires and demands of the paying guest' | Quotation | Di Domenico and Lynch, Leisure Studies 26(3): 321–338 (2007), p. 335 | "Despite this power imbalance, hosts may also be regarded as paradoxically powerless, as their essential role is one that lacks freedom when receiving guests … They must meet the desires and demands of the paying guest, the 'master/mistress' of the experience." | 1 and 2: 'They' are hosts of commercial homes, 'owner-managers of these micro businesses' who take paying guests into their own houses (abstract, p. 321). 'Commercial hosts' widens this to commercial hospitality at large | partial | | Words exact; page confirmed. Minor. Write 'hosts of commercial homes', or mark the extension to hotels as the paper's. If the draft has already defined 'commercial hosts' in the narrow sense, the row is clean. |

### X-23
> The innkeeper's liability, moreover, reached beyond his own servants to 'other guests or any unidentified party' (Sandoval-Strausz 2005: 65).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-23.1 | The innkeeper's liability reached beyond his own servants to 'other guests or any unidentified party' | Quotation | Sandoval-Strausz 2005, p. 65 | "The innkeeper's liability was in fact so strict that he was answerable not only for the acts or negligence of his servants, but also those of other guests or any unidentified party." | none; advisory on 5: the liability is for guests' goods ('The third obligation of the innkeeper was to safeguard the property of guests', p. 65), in American law as Kent and Story stated it | supported | | Words exact; page confirmed. Keep 'for guests' goods' in view if the draft's context does not supply it. A secondary source for a legal rule. |

### X-24
> The guidance on that article requires the reviewer to be someone 'who has the appropriate authority and capability to change the decision' (Article 29 Working Party 2018: 27).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
| X-24.1 | The guidance on that article requires the reviewer to be someone 'who has the appropriate authority and capability to change the decision' | Quotation; legal proposition | Article 29 Working Party, WP251rev.01 (revised and adopted 6 Feb 2018), p. 27, section F, 'Establishing appropriate safeguards' | "Human intervention is a key element. Any review must be carried out by someone who has the appropriate authority and capability to change the decision. The reviewer should undertake a thorough assessment of all the relevant data" | none | supported | | Words exact; printed p. 27 confirmed. 'That article' fits Article 22 GDPR: the passage glosses the safeguards of Article 22(3), which apply 'If the basis for processing is 22(2)(a) or 22(2)(c)'. Body: an EU advisory body; guidance, not binding. The same guidance words the test for human involvement differently on p. 21 ('the authority and competence to change the decision'). |

---

## Counts by verdict (60 rows)

| Verdict | Rows |
|---|---|
| supported | 29 |
| partial | 18 (6 of them with no passage) |
| contradicted | 0 |
| unverifiable | 3 |
| own inference: valid | 2 |
| own inference: valid with added premise | 5 (2 of them unsound as they stand) |
| own inference: not tested | 2 |
| signpost | 1 |

## Sources not supplied, and rows that wait on them

| Source | Rows | What would settle it |
|---|---|---|
| Burdick 1911, Part I (Columbia Law Review 11: 514 ff.) | X-13.1 | The text of p. 523. `burdick1911origin/1110590.txt` may hold it; the set does not name it. |
| Wyman 1904 | X-13.2 | The article, p. 159. |
| Xu et al. 2021 | X-18.1 | The article. |

## Versions and locators not confirmed

- X-12: the saved Cobbe text is arXiv v2, paged 1–13. I could not confirm '1192'.
- X-09: the version of record is dated 2027; the sentence cites 2026.
- X-06.1: the saved Lyons text is the arXiv preprint. X-02: the saved Garcia text is the CESifo working paper of December 2023.
- X-15: the page is confirmed, the year is not shown in the saved text.
- X-16: the repository's citation says 2014, the running head 2015.
- X-03, X-06, X-07, X-10, X-18, X-19 cite no page; the tables give the locators I found.

## Reading coverage

I read Hatherley (2025) from the first page to the conclusion, and Spektor et al. (2025) from §3 to the conclusion with the introduction. For every other text I read the cited page with the pages on either side, the abstract, the method and the limitations where the text has them, and searched the whole text for the terms of each proposition. A `partial (no passage)` verdict therefore rests on a full read for Hatherley and on reading plus whole-text search for Garcia, Batat and Bosma.

## Summary

| X-id | Sentence verdict | Fault, in one line |
|---|---|---|
| X-01 | sound | — |
| X-02 | faulted | The guest-and-desk scenario is the paper's own; WP29's pricing example loses its hedge and conditions and is applied to a price a manager sets. |
| X-03 | faulted | Hatherley's hedged claim about expert users of ML decision aids is moved to hotel staff and guests and made categorical; 'no one tells' has no passage. |
| X-04 | sound | — |
| X-05 | sound | — (advisory: the quoted sentence describes visitors in Jordanian houses) |
| X-06 | faulted | The Lyons clause states as the authors' finding what consultation submissions 'see', and drops 'likely'; the other two clauses hold. |
| X-07 | faulted | One upscale Chinese hotel's COVID-19 protocols become what 'hotels' do about 'the stay's rules'; 'only' is dropped. |
| X-08 | sound | — |
| X-09 | sound | — (advisory: the criterion applies within on-the-loop oversight; imprint year 2027) |
| X-10 | faulted | 'Rules stay steady' and 'staff keep their discretion' are not in Batat. |
| X-11 | faulted | The failed code at night and the unreachable authority are the paper's scenario, not Bosma's. |
| X-12 | sound | — (advisory: 'find' for an argument; p. 1192 not confirmed) |
| X-13 | unverifiable | The named Burdick files are Parts II and III and p. 523 is in Part I; no Wyman text. |
| X-14 | faulted | Luxury-hotel interviewees become 'guests'; p. 286 is the proposed mechanism and the finding is on p. 291; deeper explanation belongs after the stay, not later in it. |
| X-15 | sound | — |
| X-16 | sound | — (advisory: the authority is Beale, reported by a student article) |
| X-17 | sound | — |
| X-18 | faulted | Vignette respondents become guests, scenario abilities become fact, and the effect is not tied to failure; the Xu clause is unverifiable. |
| X-19 | faulted | Two field sites (Danish public offices; one unionized U.S. hotel whose latitude was the exception) are generalized to 'staff'; 'more of their day' is unmeasured. |
| X-20 | sound | — (advisory: Bogen answers the question himself on p. 53) |
| X-21 | sound | — |
| X-22 | faulted | Minor: hosts of commercial homes are widened to 'commercial hosts'. |
| X-23 | sound | — |
| X-24 | sound | — |
