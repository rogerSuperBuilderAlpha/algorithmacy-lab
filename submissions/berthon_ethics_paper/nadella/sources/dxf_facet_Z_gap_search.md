# Z: Gap search

*Corrected on 2026-10-12 against `../audit/AUDIT_03.md`: 30 factual fixes.*

*Facet Z, 2026-10-12. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

## What this facet covers

A documented novelty check on one claim: the scribes' move from *scriptio continua* to word separation is the design precedent for what coordination through algorithmic intermediaries now needs, and a discipline called Decision Experience Design (DXD) should look for that move. The facet asks who has already said something like this, in seven parts: (1) the analogy applied to AI, algorithms, HCI, code or explainability; (2) the history of the page treated as the origin of UX; (3) "incunabula" or pre-convention arguments about AI interfaces; (4) the term "decision experience design" and its variants; (5) the term "algorithmacy" and the critiques of "algorithmic literacy"; (6) responses to the Nadella post of 10 October 2026; (7) scholarship arguing that oversight, observability or audit-log remedies reproduce a reading model.

## The question the synthesis answers

What exact sentence of the form "I found no work that does X in [sources]" can the paper print, and which predecessors must it cite to avoid looking unaware?

## Legend for read status

- **read in full**: whole text read this session.
- **read in part**: sections named.
- **abstract only**: database abstract or publisher blurb; paraphrase only.
- **summary only**: I received a model-written summary of the page (WebFetch or WebSearch) and not the raw text. Quotations marked "via fetch" came out of that summary and must be checked against the page before use.
- **not accessible**: blocked or not opened.

All searches ran on **2026-10-12**. "Hits" is the count the source reported, or the number of results returned for web queries. OpenAlex compound Boolean queries did not behave reliably (the same count, 45, came back for two different second clauses), so I inspected the returned records by hand and treat the counts as indicative only.

---

## (a) Search log

### OpenAlex, `filter=title_and_abstract.search`

| # | Exact query | Hits | Notes |
| --- | --- | --- | --- |
| 1 | `"scriptio continua"` | 87 | Mostly NLP word segmentation (Javanese, Balinese, Japanese, Thai), epigraphy, papyrology. |
| 2 | `"scriptura continua"` | 16 | Pflug lexicon entry; Cordingley 2006 (Beckett); Slote 2014; Okasha 2002; no technology analogy. |
| 3 | `("scriptio continua" OR "scriptura continua") AND (algorithm OR algorithmic OR "language model" OR chatbot OR prompt OR "artificial intelligence" OR "machine learning")` | 14 | All technical: tokenizers, OCR, restoring papyri (Fujii 2023; Cullhed 2024, 2025; Tolmachev 2018). Also Rosehill Zenodo episode 2736. No analogy. |
| 4 | same stem `AND (interface OR "user experience" OR usability OR "human-computer" OR typography OR "user interface")` | error | No count returned (query too long for the parser). |
| 5 | same stem `AND (interface OR usability)` | 45 | Top 45 inspected. Nothing draws the analogy. HCI-venue hit: Cho 2021 (DIS), see entry. Also Rosehill 2736, 2737; Stenberg 2017 (music scores). |
| 6 | same stem `AND ("user experience" OR usability OR "user interface")` | 45 | Same 45 records as #5; the count is not trustworthy. |
| 7 | same stem `AND (typography OR "human-computer" OR HCI)` | 0 | |
| 8 | same stem `AND (code OR programming OR "programming language" OR whitespace OR syntax OR "data format")` | error | Too many terms. |
| 9 | same stem `AND (code OR programming OR whitespace OR syntax)` | 7 | Robert-Hayek 2025; Slote 2014; Stenberg 2017; none about code as writing. |
| 10 | same stem `AND ("language model" OR chatbot OR "artificial intelligence")` | 7 | Tokenizer, Thai sentiment, papyri; Rosehill 2736. |
| 11 | same stem `AND (algorithm OR algorithmic OR platform)` | 6 | Javanese and Balinese transliteration tools; Thai sentiment. |
| 12 | same stem `AND (platform OR "recommender" OR "social media" OR digital)` | 6 | Cho 2021; Willis 2017 *Reading*; Helmke 2026. |
| 13 | same stem `AND (design OR designer)` | 4 | Murawaki 2016; Cho 2021; Syauqi 2026; Stenberg 2017. |
| 14 | same stem `AND (transparency OR explainability OR opacity OR legibility)` | error | |
| 15 | same stem `AND (transparency OR explainability OR opacity)` | 7 | Runes, Glagolitic, Metaphysics manuscripts; no XAI hit. |
| 16 | same stem `AND ("silent reading" OR Saenger)` | 10 | Rosehill 2737 and 2729; Okasha; Slote; Ramírez 2007; Kasisopa 2016 (Thai eye movements); Stenberg. |
| 17 | same stem `AND ("human factors" OR ergonomics OR cognitive)` | 4 | Slote; Willis; Stenberg; Rosehill 2729. |

### OpenAlex, `filter=fulltext.search` (top 10 inspected per query; counts are for the whole index)

| # | Exact query | Hits | Notes |
| --- | --- | --- | --- |
| 18 | `"scriptio continua" "large language models"` | 50 | All tokenization/multilingual-LLM papers (Feher 2025; Gu 2024; Inoue 2026) and Rosehill 2736. Technical sense only. |
| 19 | `"scriptio continua" chatbot` | 18 | Japanese/Thai NLP. |
| 20 | `"scriptio continua" "user interface"` | 24 | Transliteration tools, Liesaputra and Witten 2012 (*Realistic electronic books*), Lecolinet 1998. None uses the analogy in the abstract; full text not opened. |
| 21 | `"scriptio continua" "human-computer interaction"` | 11 | Same group. |
| 22 | `"scriptio continua" "explainable AI"` | 3 | Syauqi 2025 survey; two Niwa records. |
| 23 | `"scriptio continua" algorithmic` | 156 | Top 10 all NLP. |
| 24 | `"scriptio continua" "interface design"`, `"scriptio continua" "user experience"`, `"scriptio continua" "algorithmic" "literacy"`, `("Space Between Words" "Saenger" "artificial intelligence")` | not run | OpenAlex free budget exhausted ("Rate limit exceeded", no API key). The full-text leg is therefore incomplete for UX and literacy. |

### OpenAlex, other parts

| # | Exact query | Hits | Notes |
| --- | --- | --- | --- |
| 25 | `"In the Vineyard of the Text"` (title_and_abstract) | 11 | Illich 1993 record; reviews by Saenger 1995, von Hagen 1994, Margadant 1994; Babich 2014. |
| 26 | `"Illich" AND ("vineyard of the text") AND (interface OR "human-computer" OR design)` | 0 | |
| 27 | `"history of the page" AND ("user experience" OR "interface design" OR "human-computer interaction")` | 2 | Unrelated (Persian museum web pages; Irish digital history). |
| 28 | six further Q2 queries on Hugh of St Victor, Mak, Drucker, punctuation and interface, medieval manuscripts and UX | error | Unparenthesised OR/AND; not rerun before the budget ended. Covered instead by Crossref (#47-50) and WebSearch. |
| 29 | `"decision experience design"` (title_and_abstract) | 0 | |
| 30 | `search="decision experience design"` | 0 | |
| 31 | `"decision experience" AND (design OR designer)` | 61 | Top 15 inspected: nursing, MBA and educational-game papers. No design-discipline use. |
| 32 | `"DXD" AND (decision OR design)` | 560 | Pharmaceutical DXd conjugates; "DxD Design for District" (Collina and Simonelli 2000-2001, Italian industrial design). |
| 33 | `"decision design" AND (algorithm OR AI OR "artificial intelligence")` | 134 | New: Morii 2026 (SSRN), Haid 2023 (AHFE). See entries. |
| 34 | `"decision-centred design"` | 13 | O'Hare 1998; Schnittker 2019; **Sun 2026 (arXiv), "Decision-Centric Design for LLM Systems"** (its spelling is "decision-centric", so not an exact match for the query). |
| 35 | `"choice experience design"` | 0 | |
| 36 | `"decision architecture" AND ("artificial intelligence" OR algorithmic)` | 440 | Top 6: 2025-26 Zenodo/SSRN governance papers. No design-discipline claim. |
| 37 | `"decision intelligence" AND (design OR "user experience")` | 385 | O'Callaghan 2023 and Zenodo preprints. |
| 38 | `algorithmacy` (title_and_abstract) | 0 | |
| 39 | `search=algorithmacy` and `fulltext.search:algorithmacy` | 1 and 1 | Oberschelp 1995, IFIP chapter "Developing analytical competency through informatics teaching". Crossref has no abstract. **Resolved by the card (library/oberschelp1995developing.md): the chapter prints the word once, p. 121; see section 5.** |
| 40 | `"algorithmic numeracy" OR "algorithmic fluency"` | 21 | Applied-field papers (ICU, education). No construct competing with algorithmacy. |
| 41 | `"human oversight" AND (critique OR illusory OR fallacy OR "meaningful")` | 1,182 | Top 8 inspected: Zhu 2026; Lermann Henestrosa 2026; Rubegni 2026. |
| 42 | `"human oversight" AND "interface" AND (AI OR algorithmic) AND "audit log"` | 8 | Jerry 2026 (oversight-by-design for generative UIs). |
| 43 | `"legibility" AND "James C. Scott" AND (algorithm OR AI OR "machine learning")` | 2 | Cordeiro 2026, "What the Control Room Knows" (democratic legibility, journalism). |
| 44 | `"seeing like a state" AND ("artificial intelligence" OR algorithmic OR "language model")` | 13 | McQuillan 2016; Liu 2021; Willis 2025; Lee 2025; Golumbia 2015. |
| 45 | `"observability" AND (critique OR limits) AND ("AI governance" OR "algorithmic accountability")` | 39 | Meyman 2026 (Zenodo). |
| 46 | `"transparency ideal" OR "limits of transparency" AND algorithmic` | 26 | Descampe 2021; Brauneis and Goodman 2017; dos Santos 2026. |
| 46a | `"algorithmic literacy" AND (critique OR "wrong frame" OR "beyond literacy" OR "individualizes")` | 23 | Dasgupta and Hill 2023; Tanksley 2024; Vindigni 2026. |
| 46b | `"algorithm awareness" AND "rhetoric"` | 1 | Unrelated (Van Zanen 2024). |
| 46c | `"human oversight" AND "interface conventions"` | 0 | |
| 46d | `"alert fatigue" OR "automation complacency" AND "audit logs" AND AI` | 0 | |

### Crossref (`query.bibliographic`)

| # | Exact query | Hits | Notes |
| --- | --- | --- | --- |
| 47 | `scriptio continua artificial intelligence interface` | relevance count only | Top 6: reference entries (Brill's New Pauly; OED), Robert-Hayek 2025, Widiarti 2020, Butskhrikidze 2022. No analogy. |
| 48 | `scriptio continua large language model prompt` | same | Reference entries; Juman++. |
| 49 | `scriptio continua user interface design human-computer interaction` | same | HCI-series books unrelated to the term. |
| 50 | `word spacing history interface design silent reading Saenger technology` | same | Saenger 1997, 1982, 2020; reviews (Mulchahey 2001, Hanna 1999, Richter 2001); Reynolds and Walker 2004 (children's reading books). |
| 51 | `scriptio continua programming languages whitespace` | same | Nothing on code. |
| 52 | `decision experience design` | same | Skavronskaya 2017 (*Visitor experience design*), as on 30 Sept. |
| 53 | `algorithmacy` | 0 | |
| 54 | `decision experience (DX) design algorithmic intermediary` | same | Nothing relevant. |
| 55 | record verification, 17 lookups (Illich review, Mak, Bolter and Grusin, Drucker, Seaver, Bucher, Dogruel, Oeldorf-Hirsch and Neubaum, Gran et al., Koenig, Green, Ananny and Crawford, Norman, Dembeck) | n/a | Each target matched at rank 1 or 2, except Cotter and Reisdorf 2020 (no Crossref record found) and Houston *Shady Characters* (Crossref returned an error). |

### Consensus (three calls, no filters)

| # | Exact query | Hits | Notes |
| --- | --- | --- | --- |
| 56 | `scriptio continua word separation as analogy for artificial intelligence or user interface design` | 20 | NLP segmentation; Cho 2021; Buschek 2024 (*Collage is the New Writing*). No analogy. |
| 57 | `history of word spacing and silent reading as precedent for human-computer interaction or interface conventions` | 20 | Saenger 1997 (blurb), reviews (Aronoff 2002, Baeuml 2002), Mirault 2019, Petrick 2020 (historiography of HCI), Grudin 1989, Dyson 2004, Hsu 2000 (word spacing in Chinese on a VDT). No paper uses the history as an HCI precedent. |
| 58 | `human oversight of AI critique: interface conventions or structural design instead of monitoring logs and audit trails` | 20 | Green 2022; Koulu 2020; Zhu 2026; Holzinger 2024; Abulibdeh 2026; Mitchell 2026; Grunde-McLaughlin 2026; Laux 2023, 2025; Sterz 2024. |

### Failed or blocked sources

| # | Source | Result |
| --- | --- | --- |
| 59 | Scholar Gateway `semanticSearch` | `ACCESS_DENIED: Access denied`. |
| 60 | Semantic Scholar `/paper/search` (four queries: scriptio continua with LLM, with HCI, "decision experience design", "algorithmacy") | HTTP 429 on every call. |
| 61 | arXiv API (`all:"scriptio continua"`, `all:"decision experience design"`, `all:algorithmacy`, and three more) | HTTP 429 / timeout. Not run. arXiv content reached only through OpenAlex and Consensus. |
| 62 | OpenAlex | Free daily budget exhausted partway; later queries returned "Rate limit exceeded" (see #24, #28). |
| 63 | Forbes (Zainescu, 11 Oct 2026) via WebFetch | HTTP 403. Summarised from WebSearch snippets only. |
| 64 | uxdesign.cc "The chat box isn't a UI paradigm" via WebFetch | HTTP 403. Snippet only. |

### WebSearch (standard unless marked extended; each returned 9-10 results)

| # | Exact query | Result |
| --- | --- | --- |
| 65 | `"scriptio continua" AI prompts OR "language models" OR chatbot space between words analogy` | Only Fujii 2023 and tokenizer pages. No analogy. |
| 66 | `"scriptio continua" user interface design history word spacing UX analogy` | Wikipedia; pen-computing patents; an art-school blog. No UX analogy. |
| 67 | `"scriptio continua" programming whitespace OR "code" OR "JSON" analogy` | Tildes thread on spaces and ambiguity; Unicode reference. Nothing on code. |
| 68 | `"scriptio continua" LLM tokens prompt "like" medieval scribes spaces blog` | Clérice 2020; popular history pages (The Collector; Freewrite marketing blog). |
| 69 | `"we are in the scriptio continua era" OR "scriptio continua of AI" OR "scriptio continua" "AI interfaces"` | No exact phrase. Wintersberger 2022 (CHI SIG, "continuous interaction", unrelated sense). |
| 70 | `Saenger "space between words" lessons for AI interface design OR user experience OR "design history"` | Wikipedia; arXiv 2508.16914 (visual segmentation and word recognition). Nothing. |
| 71 | `"scriptio continua" Hacker News` | No HN thread surfaced. McGinley Substack (2025-08-06) and reference pages. |
| 72 | `"scriptura continua" AI OR algorithm OR interface OR UX essay` | Led to Boris Mueller's Medium essay (see entry). |
| 73 | `"Rosehill" "How Word Spacing Changed Human Thinking" OR "Why AI Flagged Your Em Dash" episode` | No web record of the podcast; found through OpenAlex/Zenodo instead. |
| 74 | `"spaces between words" invention analogy "AI" "prompt" OR "agents" OR "LLM" interface needs its own "punctuation" essay Substack` | UBC course blog on Saenger; Heather Radke, "On Spacebars" (Substack); AI em-dash essays. No interface argument. |
| 75 | `AI chat interfaces skeuomorphic early stage conventions "we are still" "early days" interface design history typography analogy Gutenberg "AI UX"` | Chat-as-default critiques (Designative 2026-03-19; setproduct). No Gutenberg or typography analogy. |
| 76 | `Medium OR Substack "scriptio continua" "agents" OR "algorithms" OR "platforms" OR "LLMs" reading without spaces metaphor opaque systems literacy` | **Dembeck 2023** (see entry); arXiv 2607.27547 "AI Literacy: An Exercise in Power-Knowledge"; Roe et al.; Gupta et al. |
| 77 | `Amelia Wattenberger "Why Chatbots Are Not the Future"` | Willison link post, 2023-05-15; fetched original. |
| 78 | `Maggie Appleton "Language Model Sketchbook, or Why I Hate Chatbots"` | Fetched. |
| 79 | `Pete Koomen "AI Horseless Carriages" essay` | Coverage; fetched koomen.dev. |
| 80 | `Geoffrey Litt "Malleable software" Ink & Switch essay LLM` | Litt 2023 post; Litt et al. 2025 essay (summary only). |
| 81 | `Jakob Nielsen "AI: First New UI Paradigm in 60 Years" intent-based outcome specification` | Nielsen's Substack and UX Tigers; fetched. |
| 82 | `chat is the command line of AI "command line" era interfaces "GUI moment" for AI essay` | Tunguz; Fazi "Prompt in the Shell"; AltaML; The Register 2026-03-11; Speedinvest; uxdesign.cc. Snippets only. |
| 83 | `AI interfaces "incunabula" OR "incunable" chat interface early conventions not yet settled printing press analogy design` | No incunabula framing. Huttenlocher quote (movable type as nearest analogue to AI); Roosen, "AI is not a Printing Press". |
| 84 | `"pre-Gutenberg" OR "early printing" analogy for large language model interfaces design conventions page layout` | No such analogy. Generative-interfaces preprint (arXiv 2508.19227); deRSE25 workshop paper. |
| 85 | `Linus Lee "Prism" OR "text interface" language models "interfaces" essay thesis "Is chat the right interface"` | The search did not locate an essay by that name; his site and talks surfaced. Not read. |
| 86 | `Bret Victor "Humane Representation of Thought" OR "Magic Ink" large language models critique AI interface` | Victor's own texts only; no LLM commentary by him found. |
| 87 | `Illich "In the Vineyard of the Text" Hugh of St Victor page layout index "user interface" OR "user experience" OR "technology of reading" interface design` | Publisher pages, Goodreads, secondary essays. No UI reading of Illich found in these results. |
| 88 | `history of user experience design origins medieval manuscript page layout index punctuation "first interface" OR "first UX" scribes` | Getty, *Graphic Design in the Middle Ages* (2023): scribes as early graphic designers. Not called UX. |
| 89 | `Johanna Drucker interface "Graphesis" book as interface page design history humanities interface theory` | Publisher blurbs; reviews (Enslen 2016; Sattler 2014). |
| 90 | `Bonnie Mak "How the Page Matters" argument page as technology of reading` | Illinois project page; Monoskop; reading-course notes. |
| 91 | `"algorithmacy"` (extended) | Hunt's Substack posts; algorithmacy.org (the author's conference, 28-31 Oct 2026); two GitHub copies of the lab repo. No other author. |
| 92 | `"decision experience design" OR "Decision Experience Design (DXD)"` (extended) | Hunt's Substack post (the published Part 1); "Digital Experience Design (DXD)" job listings (Gensler via builtin). No other use. |
| 93 | `"decision experience" "DX" designer algorithm "decision design" 2026 Substack OR Medium OR LinkedIn` | Kobetz, "DX Perspective" (DX there is the newsletter's own name; no "decision experience"); Serrault, "AI & Decision Design" seminar (30 Jan 2026); Medium essay "UX Design 2026+: From producing to deciding". None uses the term. |
| 94 | `Nadella "Models as Insider Risks" Super Intelligence Era critique OR response OR analysis` (extended) | Nine news and explainer pages (Business Standard; Forbes; officechai; others). Forbes reports the post's argument; it is not a critique. |
| 95 | `Nadella insider risk post models logging audit "human oversight" OR "alert fatigue" OR "usability" OR "human factors" criticism` (extended) | Eight explainers. One source calls the post a statement of intent rather than a technical specification [unverified: see AUDIT_03]. Nothing on logs, usability or human factors. |
| 96 | `Nadella "insider risk" models Hacker News OR LessWrong OR "AI Alignment Forum" OR Schneier OR Lawfare reaction` | None of the named venues returned. Digg aggregator page shows engagement; All-In Podcast background. |
| 97 | `critique of "algorithmic literacy" OR "algorithm awareness" individualizes responsibility onto users structural alternatives design platform` | Korean-language study of recommender literacy limits; arXiv 2507.23585 ("Agency Among Agents", hypertextual friction); MSU dissertation on critical algorithmic literacy. Snippets only. |
| 98 | `"grammar of legibility" Parkes OR "legibility" interface conventions AI governance` | No source uses "grammar of legibility" for AI. Singapore Consensus 2026 (arXiv 2608.14611) and Lancaster "Legible AI by design" treat legibility as a goal [Singapore gloss unverified: see AUDIT_03]. Snippets only. |
| 99 | `Lorien Pratt "decision intelligence" definition Link book; Cassie Kozyrkov "decision intelligence" discipline definition` | Kozyrkov: "turning information into better actions" (secondary). Pratt: talk summary. |
| 100 | `"human oversight" of AI illusion OR fallacy "rubber stamp" interface design "structural" rather than oversight Green Enqvist Koulu critique 2024 2025` | Green 2021/2022 and coverage. |
| 101 | `Oberschelp "Developing analytical competency through informatics teaching" algorithmacy` and `"algorithmacy" Oberschelp OR "algorithmics" numeracy literacy "algorithmacy" 1990s informatics education` | The chapter was not found online; no source links it to "algorithmacy". The second search returned Hunt's Substack, which says the word appeared once before, in an unpublished talk (Leese and Matzner 2016). I could not verify that. |

### Fetches and downloads

| # | Item | Result |
| --- | --- | --- |
| 102 | Mueller, Medium feed `@borism` | Read first 100,000 of 122,799 characters, through the fetch tool. |
| 103 | McGinley Substack, "Scriptio Continua" | Summary only. |
| 104 | Wattenberger, wattenberger.com/thoughts/boo-chatbots | Summary only. |
| 105 | Koomen, koomen.dev/essays/horseless-carriages | Summary only. |
| 106 | Nielsen, jakobnielsenphd.substack.com | Summary only. |
| 107 | Appleton, maggieappleton.com/lm-sketchbook | Summary only. |
| 108 | Dembeck 2023 PDF, orbilu.uni.lu/handle/10993/59372 | Downloaded to `~/iit-playground/dxd_foundation_local/pdfs/Z/dembeck2023.pdf`; `pdftotext`; **read in full** (3,387 words, German). |
| 109 | Zenodo records of Rosehill episodes 2729, 2736, 2737 | Abstracts via OpenAlex (Zenodo's own API failed). |
| 110 | Abstracts via OpenAlex for Lermann Henestrosa, Zhu, Rubegni, Meyman, Cordeiro, Willis, Morii (none), Sun | Database abstracts. |
| 111 | algorithmacy.org | Page metadata only (event, dates). |

---

## (b) Entries

Ordered by closeness to the author's use. "Same claim" would mean: word separation moved work from reader to page, and that is the precedent for a design move that makes algorithmic mediation workable. **No entry is "same claim."**

### 1. Dembeck (2023), "Im Flow: Skizze über Ausdruck und Beitrag im Digitalen"
- **Key:** `dembeck2023flow`. Till Dembeck, University of Luxembourg, *andererseits* 11/12 (2023); reprinted in the 2024 yearbook, DOI 10.14361/9783839469811-020 (Crossref record found). PDF at orbilu.uni.lu/handle/10993/59372.
- **Verified by:** Crossref record for the 2024 reprint; orbilu metadata; PDF downloaded.
- **Read status:** read in full (German; translations below are mine).
- **What it argues:** Following Illich, the shift from *scriptio continua* to the two-dimensional page around 1200 founded what Dembeck calls "biblionome Literalität" (book-bound literacy: abstraction, independent expression, the standalone "Beitrag"). He then asks what "digital literacy" is, and observes that current media-literacy and fake-news education take the book paradigm as their starting point, and suggests, in a hedged conjecture ("Es könnte aber sein", §5), that this "could miss the point entirely" ("an der Sache völlig vorbeigeht").
- **Quotations (original German, section locators):**
  - §1: "Der Übergang von der Schreibweise der scriptio continua, die Buchstaben aneinanderreiht, ohne sie durch Wortzwischenräume, Interpunktion, Absatzstrukturen usw. zu organisieren, hin zur zweidimensional disponierten Seite ging dabei Hand in Hand mit einer ganzen Reihe von Entwicklungen, die sich Jahrhunderte später als zentral für das moderne Bildungsverständnis erwiesen."
  - §1: "man gerät in eine Art Tunnel" (on reading unspaced text). The modern text "erzeugt Übersicht und keinen Tunnelblick."
  - §4: the digital flow is "durch algorithmische Rechenarbeit im Hintergrund zumindest mitgesteuert" (co-steered by algorithmic computation in the background). This is the only algorithm mention; it is a relative clause in the main argument, not a parenthesis (the parenthesis that follows concerns Raymond Williams's "flow").
- **Closeness:** adjacent, and the nearest in print. It uses the same historical hinge (Illich, Parkes, Saenger in n. 1) to argue about a digital-age literacy, and it doubts, in a hedged conjecture (§5), that the goals book-bound literacy passes on to media-literacy education fit the digital. It does not treat word separation as a design move for a mediator, does not discuss algorithmic third parties, and does not propose a design remedy.
- **Bearing:** complicates a bare novelty claim for "history of the page as a lens on digital literacy". Supports the author's suspicion that book-bound literacy goals may not fit the digital (hedged in Dembeck; rulings 1 and 2). Cite as predecessor.

### 2. Mak (2011), *How the Page Matters*
- **Key:** `mak2011page`. University of Toronto Press. Existence verified by Crossref review records (Driver 2013, *Speculum*, DOI 10.1017/s0038713413001322).
- **Read status:** summary only (publisher and course-note summaries; I did not open the book).
- **What it argues (secondary):** The page is an interface that has developed since the scroll. Mak follows one fifteenth-century text (*Controversia de nobilitate*) through manuscript, print and digital forms. Chapters include "Architecture of the Page" and "The Digital Page" (Illinois news notice, via WebSearch).
- **Closeness:** adjacent. It treats the page as an interface across media, which is the claim "history of the page as human-factors history" in general form. It is not about word separation specifically or about algorithmic mediation.
- **Bearing:** the author cannot claim to be first to call the page an interface. Needs a full read before anything is said about its chapters.

### 3. Illich (1993), *In the Vineyard of the Text: A Commentary to Hugh's Didascalicon*
- **Key:** `illich1993vineyard`. Existence verified through OpenAlex (W-record, 1993) and Saenger's review (*Library Quarterly* 65, 1995, DOI 10.1086/602782). Publisher not shown in the records I opened.
- **Read status:** summary only (Equinox table of contents and secondary essays); also seen through Dembeck's page references (Illich 1991 German edition, pp. 55-60, 101-104, 121-129, as Dembeck cites them).
- **What it argues (via Dembeck, read in full):** The twelfth-century page, with its two-dimensional layout, made the text an object one could navigate and compare; Illich ranks it above the printing press in media-historical force. Dembeck reports Illich as saying the layout operation is "exakt diejenige Operation ... die man durchführen muss, um einen Text in den Druck umzusetzen" (§1).
- **Closeness:** adjacent. Illich is the strongest predecessor for "a change of page layout as a technology of reading". Nothing in searches #87 and #26 links him to UX or interface design; a WebSearch summary of a notice of the book (reported in AUDIT_03, not checked by me) says he extended the argument to the screen replacing the page.
- **Bearing:** supports the idea that layout, not only word spacing, was the move (problem 4 in the plan). Must be cited.

### 4. Buschek (2024), "Collage is the New Writing"
- **Key:** `buschek2024collage`. DIS 2024, DOI 10.1145/3643834.3660681 (Consensus record).
- **Read status:** read in full (card: library/buschek2024collage.md).
- **What it argues:** Literary concepts (collage) offer lenses for designing AI writing tools; "creators of future writing tools" should "engage not only with new technological possibilities, but also with past writing innovations" (abstract).
- **Closeness:** adjacent in method (writing history as a source of AI-interface design), distant in content (collage, one writer, one tool). The full text confirms this: his history is literary Expressionism and Manovich's 1999 "avant-garde as software" (hyperlinking as a parallel), and he explicitly limits the claim to interface form.
- **Bearing:** shows the method "learn from writing history for AI interfaces" is already in HCI. Cite as a methodological neighbour.

### 5. Mueller (2026), "The Interface is Content"
- **Key:** `muller2026interface`. Medium, 2026-02-21, borism.medium.com/the-interface-is-content-b13f4d693d66.
- **Read status:** read in part (first 100,000 of 122,799 characters, through the fetch tool).
- **What it argues:** Typography is the interface of text and cannot be separated from content. *Scriptio continua* appears once, as a counterexample to a stripped-down text; spacing "is crucial to fast reading" (via fetch).
- **Closeness:** decorative mention. It uses the history to say removing interface cues makes content less meaningful. No AI claim in the portion I saw (the unread 22,799 characters could change that).
- **Bearing:** shows a UX-side writer reaching for the same example. Not a precedent.

### 6. Rosehill, Gemini 3.1 (Flash) and Chatterbox TTS (2026), podcast episodes 2737, 2736, 2729
- **Keys:** `rosehill2026wordspacing` (DOI 10.5281/zenodo.20182987), `rosehill2026emdash` (10.5281/zenodo.20182971), `rosehill2026beehives` (10.5281/zenodo.20182929). Zenodo, May 2026.
- **Read status:** abstract only (OpenAlex records of the Zenodo deposits). The creator field names Gemini and a text-to-speech tool; DataCite also lists Daniel Rosehill as a creator (AUDIT_03), so "AI-generated" is not established.
- **What they say:** 2737 summarises Saenger's thesis that word separation "enabled silent reading, private reflection, and ultimately the modern sense of self". 2729 says Irish monks "accidentally rewired human cognition". 2736 links punctuation history to AI em-dash detectors.
- **Closeness:** decorative. None applies the analogy to interface design or algorithmic mediation.
- **Bearing:** do not cite. They repeat the "rewired cognition" claim that the standing ruling excludes.

### 7. Cho, Cheon and Kang (2021), "Giving Space to Your Message"
- **Key:** `cho2021giving`. DIS 2021, DOI 10.1145/3461778.3462078.
- **Read status:** read in full (card: library/cho2021giving.md).
- **What it says:** A real-time word-segmentation (spacing) aid for Korean typists. The abstract mentions *scriptio continua* only as the contrast case ("far from scriptio continua"); the body does the same and no more (Section 1, p. 2; Section 2, p. 3, on "indecisive spacings" in Chinese, Japanese and Korean).
- **Closeness:** an HCI paper about inserting spaces, so literal, not analogical.

### 8. NLP and digital-humanities uses of "scriptio continua" (technical sense)
- Clérice 2020 (`clerice2020evaluating`, DOI 10.46298/jdmdh.5581); Fujii, Shibata and Yamaguchi 2023 (`fujii2023how`, DOI 10.48550/arxiv.2306.09572); Butskhrikidze 2022 (`butskhrikidze2022what`, DOI 10.2478/jazcas-2022-0006); Widiarti and Pulungan 2020; Cullhed 2024/2025.
- **Read status:** Clérice, Fujii and Butskhrikidze read in full (cards); the others abstract only.
- **Bearing:** these are the "AI and *scriptio continua*" results a reviewer will find. They concern tokenization or typology of unspaced scripts, not an analogy. Fujii tested Japanese only (Thai and Chinese appear only in its introduction's list; other languages are named as future work, p. 43); Butskhrikidze is a linguistic-typology paper on Burmese, Thai and Lhasa Tibetan, not NLP; Clérice's one-line aside says *scripta continua* "disappeared around the 8th century" while "spacing remained erratic" (Section I, p. 1), a dating sentence the abstract does not show. Cite one (Fujii 2023) to show the reviewer the collision was seen.

### 9. Wattenberger (2023), "Why Chatbots Are Not the Future"
- **Key:** `wattenberger2023chatbots`. wattenberger.com/thoughts/boo-chatbots; dated 15 May 2023 by Willison's link post.
- **Read status:** read in full (card: library/wattenberger2023chatbots.md).
- **Argues (via fetch):** "Good tools make it clear how they should be used"; "the burden to learn what works still lies with every single user." No writing-history analogy. Partly about one user and a tool; also criticises automation that turns people into "machine operators".
- **Closeness:** shares the author's premise that the burden has been put on the user; different remedy (controls and affordances), different structure (one user). The full text adds that she wants the interface to carry the user's burden, the same direction as the spacing precedent, differing in scale and parties; the essay models one user and one chatbot and never mentions an interested third party.

### 10. Appleton (2023), "Language Model Sketchbook, or Why I Hate Chatbots"
- **Key:** `appleton2023sketchbook`. maggieappleton.com/lm-sketchbook; undated on the page, mid-2023 by backlink.
- **Read status:** read in full (card: library/appleton2023sketchbook.md).
- **Argues (via fetch):** "We are irreversibly anchored to this text-heavy, turn-based interface paradigm"; chat is "the lazy solution". Prototypes for one writer and one model. No history analogy. The design aim is to keep the writer's own reasoning active (card).

### 11. Koomen (2025), "AI Horseless Carriages"
- **Key:** `koomen2025horseless`. koomen.dev/essays/horseless-carriages; the essay cites April 2025.
- **Read status:** read in full (card: library/koomen2025horseless.md).
- **Argues (via fetch):** AI apps "mimic old ways of building software"; users should edit the system prompt of an agent "acting on my behalf". This is the only neighbour with an agent acting for a person, but the setting is one user and an agent (an email scenario involves a boss as recipient, not as a party the mediator reads).
- **Closeness:** the "horseless carriage" structure of the author's pre-convention claim, without the page history.

### 12. Nielsen (2023), "AI Is First New UI Paradigm in 60 Years"
- **Key:** `nielsen2023paradigm`. Substack mirror of UX Tigers. The fetch gave 22 June 2023; a search snippet gave 20 May 2023 for the original (AUDIT_03 confirms: Substack mirror 22 Jun 2023, UX Tigers original 20 May 2023). The words "articulation barrier" are the title of a separate Nielsen article linked from this one, not words in this article; this article says half the population in rich countries is "not articulate enough" to get good results from current AI bots.
- **Read status:** read in full (card: library/nielsen2023paradigm.md).
- **Argues (via fetch):** a third UI paradigm, "intent-based outcome specification", with an "articulation barrier": "half the population in rich countries is not articulate enough" to get good results. No conventions, no writing history.
- **Closeness:** the nearest claim about *who can use* AI interfaces (articulation as the new literacy), pointing the opposite way: Nielsen locates the barrier in users' writing skill and does not propose an interface convention to remove it.

### 13. Litt et al. (2025), "Malleable Software"; Litt (2023)
- **Key:** `litt2025malleable`. Ink & Switch. Read in full (card: library/litt2025malleable.md). Argues users need agency to modify software. It is not only "one person and their tools": a whole section ("Communal creation") argues that malleability is a group matter, with shared tools for teams, hospital departments and Mastodon instances. No history analogy (confirmed).

### 14. Bret Victor; Linus Lee
- Victor's "Humane Representation of Thought" (2014) and "Magic Ink" (2006): found his own texts; no commentary by him on LLMs. Lee: the search found his research on manipulable model internals; I did not locate or read an essay on chat interfaces. Neither is a precedent for the page-history analogy.

### 15. Other chat-interface commentary (snippets only)
- Tunguz, "The Text Box Isn't Enough" (DOS analogy); Fazi, "Prompt in the Shell"; AltaML, "The Chat Box is the New Command Line"; UX Collective, "The chat box isn't a UI paradigm; it's what shipped" (403 on fetch); Designative, "The Conversation Trap" (2026-03-19). The command-line and DOS analogies are common and are about one user and a tool. None used a writing-history analogy.

### 16. The oversight-fallacy literature (Q7)
All at abstract level unless noted.
- Green (2022), `green2022flaws`, *Computer Law & Security Review*, DOI 10.1016/j.clsr.2022.105681. Surveys 41 policies; finds people cannot perform the oversight functions and proposes "a shift from human oversight to institutional oversight".
- Koulu (2020), `koulu2020proceduralizing`, DOI 10.1177/1023263x20978649: oversight risks becoming "an empty procedural shell".
- Lermann Henestrosa, Grinbaum and Yamshchikov (2026), `lermannhenestrosa2026human`, PsyArXiv, DOI 10.31234/osf.io/u68y2_v1: proposes "a conceptual reorientation of human oversight away from reactive approval and toward structurally embedded control". The abstract's remedies are incentive-based ethical stress testing, normative clarity and accounting for the limits of human oversight, an institutional remedy rather than taking the work off the person. The full text also says general-purpose AI users are not served by "AI literacy" alone (section 3.3), which is close to ruling D3, but it makes the point for regulatory reasons (card).
- Zhu, Lu, Ding et al. (2026), `zhu2026designing`, *AI and Ethics*, DOI 10.1007/s43681-026-01147-7: design outputs "so that humans can efficiently check and contest them without having to resolve the task". The full text keeps the human as evaluator at run time but pushes much of the checking to design time and to sampling (pp. 5-6), and asks how to make the person's check cheaper, not what task the person keeps.
- Mitchell et al. (2026), `mitchell2026agents`, arXiv 2608.23642: agent designs "impede effective human oversight"; calls for "design-level affordances". Its solution inventory (Table 1, p. 7) includes structural items (bounded autonomy, automated pre-checks, separated roles), and it argues that design both obstructs oversight (Section 3) and erodes it (Section 4).
- Grunde-McLaughlin et al. (2026), arXiv 2602.16844: action traces "cumbersome"; a redesigned interface cut error-finding time but not final accuracy.
- Holzinger et al. (2024), `holzinger2024human`; Abulibdeh et al. (2026), `abulibdeh2026who` (*Lancet*): human-in-the-loop as "symbolic reassurance"; Meyman (2026), `meyman2026impossibility` (Zenodo, version 2.0.0): the abstract-level "formal claim that observability cannot produce ex-ante authorization" is overstated for the full text. Version 2.0.0 withdraws the universal argument of earlier editions and keeps a conditional information-sufficiency result on a stipulated model (Proposition 1, p. 11), and says observability and enforcement "remain complementary layers" (p. 18). It is a self-published, non-peer-reviewed note by an author affiliated with FERZ, Inc., the company whose doctrine it supports; its remedy is a deterministic external gate with a person only at ABSTAIN.
- **Closeness to the author's critique of observe-log-audit:** same direction. None targets the Nadella post (all predate it except Rubegni 2026-10-11, which is clinical). None draws on the history of reading. None uses "legibility" in Scott's or Parkes's sense for oversight; the only Scott hits are Cordeiro 2026 (journalism; "democratic legibility" as the capacity to read information systems; a programme statement for a newsletter, not a study) and Willis 2025 (working paper on robotics and high modernism), both abstract only.
- **Bearing:** the claim "oversight remedies reproduce a reading model" is not in these abstracts in those words. The narrower claim that human oversight as currently designed fails and needs redesign or institutional backing is established and must be cited; none of these sources replaces the human check with structure, with two qualifiers from the full texts: Zhu et al. (2026) push much of the checking to design time and sampling, so structure does replace some run-time checks, and Mitchell et al. (2026) include structural items in their inventory (bounded autonomy, automated pre-checks, separated roles), so they sit closer to the structural camp than this summary suggests.

### 17. Literacy critiques (Q5)
- Seaver (2019), `seaver2019knowing`, DOI 10.1515/9780691190600-028; Bucher (2017), `bucher2016algorithmic`, DOI 10.1080/1369118x.2016.1154086; Gran, Booth and Bucher (2021), `gran2020aware`, DOI 10.1080/1369118x.2020.1736124; Dogruel, Masur and Joeckel (2022), `dogruel2021development`, DOI 10.1080/19312458.2021.1968361; Oeldorf-Hirsch and Neubaum (2023), `oeldorfhirsch2023what`, DOI 10.1177/14614448231182662; Koenig (2020), `koenig2020algorithms`, DOI 10.1016/j.compcom.2020.102611; Ananny and Crawford (2018), `ananny2018seeing`, DOI 10.1177/1461444816676645. All verified as records in Crossref (compare titles). Read status: **not read this run**; the repo already holds cards for several (see REUSE.md).
- Cotter and Reisdorf (2020), "Algorithmic knowledge gaps": no Crossref record found; see (d).
- Dasgupta and Hill (2023), `dasgupta2023designing`: "designing for critical algorithmic literacies" (from F1; designing for learners' literacies; the full text shows the learners are children and the evidence is the authors' own case work).
- **Whether any says literacy is the wrong frame:** I did not find a paper that says so for the triad. The structural critique of individual literacy exists in scattered form (Korean recommender-literacy study; "Agency Among Agents" arXiv 2507.23585, which proposes interaction-level friction; both snippet level). Ananny and Crawford is the canonical transparency critique. Dembeck 2023 is the only one that says the *literacy frame* may be inherited from the book. Oeldorf-Hirsch and Neubaum's review (read in full, card) extends the literacy frame and does not question it.

### 18. "Algorithmacy" (Q5)
- **Uses by others found: one, Oberschelp (1995), in a different sense (see below); none in the sense the lab uses.** OpenAlex (title/abstract) 0; Crossref 0; WebSearch (extended) returned only Hunt's Substack posts, algorithmacy.org (the author's conference, 28-31 Oct 2026, Port of Spain) and two GitHub copies of the lab repository.
- **A prior printed use of the word: Oberschelp (1995), `oberschelp1995developing`**, IFIP chapter "Developing analytical competency through informatics teaching", DOI 10.1007/978-0-387-34842-1_12, p. 121 (read in full, card): "we have to preserve logicacy and algorithmacy by continuously training simple mental activities without artificial tools." The word occurs once and is not defined. It names a mental skill of carrying out algorithmic steps by hand, to be protected against tools that do the work; that is a different sense from the lab's, which is neither a capacity to navigate an algorithmic third party nor a coordination competence.
- **Author claim, unverified:** Hunt's Substack says the word appeared once before in an unpublished conference talk on algorithmic threat reasoning, citing Leese and Matzner (2016). I could not check it (WebSearch #101).
- **Competing definitions:** none found. "Algorithmic numeracy" and "algorithmic fluency" occur only in applied papers (OpenAlex #40).

### 19. "Decision experience design" and variants (Q4)
- **Scholarly use of the exact phrase:** 0 in OpenAlex (two forms), Crossref, Consensus (this run covers Consensus through three other queries only; I did not rerun the 30 Sept Consensus queries). Unchanged from 30 Sept.
- **New since 30 Sept, near collisions (abstract or title only):**
  - Morii (2026), `morii2026decision`, SSRN, DOI 10.2139/ssrn.6341998, "Decision Design as Judgment Architecture: Structuring Authority and Accountability in Human-AI Systems". No abstract in OpenAlex; not opened. **A prior or parallel use of "decision design" for human-AI systems; read before the paper uses that phrase.**
  - Sun (2026), `sun2026decision`, arXiv, DOI 10.48550/arxiv.2604.00414, "Decision-Centric Design for LLM Systems". Abstract read: an architecture that separates decision signals from the action policy so control is "explicit and inspectable". Software architecture, not user experience. It does use "decision-centric design" for AI systems and shares the word "inspectable" with the legibility paradigm the paper opposes, but in Sun "inspectable" means that developers can read the logged signal and the policy for debugging (pp. 1-3, 8); no end user or person acted on appears in the paper (card; read in part, appendices B-C skimmed).
  - Haid, Lang and Fottner (2023), AHFE, "Explaining algorithmic decisions: design guidelines for explanations in User Interfaces" (title only).
- **Practitioner use since 30 Sept:** I found none new. The author's own Substack post "Decision Experience Design" (published Part 1) is the only exact-phrase hit besides the seven practitioner uses F1 listed (G1-G7, not refetched). Kobetz's "DX Perspective" and Serrault's "AI & Decision Design" seminar (30 Jan 2026) were opened and do not use the term.
- **Acronym collision:** "DXD" is also "Digital Experience Design" (Gensler studio; job listings) and "Digital eXperience Design (DXD)" (Emakina, per AUDIT_03), "DxD Design for District" (2000-2001) and the pharmaceutical payload DXd.
- **Prior claim in decision-centred design:** Wolf, Klein and Thordsen 1991, O'Hare 1998, Thordsen 2003, Militello and Klein 2013 (from F1; keys `wolf1991decision`, `ohare1998cognitive`, `thordsen2003decision`, `militello2013decision`). I did not reopen them. The term is "decision-centered design", and F1 already concluded DXD must distinguish itself from it.
- **Prior claim in decision intelligence:** Kozyrkov: "turning information into better actions at any scale" (search snippet, secondary). Pratt: talk summary only. Neither uses "decision experience".

### 20. Nadella responses (Q6)
- **Post:** `nadella2026insider`, x.com/satyanadella/status/2108931348857827686 (URL as surfaced by search; another agent covers the text).
- **Critiques found in print:** none on human-factors grounds. Forbes, `forbes2026emergency` (Zainescu, 2026-10-11), reports the post's argument and is not itself a critique: the essay "moves responsibility for AI safety from the company that builds a model to the company that deploys it" and policing models with models "can stack one opaque system on top of another" (snippet-level paraphrase from WebSearch; page returned 403). One source (not identified in the summary) calls the post a statement of intent without a technical specification [unverified: see AUDIT_03].
- **Human-factors or design critique:** none found in tech press, security blogs or AI-safety forums. No hit from Hacker News, LessWrong, the Alignment Forum, Schneier or Lawfare. The search tools do not index X replies, so absence there is untested.
- **Related items that already carry the author's human-factors point without naming Nadella:** Green 2022; Mitchell 2026; Grunde-McLaughlin 2026; Zhu 2026 (entry 16).

---

## (c) Synthesis

### 1. Has anyone drawn the analogy?

**(a) AI, LLMs, prompts, chat, agents.** I found no work that presents the move from *scriptio continua* to word separation as a design precedent for AI. The only AI-adjacent hits are tokenization papers (technical sense) and podcast episodes whose Zenodo records name Daniel Rosehill with Gemini and a TTS tool as co-creators (decorative). Printing-press analogies for AI exist (#83) but are not about word separation. The "chat is the command line" and "horseless carriage" analogies are common (entry 15, entries 9 to 12), but none reaches for writing history in the summaries and snippets I saw.

**(b) Algorithms, platforms, recommender systems.** None found. Dembeck 2023 mentions algorithmic co-steering of "flow" in one relative clause (§4).

**(c) HCI, UX, usability in general.** Two instances: Mueller 2026 (decorative; partly read, the final 22,799 characters unread) and Cho 2021 (literal spacing aid). The page-as-interface idea is in print without the analogy (Mak, project page; Illich, a critical notice; Drucker not checked).

**(d) Code, data formats, programming.** None found. Search #67 returned only a forum thread on spaces and ambiguity. I did not search the camelCase versus underscore readability literature, which is the obvious place a programmer would look for word separation in identifiers (see (d)).

**(e) Explainability, transparency.** None found. The OpenAlex hit #15 returned no XAI work; #22's three full-text hits (Syauqi 2025, two Niwa records) were not opened.

Summary: **zero uses of the analogy as a design precedent, one adjacent use for digital literacy (Dembeck), decorative mentions in Mueller 2026 and three Rosehill episodes, and one literal spacing aid (Cho 2021).**

### 2. The page as the origin of UX

No source I found calls the medieval page the origin of UX. Mak (2011) treats the page as an interface that has developed since the scroll (project description; book not read), Drucker's *Graphesis* (2014) treats the interface as a visual form of knowledge production (blurb) [unverified: see AUDIT_03], and Getty's 2023 exhibition calls scribes early graphic designers (press page). Illich ties layout to a new technology of reading, and a WebSearch summary of a notice of his book (reported in AUDIT_03) says he extended the argument to the screen replacing the page. I verified existence but did not read these books; their claims here are from summaries. Candidates in the brief that I did not search in a way that returned evidence: Piper, Manovich, Bolter and Grusin (record verified only), Kirschenbaum, Grafton, Blair, Houston, Bringhurst, Norman. Norman's *Things That Make Us Smart* (not the 2013 *Design of Everyday Things* listed in (d) 9) exists (reviews in Crossref) but I did not test it for writing history. The claim "the author has the first human-factors reading of the page" cannot be made on this evidence; "the first reading that I found" can.

### 3. Pre-conventional AI interfaces

The nearest are Nielsen 2023 (the third-paradigm article, which says half the population in rich countries is "not articulate enough" for current AI bots; "articulation barrier" is the title of a separate Nielsen article), Wattenberger 2023, Appleton 2023, Koomen 2025 and Litt 2025. Strongest for the author's purposes: Koomen, because the agent acts for the user, and Nielsen, because his barrier is a literacy barrier. They differ in four ways: (1) one user and a tool, never two people and a mediator (Litt 2025 has a communal-creation section on shared tools for groups); (2) the remedy is more controls, a better paradigm or a malleable tool, not a convention that takes work off the person; (3) no history of reading or writing; (4) none uses "incunabula", "pre-Gutenberg" or "scriptio continua" in the summaries and search snippets I saw (searches #69, #83, #84). The deRSE25 workshop paper (eceasst 2716) and a generative-interfaces preprint (arXiv 2508.19227) also treat chat as an unsettled form (snippets only).

### 4. The term DXD

No scholarly use of the exact phrase. The new collisions are Morii 2026 ("decision design", unopened) and Sun 2026 ("decision-centric design", software architecture). The practitioner label from F1 stands. The decision-centred design lineage (Klein, Militello) holds the older claim to design organised around decisions (my gloss).

### 5. "Algorithmacy"

Not only the author: Oberschelp (1995, p. 121) prints "logicacy and algorithmacy" once, in a different sense (a mental skill of working through algorithmic steps unaided, kept alive by tool-free practice). One author-reported earlier mention (Leese and Matzner 2016) remains unchecked. The literacy-critique family exists (Seaver, Bucher, Cotter and Reisdorf, Gran et al., Dogruel, Oeldorf-Hirsch and Neubaum, Koenig), but I did not read them this run, so I cannot say which would call literacy the wrong frame.

### 6. Nadella responses

I found no published critique that targets the post on human-factors grounds. Forbes (Zainescu 2026-10-11) summarizes the post's accountability shift. No human-factors critique in the sources searched.

### 7. Oversight remedies reproduce a reading model

The prediction "human oversight as currently designed fails and needs redesign or institutional backing" is established (Green 2022 onward); none of these sources replaces the human check with structure, with two qualifiers from the full texts: Zhu et al. (2026) push much of the checking to design time and sampling, so structure does replace some run-time checks, and Mitchell et al. (2026) include structural items in their inventory (bounded autonomy, automated pre-checks, separated roles), so they sit closer to the structural camp than this summary suggests. The sharper claim, that audit logs ask people to read and so repeat the literacy model, is not in the abstracts I saw, and I found no "grammar of legibility" use for AI.

### (i) Nearest prior uses, ranked

| Rank | Source | Closeness | What it leaves undone |
| --- | --- | --- | --- |
| 1 | Dembeck 2023 | Adjacent: Illich's *scriptio continua*-to-page history applied to digital literacy; says the book-literacy goals inherited by media-literacy education may miss the digital case (§5, hedged: "könnte") | No algorithmic third party; no design move; no human-factors frame; German-language, small venue |
| 2 | Lermann Henestrosa et al. 2026; Zhu et al. 2026; Green 2022 | Adjacent in remedy: from oversight to "structurally embedded control" (the abstract's remedies are incentive-based stress testing and normative clarity) or institutional oversight | No history of reading; no triad; none addresses Nadella |
| 3 | Mak 2011; Illich 1993 | Adjacent in frame: the page as interface or technology of reading | Not about AI or algorithms; not word separation as a design move (read status: summary only) |
| 4 | Koomen 2025; Nielsen 2023 | Adjacent in claim: AI interfaces await a new design; articulation as barrier | One user and an agent or tool; no history; no convention proposal |
| 5 | Buschek 2024 | Method neighbour: literary concepts (collage) from avant-garde writing inform AI-writing-tool design | Collage, not word separation; one writer |
| 6 | Wattenberger 2023; Appleton 2023; Litt 2025 | Anti-chat | Mostly a single user (Litt 2025 has a communal-creation section on shared tools for groups); no history |
| 7 | Mueller 2026 | Decorative mention | Typography only |
| 8 | Rosehill 2026 (human host with Gemini and TTS co-creators) | Decorative | Popular summary of Saenger |
| 9 | Fujii 2023; Clérice 2020 and other NLP | Technical sense | Not an analogy |

### (ii) Draft gap statements

*Drafted by Claude for the author to accept, change or discard.*

**Strong form (what the searches support):**

> On 12 October 2026 I searched OpenAlex, Crossref, Consensus and the open web (WebSearch). In OpenAlex title and abstract (queries 1-3, 5-7, 9-13, 15-17) I searched "scriptio continua" and "scriptura continua" alone and with algorithm, language model, chatbot, prompt, artificial intelligence, machine learning, interface, usability, user experience, typography, human-computer, code, programming, whitespace, syntax, platform, recommender, social media, digital, design, transparency, explainability, opacity, silent reading, Saenger, human factors, ergonomics and cognitive. In OpenAlex full text (queries 18-23, first ten hits each) I searched "scriptio continua" with "large language models", chatbot, "user interface", "human-computer interaction", "explainable AI" and algorithmic; the full-text queries for "interface design", "user experience" and "algorithmic literacy" were not run (query 24), and prompt, platform, usability and code were not run in full text. In Crossref (queries 47-51), Consensus (56-57) and WebSearch (65-76) I searched "scriptio continua" or "scriptura continua", or "word spacing" or "space between words", with AI, language model, prompt, chatbot, user interface, interface design, human-computer interaction, silent reading, Saenger, programming, whitespace, code, agents, algorithms and platforms. Four OpenAlex queries returned errors (4, 8, 14, 28). I found no work in these results that presents the move from continuous script to word separation as a design precedent for AI interfaces, algorithmic intermediaries or human-factors practice. The uses I found are technical (tokenizing unspaced scripts), decorative (a typography essay; podcast episodes whose records name a human host with Gemini and a TTS tool as co-creators), or adjacent: Dembeck (2023) draws on Illich's account of the page to argue about digital literacy, with algorithmic co-steering of the flow mentioned once and not developed.

**Algorithmacy (add to the gap statement wherever it names the term):**

> The word "algorithmacy" is not new. Oberschelp (1995, p. 121) prints "logicacy and algorithmacy" once, in a different sense: a mental skill of carrying out algorithmic steps without tools, to be preserved by tool-free practice. I found no other use. The sense used in this paper is a different one.

**Fallback if the author or a reviewer accepts Dembeck as a close precedent:**

> Dembeck (2023) uses the same Illich-based history of the page to question whether book-bound literacy is the right frame for the digital. I found no work that carries the history of word separation into the design of coordination through an algorithmic third party.

**Limits the sentence must carry:** Semantic Scholar (#60), the arXiv API (#61) and Scholar Gateway (#59) were not available in this run, and Google Scholar was not searched (the audit's rerun of five arXiv API queries on 12-13 October 2026 found 0 hits; AUDIT_03); OpenAlex's full-text leg was cut short (#24); four OpenAlex queries returned errors; X, Hacker News and podcasts are not searchable by these tools. Do not write "no one has".

### (iii) Sources the author must cite as predecessors

1. Saenger 1997, Parkes 1992, Illich 1993 (the history itself; see facet A).
2. Dembeck 2023 (closest digital-literacy use of the same history).
3. Mak 2011 (page as interface) and Drucker 2014 (interface as visual knowledge), after reading.
4. Nielsen 2023, Wattenberger 2023, Koomen 2025 (current AI-interface critiques the paper should position itself against).
5. Green 2022, Lermann Henestrosa et al. 2026, Zhu et al. 2026, Mitchell et al. 2026 (oversight critique).
6. Morii 2026 and Sun 2026 (name collisions), after opening.
7. Wolf, Klein and Thordsen 1991; Militello and Klein 2013 (decision-centred design).
8. Ananny and Crawford 2018 (transparency ideal); Seaver, Bucher, Gran et al. (algorithmic literacy family).

### (iv) What undercuts a novelty claim

- **Dembeck 2023** already joins the history of the page to the question of digital literacy and doubts that book-bound literacy fits the digital.
- **Saenger's own blurb** states the cost-shift in nearly the author's terms: "the task of separating the words in continuous written text, which for half a millennium had been a function of the individual reader's mind and voice, became instead a labor of professional readers and scribes" (publisher abstract of *Space Between Words*, Consensus record, DOI 10.1515/9781503619081). That supports H-cost and is not the author's invention. The same blurb says "greater diffusion of literacy" was not seen as an advantage by the ancient world, which also bears on H-cause.
- **Oversight critique is already established** (Green 2022 and after). A human-factors critique of observe-log-audit regimes is not new as a direction; I found none addressed to the Nadella post. It may be new as an application to the post and as a reading-model diagnosis.
- **"Algorithmacy"** has an earlier printed use: Oberschelp 1995, p. 121, in a different sense (read in full; card). The Leese and Matzner 2016 claim is unchecked.
- **Name collisions** with "decision design" and "decision-centric design" (2026).
- **The page-as-interface idea** is in print (Mak, Illich, Drucker), so "history of the page as human factors" is not new in general form.

### Claims the sources contradict or complicate

- That nobody has linked *scriptio continua* to digital literacy: Dembeck 2023 has.
- That "decision experience design" is entirely unclaimed by neighbours: "decision design" (Morii 2026) and "decision-centric design" (Sun 2026) appear in AI contexts.
- That the "rewired cognition" line is safe: Rosehill's episode 2729 (human host with Gemini and TTS co-creators) repeats it [quote unverified: see AUDIT_03]; the standing ruling excludes it.

---

## (d) Gaps and unverified leads

1. **Morii 2026 (SSRN 6341998).** No abstract; open it. Library or SSRN download.
2. **Oberschelp 1995** (Springer, IFIP, DOI 10.1007/978-0-387-34842-1_12). Resolved: read in full (card); the word appears once, on p. 121, in a different sense.
3. **Leese and Matzner (2016)** unpublished talk cited in the author's Substack. Ask the author for the citation.
4. **Cotter and Reisdorf (2020), "Algorithmic knowledge gaps"** (*International Journal of Communication* 14). No Crossref record located; fetch from ijoc.org.
5. **Semantic Scholar, arXiv search, Google Scholar, Scholar Gateway.** Blocked (429 or access denied). Rerun when the limits clear: `"scriptio continua"` with LLM, interface, UX; `"decision experience design"`; `algorithmacy`.
6. **OpenAlex full-text leg** stopped at the free budget. Rerun #24 with an API key. Also rerun #28 with parentheses fixed.
7. **Social media.** X threads, Hacker News comment search (Algolia), Reddit, podcasts and conference talks are not covered. A person should search Algolia HN for "scriptio continua" and X for "spaces between words" with AI terms.
8. **Programming angle.** I did not search the camelCase versus underscore identifier readability literature (e.g., eye-tracking studies of identifier styles) or minified code as unspaced text. That is where a "word separation in code" paper would sit.
9. **Books not opened:** Mak 2011, Drucker 2014, Illich 1993, Manovich, Bolter and Grusin 1999, Kirschenbaum, Piper, Houston, Bringhurst, Norman 2013 (*The Design of Everyday Things*, a different book from *Things That Make Us Smart*). Needs library access. Mak and Illich are the priority.
10. **Mueller 2026**: unread final 22,799 characters; the essay could link spacing to AI.
11. **Pages read only through a fetch summary** (Wattenberger, Appleton, Koomen, Nielsen, McGinley): re-read the raw pages before quoting. Nielsen's date is settled by AUDIT_03: Substack mirror 22 June 2023, UX Tigers original 20 May 2023 (search snippet).
12. **Snippet-only items:** Forbes (403); uxdesign.cc; Tunguz; Fazi; AltaML; Singapore Consensus 2026 (arXiv 2608.14611); "Legible AI by Design" (Lancaster); "Agency Among Agents" (arXiv 2507.23585); Korean recommender-literacy study; Litt 2025. None may be relied on.
13. **Not run:** DXD in LinkedIn and Medium for items after 30 September beyond what WebSearch indexed; the seven F1 practitioner URLs were not refetched.
14. **Not verified:** Pratt's definition of decision intelligence; Kozyrkov's exact wording (secondary).
15. **Linus Lee** essay on interface thesis not located; **Bret Victor** on LLMs not found.
16. **Beyond-the-brief candidates not searched at all:** McLuhan; Kittler; Hutchins on cognitive artefacts; Eisenstein on print and typographic fixity (facets C and E cover these).

## Changes after full-text cards (2026-10-13)

- `oberschelp1995developing`: the "unresolved database hit" is resolved. The chapter prints "logicacy and algorithmacy" once, p. 121, in a different sense (a mental skill of carrying out algorithmic steps without tools, preserved by tool-free practice); "Uses by others found: none" corrected; section 5 summary, the novelty-undercut list and the open-leads item updated; a plain statement of the prior use added to the draft gap statements (marked as drafted by Claude).
- `meyman2026impossibility`: "a formal claim that observability cannot produce ex-ante authorization" replaced; version 2.0.0 withdraws the universal claim and keeps a conditional result on a stipulated model; self-published note by an author affiliated with FERZ, Inc.
- `sun2026decision`: "inspectable" means readable by developers (pp. 1-3, 8); no end user appears; read status "read in part (card)".
- `litt2025malleable`: "one person and their tools" corrected (a "Communal creation" section); read status "read in full (card)"; the summary table row and the "one user and a tool" difference list carry the qualifier.
- `mitchell2026agents`, `zhu2026designing`: structural items in Mitchell's inventory; Zhu moves checking to design time and sampling (pp. 5-6); "none of these sources replaces the human check with structure" qualified in the entry and in section 7.
- `lermannhenestrosa2026human`: added the section 3.3 point (close to ruling D3, argued on regulatory grounds).
- `buschek2024collage`, `cho2021giving`, `butskhrikidze2022what`, `fujii2023how`, `clerice2020evaluating`: read in full; Buschek's history is literary Expressionism and Manovich 1999 and he limits the claim to interface form; Cho's body matches the abstract; Butskhrikidze is a typology paper not NLP; Fujii tested Japanese only; Clérice's dating aside noted.
- `wattenberger2023chatbots`, `appleton2023sketchbook`, `koomen2025horseless`, `nielsen2023paradigm`, `cordeiro2026control`, `dasgupta2023designing`, `oeldorfhirsch2023what`, `dembeck2023flow`: read status updated to "read in full (card)"; Wattenberger wants the interface to carry the user's burden and never mentions an interested third party; Appleton's aim is to keep the writer's reasoning active; Cordeiro is a newsletter programme statement; Dasgupta's learners are children; Oeldorf-Hirsch and Neubaum extend the literacy frame.

Synthesis verdicts changed: (1) section 5 "Algorithmacy": "Only the author uses it. One unresolved database hit ... remain unchecked" became "Not only the author: Oberschelp (1995, p. 121) prints 'logicacy and algorithmacy' once, in a different sense". (2) Section 7 and entry 16 bearing: "none of these sources replaces the human check with structure" now carries two qualifiers (Zhu, Mitchell). (3) Section 4 differences list: "(1) one user and a tool" qualified for Litt 2025. (4) Novelty-undercut bullet: "Algorithmacy may have an earlier use ... Unresolved" became "has an earlier printed use ... in a different sense".
