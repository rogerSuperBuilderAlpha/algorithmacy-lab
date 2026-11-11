# QUOTE_CHECK — misses traced by hand (S8, 2026-11-05)

> [Built by Claude, 2026-11-05.] `QUOTE_CHECK.md` is generated and not edited. This file records the
> hand trace of every row it marks `not-found`.

First pass: 134 not-found, nearly all in two-column PDFs whose `-layout` text layer interleaves
columns (the S7 batches flagged this). I added a reading-order extraction (`<key>.readorder.txt`,
`pdftotext` without `-layout`) beside each of the 26 held PDFs in the local store, outside the repo.
Second pass: 17 not-found. Each traced:

| key | rows | cause | quotation stands? |
|---|---|---|---|
| tan2026impact | 10 | text-only copy (no PDF to re-extract); columns interleave and hyphens break words ("laten- cies"). Each start fragment found in the de-hyphenated text; the three longest are split mid-phrase by the other column ("adopted a cue-free interface, omitting progress indicators"; "(such as hesitation, slowed pacing, or staged disclosure of output)") | yes |
| cameron2024social, shi2026siren, stark2024animation, subramonyam2024bridging | 1 each | line/page break inside the quotation; found with whitespace collapsed | yes |
| maier2022no | 1 | sentence runs across the page break and footnote; the card says so | yes |
| maier2022no, stanton2006distributed | 1 each | parser took card prose as a quotation ("…page footers (", "missing; I quote from") | n/a |

Result: 0 quotations unsupported by the held text.

## Run 2 (`dxda-lib-2026-11b`, 2026-11-11)

[Written by Claude (Opus 5.5, lead).] `tools/quote_check.py` run on the 13 run-2 cards that carry loci
(the two abstract cards, `leveson2000intent` and `vaithilingam2025semantic`, have none). It printed
results to the terminal and did not rewrite `QUOTE_CHECK.md`. Totals: 189 found, 2 found-nospace, 3
found-partial, 5 not-found. I traced every one of the ten that were not a plain "found".

| card | n | why | supported? |
|---|---|---|---|
| lasseter1987principles, takayama2011expressing | 1 each | found-nospace: words letter-spaced for emphasis ("w h y", "w h a t") or a line break inside the quotation | yes |
| lewis2026invisible, may2003using, ribeiro2012illusion | 1 each | found-partial: the quotation crosses a page break, a figure caption or the arXiv side stamp; each card or verifier says so | yes |
| ribeiro2012illusion | 2 | not-found: the abstract's two columns interleave in both text layers, and "Disney" carries a trademark sign; the S6 verifier read both sentences on the page image | yes |
| gonzalez1996does | 1 | not-found: the scan's OCR reads "riot" for "not"; the S6 verifier read the sentence on the page image | yes |
| thomas2001applying, hoerl2015seeing | 1 each | parser took a verifier's note or a locator note as a quotation | n/a |

Result: 0 run-2 quotations unsupported by the held text. In addition, the lead re-found by hand every
locus that `../DRAFT_v1.md` quotes (scratchpad check, 2026-11-11), including Stark p. 1667 across the
page footer and Tan §5.5 in the arXiv text.

`tools/check_dois.py` on the 14 run-2 cards with DOIs: 14 ok, title match 1.00 for each. It printed
results and did not rewrite `DOI_CHECK.md`.
