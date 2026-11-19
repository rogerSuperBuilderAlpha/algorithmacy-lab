# S7 hand-check, batch 1 (Fable, 2026-11-08)

> [Written by Fable, S7, run pta-lib-2026-11.]

Nineteen cards, allison2011more to coleridge1817biographia. I read each card against its folder under
`~/iit-playground/pt_ai_animation_local/pdfs/<key>/`, recomputed every sha256, and matched every quotation
against a per-page `pdftotext` extraction of the held PDF (quote marks, ligatures and line-end hyphens
folded). The Coleridge scan's OCR garbles eight of its eleven quotations, so I checked those against the
page images (`pdftoppm`, PDF pp. 311, 312, 321, 322, 458, 573) and the two title pages (pp. 9, 309). The
inbox was empty. Verdicts: 16 index, 3 index after fix, 0 hold. Full-text and partial cards: 106 of 106
quotations found.

**Status note for the author.** The brief allows `status: cited` only where SOURCE.md, SKETCH.md or a
ruling names the work. SKETCH names Bernini, Cleland and Coleridge; Checkpoint rulings name Bongard & Levin
(A1) and Clark & Fischer (B2). Eight cards carry `cited` on the strength of the Checkpoint B approval table
alone (allison, arora, auslander, bedau2003, bedau2010, boge, burtnyk, chollet), while four on the same
footing carry `candidate` (bich, bommasani, catmull, coeckelbergh). Either reading is defensible; the cards
disagree with each other. I changed none of them. Decide whether the "Approved" rows count as rulings, and
the twelve statuses follow.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| allison2011more | metadata | 0/0 | index | nothing | c9 use rests on the triage's credit reading; status note |
| arora2024proxy | full_text | 11/11 | index | nothing | status note |
| auslander2022liveness | metadata | 0/0 | index | nothing | book unopened; status note |
| bedau2003artificial | metadata | 0/0 | index | nothing | restore "M. A." only from a byline; status note |
| bedau2010living | abstract | 0/0 | index | nothing | c4, c12 tentative until read; status note |
| bernini2025ai | abstract | 0/0 | index | nothing (filled empty Hand-check heading) | possible c7 tag ("phenomenological opacity") needs the text |
| bich2018is | metadata | 0/0 | index | nothing | philsci-archive accepted-version PDFs (12895, 12988) untried |
| boge2022two | full_text | 16/16 | index | nothing | status note |
| bommasani2021on | partial | 12/12 | index | nothing (filled empty Hand-check heading) | §§4.3, 4.5 unread by anyone |
| bongard2021living | full_text | 16/16 | index | nothing | nothing |
| bottazzigrifoni2025bewitching | full_text | 13/13 | index | nothing | nothing |
| burtnyk1976interactive | abstract | 0/0 | index | nothing | status note (vs. catmull, candidate) |
| catmull1978problems | metadata | 0/0 | index | nothing | status note (vs. burtnyk, cited) |
| chollet2019on | partial | 13/13 | index after fix | object_read "65 pp." → "64 pp." | card adds c3 beyond DECISIONS's c5, c11; status note |
| clark2023social | abstract | 0/0 | index after fix | added sha256 of crossref.json and openalex.json to object_read | role anchor vs contrast; lab-criterion test needs the text |
| cleland2002defining | metadata | 0/0 | index | nothing | SKETCH names Cleland alone for a two-author article; which Cleland work is meant? |
| cleland2019quest | metadata | 0/0 | index | nothing | book unopened; "theory, not definition" still unverified |
| coeckelbergh2021time | full_text | 14/14 | index | nothing | card argues the fit is c2 (and c7), not c4/c6; retag? |
| coleridge1817biographia | partial | 11/11 (by page image) | index after fix | Caution "618 form feeds" → "626" | SKETCH line 99 "(unverified)" can come off; "Ballads ;" spacing; no OL record or provenance.txt |

Checks beyond the quotations, in brief: every APA string matched its record (authors, year, title, venue,
volume, issue, pages, DOI); every `read_depth` matched what the folder holds; every `object_read` now
carries a sha256 that I recomputed; `Loci` is None on every metadata and abstract card; the Checkpoint B
rulings are met where they apply (clark2023social records what the abstract makes of its third party;
no c12 gap card sits in this batch). Page counts from `pdfinfo`: arora 19, boge 33, bommasani 214,
bongard 15, bottazzigrifoni 33, chollet 64, coeckelbergh 16, coleridge 626.
