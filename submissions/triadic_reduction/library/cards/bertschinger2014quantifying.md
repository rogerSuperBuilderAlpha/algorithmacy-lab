---
citekey: bertschinger2014quantifying
title: "Quantifying Unique Information"
authors: "Bertschinger, Nils; Rauh, Johannes; Olbrich, Eckehard; Jost, Jürgen; Ay, Nihat"
year: 2014
venue: "Entropy 16(4): 2161–2183 (published 15 Apr 2014)"
doi: "10.3390/e16042161"
section: "S5"
status: candidate
verified: verified
source_basis: "arXiv:1311.2852v2 PDF (25 pp., v2 16 Jan 2014; arXiv journal-ref 'Entropy, 16 (2014) 4, p. 2161-2183'), read via pdftotext -layout; Entropy record confirmed in Crossref. MDPI's PDF route returned HTML to curl, so the published text was not read; the loci are from the arXiv version, which predates publication by three months."
access_url: "https://arxiv.org/abs/1311.2852"
retrieved: 2026-09-24
sha256: "d9d90da2a964039588b1eed45458b02b197e6d5605964b14e0eb048ce557e0ac"
---

## What the talk may use it for
Bertschinger and co-authors define the bivariate decomposition that the register calls I_BROJA, a label built from the authors' initials that the paper itself never uses. They start from unique information, not redundancy. Their operational idea is that shared and unique information about X should depend only on the two pair marginals (X, Y) and (X, Z). So they minimize over the set Δ_P of all joint distributions with those marginals: unique information is the minimum conditional mutual information, and shared (SI) and synergistic (CI) information follow from it. All four terms are non-negative, and any measure with the same invariance is bounded by theirs. The introduction states the critique of I_min in one line, which the register needs.

## Loci
Page numbers are those of the arXiv v2 PDF.
- p. 1 (abstract) — "Our measures are motivated by an operational idea of unique information which suggests that shared information and unique information should depend only on the pair marginal distributions of (X, Y) and (X, Z)."
- p. 2, Eq 1 — MI(X : (Y, Z)) = SI(X : Y; Z) + UI(X : Y \ Z) + UI(X : Z \ Y) + CI(X : Y; Z).
- p. 3 — "While the general approach of [10] is intriguing, the proposed measure of shared information Imin suffers from serious flaws, which prompted a series of other papers trying to improve these results [4, 5, 2]." — [10] is Williams & Beer.
- p. 3 — the definitions: unique information as the minimum over Q ∈ Δ_P of MI_Q(X : Y | Z), shared information as the maximum over Δ_P of the co-information, and CI as MI(X : (Y, Z)) minus the minimum over Δ_P of MI_Q(X : (Y, Z)) (tildes and subscripts transcribed from the text layer).
- p. 15 — "It is easy to find examples where Imin is unreasonably large [5, 2]." and "both Ired and Imin satisfy assumption (∗). Therefore, Ired ≥ S̃I and Imin ≥ S̃I." — [5] is Harder, Salge & Polani (harder2013bivariate).

## What the preliminary sources claim about it
- imin-criticism (TR-S5-454, -524) → verified, jointly with harder2013bivariate (p. 3 here: "suffers from serious flaws, which prompted a series of other papers").
- broja-alternative-redundancy (TR-S5-525): "Modern discrete-variable implementations use alternative redundancy measures such as I_BROJA" → corrected. The measure exists and is this paper's: the shared information S̃I, derived from the unique information ŨI by optimizing over Δ_P (p. 3). The paper never uses the label "BROJA". It also defines unique information first and redundancy only through it, so "redundancy measure" is a secondary reading. Whether "modern implementations" use it is not settled by this paper.
- The note on TR-S5-454, "Lab card bertschinger2014quantifying.md exists", is now true.

## Notes
- The paper says its decomposition is bivariate: S̃I "only measures the shared information of two random variables (about a third variable)" (p. 11), unlike Williams & Beer's lattice for any number of sources.
- Griffith & Koch 2014, the third critique named in the register's corrections, is arXiv:1205.4265 ("Quantifying synergistic mutual information"). Its local copy is saved as griffith_koch_1205.4265.pdf and is not carded here.
