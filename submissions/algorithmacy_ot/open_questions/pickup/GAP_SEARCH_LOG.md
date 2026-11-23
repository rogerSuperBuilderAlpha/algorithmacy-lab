# Gap search log, stage S10d

[Written by an Opus gap-check agent, stage S10d, 2026-11-22]

Run `ot-oq-2026-11`. This log records every search query I ran for the gap check in `GAP_CHECK.md`. Candidates: C1 = shortlist §1 (communicative capacity by form of relation, oracy → literacy → algorithmic form); C2 = shortlist §2 (individual capacity that keeps the AI-mediated colleague in view, remedy for blind following); C3 = shortlist §3 (third position between technology-as-partner and technology-as-medium, with its competence).

## Sources and settings

- **OpenAlex search API**: `https://api.openalex.org/works?search=<query>&per-page=6–12`, User-Agent `research-library-client/1.0`, no email. "Hits" is `meta.count` as the API returned it. I read the title and abstract of every returned record (top 6–12 by relevance).
- **Consensus** (`search` tool, no filters; page size 20 by default, 15 where noted). "Hits" is the number of records the tool returned; Consensus does not report a total.
- **Scholar Gateway** (`semanticSearch`): every call returned `ACCESS_DENIED: Access denied`. No results came from this source.
- Queries use the questions' own vocabulary only. No query contains the author's name, the paper's title, or its sentences.
- Bibliographic confirmation (not searches): I looked up each work cited in `GAP_CHECK.md` by DOI at `api.openalex.org/works/doi:<DOI>` and `api.crossref.org/works/<DOI>` on 2026-11-22. Full texts read: Heyd (2021), Afgiansyah et al. (2026), Pfadenhauer & Kirschner (2017), all downloaded as PDFs; Yuh et al. (2026) through Consensus full-text excerpts. Downloads that failed: Snyder (2025) Deep Blue PDF (HTML landing page; 403 to the web fetcher), Curchod et al. (2019) Edinburgh repository PDF (HTML returned), Yuh et al. (2026) JMIR page (empty 202 body).

## Queries

| Cand. | Source | Query | Date | Hits |
|---|---|---|---|---|
| C1 | OpenAlex search API | algorithmic literacy triad | 2026-11-22 | 7091 |
| C1 | OpenAlex search API | oracy literacy algorithm | 2026-11-22 | 140 |
| C1 | OpenAlex search API | orality literacy digital algorithmic form of communication | 2026-11-22 | 22138 |
| C1 | OpenAlex search API | algorithmic literacy communicative competence platform | 2026-11-22 | 13066 |
| C1 | OpenAlex search API | orality literacy algorithmicity sequence of communication media | 2026-11-22 | 8097 |
| C1 | OpenAlex search API | from literacy to algorithmic literacy new form of communicative competence | 2026-11-22 | 15780 |
| C1 | OpenAlex search API | platform literacy organization communication field ratings rankings genre | 2026-11-22 | 1517 |
| C1 | OpenAlex search API | Ong orality literacy secondary orality algorithms | 2026-11-22 | 1075 |
| C1 | OpenAlex search API | media ecology algorithm literacy third form after orality and literacy | 2026-11-22 | 3517 |
| C1 | Consensus search | a new communicative capacity after oracy and literacy for algorithm-mediated relations | 2026-11-22 | 20 returned (top 20 shown) |
| C1 | Scholar Gateway semanticSearch | Is there a communicative competence beyond oracy and literacy, defined by the form of relation between people when an algorithm or platform stands between them? | 2026-11-22 | ACCESS_DENIED (tool unavailable) |
| C3 | OpenAlex search API | worker customer algorithm triad intermediary evaluates both parties | 2026-11-22 | 703 |
| C3 | OpenAlex search API | AI-enabled service triad worker customer algorithm | 2026-11-22 | 1412 |
| C3 | OpenAlex search API | Simmel triad algorithm third party arbitrator platform | 2026-11-22 | 0 |
| C3 | OpenAlex search API | algorithm as mediator versus partner communication | 2026-11-22 | 107664 |
| C3 | OpenAlex search API | algorithm third party between two people triadic relation | 2026-11-22 | 6461 |
| C3 | OpenAlex search API | machine as communicator versus medium human-machine communication mediated communication | 2026-11-22 | 90909 |
| C3 | OpenAlex search API | algorithmic intermediary triad platform work customer rating | 2026-11-22 | 722 |
| C3 | OpenAlex search API | AI-mediated communication third party evaluation between humans | 2026-11-22 | 59031 |
| C3 | OpenAlex search API | triadic algorithmic management worker customer platform | 2026-11-22 | 2363 |
| C3 | Consensus search | algorithm as a third party that evaluates both worker and customer, neither partner nor channel, and the skills workers need | 2026-11-22 | 20 returned |
| C2 | Consensus search | team members over-rely on AI guidance and lose sight of colleagues; individual capacity to keep the human counterpart in view | 2026-11-22 | 20 returned |
| C2 | OpenAlex search API | automation bias team interdependence | 2026-11-22 | 9818 |
| C2 | OpenAlex search API | generative AI teams blindly follow AI recommendations coordination among team members | 2026-11-22 | 3096 |
| C2 | OpenAlex search API | overreliance on AI advice team coordination emergent interdependence | 2026-11-22 | 71 |
| C2 | OpenAlex search API | AI-mediated collaboration awareness of human colleague competence | 2026-11-22 | 14524 |
| C2 | OpenAlex search API | algorithm-mediated teamwork attending to coworkers rather than the algorithm | 2026-11-22 | 322 |
| C2 | OpenAlex search API | human-AI team AI exposure spillover human-human interaction | 2026-11-22 | 5172 |
| C3 | OpenAlex search API | AI-mediated communication definition agenda | 2026-11-22 | 53754 |
| C3 | OpenAlex search API | service triad technology customer frontline employee | 2026-11-22 | 1256 |
| C3 | OpenAlex search API | platform as neutral intermediary versus evaluator workers clients relational work | 2026-11-22 | 2229 |
| C2 | OpenAlex search API | human aid and automated tool reliance on coworker | 2026-11-22 | 1646 |
| C2 | OpenAlex search API | teammate versus tool AI team members coordination human colleagues neglect | 2026-11-22 | 261 |
| C2 | Consensus search | training clinicians to coordinate human-AI-human collaboration rather than defer to AI recommendations | 2026-11-22 | 15 returned (page_size 15) |
| C1 | Consensus search | tertiary orality or a third stage after orality and literacy defined by algorithms | 2026-11-22 | 15 returned (page_size 15) |
| C3 | Consensus search | technology neither communication partner nor medium but a mediator that judges both parties in an interaction | 2026-11-22 | 15 returned (page_size 15) |
| C1 | OpenAlex search API | Gloy orality literacy artificial intelligence | 2026-11-22 | 6 |
| C2 | Scholar Gateway semanticSearch | When team members follow guidance from a generative AI system, what individual capacity keeps the human colleague in view and prevents blind following or automation over-reliance in interdependent teamwork? | 2026-11-22 | ACCESS_DENIED (tool unavailable) |
| C3 | Scholar Gateway semanticSearch | Is there a theoretical position that treats an algorithm neither as a communication partner nor as a medium, but as an intermediary that evaluates and binds two human parties, and what competence does it require of them? | 2026-11-22 | ACCESS_DENIED (tool unavailable) |
| C1 | OpenAlex search API | dyad triad mediated communication competence typology algorithm | 2026-11-22 | 139 |
| C3 | OpenAlex search API | tertius algorithm platform third party evaluation workers customers | 2026-11-22 | 21 |
| C3 | OpenAlex search API | worker customer algorithm triangle skills relational work platform | 2026-11-22 | 528 |
| C2 | OpenAlex search API | automation complacency teams loss of coordination between human team members decision aid | 2026-11-22 | 567 |

Totals: 43 queries. C1 14 (11 OpenAlex, 2 Consensus, 1 Scholar Gateway denied); C2 12 (9 OpenAlex, 2 Consensus, 1 Scholar Gateway denied); C3 17 (14 OpenAlex, 2 Consensus, 1 Scholar Gateway denied). Rows appear in the order I ran them.
