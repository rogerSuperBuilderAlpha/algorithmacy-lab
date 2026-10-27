# Research plan — the Berthon ethics course paper

*Written by Claude on 2026-10-13 from the author's instruction and four answers of the same day (see
`SOURCE.md`). The author approved the plan; none of the wording below is his unless quoted.*

Every facet agent reads this file first. It states the question under test, the constraints, the facet
questions, the file format and the tool rules.

## 1. What the paper is

A paper by Roger Hunt for an ethics course taught by Pierre Berthon (Bentley). The author's instruction
(2026-10-13): "we want to look at the ethical issues as world literacy grew. lets look at how as a
global community we failed on ethical grounds during the transition and consider what similar misatkes
we are making during the current transition to algorithmacy."

The paper therefore has two halves. The first is historical: what went wrong, ethically, as reading
and writing moved from a craft of the few to a condition of ordinary life. The second is present-day:
which of those failures recur as coordination moves onto algorithmic intermediaries.

**This run produces research and an outline. Nobody drafts the paper; the author writes it.**

## 2. Terms

- **Algorithmacy.** The competence to coordinate with other people through an algorithmic third party
  that reads both parties and commits outcomes binding on both. The triad is two human parties and the
  intermediary.
- **The literacy transition.** The long change in which societies came to require reading and writing
  for legal, civic, religious and economic standing. This round treats three stretches: memory to
  written record (medieval), print (c. 1450–1800), and mass literacy (c. 1800–2000).
- **Ethical failure.** A wrong done to identifiable people in the course of the transition: by
  withholding the competence, by making standing conditional on it, by imposing it at the cost of
  another way of life, or by promising returns it did not deliver. Each claimed failure needs either a
  contemporary who named it as a wrong or a stated standard by which it counts as one.

## 3. Standing rulings that bind the research

| Ruling | Locator |
| --- | --- |
| No claim that literacy restructured cognition (Ong, Goody and Watt); Street's critique stands. The claims that survive are institutional | `sources/design_ethics_DRAFT.md:85`; `sources/part2_ethics_DRAFT.md:7` |
| "Nothing here claims literacy *rewarded* the literate" (Graff's distinction between requiring literacy and rewarding it) | `sources/design_ethics_DRAFT.md:85` |
| A source is quotable only at full-text depth | lab-wide |
| The history is evidence for the historical half; the inference to algorithmacy is an analogy | the author's ruling 1 of 2026-10-13, after the first round (`SOURCE.md`) |

## 4. Problems the research must settle

1. **The two drafts document no ethical failure of the literacy transition.** They hold the "monopoly
   of knowledge" line (Innis), the supply-of-readers line (Havelock) and the persons-to-documents shift
   (Clanchy). The round must find the documented wrongs, with dates, places and numbers.
2. **Presentism.** A past practice counts as an ethical failure only if a contemporary named it one or
   the paper states the standard it applies. Record who objected at the time and on what ground.
3. **"As a global community" outruns most of the record.** Most sources are national or imperial.
   Record the scale each source actually covers and find what exists at world scale.
4. **The comparison may break.** Literacy is a competence in a medium; algorithmacy is a competence in
   a coordination that a third party binds. A failure in one may have no counterpart in the other.
5. **The literacy myth cuts both ways.** If literacy did not deliver what its promoters promised,
   then "failing to spread it" is a weaker charge and "overselling it" a stronger one.

## 5. Facets

| Facet | File stem | Question |
| --- | --- | --- |
| A | `A_documents_and_standing` | When written records replaced memory and oral testimony, who lost legal or civic standing, and who said so? Clanchy on England 1066–1307; Stock; benefit of clergy; charters and land title against customary tenure; colonial treaties and deeds signed by people who could not read them |
| B | `B_print_1450_1800` | Licensing, privilege, censorship and monopoly over the press; vernacular standardisation and what it did to dialects and minority languages; who was kept from print and by what rule. Eisenstein, Johns, Innis, Febvre and Martin, Darnton, the Stationers' Company, the Index |
| C | `C_literacy_withheld` | Laws and customs that kept reading or writing from particular people: anti-literacy statutes for the enslaved in the Americas, restrictions by sex, caste, class and religion, the separation of reading from writing in schooling for the poor |
| D | `D_literacy_as_gate` | Literacy made a condition of standing: literacy tests for voting, immigration, jury service, office and military rank; who designed them, what their authors said they were for, how they were administered, and how they ended |
| E | `E_literacy_imposed` | Literacy brought by force or as an instrument of rule: colonial and missionary schooling, residential and boarding schools, alphabetisation campaigns, script reform, and the measured loss of languages and oral traditions |
| F | `F_promise_and_campaigns` | What promoters promised literacy would do and what it did: Graff's literacy myth and its critics, mass schooling, the international campaigns (UNESCO's Experimental World Literacy Programme and its own evaluation), the current count of adults who cannot read and who they are |
| X | `X_counter_case` | The strongest case against the paper: where the transition went well by the standards of its time and ours; where contemporaries named the failures as they happened; where the comparison between literacy and algorithmacy breaks |
| Z | `Z_gap_search` | Who has already argued from the ethics or the harms of the literacy transition to AI, platforms or algorithms; current uses of "AI literacy" that repeat or avoid the earlier pattern (tests, gates, deficit framing) |
| G | `G_third_parties` | Second round, by the author's ruling 8. Scribes, notaries, scriveners and treaty interpreters as third parties between two people: where a literate intermediary wrote or translated the binding text for parties who could not read it, whose side the intermediary served, what safeguards existed, and who objected |
| H | `H_berthon_record` | Second round, by the author's ruling 6. What Pierre Berthon argues in the 2019 mindfulness paper, the 2019 digital-addiction paper and his AI papers of 2023–2026: what each diagnoses, what it prescribes, and who bears the remedy |

The lead writes `T_adjudication.md` after the facets and the audit.

## 6. What the repo already holds

- `sources/design_ethics_DRAFT.md` lines 79–87 (the print history) and 112–120 (present-day harms);
  `sources/part2_ethics_DRAFT.md` lines 17–29 (mandatory participation, exit and voice), 57–63 (the
  scribes) and 65–75 (deskilling and Socrates on writing).
- `../algorithmacy_design_ethics/literature/library/`: 194 cards. Cluster H (`INDEX.md`, "The
  orality/literacy/print history and its critics") holds Ong, Johns, Innis, Havelock, Eisenstein, Goody,
  Clanchy, Street, Graff, Halverson, Scribner and Cole, Finnegan, Collins and Blot. Most are marked
  "not yet S2-verified" and several are secondary or description-level: Clanchy is read through Ong,
  Graff is description-level, Street is secondary, Goody (1986) is contents-only.
- `../decision_experience_design/part2_ethics/literature/facets/E_reading_history_meaning.{md,bib}`:
  Saenger and Parkes at snippet depth, Knox read in full.

Each of these is a lead. Reopen the source and record your own read status before relying on it.

## 7. Facet file format

Two files per facet in `literature/facets/`: `<stem>.md` and `<stem>.bib`. Model:
`../decision_experience_design/part2_ethics/literature/facets/E_reading_history_meaning.md`.

`<stem>.md` has, in order:
1. A header line: facet, date, "Agent-drafted. The author has not reviewed it, and none of the text is
   the author's."
2. **What this facet covers** and **the question the synthesis answers**.
3. **Legend for read status**: *read in full*, *read in part* (say which pages), *abstract only*,
   *not accessible*.
4. **(a) Search log**: a numbered table of source, exact query, hits, notes. Log failures.
5. **(b) Entries**, one per source: full reference, bib key, how you verified it exists, read status,
   what it argues, quotations with page or section locators, the scale it covers (town, nation,
   empire, world), and its bearing on the five problems of §4 (supports, complicates, refutes).
6. **(c) Synthesis** by question. For each documented failure give: what was done, to whom, where and
   when, on what stated ground, who objected at the time, and what ended it. End with a list of
   claims the sources contradict.
7. **(d) Gaps and unverified leads**, including every source you could not open and where a human with
   library access would find it.

`<stem>.bib`: one entry per source, key in the form `surnameYEARfirstword` (reuse an existing key when
the source is already in a repo bib), with a DOI, arXiv ID or stable URL, and a `note` giving read
status.

## 8. Rules

- Report what the sources say, including when they sink the thesis. A facet that confirms everything is
  suspect.
- Quote exactly, with a locator. Paraphrase anything you read only as an abstract and say so.
- Never invent a DOI, a page number, a quotation or a statistic. Write "not found" instead. A figure
  you remember but cannot find in a source this session does not go in the file.
- Resolve every DOI against Crossref (`https://api.crossref.org/works/<doi>`) and compare the title.
- Statutes, court opinions and official reports are primary sources: quote them from an official or
  archival copy and give the URL.
- Do not draw the parallel to algorithmacy in facets A–F. Record the history. Facets X and Z and the
  lead's adjudication carry the comparison.
- Write only inside `submissions/berthon_ethics_course/literature/facets/`, and only your own two files.
  Do not edit any other arm. Do not run git.
- Do not use the Chrome browser tools; several agents run at once and would collide. List sources that
  need a browser in section (d).
- Do not try to get around a paywall or a bot wall. Record the block.
- Never put a person's e-mail address in a request header, URL or payload. Send anonymous requests,
  with no `mailto`, and do not use Unpaywall, which requires an address. (Added after the first round:
  see `literature/audit/AUDIT_02.md`, line 9.)
- Tools that have worked: Crossref, OpenAlex (`https://api.openalex.org/works?search=`, whose
  `open_access.oa_url` field locates open copies), Europe PMC, HAL, author copies by `curl` and `pdftotext`,
  archive.org (including its full-text search and borrowable books), Open Library, HathiTrust,
  Project Gutenberg, the UNESCO digital library (unesdoc), the UNESCO Institute for Statistics,
  Consensus (at most three calls at a time; on a rate-limit error wait 30 seconds), WebSearch and
  WebFetch.
- Scholar Gateway failed in every earlier run. Try it once and log the result.
- Put downloaded PDFs under `~/iit-playground/berthon_ethics_local/pdfs/<facet>/`, never in the repo,
  which is public.
