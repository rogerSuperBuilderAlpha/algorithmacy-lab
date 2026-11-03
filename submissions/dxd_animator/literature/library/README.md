# DXD animator project — card library

*Built 2026-11-03 at the author's request. Agent-written; the author has not reviewed the cards, and
none of the text is his.*

One card per source, `cards/<bibkey>.md`, keyed to `../references.bib`. The format follows
[`../../../dxd_foundation/literature/library/README.md`](../../../dxd_foundation/literature/library/README.md)
(round-4 rule for sources not read in full), with two added header fields: **Citation count** (source and
date) and **Pillar** (which of the project's three pillars the source serves).

Every card in this first round opens with "⚠ Not read in full." Its summary comes from the abstract and
catalogue record, checked against Crossref, Semantic Scholar, Open Library or the publisher. Before a
claim from a card goes into a draft, read the source and upgrade the card to `full_text`, then add an
`## S2 adversarial verification (date)` section as in `dxd_foundation`.

Rebuild the index after adding a card: `python submissions/dxd_animator/literature/library/build_index.py`
(CI runs it with `--check`). [`INDEX.md`](INDEX.md) lists the cards by pillar.
