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
