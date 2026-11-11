<!-- Claim register, batch A1, run rr-2026-11-k, written by a Claude (Fable 5.2) subagent on 11 Nov 2026. -->

# Claim register A1: the Abstract and the Introduction

**Scope.** Sentence ids A-1 to A-6 and S-001 to S-026 of `manuscript/DRAFT_v6.md` (SHA-256 `8951cadf…537e7`, the hash frozen in K-D5). For every id the last 'As written' line of `rewrite_2026-11/sbs/LEDGER.md` matches the draft word for word (checked by script). The ledger's S-011 covers three sentences of v6; I label them S-011a, S-011b and S-011c.

**How I judged.** I judged each row from the source's own text, never from a card or a ledger 'Truth' line. I did not open `CORRECTIONS_2026-11-11.md`, `VERIFICATION.md`, anything under `manuscript/reviews/`, or `CALIBRATION_RESULT.md`. Class numbers are the brief's: 1 population, 2 setting, 3 strength, 4 speaker, 5 scope, 6 design, 7 application, 8 version, 9 combination. Passages are pasted from the saved text with its locator.

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
