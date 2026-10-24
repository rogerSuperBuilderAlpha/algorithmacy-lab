# X: The counter-case against the foundation thesis

*Corrected on 2026-10-12 against `../audit/AUDIT_03.md`: 26 factual fixes; verbatim quotation of the Nadella post cut to 26 words.*

*Facet X of the DXD foundation paper (PHD1750-3 / HF700-1). Agent-drafted on 2026-10-12 (Sonnet 5.5, local session). The author has not reviewed it, and none of the text is the author's. Wording marked **[Agent wording]** is a proposal for the author to accept, change or reject; it is not his text.*

## What this facet covers

I am opposing counsel. `CLAIM.md` states four parts: a precedent (scribes moved work from reader to page), a consequence (H-cost or H-cause), a transfer (algorithmic coordination is "unspaced script"; DXD looks for the move that takes the work off the person) and a foil (Nadella's post as "the exact opposite"). I build the strongest case against each part, in ten objections, using sources I opened where I could and saying so where I could not. I do not survey the history of spacing (facets A, B), literacy history (C), reading science (D), the human-factors frame (E), parallel cases (F), Nadella's lineage (G) or candidate moves (H). Where an objection needs one of their findings I cite the finding and its holder.

**The question the synthesis answers.** After all ten objections are heard, which version of the thesis is still standing, and what does the author have to give up or reword to keep it?

## Legend for read status

- **Read in full**: I opened the whole text.
- **Read in part**: I opened the named pages or sections only.
- **Abstract only**: I read a database abstract and claim nothing beyond it.
- **Relayed**: I did not open the source; I am quoting the lab's own card or an earlier facet, and I say which. A relayed quotation carries the earlier reader's check, not mine.
- **Not accessible**: the record exists; I could not open the content. The entry says where a human with library access would look.
- **Argument only**: no source supports the step; I am arguing, and I say so.

---

## (a) Search log

All rows ran on 2026-10-12.

| # | Source | Exact query or request | Hits | Notes |
|---|---|---|---|---|
| 1 | Crossref `query.bibliographic` | 23 title strings (Jensen and Meckling; Eisenhardt; von Hippel; Street; Star and Ruhleder; David; Liebowitz and Margolis; Reason; Seaver; Dekker and Woods; Bjork; Rosenblat and Stark; Mathur; Gray; Buçinca; Saltzer and Schroeder; Parasuraman et al.; Sarter et al.; Cox et al.; Scribner and Cole; Graff; Hirschman; LaPorte and Consolini) | 3 of 23 | The first batch hit HTTP 429 after three requests. Another agent's script overwrote my helper in the shared scratchpad; I moved to a private subfolder and reran in smaller batches (rows 2 to 4). |
| 2 | Crossref, polite pool | 12 titles (agency theory; lead users; Star and Ruhleder; David; Liebowitz and Margolis; Seaver; Bjork; Rosenblat and Stark; Parasuraman et al.; Sarter et al.; Reason; Jensen and Meckling) | 9 resolved | Not found as titled: David (1985) has no Crossref record; Sarter, Woods and Billings is a handbook chapter, not resolved; Bjork and Bjork's chapter surfaced only as a PsycEXTRA record, dropped. Rosenblat and Stark resolves only to the SSRN working paper; the journal article is verified from its PDF. |
| 3 | Crossref | 11 titles (Scribner and Cole 1978; Graff; Dekker and Woods; Star and Ruhleder 1996; David; Lee and See; Hurwicz and Myerson; Bainbridge; Zuboff; Edgerton; Holmström) | 8 resolved | Edgerton, *The Shock of the Old*: Crossref returns only two book reviews; no book record. Zuboff: only a 2023 chapter and a 2019 interview. Dropped both. |
| 4 | Crossref direct DOI | 10.2307/1805621 (David); 10.1287/isre.7.1.111; 10.1007/s101110200022; Perrow; Roberts; Saltzer and Schroeder; von Hippel; Gray; Vasconcelos; Noessel | 9 of 10 | David's JSTOR DOI returned nothing. Star and Ruhleder carries a Crossref abstract; Dekker and Woods carries none. |
| 5 | Unpaywall | 16 DOIs | 8 OA | Open: Street 2003, Reason 2000, Cox 2016, Buçinca 2021, Gray 2018, Mathur 2019, Liebowitz and Margolis (SSRN), de Winter and Dodou. Closed: Seaver, Parasuraman et al., von Hippel 1986, Eisenhardt, Jensen and Meckling (journal), Scribner and Cole 1978, Star and Ruhleder, Dekker and Woods. |
| 6 | `curl` + `pdftotext` | Street 2003 (ufpr.br copy); Cox 2016 (White Rose); Buçinca (arXiv); Mathur (arXiv); Rosenblat and Stark (ijoc.org); von Hippel ch. 1, 2 (web.mit.edu); Jensen and Meckling (Illinois course copy); Saltzer and Schroeder (web.mit.edu HTML); Perseus Phaedrus 275a | 9 opened | PDFs under `dxd_foundation_local/pdfs/X/`. |
| 7 | `curl` | Reason 2000 (PMC, Europe PMC render, Europe PMC REST); Street 2003 (journal URL); Gray 2018 (ACM); Liebowitz and Margolis and Jensen and Meckling (SSRN); de Winter and Dodou (Springer, TU Delft resolver) | 0 | All returned HTML walls or reCAPTCHA pages. Not retried. |
| 8 | `curl` / `WebFetch` | Leveson, *Engineering a Safer World*: OAPEN bitstream (three paths), DOAB, MIT Press Direct chapter page, `sunnyday.mit.edu/safer-world.pdf` | 0 | OAPEN and MIT Press returned a bot page or HTTP 403; `sunnyday.mit.edu` did not respond. I use the lab's card, which holds page-verified quotations from the OAPEN text (entry `leveson2011engineering`). |
| 9 | Scholar Gateway `semanticSearch` | Did word separation in medieval manuscripts cause the spread of silent reading and literacy, or is that technological determinism? | 0 | `ACCESS_DENIED: Access denied`. Not retried. |
| 10 | Consensus `search` | `frictionless design hides the mediator; algorithmic recommender systems captivation engagement` | 20 | Seaver 2018 (abstract), Vasconcelos et al. and Liu et al. 2025 on hypertextual friction (not used). |
| 11 | Consensus `search` | `human-AI interaction friction cognitive forcing reduces overreliance on AI recommendations` | 20 | Buçinca et al. 2021 (opened by arXiv), Vasconcelos et al. 2023 (abstract), Noessel 2026 (abstract). Several 2025 and 2026 items have zero or few citations; I did not use them. |
| 12 | WebSearch | `Leveson "Engineering a Safer World" MIT Press open access pdf`; `Dekker Woods "MABA-MABA or abracadabra"…`; `Paul David "Clio and the Economics of QWERTY"…`; `Jensen Meckling 1976 … "residual loss" "bonding costs"`; two on Saenger and Wingo and the interpunct | — | Located the Illinois copy of Jensen and Meckling; confirmed Dekker and Woods's and David's bibliographic details through secondary pages only. No open copy of the Roman-abandonment passage. |
| 13 | WebFetch | `en.wikipedia.org/wiki/Scriptio_continua`; CAMWS 2015 abstract on interpuncts; PMC page for Reason; MIT Direct | partial | Wikipedia confirms only that "later on the Romans came to follow the Greek practice of scriptio continua", citing Moore 2001 and Wingo 1972 without pages. I do not cite Wikipedia. The CAMWS PDF returned compressed binary; Reason's PMC page, a reCAPTCHA. |
| 14 | OpenAlex | `search=` on interpunct decline, Saenger reviews, Irish scribes | 0 | "Rate limit exceeded. Insufficient budget" (the shared daily budget was spent by other agents). Google Books API: "Quota exceeded". Neither retried. |
| 15 | Repo reads | `RESEARCH_PLAN.md`, `CLAIM.md`, `SOURCE.md`, `literature/REUSE.md`; Part 1 (all 482 lines); Nadella capture; `part4_phygital/…/X_counter_case.md` (lines 1 to 130); Part 2 facet E (lines 54 to 63, 309 to 327); lab cards `leveson2011`, `bainbridge1983`, `parasuraman2000`, `scribner1981`, `graff1991`, `finnegan1988`, `zuboff2019`; `org_frontier/essays/scifi_interfaces_and_algorithmacy.md`; `dial_response_algorithmacy/draft.md:263,337`; `algorithmacy_ot/manuscript/PAPER.md:19-21` | — | Locators for objection 9 come from these. |

Housekeeping: a failed `cd` made two scratch downloads land in the worktree root early in the run; I deleted both and confirmed the root listing is unchanged. I ran no git commands.

---

## (b) Entries

Bib keys are in `X_counter_case.bib`. Entries are grouped by the objection they serve (numbers match section (c)).

### Internal documents (the target of the objections)

`hunt2026decision` | Hunt, R. (2026-09-30). *Decision Experience Design* (Part 1). Substack. Local file `submissions/decision_experience_design/published/2026-09-30_decision-experience-design.md`.
- *Verified:* read the whole file (482 lines). Line numbers below are that file's.
- *Read status:* read in full.
- *What matters for the objections (exact words):*
  - Line 118: "Written text is dyadic and asynchronous, but fundamentally passive." and "Traditional media hold still; an algorithmic intermediary does not."
  - Line 22: "The cognitive demands of this environment cannot be solved through the traditional UX toolkit of legibility, visual layout, and cognitive load reduction." Line 92: "Deciding through an algorithmic system imposes cognitive demands that research on reading, visual layout, and cognitive load cannot resolve."
  - Line 60: algorithmic environments "govern untrained, everyday users whose objectives conflict with the platform's bottom line." Line 64: "An algorithmic intermediary deployed by an on-demand labor platform or ad-driven network does not share its users' goals."
  - Line 66: Kahneman and Klein's two conditions for expertise (a valid, predictable environment and fast feedback), which "An adaptive algorithmic intermediary systematically disrupts." Line 156: "psychometric repositories contain no validated scales indexing algorithmacy".
  - Line 106: Buçinca et al.'s forcing functions "curbed uncritical acceptance far more effectively than explanatory text, even though users rated these demanding interfaces less enjoyable." (Part 1's wording; the study's result is narrower, see the Buçinca entry.)
  - Line 120: Ong and Goody and Watt "posited a 'Great Divide,' arguing that the invention of writing fundamentally rewired the neurological architecture of the human mind. Brian Street (1984) dismantled this autonomous model."
  - Lines 142, 144, 146, 148: DXD expertise is "counter-delegation, structural refusal, bounded operational envelopes, and backward-compatible behavioral updates"; envelopes "establish explicit bounds on algorithmic behavior rather than explaining black-box logic".
  - Line 22 also calls algorithmacy "a measurable, domain-specific competence that predicts decision quality".
- *Bearing:* the source of the sharpest objections (1, 3, 7, 8, 9), because the thesis contradicts it in several places. Locators for the contradictions are in 9a to 9f.

`nadella2026models` | Nadella, S. (2026-10-10). *Models as Insider Risks in the Super Intelligence Era*. X.
- *Verified:* read the local capture (paragraphs P1 to P21).
- *Read status:* read in full.
- *Fragments I rely on (paraphrase, with paragraph numbers):* P3, a provider's assurances do not discharge the organisation's responsibility. P5, the supply of intelligence is to be split from who holds "the authority over it". P6, non-deterministic models are to be wrapped in deterministic system design, plus human controls and procedures. P8, the enterprise already knows how to manage powerful insiders. P9, chain-of-thought transparency on its own is "not sufficient or dependable". P11, no program should be able to evade or alter the machinery that checks its permissions. P17, "Orgs" decide for themselves what a model may access or do. P19, "an authorized person" can halt a model mid-task. P20, disclosure "to those affected". P21, the best system is the one that lets the deployer trust the model least.
- *Bearing:* the foil. Its centre is structural (P6, P11, P17, P19), not interpretive. See objections 6 and 7.

`DIAL/author texts` (no bib keys; local files, quoted with locators in 9a to 9f): `SOURCE.md` (the author's instruction and the engagement-layer sentence), `RESEARCH_PLAN.md` §3 (Nadella count 3, rulings), `dial_response_algorithmacy/sources/phd1750_topic_and_rationale.md:52-54`, `dial_response_algorithmacy/draft.md:263, 337`, `algorithmacy_ot/manuscript/PAPER.md:19-21`, `org_frontier/essays/scifi_interfaces_and_algorithmacy.md:11`, `decision_experience_design/README.md:38-52`, `decision_experience_design/part2_ethics/README.md:8`.

### Objection 1. The analogy fails at the object

`jensen1976theory` | Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. *Journal of Financial Economics*, 3(4), 305-360. doi:10.1016/0304-405X(76)90026-X
- *Verified:* Crossref record; the Illinois course copy carries the journal running head.
- *Read status:* read in part (section 1.4, p. 308); not the rest.
- *What it argues:* a principal who delegates decisions to an agent cannot make the agent's choices match his own interest for free. "However, it is generally impossible for the principal or the agent at zero cost to ensure that the agent will make optimal decisions from the principal's viewpoint." (p. 308). The cost has three parts: monitoring by the principal, bonding by the agent, and a "residual loss" (p. 308). Footnote 9 on the same page counts "operating rules" and "compensation policies" as monitoring.
- *Bearing on objection 1:* the classic reason an interface change does not dissolve a conflict of interest. Redesign lowers the cost of monitoring or bonding; the residual loss remains whenever interests diverge. Part 1 itself says the platform's intermediary "does not share its users' goals" (line 64). **Supports** the objection; it does not refute the claim that design can shrink the loss.

`rosenblat2016algorithmic` | Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study of Uber's drivers. *International Journal of Communication*, 10, 3758-3784.
- *Verified:* open-access PDF, running head "International Journal of Communication 10(2016), 3758–3784". No journal DOI resolved; Crossref has the SSRN working paper only.
- *Read status:* read in part (abstract; introduction to p. 3763; surge-pricing section).
- *Quotations:* "the information and power asymmetries produced by the Uber application are fundamental to its ability to structure control over its workers" (abstract, p. 3758). "the labor that Uber drivers do is shaped by the company's deployment of a variety of design decisions and information asymmetries via the application to effect a 'soft control' over workers' routines" (p. 3761).
- *Bearing:* an empirical case (nine-month study) in which the interface is the instrument of the interested party's control. This is the strongest single source for "redesign the interface" handing the remedy to the party with the conflicting interest. **Supports** objection 1 and 2. It does not say interfaces cannot be redesigned by someone else.

`mathur2019dark` | Mathur, A., et al. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. *Proc. ACM HCI* 3(CSCW), Article 81. doi:10.1145/3359183
- *Read status:* read in full (card: library/mathur2019dark.md; arXiv v2).
- *Quotation:* "Dark patterns are user interface design choices that benefit an online service by coercing, steering, or deceiving users into making unintended and potentially harmful decisions." (abstract). The study finds "1,818 dark pattern instances" on about 11,000 sites and "22 third-party entities that offer dark patterns as a turnkey solution."
- *Bearing:* in the measured population the site's own page, or a vendor hired by the operator, is the instrument of the operator's interest, and the shopper is the aggrieved party. That is a two-party setting (operator and shopper, with a third-party vendor on the supply side), not a triad with a mediator serving both; the paper measures the operator's side only. The 11.1% prevalence (1,254 sites) is a lower bound and a minority of sites, and the cognitive-bias links are unvalidated ("may be more nuanced or complex", section 6.4). **Supports** objection 1. Gray et al. (2018; `gray2018dark`, read in full: card library/gray2018dark.md) is Part 1's own source for the same point (line 40); Gray does not measure how often designers are the instrument and says designers "could easily become complicit" (abstract; pp. 9-10), which is softer than "instrument".

The scribes' shared interest (no entry): the claim that scribes "shared the reader's interest" is **argument only**. Saenger's snippets below say the ancient elite did not want broad reading; nobody in my sources says the Insular scribes' interest and their readers' coincided, only that the readers were learners of Latin (Parkes p. 1, relayed).

### Objection 2. Who makes the move

`vonhippel2005democratizing` | von Hippel, E. (2005). *Democratizing Innovation*. MIT Press. doi:10.7551/mitpress/2333.001.0001
- *Verified:* Crossref; author's open copy at web.mit.edu/evhippel.
- *Read status:* read in part (chapter 1 opening and lead-user summary; chapter 2 by search).
- *Quotation:* "Users that innovate can develop exactly what they want, rather than relying on manufacturers to act as their (often very imperfect) agents." (ch. 1, p. 1 of the book).
- *Bearing:* **cuts both ways.** It is the best published support for the Insular case as user innovation (learners of Latin altering their own copies). It is also the best published statement of what the platform case lacks: the ability to modify the artefact that mediates you. von Hippel's thesis is about users who hold the means to innovate; the author's own draft says write access to the shared mediator is "the scarce capital" and is "licensed in narrow form to the many" (`dial_response_algorithmacy/draft.md`, section 5.1). The precedent therefore predicts that the move will come from users only where users hold write access, which platform users do not.

`saenger1997space`, `parkes1992pause` (relayed from Part 2 facet E; snippet depth, context unchecked)
- Saenger p. 11: "The notion that the greater portion of the population should be autonomous and self-motivated readers was entirely foreign to the elitist literate mentality of the ancient world." Abstract (per facet E): "the ancient world had no desire to make reading easier and swifter."
- Parkes p. 1: where Latin was "a foreign language, there was a need for conventions which made it easier to read."
- *Bearing:* the reader and the scribe were often the same learner or the same community. I found no source on who controlled scribal practice in the Insular scriptoria; that gap is real (see section d).

### Objection 3. Technological determinism

`street2003whats` | Street, B. V. (2003). What's "new" in New Literacy Studies? Critical approaches to literacy in theory and practice. *Current Issues in Comparative Education*, 5(2), 77-91. doi:10.52214/cice.v5i2.11369
- *Verified:* Crossref; open-access PDF with running heads.
- *Read status:* read in full (card: library/street2003whats.md).
- *Quotations (p. 77):* "The standard view in many fields, from schooling to development programs, works from the assumption that literacy in itself--autonomously--will have effects on other social and cognitive practices." "I refer to this as an 'autonomous' model of literacy." The alternative "posits instead that literacy is a social practice, not simply a technical and neutral skill; that it is always embedded in socially constructed epistemological principles."
- *Bearing:* a literacy-studies researcher's answer (the article gives his post and names his method as ethnographic, not his discipline) to a paper that credits a page convention with ignition. The article never mentions scriptio continua, word separation or any page convention, and never mentions Ong or Goody; the step from "literacy as such" to "a layout convention" is the project's. Street does not say technology is irrelevant: he grants that outside "consolidating technologies" can unsettle local meanings, and holds only that they are ideological, not autonomous (p. 79). "Spacing ignited literacy" has the form Street calls autonomous: a feature of the technology produces social and cognitive effects "regardless of the social and economic conditions". **Supports** objection 3. It also **sits in tension with** Part 1's line 118 ("Written text ... fundamentally passive"), since Street treats literacy as practice, never neutral; Part 1's "passive" means the medium does not respond, while Street's point concerns the effects of literacy.

`scribner1978literacy`, `graff1979literacy`, `finnegan1988literacy`: records verified (Scribner and Cole only in Crossref); **not accessible**. The lab's cards give their reported findings (effects track schooling and practice, not literacy as such; mobility did not follow literacy; oral and literate are a continuum). I treat them as leads and do not quote them.

`saenger1997space` (relayed): the book's abstract says word separation "originated in manuscripts copied by Irish scribes in the seventh and eighth centuries but spread to the European continent only in the late tenth century." A 300-year lag between invention and continental uptake (on Saenger's date; Parkes dates Carolingian adoption to the 8th-9th century, per facet E:316) is evidence against ignition on Saenger's own account. Part 2 facet E's safe wording: "visual aids lowered the cost and widened the group for whom fluent private reading was practical" (E1, line 327 of that file). **Supports** the H-cost reading and **refutes** H-cause as the author stated it.

### Objection 4. Survivorship and selection

`saenger1997space` (relayed): the Romans "gave up separation by interpuncts and adopted the Greek convention of scriptura continua" (p. 12); Saenger dates the end of interpunct separation "prior to the end of the second century A.D." (p. 29). Interpuncts "were ineffective aids to the physiological process of reading when compared with the interword spaces" (p. 28).
- *Bearing:* **Supports** the objection that separation was not an obvious improvement to the people who had it. It **complicates** it too: Saenger's own reason is social (the elite did not want fast reading), and an interpunct is not a space. The step "many layout conventions came and went" has no source in my set; it is **argument only** until someone supplies a catalogue of abandoned conventions (Parkes is the likely holder; I did not open him).

### Objection 5. The single-move framing

`star1996steps` | Star, S. L., & Ruhleder, K. (1996). Steps toward an ecology of infrastructure. *Information Systems Research*, 7(1), 111-134. doi:10.1287/isre.7.1.111
- *Read status:* abstract only.
- *Quotation:* "Despite high user satisfaction with the system and interface, and extensive user needs assessment, feedback, and analysis, many users experienced difficulties in signing on and use."
- *Bearing:* a case where interface quality did not decide uptake; the authors analyse "infrastructural change" as a multi-level learning problem. At abstract strength this **supports** objection 5; I cannot say what the body argues about slowness.

`david1985clio` (not accessible; secondary citations give 75(2), 332-337) and `liebowitz1990fable` (record verified; not obtained). David is the standard source for path dependence in conventions; Liebowitz and Margolis is the standard challenge to his QWERTY example. I did not read either, so the objection on path dependence is **argument only** here, with one caution: the case it leans on (QWERTY) is itself contested. Edgerton, *The Shock of the Old* (2006): I could not verify a book record (row 3), so I drop it; Bowker and Star (1999) I did not search.

### Objection 6 and 7. Nadella is right; the two are complementary

`saltzer1975protection` | Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proc. IEEE*, 63(9), 1278-1308. doi:10.1109/PROC.1975.9939
- *Read status:* read in part ("Design Principles"); the copy has no journal page numbers. Facet G holds the full treatment.
- *Quotations:* "Least privilege: Every program and every user of the system should operate using the least set of privileges necessary to complete the job." "Complete mediation: Every access to every object must be checked for authority." **"Psychological acceptability: It is essential that the human interface be designed for ease of use, so that users routinely and automatically apply the protection mechanisms correctly."**
- *Bearing:* P11 states a 1970s information-security principle (tamper-resistant enforcement) to which S&S's complete-mediation principle belongs. The same list that grounds containment contains an interface-design principle, so security engineering itself holds that containment depends on a usable human interface. **Supports objection 7** (complementarity) and **weakens objection 6's category error**.

`leveson2011engineering` | Leveson, N. G. (2011). *Engineering a Safer World*. MIT Press. doi:10.7551/mitpress/8179.001.0001
- *Read status:* **relayed** from the lab card (`leveson2011.md`); its adversarial pass checked each quotation against the OAPEN text. I could not reopen it.
- *Quotations (via card):* "Safety is a system property, not a component property, and must be controlled at the system level, not the component level" (p. 14). "The most basic concept in STAMP is not an event, but a constraint. Events leading to losses occur only because safety constraints were not successfully enforced" (p. 76). "Passive controls are those that maintain safety by their presence" and active controls "greatly increase" failure modes (pp. 76-77).
- *Bearing:* Leveson's passive controls (interlocks, fail-safe states) correspond to Nadella's deterministic external limits and to Part 1's "bounded operational envelopes". **Supports 6** (the tested practice is structural, not interpretive). The card records the limit: Leveson's controllers pursue the organisation's mission and she models no divergent-objective platform ("no notion of an objective that diverges from the operators'").

`bainbridge1983ironies` (relayed from the lab card, marked full text with page-verified quotations): "the more advanced a control system is, so the more crucial may be the contribution of the human operator" (p. 775); the remedy is for the computer to use "methods and criteria, and at a rate, which the operator can follow, even when this may not be the most efficient method technically" (p. 777). **Supports 7**: Bainbridge's answer constrains the automated system, which is Nadella's move and Part 1's line 68, and it asks for deliberate inefficiency, which cuts against "lower the load" (objection 8).

`parasuraman2000model` (relayed): automation applies at a level to each of four functions; for decision and action automation "high levels should be implemented only for low-risk situations" (p. 293). **Supports 7**: the human-factors literature already separates what the system may do (a level of automation) from what the person must do (the stage and function allocated to them).

`reason2000human`, `perrow1999normal`, `roberts1990some`: records verified. Reason **not accessible** (reCAPTCHA); Perrow not obtained; Roberts abstract only ("organizational processes necessary to operate safely technologically complex organizations", nuclear carriers as case). They stay leads. The claims that defence in depth and high-reliability practice endorse external controls are **argument only** in this facet beyond Leveson and Saltzer and Schroeder.

### Objection 8. Lowering the skill needed has costs

`bucinca2021trust` | Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think. *Proc. ACM HCI* 5(CSCW1), 188. doi:10.1145/3449287
- *Read status:* read in full (card: library/bucinca2021trust.md; arXiv v1).
- *Quotation (abstract):* "cognitive forcing significantly reduced overreliance compared to the simple explainable AI approaches. However, there was a trade-off: people assigned the least favorable subjective ratings to the designs that reduced the overreliance the most." Benefit rose with Need for Cognition.
- *Bearing:* the study the author's own Part 1 cites (line 106). The full text gives a narrower result than the abstract suggests: forcing functions beat simple explanations only on the questions where the AI was wrong; overall performance did not rise, the two kinds of design did not differ from each other, and on the wrong-AI questions no AI condition reached the no-AI level (H1b, that forcing functions improve human+AI team performance, was not supported, p. 188:16). "Worked best" holds among the AI conditions on wrong-AI questions only. **Complicates** "change the interface until the load fell" as a general rule; **supports** objection 8. One experiment (N=199) on AI-assisted decisions, with a user as sole beneficiary; it does not test a triad.

`cox2016design` | Cox, A. L., et al. (2016). Design frictions for mindful interactions: The case for microboundaries. CHI EA '16, 1389-1397. doi:10.1145/2851581.2892410
- *Read status:* read in full (extended abstract, about 4,100 words; card: library/cox2016design.md).
- *Quotations (p. 1390, the Introduction, in the proceedings pagination, which the accepted text does not show; the abstract is on p. 1389):* "The standard argument is that they [frictions] should be removed from technology in order to reduce the risk of user disengagement." "The problem with this design approach is that it can also result in mindless forms of interaction that can have negative consequences."
- *Bearing:* names the design orthodoxy the thesis adopts and the position against it. A position paper, not a test. **Supports** objection 8 at argument strength.

`seaver2018captivating` | Seaver, N. (2018). Captivating algorithms. *Journal of Material Culture*, 24(4), 421-436. doi:10.1177/1359183518820366
- *Read status:* abstract only.
- *Abstract:* recommender makers describe their purpose as "'hooking' people – enticing them into frequent or enduring usage", with the rise of "captivation metrics – measures of user retention".
- *Bearing:* an ethnography of platform builders. **Supports** the version of objection 8 that says effortless engagement serves the platform's retention goal; the abstract does not itself test whether an easier mediator benefits users less. Zuboff (2019) I leave to the lab card, which holds three passages only; I do not cite her.

`vasconcelos2023explanations` (read in full: card library/vasconcelos2023explanations.md; Part 1 cites it at line 102): explanations reduce overreliance when they lower "the costs of verifying the AI's prediction." The effect appeared only in the hard task, and a harder-to-check explanation did no better than no explanation (Studies 1 and 2). **Complicates** objection 8 in the author's favour: cost-lowering helps when it makes verification cheaper than doing the task. The abstract's own wording: "some of the null effects found in literature could be due in part to the explanation not sufficiently reducing the costs of verifying".

`noessel2026deskilling` (abstract only; a 2026 paper with zero citations at retrieval): reports a "controlled design intervention that reversed [deskilling] in a navigation task" through a "Human Goes First" forcing function. An indicator that designers are already arguing for friction; not a pillar.

`plato1925phaedrus` | Plato, *Phaedrus* 275a (Fowler tr.), read at Perseus: "this invention will produce forgetfulness in the minds of those who learn to use it ... You have invented an elixir not of memory, but of reminding; and you offer your pupils the appearance of wisdom, not true wisdom". The clause on the "appearance of wisdom" runs into 275b (card: library/plato1925phaedrus.md). The oldest form of the worry. Its subject is writing, not word spacing; the step to spacing is **argument only**.

### Objection 9. Internal consistency

No external sources. All locators are in the repo; they are listed with the reword in section (c), objection 9.

### Objection 10. What an examiner would attack

`dewinter2014fitts` (read in full: card library/dewinter2014fitts.md; the authors reject the critique's conclusion for the Fitts list, sections 3.2.1 and 4) and `dekker2002maba` (record verified; not obtained; web-search summary only, treated as unverified): the human-factors critique of static function allocation, which holds that moving work from person to machine changes the work and the person's role rather than merely subtracting it. If the web summary is right, an examiner can read "work moved from reader to artefact" as the substitution assumption the field has criticised for two decades. I cannot quote either. Part 1 cites de Winter and Dodou at line 82 and lists "function allocation" as the 1951 Fitts forecast.

---

## (c) Synthesis by objection

Each objection has four parts: the objection at full strength, the best sources, how much of the thesis it defeats, and what the author would have to concede. I say where the support is argument and not sources. Defeat is rated on `CLAIM.md`'s four parts (precedent, consequence, transfer, foil).

### 1. The analogy fails at the object

**The objection.** Reading is one person facing a text that does not respond. Algorithmic coordination is two people facing a mediator that adapts, reads both of them and commits outcomes neither controls. A page convention solved a perceptual segmentation problem: where does one word end. No perceptual fix addresses a counterpart with an objective of its own. The author already says so. Part 1 line 118: "Written text is dyadic and asynchronous, but fundamentally passive ... Traditional media hold still; an algorithmic intermediary does not." Line 64: the intermediary "does not share its users' goals". Add the interest asymmetry. The scribes were readers' kin: learners and teachers of Latin, with no reason to hide a word boundary from the person who needed it (argument only). The mediator's owner has a reason to hide, and in practice also owns the interface. Jensen and Meckling (p. 308) say the cost of aligning an agent to a principal is generally not zero, and a residual loss remains after monitoring and bonding (which include operating rules). Rosenblat and Stark (pp. 3758, 3761) document an interface that is the control instrument. Mathur et al. (abstract) find interface choices built to benefit the service, sold as turnkey. "Redesign the interface" therefore assigns the remedy to the party with the conflicting interest.

A second form concerns the "trained elite". The analogy needs a class of people who can already do the thing, to whom the move extends access. Part 1 says the opposite: Kahneman and Klein's conditions for expertise are disrupted by an adaptive intermediary (line 66), the field has "no validated scales indexing algorithmacy" (line 156), and higher self-reported AI literacy goes with worse calibration (line 138, Fernandes et al.). A reader of *scriptio continua* could master a stable code with practice, and facet E records an anecdotal report that skilled modern readers read unspaced French with ease, at a 40-70% speed cost (Mirault et al., p. 22). If nobody masters the mediator, there is no unspaced-script elite for a spacing move to un-train.

**Best sources.** `jensen1976theory`, `rosenblat2016algorithmic`, `mathur2019dark`, Part 1 lines 64, 66, 118, 138, 156. The point about the scribes' shared interest is argument only.

**Damage.** To the transfer, serious. It does not touch the precedent (spacing did lower a cost) and not much of the foil. It leaves "an artefact-side fix" possible, but not an artefact the interested party designs. It also forces a choice about which artefact: the platform's interface (compromised by interest) or one the user side or a third party controls.

**What the author must concede or change.** (a) Drop any suggestion that the platform's UX layer is where the move happens, or say who else builds it. (b) Say what in the spacing story the algorithmacy case reproduces: a public convention that no single party owns. Spacing belonged to no one. **[Agent wording]**: "Word separation was a convention that belonged to no one scribe. The algorithmic case needs a convention the intermediary's owner cannot unilaterally withdraw." This keeps the analogy at the level of where the work sits and who governs the convention, and it points to what Part 1 already names: counter-delegation (line 144, the user's own agent) and bounded envelopes (line 148). (c) Stop saying the training requirement disappears; say instead that it has not been shown that any training works, which is Part 1's own gap (line 156).

### 2. Who makes the move

**The objection.** The conventions were designed for readers who learned Latin as a foreign language (Parkes p. 1, relayed); whether the scribes were those readers is not shown. A design discipline works inside firms that own the interface. The history of a user-driven convention is weak precedent for what a firm's designers will do. von Hippel argues that users who innovate can build what they want instead of relying on manufacturers as their agents (ch. 1, p. 1).

**Best sources.** `vonhippel2005democratizing` (ch. 1, p. 1), `rosenblat2016algorithmic` (p. 3761), `saenger1997space` (p. 11, relayed), the author's own draft (section 5.1, write access as "scarce capital"). I found no source on who governed scribal practice in the Insular scriptoria; that part is argument only.

**Damage.** To the transfer, moderate; to the precedent, none. It reinforces objection 1 and changes the question from "what is the move" to "who may make it".

**What the author must concede.** The precedent supports user-side and commons-side moves (counter-delegation, standards), not firm-side UX. Part 1's remedy list (lines 142 to 148) already points the same way. The foundation paper should say that the discipline's client may not be the platform. Whether that is still "design" in the HF sense is for the author.

### 3. Technological determinism

**The objection.** "The critical UX move that ignited literacy" is the autonomous model: a feature of a technology produces a social and cognitive outcome regardless of the conditions that surround it. Street (2003, p. 77) names it and rejects it; Part 1 invokes Street to dismantle Ong and Goody and Watt (line 120; Street 2003 itself never mentions Ong or Goody, so that target is Part 1's attribution, to Street 1984) and warns that claims about algorithmic interfaces rewiring consciousness "fall into the same trap". A sociologist of literacy reading an HCI paper that credits spacing would ask who taught whom, who was permitted to read, which institutions required reading, and why uptake took three centuries on the Continent. Saenger's abstract (relayed) says separation reached the Continent "only in the late tenth century" (Saenger's date; Parkes dates Carolingian adoption to the 8th-9th century, per facet E:316). His explanation for why the ancient world did not separate words is social (the elite wanted no broad reading, p. 11); I have no source on his explanation of the continental lag.

**Best sources.** `street2003whats` (p. 77), Part 1 line 120, `saenger1997space` (abstract and p. 11, relayed). Scribner and Cole, Graff and Finnegan are the standard authorities but I could not open them.

**Damage.** To "ignited" and to H-cause, near-total. To H-cost, none. This is the cheapest objection to answer and the most damaging to the wording as it stands. `CLAIM.md`'s "Do not claim" list already includes: "That word separation created silent reading, unless the research supports it." And facets A to C hold the evidence.

**What the author must concede.** Retire "ignited". **[Agent wording]**: "Word separation lowered the cost of fluent reading of Latin and widened the group who could do it without long training; other conditions determined whether anyone did." That is facet E's safe wording (E1) restated for this paper. The author's phrase "critical UX move" needs the same treatment. "Critical" is a judgement the sources do not make.

### 4. Survivorship and selection

**The objection.** The paper picks the one layout convention that persisted and calls it critical. Hindsight chooses it. And the Romans had word dividers and gave them up (Saenger p. 12, p. 29, relayed), so the move was not an obvious improvement to the people who had it.

**Best sources.** `saenger1997space` (relayed). The wider claim that many conventions came and went is **argument only**; Parkes describes a complex of conventions (RESEARCH_PLAN §4.4, paraphrase), which is the likely place to document it.

**Damage.** To "obvious" and "critical", moderate. To the thesis as an analogy, small: the analogy needs one documented case of work moving to the page, not a prediction that such moves always win.

**What the author must concede.** Drop any wording that implies inevitability. Use the Roman reversal as an asset: it shows the move is a choice whose adoption depended on who wanted reading widened, which feeds objections 1 and 2. The author should not say "the Romans did not need it".

### 5. The single-move framing is a designer's heroic story

**The objection.** Infrastructures and conventions are slow accretions. Star and Ruhleder (abstract) report a custom system for geneticists with high user satisfaction in which many users still "experienced difficulties in signing on and use", and analyse the change as multi-level infrastructural learning. David (1985) is, on my recollection, the standard account of how conventions lock in by accumulated, interlocking choices (argument only, not read). The "killer feature" is a retrospective story. Part 1 line 118 says "Literacy, numeracy, and oracy are competencies for engaging a medium; algorithmacy is a competence for engaging a coordination", which already breaks the one-move shape.

**Best sources.** `star1996steps` (abstract only), `david1985clio` (not accessible), Part 1 line 118. Liebowitz and Margolis (1990) warn that the QWERTY lock-in story is contested; I could not read either side. Edgerton and Bowker and Star: not verified or not searched.

**Damage.** To "a similar move", moderate; to the analogy, small. RESEARCH_PLAN §4.4 already flags the shape.

**What the author must concede.** Say "a complex of conventions" or "a set of moves", not "a move". **[Agent wording]**: "We need conventions, not a feature."

### 6. Nadella is right, and the paper misreads him

**The objection.** For agentic systems with real authority, deterministic external controls, least privilege, audit and a kill switch are the tested practice of safety-critical engineering. Nadella's P6, P11, P17 and P19 are that practice: deterministic system design (P6), controls that a program cannot bypass or tamper with (P11), organisations determining independently what a model can access (P17), and a power to pause or shut a model down mid-task (P19). Leveson (via the lab card, p. 76) puts safety in enforced constraints; Saltzer and Schroeder name least privilege and complete mediation. An "engagement layer where the user reads and rewrites the shared mediator" (RESEARCH_PLAN §3) is, from that tradition, a write path into a controlled component: what security engineering forbids unless the writer is authorised, scoped, logged and reversible. And the post is about enterprise insider risk (P8, the enterprise; P17, organisations). Answering it with an interface-design argument looks like a category error, the more so because the author did not select the "enterprise, not user" reading when he listed what he opposes (`SOURCE.md`, answers table).

**Best sources.** `nadella2026models`, `saltzer1975protection`, `leveson2011engineering` (relayed). Reason, Perrow and Roberts are leads only.

**Damage.** To the foil, serious if it stands. To the thesis's core (precedent and transfer), none: the objection concerns the target, not the argument.

**Is there a principled reply?** Yes, in three parts. (1) The author's two claims sit at different layers. Containment bounds what a model may do to the organisation. The engagement layer is about a person's standing against a platform's mediator that the person did not choose, which is Part 1's setting (line 60, 64). Nothing in P1 to P21 gives the person on the other side of a platform's mediator any authority; P20 names "those affected" only as recipients of disclosure. (2) The reply must also grant the security point: write access to a shared mediator is a privilege and needs least privilege, audit and rollback. The author's own draft already treats write access as licensed (section 5.1). Counter-delegation (Part 1 line 144) is the safer form, because the user's agent acts on the user's side instead of rewriting the shared component. (3) Saltzer and Schroeder's "psychological acceptability" principle answers the charge that interface argument is out of place: security engineering writes the human interface into its own principles.

**What the author must concede.** The paper cannot say Nadella is wrong about containment; he is right inside his scope. It must say whose authority his scope covers. It also has to choose between "the user rewrites the shared mediator" and "the user's agent bargains against it", because only the second survives the objection and Part 1 already holds it.

### 7. The two are complementary, not opposite

**The objection.** Containment governs what the system may do; interface design governs what the person must do. Calling Nadella "the exact opposite" (`SOURCE.md`) is rhetorical excess, and the author's own Part 1 shows why. Part 1 says the remedy is not "to demand that the user study harder or read more complex displays" but to constrain the system so that its "parameters, criteria, and cadences" are ones "human perception can track" (line 68), and lists "bounded operational envelopes" and "structural refusal" (lines 146, 148). Those are containment. Nadella's P9 says chain-of-thought transparency on its own is "not sufficient or dependable", which is Part 1's line 136 to 140 in other words. His containment principle (P19, the emergency brake) is a containment control, close to Part 1's bounded envelopes; it differs from structural refusal in who holds it. P3 and P20 name a provider and affected people, and P14 adds several models, so "keeps the dyad" is also overstated.

The counts as set out in `RESEARCH_PLAN.md` §3 are weakened one by one:

| Author's count | What the post says | Verdict |
|---|---|---|
| Legibility paradigm: "observe, log, audit" | P6 puts the weight on deterministic system design, P11 and P17 on external control, P19 on a brake; P15 does ask for "human readable evidence" | Partly right. The post has a legibility strand (P15) inside a structural frame (P6, P11, P17, P19). It is not at its core a text that "answers opacity with more reading" (RESEARCH_PLAN §3). |
| Keeps the dyad | P3 (provider), P20 (people affected), P14 (several models) | Overstated. The post's agent is a model; the parties named include a provider and affected people. |
| Containment versus engagement | P5 splits who supplies intelligence from who holds "the authority over it" | The real difference, and it is about who holds authority, not about opposite remedies. |

**Best sources.** `nadella2026models`; Part 1 lines 68, 136-148; `parasuraman2000model` and `bainbridge1983ironies` (relayed); `saltzer1975protection`.

**Reading on which both hold.** Containment is the floor: nothing the engagement layer does may widen the model's authority, and the organisation keeps the brake. The engagement layer is what the person facing the mediator can do inside that floor. Parasuraman et al. (pp. 287-288, relayed) separate the level of automation from the function allocated to the person. On this reading the author's remedy list and Nadella's principles compose.

**Damage.** To the foil, severe as phrased; the objection leaves the thesis intact in a weaker form.

**Wording the author could defend.** **[Agent wording]**: "Nadella answers who controls a model inside an organisation. Algorithmacy asks what the person on the other side of a platform's mediator can do. The first needs deterministic containment. The second needs more than containment, because the person is not the organisation." If the author wants to keep an opposition, the defensible one is on authority (P5 against Part 1's user standing), not on remedy.

### 8. Lowering the skill needed has costs

**The objection.** Easier is not better. Bainbridge (via the lab card, pp. 775, 777) argues that automation raises the importance of the operator and that the remedy is deliberate inefficiency, a process the operator can follow "even when this may not be the most efficient". Buçinca et al. find that forcing functions beat simple explanations only on the questions where the AI was wrong, with no overall gain (H1b unsupported, p. 188:16), and users liked them least. Cox et al. (p. 1390) name the "standard argument" that frictions should go and argue it breeds "mindless forms of interaction". Plato's oldest version (*Phaedrus* 275a) says a convenience of reminding gives "the appearance of wisdom, not true wisdom". And the lab's own note says it: abstraction "lowers load while also hiding the mediator's agenda" (`org_frontier/essays/scifi_interfaces_and_algorithmacy.md:11`). The author's draft goes further and argues against abstracting the steering surface from a party "already steering" (`dial_response_algorithmacy/draft.md:337`), because it "hides her own contribution from her while keeping that contribution available to the operator". Seaver's abstract describes builders who want to hook people. A seamless mediator may serve retention more than the person.

**Best sources.** `bucinca2021trust`, `cox2016design`, `bainbridge1983ironies` (relayed), `seaver2018captivating` (abstract), `plato1925phaedrus`, the essay line and the draft. In the favour of the author: `vasconcelos2023explanations` (abstract) shows that when an explanation really cuts the cost of checking, overreliance falls.

**Damage.** To the transfer, serious in its strongest form: "take the work off the person" cannot be a general principle. It does not touch the precedent.

**The dilemma it creates.** Spacing makes the text's own structure explicit and removes nothing. Read that way, it is a legibility device (Parkes's "grammar of legibility"; RESEARCH_PLAN §4.2), which the first ruling rejects. Read the other way, as lowering load without exposing the mechanism, it is the abstraction that the essay (line 11) and the draft (line 337) say hides the mediator. The analogy has one reading that breaks the first ruling and one that breaks the second.

**What the author must concede.** The work to move is the work that does not teach the person the mediator's stakes. **[Agent wording]**: "Move the work of finding the joints; keep the work of deciding." The moved work must be work whose removal leaves the person's judgment and their view of the counterpart's interests intact. This is also what Bainbridge's remedy does (hold the system to a pace the person can follow).

### 9. Internal consistency

I list each inconsistency with its locators and the smallest reword that removes it. All rewordings are **[Agent wording]**; the author decides, and where his text is involved I flag it and leave his words in place.

**9a. The model is a legibility innovation; the rulings reject legibility.**
- Rulings: `decision_experience_design/README.md:38-43` ("Algorithmacy is not legibility"); Part 1 line 22 (the problem "cannot be solved through the traditional UX toolkit of legibility, visual layout, and cognitive load reduction") and line 92 ("research on reading, visual layout, and cognitive load cannot resolve" it).
- The model: word separation, which Parkes calls the "grammar of legibility" (RESEARCH_PLAN §4.2); `draft.md:263` and `:337`; `CLAIM.md` precedent.
- Why it matters: a visual-layout, load-reducing innovation from the history of reading is exactly what Part 1 says cannot solve the case. Lines 56 to 64 say the same of Ecological Interface Design, which also puts a constraint into a perceptual form.
- Smallest reword: say the precedent is about *where work is placed*, and drop "the interface becomes legible". **[Agent wording]**: "The precedent shows that work can be moved from the person to the artefact. It does not show that a more readable display solves the algorithmic case."

**9b. "Ignited" and the ruling that the history is an analogy.**
- `part2_ethics/README.md:8` (history is "an analogy, not a mechanism"); `decision_experience_design/README.md:45-52` (no Ong-style restructuring); Part 1 line 120 (Street "dismantled" the autonomous model); `SOURCE.md` ("ignited literacy"); `CLAIM.md` (H-cause). `RESEARCH_PLAN.md` §3 records the author's answer "Let the research decide", so the contradiction is open by design.
- Smallest reword: H-cost wording, as in objection 3. If the author keeps "ignited", it needs a source that supports a causal claim; none of my sources do.

**9c. Part 1 says the remedy is a structure; `CLAIM.md` says it is a move on the reading side.**
- `CLAIM.md` transfer: "coordination ... is today in the condition of unspaced script: only the trained can do it." Part 1 lines 66, 138, 156 give no evidence that any trained group can do it.
- Smallest reword: **[Agent wording]**: "Coordination through an algorithmic third party is a task nobody has shown how to do reliably."

**9d. "A sensibility" is a property of persons; the remedy is placed in artefacts.**
- `algorithmacy_ot/manuscript/PAPER.md:19-21`: "the sensibility to navigate opaque triadic coordinative cooptation", with competencies to interpret, specify and keep track; Part 1 line 22 calls it "a measurable, domain-specific competence". The remedy (spacing, bounded envelopes, structural refusal) is built into artefacts and structures.
- Smallest reword: **[Agent wording]**: "Algorithmacy is the person's sensibility. DXD designs the conditions under which a person without it can still act well." Part 1 line 150 already makes the matching move for designers.

**9e. The engagement layer asks the person to read; the first ruling says not to ask the person to read.**
- `SOURCE.md` (quoting `phd1750_topic_and_rationale.md:52-54`): "where reading and rewriting the shared mediator is the fundamental mode"; `RESEARCH_PLAN.md` §3, Nadella count 3: "engagement layer where the user reads and rewrites the shared mediator". The rulings: `README.md:38-43`.
- This turns the author's first count against Nadella ("he answers opacity with more reading") on his own proposal.
- Smallest reword: this is the author's text, and I leave it. If he wants to keep both, the count against Nadella has to move to authority (objection 7), because "reads" appears on both sides.

**9f. Abstraction lowers load but hides the mediator; the draft uses word separation both ways.**
- `org_frontier/essays/scifi_interfaces_and_algorithmacy.md:11` (abstraction "lowers load while also hiding the mediator's agenda"); `draft.md:263` (word separation changed "the interface so that reading no longer required the training") and `draft.md:337` (abstracting the steering surface "hides her own contribution from her"; word separation is "again the precedent"). The two sentences cannot both treat word separation as the model for load-lowering and the model against abstraction without the dilemma stated in objection 8.
- Related flag: `draft.md:337` credits Inman and Ribes (2019) with the point about what the precedent redistributes; `literature/REUSE.md` warns their paper is about seamful design and the attribution needs checking. I did not check it.

**9g. The "enterprise, not user" reading.** `SOURCE.md` answers table: the author did not select it. The post's text points to the enterprise throughout (P8, P9, P17). Not an inconsistency in his text, but the research should tell him the text favours the reading he declined.

**9h. Smaller items.** Part 1 line 120 (Ong and Goody and Watt "rewired the neurological architecture"; Street 2003 does not mention Ong or Goody) has no audit (`REUSE.md`) and sits beside the ruling against restructuring claims. The author writes "scriptura continua"; the scholarly term is *scriptio continua* (RESEARCH_PLAN §2).

### 10. What a human-factors examiner would attack first

An argument, not a source set. In order:

1. **"Ignited literacy."** A causal claim in the title position with no evidence. Street (2003, p. 77) and Part 1's own line 120 supply the rebuttal.
2. **What is "the move", and what would show it wrong?** No operational definition and no disconfirming case. Part 1 does state falsifiable propositions (lines 158 to 166); this paper does not yet.
3. **Function allocation.** "Work moved from reader to artefact" is a function-allocation claim. If the Dekker and Woods critique is as the search summary says (unverified), the examiner will ask what the paper does about work that changes character rather than disappearing. `dewinter2014fitts` is in Part 1 already; the author should read both.
4. **The analogy's dyad.** The HF literature Part 1 reviews is dyadic (line 112). The history of reading is dyadic. The examiner will ask what is human-factors about the triadic step; Part 1's answer is the unit of analysis, but the move proposed here (objections 1 and 2) leaves the human-factors discipline.
5. **Novelty.** Facet Z has not reported. I claim nothing.
6. **Provenance and citation checks.** Part 1 opens with an AI-authorship disclosure (line 15). The Gemini essays are leads, not sources (RESEARCH_PLAN §6). An examiner who checks one citation will check more.

---

### Ranking by damage, with the answer to each of the top five

Damage is the harm that remains after the cheapest repair.

| Rank | Objection | Part of the thesis it hits | Damage after cheapest repair |
|---|---|---|---|
| 1 | 1. Analogy fails at the object (interested third party; no elite to un-train) | Transfer | High. The remaining problem is who builds the artefact. |
| 2 | 9. Internal consistency (esp. 9a, 9e, 9f) | Precedent, transfer, foil | High until reworded; the repair is wording plus one decision by the author. |
| 3 | 7. Complementary, not opposite | Foil | High on "exact opposite"; low once the contrast moves to authority. |
| 4 | 3. Technological determinism ("ignited") | Consequence | Total on H-cause; none on H-cost. The cheapest repair. |
| 5 | 8. Lowering the skill has costs | Transfer | Medium. It removes "take the work off the person" as a principle. |
| 6 | 6. Nadella is right | Foil | Medium. A reply exists (scope plus least privilege). |
| 7 | 2. Who makes the move | Transfer | Medium; folds into 1. |
| 8 | 10. Examiner attacks | All | Medium; most are answered by the other repairs. |
| 9 | 5. Single-move framing | Wording | Low. |
| 10 | 4. Survivorship | Wording | Low. |

**Concessions and rewordings for the top five. All [Agent wording].**

1. *Objection 1.* Concede that the platform's UX layer cannot carry the move. "Word separation was a convention that belonged to no one scribe. The algorithmic case needs a convention the intermediary's owner cannot unilaterally withdraw." Say who builds it: the user's own agent (Part 1 line 144), a public standard, or a regulator. Also concede that no one has shown a trained elite exists (line 156).
2. *Objection 9.* Choose one of two roads and say so. Road A: the precedent is about placing work, and the paper makes no claim that a readable display solves the case (9a). Road B: the paper accepts a legibility strand and revises the ruling. Either way, take "reads" out of the engagement-layer description or move the count against Nadella to authority (9e); and settle the abstraction dilemma (9f).
3. *Objection 7.* Replace "exact opposite" with the contrast on authority (wording under objection 7). Acknowledge P6, P11, P17 and P19 as the containment floor and Part 1's bounded envelopes as the same kind of control.
4. *Objection 3.* Replace "ignited" and "critical" with the H-cost wording (objection 3). Cite Street (2003, p. 77) for why.
5. *Objection 8.* Replace "take the work off the person" with "move the work of finding the joints; keep the work of deciding" and state the condition (the moved work must not hide the counterpart's stakes from the person).

### What survives

Stated plainly, in terms the evidence in hand supports.

A page convention once moved a burden from the reader to the page. That lowered the cost of reading Latin fluently for people who were not long-trained, and it spread over several centuries, on dates that Saenger and Parkes assign differently. It is a fair example of a design principle in human factors: work can be placed on the artefact so the person need not do it. It does not show that design caused mass literacy, and it does not show that any one move is "the" move.

Coordination through an adaptive, interested intermediary lacks such a convention, and nothing in the sources says one lives on the platform's interface. The candidates are conventions the platform's owner cannot withdraw alone: the user's own agent, bounded and predictable behaviour from the mediator, a public standard, or exit. The work to move is the work of finding the joints, not the work of deciding, and the move has to leave the person able to see what the counterpart gains.

Containment, as Nadella describes it, is not the opposite of this. It is the floor under it. The two differ in who holds authority: the organisation over a model, or the person over a platform's mediator. The paper can defend that difference.

### Claims the sources contradict

1. "Written text is ... fundamentally passive" (Part 1 line 118) sits in tension with Street 2003 p. 77: literacy is "a social practice, not simply a technical and neutral skill". The two are different claims: Part 1 means the medium does not respond; Street speaks of literacy's effects.
2. "Ignited literacy" against Saenger's abstract (relayed): separation reached the Continent "only in the late tenth century", and against Street p. 77.
3. "Only the trained can do it" (`CLAIM.md` transfer) against Part 1 lines 66, 138 and 156.
4. "The exact opposite" (`SOURCE.md`) against Part 1 lines 68, 146, 148 and Nadella P6, P11, P17, P19.
5. "Keeps the dyad" against Nadella P3, P14 and P20.
6. "Lower the load" as a general design rule against Buçinca et al. (narrower than the abstract: wrong-AI questions only; card) and Bainbridge p. 777 (relayed).
7. "Answers opacity with more reading" against Nadella P9, which says chain-of-thought transparency on its own is "not sufficient or dependable". P15 does ask for human-readable evidence.

---

## (d) Gaps and unverified leads

- **Who governed Insular scribal practice** (objection 2). No source obtained. A human with library access should look in Parkes, *Pause and Effect*, chapter 3, and in Saenger, chapters on Insular scribes (pp. 34, 90 to 97 per facet E), and in Tunbridge's 1992 Oxford DPhil. Facet A holds the leads.
- **A catalogue of layout conventions that failed** (objection 4). Not found. Parkes is the likely holder; I did not open him.
- **Scribner and Cole (1981; and the 1978 article), Graff (1979), Finnegan (1988)** (objection 3). Records verified or carded; not opened. Scribner and Cole 1978 is in *Harvard Educational Review* 48(4); no open copy. Graff's open edition is on the WAC Clearinghouse site behind a Cloudflare challenge. Finnegan: library copy.
- **Leveson (2011)** is relayed from the lab card because the OAPEN file was walled. Anyone reopening it should check pp. 11-14, 63-67, 76-77.
- **Reason (2000), Perrow (1984/1999)**, and the high-reliability literature (Roberts 1990 abstract only; Weick and Sutcliffe not searched). The claim that defence in depth and HRO practice endorse external controls rests on Leveson and Saltzer and Schroeder alone.
- **David (1985), Liebowitz and Margolis (1990), Edgerton (2006), Bowker and Star (1999).** Not obtained, no book record found, or not searched. Objection 5 is thin on sources.
- **Dekker and Woods (2002), de Winter and Dodou (2014).** De Winter and Dodou has since been read in full (card); I could not open Dekker and Woods. Objection 10's point on function allocation depends on both; the Dekker and Woods description is from a web-search summary and unverified.
- **Seaver (2018)** abstract only; **Zuboff (2019)** not used. For objection 8 the body of Seaver is the next read.
- **The lab's own essay `org_frontier/essays/the_interested_third_party.md`** is named in `scifi_interfaces_and_algorithmacy.md` and bears on objection 1; I did not read it.
- **Gray et al. (2018)** and **Vasconcelos et al. (2023)**: both since read in full (cards).
- **Hirschman (1970), exit and voice**: the lab holds a local PDF (earlier Part 4 facet X, row 27). I did not use it; it bears on exit as the structural-refusal analogue in objections 1 and 7.
- **Facet Z (novelty)** has not reported. Nothing here is a claim of novelty or its absence.
- **Facets A, B, C, D, E, F, G, H**: where I cite their territory I rely on the existing Part 2 facet E and the lab cards, not on this run's other agents, whose files I did not read.

## Changes after full-text cards (2026-10-13)

- `bucinca2021trust`: result narrowed (forcing functions beat simple explanations only on wrong-AI questions; no overall gain; the two designs did not differ; no AI condition reached the no-AI level; H1b unsupported, p. 188:16); fixed in the entry, in objection 8, in the list of sources the claims contradict (item 6), and flagged beside Part 1's line 106 quotation; read status "read in full (card)".
- `street2003whats`: added that the article never mentions scriptio continua, word separation or any page convention, and never mentions Ong or Goody (the Ong and Goody target is Part 1's attribution to Street 1984), in the entry, objection 3 and item 9h; "a sociologist's answer" replaced; Street does not call technology irrelevant (p. 79); read status "read in full (card)".
- `mathur2019dark`: marked as a two-party setting (operator and shopper, vendor on the supply side), not a triad; 11.1% is a lower bound; bias links unvalidated (section 6.4); read status "read in full (card)".
- `gray2018dark`: "designer as the interested party's instrument" qualified: the paper says designers "could easily become complicit" (abstract; pp. 9-10) and does not measure how often; "not opened" updated to "read in full (card)" (here and in the open-items list).
- `vasconcelos2023explanations`: effect only in the hard task; a harder-to-check explanation did no better than none; read status "read in full (card)".
- `cox2016design`: p. 1390 marked as proceedings pagination not shown in the accepted text; `plato1925phaedrus`: the "appearance of wisdom" clause runs into 275b; `dewinter2014fitts`: read in full, authors reject the critique's conclusion for the Fitts list (3.2.1, 4); `hunt2026decision`: line 40 claim confirmed, no change.

Synthesis verdicts changed: none to the objection verdicts. The wording of two bearing verdicts changed: Buçinca "shows the design that demanded more of the user did better" became "better only on wrong-AI questions, no overall gain"; Mathur "the designer ... often the interested party's instrument" became a two-party, operator-side finding.
