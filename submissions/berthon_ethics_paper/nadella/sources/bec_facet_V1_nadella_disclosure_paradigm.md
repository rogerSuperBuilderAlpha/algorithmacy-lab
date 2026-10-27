# V1 — Nadella's post and the disclosure paradigm: the post, Microsoft's own record, and the EU AI Act

*Facet V1 of research round 7 (version 4), 2026-10-14. Agent-drafted; the author has not reviewed it, and none of the text is the author's. Notes for the drafter, not prose for the paper.*

**What this facet covers.** (Q1) What Nadella's post of 10 October 2026 proposes, move by move (P1–P21), sorted into (i) a text, record or disclosure to be read, (ii) a control held by the deploying organisation, (iii) something that builds a person's capacity; who "we" is; where the people the systems act on appear; who must read the P15 evidence. (Q2) Microsoft's own published responsible-AI record on transparency and on users: the Responsible AI Standard v2 (2022), the Responsible AI Transparency Reports (2024, 2025), a current Transparency Note, the AI Literacy Starting Guide, the Elevate skilling commitment, and the Guidelines for Human-AI Interaction that the Standard tells teams to follow. (Q3) The EU AI Act's version of the same move: Articles 3(56), 4 (as enacted and as replaced by the Digital Omnibus 2026/1744), 13, 14, 26, 50, 73, 86. (Q4) Commentary on the post.

**The thesis tested** (from `v4/SOURCE_v4.md`): the post treats disclosure as sufficient ethical design, and so (a) places the burden on the person who must read, (b) keeps the person in a literacy-based experience, (c) does not scaffold the person's growth to algorithmacy.

**Read-depth marks.** *Full* = whole text read this session. *Part* = the passages named. *Abstract* = abstract only. *Record* = catalogue entry only.

---

## Method notes

| # | Source | Request | Result |
|---|---|---|---|
| 1 | Local capture | `~/iit-playground/dxd_foundation_local/nadella_2026-10-10_models_as_insider_risks.txt` | Read in full (P1–P21). Word counts by `grep -i` on the post body (header excluded): "user" 0, "people" 0, "skill" 0, "literac" 0, "train" 1 (P2, "training data"), "learn" 2 (P8 "learned", P20 "learnings"), "read" 1 (P15 "readable"), "human" 2, "person" 1, "affected" 1, "disclos" 2 (P20). |
| 2 | Sister arm (DXD) | `wt-dxd-foundation/.../literature/facets/G_nadella_lineage.md` (B1 table, C1–C10, changes of 2026-10-13); `library/nadella2026models.md` (S2-verified); `audit/claims/CLAIMS_01.md` rows C01-05, C01-36 to C01-40; `CLAIMS_04.md` rows C04-38, C04-40, C04-43 to C04-45 | Reused; not redone. |
| 3 | This arm | `facets/Z_gap_search.md` R1–R2 (Art 4, Omnibus); `facets/N2_platform_law.md` (Arts 13, 14, 26, 86, Omnibus dates) | Reused and extended. |
| 4 | EUR-Lex | `eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689` and `...CELEX:32026R1744`; also `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` (HTTP 200) | **EUR-Lex served both texts this time** (earlier facets Z and N2 recorded a bot challenge). Saved to `berthon_ethics_local/pdfs/V1/eurlex/`. The extracted text is byte-identical to the Publications Office copies in `pdfs/N2_platform_law/eu/` (`cmp`: identical; sha256 of 32024R1689 text d89a8a4d…, of 32026R1744 text 139b2b57…). |
| 5 | Microsoft (curl) | RAI Standard v2 PDF (msblogs.thesourcemediaassets.com); Transparency Report 2024 and 2025 PDFs (cdn-dynmedia-1.microsoft.com); AI Literacy Starting Guide (Jan 2025, same CDN); Elevate post (blogs.microsoft.com, 9 Jul 2025); Microsoft 365 Copilot Transparency Note (learn.microsoft.com, ms.date 2026-10-05); Amershi et al. 2019 (microsoft.com/research) | All 200; saved to `berthon_ethics_local/pdfs/V1/ms/`, extracted with `pdftotext`. |
| 6 | WebSearch | `Microsoft 2025 Responsible AI Transparency Report PDF`; `Microsoft "AI fluency" OR "AI literacy" skilling commitment Elevate 2025 2026 users`; `blogs.microsoft.com Microsoft Elevate Brad Smith July 2025 ...` | Located the primary URLs. Search summaries not used as evidence. |
| 7 | WebSearch (extended) | `Nadella "Models as Insider Risks" critique OR analysis OR response` | Nine hits; one substantive commentary (Sudjianto, Substack, 10 Oct 2026), fetched and read in full. The rest are news summaries already in DXD facet G (TNW, Business Standard, Forbes blocked) or vendor blogs. |
| 8 | WebSearch | `Nadella insider risks essay "those affected" OR "end users" OR "customers" critique October 2026 ...` | Nothing on the affected-person or end-user angle. |
| 9 | Crossref | `/works/10.1145/3290605.3300233` | Amershi et al., CHI 2019, pp. 1–13, 13 authors: confirmed. |

**Not done / blocked.** I did not read the whole 2024 (40 pp.) or 2025 (35 pp.) Transparency Reports: I searched each for literacy, fluency, skill, Transparency Note, disclos-, overreliance, end user, Human-AI, and read the pages those hits fell on (2024: pp. 4, 11, 25, 29, 33, 34; 2025: PDF pp. 7, 22, 26, 28, 34). I did not read any other Transparency Note, the Microsoft Trust Center AI Act page, or Microsoft's 2026 report (I did not search for one). Forbes (Linzainescu) remains blocked, as DXD recorded. No login, no paywall bypass.

---

## Q1. What the post proposes, move by move

DXD facet G already read the post paragraph by paragraph (B1 table) and tested three counts against it (C7); its claims ledger revised two rows from "supported_narrower" to "supported" on the ground that "Disclosure is one strand of the proposal, not its whole" (CLAIMS_01 C01-05, C01-36). I reuse that reading and add the three-way classification the brief asks for. *Full* (local capture; checked against DXD's blog comparison).

**Who "we/us" is.** The deploying organisation. The post grounds the move in "how to handle powerful actors inside the enterprise" (P8) and applies it to "SI inside the enterprise" (P9); the only explicit holder of authority is "Orgs" (P17). DXD's ruling D5 adopted this reading; the S2 check on `library/nadella2026models.md` confirmed "user", "customer", "employee" and "people" do not occur. My own count agrees ("user" 0, "people" 0).

**Classification.** (i) = a text, record or disclosure to be read; (ii) = a control held by the deploying organisation; (iii) = builds a person's capacity.

| P | Move (paraphrase; short fragments only) | Class | Who holds it / who reads it |
|---|---|---|---|
| P1–P3 | Setting: attribution to code paths is lost (P1–P2); responsibility cannot be outsourced to the provider (P3). | — (premise) | The deployer keeps responsibility. |
| P4 | Build systems whose behaviour "we can observe", limits we can test, actions we can contain. | (ii), with an observing element | The deployer. |
| P5 | Separate "the supply of intelligence from the authority over it". | (ii) | Authority = the deployer. |
| P6 | Deterministic system design, "human controls", operating procedures, industry standards. | (ii) | The deployer; "human controls" not described. |
| P7–P8 | Treat the model as an insider risk; identity, least privilege, "log activity", containment. | (ii); logging is a record (i) | Security staff. |
| P9 | Chain-of-thought transparency as "a non-negotiable", but "not sufficient or dependable". | (i) | A reader of the CoT; who is unstated. |
| P10 | Models may test each other, but this risks "nested black boxes". | (ii) (a caution) | — |
| P11–P12 | Controls over access and action "must sit outside the model"; separate model, harness, action space. | (ii) | Enforced by the system, no reader needed. |
| P13 | Umbrella: "principles of observability". | — (heading) | — |
| P14 | Model diversity; no model verifies its own work. | (ii) | Architecture. |
| P15 | Every meaningful action leaves "tamper-proof human readable evidence"; outcomes reproducible without the model's attestation. | (i) | "We" must be able to reproduce; the reader is not named. |
| P16 | Continuous testing, including failures and attacks. | (ii) | Test engineering. |
| P17 | "Orgs" independently determine what a model can access and do. | (ii) | The organisation. |
| P18 | Independent auditability: validation independent of the intelligence validated. | (ii) relying on (i) evidence | An auditor (person or system), unnamed. |
| P19 | Containment; "an authorized person" can pause or shut down a model mid-task. | (ii) | One authorised person, inside the deployer. |
| P20 | Incident disclosure: "timely disclosure to those affected"; share what went wrong industry-wide. | (i) | Those affected (after failure) and the industry. |
| P21 | Trust the model least. | — (aphorism) | — |

**Count.** Of the substantive moves, three are disclosures or records to be read as their main content (P9, P15, P20); about ten are controls held by the organisation (P4–P8, P10–P12, P14, P16–P19; P18 relies on P15's record). **None is of type (iii).** The post contains no word for training, skill, literacy, learning by a person or education; its two "learn" words refer to what the enterprise has learned (P8) and to "learnings" shared across industry (P20), which is organisational and sectoral learning, not a person's growth.

**Where the people the systems act on appear.** Once: P20, "those affected", as recipients of "timely disclosure" when systems "fail or are compromised". The same paragraph sends lessons to the industry, not to them. P2 says the models act "on our behalf", i.e. for the deployer; the post never says toward whom. DXD's claims ledger already holds the sentence "the people on whom the model acts enter the framework only once, as recipients of a disclosure after something has failed" as supported (CLAIMS_01 C01-40) and C04-44/45 (the affected person "does not hold the brake").

**Who must read the P15 evidence.** The text does not name a reader. The sentence that follows says "We need to be able to reproduce how an outcome was achieved" (P15), so the reader is the deploying organisation, for the purpose of reconstruction. DXD G (B1, "What 'human readable evidence' asks of a person") read it as forensic rather than continuous vigilance; the auditor of P18 and the "authorized person" of P19 are the only candidates the post names. Nothing in the post makes the evidence available to those affected; P20 gives them a disclosure after failure, not access to the record.

**Bearing.**
- *Against the thesis as stated (point 4 in SOURCE_v4).* The post does not assume disclosure is sufficient. It says the one disclosure it insists on, CoT transparency, is "not sufficient or dependable" (P9), and most of its weight sits on controls that disclose nothing to anyone (P11–P12, P14, P17, P19). This is the DXD finding (C10 items 1–2; C01-05) and it stands. **The thesis is narrowed: the post does far more than disclosure.**
- *For a narrower thesis.* Every safeguard is either a text to be read or a control the organisation holds; nothing builds anyone's capacity (no (iii)); the people acted on appear once, as readers of a post-failure notice (P20). The burden the post creates for a person falls on the organisation's own staff (the P15 reader, the P19 brake-holder), and the post says nothing about how they will be equipped.
- *Narrows (a).* The burden is not placed on the end user, who is absent. It falls on the deployer's staff. "The user" of the three wrongs is two people (as SOURCE_v4 already flags): staff who must read the evidence, and the affected, who are only told.

---

## Q2. Microsoft's own published record on transparency and on users

### Q2.1 Microsoft Responsible AI Standard v2, General Requirements (June 2022) — `microsoft2022responsible`. *Full* (27 pp.).

- **Goal T1, "System intelligibility for decision making"** (p. 9): systems "that inform decision making by or about people are designed to support stakeholder needs for intelligibility of system behavior." **T1.1** requires teams to identify "1) stakeholders who will use the outputs of the system to make decisions, and 2) stakeholders who are subject to decisions informed by the system" (p. 9). **T1.2**: design "the system UX, features, reporting functions, and educational materials" so that those stakeholders can understand intended uses, "interpret relevant system behavior effectively", and "remain aware of the possible tendency of over-relying on outputs produced by the system ('automation bias')" (p. 9). **T1.3**: "Define and document the method to be used to evaluate whether each stakeholder who will make decisions or be subject to decisions based on the behavior of the system can interpret the relevant system responses reasonably well" (p. 9). **T1.4–T1.6**: release criteria, pre-release evaluation, and a gap plan if criteria are not met (p. 9).
- **Recommendation T1.2.1** (p. 10): "Follow the Guidelines for Human-AI Interaction when designing the system." T1.3.1: user researchers design evaluations "in appropriately realistic contexts of use" (p. 10).
- **Goal T2, "Communication to stakeholders"** (p. 11): documentation for "stakeholders who make decisions about whether to employ a system" and those "who develop or deploy systems that integrate with this system" (T2.1); "When the system is a platform service made available to external customers or partners, a Transparency Note is required" (T2.2). The Transparency Note's audience is the customer that deploys, not the person acted on.
- **Goal T3, "Disclosure of AI interaction"** (p. 12): inform people "that they are interacting with an AI system"; T3.3 requires a method to evaluate whether each stakeholder "is informed of the type of AI system they are interacting with or exposed to" (p. 12).
- **Goal A5, "Human oversight and control"** (p. 8): A5.2 requires the system elements ("system UX, features, alerting and reporting functions, and educational materials") that let overseers understand intended uses, "how to interpret system behavior", "when and how to override, intervene, or interrupt the system", and automation bias; **A5.4**: "evaluate whether each oversight or control function can be accomplished by stakeholders in realistic conditions of system use" (p. 8).

*Bearing.* **Narrows the thesis, and sharpens the contrast with the post.** Microsoft's own 2022 standard does more than disclose. For the person *subject to* a decision it requires designed educational materials, a test of whether that person "can interpret the relevant system responses reasonably well", and release criteria tied to the test (T1.1–T1.6). For overseers it requires a test that oversight "can be accomplished ... in realistic conditions" (A5.4). The October 2026 post has neither: its P15 reader and P19 brake-holder are never tested. So **the post is thinner than its own company's standard**. *For (b):* the competence the Standard tests is interpretation of the system's outputs, a reading competence; "educational materials" are the medium. *Not (iii) in the thesis's sense:* the Standard tests comprehension at release; it does not commit to growing a person's competence over time.

### Q2.2 Guidelines for Human-AI Interaction (Amershi et al., CHI 2019) — `amershi2019guidelines`. *Part* (abstract; Table 1, p. 3). DOI 10.1145/3290605.3300233 (Crossref-checked).

- Eighteen guidelines (Table 1, p. 3), named by the Standard as the design reference (T1.2.1, A5.3.1). Some are disclosures: G1 "Make clear what the system can do", G2 "Make clear how well the system can do what it can do", G11 "Make clear why the system did what it did", G18 "Notify users about changes". Others give the user controls over the system: G8 "Support efficient dismissal", G9 "Support efficient correction" ("Make it easy to edit, refine, or recover when the AI system is wrong"), G15 "Encourage granular feedback", G16 "Convey the consequences of user actions", G17 "Provide global controls" ("Allow the user to globally customize what the AI system monitors and how it behaves") (all p. 3).
- G13 "Learn from user behavior" is the system learning from the user, not the user learning (p. 3).

*Bearing.* **Narrows (a) and (b) for Microsoft's design canon, not for the post.** Microsoft's own interaction guidelines put controls in the user's hands (correction, dismissal, feedback, global controls) as well as disclosures. The post uses none of them; its controls are the organisation's (P17). **For (c):** none of the 18 guidelines is about growing the user's competence; the one "learn" guideline points the other way.

### Q2.3 Responsible AI Transparency Report 2024 — `microsoft2024responsible`. *Part* (pp. 4, 11, 25, 29, 33, 34 of 40).

- "We've published 33 Transparency Notes since 2019 to provide customers with detailed information about our platform services" (p. 4; again p. 25). Transparency Notes "follow a specific template to provide customers with detailed information about capabilities, limitations, and intended uses" (p. 25).
- For Copilots, "user-friendly notices in product experiences to provide important disclosures": "in-product disclosure to inform users that they are interacting with an AI application and citations to source material to help users verify information", plus "disclaimers about the potential for AI to make errors" (p. 25).
- **"Responsible use of AI applications is a shared responsibility between application developers and application users"** (p. 34). Developers should "design mitigations that enable appropriate use ... to minimize users' risk of overreliance" (p. 34). The research named includes "an Excel add-in prototype that helps users assess AI-generated code" and work on "how users interact with AI transparency features" (p. 34).
- Training is for employees: "99 percent of employees completed the responsible AI module" (p. 4; p. 29: "This journey begins with educating all of our employees").

*Bearing.* **For (a):** the company's own report names the user as co-bearer of responsibility (p. 34), and its user-facing measures are disclosures, citations "to help users verify", and disclaimers (p. 25). **For (b):** the means are texts. **Narrows (c) slightly:** a research prototype to help users assess AI output is the nearest thing to in-the-moment scaffolding I found, but it is a prototype, not a product commitment.

### Q2.4 Responsible AI Transparency Report 2025 — `microsoft2025responsible`. *Part* (PDF pp. 7, 22, 26, 28, 34 of 35).

- On the AI Act: "The first set of provisions that came into effect in February 2025 were the AI literacy requirements"; Microsoft "has undertaken various initiatives to promote AI literacy ... empowering our employees, customers, and others" (PDF p. 7, printed p. 11).
- "AI literacy efforts" (PDF p. 26, printed p. 49): literacy "helps ensure that individuals can make informed decisions regarding AI systems." Programmes for employees ("role-specific online learning paths"; Trust Code training); public resources ("AI courses that range from basic education on what AI is to technical training"); an "AI Literacy Starting Guide ... for vendors and customers"; an "AI Skills Navigator"; an AARP/OATS programme for adults over 50 funded by the Societal Resilience Fund. Customers "need to assess how literacy requirements in the EU AI Act ... apply to them".
- **A misstatement of the Act** (PDF p. 26): "The EU AI Act requires that deployers and providers of AI systems 'provide all relevant actors in the AI value chain with the insights required to ensure the appropriate compliance and its correct enforcement.'" The quoted words are from recital 20, where the subject is AI literacy itself ("AI literacy should provide all relevant actors ..."), not an operative duty on providers and deployers (recital 20, read in the OJ text). The operative duty is Article 4. Report footnote 74 cites a web edition (artificialintelligenceact.eu), not the OJ.
- Same page: new features "allow both users and admins greater visibility into Copilot-generated web queries"; admins can "search, audit, and eDiscovery" on them (PDF p. 26).
- Research on overreliance: mitigations "such as uncertainty highlighting, cognitive forcing functions, contrastive explanations, and AI critiques" (PDF p. 28, printed p. 53).

*Bearing.* **Narrows (c):** Microsoft does more than disclose; it runs training programmes and public courses aimed at literacy, and its research names in-the-interaction aids (cognitive forcing functions). **For (c) as framed:** what reaches users is courses and a curated reading list, i.e. training *about* AI outside the experience, and the literacy duty is read as a compliance item for customers. **For (b):** "visibility" into web queries is more to read; the audit version of it goes to admins.

### Q2.5 Microsoft 365 Copilot Transparency Note (now titled "Application card: Microsoft Copilot (for organizations)"), Microsoft Learn, ms.date 2026-10-05 — `microsoft2026application`. *Full* (page text).

- Limitations: "User training and adoption: Effective use of Microsoft Copilot requires users to understand its capabilities and limitations. There might be a learning curve, and users need to be trained."
- "Responsible AI is a shared commitment between Microsoft and its customers."
- Under **"End-users should:"** — "always review and verify AI-generated responses"; "users should review the responses generated by Microsoft Copilot and verify that they match their expectations and requirements"; and on overreliance: "we help mitigate this risk by adding disclaimers to our products but users should still make sure to review the accuracy of the answers."
- On grounding: "Users should always take caution and use their best judgment"; responses include "references to the sources for users to verify", and users "are also provided with explicit notice that they're interacting with an AI system and advised to check the source materials".
- Feedback: thumbs up/down; "Customer admins can review feedback".

*Bearing.* **The strongest primary support for (a) and (b) in this facet.** Microsoft's current user-facing transparency document assigns the residual work to the end user in so many words: review, verify, check the sources, use best judgment; the company's stated mitigation is "adding disclaimers". Competence is to come from users being "trained" (a limitation, not a Microsoft commitment). This is Microsoft, not Nadella's post; the paper must say so.

### Q2.6 AI Literacy Starting Guide (Office of Responsible AI, January 2025) — `microsoft2025ai`. *Full* (11 pp.).

- Purpose (p. 1): "AI literacy promotes knowledge so that we can make informed decisions regarding AI systems." "Microsoft's AI literacy materials provide a starting point to help you comply with these requirements" (the AI Act's Article 4, quoted in its 2024 wording in footnote 1).
- Form: a curated list of courses, modules, blog posts and webpages at three levels (fundamentals, intermediate, advanced) for "Using AI" and "Developing AI" (pp. 1–2). After the fundamentals, learners will be able to "Describe and define common terms" and "Understand basic concepts relating to responsible AI" (p. 2).

*Bearing.* **For (c):** Microsoft's answer to the literacy duty is a reading list and courses, separate from the product; it is training about AI, not support built into the experience. **For (b):** the medium of the literacy offer is text and video coursework.

### Q2.7 Microsoft Elevate (Brad Smith, 9 July 2025) — `smith2025microsoft`. *Full*.

- "over the next five years, we will donate on a global scale more than $4 billion in cash and AI and cloud technology to K-12 schools, community and technical colleges, and nonprofits".
- "the Microsoft Elevate Academy will help 20 million people earn an in-demand AI skilling credential ranging from foundational fluency to advanced technical training."
- Framing: "putting people first by equipping them with the skills, knowledge, and tools to thrive with AI."

*Bearing.* **Against (c) read as "Microsoft does nothing for competence".** Microsoft makes a large public skilling commitment and uses the word "fluency". **For (c) read precisely:** the commitment is credentials and courses delivered through schools, colleges, LinkedIn and GitHub, outside the systems people meet. It is a training programme, not scaffolding inside the mediated experience, and it is not in the post. Its figures are Microsoft's own targets.

---

## Q3. The EU AI Act: where the law puts the duty

Source: Regulation (EU) 2024/1689, OJ L 12.7.2024, from EUR-Lex (identical to the Publications Office copy), and Regulation (EU) 2026/1744 (Digital Omnibus on AI), OJ L 24.7.2026. `eu2024aiact`, `euomnibus2026`. *Part* (articles named). Z_gap_search R1–R2 and N2 already read Arts 3(56), 4, 13, 14, 26, 86, 113 and the Omnibus; I re-read each from EUR-Lex and add Arts 50 and 73 and the Omnibus Art 50 and Art 113 changes.

- **Art 3(56)** defines AI literacy as "skills, knowledge and understanding that allow providers, deployers and affected persons ... to make an informed deployment of AI systems, as well as to gain awareness about the opportunities and risks of AI and possible harm it can cause". Affected persons are in the definition.
- **Art 4 as enacted** (applied from 2 February 2025, Art 113): "Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, ... and considering the persons or groups of persons on whom the AI systems are to be used." The duty is on organisations; the persons made literate are their staff and agents; the people the systems are used on are only to be "considered".
- **Recital 20**: for affected persons, literacy means "the knowledge necessary to understand how decisions taken with the assistance of AI will have an impact on them"; the Board should "promote AI literacy tools, public awareness"; codes of conduct are "voluntary". No operative article gives affected persons a literacy measure.
- **Art 4 as replaced by the Omnibus** (Art 1(5) of Reg 2026/1744; in force on the third day after publication of 24.7.2026): providers and deployers "shall take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf ... This obligation does not require providers or deployers to guarantee any specific level of AI literacy of any individual." Para 2: the Commission and Member States "shall support and facilitate the efforts of providers and deployers"; para 3: the Board adopts recommendations. **Recital 8** gives the reason: "imposing such obligations creates an additional compliance burden, particularly for smaller enterprises, whereas AI literacy should be a strategic priority, regardless of regulatory obligations".
- **Art 13(1)**: high-risk systems must be "sufficiently transparent to enable deployers to interpret a system's output and use it appropriately"; 13(2): instructions "comprehensible to deployers". Transparency runs to the deployer.
- **Art 14(1)**: oversight "by natural persons"; **14(4)(b)** the overseer must "remain aware of the possible tendency of automatically relying or over-relying on the output ... (automation bias)"; **14(4)(e)** "interrupt the system through a 'stop' button". **Art 26(2)**: deployers assign oversight "to natural persons who have the necessary competence, training and authority, as well as the necessary support". Recital 91: "an adequate level of AI literacy, training and authority". The overseer is the deployer's.
- **Art 26(11)**: deployers of Annex III systems that make or assist decisions "shall inform the natural persons that they are subject to the use of the high-risk AI system". Notice only.
- **Art 50(1)**: providers ensure that "the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect". **50(2)**: synthetic outputs "marked in a machine-readable format". **50(3)–(4)**: deployers disclose emotion recognition, biometric categorisation, deep fakes, and AI-generated public-interest text. **50(5)**: the information "shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure" and conform to accessibility requirements. The Omnibus gives legacy generative systems until 2 December 2026 for 50(2) (Art 1, amending Art 111) and rewrites 50(7) on codes of practice.
- **Art 73**: serious incidents are reported by providers "to the market surveillance authorities" (73(1)); in the paragraphs I read, no notice to affected persons is required.
- **Art 85**: anyone may complain to a market surveillance authority. **Art 86(1)**: an affected person subject to a deployer's decision based on an Annex III system that produces legal or similarly significant adverse effects has "the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken"; residual (86(3)).
- **Dates** (Omnibus, replacing Art 113(c)): Chapter III Sections 1–3 (so Arts 13, 14, 26) apply from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems.

*Bearing.*
- **For (a) and (b).** Every duty the Act owes the person on the receiving end is a text: a notice of AI interaction (Art 50(1), (5)), a notice of being subject to a high-risk system (Art 26(11)), an explanation on request after a decision (Art 86). The "reasonably well-informed, observant and circumspect" person of Art 50(1) is the law's model reader, and disclosure is excused when that reader would notice anyway.
- **For (c), strongly.** Art 4 is the one place the Act addresses competence. It puts the duty on organisations, for their own staff and agents; affected persons appear in the definition (3(56)) and recital 20 but not in the operative duty. In July 2026 the Omnibus weakened even that duty from "ensure ... a sufficient level" to "support the development of", with no "specific level", for stated reasons of compliance burden (recital 8). Three months before the post, the law moved away from building competence.
- **Narrows (c).** The Act does do something besides disclosure: it requires competent, trained overseers with "the necessary support" (Art 26(2)), names automation bias (Art 14(4)(b)), and gives the affected a complaint route (Art 85). It treats competence as an organisational duty, not as the reader's own burden. But the competence is the deployer's staff's, not the affected person's.
- **Against reading the post as worse than the law on P20.** The post asks for "timely disclosure to those affected" after failures (P20). The Act's incident regime, in the paragraphs I read, reports serious incidents to authorities, not to the people affected (Art 73). On that point the post asks for more than the law.

---

## Q4. Commentary on the post

- **Sudjianto, A. (2026, 10 October). "When AI Becomes an Insider, Who Is Left to Check Its Work?" Substack** — `sudjianto2026when`. *Full*. Published the day of the post (datePublished 2026-10-10T17:24 UTC). Agrees with the separation of intelligence from authority. Argues: "Companies are rushing to automate the very work through which people develop the expertise needed to independently verify AI"; "An audit trail tells us what the agent did, not whether it should have done it. And an emergency stop is useful only when something recognizes that intervention is necessary"; "An experienced model validator does not become experienced by reading validation reports"; "There is a considerable difference between using AI to help someone understand a problem and using AI to eliminate the need for that person to understand it." Recommends: engineer verification into the system "rather than relying on human review as the primary safeguard"; "redesign junior roles around developing judgment, not merely supervising AI outputs"; measure "whether AI adoption is improving or weakening institutional competence", e.g. by planted-error exercises.
  - *Bearing.* **For (c)** from inside the enterprise frame: the post's oversight depends on competence it does not say how to grow, and reading records does not grow it. **For (b)**: competence comes from doing the work, not reading reports. **Narrows (a)**: Sudjianto, like the post, wants verification engineered into the system, so less of the burden falls on a human reader. His subject is the organisation's staff, not the affected; he does not mention end users or those affected.
- **News and vendor coverage.** TNW, Business Standard, Security Boulevard, Forbes (blocked) are in DXD facet G B1 and its cards (`constantin2026nadella`, `kumari2026nadella`). I found no further critique, and nothing on the affected-person or end-user angle (search rows 7–8).

---

## For, narrows, against

### For
1. The post contains no move of type (iii); "skill", "literacy", "people" and "user" do not occur, and its only "learn" words are organisational (P8) and sectoral (P20).
2. The people acted on appear once, as recipients of disclosure after failure (P20); they are given neither the record (P15) nor the brake (P19) (DXD C01-40, C04-44).
3. Microsoft's current Transparency Note tells end users to "review and verify", says the company mitigates overreliance "by adding disclaimers" while "users should still make sure to review", and treats user training as a limitation (`microsoft2026application`).
4. Microsoft's 2024 report calls responsible use "a shared responsibility between application developers and application users" (p. 34), and its user measures are disclosures, citations and disclaimers (p. 25).
5. Microsoft's literacy answer is a curated course list and external credential programmes (Starting Guide; Elevate), not support inside the experience.
6. The AI Act's duties to the affected are all notices or explanations (Arts 26(11), 50, 86); its one literacy duty binds organisations for their own staff (Art 4), and the Omnibus cut it to "support the development of" with no guaranteed level (Reg 2026/1744 Art 1(5), recital 8).
7. The only substantive commentary argues that oversight needs competence grown by doing the work, which records do not build (Sudjianto).

### Narrows
1. **The post does much more than disclosure.** Most of its moves are controls held by the organisation (P4–P8, P10–P12, P14, P16–P19), and it calls CoT transparency "not sufficient or dependable" (P9). The thesis that the post "assumes disclosure is sufficient" does not hold as stated; the defensible version is that its safeguards are texts or organisational controls and none builds a person's capacity (DXD C7, C10; C01-05).
2. The burden in the post falls on the organisation's staff (P15 reader, P19 brake-holder), not on end users, who are absent; "the user" must be split in two.
3. Microsoft's own Standard (2022) goes beyond disclosure: it requires evaluating whether people *subject to* decisions can interpret outputs (T1.1–T1.3) and whether overseers can perform oversight in realistic conditions (A5.4). Its design guidelines give users correction, dismissal, feedback and global controls (Amershi G8, G9, G15–G17). These measures are absent from the post, not from Microsoft.
4. Microsoft runs large training programmes (Elevate; employee literacy paths) and its research names in-the-moment aids (cognitive forcing functions; an Excel add-in prototype to help users assess AI output). The claim must be "no scaffolding inside the experience", not "no investment in competence".
5. The AI Act requires the deployer's overseers to have competence, training, authority and "support" (Art 26(2)) and names automation bias (Art 14(4)(b)); competence is an organisational duty there, not only the reader's burden.

### Against
1. On incident disclosure, the post asks for more than the AI Act: "timely disclosure to those affected" (P20) against the Act's reporting to authorities (Art 73 as read).
2. Microsoft's Standard tests comprehension by the people subject to decisions (T1.3). That is a designer's duty to check that the reader can read, which cuts against "the burden is simply placed on the person" as a description of Microsoft's own governance (not of the post).

---

## What the paper can say (notes for the drafter)

1. Nadella's post offers two kinds of safeguard: records and disclosures to be read (CoT transparency, P9; "tamper-proof human readable evidence", P15; incident disclosure, P20) and controls held by the deploying organisation (P5, P11–P12, P14, P17, P19); none of its moves builds a person's capacity (Nadella 2026; DXD `library/nadella2026models.md`).
2. The post does not treat disclosure as sufficient: it calls chain-of-thought transparency "not sufficient or dependable" (P9) and rests mainly on controls outside the model (P11–P12, P17).
3. The people the systems act on appear once, as recipients of "timely disclosure" after failure (P20); the evidence of P15 is for the organisation to reconstruct outcomes, and the brake of P19 belongs to "an authorized person".
4. Microsoft's own Responsible AI Standard (2022) asks more than the post: it requires teams to evaluate whether people subject to a system's decisions "can interpret the relevant system responses reasonably well" (T1.3, p. 9) and whether overseers can perform oversight "in realistic conditions" (A5.4, p. 8).
5. Yet the competence the Standard tests is interpretation of the system's outputs, delivered through "educational materials" and disclosures (T1.2, A5.2), a reading competence.
6. Microsoft's current user-facing documentation tells end users to "review and verify" outputs and states that it mitigates overreliance "by adding disclaimers", while "users should still make sure to review the accuracy" (Microsoft 365 Copilot transparency note, 2026).
7. Microsoft's 2024 Transparency Report calls responsible use "a shared responsibility between application developers and application users" (p. 34).
8. Microsoft's answer to the literacy duty is courses and credentials outside the product: a curated AI Literacy Starting Guide (2025) and a skilling programme promising 20 million credentials "ranging from foundational fluency to advanced technical training" (Smith 2025).
9. The EU AI Act's duties toward affected persons are notices and explanations (Arts 26(11), 50(1), 50(5), 86(1)); its only literacy duty binds providers and deployers for "their staff and other persons ... on their behalf" (Art 4).
10. In July 2026 the Digital Omnibus replaced that duty with one to "support the development of AI literacy", adding that it "does not require ... any specific level of AI literacy of any individual" (Reg 2026/1744, Art 1(5)), citing compliance burden (recital 8).
11. On one point the post exceeds the law: it asks for disclosure to those affected by incidents (P20), where the AI Act's incident regime reports to authorities (Art 73).
12. The first substantive commentary on the post accepts its architecture and argues that its oversight depends on expertise that reading records does not build: "An experienced model validator does not become experienced by reading validation reports" (Sudjianto 2026).

## Gaps

- I found no work, in the commentary searched (rows 7–8) or in DXD facet G's searches, that criticises the post for omitting the people the systems act on or for building no one's competence. The paper's charge appears to be new.
- I found no Microsoft commitment, in the documents read (RAI Standard v2; Transparency Reports 2024 and 2025, pages read; the Copilot transparency note; the AI Literacy Starting Guide; the Elevate post), to scaffold an end user's competence inside a product over time. The nearest items are research prototypes and research on cognitive forcing functions (2024 p. 34; 2025 PDF p. 28), not product requirements.
- I found no operative article of Regulation (EU) 2024/1689, as amended by 2026/1744, that requires any measure to build the competence of affected persons; they appear in Art 3(56) and recital 20 only.
- Not read: the rest of the two Transparency Reports; Microsoft's Trust Center AI Act page; any 2026 Transparency Report; the full Amershi paper beyond the abstract and Table 1; Art 73 paragraphs beyond those printed in the first block I read.
