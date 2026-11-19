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
