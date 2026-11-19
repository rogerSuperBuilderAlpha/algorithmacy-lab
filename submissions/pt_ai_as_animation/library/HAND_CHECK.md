# HAND_CHECK — S7, run pta-lib-2026-11

> [Built by Claude, 2026-11-08.] Fable read every card against its source folder in four batches
> (brief: `hand_check/BRIEF.md`). The batch files below are concatenated unchanged.

**Result: 79/79 cards hand-checked. 67 index, 12 index after fix (each change marked
"[Corrected by Fable, S7]" in the card), 0 hold.** Quotations traced on the stated pages: batch 1
106/106, batch 2 109/109, batch 3 113/113, batch 4 118/118. Every sha256 recomputed and matched.

## Follow-up done by Claude after S7

- Saved to key folders the records the hand-check found only in scratchpads or missing:
  Open Library for `tillis1992toward`, `williams2001animators` (no folder existed), `tomko2015beyond`;
  OpenAlex for `hayesroth2006puppetry`, `hooks2023acting`; Crossref for the Hooks chapter
  (10.4324/9781003289753-4), Dennett 1991 *J. Phil.* (10.2307/2027085) and `dorin2024what`.
  Each folder's `provenance.txt` says so.
- Still owed: the Wikisource revision for `kleist1972on` (batch 3 refetched it and matched the hash,
  but did not deposit it).

## For the author (merged from the four batches; S10 carries these to Checkpoint D)

1. **`cited` vs `candidate` is applied inconsistently.** README ties `cited` to SOURCE.md, SKETCH.md
   or a ruling. Batch 3 moved four cards to `candidate` (park, popa, schaeffer, scholl); batches 1, 2
   and 4 left about 27 cards `cited` on the DECISIONS approval alone. One rule for the run is needed:
   does an approved slot count as a ruling?
2. **The sketch cites Sculley through Paleyes, but the sentence is not in Paleyes et al.** Open
   Sculley 2015 (BROWSER_LIST) or drop the sentence.
3. **`popa2021human` carries c9 but is unread**, so it cannot meet ruling B2. Open it or drop c9.
4. **Gap cards read ruling B1 differently** (`rolla2026embodiment` candidate, `masumori2026openlife`
   cited). Pick one status for both.
5. **`duran2018grounds` reads essential opacity as practical**, weaker than SOURCE's "in principle
   black box". Decide which reading §4.2 means.
6. **SKETCH errors, recorded on the cards and not edited:** "about 70 definitions" belongs to
   `legg2007collection`; Thomas & Johnston's title is reversed; "Maturana & Varela" fits the 1980 book,
   not Varela et al. 1974; Coleridge's "(unverified)" can come off (Vol. II p. 2); `cleland2002defining`
   has two authors; `magee2023structured` is not named in SKETCH although CITED_WORKS says it is.
7. **Unread anchors still waiting on the browser:** Moreno & Mossio (first), Govind (Zenodo download
   settles the byline and key), Machery, Maturana & Varela, Montévil & Mossio, Meincke, Humphreys,
   Lasseter, Kaplin, Purves, Silvio ch. 1, Walton, Trifonov, von Eschenbach, Zerilli 2019, Popa.
8. Smaller items (retags, initials, Early View page mapping, preprint locators) are in the part
   files below.


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

# S7 hand-check, part 2 (run pta-lib-2026-11)

> [Written by Fable (Claude), 2026-11-08, batch 2 of the S7 hand-check; follows hand_check/BRIEF.md.]

Twenty cards read against their key folders in `pt_ai_animation_local/pdfs/`, the records there, and
SOURCE.md, SKETCH.md, FACETS.md and triage/DECISIONS.md. `inbox/` was empty. Every quotation in the nine
full-text cards was searched in the page text that its locator names (`pdftotext -f N -l N`), with
line-break, hyphenation, ligature and inner-quote differences allowed: 109 of 109 found. Every abstract
card's quoted phrases were found verbatim in the record they cite. Every sha256 the cards give was
recomputed with `shasum -a 256` and matched. Where a record sat only in a writer's scratchpad (Hayes-Roth
and Hooks OpenAlex abstracts, the Hooks chapter record, the Dennett 1991 *J. Phil.* record) I re-fetched
it live on 2026-11-08 into my own scratchpad; the sha256s came out identical to the cards' and the fields
matched. Those records are still not in the key folders.

Verdicts: 17 index, 3 index after fix (fixed here), 0 hold.

One run-wide point for the author, not fixed in any card: ten of the twenty cards carry `status: cited`
although SOURCE.md and SKETCH.md name none of those works (README: cited = SOURCE.md or SKETCH.md uses it).
S5 seems to have read "cited" as "the sketch's section uses the claim". The ten are marked in the table.
Dennett 1987 (SKETCH §2), Floridi 2023 (ruling A1) and Govind (ruling A2) are named and keep `cited`.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| crafton2012shadow | metadata | 0/0 (None) | index | nothing | `cited` though SOURCE/SKETCH do not name Crafton; `anchor` at metadata depth |
| creel2020transparency | abstract | 0/0 (None); 4 abstract phrases verbatim | index | nothing | `cited` not supported by SOURCE/SKETCH; PhilSci-Archive accepted version would raise it to full_text |
| dennett1987intentional | metadata | 0/0 (None) | index after fix | object_read and Caution said no key folder existed; the folder now holds the three Open Library records (sha256s match); rewritten | nothing |
| dennett1991real | metadata | 0/0 (None) | index | nothing | *J. Phil.* record still not in the key folder (re-fetched live, matches); `cited` rests on SKETCH naming the stance, not this article |
| dipaolo2005autopoiesis | metadata | 0/0 (None) | index | nothing | `cited` not supported by SOURCE/SKETCH |
| dorin2024what | full_text | 13/13 | index | nothing | `cited` not supported by SOURCE/SKETCH; no Crossref record saved in the folder |
| duran2018grounds | full_text | 11/11 | index | nothing | `cited` not supported by SOURCE/SKETCH; decide whether §4.2's opacity is in-principle (SOURCE) or practical (this source) |
| floridi2023ai | full_text | 13/13 (one across pp. 5–6, checked by hand) | index | nothing | nothing |
| floridi2025ai | full_text | 14/14 | index | nothing | ruling A1 names it; `candidate` could become `cited` |
| floridi2026ai | full_text | 10/10 | index | filled the empty Hand-check heading | nothing |
| froese2009enactive | metadata | 0/0 (None) | index | nothing | S8: `registered_year` for the 2008 online date? |
| gao2009psychophysics | full_text | 9/9 | index after fix | paraphrase "falls to chance past about 30°" corrected to the text's result (above 60% only at 0° and 30°; chance at 120° and 150°, §2.3) | `cited` not supported by SOURCE/SKETCH |
| gerrig1993experiencing | abstract | 0/0 (None); 3 description phrases verbatim | index | nothing | `cited` not supported by SOURCE/SKETCH |
| govind2026illusion | abstract | 0/0 (None); 9 abstract phrases verbatim | index | nothing | download v1.0 from Zenodo into inbox/ (settles byline, key and depth); record keywords look misattached |
| green2000role | abstract | 0/0 (None); Ns and experiment numbers match | index | nothing | `cited` not supported by SOURCE/SKETCH |
| gubelmann2024large | full_text | 12/12 | index | filled the empty Hand-check heading | nothing |
| hayesroth2006puppetry | abstract | 0/0 (None); 4 abstract phrases verbatim in live OpenAlex record | index | nothing | S4 should save the OpenAlex record to the folder; given name unconfirmed |
| hoerl2015seeing | full_text | 16/16 | index | nothing | `cited` not supported by SOURCE/SKETCH (FACETS upgrade); EV→issue page mapping inferred, confirm before citing pages |
| hooks2023acting | abstract | 0/0 (None); abstract and chapter record re-fetched, match | index | nothing | S4 should save the OpenAlex and chapter records to the folder |
| howdle2026anthropomorphising | full_text | 11/11 | index after fix | thesis quotation restored to SOURCE's spelling "better concieved [sic]" | writer added facet F3 to DECISIONS' F12; kept, drop if DECISIONS governs |

Ruling checks. B1 (c12 gap cards in this batch: govind2026illusion, hayesroth2006puppetry): both say what
separates the source from "AI development as a craft of animation, argued as a claim about what AI is"
(Govind: the parallel proves AI is illusion; Hayes-Roth: puppetry is a limit AI must cross). B2 (c9): no
card in this batch is tagged c9.

# S7 hand-check, batch 3 (run pta-lib-2026-11)

> [Written by Fable (Claude), 2026-11-08.] Twenty cards read against their sources per `BRIEF.md`.
> Every text-layer quotation was grepped against the held `.txt`; where that layer interleaves two
> columns (magee, masumori, park, scholl) I re-extracted the held PDF with `pdftotext -raw` or a
> 306-pt column crop and matched there. Kleist's object is a Wikisource revision, which I refetched;
> its sha256 matches the card. Every PDF and record sha256 was recomputed with `shasum -a 256`.
>
> Verdicts: 15 index, 5 index after fix, 0 hold. Fixes: four `status: cited → candidate` where neither
> SOURCE.md, SKETCH.md, CITED_WORKS.md nor a Checkpoint ruling names the work (park, popa, schaeffer,
> scholl), and one stale `object_read` clause (maturana). Each fix is marked `[Corrected by Fable, S7]`
> in the card's Hand-check section.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| humphreys2009philosophical | metadata | None | index | nothing | unread; a browser copy would let "essential epistemic opacity" be checked before §4.2 leans on it |
| kaplin1999puppet | abstract | None (abstract sentence matches record) | index | nothing | nothing |
| kleist1972on | full_text (German original, web) | 11/11 | index | nothing | text object not in the key folder (S4 owes the wikitext deposit); the cited 1972 translation is unread, so English quotations in the draft must be marked as the card's own |
| lasseter1987principles | abstract | None (3 abstract phrases match) | index | nothing | ACM copy is bronze OA; opening it raises the anchor to full text |
| legg2007collection | full_text | 8/8 | index | nothing | nothing |
| legg2007universal | full_text | 17/17 | index | nothing | SKETCH's "about 70 definitions" belongs to legg2007collection, not this article |
| machery2012why | metadata | None | index | nothing | nothing |
| magee2023structured | full_text (arXiv v1) | 9/9 (held txt interleaves columns; matched on -raw re-extraction) | index | nothing | CITED_WORKS says SKETCH names Magee et al., but the current SKETCH/SOURCE do not; decide whether the card stays cited. Loci unchecked against the SAGE version of record |
| masumori2026openlife | full_text | 14/14 (matched on column-split re-extraction) | index | nothing (filled empty Hand-check heading) | APA omits "(Accepted at ALIFE 2026)" because the text does not state it; cite the arXiv preprint |
| maturana1980autopoiesis | metadata | None | index after fix | object_read: Open Library records are now in the key folder, not scratchpad-only | book unread; author line (Beer) and publisher (Reidel vs Kluwer) wait on the title page |
| meincke2019autopoiesis | metadata | None | index | nothing | the c4 bullet's process-view objection is the library's plan, not the article's; keep it out of the draft until read |
| montevil2015biological | metadata | None | index | nothing | HAL/CiteSeerX copies are submitted versions; moreno card calls this "the open article to quote" but it is metadata too |
| moreno2015biological | metadata | None | index | nothing | first in Fable's reading order (ruling B4); the self-production objection still has no quoted source in the library |
| paleyes2023challenges | partial | 11/11 | index | nothing | "cited" rests on DECISIONS routing SKETCH's Sculley sentence here, and the card shows the sentence is not in Paleyes; promote and read Sculley (2015) or drop the sentence |
| park2023generative | partial | 15/15 (held txt interleaves columns; matched on reading-order re-extraction) | index after fix | status cited → candidate | restore "cited" if §4.1/§6 will cite it; "illusion of life" is Thomas & Johnston's phrase (ref. [96]) |
| popa2021human | metadata | None | index after fix | status cited → candidate | ruling B2 requires a third-party note on every c9 card; this one is unread, so open the article or drop c9 from its claims |
| purves2014stopmotion | abstract | None (6 abstract phrases match) | index | nothing | nothing |
| rolla2026embodiment | full_text | 11/11 | index | nothing (filled empty Hand-check heading) | status candidate here vs masumori reading ruling B1 as "cited"; decide one way for both gap cards. Check SKETCH line 10's "better conceived as creating artificial life" against SOURCE.md |
| schaeffer2023are | partial | 8/8 | index after fix | status cited → candidate | Sculley-vs-Schaeffer slot (ceiling 75) still open |
| scholl2000perceptual | full_text | 9/9 (held txt interleaves columns; matched on reading-order re-extraction) | index after fix | status cited → candidate | restore "cited" if §4.2/§4.3 will cite it; chase Berry et al. (1992), their ref. 53, for the quantized-film result |

# S7 hand-check, batch 4 (run pta-lib-2026-11)

> [Written by Claude (Fable), 2026-11-08.]

Twenty cards, schumann2022machines to zhou2026externalization. Method: for each card with a text layer I
re-extracted the held PDF (or HTML) page by page with `pdftotext`, matched every quotation after joining
line-end hyphens and normalising ligatures, dashes and quotation marks, and recomputed the sha256 of the text
object. For record-only cards I re-read the JSON in the key folder against the frontmatter. Two cards
(tillis1992toward, williams2001animators) and part of a third (tomko2015beyond) rest on Open Library and
Library of Congress records that no key folder holds; I refetched those records on 2026-11-08 into my
scratchpad, matched the content and the hashes the cards give (the editions lists and the LoC page hash
differently today, their content does not), and left the folders alone, since the brief confines me to cards.

**Verdicts: 19 index, 1 index after fix (thomas1981illusion), 0 hold.** Loci: 118/118 found across the eight
cards that quote (14, 14, 8, 15, 12, 10, 15, 15, in order below); the twelve record-only cards have
Loci = None, as the schema requires.

**One batch-wide item for the author.** README defines `status: cited` as "SOURCE.md or SKETCH.md uses it".
In this batch SKETCH names Thomas & Johnston, Trifonov, Maturana & Varela and Zaharia; rulings B1 and B2 name
Sun & Gualeni and Schumann & Du; the Checkpoint B swap names Villalobos & Dewhurst. Nine other cards carry
`cited` on the strength of the Checkpoint B approval alone: shanahan2024talking (SKETCH names a *different*
Shanahan paper, the 2023 *Nature* role-play article), silvio2019puppets, sullivan2022understanding,
voneschenbach2021transparency, wang2024survey, zednik2021solving, zerilli2019transparency,
zerilli2022explaining and zhou2026externalization (the S6 verifier flagged this one). I changed none of them;
decide whether an approved triage slot counts as a ruling, and if not, set them to `candidate`.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| schumann2022machines | full_text | 14/14 | index | nothing | whether this is the main §4.4 foil (card's Caution asks) |
| shanahan2024talking | full_text (arXiv v5, not CACM) | 14/14 | index | nothing | status `cited` rests on a different Shanahan paper in SKETCH; locators are arXiv pages |
| silvio2019puppets | metadata | None | index | nothing | book unopened (ruling 4, second); definition only via Stark; Alexy's role |
| sullivan2022understanding | abstract | None | index | nothing | abstract only; status (header) |
| sun2026between | full_text (author pre-print) | 8/8 | index | nothing | pagination provisional until the Springer chapter is seen; no editors in record |
| thomas1981illusion | metadata | None | index after fix | object_read: records now in the key folder, hashes added [Corrected by Fable, S7] | SKETCH inverts the title vs every 1981 record; principles chapter still unread |
| tillis1992toward | metadata | None | index | nothing | no key folder; S4 to save records; catalogue subtitle "puppetry as a theatrical art": admit or wait for title page |
| tomko2015beyond | abstract (publisher description) | None | index | nothing | Open Library records not in folder; Knight and Mason's role |
| trifonov2011vocabulary | metadata | None | index | nothing | "123 definitions" unverified; live OpenAlex abstract could lift depth |
| varela1974autopoiesis | metadata | None | index | nothing | initials F. G. vs Francisco J.; SKETCH's "Maturana & Varela" fits the 1980 book |
| villalobos2018enactive | full_text | 15/15 | index | nothing | nothing |
| voneschenbach2021transparency | metadata | None | index | nothing | closed; open DOI in browser if c7 cites it; status (header) |
| walton1990mimesis | metadata | None | index | nothing | book unopened (ruling 4, fourth) |
| wang2024survey | partial | 12/12 | index | nothing | status (header) |
| williams2001animators | abstract (LoC blurb) | None | index | nothing | no key folder; S4 to save records; blurb-as-abstract is a convention call |
| zaharia2024shift | full_text (web) | 10/10 | index | nothing | nothing |
| zednik2021solving | partial (arXiv preprint) | 15/15 | index | nothing | preprint pages, VoR unchecked |
| zerilli2019transparency | metadata | None | index | nothing | load-bearing but unread; Cambridge copy is .docx; status (header) |
| zerilli2022explaining | abstract | None | index | nothing | abstract only; status (header) |
| zhou2026externalization | partial | 15/15 | index | nothing | status `cited` (verifier flagged too) |
