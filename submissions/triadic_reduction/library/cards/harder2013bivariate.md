---
citekey: harder2013bivariate
title: "Bivariate measure of redundant information"
authors: "Harder, Malte; Salge, Christoph; Polani, Daniel"
year: 2013
venue: "Physical Review E 87(1): 012130 (published 23 Jan 2013)"
doi: "10.1103/PhysRevE.87.012130"
section: "S5"
status: candidate
verified: verified
source_basis: "arXiv:1207.2080v3 PDF (16 pp., v3 dated 20 Jul 2012; author's version of the PRE article, arXiv lists the PRE DOI), read via pdftotext -layout; PRE record confirmed in Crossref. The PRE typeset text was not read."
access_url: "https://arxiv.org/abs/1207.2080"
retrieved: 2026-09-24
sha256: "3b95ff14ce26bec596d6c9856b1391887bfdce1127136fe0ef150fe581df6515"
---

## What the talk may use it for
Harder, Salge and Polani give the standard counterexample to Williams and Beer's redundancy measure I_min. Take two independent, uniform bits X and Y, and let the target Z = (X, Y) simply copy both. X and Y say nothing in common about Z, since one fixes the first component and the other the second, yet I_min reports 1 bit of redundancy. I_min registers that each source gives the same *amount* of information about each outcome and ignores whether it is the same information. The authors add an "identity property" axiom that rules this out and build a projection-based measure, I_red, that satisfies it. They also report that I_min tends to overestimate redundancy. For the talk, this paper and bertschinger2014quantifying are what "I_min was contested" rests on, and they supply sourced numbers for the AND and XOR decompositions.

## Loci
Page numbers are those of the arXiv v3 PDF.
- p. 1 (abstract) — "Previous attempts to formalize redundant or synergistic information struggle to capture some desired properties."
- p. 2 — "We will argue that the redundancy measure proposed by Williams and Beer, while exhibiting a number of essential properties needed to formalize redundancy, is not capturing the concept of redundancy in a fully satisfactory way. These problems have been noted by Griffith [15]"
- p. 3 (§II.C, "Why Minimal Information is not Capturing Redundancy") — "Now we expect that there should be no redundancy between X and Y with regard to Z because we know that X and Y are independent, so the information contained about Z in X and Y respectively is clearly not the same. However, we have Imin (Z; X, Y ) = 1 bit."
- p. 3 — "even though X and Y give the same amount of information about an outcome z, they tell something different about the change of the distribution p(z)"
- p. 3 (Eq 5) — the identity property, I∩((X_A1, X_A2); A1, A2) = I(X_A1; X_A2).
- p. 6 — "In general there is a tendency of Imin to overestimate redundancy and in our examples it seems that Imin is an upper bound for Ired in most cases."
- p. 9 — XOR with uniform inputs: "Ired (Z; X, Y ) = Imin (Z; X, Y ) = 0 and get the purely synergistic decomposition"
- p. 9 — AND with uniform inputs: "Ired (Z; X, Y ) = Imin (Z; X, Y ) = 0.311278, so this is another example where minimal and redundant information coincide." The Fig. 7 caption gives "I(Z; X, Y ) = 0.811278", and the PI-diagram shows synergy 0.5 and unique information 0.

## What the preliminary sources claim about it
- imin-criticism (TR-S5-454, -524): "The I_min redundancy measure was widely criticized for failing to capture true redundancy, leading to many alternative PID formulations" / "critiqued for failing desired properties" → verified. This paper's §II.C is that critique (p. 3), it proposes an additional axiom that I_min fails (Eq 5), and it names Griffith's earlier objection (p. 2). bertschinger2014quantifying independently says that I_min "suffers from serious flaws, which prompted a series of other papers" (p. 3). "Widely" rests on these papers plus Griffith; the talk should cite two or three names, not a consensus.
- williams-beer-2010-pid-nonnegativity (TR-S5-402, -448, -451, -453): the correction's clause "Harder, Salge & Polani 2013 … contested I_min; both are metadata only here" is now read and holds. The verdict (corrected) does not change.
- synergy-hypergraph-zero-dyadic-projection (TR-S5-048): the correction's AND figures ("I(Y;Xi) ≈ 0.311 bit and Syn = 0.5 bit (my arithmetic …)") now have a source. With uniform inputs, I_min = I_red = 0.311278 bits of redundancy, total mutual information 0.811278 bits, no unique information and 0.5 bits of synergy (p. 9, Fig. 7). Since both unique atoms are 0, each I(Z; X_i) equals the redundancy, 0.311 bits.

## Notes
- The arXiv v3 header prints "Dated: November 27, 2024" (a LaTeX \today artifact at compile time); the arXiv record dates v3 to 20 Jul 2012.
- The published title in Crossref is "Bivariate measure of redundant information"; the arXiv title is "A Bivariate Measure of Redundant Information".
- arXiv:1205.4265, which an earlier fetch had filed under this citekey, is Griffith & Koch, "Quantifying synergistic mutual information". The local copy is saved as griffith_koch_1205.4265.pdf and is not carded here.
