# Stage 2 card verification: four phygital cards

Independent verifier, 13 Nov 2026 (v8 stage 2). I did not write these cards. I checked them against the
version-of-record PDFs only, and used the readers' reports (READ_batat_new.md, READ_berthon2026.md) to locate
passages, never as evidence.

## Method

- I read each source in full, page by page, with `pdftotext -f N -l N` (raw reading order, and `-layout` for
  two-column pages). I read figures and tables from rendered pages: paradigm Figure 1 (p. 359), HFPV Figure 1
  (p. 274), PHIVE Table 1 (p. 5), Figure 1 (p. 9) and Table 4 (p. 16).
- A script matched every quoted string in each card against the text of each page, on letters and digits
  only. That match tolerates ligatures, typographic quotation marks, dashes and line-break hyphens, and it
  catches changed, added or missing words. I checked by eye every string the script could not place: figure
  and table text, quotations that cross a page break interrupted by a running head, and quotations from other
  documents (call for papers, PH-CX, JOURNAL_SPEC.md).
- I ran term searches over every page, including references and biographies, for the cards' absence claims.
- Verdicts. Quotations: PASS (verbatim at the cited page) or FAIL. Claims: SUPPORTED, PARTLY, NOT SUPPORTED.

| Source | PDF pages | PDF index → printed page | Card's locators |
|---|---|---|---|
| batat2024paradigm | 9 | printed = PDF + 356 (357-365) | printed pages; stated correctly |
| batat2026hfpv | 13 | printed = PDF + 268 (269-281) | printed issue pages; stated correctly |
| batat2026phive | 22 | PDF 1 is a T&F cover sheet; printed = PDF − 1 (1-21) | online-first printed pages; stated correctly |
| berthon2026accesship | 18 | printed = PDF + 407 (408-425) | printed pages; stated correctly |

## Overview

| Card | Quotations checked | FAIL | Claims checked | PARTLY | NOT SUPPORTED | Verdict |
|---|---|---|---|---|---|---|
| batat2024paradigm | 19 | 0 | 25 | 0 | 0 | PASS WITH CORRECTIONS |
| batat2026hfpv | 47 | 0 | 29 | 5 | 0 | PASS WITH CORRECTIONS |
| batat2026phive | 48 | 0 | 25 | 5 | 0 | PASS WITH CORRECTIONS |
| berthon2026accesship | 65 | 0 | 33 | 3 | 0 | PASS WITH CORRECTIONS |

Every quotation in all four cards is verbatim at the page the card gives. The corrections concern
paraphrase and inference, chiefly in the "What the paper may say" sentences, plus omissions bearing on who
owes safeguards and on seamlessness.

---

## 1. batat2024paradigm

### Bibliographic fields

| Field | Card | PDF (p. 357 unless stated) | Verdict |
|---|---|---|---|
| Title | Guest Editorial: The Phygital Research Paradigm: … Hybrid Physical-Digital Realms | "Guest editorial: The phygital research paradigm: philosophical foundations for examining consumer experiences and behaviors in hybrid physical-digital realms" | PASS (title case only) |
| Author | Batat, Wided | Wided Batat, signature p. 363 | PASS |
| Year | 2024b (label) | 2024 | PASS |
| Venue | Qualitative Market Research | Qualitative Market Research: An International Journal | PASS (subtitle dropped) |
| Vol/issue/pages | 27(3), 357-365 | Vol. 27 No. 3, 2024, pp. 357-365 | PASS |
| DOI | 10.1108/QMR-06-2024-202 | DOI 10.1108/QMR-06-2024-202 | PASS |

### Quotations

| # | Quotation (opening words) | Card locator | Verdict |
|---|---|---|---|
| Q1 | "Batat (2022a) defines phygital as a human-centric holistic ecosystem … and vice versa." (also the sub-quotations "a seamless delivery of value" and "a seamless delivery of value from digital to physical realms, and vice versa") | Key facts; Where it bears; May say 2 | p. 357 PASS |
| Q2 | "These spaces seamlessly blend physical and digital elements … paradoxical behaviors." | Key facts | p. 357 PASS |
| Q3 | "The phygital research paradigm is a novel approach … between physical and digital settings." | Key facts | p. 358 PASS |
| Q4 | "anchored in four key philosophical foundations – … – offers researchers a comprehensive and flexible framework for exploring phenomena occurring in hybrid contexts" | Key facts | p. 357 PASS. The string is a verbatim substring, but in the source "offers" is the main verb of "the phygital research paradigm, which is anchored in …". The card's frame ("It is 'anchored … – offers researchers …'") does not parse. If reused, cut the quotation at "multimethodology". |
| Q5 | "Instead, it promotes a triadic understanding that encompasses the object, the subject and the context." | Key facts; May say 3 | p. 359 PASS |
| Q6 | "may commence in a physical setting, such as in-store, … – or vice versa" | Key facts | p. 358 PASS |
| Q7 | "discern subtle patterns associated with the continuity or discontinuity between physical and digital study settings." | Key facts; May say 4 | p. 357 PASS |
| Q8 | "steers the ethical considerations researchers must address when designing their study frameworks." | Key facts | p. 360 PASS |
| Q9 | Figure 1: "Ensures research protocol's value and ethics" | Key facts | p. 359 PASS (rendered page) |
| Q10 | Figure 1: "Guarantees authentic interpretation of participants' voices" | Key facts | p. 359 PASS (rendered page) |
| Q11 | "as co-researchers, content creators, curators and collaborators" | Key facts | p. 361 PASS |
| Q12 | "This guarantees that the participants' voices are authentically represented …" | Key facts | p. 361 PASS |
| Q13 | Schmitt: "acknowledges issues and concerns about the use of generative AI, … 'black box' problem" | Key facts | p. 362 PASS |
| Q14 | "Finally, it is crucial to address the challenges posed by the subjectivity and conceptual fluidity …" | Key facts | p. 363 PASS |
| Q15 | "from one setting to another, and vice versa" | Critical notes | p. 357 PASS |
| Q16 | Special issue title "The Future of Interpretivist Research Methodology is Phygital" | Summary | p. 358 PASS |
| Q17 | CfP: "phygital service research (PSR) (Batat, 2024b)" | Critical notes | cfp2025apa/cfp.pdf PDF p. 2 PASS |
| Q18 | HFPV: "phygital service research (PSR) paradigm ... (Batat, 2024a)" | Critical notes | batat2026hfpv p. 270 PASS (ellipsis marked) |
| Q19 | PHIVE: "The phygital research paradigm (Batat, 2024b, 2025)" | Critical notes | batat2026phive p. 6 PASS |

### Claims

| # | Claim | Card locator | Verdict |
|---|---|---|---|
| C1 | Short guest editorial, pp. 357-365, introducing the QMR special issue (p. 358) | Summary | SUPPORTED |
| C2 | Proposes the paradigm on four foundations (p. 357; Fig. 1, p. 359) | Summary | SUPPORTED |
| C3 | "Each foundation is illustrated by an article from the issue" | Summary | SUPPORTED. Most foundations get more than one: liquid ontology, Levy & Sabri and Mele et al. (p. 360); epistemology, Parnwell & Meng and Yao et al. (p. 362); multimethodology, Johnson & Barlow, Schöps & Jaufenthaler, Yu et al., Schmitt (p. 362). |
| C4 | Concerns research design throughout; prescribes nothing to firms, platforms, hosts or regulators | Summary | SUPPORTED (the publisher's author biography aside; see omission O2) |
| C5 | Hospitality, employees, governance, AI in service delivery not discussed | Summary | SUPPORTED |
| C6 | AI appears once, as a research tool (Schmitt 2023, p. 362) | Summary | SUPPORTED (one passage on p. 362; also in Schmitt's reference title, p. 364) |
| C7 | Signed by Batat alone (p. 363) | Key facts | SUPPORTED |
| C8 | "digitalization" and "physicalization" do not occur | Key facts | SUPPORTED (term search, both spellings) |
| C9 | Discontinuity appears as something to study, not to remove | Key facts | SUPPORTED |
| C10 | The editorial's ethics belong to the researcher | Key facts | SUPPORTED |
| C11 | Voice is a matter of research protocol | Key facts | SUPPORTED |
| C12 | The p. 363 sentence is the only caution about its own paradigm | Key facts | SUPPORTED |
| C13 | "PSR" and "phygital service research" occur nowhere; outside references and biography, no host, hospitality, employee, trust, fairness, well-being, governance, accountability, responsibility, complaint, recourse; "guest" only in "guest editorial/editor" | Key facts | SUPPORTED. "host" matches only inside "Ghost" (Koestler reference, p. 364). |
| C14 | CfP attributes PSR to this editorial (CfP, PDF p. 2) and lists it as 2024b | Critical notes | SUPPORTED. Locator correction: the attribution is on CfP PDF p. 2, but the reference entry that identifies its 2024b as this editorial is on CfP PDF p. 4. |
| C15 | HFPV labels this editorial 2024a and PH-CX 2024b (HFPV p. 280); CfP, PHIVE and the library label it 2024b | Critical notes | SUPPORTED (HFPV p. 280; PHIVE p. 20; CfP PDF p. 4) |
| C16 | digitalization/physicalization come from PH-CX (batat2024phcx, pp. 1230-1231) | Critical notes | SUPPORTED (I found the terms on PH-CX printed pp. 1230 and 1231, and on 1236) |
| C17 | `not-that-triad` supported by the object-subject-context triad | Critical notes | SUPPORTED |
| C18 | The editorial prescribes no safeguards and is not evidence for the gap statement | Critical notes | SUPPORTED |
| C19 | It supplies two usable lines on seamlessness and the triad | Where it bears | SUPPORTED; see omission O1 for a third "seamless" use |
| C20 | It says nothing on who owes what to whom | Where it bears | SUPPORTED |
| M1 | "rests on four foundations: liquid ontology, dual axiology, interpretivist epistemology and multimethodology (Batat 2024b: 357)" | May say | SUPPORTED |
| M2 | "Restating her definition of phygital, Batat (2024b: 357) gives its aim as 'a seamless delivery …'" | May say | SUPPORTED |
| M3 | Triad quotation (359); "its third term is a context, not a party" | May say | SUPPORTED. "Not a party" is the reader's gloss; the text and Figure 1 ("object, subject, and context") are consistent with it. |
| M4 | "The paradigm, Batat (2024b: 357) writes, helps researchers 'discern …'" | May say | SUPPORTED (source: "This adaptability empowers them to discern …") |
| M5 | Not to be said: that the editorial defines or develops PSR | May say | SUPPORTED |

### Omissions

- **O1 Seamlessness, a third use.** The editorial endorses Mele et al.'s phygital customer journey as an
  illustration of liquid ontology, and one of its four elements is "(2) blended contexts (the seamless
  integration of digital and physical spaces);" (p. 360). The card lists only the two p. 357 uses. The text
  never questions seamlessness; this third use is reported approvingly.
- **O2 The only named duty-bearers in the PDF are in the publisher's author biography.** Batat's research
  examines "how policy makers and businesses can adopt responsible initiatives that help consumers to achieve
  their well-being" (p. 364). The card's absence claim explicitly excludes the biography, so the claim holds,
  but a reader searching the PDF for "responsible" will find this line. It is not the editorial's argument
  and should not be cited as such.
- **O3 (minor) Research ethics on the agenda.** "An inquiry into ethical considerations during research
  planning and execution in these environments could yield valuable insights." (p. 363). This supports the
  card's reading that ethics here are the researcher's.
- Responsibility among several firms: the editorial says nothing. Confirmed after a full read.

**Overall: PASS WITH CORRECTIONS** (0 FAIL, 0 NOT SUPPORTED; fix the CfP locator, add the p. 360 seamless
use, and trim Q4 if reused).

---

## 2. batat2026hfpv

### Bibliographic fields

| Field | Card | PDF (p. 269) | Verdict |
|---|---|---|---|
| Title | Phygital Science and the Future of Macromarketing: The Human First Phygital Value (HFPV) Framework for Integrated Physical-Digital Ecosystems | identical | PASS |
| Author | Batat, Wided | Wided Batat | PASS |
| Year | 2026 | 2026 | PASS |
| Venue | Journal of Macromarketing | Journal of Macromarketing | PASS |
| Vol/issue/pages | 46(3), 269-281 | "2026, Vol. 46(3) 269–281"; PDF metadata Subject "Journal of Macromarketing 2026.46:269-281" | PASS |
| DOI | 10.1177/02761467261450501 | DOI: 10.1177/02761467261450501 | PASS |
| Online-first date | card: none printed | none printed (term search) | PASS |

### Quotations

All 47 strings are verbatim at the cited page. Grouped by page:

| Page | Quotations (opening words) | Verdict |
|---|---|---|
| 269 | "Editorial"; "technocentric and efficiency-driven" (abstract); "a cross-disciplinary field explaining how integrated physical-digital ecosystems …"; "seek experiences that support their sense of agency and humanity" | PASS |
| 270 | "HFPV foregrounds human dignity, emotional safety, ethical design …" (the sentence starts on p. 269, the quoted part on p. 270); "this orientation is reflected in phygital service research (PSR) paradigm …"; "Phygital science builds on these foundations through the PSR dimensions …"; "Batat, 2025a" | PASS |
| 271 | "Accordingly, HFPV is defined as: …"; "networked systems in which information flows seamlessly …"; "Central to this transformation is the emergence of the Chief Phygital Officer …"; "responsible for ensuring coherence within the phygital enterprise"; "Roederer et al. (2026) illustrate how AI becomes a "third agent" …"; Gustafsson et al. "conceptualize phygital work experience (PH-WE) …"; "Bakrim et al. (2025) reveal paradoxes …" | PASS |
| 272 | Table 1: "Reframes service ecosystems as sociotechnical triads (human-AI-organization) in the phygital marketplace."; "Batat, 2025" | PASS |
| 273 | "The framework therefore positions human-first experience, not efficiency or channel optimization, …"; "not efficiency or channel optimization"; "Technological suitability and multimodal continuity"; "Technologies must be understood as sociotechnical actors …" | PASS |
| 273-274 | "Institutions play a critical role … rather than undermine it." | PASS (break after "and how") |
| 274 | "a structural requirement rather than an optional consideration" | PASS |
| 275 | "Ethical governance requires a human-first logic … undermine trust."; "ethical AI, data governance, and algorithmic accountability"; "communities, institutions, vulnerable groups, and civil society …"; "Value in phygital ecosystems is poly-created …"; "Human-first phygital organizations institutionalize these adaptive mechanisms …"; "into organizational learning and system redesign"; "designing seamless, coherent, and emotionally resonant transitions …"; "a societal mechanism for enabling inclusion, reducing friction, and fostering trust" | PASS |
| 276 | "ensure equitable access to technological affordances, protect individuals from harm"; "When systems generate exclusion, … signal the need for redesign."; "dynamic social institutions capable of learning, self-correction, and ethical evolution."; "Systems that support clarity, reduce friction, …"; "risk eroding trust, diminishing employee well-being, …" | PASS |
| 277 | "In this way, communities act as co-governors …"; "When well-being indicators reveal harm or exclusion, …"; "bridges micro-macro gaps via integrating insights …" | PASS |
| 277-278 | "As AI systems, data infrastructures, and algorithmic decision-making … firms must ensure …" | PASS |
| 278 | "Second, phygital science calls for robust "algorithmic accountability". … Policies should mandate …"; "ensure transparency, fairness, and emotional safety"; "Macromarketing scholars must examine how institutions …"; "accountability structures"; "how hybrid embodiment, contextual fluidity, and multimodal continuity affect …" | PASS |
| 279 | Special issue "Phygital Marketing for Positive Impact" | PASS |
| 280 | Reference labels: 2024a = the QMR editorial, 2024b = PH-CX, 2025a = PSR (JSM) | PASS |

### Claims

| # | Claim | Card locator | Verdict |
|---|---|---|---|
| C1 | Headed "Editorial"; introduces the special issue (p. 279); developed with the APA Summit 2025 (p. 269) | Summary | SUPPORTED |
| C2 | Phygital science as paradigm, HFPV as architecture, four components (p. 273; Fig. 1, p. 274) | Summary | SUPPORTED (Figure 1 checked on the rendered page) |
| C3 | Macro level, against technocentric transformation | Summary | SUPPORTED |
| C4 | Gives stewardship to firms, the CPO, institutions and regulators, communities; calls for algorithmic accountability | Summary | SUPPORTED |
| C5 | Never mentions hospitality, hotels, guests or hosts (also tourism) | Summary; Key facts | SUPPORTED (term search, references included) |
| C6 | HFPV's 2024a is the QMR editorial (p. 280) | Key facts | SUPPORTED |
| C7 | Beneficiaries named as populations | Key facts | SUPPORTED |
| C8 | Many actors acknowledged, no allocation among them | Key facts | SUPPORTED (see omission O1) |
| C9 | Allocation placed on the agenda, not answered (p. 278) | Key facts | SUPPORTED |
| C10 | Feedback is aggregate and leads to redesign | Key facts | SUPPORTED |
| C11 | Correction belongs to the system | Key facts | SUPPORTED |
| C12 | Seamlessness and friction reduction stated as goals | Key facts | SUPPORTED (see omission O6) |
| C13 | HFPV names who acts and for whom; "says neither to whom … nor which … owes them" is false of this text | Critical notes | SUPPORTED |
| C14 | HFPV divides no duty among several firms that together deliver one service | Critical notes | SUPPORTED |
| C15 | The CPO secures coherence "within the phygital enterprise" (p. 271), "a single organization" | Critical notes | **PARTLY.** The quotation is exact, but HFPV also gives the CPO an ecosystem role: the CPO "orchestrates interdependencies among physical environments, digital platforms, human experience, and societal impact" (p. 271) and "serves as a cross-functional integrator who coordinates these participatory processes (Batat, 2026), ensuring that diverse voices are included in decision-making and that phygital ecosystem collaboration reflects human-first priorities" (p. 275). "A single organization" is the reader's inference, and p. 275 contests it. |
| C16 | Beneficiaries never individuals holding a claim | Critical notes | SUPPORTED |
| C17 | "algorithmic accountability" (p. 278) "names no party that renders the account and no party to whom it is rendered" | Critical notes | **PARTLY.** The "to whom" half holds: no addressee appears anywhere. But p. 275 names an overseer: "the CPO plays a critical stewardship role, overseeing ethical AI, data governance, and algorithmic accountability". |
| C18 | "Every feedback mechanism is aggregate and prospective (pp. 275-278)" | Critical notes | **PARTLY.** They are aggregate, as the card says. "Prospective" is contestable: the loops "allow systems to respond to lived experience in real time. These loops integrate signals from communities, behavioral patterns, emotional states, and emerging risks" (p. 275). The next sentence of the card holds: none is a route for one person's failed case. |
| C19 | `framing-argued-past` contested by "sociotechnical actors" (p. 273) | Critical notes | SUPPORTED |
| C20 | Roederer et al.'s human-AI-organization triad threatens `not-that-triad` | Critical notes | SUPPORTED (as HFPV reports it, pp. 271-272; Roederer not read) |
| C21 | Issue pagination; PSR cited as 2025a (p. 270) and 2025 (p. 272) | Critical notes | SUPPORTED |
| C22 | Editorial, programmatic, no data | Critical notes | SUPPORTED |
| C23 | HFPV works at macro level and places phygital service research at micro/meso (p. 277) | Where it bears | SUPPORTED |
| M1 | Ethical responsibility "a structural requirement …" (274); CPO oversees "ethical AI, data governance, and algorithmic accountability" (275) | May say | SUPPORTED |
| M2 | CPO "responsible for ensuring coherence within the phygital enterprise" (271): "one enterprise, where the cases this paper examines involve several" | May say | **PARTLY.** The quotation is exact, but "one enterprise" is the reader's inference and p. 275 (C15) contests it. A safer sentence: "HFPV charges the CPO with 'ensuring coherence within the phygital enterprise' (271) and does not say whose CPO answers when several firms deliver one service." |
| M3 | Calls for "algorithmic accountability" and "asks regulators to 'ensure transparency, fairness, and emotional safety'" (278); does not say which firm renders that account, or to whom | May say | SUPPORTED. Wording: the source's subject is "regulatory frameworks must ensure", not regulators. |
| M4 | Loops translate feedback "into organizational learning and system redesign" (275). "They improve the system for later users" | May say | **PARTLY.** The quotation is exact, but "for later users" is the reader's inference, and the same bullet says the loops let systems "respond to lived experience in real time" (p. 275). The defensible point is narrower: the loops act on the system through aggregate signals, and none routes one guest's case to someone able to correct it. |
| M5 | Leaves to future research how institutions "shape the rules, norms, and accountability structures …" (278) | May say | SUPPORTED |
| M6 | "not efficiency or channel optimization" (273) yet counts "designing seamless, coherent, and emotionally resonant transitions" among value-creating processes (275) | May say | SUPPORTED (the phrase sits in the "Phygital Processes" component, first bullet) |

### Omissions bearing on who owes safeguards, and on seamlessness

- **O1 Shared authorship among stakeholders.** "Participation is therefore a form of shared authorship that
  recognizes the interdependencies among stakeholders and the entangled nature of integrated
  physical-digital environments." (p. 275). This is HFPV's nearest approach to dividing something among several
  parties. What it divides is authorship of design and governance, not a duty.
- **O2 The CPO's ecosystem role** (p. 275, quoted under C15). This bears directly on M2.
- **O3 Accountability as something the ecosystem demonstrates.** Sustainable phygital ecosystems "cultivate
  institutional trust by embedding ethical responsibility into governance structures and by demonstrating
  accountability in the design and operation of phygital environments." (p. 276). The subject is the
  ecosystem, not a party. This supports the card's argument, and the card does not list it among the
  "accountability" loci.
- **O4 Accountability as a product of community pressure.** "Public concerns about privacy, fairness, or
  emotional safety can lead to regulatory interventions, ethical standards, or new forms of accountability."
  (p. 277). No bearer is named.
- **O5 Accountability as an institutional input.** "Phygital ecosystems are poly-produced by institutional
  arrangements, governance structures, and regulatory frameworks that shape fairness, access, accountability,
  and trust across integrated physical-digital environments." (p. 273).
- **O6 Seamlessness: discontinuity named as the threat.** Orchestration must ensure "that participation,
  access, and well-being are not disrupted by technological or contextual discontinuities." (p. 275). This
  endorses seamlessness.
- **O7 The one two-sided statement about technology, not applied to seamlessness.** Technology "can reduce
  cognitive load or intensify it, enhance emotional connection or erode it, expand access or reinforce
  exclusion." (p. 273).
- **O8 Cross-environment standards.** Policy should set "integrated physical-digital infrastructure standards
  that ensure safety, accessibility, and interoperability across environments" (p. 278). This is the nearest
  HFPV comes to coordination across separate systems, and it allocates nothing among firms.

**Overall: PASS WITH CORRECTIONS** (0 FAIL, 0 NOT SUPPORTED, 5 PARTLY; reword M2 and M4 before either enters
the manuscript).

---

## 3. batat2026phive

### Bibliographic fields

| Field | Card | PDF | Verdict |
|---|---|---|---|
| Title | The Phygital Intelligence Value Experience (PHIVE) Matrix: The Good, the Bad, and the Ugly of AI Marketing for Customer Experience Design | "The phygital intelligence value experience (PHIVE) matrix: the good, the bad, and the ugly of AI marketing for customer experience design" (p. 1) | PASS (title case only) |
| Author | Batat, Wided | Wided Batat, University of Lyon 2 | PASS |
| Year | 2026 | published online 02 Jun 2026 (cover sheet) | PASS |
| Venue | Journal of Strategic Marketing, online first | Journal of Strategic Marketing; no volume/issue | PASS |
| DOI | 10.1080/0965254X.2026.2682414 | identical (cover sheet; p. 1) | PASS |
| History | received 19 May, accepted 22 May 2026 | identical (p. 1) | PASS |

### Quotations

All 48 strings are verbatim at the cited online-first page. Grouped by page:

| Page | Quotations (opening words) | Verdict |
|---|---|---|
| 1 | Received 19 May 2026 / Accepted 22 May 2026 | PASS |
| 2 | "position paper"; "Phygitality, an ontological condition …"; "The PHIVE Matrix is a strategic decision-making tool that helps leaders …"; AI "may contribute to dehumanization, …" | PASS |
| 3-4 | "A third limitation is the fragmented deployment of AI … expect fluid movement across experiential realms." | PASS (break after "where") |
| 4 | "These outcomes show that AI-mediated experiences must be evaluated …"; "Mental-health apps that replace human care"; "AI increasingly acts as a relational, cultural, and emotional actor …" | PASS |
| 5 (Table 1, rendered) | Klaus row: Role "AI concierge tools shape luxury phygital journeys by enhancing digital planning but failing in physical execution"; Bad "Emotional disconnect, lack of human warmth, misalignment between AI plan and physical service"; Ugly "Service failures, unmet expectations, erosion of luxury value, trust breakdown". Doherty et al. row, Ugly: "workforce displacement" | PASS (column placement confirmed on the image) |
| 6 | "the emergence of new roles such as the Chief Experience Marketing Officer (CXMO)"; "The phygital research paradigm (Batat, 2024b, 2025)" | PASS |
| 7 | "Accordingly, the PHIVE Matrix is defined as: …"; "PI refers to a system's capacity …"; "AI optimizes tasks; PI orchestrates meaning." | PASS |
| 9 | "However, because AI activates only a limited set of phygital extensions, …"; Figure 1 (rendered) "Smooth, efficient, coherent experiences" | PASS |
| 10 | "When AI disrupts this continuity, …"; "technological extensions should support the holistic nature of both consumer and employee lived experiences …"; "For brands and organizations, understanding this configuration is essential …" | PASS |
| 11 | "In such cases, AI may reinforce stigma, …"; "The result is a fragmented experience …" | PASS |
| 12 | "good/fair"; "This quadrant aligns with the metaphor of water: …"; "structurally coherent yet emotionally shallow" | PASS |
| 13 | "This form of value creation can therefore be understood as a good or fair improvement …"; "is elevated through the seamless convergence …" | PASS |
| 14 | "AI becomes embedded within the 'phygital flow', …"; "Guests begin by sharing flavor preferences, dietary needs, …" | PASS |
| 15 | "AI reduces friction, enhances responsiveness, and expands experiential possibilities" | PASS |
| 16 | "Value-amplifying technologies operate sensitively and transparently, …"; "The PHIVE Matrix positions this state as the benchmark …"; Table 4 (rendered) Water example "AI-enabled mobility or hospitality systems that create seamless, efficient, and coherent phygital journeys" and outcome "Experience becomes useful, seamless, and moderately engaging" | PASS |
| 17 | "Its first contribution is reframing AI not as a functional tool but as an 'experiential agent' …"; "Each quadrant carries explicit managerial implications: …"; "It also reinforces the importance of AI systems that support; rather than replace; …" | PASS |
| 18 (Table 5) | "Repair & Rebuild"; "Use phyginography to generate smart insights and restore trust and emotional safety"; "Eliminate harmful features or extractive mechanisms"; "Restore phygital continuity" (Air row, "Stabilize & Reconnect"); "(3) how cultural, social, and institutional environments shape the development of phygital intelligence" | PASS |
| 19 | "AI enhances experience only when it supports meaning, coherence, and human agency …"; "For practitioners, it underscores the need for intentional, human-centric AI integration …" | PASS |
| 20 | Reference labels: 2024a PH-CX, 2024b QMR editorial, 2025 PSR, 2026a HFPV | PASS |

### Claims

| # | Claim | Card locator | Verdict |
|---|---|---|---|
| C1 | Position paper for the JSM special issue on GenAI and phygital CX | Summary | SUPPORTED (p. 2) |
| C2 | Axis 1 "counts how many of ERT's four experiential extensions an AI activates"; axis 2 measures fit with PH-CX's six value pillars (pp. 7-8) | Summary | SUPPORTED. "Counts" glosses "the extent to which AI activates and integrates the four experiential extensions" (p. 7); the quadrant text supports it ("activates only one experiential extension", pp. 9, 11). |
| C3 | Four quadrants and their positions (Fig. 1, p. 9; Table 4, p. 16) | Summary | SUPPORTED (the text calls Air the "bad" manifestation, p. 8, and Earthquake the "ugly", p. 10) |
| C4 | PI distinct from AI (p. 7; Table 2, p. 8); managerial actions (Table 5, p. 18) | Summary | SUPPORTED |
| C5 | Most direct about AI's harms: dehumanization, surveillance, loss of autonomy, exclusion | Summary | SUPPORTED (pp. 2, 4, 11; Table 1 "Digital exclusion", p. 5) |
| C6 | "Its master value is continuity. Discontinuity is the harm it diagnoses" | Summary | **PARTLY.** Continuity is central: PI is "a system's capacity to sustain experiential continuity …" (p. 7), and Table 2 gives PI's primary function as "Orchestrates continuity across physical-digital experiences" (p. 8). But discontinuity is the diagnosed harm of the Air quadrant only. The Earthquake harm arises when "systems prioritize efficiency, automation, and data extraction over the emotional, symbolic, ethical, and relational dimensions" (p. 11), and Water shows that continuity without alignment is only "good/fair" (p. 12). The card's own critical note states this correctly: "failures of continuity and of human alignment". |
| C7 | Seamlessness belongs to the good/fair quadrant and to the Fire benchmark | Summary | SUPPORTED |
| C8 | Addresses firms' leaders; nothing on duties, recourse or allocation among firms | Summary | SUPPORTED (term search: no duty, obligation, recourse, complaint, accountability; "responsible" only in "responsible AI marketing strategies", p. 10, and "responsible, human-centric AI research", p. 17) |
| C9 | Hospitality placed in the Water quadrant (Table 4, p. 16) | Key facts | SUPPORTED |
| C10 | `seamlessness-uncritiqued` survives, narrowed: seamlessness not sufficient, not questioned as a goal | Critical notes | SUPPORTED |
| C11 | `framing-argued-past` contested by "experiential agent" (p. 17) | Critical notes | SUPPORTED |
| C12 | The Water ranking judges experiential depth, not answerability | Critical notes | SUPPORTED |
| C13 | Klaus (Table 1, p. 5) "records a failure between an AI's plan and another party's physical execution" | Critical notes | **PARTLY.** Table 1 records "failing in physical execution" and "misalignment between AI plan and physical service"; it does not say the physical service belongs to another party. The card labels the paragraph as interpretation, but "another party" is not in PHIVE, and Klaus has not been read. |
| C14 | Kitchen Theory routes "dietary needs" through AI, then human chefs presented as creative interpreters (p. 14) | Critical notes | SUPPORTED |
| C15 | Prescribes trust, transparency, agency, well-being (pp. 16-19) to a firm's leaders; names no one beyond "consumers"; never mentions several firms; remedies are redesign actions | Critical notes | SUPPORTED. The addressees in the text are "leaders" (p. 2), "firms'" (p. 7), "brands and organizations" (p. 10), "companies and brands" (p. 13) and "practitioners" (pp. 17, 19). |
| C16 | Position paper accepted three days after receipt; cases are illustrations | Critical notes | SUPPORTED |
| C17 | Citation labels (p. 20; p. 6) | Critical notes | SUPPORTED |
| C18 | Hold rationale "the matrix addresses one firm's leaders"; Where it bears "an evaluative tool for one firm's AI" | Frontmatter; Where it bears | **PARTLY.** No passage restricts the matrix to one firm. The definition says "firms'" (plural, p. 7), and nothing addresses several firms either. See M5. |
| C19 | Both axes measure experience | Where it bears | SUPPORTED (pp. 7-8) |
| M1 | Places "AI-enabled mobility or hospitality systems …" in Water (16), "a good or fair improvement …" short of transformation (13) | May say | SUPPORTED |
| M2 | "PHIVE treats discontinuity as the harm: in its Air quadrant AI 'fails to sustain …' (9), and its prescribed remedy is to 'Restore phygital continuity' (18)" | May say | **PARTLY.** Both quotations are exact. "The harm" overstates the source: discontinuity is the Air quadrant's harm, and Earthquake's is techno-centric, low-alignment design (C6). "Restore phygital continuity" is one of four Air actions (Table 5, "Stabilize & Reconnect"). Suggested wording: "In PHIVE's Air quadrant AI 'fails to sustain the continuity required …' (9), and 'Restore phygital continuity' is among the actions prescribed (18)." |
| M3 | Benchmark "phygital flow" is "the seamless, continuous poly-creation of meaning …" (14) | May say | SUPPORTED (the phygital flow describes the Fire quadrant, p. 14; Fire is named the benchmark, p. 16) |
| M4 | Reframes AI "not as a functional tool but as an 'experiential agent'" (17); assigns AI no standing as a party that answers | May say | SUPPORTED (absence confirmed by term search) |
| M5 | Evaluates "how firms' AI-driven tools and strategies generate, sustain, or undermine experiential value" (7); "its unit is one firm's tools" | May say | **PARTLY.** The quotation is exact, but "one firm's" is not in the source: "firms'" is plural. Table 2 gives PI's "Unit of Analysis" as "Lived experience across blended environments" (p. 8), which a referee could cite against "unit". Suggested wording: "its object is firms' AI tools and strategies; it says nothing of how several firms' tools combine in one journey." |
| M6 | AI concierge tools "enhancing digital planning but failing in physical execution"; Ugly effects (5, Table 1, summarizing Klaus 2025) | May say | SUPPORTED |

### Omissions bearing on who owes safeguards, and on seamlessness

- **O1 A further "seamless" use, in Water.** "contemporary transportation platforms combine AI-driven
  navigation, predictive traffic management, voice assistants, and personalized mobility recommendations to
  create seamless travel experiences across physical and digital spaces." … "Mobility becomes more convenient
  and less stressful." (p. 13). This endorses seamlessness as a functional good. The card names transport
  platforms only as an illustration.
- **O2 Continuity across the ecosystem, prescribed to practitioners.** The matrix "emphasizes activating
  multiple extensions to ensure continuity across phygital environments and cautions against deploying AI in
  isolated touchpoints without considering the broader phygital ecosystem." (p. 17). It does not say who
  coordinates when the touchpoints belong to different firms.
- **O3 The one mention of multi-organization settings.** "Its relevance extends beyond consumer markets to
  B2B ecosystems, where AI-mediated phygitality increasingly shapes organizational processes and value
  creation." (p. 17). It allocates nothing.
- **O4 Klaus is about travel concierge services.** The prose reads: "Klaus (2025) demonstrates that AI
  concierge services can strengthen autonomy and competence for ultra-high-net-worth consumers yet weaken
  emotional resonance in physical encounters." (p. 4). The reference is Klaus, P. (2025), "Exploring
  AI-driven phygital experiences: The case of ultra-high-net-worth individuals' travel concierge services",
  *Journal of Strategic Marketing*, 1-19, doi 10.1080/0965254X.2025.2540270 (p. 20). This is the
  hospitality-adjacent source the card says to read before citing.
- **O5 (minor) Continuity paired with meaning-making.** "Addressing these shortcomings requires a shift
  toward a phygital, human-centric logic that foregrounds continuity and meaning-making across blended
  experiential realities." (p. 4). This bears on C6.

**Overall: PASS WITH CORRECTIONS** (0 FAIL, 0 NOT SUPPORTED, 5 PARTLY; reword M2 and M5 before either enters
the manuscript).

---

## 4. berthon2026accesship

### Bibliographic fields

| Field | Card | PDF (p. 408) | Verdict |
|---|---|---|---|
| Title | Access and Ownership in the Phygital: Toward a Phygital–Accesship Typology with Implications for Consumer Well-being | identical | PASS |
| Authors | Berthon, Lim, Pizzichini, Raquel, Rindfleisch, Soon | Pierre Berthon, Weng Marc Lim, Lucia Pizzichini, Steve Raquel, Aric Rindfleisch, Pei-Shan Soon (ORCID list, p. 420, same order) | PASS |
| Year | 2026 | 2026 | PASS |
| Venue | Journal of Macromarketing | Journal of Macromarketing | PASS |
| Vol/issue/pages | 46(3), 408-425 | "2026, Vol. 46(3) 408–425" | PASS |
| DOI | 10.1177/02761467251413156 | identical | PASS |
| Corresponding author | Pierre Berthon, Bentley University (p. 408) | identical | PASS |

### Quotations

All 65 strings are verbatim at the cited printed page. The card's ellipsis "firms should ... provide
low-friction cancellations" (p. 416) is correctly marked. Grouped by page:

| Page | Quotations (opening words) | Verdict |
|---|---|---|
| 408 | "Our research, which is conceptual in nature, …"; "phygital focuses on the nature (type) of a solution …" | PASS |
| 408-409 | "phygital denotes hybrid composition, … shorthand for relative dominance" | PASS (break after "delivers") |
| 409 | "How do the type of solution … affect consumer well-being?"; "A substantial body of scholarship suggests …"; "the phygital literature has remained largely silent" | PASS |
| 410 | "Ownership typically implies a long-term, …"; "Ownership also confers a more complete bundle of property rights, …"; "Within macromarketing, consumer well-being is conceptualized as …" (running head mid-sentence); "work on access-based consumption in the sharing economy …" | PASS |
| 411 | Batat (2024b) "integrates a combination of physical, human, digital and media content elements, …" ("(p. 10)"); "In essence, phygital solutions fuse …"; "We define accesship as …"; "the access–ownership structure through which …"; "Hence, accesship is orthogonal to phygital: …"; "Under access arrangements, providers typically retain responsibility for upkeep and liability …" | PASS |
| 412 | Table 1 dimensions ("Time-bound rights and journey structure", "Responsibility and maintenance", "Transferability and legal rights", "Cost structure"); Table 1 cells "Maintenance and liability largely handled by provider; minimal consumer burden" and "Owner responsible for care, maintenance, and associated costs"; "the two rows of this typology represent …"; "The four quadrants should be viewed as anchor configurations …" | PASS |
| 413 | Table 2 descriptions of Streams, Tokens, Lends, Keeps; "streaming partnerships"; "through platforms such as Bandcamp" | PASS |
| 414 | "These mechanisms yield competing predictions, …"; "consumer satisfaction (as a proxy of consumer well-being)"; "upkeep is minimal or provider-managed"; P1 | PASS |
| 415 | P2; P3 fragment "should exhibit higher levels of acquisition satisfaction, …"; P4; P5; "For example, it requires considerably less effort, money, and time to rent a historic villa in Tuscany via Airbnb …"; "since accessed solutions are typically owned by another entity, …" | PASS |
| 416 | P6 (paraphrased, correctly); "These two dimensions represent strategic levers that firms can pull …"; "firms should invest in personalization, curated journeys, …"; "thereby shifting competitive advantage toward onboarding ease, continuity guarantees, and low-friction exit"; "Access-dominant models (i.e., Streams, Lends) can expand a firm's customer base …"; "Hence, firms should disclose the total cost of use, … (Calo, 2013; Sheil et al., 2024)."; "equitable tiers"; "exploitative practices" | PASS |
| 417 | "Moreover, consumers may face limitations on functionality, interoperability, or even continued access …"; "Accordingly, policy revisions are needed … even when legal ownership is absent."; "access-heavy formats (i.e., Streams, Lends) can broaden participation, …"; "regulators can require total cost of use disclosures, friction-reduced cancellation flows, …"; "policy could require that Lends solutions, such as ridesharing services, …"; "that promote interoperability, portability, and license transparency …"; "are largely based on logical deduction …"; "purely conceptual"; "societal welfare" | PASS |
| 419 | "At present, this divergence between psychological versus legal ownership represents a grey zone …"; "societal welfare" | PASS |
| 420 | "This research was conducted as part of the American Phygital Association Summit 2025, …"; "Associate Editor" Wided Batat; "while Streams provide affordability, …"; "Keeps offer tactile gratification …"; "firms must carefully design solutions that balance control and flexibility; …"; note 1 "intentionally designed customer journeys …" | PASS |
| Other | JOURNAL_SPEC.md line 73: "Strict anonymity is accorded to both contributors and referees" (card quotes "strict anonymity") | PASS |

### Claims

| # | Claim | Card locator | Verdict |
|---|---|---|---|
| C1 | Conceptual macromarketing article; phygital = type, accesship = mode; 2 × 2 PAT, four cells | Summary | SUPPORTED |
| C2 | Each cell read as a sequenced solution | Summary | SUPPORTED (pp. 412-413; note 1, p. 420) |
| C3 | "Three psychological mechanisms … yield six propositions about which cell better supports consumer well-being, with satisfaction as the proxy" | Summary | **PARTLY.** The six propositions are stated per dimension, not per cell: P1-P3 for solution type and P4-P6 for acquisition mode (Table 3, p. 414). The authors analyse "the extreme ends of both dimensions" (p. 414). Satisfaction is the explicit proxy only in Panel B (P3, P6); P1, P2, P4 and P5 speak of "consumer well-being". Cell-level statements appear only in the implications (pp. 416-417) and the conclusion (p. 420). |
| C4 | Implications address firms, consumers and policymakers in turn | Summary | SUPPORTED |
| C5 | Firms: disclose total cost, easy cancellation; regulators: mandate licence transparency, continuity and termination disclosures, remedies | Summary | SUPPORTED (source: "policy revisions are needed … by mandating …", p. 417) |
| C6 | No hospitality setting, no AI; one accommodation example (Airbnb villa, p. 415) | Summary | SUPPORTED |
| C7 | Provenance APA Summit 2025; Associate Editor Wided Batat (p. 420) | Key facts | SUPPORTED |
| C8 | Absent terms: owe, duty, obligation, safeguard, trust, fair, recourse, complaint, correction, redress, seamless, frictionless, hospitality, hotel, host; "Guest" only at p. 422 (two references) and p. 424 (biography); "AI" only in two reference titles (pp. 421, 422) and one biography (p. 425) | Key facts | SUPPORTED. One precision: the p. 425 biography says "artificial intelligence", not "AI". |
| C9 | Medina-Hernandez et al.'s title concerns guests on peer-to-peer accommodation platforms (p. 422) | Key facts | SUPPORTED ("Attributes influencing guests' experiences: A comparison of nonprofit and for-profit peer-to-peer accommodation platforms", *Information Technology and Tourism* 26(2)) |
| C10 | Safeguards without a bearer among several firms; examples involve more than one firm (p. 413); the only allocation is two-party and descriptive (p. 411); remedies without bearer or channel (p. 417) | Critical notes | SUPPORTED (see omission O1) |
| C11 | No duty language; safeguards framed as levers, competitive advantage, measures | Critical notes | SUPPORTED |
| C12 | "Friction here favours the consumer … friction is what a firm puts in front of a leaving customer … Here the article asks for smoothness at the exit" | Critical notes | **PARTLY.** The exit point stands (pp. 416-417), but the article also prizes low friction at entry. Digital- and access-dominant solutions "typically lower initiation frictions (e.g., effort, time, and upfront financial commitment) and allow consumers to begin use quickly" (Table 3 notes, p. 414), and firms gain advantage through "onboarding ease" (p. 416). The article values smoothness at both entry and exit. "Seamless" and "frictionless" never appear: SUPPORTED. |
| C13 | "Control" is always the consumer's | Critical notes | SUPPORTED. The one ambiguous use, "balance control and flexibility" (p. 420), reads in context as the consumer's control. |
| C14 | Satisfaction proxies well-being; "purely conceptual" (p. 417) | Critical notes | SUPPORTED |
| C15 | Berthon's "Batat (2024b) … (p. 10)" is PH-CX printed p. 1229, its tenth page; Berthon's 2024a is the JRCS metaverse article (p. 421) | Critical notes | SUPPORTED (I found the words on PH-CX printed p. 1229, PDF p. 11 of 25, after a cover sheet) |
| C16 | Anonymity facts: Berthon co-authors the article; APA Summit; Batat as Associate Editor | Critical notes | SUPPORTED (pp. 408, 420) |
| C17 | Gap statement partly supported: firms and regulators named, no allocation among several firms, safeguards not framed as owed, no trust or fairness by name | Where it bears | SUPPORTED |
| C18 | K3: a hotel stay would classify as Lends; the article grounds upkeep and liability in acquisition mode and never discusses a stay | Where it bears | SUPPORTED (consistent with the p. 412 classification rule; the classification is the reader's own) |
| C19 | K7, K8, `exit-voice-standing`, `framing-argued-past`, `wellbeing-valence` readings (pp. 416-417, 419) | Where it bears | SUPPORTED |
| M1 | Phygital as type (physical- to digital-dominant), accesship as mode (access- to ownership-dominant) (408-409) | May say | SUPPORTED |
| M2 | Accesship definition (411) | May say | SUPPORTED |
| M3 | Four kinds: Streams, Tokens, Lends, Keeps (412-413) | May say | SUPPORTED |
| M4 | "the phygital literature has remained largely silent" about harms to well-being (409) | May say | SUPPORTED |
| M5 | Under access "providers typically retain responsibility for upkeep and liability" (411) | May say | SUPPORTED |
| M6 | Consumers may lose "continued access when a service is discontinued or a license is revoked"; policy to mandate "continuity and termination disclosures, … remedies when access is withdrawn" (417) | May say | SUPPORTED ("may lose" paraphrases "may face limitations on … even continued access") |
| M7 | Firms to "disclose the total cost of use, provide low-friction cancellations, and design equitable tiers" (416) | May say | SUPPORTED |
| M8 | "Their recommendations are addressed to firms in general and to policymakers, and they do not say which of several firms supplying one solution should provide a remedy (416-417, 420)" | May say | **PARTLY.** The second clause is supported. The first omits consumers, to whom the article also addresses recommendations: "consumers who seek the identity benefits of ownership but face resource constraints should favor solutions in the Lends category" (p. 417); "consumers must navigate new solutions …" (p. 420). The card's own "may not say" list names all three addressees. Suggested wording: "addressed to firms, consumers and policymakers …". |
| N1-N6 | "What the paper may not say" (six items) | May not say | All SUPPORTED |

### Omissions bearing on who owes safeguards, and on seamlessness

- **O1 Ride-sharing, the article's one multi-sided service.** "A good example of these issues is the many
  legal and regulatory challenges surrounding the operations of ride-sharing platforms (Ranchordás, 2015;
  e.g., Grab, Ola, and Uber)." (p. 417). Later on the same page: "policy could require that Lends solutions,
  such as ridesharing services, adopt minimum standards for maintenance cycles, utilization reporting, and
  end-of-life recirculation in order to better align firm incentives with societal welfare" (p. 417). The
  requirement falls on the "solution". The article does not divide it between platform and drivers. The card
  quotes the second sentence but cites only the p. 413 examples as multi-firm cases (READ_berthon2026.md
  cites pp. 413 and 417). This strengthens the K8 absence.
- **O2 Low friction at entry** (Table 3 notes, p. 414, quoted under C12). This bears on seamlessness: the
  article treats lower "initiation frictions" as a source of acquisition satisfaction.
- **O3 Who protects: the law lags.** "large portions of our current legal and regulatory system were developed
  under the assumption that solutions were mainly tangible in nature and acquired via permanent ownership"
  and "digital content licensing … often lacks the same consumer protections afforded to physical goods, such
  as rights of resale or transfer" (p. 417). Protection is framed as a regulatory gap, not as a firm's duty.
- **O4 (minor) Add-ons from other quadrants.** "Sequenced elements that appear later in the journey may borrow
  from adjacent quadrants" (p. 412); "Sequenced add-ons may incorporate elements from other quadrants without
  changing the anchor classification." (Table 2 note, p. 413). The add-ons in the examples come from other
  parties ("streaming partnerships"). The article never asks who answers for them.

**Overall: PASS WITH CORRECTIONS** (0 FAIL, 0 NOT SUPPORTED, 3 PARTLY; reword M8 before it enters the
manuscript).

---

## Notes for the authors

- No card was edited. The four "What the paper may say" sentences to reword before use are HFPV M2 and M4,
  PHIVE M2 and M5, and Berthon M8. Suggested wordings are given in the rows; they were drafted by the
  verifier, not by the authors.
- Cross-card: three cards rely on the claim that the phygital texts never allocate a safeguard among
  several firms. That claim survives a full read of all four sources. The nearest passages are HFPV's
  "shared authorship" among stakeholders (p. 275), PHIVE's B2B mention (p. 17) and Berthon's ride-sharing
  passage (p. 417). None of them allocates anything.
