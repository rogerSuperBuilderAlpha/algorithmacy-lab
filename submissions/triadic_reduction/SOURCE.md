# Sources — what came in, from where, and what is missing

The author worked this talk up with Gemini on 20 September 2026 and handed it over on 24 September as
seven share links, one NotebookLM link and one pasted script. Four of the chats (G1, G3, G5, G6) ran
inside a Gemini Project with its own source documents; the other three (G2, G4, G7) are Deep Research
chats outside it. The Project's citations led to the four Google Docs it drew on (D1–D4), and the same
Drive folder held two more Gemini documents on the argument (D5, D6). All of it is collected here
verbatim, and none of it is a source of truth. Gemini is a fast, confident drafter of scholarly claims and
an unreliable citer of them; the lab ruled one of its reports inadmissible as a source once already
([`../algorithmacy_design_ethics/literature/library/gemini_report_citation_audit.md`](../algorithmacy_design_ethics/literature/library/gemini_report_citation_audit.md)).
The rule here is the same as in [`../dial_response_algorithmacy/SOURCE.md`](../dial_response_algorithmacy/SOURCE.md):
the chats are process, and a claim from them reaches the talk only after the claims register has traced
it and a library card has verified it against the primary text.

## Inventory

The G files are captured from the share pages and the D files from Google Drive; P1 is the author's paste.
Capture details and hashes are in [`sources/MANIFEST.md`](sources/MANIFEST.md) and in each D file's header.

| id | file | origin | what it is | bears on |
| --- | --- | --- | --- | --- |
| G1 | [`G1_gem_prompt_algebraic_logic.md`](sources/G1_gem_prompt_algebraic_logic.md) | share `wifYlPqIe4ce` (Project) | Gemini's *suggested* custom instructions, drafted from "the document I added to the sources" (by timing and content, D1); nothing shows they were installed | S1, S3–S5 |
| G2 | [`G2_ux_design_ethics.md`](sources/G2_ux_design_ethics.md) | share `INo1hh79aNsi` | Deep Research on design ethics and human factors (report exported as D2) | S6, mostly out of scope |
| G3 | [`G3_pid_synergy_loss.md`](sources/G3_pid_synergy_loss.md) | share `2L9EOtC5Hywc` (Project) | Short reply examining algorithmacy, citing D2 and D1 | S5, S6 |
| G4 | [`G4_xai_information_loss.md`](sources/G4_xai_information_loss.md) | share `eWIbxgiGArtw` | Deep Research on XAI synergy loss (report exported as D3); its prompt is a paste of G3 | S5, S6 |
| G5 | [`G5_iit_org_coordination.md`](sources/G5_iit_org_coordination.md) | share `LFGcgeELx0CL` (Project) | The author's pasted "deep dive" into this repository (origin unknown) and Gemini's reply, which folds the repository into D1's "causal collapse" frame | S5, S6 |
| G6 | [`G6_foundational_literature.md`](sources/G6_foundational_literature.md) | share `cIRJ3NPUJRXz` (Project) | Six turns building a reading list. Turn 4 is the author's paste of ten per-paper reviews from an unknown tool; turn 6 has Gemini "review" works nobody in the chat had read | S1, S3–S6 |
| G7 | [`G7_tablets_to_algorithms.md`](sources/G7_tablets_to_algorithms.md) | share `SWkYyi5Ey3Ji` | Two Deep Research reports: text UX history, and sci-fi interfaces | S6 |
| D1 | [`D1_peirce_quine_iit_synthesis.md`](sources/D1_peirce_quine_iit_synthesis.md) | Doc `1YvrIj5D…` | **The Project's core document**: Peirce's thesis, Quine 1954, the PAL and clone results, the claimed synergy–teridentity correspondence, a 41-item works-cited list | S1, S3–S5 |
| D2 | [`D2_design_ethics_ux_research.md`](sources/D2_design_ethics_ux_research.md) | Doc `1Rg_Prnn…` | Export of G2's report | S6, mostly out of scope |
| D3 | [`D3_xai_synergistic_information_loss.md`](sources/D3_xai_synergistic_information_loss.md) | Doc `1nTLam9C…` | Export of G4's report | S5, S6 |
| D4 | [`D4_triads_notebook_vs_repository.md`](sources/D4_triads_notebook_vs_repository.md) | Doc `1Bc3epFh…` | Maps a "Triads" notebook onto this repository; the only Gemini source that states the lab's own genuineness/wholeness split and cause-side result | S1, S2, S4–S6 |
| D5 | [`D5_dyadic_reading_triadic_navigation.md`](sources/D5_dyadic_reading_triadic_navigation.md) | Doc `1NZpa3W4…` | Essay: from teridentity to literacy versus algorithmacy — the talk's closest ancestor | S1, S3–S6 |
| D6 | [`D6_catalog_theory_and_fiction.md`](sources/D6_catalog_theory_and_fiction.md) | Doc `13SLUNEp…` | Theory recap, thirty catalog entries (twenty-nine on speculative fiction), and a literacy/algorithmacy contrast | S1, S3–S6 |
| P1 | [`P1_gemini_presentation_script.md`](sources/P1_gemini_presentation_script.md) | author's paste | Gemini's seven-slide script and eight prepared Q&A answers | S1, S3–S6 |

Section codes: S1 Peirce's logical argument · S2 Simmel · S3 Quine and Löwenheim · S4 the modern logic
and philosophy debate · S5 the lab's IIT move · S6 algorithmacy.

## Coverage

The sources are uneven, and in one section they argue against the lab.

- **S1, Peirce.** Only Gemini's summary. The one pointer to Peirce's text is a single quotation attributed
  to CP 8.331 (D1), unverified; P1 dates the reduction thesis to 1897 without a source.
- **S2, Simmel.** One line in D4's list of the lab's thinker papers. S2 rests on the lab's own
  [`org_frontier/thinkers/simmel/`](../../org_frontier/thinkers/simmel/) and the verified Simmel cards in
  [`../slacker_thirds/library/cards/`](../slacker_thirds/library/cards/).
- **S3, Quine.** Only Gemini's reconstruction (D1, G6, P1). No source quotes Quine; his paper was an
  uploaded PDF cited once. Löwenheim appears nowhere.
- **S4, the logicians.** Burch, Hereth Correia and Pöschel, Dau and Koshkin appear in D1 and G6.
  Herzberger and Kempe appear only in D4's summary of the repository; Skidmore and Kerr-Lawson not at all.
  That part of the history comes from [`org_frontier/thinkers/peirce/`](../../org_frontier/thinkers/peirce/).
- **S5, the IIT move.** Plentiful, and mostly opposed to the lab. D1, G1, G3, G5, D5, D6 and P1 claim that a
  dyadic factorization forces Φ = 0, and D1 and P1 go on to call teridentity necessary and sufficient
  for Φ > 0. The
  lab's Peirce probes find Φ = 2.0 for a ring of one-input copies with no triadic mechanism in it, and
  Φ = 0 for branched wirings that contain three-term facts. Only D4 and P1's fourth prepared answer state
  the lab's actual result.
- **S6, algorithmacy.** Well covered: G3, G4 and D3, G7, D5, D6, and P1's second slide and first answer.

## The Gemini Project's own sources

Share pages G3, G5 and G6 cite the documents the Project was working from, and the capture keeps each
citation as a `[source: …]` marker. Besides D1–D4, the chips name the uploaded files below. The list shows
only files Gemini cited, not the Project's full upload set: G6 turn 4 discusses Rudin 2019, Miller 2019,
Oizumi et al. 2014, Williams and Beer 2010 and a Koshkin paper, none of which appears as a chip. These are
third-party papers and are not committed; the library phase acquires open-access copies and cards them.

| file name in the Project | probable work |
| --- | --- |
| `Quine-ReductionDyadicPredicate-1954.pdf` | Quine, "Reduction to a Dyadic Predicate," *JSL* 19(3), 1954 |
| `2004_Hereth_Poe.pdf` | Hereth Correia and Pöschel, "The Power of Peircean Algebraic Logic (PAL)," 2004 |
| `2006_Hereth_Poe_Teridentity.pdf` | Hereth Correia and Pöschel, "The Teridentity and Peircean Algebraic Logic," 2006 |
| `Two_Instances_of_Peirces_Reduction_Thesis.pdf` | Dau and Hereth Correia, "Two Instances of Peirce's Reduction Thesis," 2006 |
| `journal.pcbi.1011465.pdf` | Albantakis et al., "Integrated information theory (IIT) 4.0," *PLOS Comput. Biol.*, 2023 |
| `2109.13186v1.pdf` | Mediano et al., integrated information decomposition (ΦID), arXiv 2109.13186 |
| `3359183.pdf` | Mathur et al., "Dark Patterns at Scale," *Proc. ACM HCI* 3 (CSCW), 2019 |
| `EBSCO-FullText-09_20_2026.pdf` | **Unknown; the top open question for S4.** G6 cites it for Burch's PAL internals (relations-simpliciter, Listing's invariants, hypostatic abstraction) |
| `EBSCO-FullText-09_20_2026-2.pdf` | **Unknown.** G6 cites it for a text whose references include Burch 1991 and Hereth Correia and Pöschel 2004 |

The "probable work" column is inferred from file names and Gemini's use of them, and is unverified.

## Related material in the repo or on Drive, not duplicated here

- The DIAL arm ingested other documents from the same day's work. G7's first report was exported as "Text
  UX and Algorithmacy Evolution"
  ([`../dial_response_algorithmacy/sources/ux_evolution_scriptio_continua.md`](../dial_response_algorithmacy/sources/ux_evolution_scriptio_continua.md));
  its second, "Sci-Fi Interfaces and the Concept of Algorithmacy", is
  [`../dial_response_algorithmacy/corpus/essay.md`](../dial_response_algorithmacy/corpus/essay.md). "Ecological
  Ergonomics of Algorithmacy UXD", "Designing For Algorithmacy Paper Review" and the DIAS topic document sit
  in [`../dial_response_algorithmacy/sources/`](../dial_response_algorithmacy/sources/).
- **D6's source chat.** The DIAL arm lists two share links as unread
  ([`../dial_response_algorithmacy/SOURCE.md`](../dial_response_algorithmacy/SOURCE.md), "Working
  discussion"). Both open one chat, "Advanced Sci-Fi Systems Analysis Frameworks" (six turns, about 17,000
  words), whose sixth turn produced D6. `sources/capture_gemini_share.py` captures it; it belongs to the DIAL
  arm and is not ingested here.
- Two Docs from 20 September concern interface design for algorithmacy rather than the reduction argument
  and were left out: a PHD1750 paper proposal ("I want to do a paper that argues that since algori…") and
  "Algorithmacy UI Research Bibliography".
- Two earlier documents by the author bear on the argument and are not Gemini material: "Beyond the dyad:
  the triadic structure of algorithmacy" (April 2026) and "CMR – Algorithmacy: Defining a Competency for
  Triadic Coordination" (May 2026). The argument and script phases should read them first.

## Still missing

| item | why it matters | route |
| --- | --- | --- |
| NotebookLM artifact (notebook `1ac1a3d7…`, artifact `52042b1b…`) | An artifact is a Studio output inside a notebook — a report, deck or audio overview. It may be the source of G6's ten pasted reviews or a precursor of P1 | Needs the author's Google sign-in: reconnect Claude in Chrome, or export or paste it |
| The "Triads" file | G3 and G4 rest their HCI claim on it; G6 places D1's bibliographic audit in it; D4 gives it three tabs whose headings match D1, D3 and D2. No Drive document carries the name, so it is probably the Project's own name or a notebook | Ask the author |
| The chats behind D1, D4, D5 and P1 | D1 is a Deep Research report whose `[span_N]` anchors cannot be tied to its works cited without the chat; D4, D5 and P1 lack their prompts | Share links from Gemini |
| Origin of G5's pasted repository "deep dive" and G6's ten pasted reviews | P1's slide 7 and eighth answer take lane numbers and verdict strings from the deep dive; the reviews carry claims about Quine, Koshkin and Dau | Ask the author |
| The Project's installed instructions and name | G1 is only a suggestion; what actually steered G3, G5, G6 and P1 is unknown | Screenshot or paste from Gemini |
| Web-source lists for the G2, G4 and G7 reports | The share pages keep only the footnote numbers, and the Docs exports carry no lists | Re-open the reports in Gemini if a citation matters |
| A byte-exact P1 | The paste was captured as received | Re-export from Gemini if exact wording matters |

## What the lab already holds

The argument does not start from these sources. The lab's Peirce paper
([`org_frontier/thinkers/peirce/paper.md`](../../org_frontier/thinkers/peirce/paper.md), probes
#374–#378) and Simmel paper ([`org_frontier/thinkers/simmel/paper.md`](../../org_frontier/thinkers/simmel/paper.md),
#369–#373) carry the exact-Φ results the talk will use, and both are registered in `ci/reproduce.json`.
Where a Gemini source contradicts those results, the claims register logs the contradiction; the source
file stays as captured.
