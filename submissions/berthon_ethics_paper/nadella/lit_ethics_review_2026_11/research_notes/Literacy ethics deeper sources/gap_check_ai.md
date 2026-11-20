# Gap check: has anyone mapped literacy's historical distribution errors onto AI ethics, AI literacy or algorithmic systems?

Thesis checked: literacy's spread involved design-ethics errors (gates, withheld competence, one-sided records, custody
of the medium, oversold promise, capture by intermediaries, stigma); the AI-ethics movement's remedies (disclosure,
explanation, human oversight, AI literacy) repeat them; Nadella's "trust architecture" is the case.

Search run 19 Nov 2026 by a research subagent. Local copies are in
`~/iit-playground/berthon_ethics_local/lit_ethics_review/deep/<key>/`, with sha256 values given below.
Status labels: **read in full**, **partial**, **abstract only**, **not accessible (HTTP code)**.
"Lib." means the existing library card was read in place of the source.

## 1. What do Nichols, Thrall, Quiros and Dixon-Román (2024) argue, and can the full text be reached?

### Takeaway
The full text was **not accessible** by any route I tried, so whether the article draws historical-literacy parallels is
still **unverified**. The abstract and one citing paper both point to a different argument. Its subject is
"speculation" and platform logic in literacy education, not literacy's historical distribution errors. The record lists
**four** authors, not three.

### Cited Findings
- Record: Nichols, T. P., Thrall, A., Quiros, J., & Dixon-Román, E. J. (2024). Speculative capture: Literacy after
  platformization. *Reading Research Quarterly*, 59(2), 211–218. doi 10.1002/rrq.535. Published 2024-04-01; 30 cites
  (OpenAlex), 22 (Semantic Scholar). OpenAlex and Semantic Scholar both list **Ezekiel J. Dixon-Román** as fourth
  author, and so does the reference list of Kalantzis & Cope's preprint. REVIEW.md cites only three authors and
  should be corrected. — [OpenAlex](https://api.openalex.org/works/doi:10.1002/rrq.535);
  [Semantic Scholar](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rrq.535)
- Semantic Scholar marks it as HYBRID open access under a **CC BY-NC** licence. OpenAlex gives `oa_status: hybrid` and
  `any_repository_has_fulltext: False`, so a browser on an ordinary connection should be able to download it from
  Wiley. — same sources.
- The abstract (**abstract only**) defines the two senses of speculation: literacy education as "a speculative project
  – one characterized by the cultivation of particular reading and writing practices in order to prefigure different
  imagined social futures"; and the speculative logic of AI platforms, "characterized by extrapolative prediction and
  algorithmic reasoning". The authors argue "the former has allowed literacy education to be uniquely susceptible to
  the influence of the latter" and name the relation "speculative capture". — [Semantic Scholar record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rrq.535)
- Kalantzis & Cope cite the article only for "platformization". They ask educators to watch "the processes of
  'platformization' (Nichols et al. 2024)" (EdArXiv preprint, p. 28). This is indirect evidence of its focus, not a
  reading of it. — [EdArXiv preprint](https://osf.io/es5kb/download)
- Access attempts, all on 19 Nov 2026:
  - Wiley `pdfdirect`, `full` and `ila.onlinelibrary` `pdfdirect?download=true`, with a browser user agent: each
    **HTTP 403**.
  - WebFetch of `/doi/full/`: **HTTP 403**.
  - Wayback Machine availability API for the four Wiley URL forms: no snapshots.
  - Consensus `get_full_text`: "blocked: not open access … or no open-access copy held".
  - CORE API v3 search by DOI: returned a Cloudflare redirect page, not JSON.
  - Semantic Scholar `openAccessPdf`: points to the same Wiley URL.
  - Web search for title, authors and "pdf": no author or repository copy found.
  - Not tried: Unpaywall (it requires an email parameter, which the brief excluded), Google Scholar and ResearchGate.

### Inferences
- From the abstract, "capture" means literacy education being remade in the platform's predictive image, not a firm
  taking custody of a medium or an intermediary capturing readers. Even if the full text has a historical section, it
  is unlikely to set gates, records or stigma against disclosure or oversight remedies. This is an inference from the
  abstract and one citing paper only.

### Gaps
- The full text is unread. Because the article is CC BY-NC, a manual browser download (or one through a library) should
  work. Check the full text for (a) any section on literacy's history (Graff, Brandt, colonial or schooled literacy),
  and (b) any treatment of AI-ethics remedies or named firms.

## 2. Which works draw historical-literacy parallels for AI, algorithms or platforms, and how close does each come to the thesis?

### Takeaway
I found no work that sets literacy's historical distribution errors against the AI-ethics movement's remedies
(disclosure, explanation, human oversight, AI literacy) one error at a time, or that uses Microsoft or Nadella as the
case. Sources: Consensus, OpenAlex, Semantic Scholar, Crossref, CORE and one web search, 19 Nov 2026 (log below).
The field divides into two halves that do not meet:
- **History side.** Kalantzis & Cope (2024) give the strongest historical account of literacy as domination
  (exclusion, Latin and priestly intermediaries, the "ideology of opportunity", normal-curve labelling, gender and
  colonial vectors). They then call generative AI a privatisation of the "general intellect". Their remedy is a
  commons, open-source models and their own platform. They do not criticise disclosure, explanation or oversight.
- **Remedy side.** Oleart & Flores Moleon (2026), Lund & Teel (2026), Paljor et al. (2026) and Srivastava (2026)
  argue that AI literacy and disclosure-style remedies shift responsibility onto individuals or stop short of repair.
  None of them grounds the argument in literacy's history.

Kalantzis & Cope deserve more weight than REVIEW.md gives them. REVIEW.md lists them as "abs." for one clause, but
their preprint covers four or five of the thesis's error categories on the historical side.

### Cited Findings

**A. Kalantzis, M., & Cope, B. (2024). Literacy in the time of artificial intelligence. *Reading Research Quarterly*.
doi 10.1002/rrq.591.**
- Status: **partial.** I read the EdArXiv submitted version (doi 10.35542/osf.io/es5kb), 43 pp. I read pp. 1–9 in full
  and searched the rest. The Wiley version of record returned **HTTP 403** and Consensus returned "blocked".
  Preprint sha256 `e9730a73…0d9e`; local `deep/kalantzis2024literacy/preprint.pdf`.
- Pagination follows the preprint, so every quotation must be checked against the RRQ version of record before use.
  — [EdArXiv](https://osf.io/es5kb/download); [OpenAlex locations](https://api.openalex.org/works/doi:10.1002/rrq.591)
- What it claims:
  - "literacy and its means of production have been as menacing in social practice as often as they have been
    liberatory" (p. 2).
  - "In its first centuries, the printing press served two functions, as an instrument of power and to draw illiteracy
    as a line of exclusion" (p. 4).
  - "Gutenberg's Bible was in Latin, requiring the chants of priests … to serve as interlocutors between mystically
    inaccessible ruling text and popular belief" (p. 4).
  - "literacy also became a vector of gender inequality … and colonialism" (p. 4, citing Street 1995).
  - Quoting Graff (1987: 261), schooled literacy formed a "controllable, docile, respectful workforce, willing and
    able to follow orders" (p. 4).
  - "Now that literacy had become mass, it had to regulate inequality in new ways. It did this through the ideology of
    opportunity" (p. 4). The normal curve then spreads children so "only a few can be labeled" (p. 4).
  - On AI: LLMs "have privatized collective human intelligence in new ways" (p. 6). "Artificial Intelligence is a new
    colonialism, not of material space like the old colonizers, but the colonization of social intelligence by these
    insurgent moguls of human meaning" (p. 9).
  - Remedy: "We need to reappropriate the general intellect for the general public" (p. 9), through the commons and
    open-source LLMs. The later sections present their own GenAI writing application and "cyber-social literacy
    learning".
- Overlap with the thesis:
  - **Gates**: yes ("line of exclusion").
  - **Custody of the medium and intermediaries**: yes (Latin, priests as "interlocutors"; mass-media owners of "the
    means of production of meaning", p. 6).
  - **Oversold promise**: yes ("ideology of opportunity").
  - **Stigma**: partial (labelling by the normal curve).
  - **Withheld competence**: implicit in gender and colonial access only.
  - **One-sided records**: partial (first writing as "inventories of ownership", p. 3).
- Where it stops:
  - It does not take up disclosure, explanation, human oversight or AI literacy as remedies that repeat these errors.
  - It names no firm's governance framework (OpenAI is named only as the model their app uses).
  - The parallel between history and AI rests on privatisation and colonisation of the medium, not on how remedies are
    designed.

**B. Kamperman, S., & Graff, H. J. (2026). On "AI literacy". *Change* 58(4), 34–39. doi 10.1080/00091383.2026.2706429.**
- Status: **lib. (read in full per card).**
- What it claims: technological literacy campaigns "repeat many of the conceptual errors of 19th- and early
  20th-century print literacy campaigns, reiterating two harmful myths" (p. 36). AI literacy lets companies and states
  "recruit consumers at an early age" (p. 36).
- Overlap: **oversold promise** (Myth #2). Corporate capture appears only as an adjacent point.
- Where it stops: per the card, its own remedy includes "Establish norms for disclosure" (p. 37). It is an instance of
  the remedy, not a critic of it. — card `literature/cards/berthon_ethics_course/kamperman2026ai.md`

**C. Lund, B. D., & Teel, Z. A. (2026). AI literacy: An exercise in power-knowledge. *Proceedings of the AAAI/ACM
Conference on AI, Ethics, and Society*, 1745–1752. doi 10.1609/aies.v9i3.43263.**
- Status: **lib. (read pp. 1–7 of the arXiv version).**
- **Card update needed.** The card records "doi: null; journal venue not confirmed". Crossref now shows AIES 2026
  proceedings, issued 2026-10-11, pp. 1745–1752. — [Crossref](https://api.crossref.org/works/10.1609/aies.v9i3.43263)
- What it claims: frameworks "enforce a 'consumer' orientation" (abstract). "unequal access to AI tools in society
  recapitulates longstanding epistemic injustices" (abstract). Its history of literacy is one sentence citing Houston
  1983 (card).
- Overlap: **AI literacy as responsibilization or consumer training**, and **withheld competence** in a general sense.
- Where it stops: no historical mapping, no treatment of disclosure or oversight, no firm case. Its remedy
  (Participatory Governance) stays on the learner's side. — card `literature/cards/run_2026_11/lund2026powerknowledge.md`

**D. Oleart, Á., & Flores Moleon, A. (2026). Why the EU's technosolutionist focus on AI and media 'literacy' empowers
Big Tech. *Social Sciences* 15(7), 430. doi 10.3390/socsci15070430.**
- Status: **read in full** through Consensus `get_full_text` (56,000 characters, two parts). The MDPI PDF returned
  **HTTP 403** to curl. The Consensus text has no page numbers, so the locators below are section headings.
  — [Consensus record](https://consensus.app/papers/details/w:bdae46e4-9111-4ccb-8929-8409d46c5661/?utm_source=claude_desktop)
- What it claims:
  - Literacy functions "as a technology of governance that redistributes political responsibility from
    infrastructures and corporate actors towards individuals" (Introduction).
  - Under the 2022 Code of Practice, "the companies that are creating the problem in the first place are supposed to
    also be part of the solution by contributing to design 'tools to improve media literacy'" (§4, media literacy).
  - "Citizens are expected to recognise AI-generated content, interpret labels, understand algorithmic influences, and
    critically evaluate information flows, yet without corresponding interventions in extractive business models"
    (same section).
  - AI literacy serves "not only an educational function but also one of Big Tech legitimisation" (§ "The
    Normalisation of AI Through 'AI Literacy'").
  - The 2025 Digital Omnibus proposal would remove providers' and deployers' AI-literacy obligation and shift it to
    the Commission and member states (same section).
- Its historical parallels are not about literacy. Tech owners "can be seen as contemporary versions of old media
  oligarchs such as William Randolph Hearst" (Discussion), and the Luddites were "struggles over the distribution of
  power and benefits" (Conclusions).
- Overlap:
  - **Capture by intermediaries**: strong (companies designing the literacy tools).
  - **Literacy remedy and labels as responsibilization**: strong.
  - **Custody of the medium**: yes, through ownership of infrastructures.
- Where it stops:
  - No history of literacy's distribution: no Graff, no gates, records or stigma.
  - The case is EU policy, not a firm. Microsoft appears only in a list of Big Tech companies (Introduction).

**E. Paljor, Y., Proctor, C. P., et al. (2026). Preparing for compliance or critical participation? RESPECT 2026. doi
10.1145/3796496.3811753.**
- Status: **abstract only** (as in REVIEW.md).
- What it claims: treating ethics as an add-on "risks displacing responsibility for AI harms away from institutions and
  educational structures onto individual learners".
- Where it stops: no historical-literacy parallel in the abstract.
  — [Consensus record](https://consensus.app/papers/details/w:35ca1529-ae76-476e-af09-c4ec425bc18e/?utm_source=claude_desktop)

**F. Srivastava, S. (2026). *Responsible AI and Structural Justice*. Cambridge Elements (AI Ethics and Society). doi
10.1017/9781009680882. Crossref issued 2026-11-12.**
- Status: **partial** (open access). I read the abstract and pp. 13, 48–49, 53–54 and 57, and searched the whole text.
  sha256 `22d1af59…c71f`; local `deep/srivastava2026responsible/paper.pdf`.
  — [CUP PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/582EA5CDF27A65824C2F578503D30127/9781009680868AR.pdf/responsible-ai-and-structural-justice.pdf)
- What it claims:
  - "many Responsible AI initiatives remain thin by demanding disclosures without systemic repair" (abstract).
  - "There is a difference between public disclosure and disclosure for publics" (p. 13).
  - "Most current initiatives remain thin: They demand disclosure without repair" (p. 57).
  - Its remedy endorses data literacy (citing Wong 2023) as part of "thick" responsibility (pp. 53–54).
- Overlap: it critiques **disclosure as a remedy**, and it has the Microsoft material discussed under Q3.
- Where it stops: no historical-literacy parallel. It treats literacy as a remedy, not as a precedent of harm.

**G. Nama, R. (2026). Agentic literacy debt. *AI and Ethics*. doi 10.1007/s43681-026-01152-w.**
- Status: **read in full** (arXiv 2605.27396, 8 pp.). sha256 `744825d4…c785`; local `deep/nama2026agentic/`.
  — [arXiv](https://arxiv.org/pdf/2605.27396)
- What it claims:
  - The debt "is incurred by the organizations that deploy agents but paid by the users, patients, and citizens on
    whose behalf the agents act" (p. 1).
  - "design defaults are literacy interventions whether or not they are intended as such" (p. 7).
  - "The default for irreversible actions is to execute first and report after" (p. 7).
  - It cites the EchoLeak vulnerability in Microsoft 365 Copilot as an example (p. 2).
  - Its precedent is Ladson-Billings's "education debt" (p. 3), not literacy history.
- Overlap: it locates costs with the deployer and sees design defaults (authorization flow, invisible logs) as
  withheld capacity. This is close to **withheld competence** and **one-sided records**, in agent terms.
- Where it stops: no historical-literacy parallel. Its remedy is "transparency-by-design" and literacy (p. 7), so it
  is an instance of the remedy family.

**H. Rodríguez López, H., Cobarrubias Soto, N., Martínez Santos, Y. F., & Delsordo Jassan, E. L. (2025). De la
lectoescritura a la inteligencia artificial. *Revista Digital de Tecnologías Informáticas y Sistemas* 9(1). doi
10.61530/redtis.vol9.n1.2025.254.**
- Status: **partial** (I searched it and read the introduction, the Freire/Street section and the conclusions).
  sha256 `2e34ab6f…b857bd87`; local `deep/rodriguez2025lectoescritura/`.
- What it claims: the history it gives is celebratory. "Desde que la imprenta facilitó el acceso al conocimiento, la
  lectoescritura se consolidó como la llave maestra para la ciudadanía" (pp. 52–53, journal pagination inferred from
  page footers). Its remedy is XAI: the move "de la Caja Negra … a la Caja Blanca (transparencia y explicabilidad)"
  (p. 58).
- Overlap: **none**. It runs opposite to the thesis by endorsing explanation as the remedy.

**I. Trainor, J. (2026). AI is manna for writing studies or, how to stay calm in troubled times [review essay].
*Literacy in Composition Studies* 12(2). doi 10.21623/1.12.2.5. Crossref issued 2026-04-28.**
- Status: **partial** (pp. 58–65 read). sha256 `0458b6b7…c25c1`; local `deep/trainor2026manna/`.
- What it claims:
  - It reports work that asks "how technology sponsors (not just disrupts) literacy" (p. 61).
  - It credits Antonio Byrd with "extending Brandt's framework of literacy sponsorship to the age of AI" (p. 63).
  - It judges that Byrd "is less focused on systemic critique than on systemic navigation" (p. 62).
- Overlap: it points to Brandt's **sponsors** being carried into AI, which bears on capture by intermediaries.
- Where it stops: Byrd's own work (a 2023 *Composition Studies* article cited by Trainor) was **not read**. On
  Trainor's account it is about navigation, not a critique of remedies.

**J. Cheema, A. (2026). Software colonialism: Adobe as the new English in Global South art education. *Race & Class*.
doi 10.1177/03063968261422606.**
- Status: **abstract only.**
- What it claims: three mechanisms "paralleling historical colonial structures", including "gatekeeping access
  (replacing colonial English-language requirements with software requirements that function identically)". It says
  the framework "extends to artificial intelligence".
- Overlap: a **gate** and **custody** parallel from colonial language policy to a software firm.
- Where it stops: the parallel is from language, not literacy's distribution. The firm is Adobe. There is no treatment
  of AI-ethics remedies in the abstract.
  — [Consensus record](https://consensus.app/papers/details/w:200bc933-c5ec-431b-bd8d-24291ad92e3d/?utm_source=claude_desktop)

**K. Migge, B., & Schneider, B. (2025). The material making of language as practice of global domination and control:
continuations from European colonialism to AI. *AI & Society*. doi 10.1007/s00146-025-02389-5.**
- Status: **abstract only.**
- What it claims: "striking continuities" between colonial language materialisation and AI language technologies.
- Overlap: colonial continuity into AI, but about language standardisation, not literacy's distribution or remedies.
  — [Consensus record](https://consensus.app/papers/details/w:d80ed5ea-f900-4600-a710-83a4232feb7d/?utm_source=claude_desktop)

**L. Pangrazio, L. (2026). The (im)possibility of AI literacy. *Learning, Media and Technology*. doi
10.1080/17439884.2026.2615553. Published 2026-01-02; 22 cites (OpenAlex).**
- Status: **not accessible**:
  - The T&F PDF returned **HTTP 403**.
  - Consensus full text: blocked.
  - Semantic Scholar has no abstract.
  - The OpenAlex abstract is truncated after "The hype surrounding the potential of AI to augment human capabilities
    and supercharge productivity is matched by fears that it will irrevocably change life and the world as we know it.
    On the one ...".
- I cannot say what it argues. OpenAlex lists it as OA at T&F, so a browser download should work.
  — [OpenAlex](https://api.openalex.org/works/doi:10.1080/17439884.2026.2615553)

**M. Vee, A. (2013). Understanding computer programming as a literacy. *LiCS* 1(2). doi 10.21623/1.1.2.4.**
- Status: **lib.**
- What it claims (per card): in medieval England, "those who could not read text began to be recast as 'illiterate'
  and power began to shift towards those who could" (p. 51). With code, "the power balance is once again shifting
  toward those who are skilled" (pp. 54–55).
- Overlap: **gates and stigma**, applied to programming.
- Where it stops: it is about programming, not living with algorithms or AI-ethics remedies, and its remedy is wider
  access to programming. Vee's 2017 book *Coding Literacy* was **not checked**: the OpenAlex author query failed.
  — card `berthon_ethics_course/vee2013understanding.md`

**N. Burrell, J. (2016). How the machine 'thinks'. *Big Data & Society*. doi 10.1177/2053951715622512.**
- Status: **lib.**
- What it claims: it names "technical illiteracy, remediable by education" as one of three kinds of opacity. It argues
  that end-user explanations give "at best incomplete and at worst false reassurance".
- Overlap: it critiques **explanation** as a remedy.
- Where it stops: no historical-literacy parallel. — card `algorithmacy_design_ethics/burrell2016.md`

**O. Other hits checked and set aside** (abstracts only; no historical-literacy parallel):
- Mekheimer & Tohamy 2026, doi 10.1007/s44217-026-01695-4: AI literacy as "fractured cultural capital" that reproduces
  inequality in Egyptian schools. Bourdieu, not history.
- Shapiro, Souto-Otero & Watermeyer 2026, doi 10.1080/17439884.2026.2652638.
- Rapanta et al. 2025, doi 10.1007/s42438-025-00573-w.
- Monett & Grigorescu 2024, doi 10.34190/ecel.23.1.2759.
- Sundström Sjödin & Rahm 2025, doi 10.1007/s42438-025-00540-5. It surfaced on "literacy myth" + AI, but its abstract
  is about reading imaginaries in library events.

### Inferences
- The novelty claim must narrow. "AI repeats literacy's history of domination" is already on the table:
  - Kalantzis & Cope 2024: exclusion, priestly intermediaries, the ideology of opportunity, colonialism and
    privatisation, in a highly cited RRQ paper (213 cites).
  - Kamperman & Graff 2026: the myth.
  - Vee 2013: the gate shifting power to the skilled.
- So is "AI literacy and disclosure shift responsibility onto individuals":
  - Oleart & Flores Moleon 2026, Paljor et al. 2026, Lund & Teel 2026 and Srivastava 2026.
  - Burrell 2016 on explanation.
- What I did not find is the join between the two:
  - the error-by-error claim that the remedy family itself (disclosure, explanation, human oversight, AI literacy)
    repeats the historical distribution errors;
  - a firm's governance architecture (Microsoft or Nadella) as the case.
- One error category had no counterpart in anything I found: **one-sided records** (the institution keeps the record
  and the person does not). Nama's "default action log is invisible to the user" (p. 7) is the nearest, and it has no
  history.

### Gaps
- Full text unread for Nichols et al. 2024 (HTTP 403) and Pangrazio 2026 (HTTP 403). The Kalantzis & Cope version of
  record was also unread (HTTP 403); I used the preprint.
- Not read: Byrd 2023 (*Composition Studies*), Vee 2017 *Coding Literacy*, and Cheema 2026 beyond its abstract.
- Not searched directly:
  - the ACM DL (CHI, FAccT, AIES tables of contents) and arXiv full-text search;
  - business-ethics journals by name (*Journal of Business Ethics*, *Business Ethics Quarterly*);
  - Google Scholar, Unpaywall (needs an email) and Scholar Gateway (ACCESS_DENIED).
  
  The HCI and business-ethics facets therefore rest only on Consensus and OpenAlex relevance ranking.

#### Search log (19 Nov 2026; repeatable)
- **Consensus `search`** (no filters):
  1. "history of literacy as precedent for AI literacy and algorithmic accountability: literacy myth, gatekeeping,
     sponsors of literacy" (page_size 40)
  2. "AI literacy responsibilization critique shifts responsibility from companies to users" (30)
  3. "critique of Microsoft responsible AI governance, Copilot agents, Satya Nadella trust framing" (20)
  4. "AI literacy compared to colonial literacy campaigns, literacy tests, or print monopoly: historical analogy for
     algorithmic power" (20)
- **Consensus `get_full_text`**: DOIs 10.1002/rrq.535, 10.1002/rrq.591 and 10.1080/17439884.2026.2615553 were all
  blocked. Oleart & Flores Moleon came through by Consensus id.
- **OpenAlex** `api.openalex.org/works?search=…`, top 12 each, user agent `research-fetch/1.0`:
  - `"literacy myth" algorithm` (84 hits)
  - `"literacy myth" "artificial intelligence"` (46)
  - `"sponsors of literacy" "artificial intelligence"` (62)
  - `history of literacy lessons for AI ethics` (23,415; relevance-ranked, nothing on point in top 12)
  - `Microsoft "responsible AI" critique ethics washing` (229)
  - `Nadella Microsoft artificial intelligence discourse` (206)
  - DOI lookups for every work above.
- **Semantic Scholar** Graph API DOI lookups: rrq.535, Pangrazio, Trainor, Sjödin & Rahm, Srivastava, de Laat, Luther.
- **Crossref**: 10.1609/aies.v9i3.43263, 10.21623/1.12.2.5 and 10.1017/9781009680882.
- **CORE** API v3: `q=doi:"10.1002/rrq.535"` and `"speculative capture" literacy` both returned a Cloudflare redirect
  page.
- **Wayback** availability API: four Wiley URL forms for rrq.535; no snapshots.
- **WebSearch** (standard): `"Speculative capture" Nichols Thrall Quiros Dixon-Román pdf`. No relevant hit.

## 3. Has anyone critiqued Nadella's or Microsoft's responsible-AI or agent-governance framing in scholarship?

### Takeaway
Yes, but only in part. Srivastava (2026) analyses Microsoft's 2023 Azure human-rights impact assessment as an "inert
platform" defence. That is a scholarly critique of how Microsoft frames its responsibility. I found no scholarly
critique of Nadella's own "trust" framing or of Microsoft's agent-governance architecture, and none that links
Microsoft to literacy history. Sources: Consensus query 3 and two OpenAlex queries, 19 Nov 2026.

### Cited Findings
- Srivastava (2026), **partial**:
  - It reports the Foley Hoag HRIA's finding that "in no instances did the Assessors find evidence that Microsoft
    causes human rights harms" (p. 48, quoting Foley Hoag 2023: 1).
  - The assessors "validated Microsoft's claim that its 'services are merely "inert" platforms'" (p. 48).
  - Srivastava concludes that "Microsoft ducked behind the inert platform defense, long used by Uber, Airbnb, Facebook,
    and the like" (p. 49).
  - It argues that if developers "claim credit" for beneficial downstream uses, they share structural responsibility
    for harmful ones (pp. 49–50).
  
  — [CUP PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/582EA5CDF27A65824C2F578503D30127/9781009680868AR.pdf/responsible-ai-and-structural-justice.pdf)
- de Laat (2021), *Philosophy & Technology*, doi 10.1007/s13347-021-00474-3, **abstract only**. The Springer PDF came
  back as HTML. It reviews 24 companies' responsible-AI commitments and concludes "some three of the largest" made
  real implementation steps, so "charges of mere 'ethics washing' do not apply". The abstract does not name the three;
  whether Microsoft is among them is unverified. Its stance is more defence than critique.
  — [Semantic Scholar](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s13347-021-00474-3)
- Jang & Plaisance (2025), *Journal of Media Ethics*, doi 10.1080/23736992.2025.2580662, **abstract only**. A textual
  comparison of AI principles from OpenAI, Google, Microsoft and Anthropic, using Vallor's technomoral virtues. It is
  descriptive, with no literacy parallel.
  — [Consensus record](https://consensus.app/papers/details/w:61e3a0f8-c61c-48e0-bf77-e684a847c381/?utm_source=claude_desktop)
- Nama (2026), **read in full**, uses the EchoLeak vulnerability in Microsoft 365 Copilot as an example of users being
  unable to "anticipate, monitor, or contest" agent behaviour (p. 2). It is an illustration, not a critique of
  Microsoft's framing. — [arXiv](https://arxiv.org/pdf/2605.27396)
- Other Microsoft-related hits, **abstract only**:
  - Furmakiewicz et al. 2024 (arXiv 2407.09512), by Microsoft authors, describing Microsoft's four-stage
    responsible-AI lifecycle.
  - Bano et al. 2025 (arXiv 2503.17661), a user study of M365 Copilot.
  - Feng 2025 (doi 10.70267/icbms.2501063.5132), a laudatory case study of Nadella's leadership.
  
  None of them is a critique.

### Inferences
- The Microsoft case is open ground for the paper. The nearest scholarly treatment (Srivastava) critiques the
  inert-platform responsibility defence, not the trust, disclosure and human-oversight architecture. It also treats
  literacy as a remedy, not as a historical precedent.

### Gaps
- I did not search law-review or business-ethics venues by name, or ACM DL (FAccT, CHI, AIES) tables of contents, for
  "Microsoft" or "Copilot". Microsoft-specific critiques could sit there.
- I did not read the Foley Hoag (2023) HRIA itself. Srivastava's quotations of it are second-hand here.
- I did not search Nadella's "trust" vocabulary (e.g. "trust architecture", "trustworthy AI" + Nadella) in
  full-text-capable databases. Only OpenAlex title and abstract search and Consensus were used.

#### Corrections for other files (not made; flagged for the main session)
- REVIEW.md, Gap check and bibliography: Nichols et al. 2024 has four authors (adds Dixon-Román, E. J.).
- REVIEW.md: Kalantzis & Cope 2024 can be upgraded from "abs." to "partial (EdArXiv preprint)". Its historical
  argument reaches gates, intermediaries, oversold opportunity and stigma, so the "nearest works" list understates it.
- Card `lund2026powerknowledge.md`: the venue is now AIES 2026, pp. 1745–1752, doi 10.1609/aies.v9i3.43263 (Crossref,
  issued 2026-10-11).
