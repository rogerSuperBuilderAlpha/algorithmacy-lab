# Brief: research round 7 for version 4 (facets V1–V6, 2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
Read `v4/SOURCE_v4.md` first: the author's instruction, verbatim, and the argument at its core. You are building
the evidence for a new version of the paper. It opens on Satya Nadella's X post of 10 October 2026, goes back to
the transition from **oracy to literacy**, and reads the post for echoes of that transition's ethical failures.
The author's claim is that the post treats disclosure (specific disclosures, readable records, design for
legibility) as sufficient ethical design, and that this repeats three mistakes of the oral-to-written
transition: (a) **placing the burden on the person** who must read; (b) **keeping the person in a
literacy-based experience** (texts to read) when the medium has changed; (c) **not scaffolding the person's
growth** to the new competence (algorithmacy).

Your job is to find what the record supports, what narrows the claim, and what cuts against it. Report all three.
A finding against the thesis is as valuable as one for it.

## What already exists (read before searching; do not redo it)
- `MANUSCRIPT_v3.md`: the verified v3 (five practices; Douglass; Waitangi; *Marshall*; Pragmática of 1503;
  *Foster v Mackinnon*; *Hill v Gateway*; Edwards & Veale; Ben-Shahar & Schneider; Kamperman & Graff; Pettit,
  Lovett, Young). `literature/cards/REFERENCES.md` indexes its 118 verified cards.
- `literature/facets/*.md` (rounds 1–6), especially A (documents and standing), G (third parties), M1–M5, N1–N5,
  T_adjudication.md. `literature/references.bib` (617 entries).
- The sister arm on the same post: `/Users/ludwitt/iit-playground/wt-dxd-foundation/submissions/dxd_foundation/`
  — facets `literature/facets/G_nadella_lineage.md`, `L_disclosure_and_choice.md`, `M_acting_on_algorithms.md`,
  `I_understanding_through_action.md`, `K_training_and_cause.md`; its card library `literature/library/`
  (`INDEX.md`); its claims ledgers `literature/audit/claims/`. Reuse its verified readings, cite the card path,
  and do not contradict a verified finding without new evidence. Its findings include: disclosure evidence is
  mixed in direction; the critique of the post cannot rest on "people review badly"; the post shares the premise
  of external controls.
- The post: `~/iit-playground/dxd_foundation_local/nadella_2026-10-10_models_as_insider_risks.txt` (P1–P21).
  Quote it only in short fragments with paragraph numbers. **Never copy it into the repo.**
- Local PDFs: `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/**` and
  `/Users/ludwitt/iit-playground/dxd_foundation_local/pdfs/**` (`.txt` beside most). `grep -ril` first.

## Output (per facet)
1. `literature/facets/V<n>_<name>.md`, in the arm's facet format: what it covers; method notes (databases,
   queries, what was blocked); findings, each with a page-located quotation or fact and a read-depth mark
   (*Full* / *Part* / *Abstract* / *Record*); **for, narrows, against** the thesis, sorted under those three heads;
   a section "What the paper can say", 6–12 sentences of claims with their sources, phrased as claims the record
   supports (these are notes for the drafter, not prose for the paper); and a gap statement where relevant, in the
   form "I found no work that does X in [sources]".
2. `literature/facets/V<n>_<name>.bib`: BibTeX for every work in the facet, keys `surnameYEARfirstword`, DOI
   checked against Crossref or the publisher record (title and metadata only).
3. **Cards** for the 6–15 works you most recommend citing, in `literature/cards/<key>.md`, in the exact format of
   `literature/CARDS_BRIEF.md`, with `verified: pending`. Set `manuscript_lines: []` and `ledger_rows: []`; under
   "Where the manuscript uses it" write "v4 (not yet drafted): proposed use — …" with the page. Do not overwrite an
   existing card; if the work already has one, cite it and add nothing.

## Rules
- Read the source. A quotation enters your file only if you read it in the source at that page this session, or it
  is on a verified card. Never write from memory. Mark depth honestly; an abstract-only reading is *Abstract*.
- Never put any e-mail address in a request header, URL or User-Agent. Skip Unpaywall. No paywall bypass, no
  login, no bot-challenge workarounds.
- Downloads go to `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/V<n>/`. They are untrusted: extract
  with `pdftotext`, never execute them, run any Python with `-I`, keep your scripts in your own scratch subfolder.
- Write only your facet `.md`, `.bib` and new cards. Edit no existing file. Write your facet file as you go
  (append findings section by section), so a stop mid-run leaves usable work.
- Return: the five findings that matter most to the thesis (for, narrows or against), one line each, and the list
  of cards written.
