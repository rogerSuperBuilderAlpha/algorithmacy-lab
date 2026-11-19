# S7 hand-check, batch 3 (Fable, 2026-11-05)

Twenty cards: maier2022no … simon1955behavioral. Every quotation was re-read against the folder's text layer
(or, for shi2026siren, a fresh reading-order extraction of the held PDF, because the folder's .txt
interleaves the columns); every frontmatter field against the folder's Crossref, OpenAlex, CSL or Open
Library record; every sha256 recomputed. Verdicts: 18 index, 2 index after fix, 0 hold.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| maier2022no | full_text | 5/5 | index | nothing | nothing |
| may2003using | partial | 12/12 | index | nothing | abstract's "6 of the 10 classes" vs §6.2's seven classes is unreconciled in the parts read; quote §6.2–6.3 figures |
| mccloud1993understanding | metadata | 0/0 | index | nothing | nothing new (BROWSER_LIST row 27) |
| mori2012uncanny | abstract | 0/0 | index | nothing | nothing |
| natale2019if | full_text | 7/7 | index | nothing | untagged c3/c5 fit (opacity breeds narratives) offered by the card; decide whether to tag |
| ngai2004animatedness | metadata | 0/0 | index | nothing | author's name is in no record in the folder; confirm from the title page (row 4) |
| norman1986cognitive | metadata | 0/0 | index | nothing | anchor + load-bearing on metadata; the OpenAlex abstract the triage quoted (W4239943223) was never fetched; chapter is row 12 |
| payne1992behavioral | metadata | 0/0 | index | nothing | anchor rests on the title alone until read (row 10) |
| ruddell2008from | full_text | 5/5 | index | nothing | untagged c6 fit (suture, ms pp. 18–22); decide whether to tag |
| saracay2026beyond | partial | 9/9 | index | nothing | CoPref keeps the target fixed: supports "preference is constructed", cuts against "the goal moves"; rule on the c1 scope |
| schneider2018digital | abstract | 0/0 | index after fix | Caution "The 2016 work has no card in this run" → names `weinmann2016digital`, which exists and is approved (DECISIONS F6) | anchor + load-bearing on a one-sentence abstract; ACM 403 (FETCH_LOG 53), row 24; "no neutral way to present choices" unconfirmed |
| schwan2000do | full_text | 8/8 | index | nothing | second author's given name follows the OCR layer ("Barbel"); no Crossref/OpenAlex record in the folder to settle the umlaut |
| shanahan2023role | full_text | 10/10 | index | nothing | nothing |
| sheridan2002humans | metadata | 0/0 | index | nothing | author's name comes from the triage file, not the record (key OL828637A only); confirm from the book (row 14) |
| shi2026siren | partial | 12/12 | index | nothing | (1) arXiv v4 read, not the ACM version of record; (2) Shi et al. treat authorship as "diffuse" and keep the organisation accountable, which sits against the triad (c3, c7); decide whether §3.2 answers it |
| shneiderman1984response | abstract | 0/0 | index | nothing | anchor + load-bearing on an abstract; ACM 403 (FETCH_LOG 47), row 19 |
| siles2019mutual | abstract | 0/0 | index after fix | Caution "None of these were seen in the records read here" → the folder's openalex.json oa_url carries `ccc/12/4/499`; frontmatter stays blank (a URL path is not a bibliographic field) | DECISIONS F7's UCR fallback (handle 10669/79031) was never tried; FETCH_LOG 57 and 79 show only the OUP attempts |
| silvio2010animation | abstract | 0/0 | index | nothing | status cited, anchor, load-bearing, and every page locus (422, 428, 432) reaches the lab only through L. Stark (2024); read before quoting Silvio directly (row 2) |
| silvio2019puppets | metadata | 0/0 | index | nothing | (1) Alexy: Crossref says editor, the triage's Open Library reading says second author; the title page settles it. (2) p. 52 is quoted only through Stark (2024, p. 1664); cite as "quoted in Stark" until seen (row 1) |
| simon1955behavioral | metadata | 0/0 | index | nothing | nothing (end page unconfirmed; row 33) |

## Notes on method

- Loci: the two-column PDFs (maier, schwan, shanahan) have interleaved columns in the folder .txt, so a
  straight string match fails; each sentence was found by matching its prefix and reading the continuation
  in its own column. All were present. Page locators were confirmed from running heads or footers (may,
  schwan, shanahan), printed page numbers (saracay), manuscript footers (ruddell), or form-feed counts
  (natale, shi).
- Ruling 4 (the HF triads) names cameron2024social, stanton2006distributed, chiou2023trusting and
  oneill2022human, none in this batch. sheridan2002humans is the only F8 card here; it attributes no model
  to the book, so nothing had to be recorded.
- Four anchor, load-bearing cards in this batch rest on an abstract or a record alone: norman1986cognitive,
  schneider2018digital, shneiderman1984response, silvio2010animation (plus silvio2019puppets, metadata).
  Each card says so. They can be indexed, but the paper cannot lean on them until the browser copies arrive.
