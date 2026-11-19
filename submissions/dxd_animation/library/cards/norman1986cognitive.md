---
key: norman1986cognitive
apa: "Norman, D. A. (1986). Cognitive engineering. In *User centered system design* (pp. 31–62). CRC Press. https://doi.org/10.1201/9780367807320-3 [editors, subtitle and original publisher unchecked: the Crossref record names none]"
authors: "Norman, Donald A."
year: 1986
title: "Cognitive Engineering"
venue: "User Centered System Design"
volume: ""
issue: ""
pages: "31–62"
doi: "10.1201/9780367807320-3"
url: "https://www.taylorfrancis.com/books/9780367807320/chapters/10.1201/9780367807320-3"
type: chapter
facets: [F5]
claims: [c1]
role: anchor
load: load-bearing
read_depth: metadata
object_read: "Crossref work record (JSON) for DOI 10.1201/9780367807320-3, CRC Press (Boca Raton) chapter record, no abstract and no text of the chapter; local folder ~/iit-playground/dxd_animation_local/pdfs/norman1986cognitive/crossref.json; original URL none recorded (FETCH_LOG.tsv row norman1986cognitive: 'Crossref 200; records only', status records-only; no provenance.txt); read 2026-11-05; sha256 3004ee9201e7c521182b2b3bbc75d72ea2e2535ebaed93e289c1aed1ea9098c2"
verified: verified
verified_against: "crossref.json (DOI 10.1201/9780367807320-3), sha256 recomputed; FETCH_LOG row 10; BROWSER_LIST row 12; triage F5-F6 row 4"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

This is a metadata card. The Crossref record shows only that a chapter titled "Cognitive Engineering", by Donald A. Norman, appears at pp. 31–62 of a book titled *User Centered System Design*, which CRC Press (Boca Raton) registers under ISBN 9780367807320 with a 1986 print date. The record carries no abstract, no editors and no subtitle. Nothing in the read object says what the chapter argues.

## What the paper uses it for

- **c1.** The triage file (F5-F6.md, row 4) wants this chapter as the earlier statement of Norman's gulfs, so that OUTLINE §2 can say the classic model forms the goal first and bridges the gulfs of execution and evaluation after it. OUTLINE §2 now holds that point only through Norman (1988), read through secondaries, and Hutchins, Hollan and Norman (1985). This card cannot support the point: no text was read, so it cannot say whether or where the chapter puts goal formation before the gulfs. Until the chapter is read, the c1 use is unread and the citation should stay at "exists".
- Where the use might stretch: even a full read would show a goal-first model for single-user computer tasks. The step from that model to "conversion-era design inherited it" is the paper's.

## Loci

None.

## Caution

- The claim c1 would rest on is unread. BROWSER_LIST row 12 asks for ch. 3, pp. 31–62, "where goal formation precedes the gulfs".
- DECISIONS (F5 table) and the triage row set the expected depth as "abstract", and the triage row quotes an OpenAlex abstract ("to show how to make better choices when they exist", OpenAlex W4239943223). No OpenAlex record is in the local folder, so this card did not see that abstract and does not use the quotation. The depth is metadata.
- The Crossref record is the CRC Press reissue (record created 2026-03-13; ISBN 9780367807320, electronic). The triage row gives the original as Lawrence Erlbaum, edited by D. A. Norman and S. W. Draper, with the subtitle *New perspectives on human-computer interaction*. None of these appears in the record read, so the APA line leaves them out and marks them unchecked.
- The record writes the author in capitals ("DONALD A." "NORMAN"); the card normalises the case.
- Not to be confused with Norman (1988), the book OUTLINE §2 cites (`norman1988psychology`, dxd_foundation).
- OUTLINE and SOURCE do not cite this chapter, so its status is candidate.

## Verification

2026-11-05 · S6 verifier, batch b09 (opus; not the writer) · verdict: verified · checked: loci 0/0 (None, correct for metadata); title, author, container, pp. 31-62, 1986 print date, DOI, URL, CRC Press/Boca Raton, ISBN and created date match crossref.json; depth metadata honest (no abstract in the record); no claim beyond the record; sha256 matches; four sections in order · changed: nothing

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (None, metadata card); frontmatter vs crossref.json (Norman; "Cognitive Engineering"; *User Centered System Design* pp. 31–62; CRC Press, Boca Raton; 1986 print date; ISBN 9780367807320; DOI; record created 2026-03-13); sha256 recomputed; metadata depth honest; the c1 use is marked unread.
- Changed: nothing.
- For the author: `role: anchor`, `load: load-bearing` on a metadata card. The triage row quoted an OpenAlex abstract (W4239943223) that was never fetched into the folder; a fetch would lift the card to abstract depth. The chapter is BROWSER_LIST row 12.
