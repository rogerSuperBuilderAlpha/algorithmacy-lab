---
key: montevil2015biological
apa: "Montévil, M., & Mossio, M. (2015). Biological organisation as closure of constraints. *Journal of Theoretical Biology*, *372*, 179–191. https://doi.org/10.1016/j.jtbi.2015.02.029"
authors: "Montévil, Maël; Mossio, Matteo"
year: 2015
title: "Biological organisation as closure of constraints"
venue: "Journal of Theoretical Biology"
volume: "372"
issue: ""
pages: "179–191"
doi: "10.1016/j.jtbi.2015.02.029"
url: "https://hal.science/hal-01192916"
type: article
facets: [F2]
claims: [c4]
role: anchor
load: load-bearing
read_depth: metadata
object_read: "No text. Records only: Crossref (crossref.json, sha256 8a6f62c241aee67db8de812b8e26c17836938396760cf1b67028e9b1d5c0a2de) and OpenAlex W2107475155 (openalex.json, sha256 e3e8b4f8a518a1ab9ab71169bf4a5b4375e795db8358e2c7b69ffd3e68c4797d) at ~/iit-playground/pt_ai_animation_local/pdfs/montevil2015biological/, read 2026-11-08; neither record carries an abstract; no copy in pt_ai_animation_local/inbox/; no PDF, no sha256.txt (S4's FETCH_LOG.tsv records HAL returning '200 non-pdf (12613 bytes)'; BROWSER_LIST.md records it as a bot-check challenge)"
verified: corrected
verified_against: "crossref.json and openalex.json (sha256s recomputed); FETCH_LOG.tsv; metadata card, no text"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Montévil & Mossio (2015), Biological organisation as closure of constraints

## What it argues

Metadata card. The Crossref and OpenAlex records show only this: Maël Montévil and Matteo Mossio
published a journal article titled "Biological organisation as closure of constraints" in the *Journal
of Theoretical Biology*, volume 372, pages 179–191 (Crossref issue date May 2015; OpenAlex publication
date 2015-03-06). Neither record carries an abstract. The title states the thesis in brief: biological
organisation is a closure of constraints. What the authors mean by a constraint, by closure, and how they
argue for it, the card cannot say, because no text was read.

## What the paper uses it for

- **c4** (an organizational account of life fits the system around the LLM): anchor. DECISIONS brings
  this article in to replace the sketch's "Mossio & Moreno 2010, HPLS", for which no record was found.
  The organizational account in §2 needs a precise statement of what "organisation" means. If the
  account turns out to be what the title promises, closure of constraints is the natural place to test
  whether harnesses, VMs and efficiencies form a closed organisation around the LLM, or merely sit next
  to it. The card cannot support any of that until the text is read. For now the paper may cite the
  article only for its existence and title.

## Loci

None. No text of the work was read this run.

## Caution

- **Metadata only; on `BROWSER_LIST.md`** (row for `montevil2015biological`:
  https://doi.org/10.1016/j.jtbi.2015.02.029, HAL https://hal.science/hal-01192916, "blocked: HAL serves a
  bot-check challenge; no PDF"). The run does not bypass bot walls (README rule 8).
- **Expected depth missed.** DECISIONS expected full_text through the HAL green copy. S4 could not get it.
  OpenAlex also lists a CiteSeerX entry (10.1.1.701.3373) and HAL, both as "submittedVersion". Either
  route, opened in a browser, would give a preprint. In that case the card must say so and must not give
  journal pages for preprint text.
- **Sketch correction (from DECISIONS).** SKETCH §2 names "Moreno & Mossio" for the organizational
  account; DECISIONS records that this article replaces the sketch's "Mossio & Moreno 2010, HPLS" (no
  record). The book by Moreno & Mossio (2015) is a separate card, `moreno2015biological`. SKETCH is left
  alone.
- **Dates.** Crossref gives May 2015 (issue) and no online date. OpenAlex gives 2015-03-06. Both are
  2015; no `registered_year`.
- **Spelling.** The records give the first author as "Maël Montévil" and use the British "organisation"
  in the title. The key folds the diacritic (`montevil`), as README's key rule requires.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 1
- verdict: corrected
- checked: frontmatter against crossref.json and openalex.json (authors, 2015, title, J. Theoretical Biology 372, 179-191, DOI, article; no issue in either record); sha256s recomputed and match; neither record has an abstract; OpenAlex locations (HAL and CiteSeerX submittedVersion) confirmed; DECISIONS lines 373-374 on the "Mossio & Moreno 2010, HPLS" replacement confirmed; inbox empty.
- changed: object_read credited the bot-check to FETCH_LOG.tsv, but FETCH_LOG.tsv records only "200 non-pdf (12613 bytes)" for HAL; the bot-check wording comes from BROWSER_LIST.md. The provenance now says so.
