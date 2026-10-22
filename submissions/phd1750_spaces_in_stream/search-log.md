# Search log — PHD1750 "Spaces in the Stream" literature review

Run 2026-10-20 by Claude for Roger Hunt. Scholar Gateway returned ACCESS_DENIED on first call; I substituted OpenAlex (api.openalex.org) and Crossref as second sources.

| # | Facet | Source | Query | Results / notes |
|---|---|---|---|---|
| 1 | 5 Streaming LLM UI | Consensus | eye tracking streaming text generation large language model chatbot interface | 20 shown; relevant: Park & Lee 2024; Bolliger et al. EMTeC; Resulbegoviq et al. 2026 systematic review |
| 2 | 1 Reading | Consensus | eye movements reading scrolling or moving text comprehension | 20 shown; relevant: Harvey et al. 2017, 2018; Haverkamp et al. 2022; Öquist & Goldstein 2007; Metzner et al. 2017; Rayner 1998 review; Akthar et al. 2021 |
| 3 | 4 Automation / LLM reliance | Consensus | overreliance on AI explanations automation bias large language model users verification | 20 shown; relevant: Kim et al. 2024, 2025; Vasconcelos et al. 2023; Si et al. 2023; Steyvers et al. 2025; Liu et al. 2026 CHI; Romeo & Conti 2025 |
| 4 | 5 | Scholar Gateway | streaming chatbot responses eye movements/trust | ACCESS_DENIED |
| 5 | 5 | OpenAlex | streaming text large language model user interface | 115,166 hits; top 15 off-target (surveys) |
| 6 | 5 | OpenAlex | word by word text generation chatbot reading | 17,452; off-target |
| 7 | 5 | OpenAlex | eye tracking ChatGPT response reading | 5,650; off-target |
| 8 | 1 | OpenAlex | incremental text presentation reading eye movements | 9,660; general reading models only |
| 9 | 2 Event segmentation | Consensus | event segmentation during reading narrative text boundaries memory | 20; relevant: Zacks et al. 2009; Speer et al. 2007; Pettijohn et al. 2016; Ezzyat & Davachi 2011; Kumar et al. 2023 |
| 10 | 2/4 Breakpoints | Consensus | interruptions at breakpoints in task structure event boundaries user interface | 20; relevant: Powers & Scerbo 2021 (Human Factors, EST + breakpoints); Bailey & Iqbal 2006; Iqbal & Bailey 2007; McFarlane 2002 |
| 11 | 3 Attention capture | Consensus | abrupt onset of new objects captures visual attention | 20; relevant: Yantis & Jonides 1984, 1990; Franconeri et al. 2005; Zhang et al. 2025 review |
| 12 | 5 gap | WebSearch (extended) | streaming LLM responses token by token user study reading comprehension trust CHI | Just-in-Time Tokens (CHI EA 2026); Streaming, Fast and Slow (UIST 2025?) — check |
| 13 | 4 | Consensus | cognitive forcing functions reduce overreliance on AI decision support | 20; Buçinca et al. 2021; de Jong et al. 2025; Li et al. 2026 CHI |
| 14 | 1 | Consensus | regressions in reading allow rereading function of backward eye movements | 20; Booth & Weger 2013; Inhoff et al. 2019; Metzner et al. 2017; Christianson et al. 2024 |
| 15 | 1 | Consensus | rapid serial visual presentation speed reading apps comprehension eye movements | 20; Benedetto et al. 2015; Acklin & Papesh 2017; Rubin & Turano 1992; Koornneef & Mulder 2019 |
| 16 | 3 | Consensus | sensorimotor contingencies account of vision and visual consciousness | 19; O'Regan & Noë 2001 |
| 17 | 4/5 | Consensus | human oversight monitoring of autonomous AI agents interface intervention | 20; Chen et al. 2026 (CUA oversight); Dhanorkar et al. 2026; Endsley 2017; Sterz et al. 2024 |
| 18 | 4 | Consensus | trust in automation calibration appropriate reliance review | 20; Lee & See 2004; Wischnewski et al. 2023 |
| 19 | 5 | OpenAlex | title_and_abstract: streaming AND (LLM OR "language model") AND (user OR reading OR readers) | 1,202; top-cited off-target |
| 20 | 2 | OpenAlex | title_and_abstract: "event segmentation" AND (interface OR display OR automation) | 45; Event perception in mobile interaction (2011) |
| 21 | 3 | OpenAlex | title: affordances AND (technology OR interface OR design) | 3,195; Norman 1999; Gaver 1991; Hartson 2003 |
| 22 | 4 | OpenAlex | title_and_abstract: "automation complacency" OR "automation bias" | 2,151; Goddard et al. 2012; Mosier & Skitka papers; Lyell & Coiera 2017 |
| 23 | 5 gap | WebSearch (extended) | eye tracking study streamed versus full LLM chatbot response presentation reading regressions | No direct comparison found; OASST-ETC dataset (eye-tracking on LLM responses, not streamed) |
| 24 | 5 gap | WebSearch (extended) | pausing or chunking LLM streaming output at checkpoints to support user verification HCI study | No user study found; only machine-side guardrail/attestation work |
| 25 | 5 gap | arXiv API | abs:streaming AND abs:LLM AND abs:reading AND abs:users | 8; only Streaming, Fast and Slow relevant |
| 26 | 4/5 | arXiv API | abs:"computer-use agents" AND abs:oversight | 8; Chen et al. 2026 Comparing Human Oversight Strategies |
| 27 | 5 | Consensus | chatbot typing indicator response delay dynamic message display user perception | 20; Bhat 2025 IUI (dynamic vs static display); Gnewuch et al. 2018, 2022 |
| 28 | 1 | Consensus | text signaling devices headings typographic cues effects on reading and memory | 20; Lorch 1989; Hyönä & Lorch 2004 (eye fixations, headings); Lorch et al. 1993, 1995 |
| 29 | 1/5 | Consensus | segmenting text into meaningful chunks line breaks phrase boundaries improves reading | 20; Tsoukala et al. 2025 (line breaks vs clause boundaries, eye tracking); Keenan 1984 (chunking slowed reading); Koornneef 2023; LeVasseur et al. 2006 |
| 30 | — | Unpaywall API | OA lookup for 26 candidate DOIs | see notes/; several publishers block scripted download → read in browser |
| 31 | — | Europe PMC REST | PMCID lookup for 10 DOIs | Cho & Lim PMC13513764; Resulbegoviq PMC13600100; Zacks 2009 PMC8710938; Zacks 2007 PMC2852534; Wolfe 2021 PMC8965574 |
| 32 | read | Browser (Chrome, get_page_text) | Cho & Lim 2026 PMC; Park & Lee 2024 aodr.org full text | read in full; publisher sites blocked scripted download |
| 33 | gap | WebSearch (extended) | "scriptura continua" AI generated text interface reading chatbot | No scholarly use of the analogy found; only Wikipedia entry and unrelated Bible apps |
| 34 | 4/5 gap | Consensus | eye tracking users supervising AI agent or LLM output verification errors detection | 20; Wu et al. 2025 RelEYEance; Cao et al. 2022; Han et al. 2026; Grunde-McLaughlin et al. 2026; none streams text |
| 35 | read | Browser | ACM DL (Bhat 2025) and SAGE (Powers & Scerbo 2021) | Both showed bot-verification pages; not bypassed → abstract only |
| 36 | read | curl | ODU repository DOI 10.25777/3h39-5r96 | Is Powers' MS thesis, not the Human Factors article → article kept as abstract only |
| 37 | R2 verify | Crossref bibliographic query | 20 packet citations (Drieghe 2017 … JIT Tokens 2026) | All resolved except Sharmin 2016 SKY and Knox 1968 (not in Crossref) |
| 38 | R2 verify | arXiv API | 2404.16283, 2604.04418, 2605.14999, 2607.14049, 2601.18033, 2506.23678 | All found; first author of 2604.04418 is Zhu, not Aggarwal |
| 39 | R2 verify | Open Library | Parkes, Pause and effect; Saenger | Parkes 1992 confirmed |
| 40 | R2 verify | Unpaywall + direct download | 16 packet DOIs | 8 full texts downloaded; Europe PMC (Kurby & Zacks) and SOTON eprints (Drieghe) blocked; browser extension disconnected |
| 41 | R2 verify | Crossref abstract field / Europe PMC records | Lei 2023, Kurby & Zacks 2008/2012, PNAS 2026 | abstracts retrieved |
| 42 | R2 verify | Consensus | Valsecchi 2013; Sharmin dynamic text; Drieghe 2017; Mangen 2013 | abstracts retrieved |
| 43 | R2 verify | WebSearch | Knox 1968 GRBS; Parkes "grammar of legibility" | Knox GRBS 9(4), 421–435; "Grammar of Legibility" is Parkes ch. 3 title |
| 44 | debate | Crossref + OpenAlex | 17 pasted debate citations, by DOI then by title | 5 of 17 DOIs resolved, 3 of those to other papers; all 17 records found by title (debate/records.md) |
| 45 | debate | OpenAlex abstract_inverted_index | Forshaw 2026; Horvers 2026; Yang 2026; Zhang 2026 | abstracts for Forshaw and Horvers; none for Yang, Zhang |
| 46 | debate | Semantic Scholar + Unpaywall + curl | Yang 2026 OA PDF (S1071581926001953) | ScienceDirect bot check; not bypassed |
| 47 | debate | Consensus | augmented reality pedestrians gaze patterns crossing probability automated vehicles | 20; Yang et al. 2026 abstract |
| 48 | debate | Consensus | user agency generative presence therapeutic self-attribution AI-driven VR mindfulness | 20; Zhang et al. 2026 record, no abstract |
| 49 | debate | Roger-supplied PDFs | 17 PDFs from Downloads -> debate/pdfs, pdftotext -> debate/texts | read; notes in debate/NOTES_FULLTEXT.md |
| 50 | lead | Crossref bibliographic | Design frictions for mindful interactions microboundaries Cox | 10.1145/2851581.2892410 found; not read |
| 51 | gap rerun 2026-10-20 | arXiv API (https) | streaming+LLM+"eye tracking"; streamed+"language model"+reading; "token streaming"+users; friction+LLM+verification; "decision spaces"+interface; chunking+"LLM output"+users | 2 / 100 / 11 / 5 / 11 / 1 hits; none segments streamed output for users; "decision spaces" not used for this concept |
| 52 | gap rerun | Consensus | eye tracking users reading streaming LLM chatbot responses incremental text | 19; only Park & Lee 2024 on streaming; others corpora/alignment |
| 53 | gap rerun | Consensus | pausing or segmenting AI-generated text output to support user verification | 19; none on paused/segmented streams; Kazemitabaar et al. 2024 (task decomposition) nearest |
| 54 | gap rerun | Consensus | design friction microboundaries LLM interfaces overreliance | 20; Collins et al. 2024 (selective frictions); Arun et al. 2026 (preparatory friction, N = 40); Dey et al. 2025 (friction turns); all friction before or around access, none inside streamed output |
| 55 | gap rerun | WebSearch (extended) | user study streaming LLM output pauses breaks verification eye tracking 2026 | none; Xiao & Yang 2025 nearest |
| 56 | read | Unpaywall + White Rose eprint | Cox et al. 2016 | read in full |
| 57 | verify | Crossref + OpenAlex | Gould, Cox, Brumby & Wickersham 2016, CHI, 3311–3323 | record and abstract; OA copy at Birmingham repository not fetched |
| 58 | journal | T&F PDFs hhciaims, hhciauth, hhciguidelines; T&F site and hci-journal.com | HCI length limit | No limit in any official document; hhciauth/guidelines are dated (editor Moran, APA 4th ed.); live pages behind bot check |
| 59 | §3 vetting | OpenAlex | chatbot response delay typing indicator perception humanness | Gnewuch et al. 2022 (BISE, N = 202); Tan et al. 2026 (CHI, latency); Milana et al. 2023 |
| 60 | §3 vetting | OpenAlex | streaming LLM response user experience perceived latency | Tan et al. 2026; Andes (already held) |
| 61 | §3 vetting | OpenAlex | reading dynamic scrolling text comprehension display | Kang & Muter 1989 (Times Square vs RSVP) |
| 62 | §3 vetting | OpenAlex | LLM overreliance verification convincingly wrong | Si et al. 2024 (NAACL); Kim et al. 2024 (FAccT) |
| 63 | §3 vetting | OpenAlex | eye tracking LLM chatbot responses reading | nothing new on streamed text |
| 64 | §3 vetting | OpenAlex | processing fluency judgments of truth | truth-effect literature; Reber & Schwarz 1999 verified via Crossref |
| 65 | §3 vetting | OpenAlex | automation bias review; explanations overreliance; LLM search; GenAI critical thinking; AI-framed questioning; agent oversight; live subtitles | Goddard et al. 2012; Vasconcelos et al. 2023; Fok & Weld 2024; Spatharioti et al. 2025; Lee et al. 2025; Danry et al. 2023 |
| 66 | §3 vetting | arXiv API | streaming/interrupt/agent oversight/streamed eye tracking/checkpoint queries | no results returned (API) |
| 67 | gap rerun | Consensus | streaming vs static presentation of AI chatbot responses on verification | Anderl et al. 2024 (Sci Rep) — READ IN FULL; Gnewuch 2022; Koscelny 2025; Yu et al. 2026 |
| 68 | gap rerun | Consensus | interrupting or pausing LLM generation for human oversight | WaitGPT (Xie et al. 2024, UIST) — READ (sections 1, 3–5, 7); AI Chains; Zhou et al. 2024 Nature; Taş et al. 2026 |
| 69 | gap rerun | Consensus | eye movements incremental word-by-word text, captions, regressions | Sharmin et al. 2016 abstract confirmed (letter by letter; 90.8% vs 57.1%); Inhoff et al. 2019; Wilcox et al. 2024; Lopes Rego et al. 2026 |
| 70 | verify | Crossref + DataCite | Bainbridge 1983; Reber & Schwarz 1999; Magentic-UI 2025; AI-Resilient Interfaces 2024 | all records verified |
