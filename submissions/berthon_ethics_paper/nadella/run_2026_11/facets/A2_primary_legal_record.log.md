# A2 log — primary legal and official record

Agent-drafted. One line per search and per source, appended as the run goes.

| time | query or URL | result | status |
|---|---|---|---|
| 20:52 | https://www.govinfo.gov/content/pkg/USREPORTS-380/pdf/USREPORTS-380-145.pdf | official U.S. Reports PDF, pp. 145-156 read in full; record matched on govinfo details page | DONE louisiana1965louisiana |
| 20:58 | courtlistener search API "Davis v. Schnell" | 401, needs a key; not used | SKIPPED auth |
| 20:59 | https://static.case.law/f-supp/81/html/0872-01.html | CAP OCR of 81 F. Supp. 872-881, read in full; record matched in CAP volume metadata | DONE davis1949davis |
| 21:04 | https://www.govinfo.gov/content/pkg/USREPORTS-238/pdf/USREPORTS-238-347.pdf | official U.S. Reports PDF; opinion pp. 354-368 read in full; key reused from references.bib (not in CARD_INDEX) | DONE guinn1915guinn |
| 21:08 | https://www.usccr.gov/files/historical/1961/61-vol1.pdf | 404 | (route failed) |
| 21:08 | https://www2.law.umaryland.edu/marshall/usccr/documents/cr11961bk1.pdf | 424-page GPO scan; pp. 58-67 and 133-142 read | DONE usccr1961voting |
| 21:12 | OpenAlex search "1961 Commission on Civil Rights Report Voting" | malformed response (no results key); record taken from the document's own title page and imprint | - |
| 21:15 | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title52-section10508 | 404 | (route failed) |
| 21:16 | https://www.govinfo.gov/content/pkg/USCODE-2023-title52/html/USCODE-2023-title52-subtitleI-chap105-subchapI-sec10508.htm | govinfo "Page Not Found"; current Code text not opened | (route failed) |
| 21:16 | https://www.govinfo.gov/content/pkg/STATUTE-96/pdf/STATUTE-96-Pg131.pdf | Pub. L. 97-205, 96 Stat. 131-135, read in full; s. 5 adds s. 208 | DONE uscongress1982voting |
| 21:22 | https://www.govinfo.gov/content/pkg/STATUTE-89/pdf/STATUTE-89-Pg400.pdf | Pub. L. 94-73, 89 Stat. 400-406, read in full; bilingual-materials duty and permanent test ban | DONE uscongress1975voting |
| 21:26 | WebSearch "Report on the First General Elections in India 1951-52" Election Commission pdf symbols | discovery: scan on a news organisation's library CDN; JAS review record | - |
| 21:27 | Crossref query.bibliographic "Report on the First General Elections in India 1951-52" | review record Tinker 1956, 10.2307/2941789, confirms title | - |
| 21:28 | https://cdn.downtoearth.org.in/library/0.61706000_1558592806_first-general-elections-in-india%2C-vol.pdf | 269-page scan of vol. I (1955); pp. 10-11, 80-92 read | DONE eci1955report |
| 21:33 | ~/iit-playground/berthon_ethics_local/run_2026_11/A2/hansard1807/hansard1807.html (scout download of the Historic Hansard page) | cc. 798-806 read in full | DONE hansard1807parochial |
| 21:37 | https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/cth/HCA/2002/58.html | 403 "Just a moment..." challenge page | (blocked, not bypassed) |
| 21:37 | https://eresources.hcourt.gov.au/showCase/2002/HCA/58 and hcourt.gov.au summary PDF | HTTP/2 stream errors, nothing received | (route failed) |
| 21:38 | https://archive.org/wayback/available (AustLII HCA 2002/58; BAILII UKHL 1970/5) | captures exist for both | - |
| 21:39 | https://web.archive.org/web/20150506060319/http://www.austlii.edu.au/au/cases/cth/HCA/2002/58.html | public IA capture of AustLII text; paras 58-69, 96-125, 134-136, 143-146 read | DONE yorta2002members |
| 21:46 | https://web.archive.org/web/20260109180412/http://www.bailii.org/uk/cases/UKHL/1970/5.html | public IA capture of BAILII transcription of the HL print; Lord Reid and Lord Wilberforce read in full, facts from Lord Hodson | DONE saunders1971anglia |
| 21:47 | card cap (10) reached | remaining targets not attempted: Tilden Rent-A-Car v. Clendenning (1978); Locke's memorandum on the Licensing Act (1694-95); Stamp Act 1712; Declaration of Persepolis (1975); UNESCO/UNDP EWLP critical assessment (1976); Macaulay's Minute (1835, already on disk) | SKIPPED card cap |
