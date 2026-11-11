<!-- Claim register, batch A1, run rr-2026-11-k, written by a Claude (Fable 5.2) subagent on 11 Nov 2026. -->

# Claim register A1: the Abstract and the Introduction

**Scope.** Sentence ids A-1 to A-6 and S-001 to S-026 of `manuscript/DRAFT_v6.md` (SHA-256 `8951cadf…537e7`, the hash frozen in K-D5). For every id the last 'As written' line of `rewrite_2026-11/sbs/LEDGER.md` matches the draft word for word (checked by script). The ledger's S-011 covers three sentences of v6; I label them S-011a, S-011b and S-011c.

**How I judged.** I judged each row from the source's own text, never from a card or a ledger 'Truth' line. I did not read `CORRECTIONS_2026-11-11.md`, `VERIFICATION.md`, anything under `manuscript/reviews/`, or `CALIBRATION_RESULT.md`. Class numbers are the brief's: 1 population, 2 setting, 3 strength, 4 speaker, 5 scope, 6 design, 7 application, 8 version, 9 combination. Passages are pasted from the saved text with its locator.

**Depth of reading, stated plainly.** For the open texts I read the passages that bear on each row and searched the whole file for terms that could refute it; I did not read every source cover to cover. Where a verdict would need a cover-to-cover read (`not in source`), I did not give it. The texts and what I read of each are listed under closing list 3.

**Paths.** Saved texts are under `manuscript/revision_2026-11/research/sources/<citekey>/` unless a row says `corpus/` (`manuscript/rewrite_2026-11/journal/corpus/<key>/`). Abstracts marked 'Crossref' or 'Semantic Scholar' were fetched from the API on 11 Nov 2026.

---

## Abstract

### A-1 · Abstract s1
> Hospitality firms now hand much of the work of hosting, from admission and pricing to check-in, room allocation and complaints, to algorithmic systems supplied by several firms at once.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| A-1.1 | Hospitality firms now hand much of the work of hosting to algorithmic systems | Empirical generalization (uncited here; rests on S-002 to S-004) | Garcia, Tolvanen and Wagner, CESifo WP 10849 (Dec 2023, 'accepted for publication in Management Science'), p. 2 (PDF p. 5), `garcia2026strategic/text.txt`; Boo and Chua 2022, Crossref abstract; Bosma 2022: 605 | Garcia p. 2: 'machines augment human decisions by acting as advisors to human managers who retain the final decision right'. Boo and Chua, abstract: 'A self-administered online questionnaire … Guests who stayed in four- or five-star hotels in Singapore were recruited'. | 3 ('hand' and 'much': the pricing source shows advice to a manager who decides); 6 (an adoption-intention survey and a platform's option stand in for observed practice) | partial | material | Say what the sources show: systems advise on price, check guests in and admit them to rentals. Drop 'much' or source it. |
| A-1.2 | The handed-over work runs 'from admission and pricing to check-in, room allocation and complaints' | Empirical generalization (uncited) | No source in v6 for admission, guest room allocation or complaints. Library searched (`grep` of `library/cards/` for room allocation or assignment, risk scoring, instant book, chatbot, complaint): the only room-assignment system carded assigns rooms to housekeepers (Spektor et al.), and the only study of 'decisions left to AI' is a survey of hoteliers' preferences (Ivanov and Webster 2024, abstract). | None. v6 itself calls its admission case 'a case we construct' ('Three conditions and six questions' ¶4). | 6; 7 (the paper's constructed admission case underwrites a statement of present fact) | partial | material | Cut the list to the instances sourced (pricing, check-in, entry to a rental) or add one observational source each for admission, room allocation and complaints. |
| A-1.3 | The systems are 'supplied by several firms at once' | Empirical generalization (rests on S-005) | Cobbe, Veale and Singh 2023, FAccT '23 proceedings p. 1187 (UCL copy of the version of record, `cobbe2023understanding_vor/vor.txt`; same text arXiv v2 p. 2) | 'Instead, they often now involve a group of organisations arranged together in a data-driven supply chain, each retaining control over component systems they provide as services to others.' | 2 (AI and cloud services in general; the paper names no hospitality system); 3 ('often now' becomes a flat statement); 7 (the application to hotels is the paper's) | partial | material | 'often supplied by several firms' and say the evidence comes from AI services at large; or cite a hospitality source. In Garcia the supplier is one 'independent revenue management company' (p. 2). |

### A-2 · Abstract s2
> Each places the party that decides at a distance from the guest it affects.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| A-2.1 | Every such system places the deciding party at a distance from the guest | Own inference (a universal drawn from the instances in S-002 to S-005) | Tested against the paper's own instances: Garcia WP pp. 2, 10; Bosma 2022: 605 | Garcia p. 10: 'hotels are family-run and thus managing prices takes only a small fraction of a hotel manager's weekly workload'; about 50 rooms each. Bosma p. 605: such changes 'help property owners to run an STR without having to be physically present'. | — | invalid | material | 'Each can place…' or 'Many place…'. The universal fails on the paper's first instance. |

- **Premises.** P1 (sourced, S-002): a revenue-management system recommends prices. P2 (sourced, abstract only, S-003): facial recognition checks identity at check-in. P3 (sourced, S-004): self-check-in lets a rental guest enter without meeting anyone. P4 (assumption): in each case someone other than a person the guest meets decides. C: each system places the party that decides at a distance from the guest.
- **Counter-model.** Garcia's own sample: the decider is the manager of a family-run hotel of about 50 rooms, who 'retain[s] the final decision right' (p. 2) and may stand at the desk. P1 is true and C is false.
- **Terms.** 'The party that decides' has no referent for a robot that greets or a lock that opens: nothing is decided about the guest. v6 itself later says of the projected chef that it 'decides nothing about the guest'.
- **Quantifiers.** 'Each' does not follow from four instances, one of which contradicts it.
- **Overgeneration / undergeneration.** Not a duty claim; not applicable.
- **K claim.** K9 (it is the factual ground for K9's 'what can fail is the channel').

### A-3 · Abstract s3
> The article begins from hospitality studies' account of what a host owes and argues, with the law of innkeepers as evidence, that the commercial host's obligation is a role obligation, imposed on whoever takes up the role of receiving travellers and taken up by holding out.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| A-3.1 | The article begins from hospitality studies' account of what a host owes | Signpost | — | — | — | — | — | It presupposes that such an account exists and covers commercial hosts; see S-008.1, S-009.1 and S-009.2. |
| A-3.2 | The commercial host's obligation is a role obligation, imposed on whoever takes up the role of receiving travellers | Own inference | Premises rest on rows in batches A2 and A3. Primary texts I checked for the test: Hotel Proprietors Act 1956 s 1(1) (`hpa1956/s1.txt`); Calye's Case, Coke's Reports Part VIII (1777 ed., saved OCR, `calye1584/`) | HPA s 1(1): 'An hotel within the meaning of this Act shall, and any other establishment shall not, be deemed to be an inn'. Calye: 'if the guest be beaten in the inn, the innkeeper shall not answer for it … the innholder ought to keep the goods and chattels of his guest, and not his person'. | — | equivocal (and undergenerates) | material | State the register of each step. Claim the role obligation for inns and hotels in the named jurisdictions; say that restaurants and rentals fall outside the admission duty. |
| A-3.3 | The role is 'taken up by holding out' | Own inference | HPA 1956 s 1(3), as quoted in v6 (batch A2 holds the row) | — | — | valid with added premise | minor | The added premise: the statutory test for an hotel ('held out by the proprietor') describes how every commercial host takes up the role. State it as the paper's reading. |

- **Premises (A-3.2).** P1 (sourced, customary register; S-009, S-027 to S-036): hospitality scholars hold that a host protects and provides for the guest. P2 (sourced, legal register; batch A2): English and United States common law laid duties on whoever kept a common inn, whatever the motive. P3 (assumption): the duties in P2 are the obligation in P1. P4 (assumption): what the law laid on innkeepers it lays on 'the commercial host'. C: the commercial host's obligation is a role obligation imposed on whoever receives travellers.
- **Counter-model.** A restaurant or an Airbnb host. P1 and P2 are true. No law imposes a duty to receive on either (HPA 1956 s 1(1): no other establishment is an inn; v6 itself reports the shopkeeper 'free to refuse'). C is false of them.
- **Terms.** 'Obligation' is customary in P1 and legal in P2. The contents differ: P1's obligation is to protect the guest from harm (S-009); the innkeeper's strict duty covered goods 'and not his person' (Calye). 'Imposed' is a legal word; A-3 does not say 'by law', though the Conclusion does.
- **Quantifiers.** 'The commercial host' (all) from innkeepers and statutory hotels (some).
- **Overgeneration.** Yes: the same form of argument fits carriers, banks, any service provider under the Equality Act, and hospitals under EMTALA. v6 concedes it ('not this mechanism, which is general').
- **Undergeneration.** It fails for a restaurant, for a short-term rental in the host's home (v6's own limit), and for a guest placed and paid for by a third party, who is not the 'traveller … able and willing to pay' of s 1(3).
- **K claim.** K2 and K3. v6 is stronger than K3: it lets the role, through the law, bind; K3 says the role specifies and three outside grounds bind. It also merges K4's two tiers (admission and reception).

### A-4 · Abstract s4
> It then asks what becomes of that obligation when the work is handed on: the work can be delegated and the duty cannot, so the guest's standing survives, but its exercise depends on a reachable party with authority to change the decision.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| A-4.1 | The work can be delegated and the duty cannot | Own inference resting on a legal proposition | Woodland v Essex County Council [2013] UKSC 66, UK Supreme Court (appeal from England and Wales), Lord Sumption for the majority, paras 7, 22, 24, 25(3) (`woodland2013uksc/woodland.txt`); Occupiers' Liability Act 1957 s 2(4)(b) (`ola1957/s2.html`). Later treatment not checked. | Para 7: 'The work required to perform such a duty may well be delegable, and usually is. But the duty itself remains the defendant's.' Para 22: 'Non-delegable duties of care are … exceptional.' Para 24: 'as a general rule he is not liable for the contractor's negligence.' | — | invalid | fatal | State it per duty, as K8 does. The abstract drops the body's own hedge ('we borrow its structure without claiming that the law already places hotels in its category'). |
| A-4.2 | So the guest's standing survives | Own inference | — | — | — | valid with added premise | minor | Added premises: the definition of standing held (the guest's position as the one to whom the duties are owed), which the abstract does not give, and A-4.1. A reader will take 'standing' as a power to press a claim. |
| A-4.3 | Its exercise depends on a reachable party with authority to change the decision | Own inference | — | — | — | valid with added premise | material | Added premise: pressing a claim counts as exercise only if it can still change the outcome. Say so, or the sentence is false of a claim pressed afterwards for damages. |

- **Premises (A-4.1).** P1 (sourced): for the second category of non-delegable duty the work is delegable and the duty stays (Woodland para 7). P2 (assumption): the commercial host's duty to the guest belongs to that category. C: the host's work can be delegated and its duty cannot.
- **Counter-model.** An hotel is also an occupier. Under s 2(4)(b) it 'is not to be treated without more as answerable for the danger if in all the circumstances he had acted reasonably in entrusting the work to an independent contractor' and checked the contractor's competence and the work. P1 is true; for this duty and this delegate C is false. Woodland para 25(3) adds that a party whose duty is 'only to arrange for its performance' is not liable; v6 quotes it.
- **Terms.** 'The duty' is singular in A-4 and plural in the body (to receive, to keep goods, to take care, to perform the contract). The claim is true of some (the innkeeper's liability for goods; the contract with a paying guest, cf. para 7: the contracting party 'will normally be taken to contract that the work will be done carefully by whomever he may get to do it') and false of others.
- **Quantifiers.** A universal ('the duty cannot') from an exceptional category whose first feature is a claimant who is 'a patient or a child, or for some other reason … especially vulnerable or dependent' (para 23(1)).
- **Overgeneration.** Yes, for any firm with customers; Woodland itself warns against 'the exception … eating up the rule' (para 22).
- **Undergeneration.** A placed guest has no contract with the hotel; a restaurant has no innkeeper's liability.
- **K claim.** K8. v6 states universally what K8 states per duty, and DECISIONS_K (K-D1) already records the universal as false of English law.
- **Premises (A-4.3).** P1 (stipulation, section 3): standing exercised is 'the guest's pressing of that claim … on a party able to receive it'. P2 (assumption): only a party with authority to change the decision is able to receive it. C: exercise depends on a reachable party with such authority.
- **Counter-model.** A guest sues afterwards and recovers damages. The claim was pressed on a party able to receive it; nobody with authority to change the decision was reachable at the time.
- **Terms.** 'Able to receive' (the definition) becomes 'with authority to change the decision' (the abstract). 'Depends on' describes; it lays no duty on the host to supply such a party.
- **K claim.** K7, by the second route (from the guest's standing), which K7 keeps only as support. K6.

### A-5 · Abstract s5
> It offers a test of phygital touchpoints, scoped by the type of decision, and a roadmap for organizations.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| A-5.1 | The article offers a test, scoped by type of decision, and a roadmap | Signpost | — | — | — | — | — | None. |

### A-6 · Abstract s6
> We argue that what algorithmic mediation removes is rarely the host's obligation and more often the guest's path to anyone with authority to answer for it.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| A-6.1 | Algorithmic mediation rarely removes the host's obligation | Own inference | Rests on A-3.2 and A-4.1 | — | — | valid with added premise | material | Added premise: every duty of the host stays with the holder when a system does the work. A-4.1 does not establish it. Name the exception K9 names: a system that decides admission can prevent the duty from arising. |
| A-6.2 | It more often removes the guest's path to anyone with authority | Own inference with a claim of frequency | No frequency evidence in v6. Conclusion ¶4: 'We found no such study in hotels, restaurants or bars'; section 4 ¶1: cases 'illustrate the distinctions rather than test them'. | — | — | invalid | material | Replace the frequencies with the modal claim the Conclusion makes: mediation 'leaves the obligation in place and takes away, where it takes anything, the guest's path'. |
| A-6.3 | The party sought has 'authority to answer for' the obligation | Definition in use | v6 section 3 ¶2 stipulates authority as 'the power, assigned by an organization, to change a decision or the rule behind it' | — | — | equivocal | minor | 'Authority to answer for it' joins the two things the paper separates (authority; answerability). Write 'anyone who can change the decision and must answer for it'. |

- **Premises (A-6.1, A-6.2).** P1 (earlier inference, A-3.2): the obligation attaches to the role-holder. P2 (earlier inference, A-4.1): handing on the work does not move the duty. P3 (assumption): using an algorithmic system is handing on work. C1: mediation does not remove the obligation. P4 (assumption, empirical): in phygital arrangements the party with authority is often out of the guest's reach. C2: what mediation removes is more often the path than the obligation.
- **Counter-model.** A hotel whose pricing system only advises a manager at the desk (Garcia). The obligation stays and so does the path. C2's 'more often' is a count; nothing in the premises counts anything.
- **Terms.** 'Authority' (see A-6.3). 'Answer' means explain and justify to a forum in section 3 (Bovens); here it means holding the duty.
- **Quantifiers.** 'Rarely' and 'more often' do not follow: P1 to P3 are conceptual and P4 rests on illustrations.
- **Overgeneration.** The argument proves the same of banks and online retail; v6 concedes that inaccessible decision-makers 'trouble banking and online retail as much as hospitality'.
- **Undergeneration.** Before reception a system that refuses admission removes the occasion for the duty (K9); a placed guest and a restaurant diner fall outside A-3.2.
- **K claim.** K9, with K7.

---

## Introduction

### S-001 · Introduction ¶1
> Phygital hospitality hands much of the work of hosting, from admission and pricing to check-in, room allocation and complaints, to systems and firms that the guest rarely sees.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-001.1 | Phygital hospitality hands much of the work of hosting, from admission to complaints, to systems and firms | Empirical generalization (uncited; S-002 to S-005 are its instances) | As A-1.1 and A-1.2 | As A-1.1 and A-1.2 | 3; 6; 7 | partial | material | As A-1.1 and A-1.2. 'Phygital' is never defined in the Introduction, and a revenue-management recommender that no guest meets is not phygital in the sense of Batat 2024: 1230 ('how customers navigate through digital spaces and physical places'). |
| S-001.2 | The guest rarely sees those systems and firms | Empirical generalization (uncited) | No source. Belanche et al. 2020: 273 and Bosma 2022: 605 bear on it. | Belanche p. 273: 'Connie is a robot concierge introduced by Hilton, able to inform guests…'. Bosma p. 605: 'smart lock providers and other companies … integrate their services on the Airbnb platform'. | 3 (true of vendors, false of the robot and the kiosk, which the guest meets) | partial | minor | 'to systems the guest may meet and firms the guest rarely sees'. |

### S-002 · Introduction ¶1
> Revenue-management systems recommend the price a guest is quoted (Garcia et al. 2026).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-002.1 | Revenue-management systems recommend the price a guest is quoted | Paraphrase | Garcia et al., CESifo WP 10849, pp. 9 and 11 (PDF pp. 12, 14). The reference list gives Management Science 72(1), which I did not read; its Crossref record (10.1287/mnsc.2022.03740, pp. 609–626) exists. | p. 9: 'We observe for each room and each possible arrival day the flow of bookings, the recommended price by the revenue management service and the actual price charged by the hotel.' p. 11: 'Managers adjust prices only infrequently, on average, once every 35 days'. | 3 (in its paragraph the sentence reads as work handed to a system; the source shows a manager who sets the price and often leaves the recommendation unused); 8 (working paper read, journal version cited) | partial | minor | 'recommend prices to hotel managers, who set the price a guest is quoted'. Sample: nine hotels, clients of one European firm (p. 9). |

### S-003 · Introduction ¶1
> Facial-recognition systems verify identity at check-in (Boo and Chua 2022), and service robots greet, direct and serve guests; in vignette experiments, respondents held the firm more responsible when a robot rather than an employee failed (Belanche et al. 2020).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-003.1 | Facial-recognition systems verify identity at check-in | Paraphrase | Boo and Chua 2022, IJCHM 34(11): 4052–4079, Crossref abstract only. Closed (Unpaywall, OpenAlex, Semantic Scholar: no open copy). | 'Results showed that hotel guests performed calculative cognitive processes, weighing the benefits and risks of using facial recognition check-in system.' | — | supported (abstract only) | minor | The abstract supports only that such a check-in system exists and that guests' intentions towards it were surveyed in Singapore. It says nothing of how widely hotels use it. Read the article or cite a source on deployment. |
| S-003.2 | Service robots greet, direct and serve guests | Empirical generalization (uncited; nearest text is Belanche) | Belanche et al. 2020, JOSM 31(2), version of record, pp. 268, 273 (`belanche2020/user_pdf/fulltext.txt`) | p. 273: 'robots are starting to be implemented to attend customers at several hotels worldwide. For example, Connie is a robot concierge introduced by Hilton, able to inform guests about nearby places of interest'. p. 268: 'robot waiters seem to have taken off at some restaurants in China'. | 3 ('starting to', 'seem to', 'some' dropped; 'greet' appears only in the authors' own vignette, Appendix 1) | partial | minor | 'service robots have begun to direct and serve guests in some hotels and restaurants', with the pages. |
| S-003.3 | In vignette experiments, respondents held the firm more responsible when a robot rather than an employee failed | Case description (study) | Belanche et al. 2020: Study 1 (hotel reception, 331 US participants, p. 273), results pp. 275–277; Study 2 (restaurant, 229 US participants, p. 278), results pp. 280–281 | pp. 276–277: for 'the hotel's responsibility … the effect of human vs. robot is only significant for the service failure condition (F_FAILURE = 3.97; p < 0.05 …)'. p. 281: firm responsibility 'in the analytical robot condition also did not differ from the frontline employee condition (… t = 1.24, p > 0.10)'. | 3 ('experiments', plural: in Study 2 the difference held for the mechanical robot only, t = 2.13, p < 0.05, and pooled at p < 0.10) | partial | minor | 'in a vignette experiment set at a hotel reception … ; a second, set in a restaurant, found it only for a robot described as mechanical'. Population and design are stated correctly. |

### S-004 · Introduction ¶1
> In short-term rentals, self-check-in replaces the handover of keys (Bosma 2022: 605).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-004.1 | In short-term rentals, self-check-in replaces the handover of keys | Paraphrase | Bosma 2022, EPA 54(4), version of record, p. 605; cf. p. 602 (`bosma2022platformed/b.txt`) | p. 605: 'the Host Assist program allows smart lock providers and other companies to integrate their services on the Airbnb platform, allowing guests to enter their holiday apartments without meeting anyone in person. To be eligible for business travelers, such a self-check-in option is required by Airbnb.' | 3 ('allows' and a condition for one listing category become 'replaces'); 5 (one platform; on p. 602 a host 'always met guests in person to hand over the keys') | partial | minor | 'self-check-in can replace the handover of keys, and Airbnb requires it of listings for business travellers'. Locator correct. |

### S-005 · Introduction ¶1
> Behind each of these stands a chain of vendors, none of whom the guest meets (Cobbe et al. 2023).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-005.1 | Behind each of these systems stands a chain of vendors | Paraphrase | Cobbe et al. 2023, proceedings p. 1187 | 'Instead, they often now involve a group of organisations arranged together in a data-driven supply chain, each retaining control over component systems they provide as services to others.' | 2 (AI services in general, no hospitality case); 3 ('often now' becomes 'each'); 7 | partial | material | 'Such systems are often assembled from services that several firms supply (Cobbe et al. 2023: 1187)'. A-1.3, S-013 and S-021 lean on this row. |
| S-005.2 | None of those vendors meets the guest | Own application, cited to Cobbe | Cobbe et al. 2023, p. 1193. I searched the full text for end-user, affected, visib-, see, customer and public, and read each hit. | p. 1193: 'the accountability horizon – the point beyond which an actor cannot 'see', which depends on the actor and the chain.' The horizon is what one supplier can see of another; 'customers' are the firms that buy AI services. | 7 (the paper's own observation carries the source's citation) | partial | minor | Move the citation to the first clause and own the second: 'and the guest meets none of them'. |

### S-006 · Introduction ¶1
> We call software that takes or shapes a decision about a guest an algorithmic system; the guest, the staff, the property, the firms and the systems together, a phygital arrangement; and any moment at which the guest meets that arrangement, a touchpoint.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-006.1 | Algorithmic system: software that takes or shapes a decision about a guest | Definition | — | — | — | equivocal | minor | Uses in another sense, listed below. |
| S-006.2 | Phygital arrangement: guest, staff, property, firms and systems together | Definition | — | — | — | valid | — | Used once more in the batch ('that arrangement') in the same sense. |
| S-006.3 | Touchpoint: any moment at which the guest meets the arrangement | Definition | — | — | — | valid | — | A-5, S-017 and S-021 use it in this sense. Outside the batch, Batat's 'touchpoints' are channels; a later auditor should check section 4. |

- **Uses of 'algorithmic system' in another sense.** S-005 and S-007 ('each of these', 'each takes over … and places the party who decides'): the robot that greets (S-003) and the lock that opens (S-004) take or shape no decision about a guest. S-011b ('such systems'): the cited works speak of automated social presence, AI-based service encounters and phygital strategy, none of them defined by a decision about a guest. S-025 ('such systems'): machines in general.
- **Undefined in the batch.** 'Phygital' (S-001), 'standing' (A-4, S-016, S-017, S-020), 'authority' (A-4, A-6, S-018) and 'holding out' (A-3) are used before the sections that define them.

### S-007 · Introduction ¶1
> The technologies and their jobs differ across hotels, restaurants and rentals, but each takes over part of what a host once did in person and places the party who decides at a distance from the guest it affects.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-007.1 | The technologies and their jobs differ across hotels, restaurants and rentals | Own inference (summary of S-002 to S-004) | — | — | — | valid | — | The paragraph's only restaurant instance is Belanche's second vignette. |
| S-007.2 | Each takes over part of what a host once did in person | Own inference | — | — | — | valid with added premise | minor | Added premise: pricing, checking identity, greeting and handing over keys were once the host's work in person. |
| S-007.3 | Each places the party who decides at a distance from the guest it affects | Own inference | As A-2.1 | As A-2.1 | — | invalid | material | As A-2.1. |

- **S-007.3.** Premises, counter-model, terms and quantifier as under A-2.1. K claim: K9.

### S-008 · Introduction ¶2
> Hospitality scholars have long resisted a definition of hospitality as the provision of food, drink and a bed, and the founding editors of this journal set out to study it as a lens on social relations and power (Lynch et al. 2011).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-008.1 | Hospitality scholars have long resisted a definition of hospitality as the provision of food, drink and a bed | Paraphrase | Lynch et al. 2011, H&S 1(1): 3–24, accepted-manuscript copy without journal pages (`corpus/lynch2011/plain.txt`), Introduction ¶3 | 'the definition that tends to dominate public and academic discourse on the topic is one based on organizational practices and the provision of food, drink and accommodation. Such a definition, whilst useful, is limited as it fails to address the essence of hospitality'. | 3 ('long' and the generic 'hospitality scholars' are not in the source); 4 (the editors criticize the definition in 2011; they report that it dominates academic discourse and call it 'useful') | partial | minor | 'The founding editors of this journal judged the dominant definition, the provision of food, drink and accommodation, too narrow'. This passage narrows K1: the editors themselves report that the field's prevailing definition names no duty. |
| S-008.2 | The founding editors set out to study hospitality as a lens on social relations and power | Paraphrase | Lynch et al. 2011, same copy, 'An agenda for hospitality studies' ¶1–2 | 'Hospitality is, as Lashley, Lynch and Morrison (2007) suggest, a social lens. … we see hospitality as both a condition and an effect of social relations, spatial configurations and power structures.' | — | supported | — | Add the page from the printed article if a locator is wanted; the saved copy has none. |

### S-009 · Introduction ¶2
> On that view the host owes the guest more than a service, and Shryock's good host is one able to 'protect guests from harm' (2012: S20).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-009.1 | On the editors' view the host owes the guest more than a service | Own inference presented as the source's view | Lynch et al. 2011, same copy, Introduction ¶2 | 'In these traditions, hospitality entailed a sacred obligation not just to accommodate the guest, but to protect the stranger who arrived at the door.' ('These traditions' are the 'Greek and Roman or Enlightenment antecedents' of historical accounts, cited to O'Gorman 2007 and Still 2006.) | 4 (the editors report what historians say of ancient traditions; their own 'lens' states no duty of hosts); 5 (a sacred duty to the stranger at the door becomes what 'the host owes the guest', commercial hosts included) | partial | material | 'The editors recall that in the Greek, Roman and Enlightenment traditions hospitality was a sacred obligation to protect the stranger'. v6 already says this accurately at S-031; the Introduction should not say more. |
| S-009.2 | Shryock's good host is one able to 'protect guests from harm' | Quotation | Shryock 2012, JRAI 18(S1), publisher-typeset copy, p. S20; cf. p. S31 (`shryock2012breaking/plain.txt`) | S20: 'The man who is karim (hospitable, generous, noble) is able to feed others, project an honourable and enviable reputation, and protect guests from harm. Hospitality, as Bedouin describe it, is a quality of persons and households, of tribal and ethnic groups'. | 2 (Balga Bedouin, Jordan; the sentence names no setting); 4 ('as Bedouin describe it'); 5 and 9 (an ability that tests sovereignty is joined to 'owes'; the source says the Balga 'would never confuse karam with the hospitality offered to tourists', S31) | partial | material | Words and page are exact. Add the setting ('among the Balga Bedouin of Jordan') and keep 'is able to' apart from 'owes'. Shryock is a defeater as much as a support: at S31 he calls host–guest relations in commerce 'depersonalized, formulaic, monetized'. |

- **S-009.1 as inference.** P1 (sourced): the editors study hospitality as a lens on social relations and power. P2 (sourced, reported speech): historians describe an ancient sacred obligation to protect the stranger. C: on the editors' view the host owes the guest more than a service. C does not follow from P1; from P2 it follows only for the traditions named. Customary register. K claim: K1, in its weakest form (a source 'that describe[s] an ideal and do[es] not claim that hosts are bound').

### S-010 · Introduction ¶2
> This journal has studied platforms since its first volume: Bialski (2012: 257) found that a hospitality network's profiles gave hosts 'the power to choose one member over the other', Germann Molz (2018: 244) described Airbnb using its status as a platform to evade legal responsibility, and later work describes guests without hosts and an algorithmic hostility towards food-delivery workers (Germann Molz 2026; Riordan 2024).

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-010.1 | This journal has studied platforms since its first volume | Paraphrase | Bialski, H&S 1(3): 245–260 (Crossref 10.1386/hosp.1.3.245_1, issued 16 Feb 2012; typeset proof, `corpus/bialski2012/body.txt`) | Header: 'Hospitality & Society Volume 1 Number 3'. Abstract: 'New technologies in use today like CouchSurfing.com are allowing people to create…'. | — | supported | — | The platform is a non-commercial network; the sentence says 'hospitality network', which is right. |
| S-010.2 | Bialski found that a hospitality network's profiles gave hosts 'the power to choose one member over the other' | Quotation | Bialski 2012: 257 | 'The online profile offers hosts the power to choose one member over the other – and the host chooses the visitor (and vice versa) based on the perceived ease of interaction.' | — | supported | — | None. Bialski calls this a 'fantasy of control' on the same page; the sentence does not need it. |
| S-010.3 | Germann Molz described Airbnb using its status as a platform to evade legal responsibility | Paraphrase (close to quotation) | Germann Molz 2018, H&S 8(3), version of record, p. 244 (`corpus/germannmolz2018/plain.txt`) | 'The Community Commitment to anti-discrimination was a preemptive move that brings into stark relief the lengths to which Airbnb goes to use its status as a digital platform to evade legal responsibility.' | — | supported | — | None. The responsibility in question is under anti-discrimination and tax law. |
| S-010.4 | Later work in the journal describes guests without hosts | Paraphrase | Germann Molz 2026, H&S 16(1): 63–82, Crossref abstract only. Closed. | 'This article uses the concept of guests without hosts to explore digital biopolitics in hospitality … Originally conceived to describe the blurring of hosting and guesting practices in network hospitality'. | — | supported (abstract only) | minor | The abstract reads the phrase two ways, as 'an inhospitable form of institutional and algorithmic governance' and as 'a potential model of collaborative sociality'. Nothing beyond the abstract may be said. The full text is the nearest neighbour in the target journal and could defeat S-011c.3, S-023 and A-6; see closing list 3. |
| S-010.5 | Later work describes an algorithmic hostility towards food-delivery workers | Paraphrase | Riordan 2024, H&S 14(3): 277–299, Crossref abstract only. Closed. | 'this article introduces the concept of algorithmic hostility to demonstrate how platforms, restaurant staff, customers and others utilize digital technologies and existing social divisions to exploit contingent workers'. | — | supported (abstract only) | minor | None beyond obtaining the text. |

### S-011 · Introduction ¶2 (three sentences in v6)
> (a) Phygital operation may now be the normal condition of services (Brochado et al. 2026). (b) The literature on it presents such systems as means to a smoother and more personal experience (Batat 2024) and describes them by what they do, as social presences, mediators, facilitators and co-creators (van Doorn et al. 2017; Li et al. 2021; Xing and Zhang 2026). (c) Where it turns to governance, it calls for human-first design and contestable rules (Batat 2026; Shabnam et al. 2026), without saying to whom these safeguards are owed or which of the firms behind a system owes them.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-011a.1 | Phygital operation may now be the normal condition of services | Paraphrase | Brochado et al. 2026, J. Services Marketing (online first, pp. 1–20), Crossref abstract only. Closed. | 'This study aims to explore how recent research has reflected the evolving role of phygital strategies in services marketing … The review covered 105 papers from the Scopus database'. | — | unverifiable | minor | The title asks 'Is phygital the new normal?'; the abstract does not answer it and reviews research, not operations. The full text would settle it. Until then cite the title's question as a question, or drop the sentence. |
| S-011b.1 | The phygital literature presents such systems as means to a smoother and more personal experience | Paraphrase | Batat 2024, J. Strategic Marketing 32(8), version of record, pp. 1220, 1223, 1230 (`batat2024phcx/user_pdf/fulltext.txt`) | p. 1220: 'This is done by fluidifying the journeys of customers from online to offline and inversely, along with capturing consumers' values and responding to their tangible needs … and their intangible needs (e.g., their emotional needs).' | 5 (Batat's subject is the phygital strategy and its connectors, not software that decides about a guest); 3 ('more personal': 'personalized services' appears on p. 1223 as a benefit others claim for multichannel strategies) | partial | minor | 'presents the phygital journey as one to be made fluid (Batat 2024: 1220, 1230)'. |
| S-011b.2 | It describes them as social presences | Paraphrase | van Doorn et al. 2017, J. Service Research 20(1), published PDF, p. 43 (`vandoorn2017domo/text.txt`) | 'it introduces the novel concept of automated social presence (ASP; i.e., the extent to which technology makes customers feel the presence of another social entity) to the services literature.' | 5 (service research of 2016–17; the word 'phygital' does not occur in the article) | partial | minor | Write 'service research' for this source, not 'the literature on [phygital operation]'. |
| S-011b.3 | … as mediators and facilitators | Paraphrase | Li et al. 2021, IJHM 95, 102930, abstract only (Semantic Scholar; Crossref carries none). Closed. | 'the study identified 4 modes of AI technology-based service encounters: AI-supplemented, AI-generated, AI-mediated, and AI-facilitated encounters.' | — | supported (abstract only) | minor | The abstract names kinds of encounter, not kinds of system; 'mediators, facilitators' is a fair noun for them. Same scope note as S-011b.2. |
| S-011b.4 | … and as co-creators | Paraphrase | Xing and Zhang 2026, IJCHM 38(4): 1433–1452, title and Crossref abstract only. Closed. | Title: 'The algorithmic guest: AI as a co-creator in customer experience management'. The abstract does not use the word. | — | supported (abstract only) | minor | The support is the title alone. Read the article or drop the citation. |
| S-011c.1 | Where the literature turns to governance it calls for human-first design | Paraphrase | Batat 2026, J. Services Marketing 40(4): 505–518, Crossref abstract only. Closed. | 'proposes a human-first logic grounded in "phygital phenomenology" by integrating technology without compromising experiential authenticity.' | — | supported (abstract only) | minor | None beyond obtaining the text. |
| S-011c.2 | … and for contestable rules | Paraphrase | Shabnam et al. 2026, J. Services Marketing, published-online version, PDF p. 14, §7.2 (`shabnam2026tpsr/user_pdf/fulltext.pdf`) | 'Secondly, algorithmic governance must remain contestable. Digitally enforced rules should incorporate escalation pathways and human oversight to prevent rigid exclusion.' | — | supported | — | None. |
| S-011c.3 | The literature does not say to whom these safeguards are owed or which of the firms behind a system owes them | Gap claim | Tested on Shabnam et al. 2026 (full text saved; I read §2 and §7 and searched the rest), Batat 2026 (abstract), the library, and the queries in closing list 4. Defeater texts read: Sharma and Mattila 2026, JHTR 50(6): 911, 915; Gursoy 2026, JHMM 35(2): 155–156, 160 (both saved, neither cited in v6). | Sharma and Mattila p. 911: 'who should be blamed? The restaurant company, the robotic manufacturer who provided the robot, or the algorithm creators who made it? Or was the manager on duty responsible…?' Gursoy p. 160: 'Algorithmic governance shifts authority from interpersonal judgment to computational logics, raising questions about accountability when harm, bias, or exclusion arise'. | — | partial | material | The gap survives only in a narrow form. Rewrite as: 'I found no work that states a duty owed to the guest or allocates it among the firms behind a system [databases, queries, date]', and engage the two papers that pose the question. Detail below. |

- **S-011c.3, what the texts say.** Shabnam et al. address 'managers' and 'organisations' ('organisations should prioritise transparent artefact design', PDF p. 14) and policymakers, and name the beneficiary ('advancing consumer well-being'). They state no duty owed to the customer and do not divide the task among several firms. So 'without saying to whom … or which of the firms' is true of duty and of allocation, and misleading if read as 'the literature names neither an actor nor a beneficiary'.
- **Limits of the evidence.** One of the two governance sources was read only in abstract, so its silence is unknown. 'The phygital literature' in (b) is built from service-robot and AI-encounter papers; on that same wide reading, hospitality papers on AI belong to it, and two of them ask the 'which party' question in terms of blame and liability (Sharma and Mattila 2026: 911, 915) or say that AI 'shifts responsibility' and 'authority' (Gursoy 2026: 155–156, 160). Neither answers it, and neither grounds it in what a host owes. That is the gap the paper can claim.
- **Unread leads that could close the gap further** (records fetched, texts not read): Wirtz, Kunz, Hartley and Tarbit 2022, 'Corporate digital responsibility in service firms and their ecosystems', J. Service Research 26(2): 173–190; Kunz and Wirtz 2026, 'Corporate digital responsibility in tourism and hospitality', in *The Ethics of AI in Hospitality and Tourism*, pp. 57–71; Gustafsson 2026, 'Unmanned, not unmanaged', J. Services Marketing. See closing list 5.

### S-012 · Introduction ¶2
> Algorithmic-accountability research looks for answerability among those who design or deploy a system and ties it to harm (Nissenbaum 1996; Kong 2026: 5), and hospitality research measures hospitableness as a motive of individual hosts (Lashley 2015: 1), so the host's obligation is sought either in an injury or in a person's motive.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-012.1 | Algorithmic-accountability research looks for answerability among those who design or deploy a system | Paraphrase | Nissenbaum 1996, author's preprint (18 pp., not journal pages), pdf p. 11 (`nissenbaum1996accountability/author_preprint.txt`); Kong 2026, AI and Ethics 6:518, version of record, p. 5 (`kong2026delegation/user_pdf/fulltext.pdf`) | Nissenbaum: 'working out new lines of accountability may point to designers of the system, the human experts who served as sources, or the organization that chooses to put the system to use.' Kong p. 5: answerability 'is relocated to the prior act of delegation: the choice of objective, the choice of constraints, and the choice to release the process'. | — | supported | — | None. Kong's locator is right. Nissenbaum has no page in v6; a journal page (25–42) would need the printed article. |
| S-012.2 | … and ties it to harm | Paraphrase used as a characterization of a field | Nissenbaum pdf p. 2; Kong pp. 3, 5. Against: Lyons, Velloso and Miller 2021 (in v6's reference list), arXiv copy p. 3, §2.1 (`lyons2021conceptualising/arxiv.txt`). | Nissenbaum: accountability 'specifically for the harms and risks of faulty and malfunctioning systems'. Kong p. 5: 'A gap is genuine only when the harmful disposition the agent expressed was not a foreseeable property of the deployment specification'. Lyons et al.: the ability to contest 'is an important way to uphold human dignity and autonomy'. | 3 and 5 (true of the two works cited; widened to 'algorithmic-accountability research') | partial | material | 'Nissenbaum (1996) and Kong (2026: 5) tie answerability to harmful outcomes'. Work the paper itself cites grounds contestation in dignity and autonomy (Lyons et al.), and GDPR art. 22, as v6 itself paraphrases it, turns on legal or similarly significant effects, not harm (I did not re-read the Regulation for this row). Kong also grounds answerability in a role taken up (p. 3: 'provided one occupied a role, undertook a task, or created a risk'), which is close to the paper's own move and should be credited. |
| S-012.3 | Hospitality research measures hospitableness as a motive of individual hosts | Paraphrase used as a characterization of a field | Lashley 2015, RHM 5(1), published PDF, p. 1 (`lashley2015hospitality/paged.txt`). Against: Pijls et al. 2017, IJHM 67: 125–126; Tasci, Aktas and Acikgoz 2021, THM 27(2): 341 (open copy saved this session, `tasci2021cultural/`). | Lashley p. 1: 'a research instrument that can be used to identify those individuals who are driven by a personal desire to be hospitable to others.' Tasci et al. p. 341: 'most studies measured hospitableness and hospitality at the firm level'. Pijls et al. p. 126: a scale that 'includes the experience of hospitality offered by the organization as a whole'. | 3 (one instrument stands for 'hospitality research'; other scales measure providers' behaviour as guests perceive it, or the organization's hospitality) | partial | minor | 'Lashley's instrument measures hospitableness as a motive of individuals (2015: 1)'. Locator correct. |
| S-012.4 | So the host's obligation is sought either in an injury or in a person's motive | Own inference | Lashley 2015: 3, 4 | p. 4: 'the duty to provide hospitality, to act with generosity as a host, and to protect visitors is more than a matter left to the preferences of individuals.' p. 3: 'Offering guests hospitality has been, in all human settings, a moral obligation until the advent of mass travel and commercialism.' | — | equivocal | material | Rebuild on K2's wording: the hospitality literature states the host's duty and has not said who holds it when the host is an organization. Detail below. |

- **Premises (S-012.4).** P1 (sourced, S-012.2): two accountability writers tie answerability to harmful outcomes. P2 (sourced, S-012.3): one hospitality instrument measures hospitableness as an individual's motive. C: the host's obligation is sought either in an injury or in a person's motive.
- **Counter-model.** Both premises are true and the paper's own next paragraph refutes C: hospitality studies has an 'account of what a host owes' (S-013), which v6 finds in custom and law, not in injury or motive. Lashley himself puts the obligation in moral and religious systems (pp. 3–4) and says it held 'until the advent of mass travel and commercialism' (p. 3).
- **Terms.** 'Answerability' (P1) and 'hospitableness' (P2) both become 'the host's obligation' in C. Accountability research does not seek a host's obligation at all; hospitableness research measures a disposition and says so. Kong keeps answerability apart from owing: his position 'is consistent with a deployer's turning out … to owe nothing at all' (p. 3).
- **Quantifiers.** 'Either … or' is exhaustive; two literatures, each reduced to one or two works, cannot exhaust where an obligation 'is sought'.
- **Overgeneration / undergeneration.** Not a duty claim; not applicable.
- **K claim.** K2. Lashley pp. 3–4 also narrows K1: he confines the strong obligation to pre-commercial settings.

### S-013 · Introduction ¶3
> This article seeks to keep hospitality studies' account of what a host owes, and to say where that obligation goes when the work of hosting is delegated to algorithmic systems spread across several firms.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-013.1 | The article's aim: keep the account of what a host owes and say where the obligation goes under delegation | Signpost | — | — | — | — | — | Two presuppositions carry over from rows above: that hospitality studies has one account of what a host owes that covers commercial hosts (S-008.1, S-009.1, S-009.2, S-012.4), and that the work is delegated to systems 'spread across several firms' (S-005.1). |

### S-014 · Introduction ¶3
> Read as a role, the obligation has a content, a moment at which it comes into force and a holder, and the law of innkeepers supplies all three.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-014.1 | A role obligation has a content, a moment at which it comes into force and a holder | Definition | — | — | — | valid | — | Used in this sense in A-3 and S-015. It matches K3 ('content … trigger … holder'). |
| S-014.2 | The law of innkeepers supplies all three | Own inference | Premises rest on rows in batch A2. Primary texts I checked: Hotel Proprietors Act 1956 s 1(1), (3); Calye's Case (1777 ed. of Coke, Part VIII; v6 cites fol. 33b, which I did not re-check against the folio marks) | HPA s 1(1): the innkeeper's duties 'shall … attach to the proprietor of such an hotel and shall not attach to any other person'. Calye: 'if the guest be beaten in the inn, the innkeeper shall not answer for it'. | — | equivocal | material | Say which obligation the law supplies: a duty to receive and a strict duty for goods, for inns and statutory hotels, in English law. Protection of the guest's person needs another source (K4's reception tier). |

- **Premises (S-014.2).** P1 (sourced, batch A2): innkeeper law names duties to receive and to keep the guest's goods. P2 (sourced): the 1956 Act makes an hotel one 'held out by the proprietor' to 'any traveller presenting himself' (s 1(3)). P3 (sourced): it attaches the duties to 'the proprietor' and no other person (s 1(1)). P4 (assumption): the obligation so described is 'that obligation' of S-013, the one hospitality studies describes. C: the law of innkeepers supplies the content, the moment and the holder of the host's obligation.
- **Counter-model.** P1 to P3 hold and C fails on content: S-009 names protection from harm as what the host owes, and Calye's Case excludes the guest's person from the innkeeper's strict duty. C fails on holder for v6's own purposes: s 1(1) excludes every person but the proprietor, while v6 goes on to name operators and brands as holders.
- **Terms.** 'The obligation' is customary in S-013 and legal in S-014. 'The law of innkeepers' is English common law and one statute, with United States common law reported at second hand.
- **Quantifiers.** 'All three' holds only for an inn or a statutory hotel.
- **Overgeneration.** The same three items can be read off the law of carriers.
- **Undergeneration.** No content, moment or holder is supplied for a restaurant, a rental in the host's home or a placed guest.
- **K claim.** K3 and K4.

### S-015 · Introduction ¶3
> Because the law attaches the duty to the role, the work of hosting can pass to staff, contractors or systems while the duty, and the answering for it, stay with the holder.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-015.1 | Because the law attaches the duty to the role, work can pass to staff, contractors or systems while the duty and the answering for it stay with the holder | Own inference | As A-4.1: Woodland [2013] UKSC 66 paras 7, 22, 24, 25(3); Occupiers' Liability Act 1957 s 2(4)(b). Later treatment not checked. | OLA s 2(4)(b): 'the occupier is not to be treated without more as answerable for the danger if in all the circumstances he had acted reasonably in entrusting the work to an independent contractor and had taken such steps (if any) as he reasonably ought in order to satisfy himself that the contractor was competent and that the work had been properly done.' | — | invalid | fatal | Replace with K8's statement per duty: the innkeeper's liability for goods stays; the holder answers for employees; for contractors the rule varies; the party that promised the stay answers for its performance. Say that no authority yet covers systems. |

- **Premises.** P1 (earlier inference, S-014.2): the law attaches the duty to the role. P2 (sourced): where a duty is non-delegable the work may be delegated and the duty stays (Woodland para 7). P3 (assumption): a duty that the law attaches to a role is non-delegable, whoever the delegate. C: the work can pass to staff, contractors or systems while the duty, and the answering for it, stay with the holder.
- **Counter-model.** P1 and P2 are true. A hotel entrusts lift maintenance to a competent contractor, checks the work, and a guest is hurt. Under s 2(4)(b) the hotel is 'not … answerable'. The duty attached to a status (occupier) and did not stay. P3 is false, so 'because' fails: attaching a duty to a role does not make it non-delegable. Woodland says the same in general terms: 'as a general rule he is not liable for the contractor's negligence' (para 24), and a party whose duty is 'only to arrange for its performance' is not liable (para 25(3)).
- **Where C does hold.** For staff (v6's Calye passage: 'a default in him or his servants'); for the innkeeper's goods liability; for the contract with a paying guest (Woodland para 7 on the contracting party).
- **Terms.** 'The answering for it' means liability here, accountability to a forum in section 3, and Kong's answerability in S-012. The statute's own word for liability is 'answerable', and it withholds it in the contractor case. For 'systems' v6 cites no authority; S-025 sets aside whether a machine can bear a host's duties, yet this sentence needs the answer 'no', and Kropf et al. (S-025.2) hold that a robot can bear role responsibility.
- **Quantifiers.** One rule for three kinds of delegate; the law has three rules.
- **Overgeneration.** Yes: any firm whose duties attach to a status. Woodland warns against 'the exception … eating up the rule' (para 22).
- **Undergeneration.** A placed guest has no contract; a restaurant has no innkeeper's liability.
- **K claim.** K8 (and K3). The sentence states as a universal what K8 states per duty.

### S-016 · Introduction ¶3
> The guest's standing therefore survives delegation.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-016.1 | The guest's standing survives delegation | Own inference | Rests on S-015.1 and the definition in section 3 ¶6 | — | — | valid with added premise | minor | Added premises: the stipulated sense of 'standing held' (not yet given), and that each duty which stays is owed to the guest (K5). It inherits S-015.1's fault: where the duty does not stay, neither does the standing. |

- **Premises.** P1 (earlier inference, S-015.1): the duty stays with the holder. P2 (stipulation, section 3): standing held is 'the guest's position as the one to whom the host's directed duties are owed'. P3 (assumption): the duties that stay are directed to the guest. C: the guest's standing survives delegation.
- **Counter-model.** A duty that stays and is public, enforced by the state and not by the traveller (the case K5 lists as its defeater; I did not read that source). P1 is true and the guest holds nothing.
- **Terms.** 'Standing' in ordinary and legal use is a power to bring a claim; here it is a position. A reader of the Introduction has only the ordinary sense.
- **K claim.** K5 and K6.

### S-017 · Introduction ¶3
> What can fail is its exercise, and from that distinction we derive a test, scoped by the type of decision, of whether a touchpoint keeps the conditions under which a guest can press a claim.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-017.1 | What can fail is the exercise of standing | Own inference | Rests on S-016.1 and the definition of 'standing exercised' | — | — | valid with added premise | minor | Added premise: the definition of exercise (pressing the claim 'on a party able to receive it'), not yet given. |
| S-017.2 | The test is derived from the distinction between holding and exercising standing | Own inference | v6 'Three conditions and six questions' ¶1 | v6: 'Its conditions take their names from the study of coordination … Their content here comes from the host's duties'. | — | valid with added premise | minor | Added premises: three conditions from Okhuysen and Bechky, the sixth question from Hirschman, the scoping from Baum and Laux. 'Build' is truer than 'derive'. |
| S-017.3 | The test is scoped by the type of decision and asks whether a touchpoint keeps the conditions for pressing a claim | Signpost | — | — | — | — | — | None. |

- **K claim (S-017.1, S-017.2).** K7, second route; K9.

### S-018 · Introduction ¶3
> We argue that algorithmic mediation rarely removes the host's obligation; what it removes is the path from the guest to anyone with the authority to answer for it.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-018.1 | Mediation rarely removes the obligation; what it removes is the guest's path to authority | Own inference | As A-6.1 and A-6.2. v6 section 4, 'The authority–answerability split' ¶3 | v6: 'the path from the guest to graded authority, which an algorithmic system can lengthen, obscure or remove'. | — | invalid | material | The body says 'can … remove'; the thesis says 'removes'. Use the body's modal. Premises and tests as under A-6. |
| S-018.2 | The party sought has 'the authority to answer for' the obligation | Definition in use | As A-6.3 | — | — | equivocal | minor | As A-6.3. |

- **K claim.** K9, with K7.

### S-019 · Introduction ¶4
> The article begins by setting out the host's power and obligation as hospitality studies describes them, and argues that the obligation belongs to a role.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-019.1 | Roadmap: first section | Signpost | — | — | — | — | — | None. |

### S-020 · Introduction ¶4
> The second section follows the obligation when its holder hands on the work, and defines the guest's standing from it.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-020.1 | Roadmap: second section | Signpost | — | — | — | — | — | None. |

### S-021 · Introduction ¶4
> The third section examines touchpoints in hotels, short-term rentals and restaurants, each of which hands part of a host's work to a system with several firms behind it.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-021.1 | Roadmap: third section | Signpost | — | — | — | — | — | None. |
| S-021.2 | Hotels, short-term rentals and restaurants each hand part of a host's work to a system with several firms behind it | Empirical generalization (uncited; rests on the cases of section 4) | Garcia WP p. 2; Bosma 2022: 605; v6 section 4 on the restaurant case | Garcia p. 2: 'an independent revenue management company (the algorithm's designer)'. v6 on the projected chef: it 'decides nothing about the guest', and 'staff go on hosting'. | 3 ('each … several firms': the pricing case shows one supplier, and the restaurant case shows no handed-over work and names no firm) | partial | minor | 'each of which can hand part of a host's work to a system, often one that other firms supply'. |

### S-022 · Introduction ¶4
> We close with the paper's limits, three studies it calls for, and what it asks of organizations.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-022.1 | Roadmap: the close | Signpost | — | — | — | — | — | None. (The roadmap for organizations sits in section 4, not in the Conclusion.) |

### S-023 · Introduction ¶4
> We suggest that, by looking for the obligation in the host's motive, the debate about commercial hospitality has had no way to say where it goes once no person does the hosting.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-023.1 | The debate about commercial hospitality looks for the obligation in the host's motive | Paraphrase used as a characterization of a field | Lashley 2015: 1, 3, 4 (the debate's main voice in v6). Telfer, on whom the debate rests, is closed and unread. | p. 4: 'the duty to provide hospitality, to act with generosity as a host, and to protect visitors is more than a matter left to the preferences of individuals. Beliefs about hospitality and obligations to others are located in views and visions about the nature of society'. | 5 (the debate looks for hospitableness, the genuineness of the welcome, in motive; Lashley places the obligation in moral and religious systems) | partial | material | 'by asking whether a paid welcome can be genuine, the debate has tied hospitableness to a person's motive'. Then make K2's claim: the literature states the duty and names no holder for a host that is an organization. |
| S-023.2 | The debate has had no way to say where the obligation goes once no person does the hosting | Gap claim | Library and queries in closing list 4. Texts read: Liu et al. 2026, IJHM 135, 104640, p. 9 (cited in v6); Sharma and Mattila 2026: 915 and Gursoy 2026: 155–156 (not cited in v6); Kropf et al. 2026: abstract, p. 7. | Liu et al. p. 9: 'robotic hospitableness is relationally experienced by guests rather than internally possessed by the machine.' Sharma and Mattila p. 915: 'What are the rights and responsibilities of a human employee, and how should the firm (owners and management) translate those into the service robot context?' | — | partial | material | Hospitality research has begun to say where hospitableness and responsibility go when a machine hosts: to the guest's experience (Liu et al.), to the firm as a matter of liability and governance (Sharma and Mattila), to 'hospitality firms' (Gursoy). None grounds this in what a host owes or picks a holder among several firms. Claim that, in the form 'I found no work that…', and cite the three. |

- **S-023 as inference.** P1 (S-023.1): the debate looks for the obligation in the host's motive. P2 (v6 section 2 ¶4): a motive belongs to a person and cannot be handed on. C: the debate cannot say where the obligation goes once no person hosts. P1 swaps 'obligation' for 'hospitableness'; with the right term the conclusion is that the debate cannot say where *hospitableness* goes, and Liu et al. (2026) say exactly that. The hedge 'We suggest' is kept.
- **K claim.** K2. Its listed defeater is a hospitableness scholar who assigns the host's duty to an organization; I found none who does so as a duty to the guest, and the nearest are named in the row.

### S-024 · Introduction ¶4
> The role account brings into view the parties, such as operators, brands and vendors, that now do much of that work.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-024.1 | The role account brings into view the operators, brands and vendors that now do much of the hosting | Own inference | — | — | — | valid with added premise | minor | Added premise (empirical, uncited here): operators, brands and vendors now do much of the work of hosting. Note that on v6's own proposal a vendor 'answers to the host' and holds no role towards the guest; the account brings vendors into view as performers, not as holders. |

- **K claim.** K8.

### S-025 · Introduction ¶4
> Whether a machine could itself bear a host's duties we set aside: a robot can occupy a role without being a moral agent (Kropf et al. 2026: 7), and our concern is the parties who deploy such systems and the guests who meet them.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-025.1 | The paper sets aside whether a machine could itself bear a host's duties | Stipulation (scope) | — | — | Not one of the nine: the stipulation is not kept | partial | minor | S-015 ('the duty … stay[s] with the holder' when work passes to systems) needs the answer 'no'. Either keep the question open in S-015 or say here that the paper assumes the machine holds no duty. |
| S-025.2 | A robot can occupy a role without being a moral agent | Paraphrase | Kropf, Spöck and Werner 2026, Int. J. Social Robotics 18:30, version of record, p. 7 (`kropf2026blame/user_pdf/fulltext.pdf`) | 'Robots are not moral agents, but social actors who, due to their role, are subject to evaluation and certain reactions from interacting humans.' | — | supported | — | Locator correct. The source is about AI-based care robots and goes further than the sentence: such robots 'can still hold role responsibility based on their social function in caregiving contexts' (abstract, p. 1). That cuts against S-015; see there. |
| S-025.3 | The paper's concern is the deploying parties and the guests | Signpost | — | — | — | — | — | None. |

### S-026 · Introduction ¶4
> The study of phygital hospitality has to ask who answers to the guest, and what an organization must keep for its guests to remain guests.

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | Severity | Action |
|---|---|---|---|---|---|---|---|---|
| S-026.1 | The field must ask who answers to the guest, and what an organization must keep for its guests to remain guests | Own inference (normative) | v6 section 4, 'Three conditions and six questions' ¶1 | v6: 'a guest who understands a system and can predict it has still been hosted by no one if no party is obliged to answer'. | — | equivocal | minor | 'Guest' has two senses. In S-016 a guest is whoever is owed the host's duties, and stays one under delegation. Here a guest stops being one if the organization fails to keep something. Write 'for its guests to be able to press what they are owed'. |

- **Premises.** P1 (earlier inference, S-016.1): the guest's standing survives delegation. P2 (earlier inference, S-018.1): what can be lost is the path to authority. C: the field has to ask who answers to the guest, and what an organization must keep for its guests to remain guests.
- **Counter-model.** By P1 a guest with no path to authority is still a guest. So nothing the organization keeps or drops decides whether 'its guests … remain guests', unless 'guest' changes sense.
- **Terms.** 'Answers to' is accountability to a forum (section 3); S-015's 'answering for' is liability. 'Guest' as above.
- **Overgeneration.** A bank's customers could be said to 'remain customers' on the same terms; v6 concedes the mechanism is general.
- **K claim.** K7 and K9.

---

## Closing lists

### 1. Counts by verdict

72 rows across 32 sentence ids.

| Verdict | Rows | Severity |
|---|---|---|
| supported | 7 | — |
| supported (abstract only) | 6 | 6 minor |
| partial | 23 | 11 material, 12 minor |
| not in source | 0 | — |
| contradicted | 0 | — |
| unverifiable | 1 | 1 minor |
| valid | 4 | — |
| valid with added premise | 9 | 2 material, 7 minor |
| equivocal | 7 | 3 material, 4 minor (one of the material rows also undergenerates) |
| overgenerates / undergenerates (as the main verdict) | 0 | — |
| invalid | 6 | 2 fatal, 4 material |
| signpost (no verdict) | 9 | — |

Severity in all: 2 fatal, 20 material, 30 minor. Of the 26 rows that test an inference or a definition, 4 stand as written (three definitions and one summary).

### 2. The fifteen rows that most endanger the paper

1. **S-015.1** (fatal). 'Because the law attaches the duty to the role … the duty, and the answering for it, stay with the holder': attaching a duty to a role does not make it non-delegable, and for contractors the Occupiers' Liability Act 1957 s 2(4)(b) and Woodland paras 22, 24 and 25(3) say the opposite.
2. **A-4.1** (fatal). The abstract states 'the work can be delegated and the duty cannot' as a rule and drops the body's hedge that Woodland's category may not include hotels.
3. **S-014.2** (material). 'The law of innkeepers supplies all three': the content it supplies leaves out the guest's person (Calye), the holder it names excludes everyone but the proprietor (HPA 1956 s 1(1)), and it reaches inns only.
4. **A-3.2** (material). The role obligation is claimed of 'the commercial host'; the argument moves from a customary obligation to a legal one and fails for restaurants, rentals and placed guests.
5. **S-012.4** (material). 'The host's obligation is sought either in an injury or in a person's motive': two terms change sense, the dichotomy is not exhaustive, and Lashley (2015: 3–4) and the paper's next paragraph both locate the obligation elsewhere.
6. **S-018.1** (material; twin A-6.2). The thesis says mediation 'rarely' removes the obligation and 'removes' the path; the paper has no frequency evidence and its own body says 'can … remove'.
7. **S-023.2** (material). 'No way to say where it goes once no person does the hosting': Liu et al. (2026: 9), Sharma and Mattila (2026: 911, 915) and Gursoy (2026: 155–156, 160) have begun to say, and v6 cites only the first, for another point.
8. **S-011c.3** (material). The gap in the phygital governance literature rests on one full text and one abstract, and two hospitality papers that pose the 'which party' question are missing from v6.
9. **S-009.2** (material). Shryock's 'protect guests from harm' describes the Balga Bedouin's karim man; the sentence drops the setting, and Shryock (S31) separates karam from 'the hospitality offered to tourists'.
10. **S-023.1** (material). The debate looks for hospitableness in motive; Lashley places the obligation in moral and religious systems (2015: 4). The sentence swaps the two.
11. **S-012.2** (material). 'Ties it to harm' is true of Nissenbaum and Kong and false as a statement about algorithmic-accountability research; Lyons et al. (2021), in v6's own list, ground contestation in dignity and autonomy.
12. **S-007.3** (material; twin A-2.1). 'Each … places the party who decides at a distance': in Garcia's sample the decider is the manager of a family-run hotel.
13. **S-001.1** (material; twins A-1.1, A-1.2). 'Hands much of the work … from admission … to complaints': admission, room allocation and complaints have no source, and the paper's one admission case is constructed.
14. **S-005.1** (material; twin A-1.3). 'Behind each of these stands a chain of vendors' rests on a paper about AI services at large that says 'often now'.
15. **S-009.1** (material). 'On that view the host owes the guest more than a service': the editors report what historians say of ancient traditions; their own view states no duty.

Next in line: A-4.3 and A-6.1 (material), each valid only with a premise the abstract does not state.

### 3. Sources I could not read in full, and the rows that wait on them

**Closed; abstract or less.**

| Source | What I had | Rows that wait |
|---|---|---|
| Boo and Chua 2022 (10.1108/IJCHM-12-2021-1471) | Crossref abstract. Unpaywall, OpenAlex and Semantic Scholar report no open copy. | S-003.1 |
| Germann Molz 2026 (10.1386/hosp_00107_1) | Crossref abstract. Unpaywall: closed. | S-010.4; and, as the nearest neighbour in the target journal, S-011c.3, S-023.2, A-6.2, S-018.1 |
| Riordan 2024 (10.1386/hosp_00083_1) | Crossref abstract. Closed. | S-010.5 |
| Brochado et al. 2026 (10.1108/JSM-09-2025-0709) | Crossref abstract. Closed. | S-011a.1 |
| Li et al. 2021 (10.1016/j.ijhm.2021.102930) | Semantic Scholar abstract. Closed. | S-011b.3 |
| Xing and Zhang 2026 (10.1108/IJCHM-07-2025-1138) | Title and Crossref abstract. Closed. | S-011b.4 |
| Batat 2026 (10.1108/JSM-09-2025-0600) | Crossref abstract. Closed. | S-011c.1, S-011c.3 |
| Telfer 1995, and the 2000 chapter | Nothing; closed (card records the attempts). Not cited in v6, but the debate that S-012.3 and S-023.1 characterize rests on her. | S-012.3, S-023.1; K2 |
| Garcia et al. 2026, version of record (10.1287/mnsc.2022.03740) | Crossref record only. I read the CESifo working paper. | S-002.1; A-2.1 and S-007.3 use its pp. 2 and 10 |
| Wirtz et al. 2022 (10.1177/10946705221130467); Kunz and Wirtz 2026 (10.4324/9781003643951-4) | Crossref records. The Sage PDF returned a bot challenge, which I did not try to pass; the chapter is closed. | S-011c.3 (possible defeaters) |

**Read in a version other than the one cited.** Lynch et al. 2011, accepted manuscript without journal pages (S-008.1, S-008.2, S-009.1). Nissenbaum 1996, author's preprint with its own pagination (S-012.1, S-012.2). Lyons et al. 2021, arXiv copy (S-012.2). Calye's Case, 1777 edition of Coke's Reports by OCR, folio not re-checked (A-3.2, S-014.2).

**Open texts read in part.** For these I read the passages named and searched the whole file; a second reader should not take my silence about the rest as a finding. Garcia WP (abstract, pp. 2–4, 9–11, 33). Belanche et al. (abstract, pp. 268, 273–277, 280–282, appendices). Bosma (pp. 602–605). Cobbe et al. (pp. 1187–1188, 1192–1193, and every hit for end-user, affected, visib-, customer). Lynch et al. (Introduction, 'Hospitality as social control', 'An agenda', 'Journal ambitions'). Shryock (S20–S21, S30–S31). Bialski (method statement, p. 257 and the pages either side). Germann Molz 2018 (method, pp. 241–244). Batat 2024 (pp. 1220, 1223, 1230, 1235, and every hit for smooth, seamless, fluid, personal). van Doorn et al. (abstract, p. 43). Shabnam et al. (abstract, §2, §7, and every hit for governance, accountab-, responsib-, contest-). Nissenbaum (pdf pp. 1–2, 11, 13). Kong (pp. 1–5). Lashley 2015 (pp. 1, 3–4, and every hit for obligation, duty, motive, instrument). Kropf et al. (abstract, pp. 6–7). Woodland (paras 7, 22–25); later treatment not checked, and Armes v Nottinghamshire [2017] UKSC 60 is saved and unread by me. HPA 1956 s 1. OLA 1957 s 2. Gursoy 2026 (pp. 155–157, 159–160, 162). Sharma and Mattila 2026 (pp. 908–909, 911, 915). Liu et al. 2026 (pp. 2, 7, 9). Pijls et al. 2017 (pp. 125–126). Tasci et al. 2021 (pp. 340–342). Slattery 2002 (pp. 22–23). Lyons et al. 2021 (arXiv p. 3).

### 4. Gap and characterization claims, with the queries I ran

All queries ran on 11 Nov 2026 and carried no author or project detail.

**Query log.**

- *Consensus* (20 records returned and read for each): Q1 'phygital service accountability: who is responsible to the customer for algorithmic decisions in hybrid physical-digital service'. Q2 'organizational hospitableness: hospitality organization as host, duty or obligation to guests beyond individual employee motive'. Q3 'hotel guests automated or AI decisions recourse: reaching a human with authority, accountability to guests in unmanned or smart hotels'. Q4 'algorithmic accountability as answerability owed to decision subjects regardless of harm: contestability, due process, right to human review'. Q5 'who is the host when hotels automate: host obligation, responsibility and hospitality without human hosts (robots, self-service, platforms)'. Q6 'hospitableness measurement scale organizational level hospitality culture scale firm-level hospitableness'. Q7 'hospitality studies host duty of care to guests assigned to hotel company or organization rather than individual host; role-based obligation of commercial hosts'.
- *Crossref* (`query.bibliographic`, first 12 of each read; the ranking is loose and none of the first 12 bore on the claim): C1 'phygital accountability responsibility algorithmic governance customer' (719,542 matches). C2 'phygital service contestable escalation human oversight who is accountable' (4,368,470). C3 'organizational hospitableness host obligation duty firm level' (1,402,610). C4 'hotel guest algorithmic decision recourse human authority accountability' (4,247,672). C5 'hospitality host obligation algorithm delegation who answers to the guest' (1,687,008).
- *Semantic Scholar*: 'algorithmic management hospitality guest complaint escalation' (160 matches, first 12 read, none on a guest's recourse). Three other queries failed with HTTP 429 after four tries each.
- *OpenAlex*: every attempt returned HTTP 429.
- *WebSearch*: W1 'phygital service research accountability "who is responsible" OR "responsibility" algorithmic decisions customers firm vendor'. W2 'hospitality theory "organisation as host" OR "organizational host" OR "corporate host" obligation to guests hospitableness beyond individual'. W3 'algorithmic accountability answerability "regardless of" harm OR "even without harm" OR "dignity" right to contest automated decision procedural justice'.
- *Library*: `grep` of all 265 cards, held and rejected included, for phygital; responsib-, accountab-, owed, duty, liab-; vendor; chatbot, complaint, room allocation or assignment, risk scoring, instant book; hospitableness. Search summaries served as leads only; each text quoted in a row I opened myself.

**The claims.**

| Claim (row) | Queries | What I found |
|---|---|---|
| The phygital literature does not say to whom its safeguards are owed or which firm owes them (S-011c.3) | Q1, Q3, Q5; C1, C2; W1; library | I found no work that states a duty owed to the customer or guest, or that allocates such a duty among the firms behind a system, in the phygital service literature. I found two hospitality papers that pose the question of which party answers (Sharma and Mattila 2026: 911, 915; Gursoy 2026: 155–156, 160), both in terms of blame, liability and governance. Unread leads that could go further: Wirtz et al. 2022; Kunz and Wirtz 2026; Gustafsson 2026; Bakrim et al. 2025; Beckers and Teubner 2023. One of the two sources v6 cites for the governance turn is abstract-only. |
| Algorithmic-accountability research ties answerability to harm (S-012.2) | Q4; W3; library | Refuted as a statement about the field. Lyons et al. (2021, arXiv p. 3) ground the ability to contest in 'human dignity and autonomy'; Yurrita et al. (2025, saved, abstract) speak of 'decision subjects' rights to dignity and autonomy'. Q4 returned a body of work on contestability, procedural justice and relational accountability (Metcalf et al. 2023; Novelli et al. 2023; Kinchin 2024; Henin and Le Métayer 2021), which I did not read. True of Nissenbaum and Kong. |
| Hospitality research measures hospitableness as a motive of individual hosts (S-012.3) | Q2, Q6, Q7; C3; W2; library | True of Blain and Lashley's instrument (Lashley 2015: 1). Narrowed by Pijls et al. (2017: 125–126) and Tasci et al. (2021: 341). Unread leads on hospitality measured as an organization's culture: Dawson et al. 2011; Pizam 2020; Bandi Tanner et al. 2026. |
| The commercial-hospitality debate looks for the obligation in motive and cannot say where it goes once no person hosts (S-023.1, S-023.2) | Q2, Q3, Q5, Q7; C5; W2; library | I found no hospitality scholar who assigns the host's duty to the guest to an organization and names its holder among several firms. I found work that says where hospitableness or responsibility goes when a machine hosts (Liu et al. 2026: 9; Sharma and Mattila 2026: 915; Gursoy 2026: 155–156). Unread leads: Koo and Kwon 2026 ('socio-hospitality' for machine-mediated contexts); van Rheede and Dekker 2016 ('host as shepherd'); Lashley 2014 (editorial on the host's duty to protect); Germann Molz 2026 (closed). |
| No prior work makes the paper's argument for hospitality (A-6, S-018; K9's defeater) | Q3, Q5; C4; Semantic Scholar; library | I found no work that argues that algorithmic mediation leaves a host's duty in place and removes the guest's path to someone with authority. Nearest: Gursoy 2026: 157 ('human-led resolution' that preserves 'accountability'), 160; Germann Molz 2026 (abstract: 'erasing hosts'). The studies of unmanned hotels that Q3 returned measure acceptance, satisfaction and forgiveness. |
| Hospitality scholars have long resisted the food-drink-bed definition (S-008.1) | Source text only | Lynch et al. report that this definition dominates academic discourse. Slattery (2002: 23) quotes Brotherton and Wood's definition of hospitality as 'a contemporaneous human exchange, which is voluntarily entered into', which names no duty. Both narrow K1. |

### 5. Sources to drop, and leads to replace or add

**Drop, replace or confine.**

- **Boo and Chua 2022** (S-003.1). An adoption-intention survey read in abstract cannot carry 'verify identity at check-in' as a fact about hotels, nor the later claim that such a system 'does a clerical job'. I found no replacement; a source on deployed biometric check-in is needed. Xu et al. (card `xu2020facial`) is also abstract-only.
- **Brochado et al. 2026** (S-011a.1). The abstract does not state the proposition. Drop the sentence or read the review.
- **Xing and Zhang 2026** (S-011b.4). Title-only support. Drop or read.
- **van Doorn et al. 2017** and **Li et al. 2021** (S-011b.2, S-011b.3). Keep, as service research on robots and AI encounters; they are not 'the literature on [phygital operation]'.
- **Cobbe et al. 2023** (S-005). Keep for AI supply chains. It cannot carry a fact about hospitality systems or about what a guest meets.
- **Shryock 2012** (S-009.2). Keep only with its setting; it supports the customary duty among the Balga and, at S31, cuts against carrying it into commerce.
- **Lynch et al. 2011** (S-008.1, S-009.1). Keep for the editors' aim; do not cite it for a duty that hosts owe.

**Leads** (record, and where I found it; 'read' means I opened the saved text).

| Lead | Record | Where found | Bears on |
|---|---|---|---|
| Sharma and Mattila 2026, 'Rights and responsibilities of hospitality service robots', JHTR 50(6): 904–920 | 10.1177/10963480251393749 (Crossref) | Library (`sharmamattila2025rights`, full text saved); Q3, Q5, Q7. Read pp. 908–909, 911, 915. | S-011c.3, S-023.2: poses 'who should be blamed' among restaurant, manufacturer, algorithm maker and manager |
| Gursoy 2026, 'Reconceptualizing customer experience co-creation…', JHMM 35(2): 151–165 | 10.1080/19368623.2025.2611513 (Crossref) | Library (`gursoy2026reconceptualizing`, full text saved); Q3, Q5. Read pp. 155–157, 160. | S-011c.3, S-023.2, A-6: AI 'shifts responsibility'; accountability 'when harm, bias, or exclusion arise' |
| Tasci, Aktas and Acikgoz 2021, 'Cultural differences in hospitableness', THM 27(2): 339–361 | 10.20867/thm.27.2.6 (Crossref; open, CC BY-NC-SA) | Q6. Saved this session at `sources/tasci2021cultural/`. Read pp. 340–342. | S-012.3: how hospitableness has been measured |
| Pijls et al. 2017, 'Measuring the experience of hospitality', IJHM 67: 125–133 | 10.1016/j.ijhm.2017.07.008 (Crossref) | Library (`pijls2017measuring`, saved). Read pp. 125–126. | S-012.3 |
| Lyons, Velloso and Miller 2021 (already in v6's list) | 10.1145/3449180 (Crossref) | Library (saved arXiv copy). Read p. 3. | S-012.2: a ground other than harm |
| Liu, Benckendorff and Walters 2026 (already in v6's list) | 10.1016/j.ijhm.2026.104640 | Library (saved). Read p. 9. | S-023.2 |
| Wirtz, Kunz, Hartley and Tarbit 2022, 'Corporate digital responsibility in service firms and their ecosystems', J. Service Research 26(2): 173–190 | 10.1177/10946705221130467 (Crossref; Unpaywall lists it as hybrid open access) | Q1. Not read: the publisher PDF returned a bot challenge. | S-011c.3: responsibility across a service firm and its partners |
| Kunz and Wirtz 2026, 'Corporate digital responsibility in tourism and hospitality', in *The Ethics of AI in Hospitality and Tourism*, pp. 57–71 | 10.4324/9781003643951-4 (Crossref) | Crossref search for the item above. Closed; not read. | S-011c.3, A-6 |
| Gustafsson 2026, 'Unmanned, not unmanaged: phygital service design…', J. Services Marketing | 10.1108/jsm-09-2025-0693 (Crossref) | Q1. Not read. | S-011c.3; unstaffed formats in the phygital literature |
| Bakrim et al. 2025, 'Navigating paradoxes in phygital systems', J. Macromarketing 46(3): 343–363 | 10.1177/02761467251409668 (Crossref) | Q1. Not read. | S-011b.1: a phygital paper on surveillance and exclusion, against 'smoother and more personal' |
| Beckers and Teubner 2023, 'Human–algorithm hybrids as (quasi-)organizations?', J. Law and Society 50(1): 100–119 | 10.1111/jols.12412 (Crossref) | Q1. Not read. | S-012.1: accountability placed on a collective actor, not on designer or deployer |
| Novelli, Taddeo and Floridi 2023, 'Accountability in artificial intelligence', AI & Society 39(4): 1871–1882 | 10.1007/s00146-023-01635-y (Crossref) | Q4. Not read. | S-012.2 |
| Dawson, Abbott and Shoemaker 2011, 'The Hospitality Culture Scale', IJHM 30(2): 290–300; Pizam 2020, 'Hospitality as an organizational culture', JHTR 44(3): 431–438 | 10.1016/j.ijhm.2010.10.002; 10.1177/1096348020901806 (Crossref) | Q2, Q6. Not read. | S-012.3, S-023.1: hospitality measured at the level of the organization |
| Koo and Kwon 2026, 'Three ages of hospitality reflection', IJCHM | 10.1108/ijchm-10-2025-1555 (Crossref; an erratum exists) | Q5. Not read. | S-023.2, A-6: hospitality as an ethical process in machine-mediated settings |
| van Rheede and Dekker 2016, 'Hospitableness and sustainable development', RHM 6(1): 77–81; Lashley 2014, 'Editorial', RHM 4(1–2): iii–v | 10.2989/rhm.2016.6.1.10.1298; 10.1080/22243534.2014.11828306 (Crossref) | Q2, Q7. Not read. | S-023.1, K1, K2: the host's responsibility and duty in the hospitableness literature |
| Slattery 2002: 23 (already in v6's list), quoting Brotherton and Wood | — | Library (saved). Read pp. 22–23. | S-008.1, K1: a canonical definition with no duty |
