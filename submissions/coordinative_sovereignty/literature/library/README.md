# Literature library — Algorithmacy and Sovereignty

One annotated card per source. Built 2026-08-23 from three inputs: the chapter's reference list (109 + 2 cases + 9 additional reading), the evidence audit's proposed second sources (`reviews/2026-08-23/EVIDENCE_AUDIT.md`), and the literature gap sweep (`reviews/2026-08-23/LITERATURE_GAPS.md` and its seven strand reports), plus twelve uncited entries carried from the July `references.bib`.

Files
- `cards/<id>.md`: YAML frontmatter (bibliographic fields, origin, priority, role, chapter sections, verification status and method, corrected APA entry, corrections, anonymization risk) followed by Summary, Use in the chapter, Key quotations (only those seen this session, with locators), Related cards. Spec in `CARD_SPEC.md`.
- `INDEX.md`: all cards, sortable by priority.
- `library.bib`: BibTeX generated from `sources.json`; keys are card ids. Supersedes `../references.bib` for this chapter.
- `sources.json`: the master list (405 entries) the cards and bib are generated from.
- `TODO.md`: cards still to write.

Conventions. Summaries are withheld where nothing substantive was opened; `verified` records the level reached (full / abstract / api / search / unverified). Corrections against the chapter's current reference list are recorded on the card, not applied to the chapter. Quotations inside cards may contain em-dashes where the source does; card prose does not.

Regenerate INDEX.md and library.bib from sources.json and the card frontmatter (see reviews/2026-08-23 session notes).
