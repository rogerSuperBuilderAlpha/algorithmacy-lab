# Scout A log (run_2026_11, 18 Nov 2026)

Agent-drafted. The author has not reviewed it and none of the text is his.

Scope run: Brief S, Scout A, targets from Briefs A1–A5 (PLAN §11). No cards written. No git commands run.

Note on logging: the log was written after each stage (targets, Crossref, OpenAlex, downloads, disk check), not after each item. Times are not recorded per line.

## Stage 1. Targets
- 75 leads listed from the target lists of A1–A5; 7 more added from brief text (ECI 1951–52, VRA 1982 §208, Stamp Act 1712, Locke memorandum, benefit studies, Graff 1979 conditional, two Brazil/India items). Total 82 rows in SOURCES_A.tsv.
- Carded or already in CARD_INDEX checked by surname prefix only. Index lookups for graff1991, brandt1998, vee2013, clegg1997, newland2022, holmes1975 and margo2005 confirmed; the other keys were not found under their surnames.

## Stage 2. Records (Crossref, one request per second, generic client name)
- Query: `api.crossref.org/works?query.bibliographic=…&rows=5` for 75 targets (crossref_A_1.txt, local scratch). Second batch for Graff 2013, Stuckey, Cornelius, Laqueur, Hewitt, Freire.
- Result across the 82 rows: 52 OK (own record); 13 OK-review-only (resolved only through reviews, citing chapters or dataset records); 4 NOT FOUND; 1 MISMATCH (Siebert: lead gives 1965, a Crossref review is dated 1953); 12 UNSEARCHED (cases, statutes, reports not checked against their own sites). Cases were not checked against court or reporter sites.
- Crossref lacks case law, most government reports and most pre-1990 monographs, so those rows are UNSEARCHED rather than NOT FOUND.
- Lookups I could not resolve: Lind 1986 (NOT FOUND); Ngũgĩ 1986 (NOT FOUND); Newland vol. 2 2024 (NOT FOUND, agency site not checked); UNESCO/UNDP 1976 assessment under its own title (NOT FOUND; chapter resolves).

## Stage 3. Disk (DISK_INVENTORY.tsv)
- Matches confirmed on the first page: Graff 2013, Vieira 2013, Graff 2022 (hash-equal to run download), Johnes 2024 (hash-equal to run download), Macaulay 1835 (text), Hansard 1807 (text), boyd 2018 (text), Freire 1970 (Duke library copy; origin doubtful, locate only).
- Not copies: pdfs/M2/vincent.pdf (Nicholas Vincent, not the historian); Ngũgĩ files (Internet Archive 'Page Not Found', publisher list, 146–172-byte stubs); darnton1995.pdf (bot-challenge page); schwartz.pdf (stub); brandtclinton2002.pdf (HTML); jones2018_ucf_record.txt (catalogue record); pdfs/M1/brandt_eric.pdf (1997 ERIC report, not the carded 1998 article).
- Inbox /run_2026_11/inbox is empty: no Graff 1979 pages.

## Stage 4. Open copies and downloads (run folders under ~/iit-playground/berthon_ethics_local/run_2026_11/)
- Downloads that succeeded (SOURCE_URL.txt beside each):
  - A1/graff2022 (LiCS, diamond). Full. PDF plus txt.
  - A2/hansard1807 (api.parliament.uk historic Hansard). Full.
  - A2/macaulay1835 (mssu.edu classroom edition). Full.
  - A3/kousser1974 (CaltechAUTHORS author deposit of the book, 339 pp; copyright 1974, second printing 1975). Full.
  - A3/ragas2007 (Histórica, diamond, 28 pp). Full.
  - A3/shani2018 (Cambridge introduction, 20 pp). Partial (introduction only).
  - A5/johnes2024 (UWP open edition, CC BY, 458 pp). Full. Hash equals disk copy.
  - A5/boyd2018 (Data & Society web essay). Full.
- Downloads that failed (three attempts each; no circumvention):
  - A4/vanderwal2021: empty response from the publisher PDF URL. Blocked.
  - A4/darnton1995: bot-challenge page from the publisher. Blocked.
  - A5/bulgerdavison2018: bot-challenge page from the repository. Blocked.
  - A5 Ngũgĩ 1986: no clean copy located (Internet Archive page not found). Blocked.
- Discarded HTML saved under a .pdf name (Caltech landing page for Kousser); removed before the book copy was stored.

## Stage 5. Search for what the lists miss
- Not done in this pass. The brief asks for up to fifteen new rows per facet and citing-work lists for three anchors (Graff 1979, Street 1984, Kamperman and Graff 2026). I ran none of these searches. This is a gap in the run.
- Scout B tasks are not part of this brief.

## Tally
- record_status: OK 52; OK-review-only 13; UNSEARCHED 12; NOT FOUND 4; MISMATCH 1. Total 82.
- access: full 9; partial 1; abstract 1; blocked 4; library 34; unsearched 33. Total 82.
- Cards written: 0 (Scout A writes no cards).
- Blocked: vanderwal2021, darnton1995, bulgerdavison2018, ngugi1986.
