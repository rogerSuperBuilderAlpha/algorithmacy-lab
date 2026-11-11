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
