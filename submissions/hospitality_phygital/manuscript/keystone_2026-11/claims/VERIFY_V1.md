<!-- Independent verification of claim registers A1, A6, A7, run rr-2026-11-k, written by a Claude (Fable 5.2) subagent on 11 Nov 2026. -->

# Verification V1: claim registers A1, A6 and A7

**What I checked.** 63 rows of `CLAIM_REGISTER_A1.md`, `CLAIM_REGISTER_A6.md` and `CLAIM_REGISTER_A7.md`, against `manuscript/DRAFT_v6.md` (SHA-256 `8951cadf…537e7`, the hash frozen in K-D5) and against the source texts. I opened each source myself, found the passage, and gave my own verdict before weighing the auditor's reasoning. For inference rows I ran the brief's tests first. I edited no register, card or other file, and I did not open `VERIFY_V2.md` or `VERIFY_V3.md`.

**Selection, and how I read the rule.**

- *Rule 1*, every `fatal` row: A-4.1, S-015.1; S-175.1; S-192.3.
- *Rule 2*, rows named for a second reader. The registers' closing sections name none. The auditors' reports do, and they are not saved in the run folder, so I read each report from the lead session's subagent transcript (read only). A1's report names S-011c.3, S-023.2, S-009.2 and S-012.2 (and the legal counter-models, already under rule 1). A6's names S-158.2 and S-168.2 (and S-175.1). A7's names S-192.3, the rows on five abstract-only sources and on Hirschman (S-193.1, S-198.1, S-199.1, S-199.2, S-202.1, S-202.2, S-202.3, S-189.3) and the two equivocal rows S-186.q5 and S-183.2.
- *Rule 3*, every fourth of the remaining rows whose verdict is not `supported`, `valid` or a signpost. I took the verdict strings exactly, so `supported (abstract only)` and `valid with added premise` fall in this pool. A1 (46 in the pool): A-1.1, A-3.2, A-6.1, S-001.2, S-003.3, S-006.1, S-009.1, S-011b.1, S-011c.1, S-016.1, S-018.2, S-025.1. A6 (30): S-149.1, S-151.3, S-156.1, S-162.1, S-165.1, S-169.3, S-173.2, S-176.1. A7 (33): S-179.1, S-182.2, S-185.2, S-188.1, S-191.2, S-192.5, S-195.3, S-197.1, S-201.2.
- *Rule 4*, every sixth `supported` or `valid` row. A1 (11 such rows): S-006.2, S-010.3. A6 (16): S-150b.1, S-156.2, S-168.1. A7 (15): S-179.2, S-186.q1, S-195.2.
- *Dispute rows* added outside the rule, because the four disputes cannot be settled without them: S-012.3 and S-023.1 (A1); S-158.1 (A6); S-192.1, S-192.2 and S-192.4 (A7).

**Texts.** Saved texts are under `manuscript/revision_2026-11/research/sources/<citekey>/` unless marked `corpus/` (`manuscript/rewrite_2026-11/journal/corpus/<key>/`). I re-fetched the Crossref records of Batat 2026, Boo and Chua 2022, Bendoly 2013, Fuller and Smith 1991, Morrison 2014, Cheng et al. 2025 and Garcia et al. 2026 on 11 Nov 2026; the five abstracts the auditor of A7 saved are identical to what Crossref returns now. Unpaywall and OpenAlex report all of these closed except Morrison (bronze) and Garcia (hybrid); the publisher copies of both, and the Tor Vergata repository copy of Garcia, returned a bot challenge (HTTP 403), which I did not try to pass. Hirschman 1970 has no open copy (Open Library: print-disabled lending only). I read sources by passage and by whole-text search, as the auditors did; for Garcia et al. I read pp. 1–15 and 32–34 and the opening of Appendix C, and skimmed pp. 16–31.

**Entry format.** Row and selection rule; the auditor's verdict and severity; the passage I rely on; my verdict and severity; AGREE, AGREE-WITH-NOTE or DISAGREE; the reason.

---

## Register A1: the Abstract and the Introduction

### Rule 1: fatal rows

**A-4.1** · 'the work can be delegated and the duty cannot'
- Auditor: invalid · fatal.
- Passages. *Woodland v Essex CC* [2013] UKSC 66 (`woodland2013uksc/woodland.txt`), para 7: 'The work required to perform such a duty may well be delegable, and usually is. But the duty itself remains the defendant's.' Para 22: 'Non-delegable duties of care are inconsistent with the fault-based principles on which the law of negligence is based, and are therefore exceptional.' Para 24: 'as a general rule he is not liable for the contractor's negligence.' Occupiers' Liability Act 1957 s 2(4)(b) (`ola1957/s2.html`): 'the occupier is not to be treated without more as answerable for the danger if in all the circumstances he had acted reasonably in entrusting the work to an independent contractor'.
- Mine: invalid · fatal. Premises: (1) for Woodland's second category the work is delegable and the duty stays; (2, unstated) every duty of a commercial host is of that category. Counter-model: a hotel entrusts repair to a competent contractor and checks the work; under s 2(4)(b) it does not answer for the contractor's fault. The quantifier ('the duty', singular and universal) does not follow from a category the court calls exceptional.
- **AGREE-WITH-NOTE.** Two things strengthen the auditor's row. The 1957 Act, s 5(1) (`ola1957_s5/s5.txt`), gives a person who enters 'in exercise of a right conferred by contract' the same 'common duty of care', so the counter-model holds for a paying guest and not only for a visitor. And later treatment, which the auditor did not check, keeps the line: *Armes v Nottinghamshire CC* [2017] UKSC 60, para 37 (`armes2017uksc/`), asks whether the function 'was one which the local authority were themselves under a duty to perform … or was one which they were merely bound to arrange to have performed'.

**S-015.1** · 'Because the law attaches the duty to the role … the duty, and the answering for it, stay with the holder'
- Auditor: invalid · fatal.
- Passages: as A-4.1; and *Woodland* para 25(3): schools 'will not be liable for the negligence of independent contractors where on analysis their own duty is not to perform the relevant function but only to arrange for its performance.'
- Mine: invalid · fatal. 'Because' needs the premise that a duty attached to a role is non-delegable whoever the delegate; the occupier's duty attaches to a status and is discharged by reasonable entrustment. The sentence holds for employees, for the innkeeper's liability for goods and for what the host has contracted to do (para 7: 'The contracting party will normally be taken to contract that the work will be done carefully by whomever he may get to do it').
- **AGREE-WITH-NOTE.** The auditor writes that the occupier's duty 'did not stay'. That is loose: the duty of reasonable care stays with the occupier; what the statute withholds is answering for the contractor's fault. The counter-model therefore defeats 'the answering for it', which is the half of the sentence the argument needs. Verdict, severity and action stand.

### Rule 2: rows named for a second reader

**S-009.2** · Shryock's good host is one able to 'protect guests from harm' (2012: S20)
- Auditor: partial (classes 2, 4, 5, 9) · material.
- Passage (`shryock2012breaking/plain.txt`), S20: 'The man who is karim (hospitable, generous, noble) is able to feed others, project an honourable and enviable reputation, and protect guests from harm. Hospitality, as Bedouin describe it, is a quality of persons and households'. S31: 'The Balga Bedouin, who would never confuse karam with the hospitality offered to tourists or the bureaucratic handling of foreigners by the state'.
- Mine: partial (2, 4, 5) · material. Words and page are exact. The good host is the Balga Bedouin's, by their description, and the passage states an ability that tests sovereignty; the sentence joins it to 'owes' and gives no setting.
- **AGREE.** Shryock's own S30–S31 sets commercial hospitality apart ('depersonalized, formulaic, monetized'), so the missing setting changes what a reader takes.

**S-011c.3** · the phygital literature calls for human-first design and contestable rules 'without saying to whom these safeguards are owed or which of the firms behind a system owes them' (gap row; see also 'Disputes settled')
- Auditor: partial · material; the gap survives only in a narrow form.
- Passages. Shabnam et al. 2026 (`shabnam2026tpsr/user_pdf/fulltext.txt`, §7.2, PDF p. 14): 'organisations should prioritise transparent artefact design … Secondly, algorithmic governance must remain contestable. Digitally enforced rules should incorporate escalation pathways and human oversight'; the section ends on 'advancing consumer well-being'. Gursoy 2026: 155 (`gursoy2026reconceptualizing/`): 'hospitality firms transition from being providers of human-centric service to stewards of algorithmic governance'. Sharma and Mattila 2026: 911 (`sharmamattila2025rights/`): 'who should be blamed? The restaurant company, the robotic manufacturer who provided the robot, or the algorithm creators who made it? Or was the manager on duty responsible'.
- Mine: partial (3, 5) · material. The cited text names who should act (managers, organisations, policymakers) and for whose good (consumers). It states no duty owed to the customer and does not divide the task among firms. One of the two sources cited, Batat 2026, is closed, and its abstract does not mention governance (see S-011c.1).
- **AGREE.** The narrow form the auditor proposes is the one the texts license.

**S-012.2** · algorithmic-accountability research 'ties it to harm' (gap row)
- Auditor: partial (3, 5) · material.
- Passages. Nissenbaum 1996, preprint p. 2 (`nissenbaum1996accountability/`): 'accountability for the impacts of computing, specifically for the harms and risks of faulty and malfunctioning systems'. Kong 2026: 5 (`kong2026delegation/`): 'A gap is genuine only when the harmful disposition the agent expressed was not a foreseeable property of the deployment specification'. Against: Lyons et al. 2021, arXiv §2.1 (`lyons2021conceptualising/arxiv.txt`): 'the ability to contest decisions that have a significant impact on a person's life, whether made by a human or algorithm, is an important way to uphold human dignity and autonomy'.
- Mine: partial (3, 5) · material. True of the two works cited; false as a statement about the field.
- **AGREE-WITH-NOTE.** A nearer refuter sits in v6's own reference list and the auditor did not use it. Cobbe et al. 2023: 1187 (`cobbe2023understanding_vor/vor.txt`, §2) describe accountability in this literature as 'an institutional arrangement whereby an actor provides accounts to a forum, who deliberates on those accounts and may impose consequences', and add that 'Some algorithmic accountability literature explicitly views accountability as a mechanism for holding actors to account for their systems'. That definition has no harm condition. Cobbe et al. take it from Bovens (their reference 12), whose relation the paper itself adopts.

**S-023.2** · the debate 'has had no way to say where it goes once no person does the hosting' (gap row)
- Auditor: partial · material.
- Passages. Liu et al. 2026: 9 (`liu2026hospitableness/`): 'robotic hospitableness is relationally experienced by guests rather than internally possessed by the machine.' Sharma and Mattila 2026: 915: 'What are the rights and responsibilities of a human employee, and how should the firm (owners and management) translate those into the service robot context?'
- Mine: partial (3, 5) · material. Hospitality research has begun to say where hospitableness and responsibility go when a machine serves; none of it states a duty owed to the guest or picks a holder among several firms.
- **AGREE-WITH-NOTE.** The auditor missed that v6 answers its own sentence. 'Delegation and standing' ¶3 says 'This journal already has words for the result', citing Bulley's assembled host and Lynch et al.'s 'micro-hosts … and macro-hosts such as the train company' (Lynch et al. 2011, `corpus/lynch2011/plain.txt`, 'Hospitality as social and economic exchange'). A company named as host in the journal's founding editorial narrows 'no way to say' further than the three papers the auditor names.

### Rule 3: every fourth of the other faulted rows

**A-1.1** · 'Hospitality firms now hand much of the work of hosting … to algorithmic systems'
- Auditor: partial (3, 6) · material.
- Passages. Garcia et al., CESifo WP 10849 (`garcia2026strategic/text.txt`), p. 2: 'algorithmic price recommendations of an independent revenue management company (the algorithm's designer), prices set by hotel managers (human manager)'. Boo and Chua 2022, Crossref abstract: 'A self-administered online questionnaire … Guests who stayed in four- or five-star hotels in Singapore were recruited'. Bosma 2022: 605 (`bosma2022platformed/paged.txt`): 'such a self-check-in option is required by Airbnb'.
- Mine: partial (3, 6) · material. The sources show advice on price, a survey of intentions and one platform's option; none shows 'much'.
- **AGREE.** The auditor's Garcia quotation ('human managers who retain the final decision right', p. 2) is the authors' general remark about 'many of these applications'; the hotel-specific words are those above and on p. 10. The point is unaffected.

**A-3.2** · the commercial host's obligation is a role obligation, imposed on whoever receives travellers
- Auditor: equivocal (and undergenerates) · material.
- Passages. Hotel Proprietors Act 1956 s 1(1) (`hpa1956/s1.txt`): 'An hotel within the meaning of this Act shall, and any other establishment shall not, be deemed to be an inn'. Calye's Case, 1777 ed. of Coke (`calye1584/`): 'if the guest be beaten in the inn, the innkeeper shall not answer for it … the innholder ought to keep the goods and chattels of his guest, and not his person'.
- Mine: equivocal, undergenerates · material. 'Obligation' is customary in the first premise and legal in the second, with different contents; the conclusion fails for a restaurant, a rental and a placed guest; the same form of argument fits carriers and banks, which v6 concedes.
- **AGREE.**

**A-6.1** · 'algorithmic mediation rarely removes the host's obligation'
- Auditor: valid with added premise · material.
- Mine: valid with added premise · material. The added premise is that every duty stays with the holder when a system does the work, which A-4.1 does not establish. Counter-model: a system that refuses admission, so that no duty arises.
- **AGREE.**

**S-001.2** · systems and firms 'that the guest rarely sees'
- Auditor: partial (3) · minor.
- Passages. Belanche et al. 2020: 273 (`belanche2020/user_pdf/fulltext.txt`): 'Connie is a robot concierge introduced by Hilton'. Bosma 2022: 605: 'the Host Assist program allows smart lock providers and other companies to integrate their services on the Airbnb platform'.
- Mine: partial (3) · minor. True of suppliers; false of the robot, the kiosk and the lock, which the paragraph itself lists.
- **AGREE.**

**S-003.3** · 'in vignette experiments, respondents held the firm more responsible when a robot rather than an employee failed'
- Auditor: partial (3) · minor.
- Passages (Belanche et al. 2020). Study 1, pp. 276–277: 'is only significant for the service failure condition (F_FAILURE = 3.97; p < 0.05'. Study 2, pp. 280–281: mechanical robot against human 't = 2.13, p < 0.05'; analytical robot against human 't = 1.24, p > 0.10'; pooled 't = 1.91, p < 0.10'; overall F = 2.18, 'n.s.'.
- Mine: partial (3) · minor. The plural holds for Study 1 and, in Study 2, for the robot described as mechanical only.
- **AGREE.** The auditor went to the results and not to the abstract's summary line, as the brief requires.

**S-006.1** · definition of 'algorithmic system'
- Auditor: equivocal · minor.
- Mine: equivocal · minor. The greeting robot of S-003 takes or shapes no decision about a guest, and 'such systems' at S-011b and S-025 are not defined by a decision.
- **AGREE-WITH-NOTE.** The auditor lists the lock of S-004 among the non-deciders. v6 itself counts 'a key card that opens or does not' among 'digital rulings' (S-158), so the lock is a weak instance; the robot carries the row.

**S-009.1** · 'On that view the host owes the guest more than a service'
- Auditor: partial (4, 5) · material.
- Passage (Lynch et al. 2011, `corpus/lynch2011/plain.txt`, Introduction): 'historical accounts of hospitality, which often hark back to Greek and Roman or Enlightenment antecedents (O'Gorman 2007; Still 2006). In these traditions, hospitality entailed a sacred obligation not just to accommodate the guest, but to protect the stranger who arrived at the door.'
- Mine: partial (4, 5) · material. The editors report historians on ancient traditions; they state no duty of commercial hosts.
- **AGREE-WITH-NOTE.** The nearest passage to the sentence is one the auditor did not paste: the dominant definition 'reduces hospitality to an economic activity, just as it reduces the interactions between hosts and guests to commercial exchanges' (Introduction, next paragraph). It licenses 'more than a service' as a description of the relation. It does not license 'owes'.

**S-011b.1** · the phygital literature presents such systems 'as means to a smoother and more personal experience (Batat 2024)'
- Auditor: partial (5, 3) · minor.
- Passages (`batat2024phcx/user_pdf/fulltext.txt`). p. 1220: 'This is done by fluidifying the journeys of customers from online to offline and inversely'. p. 1223: 'offer them personalized services', said of benefits others claim for multichannel strategy.
- Mine: partial (5, 3) · minor. Batat's subject is a strategy and its connectors, not software that decides about a guest; 'more personal' is not her claim for phygital.
- **AGREE.** v6 gives no page for this citation; a locator belongs with the fix.

**S-011c.1** · 'Where it turns to governance, it calls for human-first design' (Batat 2026)
- Auditor: supported (abstract only) · minor.
- Passage (Crossref abstract, 10.1108/JSM-09-2025-0600, fetched 11 Nov 2026): 'proposes a human-first logic grounded in "phygital phenomenology" by integrating technology without compromising experiential authenticity.'
- Mine: supported (abstract only) for 'calls for human-first design' · minor.
- **AGREE-WITH-NOTE.** The abstract does not use the word governance or name any safeguard. The frame 'Where it turns to governance' and the 'safeguards' of S-011c.3 therefore rest, for this source, on nothing anyone has read.

**S-016.1** · 'The guest's standing therefore survives delegation'
- Auditor: valid with added premise · minor.
- Mine: valid with added premise · minor. Added: the stipulated sense of standing held, and that each duty which stays is owed to the guest. Counter-model: a duty that stays and is enforced by the state alone.
- **AGREE.** The row inherits less from S-015.1 than the auditor says: where the occupier discharges the duty by entrustment the guest is still the person to whom reasonable care is owed.

**S-018.2** · 'the authority to answer for it'
- Auditor: equivocal · minor.
- Passage (v6, 'Delegation and standing' ¶2): 'Authority is the power, assigned by an organization, to change a decision or the rule behind it'.
- Mine: equivocal · minor. The phrase gives authority the object of accountability.
- **AGREE.**

**S-025.1** · the paper sets aside whether a machine could itself bear a host's duties
- Auditor: partial (the stipulation is not kept) · minor.
- Passage (Kropf et al. 2026, abstract, `kropf2026blame/`): care robots 'can still hold role responsibility based on their social function in caregiving contexts'.
- Mine: partial · minor.
- **AGREE-WITH-NOTE.** S-015 by itself does not need the answer 'no': a holder's duty can stay whether or not the delegate also bears one, as it does with staff. The stipulation is broken outside the batch, where 'Delegation and standing' ¶5 adopts Kong's 'one who elects a delegate that cannot answer thereby elects to answer for it' and Kropf's view that a robot's answerability 'is currently inconceivable'. The fix belongs there.

### Rule 4: every sixth passed row

**S-006.2** · definition of 'phygital arrangement'
- Auditor: valid.
- Mine: valid, with a looseness. The definition puts the guest inside the arrangement ('the guest, the staff, the property, the firms and the systems together') and the next clause has the guest meet it ('any moment at which the guest meets that arrangement').
- **AGREE-WITH-NOTE.** The auditor wrote that the one other use in the batch is 'in the same sense'. It is not quite: there the arrangement is what faces the guest, as it is at S-154 and S-170; the Conclusion returns to the inclusive sense ('scattered those jobs across guest, employee, brand, vendor and platform'). A minor point, and one the definition row should have listed.

**S-010.3** · Germann Molz (2018: 244) described Airbnb using its status as a platform to evade legal responsibility
- Auditor: supported.
- Passage (`germannmolz2018scale/user_pdf/fulltext.txt`, p. 244): 'The Community Commitment to anti-discrimination was a preemptive move that brings into stark relief the lengths to which Airbnb goes to use its status as a digital platform to evade legal responsibility.'
- Mine: supported. All nine classes clean: the firm is named, the verb 'described' fits a discourse analysis, the judgement is the author's, and the page is that of the version of record.
- **AGREE.**

### Dispute rows outside the rule

**S-012.3** · 'hospitality research measures hospitableness as a motive of individual hosts (Lashley 2015: 1)'
- Auditor: partial (3) · minor.
- Passages. Lashley 2015: 1 (`lashley2015hospitality/paged.txt`): 'a research instrument that can be used to identify those individuals who are driven by a personal desire to be hospitable to others.' p. 6: 'the instrument is clearly focused on one narrow motive for offering hospitality'. Pijls et al. 2017: 126 (`pijls2017measuring/verifier2/pijls.txt`): a scale that 'includes the experience of hospitality offered by the organization as a whole'. Tasci et al. 2021: 341 (`tasci2021cultural/tasci2021.txt`): 'most studies measured hospitableness and hospitality at the firm level while only a few measured the construct in the destination context.'
- Mine: partial (3) · minor. One instrument stands for a field; its own author calls it narrow.
- **AGREE.** Tasci's 'firm level' means in firms as against destinations, measured as customers perceive it. It narrows 'motive of individual hosts'; it does not show an organization measured as a host.

**S-023.1** · the debate looks 'for the obligation in the host's motive'
- Auditor: partial (5) · material.
- Passages. Lashley 2015: 4: 'the duty to provide hospitality, to act with generosity as a host, and to protect visitors is more than a matter left to the preferences of individuals.' Blain and Lashley 2014: 2 (`blain2014hospitableness/paged.txt`): 'there is an obligation, accepted by hosts, to care for and protect guests'; religious strictures 'represent an obligation which may be at odds with Telfer's notion of hospitableness because the host is behaving in a way that has been externally imposed'.
- Mine: partial (5) · material. The debate ties hospitableness, the genuineness of the welcome, to motive. The same authors state the obligation apart from motive and set the two against each other.
- **AGREE.**

### A1 summary

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 fatal | 2 | 0 | 2 | 0 |
| 2 named | 4 | 2 | 2 | 0 |
| 3 every fourth | 12 | 8 | 4 | 0 |
| 4 every sixth passed | 2 | 1 | 1 | 0 |
| Dispute rows | 2 | 2 | 0 | 0 |
| **All** | **22** | **13** | **9** | **0** |

**DISAGREE.** None. Every passage I checked is at its locator and says what the auditor reports.

**Faults the auditor missed.**

1. S-012.2: Cobbe et al. (2023: 1187), cited in v6, define accountability in this literature as an actor giving accounts to a forum, with no harm condition. It refutes 'ties it to harm' from inside the field.
2. S-023.2 with S-023.1: v6's own 'Delegation and standing' ¶3 ('This journal already has words for the result') contradicts the Introduction's 'has had no way to say'.
3. S-011c.1: Batat 2026's abstract has no governance in it, so half of the citation for 'Where it turns to governance' is unread.
4. S-015.1 and A-4.1: the 1957 Act s 5(1) carries the counter-model to paying guests; *Armes* (2017) confirms the reading of *Woodland*; and the counter-model defeats 'the answering', not 'the duty stays'.
5. S-006.2: the guest is inside the arrangement and also meets it.
6. S-009.1: the nearer passage ('reduces the interactions between hosts and guests to commercial exchanges') was not pasted.

**Disputes settled: the gap rows.**

| Statement in v6 | Source in the library that most nearly refutes it | Can it stand, and in what form |
|---|---|---|
| The phygital literature calls for safeguards 'without saying to whom these safeguards are owed or which of the firms behind a system owes them' (S-011c.3) | Within the phygital literature, the cited text itself: Shabnam et al. 2026, §7.2–7.3 (PDF p. 14) names managers, organisations and policymakers as the actors and 'consumer well-being' as the end. Beside it, Gursoy 2026: 155–156 makes hospitality firms 'stewards of algorithmic governance', and Sharma and Mattila 2026: 911 ask which of company, manufacturer, algorithm maker and duty manager is to blame. Neither of the last two uses the word phygital. | Yes, narrowed: the literature addresses its safeguards to managers and policymakers for the consumer's good; it does not state them as duties owed to the customer or guest, and it does not divide them among the firms behind a system. Hospitality papers on AI have posed the second question and left it open. Batat 2026 can be cited only for 'human-first' until someone reads it. |
| Algorithmic-accountability research 'ties it to harm' (S-012.2) | Cobbe et al. 2023: 1187 (accountability as accounts given to a forum); Lyons et al. 2021, §2.1 (contesting upholds 'human dignity and autonomy'). Both are in v6's reference list. | Not as a statement about the field. It stands as: Nissenbaum (1996) and Kong (2026: 5) look for answerability among designers and deployers and frame it by the harms a system causes. Kong also grounds it in a role taken up (p. 3: 'provided one occupied a role, undertook a task, or created a risk'), which the paper should credit. |
| 'Hospitality research measures hospitableness as a motive of individual hosts' (S-012.3), and the debate, 'by looking for the obligation in the host's motive', has had 'no way to say where it goes once no person does the hosting' (S-023.1, S-023.2) | For measurement: Pijls et al. 2017: 126; Lashley 2015: 6 on his own instrument. For the obligation: Lashley 2015: 4 and Blain and Lashley 2014: 2, who state it apart from motive. For 'no way to say': Lynch et al. 2011 on macro-hosts such as a train company, which v6 itself cites; Liu et al. 2026: 9; Sharma and Mattila 2026: 915. | Yes, narrowed and with the terms kept apart: the debate over whether a paid welcome can be genuine ties hospitableness to a person's motive (Lashley 2015: 1, 5); the same literature states the host's obligation separately and has named organizations as hosts; it has not said which organization holds that obligation, towards the guest, when systems and several firms do the hosting. As a gap statement that last clause takes the form 'I found no work that…', with the auditor's queries. |

---

## Register A6: the opening of 'Assembled hosts' and 'The authority–answerability split'

### Rule 1: fatal row

**S-175.1** · 'Authority over the rule drifts towards whoever designs, configures or controls it, often a vendor' (dispute)
- Auditor: partial (2, 6, 5) · fatal; 'its hospitality evidence points the other way'; two hotel studies in the library show managers keeping the rule.
- Passages. The cited source, Cobbe et al. 2023: 1195 (`cobbe2023understanding_vor/vor.txt`, §4.3.1): 'service models offer providers new ways to extend control past the point of deployment … providers seek to use service agreements to maximise control over deployment of their technologies by reserving rights to dictate terms of use and change, withdraw, or cancel products and services at will.' The words hotel, hospitality and guest do not occur in the paper.
- The two hotel studies are Garcia, Tolvanen and Wagner (CESifo WP 10849, the saved version of Garcia et al. 2026) and Spektor et al. 2025.
  - Garcia, for the auditor: p. 2, 'prices set by hotel managers (human manager)'; p. 10, 'The hotel manager decides every day whether to use the revenue management system to update prices.'
  - Garcia, against the auditor: p. 7, 'In the spirit of Aghion and Tirole (1997), machines hold real authority because the information-processing costs of the human decision maker vastly exceed those of the algorithmic advisor.' p. 4 n. 6: 'the average probability of copying the recommendation conditional on a price change is 84%'. p. 34: 'the responsibility for mistakes typically rests with the final decision maker while the designer of the algorithm largely escapes liability for poor advice.'
  - Spektor et al. 2025, for the auditor (`spektor2025working/verifier2/sp25.txt`, §6.1): 'What appears as self-sequencing is actually a tacit workaround enabled by the union contract at this hotel'. Against, §5.1.1: 'In most implementations of UpKeep, rooms are algorithmically assigned and enforced'; 'UpKeep does not currently support self-sequencing directly'; 'Without this contractual flexibility, workers would be required to follow the sequence dictated by UpKeep.' The rule in question orders housekeepers' work; no rule applied to a guest is studied.
  - A third hotel text in the library says who configures: Spektor et al. 2023 (`spektor2023designing/verifier2/sp23.txt`), 'GRAs' ability to control their own task flow now depends on the configuration of UpKeep within their hotel properties' (the extraction drops the ligatures in 'flow' and 'configuration'; I restored them).
- Mine: partial (2, 5, 6; and 3, since 'seek to … by reserving rights' becomes 'keeps the right') · **material**.
- **DISAGREE (severity).** The verdict stands: the cited paper is about AI and cloud services and counts nothing. The grade does not. The two studies do not 'show managers keeping the rule'; each shows the property holding the formal power to depart from a supplier's default and the default prevailing most of the time, and Garcia et al. say in terms that the machine holds 'real authority'. The library's hotel evidence therefore supports a narrower sentence and does not refute the possibility the argument needs, which is that power over the rule can sit where the guest cannot reach it. Rewrite as a possibility, say that the configurer is often the property (Spektor), and cite Garcia pp. 7 and 34 for a supplier whose advice is mostly copied and who 'largely escapes liability'. That is a correction before submission, not a collapse.

### Rule 2: rows named for a second reader

**S-158.2** · the two processes 'can as accurately be called a relay' (dispute)
- Auditor: partial (7, 9, 5) · material; the relay is not Batat's two processes.
- Passages (`batat2024phcx/user_pdf/fulltext.txt`). pp. 1230–1231: 'The customer's experience is created and shaped through two processes: shifting from physical to digital ('digitalization') and from digital to physical ('physicalization.')' p. 1236: 'the digitalization process is meant to transform physical customer experiences into digital ones. By shifting from physical to digital, there is a need to enhance … immersivity, sensoriality, and affectivity.' pp. 1236–1237: 'the physicalization process refers to the transformation of digital customer experiences into physical ones … by introducing digital devices and technologies along with emphasizing the value continuum from digital to physical settings and thus humanizing the contact with customers.'
- Search: record, ruling, relay, authorit, discretion, complain, 'key card' and 'check-in' occur nowhere in the article; 'decision' occurs four times in the body, each time of a consumer's or patient's own decision. I confirm the auditor's counts.
- Mine: partial (7, 9, 5) · material.
- **AGREE.** What may be credited to Batat: the two names; that they are two processes through which a customer's experience 'is created and shaped', one shifting it from physical to digital and one back (pp. 1230–1231); and that each is a transformation of customer experiences with its own design priorities (p. 1236). What may not: a relay, handoffs, records, rulings, the key card, the price on the screen, or any question of who holds authority. Her processes carry an experience and its value between settings; the paper's relay carries data and decisions. 'As accurately' asserts that the second redescribes the first, and it does not. The relay is the paper's own figure and should be offered as one.

**S-168.2** · a manager told staff that guests 'are here as your guests, but they cannot demand everything', because the hotel has its 'own standard'
- Auditor: partial (4, context, 7) · material; either keep the parts that show the frontline being handed the house 'or stop using the remark as the evidence for graded authority'.
- Passage (`golubovskaya2017meaning/user_pdf/fulltext.txt`, p. 1297): 'participants refer to their managers not only by saying but also practicing hospitality values themselves and giving employees confidence and power to feel like a "host": … Particularly thanks to the manager who told us just be confident, they are here as your guests, but they cannot demand everything, always try to help them, but we have own standard […] just consider it as your house (P-7).'
- Mine: partial (4, 7) · material. The quoted words are exact and on p. 1297. An employee, P-7, reports the manager; the authors offer the remark under 'leadership'; 'because' is the paper's.
- **AGREE-WITH-NOTE.** I agree on verdict and severity and differ on the action. Read whole, the remark shows a manager handing the frontline a bounded power ('just consider it as your house') under an organizational limit ('we have own standard'). That is what 'graded' means, so the remark can stay as evidence if the speaker is named and the cut restored. It remains one employee's recollection, which is the fault S-166.1 already records.

### Rule 3: every fourth of the other faulted rows

**S-149.1** · a guest's claim has a path to travel to the holder
- Auditor: valid with added premise · minor.
- Mine: valid with added premise · minor. Added: the receiver of a claim is often not the holder, and a claim does its work only on arrival. Counter-model: an owner-manager at the desk.
- **AGREE.**

**S-151.3** · Germann Molz describes 'the other end of the path'
- Auditor: partial (5, 7) · minor.
- Passage (p. 244): 'In response to civil rights claims, Airbnb lawyers have argued that "any penalty should be on the hosts renting out their homes, not on the company" (Mock 2017)'; p. 243: Airbnb 'can claim exemption from other regulations as well, namely state and city taxes, and fair and equal housing laws.'
- Mine: partial (5, 7) · minor. Only the civil-rights sentence concerns a guest's claim on the company; the rest is tax, housing and employment law.
- **AGREE.**

**S-156.1** · accounts 'describe the movement between physical and digital touchpoints as fluid'
- Auditor: partial (3; 5 slight) · minor.
- Passages (Batat 2024). p. 1220: 'This is done by fluidifying the journeys of customers'. p. 1230: 'by fluidifying how customers navigate through digital spaces and physical places.' p. 1232: 'The idea of connectors goes beyond the touchpoints logic often used in channel marketing'.
- Mine: partial (3) · minor. Batat sets fluidity as what design should bring about.
- **AGREE.**

**S-162.1** · 'the platform divides the host's role among primary hosts, co-hosts and listing administrators (Bosma 2022: 601)'
- Auditor: partial (2; 3 slight) · minor.
- Passage (`bosma2022platformed/paged.txt`, p. 601): ''host' might refer to users with different roles: 'primary hosts,' 'listing admins or owners,' and 'co-hosts' (Airbnb Help Center, n.d.).' p. 605: hosting 'is increasingly being broken down into separate types of labor'.
- Mine: partial (2) · minor. One platform's account types, from its help centre.
- **AGREE.** The auditor is right to keep 'or owners': p. 601 adds that listing owners 'have access to the payout from Airbnb, while a co-host does not'.

**S-165.1** · the question is whether a claim reaches 'someone with authority over the rule'
- Auditor: equivocal ('authority') · minor.
- Passages (v6). S-102: 'to change a decision or the rule behind it'. S-154: 'the party that can change a decision, or the rule behind it'. Here: 'authority over the rule'.
- Mine: equivocal · minor. The object narrows from decision-or-rule to rule; the restaurant case leaves the question without an object.
- **AGREE.**

**S-169.3** · 'decades before any algorithm'
- Auditor: partial (no passage) · minor.
- Passages. *Crinkley*, 844 F.2d at 158 (`crinkley1988holiday/fable/cap_844F2d156.html`): 'Sometime before the weekend of February 27, 28, 1981'. Bosma 2022: 605: 'PMSs have been in widespread use in the hotel industry since the 1980s (Collins, 1988)'.
- Mine: partial (no passage) · minor. The dating is the paper's own, and hotel software is as old as the case.
- **AGREE.**

**S-173.2** · the system can hold a guest's history, preferences, spending and loyalty status
- Auditor: partial (no passage) · minor.
- Search: Rahman 2021 has 'hotel' once, in a list of rated services, and neither 'guest' nor 'loyalty'; Calo and Rosenblat mention hotels only as legacy competitors of platforms.
- Mine: partial (no passage) · minor.
- **AGREE.** A nearer source sits in the library uncited: Gursoy 2026: 155, 'AI systems collect, infer, and act upon guest data in ways that reshape power relations across the service ecosystem.'

**S-176.1** · 'Discretion acts on the single case and authority on the rule'
- Auditor: equivocal · material.
- Passages (v6). S-102 as above. Abstract: 'a reachable party with authority to change the decision'. S-144: requests 'reach someone with authority to grant them'.
- Mine: equivocal · material. Power over the single case is authority at S-102, in the abstract and at S-144, and discretion here. The conclusion follows from the stipulations; the fault is that the second stipulation contradicts the paper's definition, so the paper's success case (S-145) becomes this sentence's failure case.
- **AGREE.**

### Rule 4: every sixth passed row

**S-150b.1** · Glasgow hotels housed asylum seekers during the pandemic
- Auditor: supported.
- Passage (`corpus/petie2025/plain.txt`; PDF p. 9): 'Badreddin and Adnan were two of 300 asylum seekers moved from community housing into one of six Glasgow-based hotels at the outbreak of the Covid-19 pandemic.'
- Mine: supported. Population and setting are named in the sentence; nothing is widened; the advisory on version (accepted manuscript, no journal page) is correct.
- **AGREE.**

**S-156.2** · accounts 'make smoothness a goal of design (Batat 2024: 1220, 1233)'
- Auditor: supported.
- Passage (p. 1233): 'These strategies should fit with the design of the company's website and vice versa to ensure a seamless customer experience is delivered-one in which the customer can recognize the DNA of the company's brand image'.
- Mine: supported.
- **AGREE-WITH-NOTE.** 'Seamless' on p. 1233 means that store merchandising and website carry one brand image. The pages on smooth movement between settings are p. 1230 ('fluidifying how customers navigate') and p. 1235 ('fluidifying the shift of the shopping experience from physical to digital settings and vice versa'). The claim holds of the article; the second locator fits it loosely.

**S-168.1** · the hotels studied were upscale
- Auditor: supported.
- Passage (p. 1300): 'the research sample was limited to upscale hotels in one region of Australia.' Method: 'frontline employees working in 4-5-star hotels in eastern Australia'.
- Mine: supported; nine classes clean.
- **AGREE.**

### Dispute row outside the rule

**S-158.1** · Batat names the two directions digitalization and physicalization (2024: 1230–1231)
- Auditor: supported.
- Passage: as S-158.2; the sentence runs across the page break.
- Mine: supported. Her word is 'processes'; 'directions' is a fair paraphrase of 'shifting from physical to digital … and from digital to physical'.
- **AGREE.**

### A6 summary

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 fatal | 1 | 0 | 0 | 1 |
| 2 named | 2 | 1 | 1 | 0 |
| 3 every fourth | 8 | 8 | 0 | 0 |
| 4 every sixth passed | 3 | 2 | 1 | 0 |
| Dispute row | 1 | 1 | 0 | 0 |
| **All** | **15** | **12** | **2** | **1** |

**DISAGREE.**

| Row | Auditor | Mine | Reason |
|---|---|---|---|
| S-175.1 | partial · fatal | partial · material | The 'contrary' hotel studies cut both ways: managers keep the formal decision, and Garcia et al. say machines 'hold real authority' (WP p. 7), with recommendations copied in 84 per cent of price changes; Spektor et al. report that 'In most implementations' the supplier's assignment is 'enforced'. The sentence is unsupported as written and survives as a hedged possibility with these sources. |

**Faults the auditor missed.**

1. S-175.1: Garcia WP p. 7 ('real authority') and p. 4 n. 6 (84 per cent), and Spektor 2025 §5.1.1 ('In most implementations'), all in texts the auditor opened, weigh against its own summary of the evidence.
2. S-168.2: the whole remark supports 'graded'; the proposed action would discard usable evidence.
3. S-156.2: the p. 1233 locator concerns brand consistency; pp. 1230 and 1235 concern movement.
4. S-173.2: Gursoy 2026: 155 is a hospitality source for what such systems hold.

**Disputes settled.**

- *The relay.* Credit Batat with the two names and with two processes that shape a customer's experience by shifting it from physical to digital and back (pp. 1230–1231, 1236). The relay of records and rulings is the paper's. The auditor's judgement stands.
- *Authority drifts to a vendor.* The studies are Garcia et al. (CESifo WP 10849) and Spektor et al. 2025. The verdict `partial` stands; `fatal` does not. I grade it material.

---

## Register A7: 'Three conditions and six questions'

### Rule 1: fatal row

**S-192.3** · 'neither a guest nor the staff at the desk could … reach the managers who held it' (dispute)
- Auditor: not in source (class 7) · fatal.
- Passages (Garcia et al., CESifo WP 10849, `garcia2026strategic/text.txt`).
  - Sample and setting, p. 9: 'an anonymous corporate sponsor, who is based in Europe and provides revenue management services to hundreds of independent hotels. The pricing and booking data come from 9 different hotels, eight of which are located at resort destinations … and one in an urban area'. p. 10: 'with about 50 rooms each, they are relatively small by international standards. According to private communication with the revenue management service, hotels are family-run and thus managing prices takes only a small fraction of a hotel manager's weekly workload.'
  - Who decides, p. 2: 'prices set by hotel managers (human manager)'. p. 10: 'The hotel manager decides every day whether to use the revenue management system to update prices. If she logs into the system, the dashboard displays for each room the current recommended price and the actual price. She then decides which price to update and by how much.'
  - The 'revenue manager' of the source is the supplier, p. 9: 'The hotels pay the revenue manager a fixed fee'.
  - Guests and staff: the strings guest, staff, desk, recepti, reach, contact, complain, owner and employee occur nowhere in the 2,728 lines. Consumers appear twice, as people who might dislike price changes (p. 18 n. 20; p. 25).
- Mine: not in source · fatal. I skimmed pp. 16–31, which the auditor only searched; they hold the model and the estimates and nothing on who can reach whom.
- **AGREE-WITH-NOTE.** The grade stands. The clause supplies a fact the study does not report, and the setting tells against it: nine family-run hotels of about fifty rooms, in which the person who sets the price is the hotel's own manager. 'On our reading' cannot carry it. It is the only premise for 'fails on accountability' (S-192.4), and S-197.1 leans on that verdict, so the pricing case cannot stand as a failure of the test. The grade is fatal to the case; no K claim rests on the case. The same source offers a true version of the point, and the auditor found half of it: the hotel's manager keeps the decision and the blame, while the machine holds 'real authority' (p. 7) and 'the designer of the algorithm largely escapes liability for poor advice' (p. 34). That split lies between the hotel and its supplier. Whether a guest can reach the manager is a question the study does not touch. I could not open the *Management Science* version (bot challenge); its Crossref abstract is word for word the working paper's.

### Rule 2: rows named for a second reader

**S-183.2** · the other two cannot make up for a missing accountability, since a guest 'has still been hosted by no one if no party is obliged to answer'
- Auditor: equivocal · material.
- Passages. v6, 'Delegation and standing' ¶5: 'the duty to the guest, and the answering for how it is performed, remain with the party that took the role up.' ¶6: 'the guest still holds standing, because the host's obligation persists'. Okhuysen and Bechky 2009: 490 (`okhuysenbechky2009/paged.txt`): 'in some situations, the relationship between these integrating conditions is one of substitution— common understandings can replace predictability and vice versa.'
- Mine: equivocal · material. On the paper's theory some party is always obliged to answer once the guest is received, so the antecedent is never true unless 'obliged' means assigned and reachable. The term changes sense between the theory and the rule.
- **AGREE.** The rule also departs from the source of the three names, as the auditor says, and v6 does not say so.

**S-186.q5** · 'Who must answer if it is disputed?'
- Auditor: equivocal · material.
- Mine: equivocal · material. Read as duty, the paper's proposal answers it for every touchpoint (the party that holds itself out, alongside the party in control). Read as assignment, it tests the arrangement. The cases apply it as reachability, which the question does not ask.
- **AGREE.**

**S-189.3** · 'an alternative is what gives a complaint its weight (Hirschman 1970)'
- Auditor: unverifiable · material.
- Passage: none. The card `hirschman1970exit` records `read_depth: metadata`. Open Library confirms the record (1970, Harvard University Press) and offers no open copy.
- Mine: unverifiable · material. What would settle it: the chapters on voice and on exit combined with voice, with a page, and whether Hirschman's exit covers a second channel inside one firm.
- **AGREE.**

**S-193.1** · a facial-recognition system that confirms identity 'does a clerical job (Boo and Chua 2022)'
- Auditor: partial (7, 6) · minor.
- Passage (Crossref abstract, re-fetched): 'Guests who stayed in four- or five-star hotels in Singapore were recruited … hotel guests performed calculative cognitive processes, weighing the benefits and risks of using facial recognition check-in system … risk perception was triggered by privacy concern.'
- Mine: partial (7, 6) · minor. The abstract shows that such systems exist and that guests were surveyed. 'Clerical' is the paper's.
- **AGREE.**

**S-198.1** · 'An employee often stands between the guest and the system'
- Auditor: supported (abstract only) · minor; 'Holds for reservation agents on the abstract's word. For other touchpoints it rests on S-171 to S-174'.
- Passage (Bendoly 2013, Crossref abstract, re-fetched): 'Given the risk of forecast error in certain reservation contexts, hotel agents are often given the latitude to accept rate bids below the pricing prescriptions of these systems.'
- Mine: **partial (5, 3; abstract only)** · minor. The sentence is general and uncited. The abstract speaks of reservation agents and rate bids, and its 'often' qualifies the latitude, not the employee's presence. v6's own rental case has no employee in the chain.
- **DISAGREE (verdict).** The auditor's note is a caution that changes what a reader takes, and the brief makes that a `partial`. A6 graded the twin of this sentence, S-171.1, `partial (no passage)`. Severity and action are unaffected.

**S-199.1** · reservation agents are often given latitude to accept bids below the system's prescriptions
- Auditor: supported (abstract only) · minor.
- Passage: as S-198.1.
- Mine: supported (abstract only) · minor. A background sentence of 2012–13, as the auditor says.
- **AGREE.**

**S-199.2** · 'in a laboratory experiment how far they used it depended on how they expected management to view their actions'
- Auditor: partial (6, 9, 1) · material.
- Passage (same abstract): 'The frequency and extent of such deviation is dependent in large part on the judgment of reservation agents, who in turn are influenced by their perceptions of how their actions will be viewed by higher levels of management. In this study, we use a laboratory experiment to investigate how different forms of continuous performance feedback influence agent decisions.'
- Mine: partial (6, 9) · material. The dependence on management's view is background. The experiment manipulates two forms of feedback, and the abstract reports no result ('The results suggest implications').
- **AGREE.**

**S-202.1** · 'Managers can use guests' reports to monitor and discipline staff (Fuller and Smith 1991)'
- Auditor: partial (2) · minor.
- Passage (Crossref abstract, re-fetched): 'This paper investigates how managers and employers use customer feedback to monitor, evaluate and discipline service workers.'
- Mine: partial (2; abstract only) · minor. 'Customer' and 'service firms'; no sample or sector.
- **AGREE.**

**S-202.2** · 'employees fall silent when speaking up looks futile (Morrison 2014)'
- Auditor: unverifiable · minor.
- Passage (Crossref abstract, re-fetched): 'I review the current state of knowledge about the factors and motivational processes that affect whether employees engage in upward voice or remain silent'. No factor is named. The publisher's PDF returned HTTP 403 with a bot challenge on my attempt as well.
- Mine: unverifiable · minor.
- **AGREE.**

**S-202.3** · frontline hospitality employees 'aware of artificial intelligence in their jobs report more silence'
- Auditor: partial (5, 2, 6) · material.
- Passage (Crossref abstract, re-fetched): 'concerns among frontline service employees about their future careers, namely, AI awareness … 355 frontline service employees in Chinese hotels using a two-wave survey … AI awareness increases frontline service employees' silence by prompting psychological contract breach.'
- Mine: partial (5, 2, 6) · material. The construct is worry about one's career, not knowledge that AI is in use; the effect is indirect.
- **AGREE.**

### Rule 3: every fourth of the other faulted rows

**S-179.1** · the test 'tells whether' the conditions survive
- Auditor: valid with added premise · material.
- Mine: valid with added premise · material. The six questions are open 'who' and 'what' questions and no sentence says which answers count as a condition present. Counter-model: all six answered, and the reader still cannot say.
- **AGREE.**

**S-182.2** · predictability 'from terms held steady enough to be negotiated'
- Auditor: invalid · material.
- Passages (v6). S-065: the duties are 'to receive, to sustain, to protect and to attend'. S-064: 'None of these sources makes a negotiated exception something the guest is owed'.
- Mine: valid with added premise, the premise being absent from the paper · material. The sentence promises a derivation from the host's duties and names a state of affairs. Counter-model: a hotel reprices daily and a duty manager answers every query.
- **AGREE-WITH-NOTE.** Fault, severity and action stand. The label is a matter of degree: one missing premise, a duty as to terms, would make the step valid, and the auditor is right that v6 states none. I do not offer a source for such a duty; that is for the readers of P4a.

**S-185.2** · the questions come 'in the order in which a claim would travel'
- Auditor: equivocal · minor.
- Passage (v6, S-171): 'from guest to employee to system to whoever configured the system'.
- Mine: partial (the description is not accurate) · minor. Q1 begins at the far end of that path, Q2 precedes any claim and Q6 concerns leaving.
- **AGREE-WITH-NOTE.** No term changes sense, so `equivocal` is the wrong label for a description that is simply off. Same severity, same action.

**S-188.1** · Q4 and Q5 'separate the power over the single case from the duty to answer for the rule'
- Auditor: equivocal · material.
- Passages (v6). Q4: 'Who can override it?' Q5: 'Who must answer if it is disputed?' In both 'it' is the outcome.
- Mine: equivocal · material. Q5 as worded concerns the outcome and S-188 says it concerns the rule. No question asks who can change the rule or whether the guest can reach anyone, and the verdicts at S-192 and S-195 turn on exactly those.
- **AGREE.**

**S-191.2** · 'in order to move managers who repriced too rarely'
- Auditor: partial (6, 8) · minor.
- Passages (Garcia WP). p. 3: 'The algorithm's designer has an incentive to offer recommendations that exaggerate the change in the optimal price to induce the human manager to update prices faster'. p. 5: 'We posit that the algorithm aims to induce revenue-maximizing decisions'. p. 11: 'Managers adjust prices only infrequently, on average, once every 35 days'.
- Mine: partial (6, 8) · minor. The infrequency is observed; the purpose is the model's posit.
- **AGREE.**

**S-192.5** · the regulators' guidance on differential pricing
- Auditor: partial (5) · material.
- Passages (Article 29 Working Party 2018, `wp29_2018adm/wp251.txt`). p. 22: 'Automated decision-making that results in differential pricing based on personal data or personal characteristics could also have a significant effect if, for example, prohibitively high prices effectively bar someone from certain goods or services.' p. 20: 'If a human being reviews and takes account of other factors in making the final decision, that decision would not be 'based solely' on automated processing.'
- Mine: partial (5, 7) · material. The sentence drops 'based on personal data or personal characteristics' and applies guidance on solely automated decisions to a price a manager sets from dates, weather and competitors' prices (WP p. 9).
- **AGREE.**

**S-195.3** · 'the app may answer the first three questions well'
- Auditor: valid with added premise · minor.
- Mine: valid with added premise · minor. The premise is the whole content, and Bosma studies hosts.
- **AGREE.**

**S-197.1** · 'Together the cases show that the questions separate touchpoints that decide something about the guest from those that decide nothing'
- Auditor: invalid · material.
- Mine: invalid · material. In each case v6 says whether the touchpoint decides before any question is put ('does a clerical job', 'would be deciding admission', 'decides nothing'), so the sorting is an input. The identity check decides something and is said barely to engage the questions. 'Show' breaks the stipulation at S-153.
- **AGREE.**

**S-201.2** · 'The translation is fragile'
- Auditor: valid with added premise · minor.
- Passage (Hatherley 2025: 7, `hatherley2025moving/user_pdf/fulltext.txt`): the user is likely 'to have developed a functional mental model of when to rely on the system's outputs and when to reject them. Once the model is updated, however, these expectations may be undermined, and the user's mental model may become outdated.' p. 1: 'high-stakes environments including healthcare, finance, and warfare'.
- Mine: valid with added premise · minor. Added: a desk employee's sense of what a system will accept is a mental model of that kind, and hotel systems are updated in that way. Hatherley's model is one of trust in outputs.
- **AGREE.**

### Rule 4: every sixth passed row

**S-179.2** · 'it measures neither satisfaction nor harm'
- Auditor: valid; 'No case in the batch reports satisfaction or harm.'
- Mine: valid as a stipulation about the six questions, none of which asks about either.
- **AGREE-WITH-NOTE.** The auditor's supporting remark is not accurate. S-192's third sentence weighs the pricing failure by a harm-like effect ('prohibitively high prices bar from a service'), and S-196 rests part of the restaurant case on diners' favourable reports ('the staff smiling'). The stipulation survives because stakes enter at the scoping step (Table 1) and not in the test, and v6 should say so.

**S-186.q1** · 'What rule or actor determined the outcome?'
- Auditor: valid.
- Mine: valid. It matches S-187's gloss ('whether the decision can be located at all'), and the restaurant case shows what an empty answer looks like.
- **AGREE.**

**S-195.2** · guests can arrive 'without meeting anyone in person' (Bosma 2022: 605)
- Auditor: supported.
- Passage (p. 605): 'the Host Assist program allows smart lock providers and other companies to integrate their services on the Airbnb platform, allowing guests to enter their holiday apartments without meeting anyone in person. To be eligible for business travelers, such a self-check-in option is required by Airbnb.'
- Mine: supported. Words exact, the author's own, version of record. On class 9: v6 joins the phrase to the eligibility rule with 'so that'; in the source 'such a self-check-in option' points back to the phrase, so the two still mean together what each means alone.
- **AGREE.**

### Dispute rows outside the rule

**S-192.1** · 'The final decision stayed with revenue managers, who could set the advice aside'
- Auditor: partial (1, 8) · material.
- Passages: as S-192.3.
- Mine: partial (1, 8) · material. The deciders are hotel managers of small family-run hotels; in the source 'the revenue manager' is the firm the hotels pay.
- **AGREE.** The mislabel is what lets S-192.3 read as plausible.

**S-192.2** · 'neither a guest nor the staff at the desk could anticipate the operative rule'
- Auditor: overgenerates · material.
- Mine: overgenerates, and valid only with an added premise the source does not give (that neither the recommendation nor the manager's response is disclosed to guests or desk staff) · material. On this reading every dynamically priced service fails predictability. Q2 asks about the outcome, which a guest sees as a quoted price before booking.
- **AGREE.**

**S-192.4** · 'so the touchpoint fails on predictability and on accountability'
- Auditor: invalid · material.
- Mine: invalid · material. It stands on S-192.2 and S-192.3, and no rule says what failing is.
- **AGREE.**

### A7 summary

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 fatal | 1 | 0 | 1 | 0 |
| 2 named | 10 | 9 | 0 | 1 |
| 3 every fourth | 9 | 7 | 2 | 0 |
| 4 every sixth passed | 3 | 2 | 1 | 0 |
| Dispute rows | 3 | 3 | 0 | 0 |
| **All** | **26** | **21** | **4** | **1** |

**DISAGREE.**

| Row | Auditor | Mine | Reason |
|---|---|---|---|
| S-198.1 | supported (abstract only) · minor | partial (5, 3; abstract only) · minor | A general, uncited sentence was passed on an abstract about reservation agents, with the limit written as a note. The brief makes such a note a `partial`. |

**Faults the auditor missed.**

1. S-198.1: a caution carried as a pass.
2. S-192.3: Garcia WP p. 7 ('machines hold real authority'), which with p. 34 gives the split the paper wants, between hotel and supplier. The auditor has p. 34 among its leads and not p. 7.
3. S-179.2: the statement that no case reports satisfaction or harm is wrong on S-192 and S-196.
4. Labels. `not in source` was given at S-192.3 without the full read the brief asks for; my skim of pp. 16–31 does not change it. Uncited suppositions are graded `valid with added premise` or `not in source` here and `partial (no passage)` in A6, so counts by verdict are not comparable across the two registers.

**Dispute settled: the hotel-pricing case.** The study's sample is nine family-run hotels of about fifty rooms, eight in resorts and one urban, all clients of one European revenue-management firm. The hotel's own manager holds the final pricing decision. The study says nothing of guests or desk staff. The fatal grade on S-192.3 stands.

---

## All three registers

| Rule | Rows | AGREE | AGREE-WITH-NOTE | DISAGREE |
|---|---|---|---|---|
| 1 fatal | 4 | 0 | 3 | 1 |
| 2 named | 16 | 12 | 3 | 1 |
| 3 every fourth | 29 | 23 | 6 | 0 |
| 4 every sixth passed | 8 | 5 | 3 | 0 |
| Dispute rows | 6 | 6 | 0 | 0 |
| **All** | **63** | **46** | **15** | **2** |

I agree with the auditor's finding in 62 of 63 rows and with the severity in 62 of 63; in two of the 62 (S-182.2, S-185.2) I would give the same fault a different label. In the eight rows passed outright I found no fault that should have failed a row; three carry a looseness worth a line. The one over-pass I found (S-198.1) was a `supported (abstract only)` row. Eight is a small sample, so the rate of over-passing is bounded loosely: none in eight among `supported` and `valid`, one in the three `supported (abstract only)` rows I saw.

## Overall judgment

These registers can be relied on for what a source says and where it says it: in 63 rows every passage I checked sits at its locator and says what the auditor reports, the inference verdicts survived my own counter-models, and I changed one verdict and one severity. They cannot be relied on, without a second look, for the top of the severity scale or for a summary of 'contrary evidence': the fatal on S-175.1 rests on a one-sided reading of two hotel studies that also say the machine holds 'real authority', whereas the fatals on A-4.1, S-015.1 and S-192.3 hold. Rows that rest on closed texts (six abstract-only sources, Hirschman, the published Garcia et al.) are exactly as open as the auditors left them, and the gap rows of A1 hold only in the narrowed forms set out above.
