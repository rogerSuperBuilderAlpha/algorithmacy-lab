# Pick-up card verification (S10e)

Run `ot-oq-2026-11`, stage S10e, 22 November 2026. Verifier: Claude Opus 5.5, who did not write the cards. I checked each of the 19 cards in `pickup/cards/` against its Crossref record (fetched 22 Nov 2026, User-Agent `research-library-client/1.0`), or against the work's own title page or landing page where there is no DOI. I confirmed each citation of the OT article in the reference list of the text or, for abstract-only cards, in the Crossref or OpenAlex reference list. I located every quotation in `citing/pdfs/<key>.txt`; where the layout-mode text splits columns (alishani2025, choroszewicz2026), a plain `pdftotext` re-extraction of the same PDF served to confirm the quotation. Corrections are made in place and marked `[S10e: …]`; each card ends with a `## Verification` section.

Totals: 19 cards; 7 verified, 12 verified_with_corrections, 0 problems. Quotations checked 149, corrected 7 (five on gulbrandsen2025, one each on chao2026 and zelles2026). One classification changed (ivarsson2026). Four read depths changed from full to partial.

| card | quotes checked / corrected | classification change | verdict | note |
|---|---|---|---|---|
| akhil2026 | 3 / 0 | none | verified | abstract only; citation from OpenAlex referenced_works |
| aleksic2026 | 6 / 0 | none | verified | |
| alishani2025 | 9 / 0 | none | verified | |
| avnoon2026 | 13 / 0 | none | verified | six in-text citations confirmed |
| bujold2026 | 15 / 0 | none | verified | answers (3) supported within its stated scope |
| chao2026 | 9 / 1 | none | verified_with_corrections | card paraphrase stood in quotation marks |
| choroszewicz2026 | 12 / 0 | none | verified_with_corrections | issue 43(2) added; depth full → partial |
| decius2026 | 17 / 0 | none | verified_with_corrections | Crossref gives no container; "SSRN Electronic Journal" removed |
| dowsett2026 | 4 / 0 | none | verified | |
| gulbrandsen2025 | 6 / 5 | none | verified_with_corrections | all four page locators one page low; one paraphrase in quotation marks |
| hall2025 | 1 / 0 | none | verified | metadata only; Crossref ref049 |
| hubert2025 | 8 / 0 | none (takes_up on 2 is borderline, kept) | verified_with_corrections | nine in-text citations, not eight; depth full → partial |
| ivarsson2026 | 2 / 0 | 6: takes_up → answers (abstract) | verified_with_corrections | the card's own Caution already said "answers"; now consistent with akhil2026 |
| johnsson2026 | 7 / 0 | none | verified | |
| phillips2026 | 14 / 0 | none | verified_with_corrections | three in-text citations, not four |
| rikala2025 | 8 / 0 | none | verified_with_corrections | eleven in-text citations, not nine; depth full → partial |
| steiger2026 | 5 / 0 | none | verified_with_corrections | issue 36(1) added; depth full → partial |
| zelles2026 | 7 / 1 | none | verified_with_corrections | "communicate" remark at pp. 10, 12, 16, not p. 17 |
| zientara2026 | 3 / 0 | none | verified | abstract only |

## Knock-on edits for the batch reports (not made here)

- `PICKUP_P1.md` quotes Gulbrandsen and Just at "p. 162" and "p. 161"; the correct pages are 163 and 162.
- `PICKUP_P2.md`, candidate 6, lists ivarsson2026 under "Take it up"; the card now classes it answers (abstract only).
