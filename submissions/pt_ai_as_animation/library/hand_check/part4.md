# S7 hand-check, batch 4 (run pta-lib-2026-11)

> [Written by Claude (Fable), 2026-11-08.]

Twenty cards, schumann2022machines to zhou2026externalization. Method: for each card with a text layer I
re-extracted the held PDF (or HTML) page by page with `pdftotext`, matched every quotation after joining
line-end hyphens and normalising ligatures, dashes and quotation marks, and recomputed the sha256 of the text
object. For record-only cards I re-read the JSON in the key folder against the frontmatter. Two cards
(tillis1992toward, williams2001animators) and part of a third (tomko2015beyond) rest on Open Library and
Library of Congress records that no key folder holds; I refetched those records on 2026-11-08 into my
scratchpad, matched the content and the hashes the cards give (the editions lists and the LoC page hash
differently today, their content does not), and left the folders alone, since the brief confines me to cards.

**Verdicts: 19 index, 1 index after fix (thomas1981illusion), 0 hold.** Loci: 118/118 found across the eight
cards that quote (14, 14, 8, 15, 12, 10, 15, 15, in order below); the twelve record-only cards have
Loci = None, as the schema requires.

**One batch-wide item for the author.** README defines `status: cited` as "SOURCE.md or SKETCH.md uses it".
In this batch SKETCH names Thomas & Johnston, Trifonov, Maturana & Varela and Zaharia; rulings B1 and B2 name
Sun & Gualeni and Schumann & Du; the Checkpoint B swap names Villalobos & Dewhurst. Nine other cards carry
`cited` on the strength of the Checkpoint B approval alone: shanahan2024talking (SKETCH names a *different*
Shanahan paper, the 2023 *Nature* role-play article), silvio2019puppets, sullivan2022understanding,
voneschenbach2021transparency, wang2024survey, zednik2021solving, zerilli2019transparency,
zerilli2022explaining and zhou2026externalization (the S6 verifier flagged this one). I changed none of them;
decide whether an approved triage slot counts as a ruling, and if not, set them to `candidate`.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| schumann2022machines | full_text | 14/14 | index | nothing | whether this is the main §4.4 foil (card's Caution asks) |
| shanahan2024talking | full_text (arXiv v5, not CACM) | 14/14 | index | nothing | status `cited` rests on a different Shanahan paper in SKETCH; locators are arXiv pages |
| silvio2019puppets | metadata | None | index | nothing | book unopened (ruling 4, second); definition only via Stark; Alexy's role |
| sullivan2022understanding | abstract | None | index | nothing | abstract only; status (header) |
| sun2026between | full_text (author pre-print) | 8/8 | index | nothing | pagination provisional until the Springer chapter is seen; no editors in record |
| thomas1981illusion | metadata | None | index after fix | object_read: records now in the key folder, hashes added [Corrected by Fable, S7] | SKETCH inverts the title vs every 1981 record; principles chapter still unread |
| tillis1992toward | metadata | None | index | nothing | no key folder; S4 to save records; catalogue subtitle "puppetry as a theatrical art": admit or wait for title page |
| tomko2015beyond | abstract (publisher description) | None | index | nothing | Open Library records not in folder; Knight and Mason's role |
| trifonov2011vocabulary | metadata | None | index | nothing | "123 definitions" unverified; live OpenAlex abstract could lift depth |
| varela1974autopoiesis | metadata | None | index | nothing | initials F. G. vs Francisco J.; SKETCH's "Maturana & Varela" fits the 1980 book |
| villalobos2018enactive | full_text | 15/15 | index | nothing | nothing |
| voneschenbach2021transparency | metadata | None | index | nothing | closed; open DOI in browser if c7 cites it; status (header) |
| walton1990mimesis | metadata | None | index | nothing | book unopened (ruling 4, fourth) |
| wang2024survey | partial | 12/12 | index | nothing | status (header) |
| williams2001animators | abstract (LoC blurb) | None | index | nothing | no key folder; S4 to save records; blurb-as-abstract is a convention call |
| zaharia2024shift | full_text (web) | 10/10 | index | nothing | nothing |
| zednik2021solving | partial (arXiv preprint) | 15/15 | index | nothing | preprint pages, VoR unchecked |
| zerilli2019transparency | metadata | None | index | nothing | load-bearing but unread; Cambridge copy is .docx; status (header) |
| zerilli2022explaining | abstract | None | index | nothing | abstract only; status (header) |
| zhou2026externalization | partial | 15/15 | index | nothing | status `cited` (verifier flagged too) |
