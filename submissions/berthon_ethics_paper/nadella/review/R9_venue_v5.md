# R9 — Venue assessment for the v5 paper (seventeen errors; Nadella as case)

**Agent-drafted, 2026-11-19; the author has not reviewed it.** Not committed (the brief said not to; the repo
CLAUDE.md asks for commit-and-push after each step, and the brief overrides it for this file).

## 1. Scope and method

The paper as `STRUCTURE.md` v5 describes it: a normative design-ethics essay, about 12,000–12,500 words, author-date,
historical evidence + republican non-domination + internal critique of one firm's architecture, ending in duties.
Business-school authors, one a marketing scholar. R7 §1–2 (model-essay search over BEQ, JBE, P&T, EIT, JPP, PPA) was
read and not redone; this run asks a different question (where to submit, by prestige and fit).

Sources used this session (all fetched 2026-11-19 unless a snapshot date is given):

- **FT50.** ft.com refused the fetch. The 2016-era list came from a secondary copy
  (mdahsanul.netlify.app, post dated 27 Apr 2026, citing the FT). The April 2026 revision came from
  Poets&Quants, "Deans decry journals' removal from influential Financial Times list", 8 May 2026
  (poetsandquants.com/2026/05/08/…): **Human Relations, Journal of Business Ethics and Organization Studies were
  removed**; Academy of Management Annals, American Sociological Review and Psychological Science were added. The
  FT's own current page was not read, so "on FT50" below means "on the 2016 list and not named among the 2026
  removals".
- **Chartered ABS AJG 2024.** The guide is behind a login (charteredabs.org/academic-journal-guide). **Every AJG
  2024 grade is unverified.** One conflict matters: Cambridge's BEQ metrics page shows "ABS (UK) Rating 4 (2021)",
  while Wikipedia's BEQ article says BEQ went from 4 to 3 in the November 2024 AJG (citing the AJG site). The author
  should check BEQ's AJG 2024 grade at his school's login before relying on it.
- **VHB Rating 2024** (German business-school association), read from the PDFs:
  `vhbonline.org/fileadmin/vhb/Services/vhb-rating/{ORG,MARK,WI}/VHB_Rating_2024_Area_rating_*.pdf`. Ratings are
  per area; the area is given.
- **Impact factors** only where a publisher page showed one today: Springer journal home pages ("Journal metrics",
  JIF labelled 2025); Cambridge BEQ metrics page (no year given); AOM AMR page ("© Clarivate 2026"). Sage and Wiley
  pages returned HTTP 403, so their JIFs are **unverified**.
- **OpenAlex** `sources` records (2yr_mean_citedness, h-index), fetched before OpenAlex's anonymous daily budget ran
  out mid-session. This is OpenAlex's own metric, not a JIF.
- **Aims and guidelines.** Cambridge (BEQ) and Springer (JBE, P&T, EIT, AI & Society, Minds and Machines) pages read
  directly; AMA pages for JM and JPP&M read directly; EGOS page for Organization Studies. Wiley (JMS, JPP, PPA) and
  Sage (BD&S, OS guidelines, Business & Society, JPP&M aims, JM aims, Macromarketing) pages blocked → read from
  **Wayback Machine snapshots**, snapshot date given in each entry; these may predate current versions.
- **Fit papers.** Crossref `journals/<ISSN>/works?query.bibliographic=…&filter=from-pub-date:2023-01-01` (OpenAlex
  was exhausted), then every DOI below checked against its Crossref `works/<doi>` record for title, journal and year
  (log: scratchpad `r9/verified.txt`). Titles only; **I read none of these papers**, so "close in topic" is judged from
  the title.

## 2. Journal-by-journal

### Business Ethics Quarterly (Cambridge; ISSN 1052-150X)

- **Prestige.** Not FT50. ABS 4 (2021) per Cambridge metrics page; AJG 2024 **unverified** (possible downgrade to 3,
  Wikipedia). VHB 2024 (ORG area): **B**. JIF 4.3, 5-yr 4.7 (Cambridge page, year not stated); "7th of 77 ethics
  journals". OpenAlex 2yr mean citedness 3.31, h 151.
- **Aims (about-this-journal page).** "publishes theoretical and empirical research relevant to the ethics of
  business, corporate social responsibility, and corporate sustainability … it publishes scholarship from the
  humanities, social sciences, and professional fields". Research-article types include "Historical … work that makes
  an original theoretical contribution."
- **Type and length (preparing-your-materials page).** Research article; "12,000 words (including the body of the text
  and the footnotes, but not including the abstract, tables, figures, or references)". AMJ style, Chicago author-date
  or Chicago notes; one only.
- **Fit evidence.** Schade 2023, "Dark Sides of Data Transparency: Organized Immaturity After GDPR?",
  10.1017/beq.2022.30. Robson 2026, "Price Personalization in the Age of AI: Complicating the Defense",
  10.1017/beq.2026.10112. Diamantis 2025, "The Danger of Contextual Integrity", 10.1017/beq.2025.10085 (R7's prose
  model). R7 found no BEQ article 2018–2026 that uses a historical record to judge a present technology.

### Journal of Business Ethics (Springer; 0167-4544)

- **Prestige.** **Removed from FT50 in April 2026** (Poets&Quants, 8 May 2026). VHB 2024: **A** (ORG area), B
  (MARK and WI areas). JIF 6.3, 5-yr 9.7 (2025; Springer home page). OpenAlex 2yr 9.55, h 446. AJG 2024 unverified.
- **Aims (aims-and-scope page).** "publishes only original articles from a wide variety of methodological and
  disciplinary perspectives concerning ethical issues related to business … Systems of production, consumption,
  marketing, advertising … are analysed from a moral viewpoint." "Speculative philosophy as well as reports of
  empirical research are welcomed."
- **Type and length (submission guidelines).** "Original paper: A conceptual paper, literature review or empirical
  paper which makes an original contribution". Average "approximately 8,000 - 10,000 words (including references).
  Articles should be no longer than 12,000 words." References count: the paper would need to lose roughly a quarter.
  APA.
- **Fit evidence.** Cordasco & Véliz 2026, "The Accuracy-Explainability Trade-off, the Right to Explanation, and the
  Implications for Organisations", 10.1007/s10551-026-06305-9. Kugelberg & Kugelberg 2026, "Practice-Dependent
  Governance of AI", 10.1007/s10551-026-06377-7. Dieveney 2026, "The New 'Parent' Corporation (Moral Responsibility
  for Sophisticated AI Systems)", 10.1007/s10551-026-06374-w.

### Philosophy & Technology (Springer; 2210-5433)

- **Prestige.** No JIF shown on the Springer home page today (**unverified**). OpenAlex 2yr 8.54, h 103. Not on
  business lists checked.
- **Aims.** "The journal aims to publish the best research produced in all areas where philosophy and technology
  meet. It welcomes high-quality submissions, regardless of the tradition, school of thought or disciplinary
  background from which they derive."
- **Type and length.** Research articles; I found no word limit on the submission-guidelines page (commentaries
  max 2,000, invited). APA.
- **Fit evidence.** Saura García 2024, "Datafeudalism: The Domination of Modern Societies by Big Tech Companies",
  10.1007/s13347-024-00777-1 (historical analogy + domination). Buijsman et al. 2025, "The Role of Digital Literacy in
  Maintaining Autonomy in AI Decision-Support: Balancing the Burdens", 10.1007/s13347-025-00963-9 (the literacy-burden
  question head-on). Bozdağ 2026, "AI as Political Infrastructure", 10.1007/s13347-026-01058-9.

### Ethics and Information Technology (Springer; 1388-1957)

- **Prestige.** JIF 5.5, 5-yr 5.9 (2025). OpenAlex 2yr 12.05, h 122.
- **Aims.** "dedicated to advancing the dialogue between moral philosophy and the field of information and
  communication technology … Research that deals with the history of ideas and provides intellectual resources for
  moral and political reflection on ICT is also welcomed."
- **Type and length.** Original Research Paper, "minimum length of approx. 5000 words and a maximum length of approx.
  8000 words of content" (title, abstract, references excluded). **Too short by ~4,000 words.**
- **Fit evidence.** Casiraghi 2023, "Anything new under the sun? Insights from a history of institutionalized AI
  ethics", 10.1007/s10676-023-09702-0. Herzog 2024, "Big data and the risk of misguided responsibilization",
  10.1007/s10676-024-09794-2 (cf. error 8). Buijsman 2024, "Transparency for AI systems: a value-based approach",
  10.1007/s10676-024-09770-w.

### Journal of Political Philosophy (Wiley; 0963-8016)

- **Prestige.** JIF unverified. OpenAlex 2yr 3.31, h 132.
- **Aims (Wayback, 17 Jul 2024).** "journal devoted to the study of theoretical issues arising out of moral, legal and
  political life. It welcomes … work cutting across a variety of disciplinary concerns, among them philosophy,
  sociology, history, economics and political [science]".
- **Length (Wayback, 17 Jul 2024).** "Manuscripts over 10,000 words will be considered only in exceptional
  circumstances … These counts include all text, footnotes, references". **Too long.**
- **Fit evidence.** Crossref returned no AI/technology article 2023–2026 for my queries. Nearest: Vredenburgh,
  "The Right to Explanation", 10.1111/jopp.12262 (Crossref issued 2021; outside the window).

### Philosophy & Public Affairs (Wiley; 0048-3915)

- **Prestige.** JIF unverified. OpenAlex 2yr 2.34, h 146. (Its standing among philosophers is not something I could
  verify this session.)
- **Aims (Wayback, 17 Jul 2024).** "welcomes philosophical discussion of substantive legal, social, and political
  problems … In addition, it aims to publish studies of the moral and intellectual history of such problems."
- **Length.** "generally prefer submissions that are no longer than 12,000 words"; Chicago footnotes with all
  bibliographic information in the notes (author-date would have to be converted).
- **Fit evidence.** Lazar 2025, "Governing the Algorithmic City", 10.1111/papa.12279. Goodrich 2025, "Seize the Means
  of Prediction! Data, Domination, and Antitrust", 10.1111/papa.12288.

### Academy of Management Review (AOM; 0363-7425)

- **Prestige.** FT50 (2016 list; not among 2026 removals). VHB 2024: **A+** (ORG). JIF 13.8, 5-yr 21.6 (AOM page,
  © Clarivate 2026). OpenAlex 2yr 11.53, h 608.
- **Aims (aom.org/research/journals/review).** "to publish theoretical insights that advance our understanding of
  management and organizations." "Submissions to AMR must extend theory in ways that develop testable
  knowledge-based claims." Humanities perspectives are named as possible grounding.
- **Type and length.** Not stated on the page read; **unverified**.
- **Fit evidence.** Grote et al. 2026, "Taming Artificial Intelligence: A Theory of Control-Accountability Alignment
  among AI Developers and Users", 10.5465/amr.2023.0117. Marquis & Qiao 2025, "History Matters for Organizations",
  10.5465/amr.2022.0238. **Misfit:** a normative essay that ends in duties does not "develop testable
  knowledge-based claims".

### Journal of Management Studies (Wiley; 0022-2380)

- **Prestige.** FT50 (2016 list; not among 2026 removals). VHB 2024: **A** (ORG). JIF unverified. OpenAlex 2yr 9.45,
  h 358.
- **Aims (Wayback, 30 Sep 2023).** "to publish original, innovative, and high-quality papers that advance conceptual
  and empirical knowledge, and address practice in the area of management and organization … in such fields as
  organization theory … and critical management studies."
- **Length (Wayback, 9 Dec 2023).** "9,000-12,000 words typically; anything exceeding 15,000 words may be returned";
  JMS Says essays 3,000 words; Point 9,000–12,000.
- **Fit evidence.** Wu 2026, "Algorithmic Status Inequality: An Integrative Perspective on AI-Driven Social
  Stratification", 10.1111/joms.70134. Lindebaum et al. 2023, "Big Data, Proxies, Algorithmic Decision-Making and the
  Future of Management Theory", 10.1111/joms.13032. No normative-ethics essay found.

### Organization Studies (Sage; 0170-8406)

- **Prestige.** **Removed from FT50 in April 2026.** VHB 2024: **A** (ORG). JIF unverified. OpenAlex 2yr 6.29, h 296.
- **Aims (EGOS page).** "promotes the understanding of organizations, organizing and the organized"; "welcomes
  innovative, high-quality research from all paradigms and disciplines".
- **Length (Wayback, 6 Jul 2025).** Research article max 13,000 words "including references and appendices";
  "X and Organization Studies" essays 7,500.
- **Fit evidence.** Brossard 2026, "Emancipatory Agency and Rebalancing of Power in Algorithmic Systems: A Simondonian
  perspective", 10.1177/01708406261459055. Little else on AI ethics 2023–2026 in my queries.

### Journal of Public Policy & Marketing (Sage/AMA; 0743-9156)

- **Prestige.** Not FT50. VHB 2024: **B** (MARK). JIF unverified. OpenAlex 2yr 5.87, h 140.
- **Aims.** AMA page: "a forum for understanding the nexus of marketing and public policy, with each issue featuring a
  wide-range of topics, including … ethics and social responsibility … security and privacy." Sage aims (Wayback,
  20 Jun 2022): suitable work includes "providing ethical foundations of appropriate marketing activity".
- **Type and length (AMA submission guidelines).** Research articles (empirical or conceptual) within "50 pages …
  inclusive of title, abstract, keywords, text, footnotes, references"; plus a required Policy Contribution Statement
  (≤300 words).
- **Fit evidence.** Donovan 2025, "A Short History of Misinformation-at-Scale and Efforts to Mitigate It",
  10.1177/07439156251384249. Zayer et al. 2026, "A Transformative Agenda for Digital Inclusion: Unpacking the
  Institutional Dynamics of Algorithmic Systems", 10.1177/07439156261437698. Mousavi & Villanova 2025, "Consumer
  Evaluations of Generative AI Disclosures …", 10.1177/07439156251367762 (disclosure as remedy).

### Journal of Marketing (Sage/AMA; 0022-2429)

- **Prestige.** FT50 (2016 list; not among 2026 removals). VHB 2024: **A+** (MARK). JIF unverified. OpenAlex 2yr
  15.39, h 534.
- **Aims (AMA page).** "develops and disseminates knowledge about real-world marketing questions useful to scholars,
  educators, managers, policy makers, consumers, and other societal stakeholders … the premier outlet for substantive
  marketing scholarship." The page carries the banner "Better Marketing for a Better World".
- **Type and length.** Same AMA 50-page rule as above.
- **Fit evidence.** Tully et al. 2025, "Lower Artificial Intelligence Literacy Predicts Greater AI Receptivity",
  10.1177/00222429251314491 (bears on the AI-literacy remedy, but empirical). Dion et al. 2024, "The Enrichment
  Economy: Market Dynamics, Brand Strategy, and Ethics", 10.1177/00222429241275014. **Misfit:** no normative
  philosophical essay found; the paper's object is not a marketing question.

### Big Data & Society (Sage, open access; 2053-9517)

- **Prestige.** VHB 2024: **B** (ORG). JIF unverified. OpenAlex 2yr 13.26, h 127.
- **Aims.** The Sage aims tab did not render in the Wayback snapshot; the guidelines (Wayback, 5 Jun 2025) say only
  that BD&S "is an open access, peer-reviewed journal". **Aims statement not read.**
- **Length (Wayback, 5 Jun 2025).** "original research articles of up to 10,000 words including all references".
  Open access (APC not checked).
- **Fit evidence.** Bareis 2024, "The trustification of AI. Disclosing the bridging pillars that tie trust and AI
  together", 10.1177/20539517241249430 (closest title to the "trust architecture" case). Högberg 2024, "Stabilizing
  translucencies: Governing AI transparency by standardization", 10.1177/20539517241234298. Mao et al. 2025,
  "Strategising imaginaries: How corporate actors … shape AI governance", 10.1177/20539517251400727.

### AI & Society (Springer; 0951-5666)

- **Prestige.** JIF 6.1, 5-yr 6.7 (2025). VHB 2024: **C** (WI). OpenAlex 2yr 9.54, h 125.
- **Aims.** "focuses on societal issues including the design, use, management, and policy of information,
  communications and new media technologies, with a particular emphasis on cultural, social, cognitive, economic,
  ethical, and philosophical implications".
- **Type and length.** "Normal word length: Research 10k, Open Forum 8k".
- **Fit evidence.** Foth 2026, "Hostile interaction design: AI, governance, and the quest for human oversight",
  10.1007/s00146-026-03065-y. Migge & Schneider 2025, "The material making of language as practice of global
  domination and control: continuations from European colonialism to AI", 10.1007/s00146-025-02389-5 (historical
  continuity argument). Nakagawa 2026, "Governing the AI-mediated corporation", 10.1007/s00146-026-03333-x.

### Minds and Machines (Springer; 0924-6495)

- **Prestige.** JIF 4.7, 5-yr 10.3 (2025). OpenAlex 2yr 11.37, h 97.
- **Aims.** "a philosophy journal … at the intersection between cognitive philosophy, logic, epistemology, ethics and
  computer and data science", including "the ethical and social implications of the design, development and use of
  digital [technologies]".
- **Type and length.** Original research articles; no word limit found.
- **Fit evidence.** Hine & Floridi 2023, "The Blueprint for an AI Bill of Rights: In Search of Enaction, at Risk of
  Inaction", 10.1007/s11023-023-09625-1. Narayanan & Tan 2023, "Attitudinal Tensions in the Joint Pursuit of
  Explainable and Trusted AI", 10.1007/s11023-023-09628-y. Leans epistemology/cognition; weak fit for a historical
  business-ethics essay.

### Other venues found

- **Business & Society** (Sage; 0007-6503). VHB 2024 **B** (ORG); OpenAlex 2yr 5.44. Aims (Wayback, 5 May 2021):
  "will consider a wide range of theoretical, empirical …, normative, and methodological submissions … all papers
  should in a substantial way address the societal role, impacts and intersections of and with business." Length
  (Wayback, 26 Jun 2025): "7000-12,000 words … including tables, figures and references". Fit: Mergen 2026, "The
  Algorithmic Leviathan or the Digital Agora? …", 10.1177/00076503261455110; Stadtler et al. 2026, "When the Ground
  Shifts: Why Artificial Intelligence Requires Both Policy and Debate", 10.1177/00076503261502876.
- **Journal of Macromarketing** (Sage; 0276-1467). VHB 2024 **C** (MARK); OpenAlex 2yr 3.74. Aims page not reached.
  Length (Wayback, 8 Jun 2025): "8,000 and 12,000 words (inclusive of references …)". Fit: Anupam et al. 2026,
  "Artificial Intelligence and Consumer Emancipation …", 10.1177/02761467261447432; Ferrell & Ferrell 2024, "Building
  a Better World: The Role of AI Ethics and Social Responsibility", 10.1177/02761467241285793.
- **Organization** (Sage; 1350-5084). VHB 2024 **B** (ORG). Aims and guidelines not reached. Fit: Zientara 2026,
  "Against acceptance as legitimacy: Ethics and algorithmic management", 10.1177/13505084261443023.

## 3. Table

| Journal | FT50 (after Apr 2026) | VHB 2024 | JIF (page, year) | OpenAlex 2yr / h | Aims fit | Length vs ~12k body | Fit papers 2023–26 | Overall |
|---|---|---|---|---|---|---|---|---|
| BEQ | no | B (ORG) | 4.3 (Cambridge, yr n/s) | 3.31 / 151 | strong: "Historical" type named | fits: 12k excl. refs | Schade 2023; Robson 2026; Diamantis 2025 | **1** |
| JBE | **removed 2026** | A (ORG) | 6.3 (2025) | 9.55 / 446 | strong | over: 12k **incl.** refs | Cordasco & Véliz 2026; Kugelberg 2026; Dieveney 2026 | **2** |
| Philosophy & Technology | no | – | not shown | 8.54 / 103 | strong | no limit found | Saura García 2024; Buijsman et al. 2025 | **3** |
| PPA | no | – | unverified | 2.34 / 146 | good ("moral and intellectual history") | ≤12k preferred; Chicago notes | Lazar 2025; Goodrich 2025 | stretch |
| JPP&M | no | B (MARK) | unverified | 5.87 / 140 | good ("ethical foundations of … marketing") | 50 pp. incl. refs | Donovan 2025; Zayer 2026 | marketing alt. |
| Business & Society | no | B (ORG) | unverified | 5.44 / 163 | good ("normative") | 12k incl. refs | Mergen 2026; Stadtler 2026 | alt. |
| Big Data & Society | no | B (ORG) | unverified | 13.26 / 127 | likely; aims not read | 10k incl. refs | Bareis 2024; Högberg 2024 | alt. (cut) |
| AI & Society | no | C (WI) | 6.1 (2025) | 9.54 / 125 | good | 10k research | Foth 2026; Migge & Schneider 2025 | safe alt. |
| JMS | yes | A (ORG) | unverified | 9.45 / 358 | weak (theory/practice of management) | 9–12k | Wu 2026; Lindebaum 2023 | low fit |
| Organization Studies | **removed 2026** | A (ORG) | unverified | 6.29 / 296 | weak | 13k incl. refs | Brossard 2026 | low fit |
| AMR | yes | A+ (ORG) | 13.8 (© Clarivate 2026) | 11.53 / 608 | misfit ("testable … claims") | unverified | Grote 2026; Marquis & Qiao 2025 | no |
| JM | yes | A+ (MARK) | unverified | 15.39 / 534 | misfit (marketing questions) | 50 pp. | Tully 2025 | no |
| EIT | no | – | 5.5 (2025) | 12.05 / 122 | strong | **8k max** | Casiraghi 2023; Herzog 2024 | only if halved |
| JPP | no | – | unverified | 3.31 / 132 | fair | **10k incl. all** | none found 2023–26 | no |
| Minds and Machines | no | – | 4.7 (2025) | 11.37 / 97 | weak | no limit found | Hine & Floridi 2023 | no |
| J. Macromarketing | no | C (MARK) | unverified | 3.74 / 105 | aims not read | 8–12k incl. refs | Anupam 2026; Ferrell & Ferrell 2024 | no |
| Organization | no | B (ORG) | unverified | – | not read | not read | Zientara 2026 | no |

AJG 2024 grades: all unverified (login). "–" = not on the VHB area lists I read.

## 4. Ranked recommendation

1. **Business Ethics Quarterly.** The only journal whose own guidelines name historical work as an article type, and
   whose limit (12,000 words of body and footnotes, references excluded) fits the paper after the §3 trim already
   planned. Chicago author-date is accepted as is. It has published normative essays on AI transparency and
   explanation (Schade 2023; Kim & Routledge 2022 per R7; Robson 2026). The prestige case needs the author's check:
   ABS 4 in 2021, a possible AJG 2024 downgrade to 3, VHB B.
2. **Journal of Business Ethics.** The strongest verified list standing of the fitting journals (VHB A in the
   organisation area, JIF 6.3) and an aims statement that names marketing and welcomes "speculative philosophy". Two
   costs: it left the FT50 in April 2026, and its 12,000-word ceiling includes references, so the paper must lose
   about a quarter of its length (the cut would fall on §3, which carries the seventeen errors).
3. **Philosophy & Technology.** The best philosophy-of-technology fit: it has published a historical-analogy
   domination argument about big tech (Saura García 2024) and a paper on literacy as a burden placed on the person
   (Buijsman et al. 2025), and I found no word cap. It ranks below the business-ethics journals on business-school
   lists (not on VHB areas read; no JIF shown).

*Stretch:* Philosophy & Public Affairs. Its aims invite "studies of the moral and intellectual history of such
problems" and it published Lazar 2025 and Goodrich 2025. However, it expects one tight analytical argument in Chicago
notes, not seventeen errors.
*Marketing-side alternative:* JPP&M (aims name ethics, privacy and "ethical foundations of appropriate marketing
activity"; Donovan 2025 is a history piece). This would need a Policy Contribution Statement and a marketing-policy
frame.

**FT50 venues.** The three remaining FT50 journals I checked (AMR, JMS, JM) do not fit a normative essay on present
evidence. AMR requires testable claims, JM publishes marketing questions, and in JMS I found no normative-ethics
essay. If an FT50 outlet is required, JMS is the least poor option, and the paper would have to be recast as a
management-theory contribution.

## 5. Gaps

- AJG 2024 grades (login); FT's own 2026 list page (ft.com refused fetch); Sage/Wiley impact factors (403).
- Aims pages not read: Big Data & Society, Journal of Macromarketing, Organization; AMR length limits.
- Wayback snapshots (2021–2025) may predate current guidelines for JMS, JPP, PPA, OS, B&S, BD&S, JPP&M, Macromarketing.
- Fit papers are judged by title from Crossref records; none was opened.
- OpenAlex anonymous budget exhausted mid-run; fit searches used Crossref only.
