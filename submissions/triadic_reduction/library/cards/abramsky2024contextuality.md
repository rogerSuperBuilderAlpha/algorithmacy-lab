---
citekey: abramsky2024contextuality
title: "Combining contextuality and causality: a game semantics approach"
authors: "Abramsky, Samson; Barbosa, Rui Soares; Searle, Amy"
year: 2024
venue: "Philosophical Transactions of the Royal Society A 382(2268): 20230002 (published 29 Jan 2024, CC BY 4.0)"
doi: "10.1098/rsta.2023.0002"
section: "S5 (peripheral)"
status: candidate
verified: corrected
source_basis: "arXiv:2307.04786v2 PDF (14 pp., 26 Jan 2024; arXiv journal-ref 'Phil. Trans. R. Soc. A 382: 20230002 (2024)'), §§1–2 and the definition of causal contextuality (p. 8) read via pdftotext -layout, the rest searched by keyword. The Royal Society PDF URL returned an HTML page, so the version of record was not read. Title, volume, issue, article number, licence and authors from Crossref"
access_url: "https://arxiv.org/abs/2307.04786v2"
retrieved: 2026-09-24
sha256: "bbd7d06dd6734daddc735adb542a83fa2f9dc747b06979a1025863faca9df250"
---

## What the talk may use it for
Peripheral to S5, and probably not needed. Abramsky, Barbosa and Searle extend the sheaf-theoretic account of contextuality (abramsky2011structure) to settings with causal order. They treat an experiment as a two-person game in which the Experimenter's moves are measurements and Nature's moves are outcomes, and they replace the event sheaf by a presheaf of strategies. A model is causally non-contextual when its compatible family extends to a global section of that presheaf. The causal settings they name are spacetime structure, the causal order of an experiment, and feed-forward in measurement-based quantum computation (MBQC). If the talk cites the contextuality analogy at all, abramsky2011structure is the source to cite.

## Loci
Page numbers of the arXiv v2 PDF; the journal pagination was not seen. Quotations matched against the pdftotext layer.
- p. 1 (abstract) — "The key idea is to view contextuality as arising from a game played between Experimenter and Nature" — the approach.
- p. 1 — "fundamental aspects of the physical setting, in particular the causal structure of spacetime;" — the first of three sources of causality; the others are the causal structure of an experiment and "feed forward in measurement-based quantum computation (MBQC)".
- p. 1 — "The game format is already familiar in the form of non-local games." — the link to non-local games.
- p. 2 — "Our treatment builds upon the sheaf-theoretic approach to contextuality." — continuity with abramsky2011structure (their ref. [7]).
- p. 2 — "connections with logic and computation, database theory, constraint satisfaction" — one item in the authors' list of what the sheaf-theoretic approach supports (refs. [2, 21]).
- p. 4 — "The output of the OR function is read off from the XOR of the three outcome bits." — §3.2, "Example II: Anders–Browne", a GHZ-based MBQC example in which XOR is classical side-processing.
- p. 8 — "The empirical model is causally non-contextual if this compatible family extends to a global section of the presheaf" DR Γ — the definition.

## What the preliminary sources claim about it
- abs-2024-bib (TR-S4-027, -058, -137) → corrected: Abramsky, S., Barbosa, R. S. & Searle, A. (2024), "Combining contextuality and causality: a game semantics approach", Phil. Trans. R. Soc. A 382(2268): 20230002. TR-S4-027 and -058 are right; TR-S4-137 drops the subtitle.
- abs-2024-causality (TR-S4-176, -177) → corrected. -176: the paper covers "causal background structure, adaptive measurement-based quantum computation, and causal networks" (abstract); spacetime light cones are one motivation (p. 1), so "relativistic causality" is too narrow. -177: the global-section criterion is right (p. 8), but its substance comes from abramsky2011structure (p. 9; Theorem 8.1, pp. 23–24). "Non-factorizable relational systems" is not either paper's phrase.
- contextuality-obstruction-global-section, abramsky-xor-bell-games, sheaf-literature-not-linked-to-clones (TR-S4-031, -138, -185, -034, -186), where they cite this paper → see abramsky2011structure. This paper frames contextuality as a game and mentions non-local games (p. 1). Its XOR is not a non-local game: in a GHZ-based MBQC example it uses "XOR on the bit representations" to set Charlie's measurement and reads an OR gate off "the XOR of the three outcome bits" (p. 4). It names database theory and constraint satisfaction among the approach's connections (p. 2); it mentions no clones, PAL, PID or IIT.

## Notes
- Peripheral to S5. Read only as far as the register rows needed.
- Page numbers are arXiv v2 pages; v2 was posted three days before journal publication.
