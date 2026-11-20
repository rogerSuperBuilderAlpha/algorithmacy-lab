# F follow-up log — records, upgrade and new cards after ADJUDICATION

Agent-drafted (F drafter, opus, 2026-11-19). The author has not reviewed it and none of the text is his. One line
per search and per source, appended as the run goes. Client name on every request: `research-fetch/1.0`; no
e-mail, key or cookie sent. Local files under `~/iit-playground/berthon_ethics_local/run_2026_11/F/<citekey>/`.

| time | query or URL | result | status |
|---|---|---|---|
| 09:11 | https://api.crossref.org/works/10.17763/haer.52.3.77p7168115610811 | 200; title, Levine, 1982-09, HER 52(3) 249-266 match; no abstract; saved crossref.json | - |
| 09:11 | https://api.openalex.org/works/doi:10.17763/haer.52.3.77p7168115610811 | 200; abstract (inverted index); oa_status closed; saved openalex.json | - |
| 09:11 | https://doi.org/10.17763/haer.52.3.77p7168115610811 | 200, harvardeducationalreview.org/content/52/3/249; abstract on page; saved publisher.html | - |
| 09:12 | https://www.harvardeducationalreview.org/content/52/3/249.full.pdf | redirected to the abstract page (subscriber-only); copy deleted, no further attempt | - |
| 09:11 | https://api.crossref.org/works/10.1080/096145249100077481 | 200; title, Sandiford et al., 1994-01, Development in Practice 4(1) 35-49 match; no abstract | - |
| 09:11 | https://api.openalex.org/works/doi:10.1080/096145249100077481 | 200; abstract; oa_status closed; saved openalex.json | - |
| 09:11 | https://doi.org/10.1080/096145249100077481 | 403 challenge page at tandfonline.com, not bypassed; saved as publisher.html for the record | - |
| 09:11 | https://api.crossref.org/works/10.1017/s0020743811000900 | 200; title, Yılmaz, 2011-11, IJMES 43(4) 677-697 match; abstract in record | - |
| 09:11 | https://api.openalex.org/works/doi:10.1017/s0020743811000900 | 200; same abstract; oa_status closed | - |
| 09:11 | https://doi.org/10.1017/s0020743811000900 | 200, cambridge.org/core abstract page; same abstract; full text behind access; saved publisher.html | - |
| 09:20 | task 1, levine1982functional | record and abstract saved; card brought to the saved publisher page; stays abstract-only | DONE levine1982functional |
| 09:20 | task 1, sandiford1994nicaraguan | record and abstract (OpenAlex) saved; publisher page bot-walled; stays abstract-only | DONE sandiford1994nicaraguan |
| 09:20 | task 1, yilmaz2011learning | record and abstract saved (Crossref and Cambridge page agree); stays abstract-only; one Summary verb softened to the abstract | DONE yilmaz2011learning |
| 09:13 | search ~/iit-playground/berthon_ethics_local/ for Copilot terms | two copies on disk, pdfs/nadella/N1/ms_copilot_consumer_terms/page.html and pdfs/nadella/R2/ms_copilot_terms/page.html, same sha256 1c77b8d3…; "Effective: August 18, 2026"; indemnity sentence present in "Important disclosures & warnings" | - |
| 09:14 | https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse | live recapture, 200; still "Effective: August 18, 2026"; indemnity and "solely responsible" sentences unchanged; saved to F/microsoft2026copilot/ (sha256 4353cb5c…) | - |
| 09:25 | task 2, microsoft2026copilot | upgrade card written from the on-disk copy, supersedes the library card | DONE microsoft2026copilot |
| 09:14 | search ~/iit-playground/berthon_ethics_local/ for the two OJ texts | Reg. 2024/1689 at pdfs/nadella/N4/aiact/32024R1689.txt (sha256 d89a8a4d…, the copy behind eu2024aiact); Reg. 2026/1744 at pdfs/nadella/N4/omnibus/32026R1744.txt (sha256 139b2b57…, the copy behind euomnibus2026); R2 and B0 hold further copies (XHTML identical by sha256 to N4) | - |
| 09:15 | text search of 32024R1689.txt and 32026R1744.txt | art. 26(11) at line 1037, art. 26 under Chapter III, Section 3; original art. 113; Omnibus art. 1 point (40)(b) and recital 40; Omnibus text contains no "Article 26" | - |
| 09:28 | task 3, euaiact2026dates | new card from the two OJ texts on disk; no fetch | DONE euaiact2026dates |
| 09:15 | https://www.govinfo.gov/content/pkg/STATUTE-89/pdf/STATUTE-89-Pg400.pdf | 200; Pub. L. 94-73, 89 Stat. 400; sha256 c936564b… identical to the A2 copy | - |
| 09:15 | https://www.govinfo.gov/content/pkg/STATUTE-84/pdf/STATUTE-84-Pg314.pdf | 200; p. 314 only (sha256 62ced17e…) | - |
| 09:16 | https://www.govinfo.gov/link/statute/84/314?link-type=pdf | 200, STATUTE-84-Pg314-2.pdf; Pub. L. 91-285 through 84 Stat. 319; sha256 08d0c0cf… identical to pdfs/D/st84_c.pdf; s. 201 as added in 1970 at 84 Stat. 315 | - |
| 09:17 | https://www.govinfo.gov/link/uscode/42/1973aa?year=1994&link-type=html | 200, USCODE-1994-title42 … sec1973aa.htm; official compilation of s. 201 with credits: added by Pub. L. 91-285 s. 6, amended by Pub. L. 94-73 s. 102 only | - |
| 09:32 | task 4, uscongress1975section201 | new card on s. 201 as it stood after the 1975 amendments, from the two Statutes at Large prints and the 1994 Code | DONE uscongress1975section201 |
| 09:18 | grep literature/CARD_INDEX.md and literature/cards for gadeke2020mugger | card at literature/cards/berthon_ethics_paper/gadeke2020mugger.md; source_basis partial-text; verified pending | - |
| 09:18 | ~/iit-playground/berthon_ethics_local/pdfs/nadella/R3/gadeke2020/gadeke2020.pdf | on disk; sha256 0ee9d676… matches the card; all 17 quoted strings in the card string-match gadeke2020.txt (page locators not re-checked) | - |
| 09:33 | task 5, gadeke2020mugger | source already on disk, so no fetch and, per the brief, no upgrade card; the card awaits the lead's verifier and Fable read | DONE gadeke2020mugger (no new card) |
