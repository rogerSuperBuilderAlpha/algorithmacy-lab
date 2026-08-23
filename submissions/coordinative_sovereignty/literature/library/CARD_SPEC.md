# Card spec — coordinative_sovereignty library

One markdown file per source at /tmp/library/cards/<id>.md, where <id> is the "id" field from /tmp/library/sources.json. Do not rename ids.

File layout (exact):

---
id: <id>
type: <type>
authors: [ "Last, F. M.", ... ]
year: <year>
title: "<title>"
container: "<journal | book | court | OJ>"
volume: ""  issue: ""  pages: ""  publisher: ""
doi: ""
url: ""
origin: [cited, audit, sweep, ...]
priority: cited|must|should|optional
role: support|second_source|contests|position_against|legal_instrument|optional
chapter_sections: ["§3.2", ...]
tags: [...]
verified: full|abstract|api|search|unverified
verified_on: 2026-08-23
verified_how: "what you opened: DOI landing page / publisher abstract / PDF / EUR-Lex / Curia / Crossref record / could not open"
apa: "<full APA 7 reference-list entry, corrected>"
corrections: "<any change from the chapter's current entry, or 'none'>"
anonymization_risk: none|low|high  (high only if the source identifies the author or the 'algorithmacy' term)
---

## Summary
About 150 words in your own prose (no bullets): what the work argues or finds, its method and setting where empirical, and its central result. Write from the abstract or full text you opened this session. If you could not open anything, write "Not opened this session; summary withheld" and nothing else here.

## Use in the chapter
Two to five sentences. Where the chapter cites it (quote the in-text cite span ≤12 words from chapter.md, with section), or where the audit/sweep proposes it and why. State the role: support, second source for which claim, contests which claim, or construct to position against. If the audit flagged overreach or a wording mismatch, state it here.

## Key quotations
Only quotations you actually saw this session, each with a page or paragraph locator or "(Abstract)". Two to four. If none seen, write "None verified this session."

## Related cards
Three to six ids from sources.json that a reader of this card should see next (neighbours, rivals, second sources).

Rules: APA 7, sentence case titles, no em-dashes in your prose, no bullets in Summary or Use sections. Never invent a quotation or a page number. Never invent a DOI; if sources.json has none and you find one on the publisher page, add it and say so in verified_how. Where sources.json has a known open issue in notes (end page, year, author order), try to resolve it from the page you open and record the resolution in corrections; if unresolved, say so.
