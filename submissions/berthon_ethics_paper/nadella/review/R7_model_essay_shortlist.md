# R7 — Model essays for the sentence-by-sentence rewrite

Run R7 · 2026-10-24/25 · Agent-drafted. The author has not reviewed it.

## 1. Scope and method

The task: find the published essay that best serves as a model, for structure and for sentence-level prose,
when the lead rewrites `../manuscript/DRAFT_v1.md` (about 8,300 words; BEQ limit 12,000). The criteria, in
the order the brief gave them: (1) BEQ first, then JBE, *Philosophy & Technology*, *Ethics and Information
Technology*, JPP, PPA; (2) one normative argument that uses a historical record, precedent or genealogy to
judge a present practice; (3) concessions and an objections section; (4) ends with duties, principles or
design prescriptions; (5) 9,000–12,000 words; (6) 2018–2026; (7) full text legally obtainable; (8) prose
widely regarded.

I read the openings and section skeletons of the twelve BEQ corpus texts in
`~/.claude/skills/draft/registers/beq/corpus/`, the earlier notes (`scratchpad/beq/NOTES.md`,
`scratchpad/journals/NOTES.md`, `shortlist.txt`), then ran new Crossref and OpenAlex searches over the six
journals, pulled the complete BEQ article list for 2018–2026 (364 records) and screened every title by hand,
and opened the full text of every candidate I could reach legally. Word counts marked **measured** come from
`pdftotext` on a copy I opened; "body" means the text before the reference list (footnotes and running heads
remain in the count unless stated). Downloads are in `~/iit-playground/berthon_ethics_local/pdfs/nadella/R7/<key>/`,
each with a `SOURCE_URL.txt` recording the URL, date and outcome.

**The headline finding.** No BEQ article from 2018 to 2026 uses a historical record as evidence to judge a
present technology or corporate design. I found none in the 364-record list, none in 28 Crossref and 16
OpenAlex query sets across the six journals, and none by web search. The nearest BEQ items use history as
background (Moysidou & Fotaki 2024), as a precedent for a duty (Kingston & Carnovale 2026) or as a
disanalogy check (Kim & Routledge 2022). The one article in the target journals that does read a present AI
practice against a historical record, Casiraghi (2023, *EIT*), is STS-descriptive by its abstract and I could
not open its full text (§5). So the model for criteria 1, 3–8 and the model for criterion 2 are different
essays, and the rewrite will have to graft the historical structure (Luchs 2026, the earlier model, or
Casiraghi if the author can open it) onto a BEQ frame and voice.

## 2. Search log

Tools that failed, logged once each: Consensus (monthly quota exhausted, "500 included searches"; three
calls refused), Scholar Gateway (`ACCESS_DENIED`, one call). WebSearch: four queries (BEQ + history + AI;
Bhargava & Velasquez details; Lazar PPA status; JBE/P&T/EIT + "printing press"; "lessons from the history of"
+ AI agents). None surfaced a candidate the database searches had missed.

Crossref `journals/<ISSN>/works?query.bibliographic=…&filter=from-pub-date:2018-01-01,type:journal-article`
(rows 20 for queries 1–18, rows 8 for 19–28) and OpenAlex
`works?filter=primary_location.source.issn:<ISSN>,publication_year:2018-2026&search=…` (per-page 25). Hit
counts per journal (JPP and PPA were not run on OpenAlex: HTTP 429 on every call; Crossref covered them):

| # | Source | Query | BEQ | JBE | P&T | EIT | JPP | PPA |
|---|---|---|---|---|---|---|---|---|
| 1 | Crossref | history lessons technology ethics | 20 | 20 | 20 | 20 | 3 | 1 |
| 2 | Crossref | historical precedent corporate power | 20 | 20 | 11 | 9 | 4 | 4 |
| 3 | Crossref | genealogy present practice critique | 10 | 20 | 9 | 9 | 1 | 0 |
| 4 | Crossref | printing press literacy analogy | 20 | 18 | 6 | 3 | 0 | 1 |
| 5 | Crossref | nineteenth century regulation lessons artificial intelligence | 7 | 20 | 20 | 20 | 0 | 0 |
| 6 | Crossref | domination republican freedom technology | 4 | 20 | 20 | 20 | 5 | 6 |
| 7 | Crossref | surveillance workers history power | 4 | 20 | 13 | 14 | 5 | 5 |
| 8 | Crossref | algorithm accountability duties design | 3 | 20 | 20 | 20 | 1 | 4 |
| 9 | Crossref | corporate power history East India Company | 20 | 20 | 12 | 10 | 4 | 4 |
| 10 | Crossref | past institutions precedent AI governance | 9 | 20 | 20 | 20 | 0 | 2 |
| 11 | Crossref | platform history telegraph railroad | 4 | 11 | 5 | 3 | 1 | 0 |
| 12 | Crossref | artificial intelligence objections duties firms | 11 | 20 | 20 | 20 | 0 | 3 |
| 13 | Crossref | historical analogy automation labor | 1 | 20 | 13 | 3 | 2 | 0 |
| 14 | Crossref | guilds professions licensing history ethics | 20 | 20 | 20 | 20 | 3 | 1 |
| 15 | Crossref | data colonialism history | 5 | 20 | 20 | 20 | 2 | 2 |
| 16 | Crossref | right to explanation | 2 | 20 | 14 | 7 | 4 | 0 |
| 17 | Crossref | privacy history | 3 | 15 | 19 | 20 | 3 | 0 |
| 18 | Crossref | contracts terms of service consent duty to read | 6 | 20 | 7 | 3 | 3 | 6 |
| 19 | Crossref | Gutenberg artificial intelligence | 3 | 8 | 8 | 8 | – | – |
| 20 | Crossref | scribes manuscript medieval technology | 2 | 8 | 8 | 8 | – | – |
| 21 | Crossref | telegraph electricity automobile analogy artificial intelligence | 3 | 8 | 8 | 8 | – | – |
| 22 | Crossref | industrial revolution lessons artificial intelligence | 4 | 8 | 8 | 8 | – | – |
| 23 | Crossref | bioethics history lessons AI ethics | 8 | 8 | 8 | 8 | – | – |
| 24 | Crossref | medieval guild analogy platform | 2 | 8 | 5 | 2 | – | – |
| 25 | Crossref | company state colonial charter technology firm | 8 | 8 | 8 | 8 | – | – |
| 26 | Crossref | Socrates writing Phaedrus technology | 2 | 8 | 8 | 8 | – | – |
| 27 | Crossref | Luddite | 0 | 0 | 0 | 0 | – | – |
| 28 | Crossref | what history teaches artificial intelligence | 7 | 8 | 8 | 8 | – | – |
| 29 | OpenAlex | history lessons technology | 24 | 120 | 97 | 50 | 429 | 429 |
| 30 | OpenAlex | historical precedent | 5 | 21 | 18 | 11 | 429 | 429 |
| 31 | OpenAlex | genealogy | 16 | 47 | 40 | 14 | 429 | 429 |
| 32 | OpenAlex | printing press | 1 | 23 | 21 | 7 | 429 | 429 |
| 33 | OpenAlex | literacy | 6 | 82 | 64 | 35 | 429 | 429 |
| 34 | OpenAlex | nineteenth century regulation | 7 | 41 | 24 | 4 | 429 | 429 |
| 35 | OpenAlex | domination republican | 7 | 5 | 15 | 4 | 429 | 429 |
| 36 | OpenAlex | analogy past technology | 8 | 33 | 71 | 29 | 429 | 429 |
| 37 | OpenAlex | telegraph railroad lessons | 0 | 0 | 0 | 0 | 429 | 429 |
| 38 | OpenAlex | East India Company | 3 | 74 | 6 | 6 | 429 | 429 |
| 39 | OpenAlex | precedent governance artificial intelligence | 0 | 4 | 14 | 9 | 429 | 429 |
| 40 | OpenAlex | surveillance history workplace | 7 | 38 | 25 | 13 | 429 | 429 |
| 41 | OpenAlex | algorithmic management duties | 6 | 65 | 65 | 37 | 429 | 429 |
| 42 | OpenAlex | right to explanation | 56 | 432 | 216 | 113 | 429 | 429 |
| 43 | OpenAlex | terms of service consent reading | 11 | 160 | 79 | 21 | 429 | 429 |
| 44 | OpenAlex | Luddites automation history | 2 | 1 | 2 | 429 | 429 | 429 |
| 45 | Crossref | BEQ complete listing 2018–2026, `journals/1052-150X/works`, cursor, 500 rows | 364 records; 183 non-review titles screened by hand | | | | | |

Record lookups (`api.crossref.org/works/<doi>`, `api.openalex.org/works/doi:<doi>`, OpenAlex `locations`,
Europe PMC `search?query=DOI:` ): 34 DOIs, listed in `scratchpad/r7/crossref_log.txt` (103 lines). Crossref
`query.bibliographic` on PPA for "Lazar Governing the Algorithmic City" (5 hits; 10.1111/papa.12279 first) and
on JPP for "Vredenburgh right to explanation" (5 hits; 10.1111/jopp.12262 first). Raw hit files:
`scratchpad/r7/cr_hits.json` (764 records), `oa_hits.json` (672), `beq_all.json` (364).

**Blocks (no circumvention attempted).** Springer PDF links served a JavaScript challenge page
(`/_fs-ch-…`) for Taylor 2021, Casiraghi 2023, Custers 2023, Hoeksema 2023, Schwerzmann 2021, Cordasco &
Véliz 2026; the Springer HTML article page redirected to `idp.springer.com/authorize?response_type=cookie`.
Wiley `pdfdirect` served a Cloudflare "Just a moment" page for Lazar 2025 and Goodrich 2025. PhilPapers
archive served the same for Grigoriev 2021. Repository routes recovered Taylor (OSF accepted version),
Hoeksema (Europe PMC full-text XML, PMC10007650), Custers (Leiden repository, publisher's version) and Lazar
(arXiv 2410.20720, preprint). VUB (Casiraghi) returned HTTP 503 twice; St Andrews (Mansell) 503 twice; CBS
(Schade) 403. Cambridge Core PDFs for BEQ downloaded without a challenge.

## 3. The candidates

Fit score: one point per criterion met, half for partly met, out of 8. Scores are my judgement from the
texts I opened; Casiraghi is scored from its abstract only.

### C1. Diamantis (2025), "The Danger of Contextual Integrity", *BEQ* — score 6.5

- **Reference.** Diamantis, M. E. (2025). The danger of contextual integrity. *Business Ethics Quarterly*,
  published online 27 October 2025, pp. 1–21. https://doi.org/10.1017/beq.2025.10085. Crossref: title,
  venue and date match; licence CC BY 4.0.
- **Words.** 11,514 **measured** on the corpus text (footnotes included; legal-style notes are heavy). Body
  without notes about 7,000 (earlier measurement, `scratchpad/beq/NOTES.md`).
- **Skeleton.** Epigraph ("Trojan Horse", NIST definition) → opening without heading (CI's dominance by
  counts; prior critics; "from theory to practice"; legal-realist method; scope: internal critique, no
  alternative; roadmap) → 1. Defining Contextual Integrity → 2. A Legal Realist Framework → 3. Contextual
  Integrity Would Erode Privacy: 3.1 What If the Decisionmakers Aren't Neutral? · 3.2 Errors Due to Value
  Indeterminacy · 3.3 Errors Due to Context Indeterminacy · 3.4 Indeterminacy and Complexity Favor the
  Powerful Litigants · 3.5 Heads Google Wins, Tails You Lose · 3.6 A Frog in Hot Water · 3.7 A One-Way
  Ratchet · 3.8 Persistent Particularism → 4. Conclusion.
- **Historical record:** no. **Concessions:** yes, spread through the body (CI's good prescriptions
  conceded, p. 7; the exercise "stacks the legal realist deck in favor of contextual integrity", p. 8; "For
  all I have said, contextual integrity may still be the best theory available", p. 19). **Objections:**
  answered inside the mechanism sections (§3.1, §3.8), no separate section. **Duties:** no; three
  "refinements" offered to CI's architects in §4.
- **Access.** Open access, CC BY, Cambridge Core. Local copy: `scratchpad/beq/pdfs/diamantis2025.pdf` and the
  corpus `.txt`.
- **Representative paragraph** (§3.5, p. 15; footnote markers 90–91 dropped):

  > But public libraries are governed by a far richer set of informational norms. Coincidentally, I recently
  > took my son to get a library card, a necessary first step to accessing our local library's services. As
  > part of the registration process, I had to hand over my driver's license. If I gave the clerk a false ID,
  > I would have committed a felony. In the terminology of contextual integrity, before research information
  > flows from libraries to patrons (i.e. they check out books), transmission norms require identification
  > information to flow from patrons to libraries. Patrons who acquire library books without providing
  > truthful information about themselves violate contextual integrity.

- **Fit.** The best prose in the set for our purpose: short declarative sentences carrying a concrete case,
  the opponent's own example turned against it, concessions placed where they cost the argument most, and a
  first person that marks the author's moves ("I recently took my son") and never the claim. The structure
  of §3 (one mechanism per subsection, each showing the harm running to the stronger party, with one worked
  case) is the shape our §3 ("the insider post read through the record") needs. **Main misfit:** no
  historical record and no duties; its target is a scholarly theory, not a firm's design; its notes are
  legal-citation style, which BEQ permits but our paper will not use.

### C2. Kim & Routledge (2022), "Why a Right to an Explanation of Algorithmic Decision-Making Should Exist", *BEQ* — score 6.5

- **Reference.** Kim, T. W., & Routledge, B. R. (2022). Why a right to an explanation of algorithmic
  decision-making should exist: A trust-based approach. *Business Ethics Quarterly*, 32(1), 75–102.
  https://doi.org/10.1017/beq.2021.3. Crossref: match (issued 2021, print 2022). OpenAlex: hybrid OA; 89
  citations.
- **Words.** 14,943 **measured** on the Cambridge PDF (28 pp.; Chicago-style footnotes, no reference list,
  so notes and running heads are inside the count). Body without notes estimated 10,500 (**estimate**).
- **Skeleton.** Opening without heading (algorithms in business; GDPR; the legal debate assumes a right it
  never justifies; "we search for a philosophical foundation") → 1. What Is an Algorithm? → 2. The Legal
  Debate and the Contours of a Right to Explanation → 3. Defending the Right to Explanation: 3.1 Informed
  Consent · 3.2 Limitations of the Autonomy-Based Account · 3.3 An Alternative: A Trust-Based Account ·
  3.4 Trust and a Right to a Remedial Explanation · 3.5 Trust and a Right to an Updating Explanation →
  4. What Can Be Explained: 4.1 Ex Ante · 4.2 Ex Post · 4.3 Who Can Be a Right-Holder? → 5. Addressing
  Objections: 5.1 Ignorant Dependency · 5.2 Is the Use of Algorithms Unique? · 5.3 Analogy or Dis-analogy? ·
  5.4 The Reality Check → 6. Conclusion.
- **Historical record:** no; medical informed consent and shareholder fiduciary duty serve as analogical
  precedents, and §5.3 tests the analogy for disanalogies (our Bartha move). **Concessions:** yes, inside
  §5. **Objections:** a dedicated section with four named objections. **Duties:** yes, a right whose
  correlative duties fall on data-processing firms (remedial and updating explanations).
- **Access.** Cambridge Core, downloaded without login (OpenAlex "hybrid"). Local copy:
  `…/R7/kim2022right/kim2022right.pdf`.
- **Representative paragraph** (§5.3, p. 99; footnote marker 81 dropped):

  > The medical context is, of course, an analogy; it is not the same as the algorithmic context. For
  > instance, the public service ethos that is pervasive in the medical field is absent in the sectors of
  > the economy in which most data-capturing companies operate. Yet, a growing number of such companies—and
  > other relevant industry stakeholders—are actively deliberating the creation of algorithmic codes of
  > ethics. Historically, the modern medical field did not have such a public ethics infrastructure at its
  > onset—but one was developed as the field grew and matured over many decades.

- **Fit.** The closest BEQ match on structure: present AI practice → normative foundation → what the right
  demands in practice → a named objections section that includes an analogy/disanalogy test → duties on
  firms. **Main misfit:** the historical dimension is a one-paragraph aside, not evidence; the prose is
  workmanlike rather than distinguished (long sentences that stack qualifications; the opening leans on a
  legal debate rather than on a dominant actor's own words).

### C3. Bhargava & Velasquez (2021), "Ethics of the Attention Economy", *BEQ* — score 6

- **Reference.** Bhargava, V. R., & Velasquez, M. (2021). Ethics of the attention economy: The problem of
  social media addiction. *Business Ethics Quarterly*, 31(3), 321–359. https://doi.org/10.1017/beq.2020.32.
  Crossref: match. OpenAlex: hybrid OA; 291 citations; cited in a federal court filing (*NetChoice v.
  Griffin*) and in drafts of California SB 976 (GWU news page, via WebSearch; not independently verified).
- **Words.** 20,292 **measured** total; 13,872 body before the reference list (footnotes included).
- **Skeleton.** Opening without heading (the attention-economy business model; misuse vs design; the gap;
  roadmap) → 1. On the Nature of Internet Addiction → 2. The Impermissibility of Making Social Media
  Addictive: 2.1 The Harm Argument · 2.2 The Adding Insult to Injury Argument · 2.3 The Exploitation
  Argument · 2.4 Summary → 3. A Business That Incentivizes Wrongdoing → 4. Implications for Theory and
  Practice → Conclusion.
- **Historical record:** no (one mention; older attention businesses named in passing). **Concessions:**
  yes ("the benefits of social media are not negligible"; 18 "objection" passages inline). **Objections:**
  met inline, no section. **Duties:** implications for managers and policy in §4, not a duty list.
- **Access.** Cambridge Core, downloaded without login. Local copy: `…/R7/bhargava2021attention/`.
- **Representative paragraph** (§2.3, p. 336):

  > But not all acts of taking advantage of another's weakness or vulnerability for one's own ends are
  > morally objectionable—that is, not all acts of exploitation are morally objectionable. For example, it
  > is not wrong in basketball to exploit a defender's lapse in attention to pass the ball to a teammate for
  > an easy layup, nor is it objectionable for an attorney to exploit a weakness in the opposition's argument
  > (Wood, 1995: 152). So, what makes an act of exploitation morally objectionable? For an act of
  > exploitation to be a wrongful kind, it must involve disrespect toward the object of exploitation (Arnold,
  > 2010; Wood, 1995).

- **Fit.** The most widely read BEQ essay in the set on a present corporate *design* practice; three named
  arguments, each a subsection; a section on the business model that makes the wrong profitable (our
  "custody" theme); plain sentences. **Main misfit:** 13,900 body words (over the 12,000 limit even before
  BEQ's footnote rule), no history, no objections section, implications rather than duties.

### C4. Kingston & Carnovale (2026), "Social Upgrading in Global Supply Chains", *BEQ* — score 6.5

- **Reference.** Kingston, E., & Carnovale, M. (2026). Social upgrading in global supply chains: Reframing
  corporate responsibilities. *Business Ethics Quarterly*, published online 14 January 2026, pp. 1–28.
  https://doi.org/10.1017/beq.2025.10103. Crossref: match; licence CC BY-NC-ND 4.0.
- **Words.** 12,109 **measured** on the corpus text (footnotes included, references stripped).
- **Skeleton.** Opening without heading (sweatshops; two assumptions; three groups of theorists; roadmap) →
  1. Oversimplification in Philosophical Work on Sweatshops: 1.1 The Vertical Integration Assumption
  (1.1.1 Nonworseness objection · 1.1.2 "Typically false") · 1.2 The Control Assumption (1.2.1 Against it ·
  1.2.2 Kates's "making with" argument) → 2. Big Buyers' Responsibilities under Constrained Influence:
  2.1 Multiple Sources (2.1.1 individual · 2.1.2 collective) · 2.2 Concrete Content (2.2.1 Requirements ·
  2.2.2 Principles in Action: The International/Bangladesh Accord · 2.2.3 Could There Ever Be an
  International Accord on Wages?) → 3. Implications and Conclusion.
- **Historical record:** no; empirical supply-chain structure (Table 1 from 10-K filings) does the
  evidentiary work, and the Accord is a working precedent. **Concessions:** yes. **Objections:** yes,
  from market advocates in §2.2.3 and §3. **Duties:** yes, concrete, with Table 2 (feature → why it
  constrains → available response) and a real regime that already embodies them.
- **Access.** Open access, CC BY-NC-ND, Cambridge Core. Local copy: `scratchpad/beq/pdfs/kingston2026.pdf`.
- **Representative paragraph** (§2.2.2, p. 19):

  > The principles of collective action among buyers ceding power via legally binding commitments to
  > materially support collectives of workers, factories, and unions in social upgrading might sound overly
  > ideal. However, there is at least one supply chain governance regime that contains all of these elements,
  > if in imperfect form. It is the International Accord (nee the Bangladesh Accord) for Health and Safety
  > in the Textile and Garment Industry. This agreement between factories, workers, and big buyers contains
  > the elements that help big buyers fulfill their responsibilities for social upgrading, despite their
  > individual constrained influence.

- **Fit.** The model for our §5: duties stated, then shown to exist "if in imperfect form" in a named
  regime, with the objection ("overly ideal") voiced and answered in the same breath. **Main misfit:** the
  target is a scholarly assumption rather than a firm's design; no history; the prose is serviceable, with
  long nominal subjects.

### C5. Moysidou & Fotaki (2024), "The Ethicality of Welfare Crowdfunding", *BEQ* — score 6

- **Reference.** Moysidou, K., & Fotaki, M. (2025). The ethicality of welfare crowdfunding in the context of
  the neoliberal welfare state: A Rawlsian perspective. *Business Ethics Quarterly*, 35(2), 216–247.
  https://doi.org/10.1017/beq.2024.15. Crossref: match (issued 5 November 2024); licence CC BY 4.0.
- **Words.** 12,243 **measured** on the corpus text.
- **Skeleton.** Opening without heading (neoliberal retrenchment; platforms praised; GoFundMe's dominance;
  Rawls; three arguments previewed; roadmap) → 1. Reliance on Crowdfunding for Social Welfare (history of
  welfare provision) → 2. The Scope of Our Ethical Analysis → 3. Rawls's Just Society and the Role of
  Private Actors → 4. An Ethical Critique of Welfare Crowdfunding: 4.1 The "Unjust Distribution" Argument ·
  4.2 The "Weakening Social Welfare" Argument · 4.3 The "Neoliberalization of the State" Argument ·
  4.4 Summary → 5. Implications for Theory and Practice → Conclusion.
- **Historical record:** partly. §1 is a history of welfare provision used as background, and §4.2 reads
  GoFundMe's narratives as a return to Victorian philanthropy's "deserving poor"; the history warns rather
  than judges. **Concessions:** yes ("prima facie justification"; not advocating prohibition).
  **Objections:** weak, no section. **Duties:** regulatory and platform obligations in §5.
- **Access.** Open access, CC BY, Cambridge Core. Local copy: `scratchpad/beq/pdfs/moysidou2024.pdf`.
- **Representative paragraph** (§4.2, pp. 229–230; footnote marker 3 dropped):

  > However, despite GoFundMe's ostensible aim to address the symptoms of systemic failure in the US welfare
  > system rather than substitute for it, we show that the platform may be equally problematic owing to its
  > narratives and modi operandi. Specifically, GoFundMe deploys narratives presenting itself as the best
  > solution to welfare provision, potentially distracting public attention from systemic flaws. In media
  > interviews, some GoFundMe executives have disavowed any intention of substituting for the welfare safety
  > net; yet they concurrently claim that GoFundMe aspires to become "the most helpful place in the world
  > for people and organizations" (Cadogan 2022), "the first and only choice that people think about when
  > they think about social fundraising" (Ainsley Harris 2018), and the singular "giving layer of the
  > internet" (Solomon 2019).

- **Fit.** The only BEQ essay in the set that pairs a dominant firm's own executives' words with a historical
  echo and ends in obligations; the move of quoting the company against itself is the one our §3 makes with
  Nadella's post. **Main misfit:** the history is background, not evidence; objections are thin; the prose
  hedges ("may", "potentially") and runs long framework sections.

### C6. Taylor (2021), "Public Actors Without Public Values", *Philosophy & Technology* — score 6

- **Reference.** Taylor, L. (2021). Public actors without public values: Legitimacy, domination and the
  regulation of the technology sector. *Philosophy & Technology*, 34(4), 897–922.
  https://doi.org/10.1007/s13347-020-00441-4. Crossref: match; licence CC BY 4.0. OpenAlex: 100 citations.
- **Words.** 13,911 **measured** total and 12,275 before the reference list, on the OSF accepted version
  (36 pp. typescript). Published version not opened (Springer challenge page).
- **Skeleton.** 1. Introduction: The problem with data governance → 2. What is missing from the current
  regulatory perspective on data? 2.1 the public–private overlap · 2.2 Defining what is public technology ·
  2.3 Updating corporate legitimacy → 3. Interrogating legitimacy as a route to non-domination: 3.1
  Thickening the concept of corporate legitimacy → 4. Corporate authority and public consent: 4.1 The
  (technologically mediated) sphere of public reason · 4.2 Case example: humanitarian data → 5. Five
  criteria (scale; articulated purpose; accountability for effects; contracts transparent to and contestable
  by the public; time-limited involvement): 5.1 Targeting accountability → 6. A framework for legitimacy →
  7. Conclusions.
- **Historical record:** no (zero occurrences of "histor" in the body). **Concessions:** some.
  **Objections:** three passages, no section. **Duties:** yes, five criteria posed as questions to the
  firm, then a framework.
- **Access.** CC BY at SpringerLink (a Bentley user opens it there directly); accepted version at
  https://osf.io/gtw2x (public domain per OpenAlex); published version in PMC7816553. Local copy:
  `…/R7/taylor2021public/` (OSF accepted version).
- **Representative paragraph** (accepted version p. 10, §3; published pagination differs):

  > Although data protection is usually cited as the key to controlling the power of technology firms, its
  > underlying premise – the rational, informed, liberal subject – is vulnerable with respect to the new
  > paradigm of big data and AI. In this new paradigm what happens to data after the individual (often
  > unconsciously) generates it is largely opaque and takes place mainly within corporate architectures. The
  > terms-of-service information people receive about data's lifecycle usually refer to 'research' and
  > 'third parties' as if this constituted meaningful information based on which people could exercise
  > rights over their data. Everyday life in the data economy, however, demonstrates that this kind of
  > control and knowledge are an illusion.

- **Fit.** Republican non-domination (Lovett's three marks) applied to technology firms that people cannot
  opt out of, ending in criteria a firm must meet toward the people it acts on: the normative frame of our
  A7 and the "second party" of our CA. **Main misfit:** no history, no objections section, and the voice is
  a policy framework's, not a single argument's; a journal below BEQ in the brief's order.

### C7. Lazar (2025), "Governing the Algorithmic City", *Philosophy & Public Affairs* — score 5.5

- **Reference.** Lazar, S. (2025). Governing the algorithmic city. *Philosophy & Public Affairs*, 53(2),
  102–168. https://doi.org/10.1111/papa.12279. Crossref: match (issued 27 January 2025); licence CC
  BY-NC-ND 4.0. OpenAlex: 22 citations. Based on the 2023 Stanford Tanner Lectures.
- **Words.** 26,535 **measured** total and 23,969 before the reference list, on the arXiv preprint
  (2410.20720, 52 pp.); the Wiley version was not opened (Cloudflare challenge). The journal version is
  67 pages.
- **Skeleton.** 1. Introduction → 2. The Algorithmic City → 3. The Nature and Justification of Algorithmic
  Power: 3.1 Dimensions · 3.2 Analysing Algorithmic Power · 3.3 Eliminate or Justify Algorithmic
  Intermediary Power? · 3.4 Justifying Algorithmic Governance → 4. Authority, Coercion, and Pre-emption →
  5. Procedural Legitimacy and Algorithmic Governance → 6. Justificatory Neutrality → 7. Objections: 7.1
  Review · 7.2 Stakes · 7.3 Ease of Exit · 7.4 Governance of Algorithms? → 8. Recap.
- **Historical record:** no (Dewey on steam and electricity frames the opening; six passing uses).
  **Concessions:** yes. **Objections:** a dedicated section with four named objections. **Duties:**
  principles (substantive justification, procedural legitimacy, proper authority), not a duty list.
- **Access.** CC BY-NC-ND at Wiley (a Bentley user opens it through the library's Wiley subscription or the
  open licence); preprint at https://arxiv.org/abs/2410.20720. Local copy: `…/R7/lazar2025governing/`
  (preprint).
- **Representative paragraph** (preprint §3.3):

  > Both approaches are missing an important further step: the step where we reflect on and argue for the
  > guiding principles that should shape power relations in the Algorithmic City. This is not the anaemic
  > process of agreeing on 'AI Ethics Principles', but rather is about determining what we care about, so
  > our moral diagnoses have depth and our regulatory or technical interventions have purpose. This is
  > political philosophy's task (whether undertaken by those trained as philosophers or not).

- **Fit.** The strongest prose in the set outside BEQ: claim-first paragraphs, a named objections section,
  intermediaries that "govern" the people they act on (our A4). **Main misfit:** twice the permitted length,
  a lecture's scope rather than one argument, no historical record, and PPA's register is further from BEQ's
  than any other candidate's.

### C8. Casiraghi (2023), "Anything new under the sun?", *Ethics and Information Technology* — score 4.5 (abstract only)

- **Reference.** Casiraghi, S. (2023). Anything new under the sun? Insights from a history of
  institutionalized AI ethics. *Ethics and Information Technology*, 25(2), art. 28.
  https://doi.org/10.1007/s10676-023-09702-0. Crossref: match (issued 24 April 2023); licence CC BY 4.0.
  OpenAlex: 17 citations.
- **Words.** Not measured; **estimate** 8,000–10,000 from the journal's article length. **Abstract only.**
- **Skeleton.** Not available. From the abstract: a history of bioethics, technology assessment, ELSA
  research and RRI as successive "ethification" episodes, read for what they show about present challenges
  to AI ethics "related to methodological issues, mobilization of expertise and public participation".
- **Historical record:** yes, a documented institutional history used to judge a present practice: the one
  article in the target journals that does this. **Concessions / objections / duties:** unknown; the
  abstract's STS framing ("a need for governments to gain more control") suggests a descriptive-critical
  essay with "insights", not duties.
- **Access.** CC BY at SpringerLink; the publisher PDF and HTML both served challenge pages to this agent,
  the VUB repository copy returned 503 twice, and Europe PMC does not hold it. A Bentley user opens it at
  the DOI.
- **Representative sentence** (abstract, Crossref record; no paragraph from the body could be opened):

  > The focus is on how a brief history of the institutionalization of these approaches can provide
  > insights into present challenges to the ethics of AI related to methodological issues, mobilization of
  > expertise and public participation.

- **Fit.** The only in-journal exemplar of criterion 2. **Main misfit:** unverified structure and prose;
  by its abstract it describes rather than condemns, and it names no duties; EIT is the fourth journal in
  the brief's order.

### Screened and set aside

| Item | DOI | Why not a candidate |
|---|---|---|
| Luchs 2026, *ICS* | 10.1080/1369118x.2026.2740039 | Earlier structural model; 6,591 body words (N5 measurement); not a target journal; no objections, no duties. Still the only read-in-full exemplar of criterion 2. |
| Steinberg 2020, *BEQ* 30(1) 97–117 | 10.1017/beq.2019.19 | 10,752 body **measured**; one objection subsection; no history; no duties. Clean prose; a fallback prose model. |
| Frye 2020, *BEQ* 30(2) 229–249 | 10.1017/beq.2019.30 | 9,621 body **measured**; objection-dense (40 mentions), ends with a permissibility test; no history; defends the practice. |
| Claassen & Gerbrandy 2018, *BEQ* 28(4) 401–425 | 10.1017/beq.2018.2 | 12,672 body **measured**; "Two Practical Objections"; delegated-governance duties; competition-law history is four passing mentions. |
| Ruehle 2023, *BEQ* 33(3) 502–531 | 10.1017/beq.2023.4 | 12,447 body **measured**; republican "arbitrary domination"; framework, not argument; no history. |
| Bhargava & Young 2021, *BEQ* 32(4) 519–545 | 10.1017/beq.2021.40 | 12,371 body **measured**; no objections section; no history. |
| Bhargava & Assadi 2023, *BEQ* 34(2) 201–230 | 10.1017/beq.2022.41 | 12,174 body **measured**; "Clarifications and Objections" section; no history; defends a practice. |
| Schade 2023, *BEQ* 33(3) 473–501 | 10.1017/beq.2022.30 | Judges GDPR transparency through "organized immaturity"; green copy at CBS returned 403; abstract only. |
| Mansell 2024, *BEQ* 35(2) 187–215 | 10.1017/beq.2024.17 | Hobbes's text as theory, not a record; St Andrews copy 503. |
| Hoeksema 2023, *P&T* 36(1) art. 17 | 10.1007/s13347-023-00618-7 | 8,595 body **measured** (Europe PMC XML); radical republicanism; no objections section; no history. Already carded (N5). |
| Custers 2023, *EIT* 25(4) art. 58 | 10.1007/s10676-023-09737-3 | 9,594 **measured** (Leiden copy); analogy with evolutionary biology; no objections; three passing historical mentions. |
| Vredenburgh 2022, *JPP* 30(2) 209–229 | 10.1111/jopp.12262 | 9,361 body **measured** (LSE eprint); tight analytic argument for a right; no history; JPP register. |
| Goodrich 2025, *PPA* 53(3) 254–270 | 10.1111/papa.12288 | Neo-Brandeisian antitrust (a tradition, not a record); 17 pp.; Wiley challenge page; abstract only. |
| Sturino 2025, *PPA* 53(3) 229–242 | 10.1111/papa.12284 | Digital media vs physical media; short; abstract only. |
| Grigoriev 2021, *JPP* 29(1) 94–116 | 10.1111/jopp.12225 | On judging past actors by Hume's general point of view: bears on our A3 method, not on structure; PhilPapers copy blocked. |
| Aßländer 2019, *JBE* 170(2) 313–328 | 10.1007/s10551-019-04293-7 | "Lessons from the 19th century sweatshop discussion"; closed access, no repository copy; title-level only. |
| Phillips, Schrempf-Stirling & Stutz 2019, *JBE* 166(2) 203–213 | 10.1007/s10551-019-04319-0 | How history bears on CSR judgement (method, 11 pp.); bronze OA; not a structural model. |
| Sharon & Gellert 2024, *ICS*; Kugelberg & Kugelberg 2026, *JBE* | see `scratchpad/journals/NOTES.md` | Read in the earlier round; grafts (risk × instrument cross-test; steelman before objections), not whole-essay models. |

## 4. Ranked top three

1. **Diamantis (2025), *BEQ*, 10.1017/beq.2025.10085** — 11,514 words measured with footnotes (body about
   7,000); open access, CC BY, Cambridge Core. The model for sentence-level prose and for the
   mechanism-by-mechanism middle with a worked case and distributed concessions. Main misfit: no historical
   record, no duties; the history and the duties must come from elsewhere (Luchs for the genealogy's shape,
   Kingston & Carnovale for duties with a precedent).
2. **Kim & Routledge (2022), *BEQ* 32(1), 10.1017/beq.2021.3** — 14,943 words measured with footnotes
   (body about 10,500, estimate); Cambridge Core, downloadable without login. The model for the whole-essay
   skeleton: present AI practice → foundation → what it demands → a named objections section with an
   analogy/disanalogy test → duties on firms. Main misfit: history appears only as a one-paragraph aside,
   and the prose is less sharp than Diamantis's.
3. **Kingston & Carnovale (2026), *BEQ*, 10.1017/beq.2025.10103** — 12,109 words measured; open access,
   CC BY-NC-ND. The model for the closing section: duties, then a working precedent that embodies them "if
   in imperfect form", with the "overly ideal" objection answered on the spot. Main misfit: its target is a
   scholarly assumption and its evidence is empirical, not historical.

Bhargava & Velasquez (2021) is the alternate if the author weights criterion 8 (reach and plain prose) over
length. Casiraghi (2023) is the one in-journal essay that does what criterion 2 asks; the author can open it
at the DOI and decide whether it displaces Luchs as the model for the historical sections.

## 5. Gaps and blocks

- **Casiraghi 2023 (EIT).** CC BY; SpringerLink PDF and HTML served challenge pages; VUB repository 503
  (twice). A Bentley user: open https://doi.org/10.1007/s10676-023-09702-0 directly (open licence), or
  through the library's SpringerLink subscription.
- **Lazar 2025 and Goodrich 2025 (PPA).** Wiley `pdfdirect` served Cloudflare challenges. Lazar's preprint
  (arXiv 2410.20720) was used; Goodrich has no repository copy. A Bentley user: the CC BY-NC-ND copy at the
  DOI in a browser, or Wiley Online Library through the library's subscription if it covers PPA (not
  checked).
- **Schade 2023 and Mansell 2024 (BEQ).** Repository copies failed (CBS 403; St Andrews 503). Cambridge Core
  through the library; Mansell is CC BY at the DOI.
- **Aßländer 2019 (JBE).** Closed; no repository copy. SpringerLink through the library.
- **Grigoriev 2021 (JPP).** PhilPapers archive blocked; Wiley through the library.
- **Published pagination for Taylor 2021.** Only the OSF accepted version was opened; quote located by
  typescript page. Published pages 897–922, Springer, CC BY.
- **Word counts.** Counts are `pdftotext` word counts of whole files (or of text before the reference list)
  and include footnotes and running heads; a BEQ-style count (body plus footnotes, no references) would run
  5–10 per cent lower. Only Luchs has a body-only count (N5, 6,591).
- **Consensus and Scholar Gateway** were unavailable this run (quota; access denied), so the semantic-search
  layer is missing. Crossref, OpenAlex (four journals), the complete BEQ listing and four web searches stand
  in for it.
