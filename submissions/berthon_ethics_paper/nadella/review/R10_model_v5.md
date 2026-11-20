# R10 — A structural model for the v5 outline (seventeen errors)

*Agent-drafted, 2026-11-19; the author has not reviewed it.*

## 1. Task and incumbent

The v5 outline (`../STRUCTURE.md`) is a typology. A present case opens the paper, and a construct and a precedent follow, then criteria. Seventeen errors come next, grouped into five families, and each entry runs historical instance → contemporary objector → present repetition → Nadella's move. A consolidated table follows, then disanalogies, objections, a table of duties (each the inverse of a family) and a short conclusion. The brief asked for a 2022–2026 journal article built the same way, scored against the incumbent, Diamantis (2025, *BEQ*), which R7 and `MODEL_CHOICE.md` chose for the v1 draft.

Word counts marked **measured** come from `pdftotext` on the copies in
`~/iit-playground/berthon_ethics_local/pdfs/nadella/R10/<key>/` (each with `SOURCE_URL.txt`). Section counts run
from one heading to the next. They include footnotes, tables and running heads, and exclude the reference list.

## 2. Result in one paragraph

No 2022–2026 article in the priority journals is built the way v5 is built. The closest structural match is **Kroll, Smart, Geiger & Jacobs (2026), *Harvard Data Science Review***. It presents six named "unlearned lessons", each its own subsection and each drawn from historical disasters before being mapped to present AI. A consolidated table follows (lesson → symptom → from disasters → expression in AI systems), then eight mitigating practices, and a conclusion that turns on Nader's *Unsafe at Any Speed*. Its venue and prose fall below Diamantis's, and on the brief's weighted score it finishes narrowly second (28.5 against 30, §5). **Recommendation: Diamantis stays as the single sentence-level model. Kroll et al. should be recorded as the structural graft for §3's entry form and the consolidated table.**

## 3. Candidates opened in full

### K1. Kroll, Smart, Geiger & Jacobs (2026), "Unsafe at any AUC: Unlearned Lessons From Sociotechnical Disasters for Responsible AI", *Harvard Data Science Review* 8(3)

- **DOI** 10.1162/99608f92.91b8834f (Crossref: issued 2026-09-01; vol. 8, issue 3). Diamond OA at HDSR. The HDSR PDF
  link returned 403 to curl, so I used the arXiv copy, 2607.14353v1, whose header reads "Volume 8 Issue 3 / DOI
  10.1162/99608f92.91b8834f". I did not collate it against the HDSR page.
- **Skeleton, measured** (body before references ≈ 13,100):

  | Section | Words |
  |---|---|
  | 1. Introduction | 1,139 |
  | 2. Systems Safety as an Analytical Lens | 1,138 |
  | 3. Unlearned Lessons (preamble) | 251 |
  | 3.1 Poor Risk Perception | 429 |
  | 3.2 Incentives | 233 |
  | 3.3 Permanent Rush Cultures | 319 |
  | 3.4 No Bad News | 242 |
  | 3.5 Safe Components Do Not Imply Safe Systems | 557 |
  | 3.6 Kick the Can | 832 |
  | Table 1. Unlearned Lessons from Sociotechnical Disasters | 255 + (table text runs into §4 count) |
  | 4. Mitigating Risk Sociotechnically, not Instrumentally (4.1–4.2) | 775 |
  | 4.3 Curmudgeons & Critics | 378 |
  | 4.4 Traceable Processes | 870 |
  | 4.5–4.7 Inclusive spaces · External participation · Failure is normal | 825 |
  | 4.8 Structural Incentives for Meaningful Self-Regulation | 488 |
  | 5. Research agenda (5.1 SRE as precedent · 5.2 Who Governs Safety? · 5.3 Operationalizing Risk Frameworks) | 2,159 |
  | 5.4 Applying Systems-Safety Methods to AI | 1,046 |
  | 6. Conclusion: History Doesn't Repeat Itself, But It Rhymes | 1,180 |

- **Fit to v5.** Each lesson follows the same order: it names the error, gives one or more historical disasters (Challenger, Three Mile Island, Therac-25, USS Scorpion, Chernobyl, Boeing 737 MAX, SVB), then a present AI example. That is our entry form without the "contemporary objector" slot. Table 1's columns (*Unlearned Lesson · Symptom · From Disasters · Expression in AI Systems*) are our consolidated table almost exactly. Section 4's eight practices are remedies, and they read as the inverse of the lessons, as our duties do, though they are not stated as duties. The entries run 233–832 words, close to our planned ≈380 per error (6,500 ÷ 17).
- **Misfit.** It has no single corporate case, no construct-and-precedent section, no disanalogy section and no objections section. Its §5 research agenda (≈3,200 words) has no counterpart in our paper. The criteria section (§2, "systems safety as lens") is a lens rather than a test of gravity.
- **A content point, not only a structural one.** The conclusion (raw text lines 1032–1040) says the auto industry's "three E's: Engineering, Education, and Enforcement" "framed safety problems away from vehicles to avoid taking responsibility for the ways system design could cause harm". That is the paper's own historical parallel for our family D (who bears the burden) and for "AI literacy" as a remedy. If it is used, it needs carding and a check against the HDSR page.
- **Representative paragraph** (§3.3, second and third paragraphs; arXiv pp. 7–8):

  > A similar rush culture has been identified in the former Soviet Union as contributing to the Chernobyl
  > disaster. The Politburo demanded to increase the speed of construction of nuclear power plants to meet urgent
  > domestic energy demands, and this constant haste lead to the nuclear industry in the USSR ignoring hazards,
  > safety shortcomings, and design flaws (Chernov & Sornette, 2016). Risks to reactors were systematically
  > downplayed as insignificant. Proximate to the accident, a planned safety test was delayed many hours into the
  > night so that power output could remain high to support the meeting of end-of-quarter production quotas at
  > nearby factories, causing a hazardous condition unrecognized by the late-shift operators.

  The prose is clear and concrete, with list-heavy sentences and a data-science/STS register. It has a slip ("lead" for "led") and no sentence-length variation of Diamantis's kind.

### K2. Muldoon & Wu (2023), "Artificial Intelligence in the Colonial Matrix of Power", *Philosophy & Technology* 36(4), art. 80

- **DOI** 10.1007/s13347-023-00687-8; CC BY 4.0; Springer PDF downloaded. OpenAlex: 230 citations.
- **Skeleton, measured** (body ≈ 9,000): 1 Introduction 959 · 2 The Colonial Matrix of Power 943 · 3 Decolonial
  Perspectives on Data and Technology 1,423 · 4 The Colonial Supply Chain of AI 1,500 · 5 An International Division of
  Digital Labour 1,496 · 6 Hegemonic Knowledge Production + 7 Conclusion 2,697 (the conclusion heading did not separate
  in the extraction).
- **Fit.** Three named dimensions, each reading a present AI practice as a continuity of a historical (colonial) structure. Among the priority journals, this is the closest to "history judges the present, dimension by dimension".
- **Misfit.** It has three dimensions, not a typology of many entries, and no single firm case, consolidated table, duties or objections. A framework section and a literature section take a third of the body.
- **Representative paragraph** (§4, p. 8): "Technology companies frame AI technologies as tools for increasing human
  and technical productivity, with promises of creating an environmentally friendly and efficient global economy
  (Dauvergne, 2022; Nost & Colven, 2022). Crawford (2021, 48) reminds us that corporate narratives of AI are often
  completely abstracted from the physical reality of its operation … Through analysis of the connections within
  multi-layered supply chains, we uncover how the global relationships of labour exploitation and knowledge
  extraction in the AI supply chain are actively enabled by the continuities of historical colonialism." The prose is citation-dense and theory-led, with long nominal subjects.

### K3. Coggins & Steinert (2023), "The seven troubles with norm-compliant robots", *Ethics and Information Technology* 25(2), art. 29

- **DOI** 10.1007/s10676-023-09701-1; CC BY 4.0; Springer PDF downloaded.
- **Skeleton, measured** (body ≈ 11,300): Introduction 918 · What are norms? 1,027 · Seven troubles (preamble) 186 ·
  Norm biases 767 · Paternalism 895 · Tyranny of the Majority 1,215 · Pluralistic ignorance 1,062 · Paths of least
  resistance 1,361 · Outdated norms 1,203 · Robot-Induced Norm Change 1,708 · Conclusion (with mitigation
  strategies) 960.
- **Fit.** It is the cleanest "N named wrongs, one section each" typology in a priority journal, and it ends in remedies.
- **Misfit.** The paper has no historical cases (the troubles come from older theory, such as Mill), no firm case, no table and no duties. The prose is weak: it comments on itself ("We aimed to introduce our readers…"), repeats itself, and has typos ("norm-compliment robots").
- **Representative paragraph** (Paternalism, p. 5): "We mentioned earlier that organizations that wish to create
  norm-compliant robots could ask a group of experts or stakeholders to select norms they believe a robot should
  observe. … In this section, we critique the notion that we should let some, pre-selected people decide which
  norms a robot will uphold. We argue that this strategy may produce robots that enforce norms an authority
  unilaterally decided others ought to follow for their own good."

### K4. Braun & Müller (2024), "Missed opportunities for AI governance: lessons from ELS programs in genomics, nanotechnology, and RRI", *AI & Society* 40(3), 1347–1360

- **DOI** 10.1007/s00146-024-01986-0; CC BY 4.0. **Measured** body ≈ 8,000: §1 1,304 · §3.1 genomics era 1,408 · §4
  nano era 1,596 · §5 RRI era 1,064 · §6 summary 264 · §7 "All ethics, all good? ELS programs and AI" 2,387.
- **Fit/misfit.** The history runs era by era, and the lessons for AI come only at the end in one section. That is v4's shape (history, then present), not v5's error-by-error shape. It is short.

## 4. Screened and set aside

| Item | DOI | Why not |
|---|---|---|
| Raji, Kumar, Horowitz & Selbst 2022, "The Fallacy of AI Functionality", FAccT | 10.1145/3531146.3533158 | Conference paper, not a journal article. **Measured** ≈ 9,950 before references, with a failure taxonomy (§4.2, 3,633) and interventions (§5, 2,727). Case-based taxonomy, no history. arXiv 2206.09511 copy saved. |
| Napoli & Adi 2026, "On moving fast and breaking things … again", *Information, Communication & Society* 29(6) 1912–1928 | 10.1080/1369118x.2025.2513668 | By its abstract, a set of social-media governance "missteps" mapped onto generative AI, so a likely typology. Closed access: Taylor & Francis returned 403, OpenAlex lists no OA location, and the Duke Scholars record links only the DOI. **Abstract only**, 17 pp. The author can open it through the library. |
| Ulnicane et al. 2021, *Interdisciplinary Science Reviews* | 10.1080/03080188.2020.1840220 (from Consensus record) | "Déjà vu" lessons from earlier emerging technologies; 2021 is outside the date range. |
| "Responsible research in AI: lessons from the past", *AI & Society* 2024 | 10.1007/s00146-024-01929-9 | **Measured** 1,017 words (letter). |
| Rafanelli 2022, *Big Data & Society* | 10.1177/20539517221080676 | Lessons from political theory, not from historical cases. |
| Toffert et al. 2026, "Seven barriers…", *AI & Society* | 10.1007/s00146-026-03118-2 | Systematic review (1,085 publications); typology without history. |
| Tacheva & Ramasubramanian 2023, "AI Empire", *BD&S* | 10.1177/20539517231219241 | Interlocking-oppression framework; Sage PDF returned 403; abstract only. |
| Judge, Nitzberg & Russell 2024, *Policy and Society* | 10.1093/polsoc/puae020 | Lessons from aviation and nuclear regulation, argued as a regulatory model, not a typology. |
| Silver et al. 2024, "Excusing Corporate Wrongdoing and the State of Nature", *AMR* | 10.5465/amr.2020.0236 | Uses Hobbes as theory; a single excuse, not a typology. |
| Müller et al. 2026, "Seven deadly sins in AI for digital medicine", *npj Digital Medicine* | 10.1038/s41746-026-0260… (truncated in Consensus) | Clinical-informatics perspective; not a target venue; not opened. |
| Becerra Sandoval & Jing 2025, "Rethinking AI Safety: Provocations from the History of … Road and Driver Safety", FAccT | not resolved | Conference paper; history → provocations. Not opened. |

## 5. Scores

Scale 0–5 per criterion. Structure counts double, so the maximum is 35. These are my judgements from the texts I opened. For Diamantis I used the R7 data plus the section counts I took from `model/diamantis2025/diamantis2025.body` (measured, footnotes included): opening 1,991 · §1 1,339 · §2 521 · §3 preamble 267 · §3.1–3.8 269 / 1,326 / 1,594 / 686 / 547 / 616 / 547 / 532 · §4 conclusion 1,279.

| | Structure (×2) | Venue | Recency | Length | Prose | Access | **Total** |
|---|---|---|---|---|---|---|---|
| **Diamantis 2025, *BEQ*** | 3 → 6 (8 named mechanisms, one subsection each; no history, table or duties) | 5 | 5 | 4 (11,514 with notes) | 5 | 5 | **30** |
| **Kroll et al. 2026, *HDSR*** | 4.5 → 9 (6 lessons, history → AI each; consolidated table; remedies) | 2.5 (not a priority venue; data-science register) | 5 | 4 (≈13,100) | 3 | 5 | **28.5** |
| Muldoon & Wu 2023, *P&T* | 2.5 → 5 | 4.5 | 4 | 4.5 (≈9,000) | 3 | 5 | **26** |
| Coggins & Steinert 2023, *EIT* | 3 → 6 | 4 | 4 | 5 (≈11,300) | 2 | 5 | **26** |
| Braun & Müller 2024, *AI & S* | 2 → 4 | 3.5 | 4.5 | 3 (≈8,000) | 3 | 5 | **23** |

## 6. Top three against Diamantis

- **Kroll et al. vs Diamantis.** Kroll has the v5 middle and Diamantis does not: each entry moves from history to the present, and a table collects the entries. Kroll also has a closing turn on a historical precedent (Nader) and practices that invert the lessons. Diamantis has the BEQ voice, short turning sentences, concessions placed where they cost most, and a first person that marks moves. Kroll has none of these, and its register would pull the rewrite toward a technical-report cadence. Sentence-by-sentence rewriting copies the model's sentences, so a model with better structure and weaker sentences is a poor trade.
- **Muldoon & Wu vs Diamantis.** It is the better "history judges the present" exemplar in a priority journal. But it has three dimensions, not a typology, and its prose is citation-led. It does not beat Diamantis on any criterion except the presence of history.
- **Coggins & Steinert vs Diamantis.** Both are typologies with one section per entry. Diamantis's entries carry worked cases and better sentences. Coggins & Steinert has neither history nor a case.

## 7. Recommendation

**Diamantis stays** as the one model for the sentence-by-sentence rewrite. Record two departures, each grafted from **Kroll et al. (2026)**:

1. **Entry form for §3.** Name the error, give the historical instance(s), then the present expression, with each entry a numbered subsection of 230–830 words. Diamantis's 3.x subsections supply the sentences, and Kroll's 3.x subsections supply the order of moves.
2. **The consolidated table.** Model it on Kroll's Table 1: *Error · Symptom · Historical instance · Expression in AI ethics · Nadella's move*.

If the author would rather weight structure above everything, Kroll is the only candidate that matches the v5 skeleton entry by entry. The price is a non-business-ethics venue and plainer prose.

## 8. Search log

- **Consensus** (8 searches, page sizes 25–50; one with `year_min` 2022, at the brief's date range): typology of
  harms/wrongs of AI with historical cases; fallacies of AI ethics repeating technology-governance history; lessons
  from history for AI governance; seven deadly sins / N mistakes of AI ethics; historical analogy that AI repeats
  past injustices; typology of manipulation/domination mechanisms in platform design; Big Tech and the tobacco
  playbook; AI literacy repeating the literacy myth; historical cases of past technology harms mapped to AI with
  principles; JBE/BEQ conceptual papers on distinct wrongs of corporate AI. About 380 records screened by title.
- **OpenAlex** `works?filter=primary_location.source.issn:<ISSN>,publication_year:2022-2026,type:article&search=…`
  over BEQ, JBE, AMR, P&T, EIT, BD&S, AI & S, M&M and JPPM (15 per journal): "lessons from history", "fallacies",
  "typology of wrongs", "seven sins", "pathologies errors repeat". Record lookups for 18 DOIs (abstracts, OA status).
  An unauthenticated budget notice appeared but did not block calls.
- **Crossref** `journals/<ISSN>/works?query.bibliographic=…&filter=from-pub-date:2022-01-01,type:journal-article`
  (12 rows) over the same nine journals plus ICS: "lessons history artificial intelligence mistakes repeat",
  "fallacies errors AI ethics", "typology harms wrongs", "seven deadly sins technology", "failure modes ethics
  remedies transparency". Raw output in the session scratchpad (`r10/cr_log.txt`). Metadata checks for 5 DOIs.
- **WebSearch** (6 queries): Kroll et al. title; "repeats the mistakes" + P&T/BD&S; BEQ/JBE + "five wrongs"/"fallacies";
  P&T/EIT/AI & S + lessons from earlier technologies; Napoli & Adi full text; BEQ/JBE + historical parallels; "old wine
  in new bottles"/"history rhymes" + target journals. None surfaced a priority-venue article that the database
  searches had missed.
- **Fetches.** Springer PDFs downloaded without a challenge this run (Muldoon & Wu, Braun & Müller, Coggins &
  Steinert, the *AI & S* letter). The HDSR PDF, ACM PDF, Sage PDF and Taylor & Francis PDF each returned 403. Kroll and Raji
  were recovered from arXiv, while Tacheva and Napoli & Adi were not recovered. Duke Scholars was checked for Napoli (no
  author copy). No circumvention was attempted.
- **Not re-screened.** R7's candidates (Kim & Routledge, Kingston & Carnovale, Bhargava & Velasquez, Moysidou &
  Fotaki, Taylor, Lazar, Casiraghi) were used only for comparison.
