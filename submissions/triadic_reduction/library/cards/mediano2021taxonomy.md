---
citekey: mediano2021taxonomy
title: "Towards an extended taxonomy of information dynamics via Integrated Information Decomposition"
authors: "Mediano, Pedro A. M.; Rosas, Fernando E.; Luppi, Andrea I.; Carhart-Harris, Robin L.; Bor, Daniel; Seth, Anil K.; Barrett, Adam B."
year: 2021
venue: "arXiv:2109.13186v1 [q-bio.NC] (27 Sep 2021). Published as: Mediano, P. A. M.; Rosas, F. E.; Luppi, A. I.; Carhart-Harris, R. L.; Bor, D.; Seth, A. K.; Barrett, A. B. (2025), 'Toward a unified taxonomy of information dynamics via Integrated Information Decomposition', PNAS 122(39): e2423297122, doi 10.1073/pnas.2423297122"
doi: "10.48550/arXiv.2109.13186"
section: "S5"
status: candidate
verified: corrected
source_basis: "arXiv PDF of 2109.13186v1 (21 pp. + appendix), read in full via pdftotext -layout. Published version: PNAS 122(39): e2423297122 (22 Sep 2025), doi 10.1073/pnas.2423297122, CC BY 4.0; title, volume, issue, article number and authors from Crossref, and the Europe PMC full-text XML (PMC12501198) searched for each locus phrase on 2026-09-24 but not read in full"
access_url: "https://arxiv.org/abs/2109.13186"
retrieved: 2026-09-24
sha256: "98b0e23fa2dca89fcd8ac73a901c9e09d27561cb51aa8dbd625bfe4291a6270a"
---

## What the talk may use it for
Mediano, Rosas, Luppi and co-authors extend PID from one target to many. Their Integrated Information Decomposition (ΦID) splits the time-delayed mutual information I(X_t; X_{t+1}) of a Markovian system over a product lattice A × A. For two elements that lattice has 16 atoms, each a pair of PID atoms written "past → future" (e.g., Syn → Un¹). Shannon theory and PID supply only 15 equations for those 16 atoms, so a double-redundancy function must fix the remaining one, and the authors leave its form open. They group the atoms into six modes: storage, copy, transfer, erasure, downward causation and upward causation. Syn → Syn, which they call synergistic storage, is new. The "Φ" in the paper is the empirical whole-minus-sum measure Φ^WMS and a revised Φ^R, not IIT 4.0's φ_s or Φ. The paper shows these measures are aggregates of several ΦID atoms. It does not show that IIT's Φ is "driven by" synergy.

## Loci
Pages are those of the arXiv v1 PDF; quotations matched against its pdftotext layer. Each line says whether the wording also appears verbatim in the PNAS 2025 text. Lines marked **v1 only** must be cited to arXiv:2109.13186v1, not to PNAS.
- p. 2 — "the information taxonomy introduced by PID is only valid in scenarios with a single target variable" — ΦID's motivation. **v1 only**; PNAS rewords it ("only valid in scenarios with many sources of information but only a single target variable").
- p. 3 — "there are not four, but rather 16 distinct information atoms" — 16 atoms for a two-element system. Also in PNAS.
- p. 4 — "standard Shannon theory and PID together specify a system of 15 equations for the 16 ΦID atoms, yielding an underdetermined system." — hence the double-redundancy function. **v1 only**; PNAS: "Φ ID specifies a system of 15 equations for 16 atoms".
- p. 5 — "Downward causation Collective properties that define individual futures. Comprises Syn → Un1 , Syn → Un2 , and Syn → Red." — one of six modes (superscripts flattened in the text layer). The gloss "Collective properties that define individual futures" is also in PNAS.
- p. 6 — "upward causation and synergistic storage (Syn → Syn) have, to our knowledge, not been reported in the literature." — the new modes. Also in PNAS.
- p. 10 — "the negative of the Red → Red atom" — Φ^WMS enters the Red → Red atom with a minus sign; the atom itself is not said to be negative. Also in PNAS, which adds "this negative double-redundancy term" for the signed term.
- p. 14 — "there is not yet a consensus on one that is universally preferable" — about PID redundancy functions, carried over to double-redundancy. **v1 only**; PNAS: "none of them is universally preferable".
- p. 14 — "it might miss relevant phenomena in systems with non-Markovian dynamics" — the Markovian limitation. **v1 only**; PNAS: "it might miss important phenomena in systems with non-Markovian dynamics".

## What the preliminary sources claim about it
- phiid-mediano-rosas-luppi (TR-S5-005, -039) → corrected: the year and authors are wrong. The 2019 version (mediano2019information) has no Luppi, the Luppi-coauthored arXiv is 2021, and the published version is PNAS 2025. Synergy is not defined by "vanishing across pairwise marginals". Mediano et al. gloss it as "the information conveyed by both sources together but none of them in isolation" (p. 2). TR-S5-039's substance, ΦID over (X_t, Y_t) → (X_{t+1}, Y_{t+1}), is verified.
- phiid-phi-driven-by-synergy, phiid-synergy-drives-phi (TR-S5-040, -404, -416) → refuted: the paper decomposes Φ^WMS, ψ, Φ^G and causal density into atoms (Table 1, pp. 8–9). It shows that Φ^WMS counts all synergy, unique transfer and minus Red → Red (p. 10). It proves no claim that IIT's Φ is "driven by" synergy, and nothing about "dyadic channels".
- phiid-dynamic-synergy-definition (TR-S5-041) → corrected: the atoms are pairs of PID atoms (p. 3). "Vanish under decomposition into dyadic channels" is Gemini's gloss.
- pid-phiid-nonnegative-lattices (TR-S5-046) → corrected: W&B's I_min atoms are non-negative (williams2010decomposition, Theorem 5). ΦID claims no general non-negativity. Its appendix proofs assume a non-negative double-redundancy (Appendix IV), and the numerical examples use a CCS-based double redundancy. The register's "negative Red → Red atom" misreads p. 10, where the atom enters Φ^WMS with a minus sign. Line 21 of lab card mediano2021towards.md repeats the misreading.
- phiid-mediano-2021, phiid-citation (TR-S5-052, -230, -403, -410, -591) → corrected: arXiv:2109.13186 is right, and its full title is the one above. TR-S5-403 merges this paper with a different one: Luppi, Mediano, Rosas et al. 2021, "What it is like to be a bit" (luppi2021bit).
- phiid-pnas-unified-taxonomy (TR-S5-147) → metadata only: the entry is right. PNAS 122(39): e2423297122 (22 Sep 2025), same seven authors, title "Toward a unified taxonomy of information dynamics via Integrated Information Decomposition" (Crossref; Europe PMC PMC12501198). The PNAS text was searched for the loci above, not read in full.
- phiid-16-atom-lattice, phiid-16-atoms, phiid-product-lattice (TR-S5-117, -267, -590, -592, -428, -456) → corrected: 16 atoms on a product lattice hold for two elements (p. 3; Methods, p. 15), verified. TR-S5-428 is incomplete: tracking PID atoms leaves the system underdetermined until a double-redundancy function is chosen (p. 4; Proposition 1, "15-for-free", p. 17). The mapping of the lattice to Thirdness (TR-S5-590) is Gemini's.
- phiid-taxonomy-mode-names (TR-S5-268, -269, -287) → corrected: the modes are storage, copy, transfer, erasure, downward causation and upward causation (p. 5). Syn → Un is downward causation and Syn → Syn is synergistic storage. "Downward transformation" and "persistent synergistic loops" are not the paper's terms. ΦID stands for Integrated, not "Intrinsic", Information Decomposition. Transfer is Un¹ → Un² and Un² → Un¹, as TR-S5-268 says.
- phiid-multi-target (TR-S5-423, -426, -427) → verified: PID takes a single target, which may be multivariate (pp. 2–3), and ΦID extends it to many targets. TR-S5-427's "existing metrics" should read "PID".
- phiid-new-modes (TR-S5-424, -457) → verified: the paper names synergistic storage and decomposes transfer entropy into four atoms (Fig 7). Its parity-preserving system has zero causal density and zero AIS but Φ^WMS = 1 (p. 10).
- causal-discovery-ignores-higher-order (TR-S5-425) → verified: cause–effect-pair approaches "neglect higher-order relationships that cannot be expressed in terms" of causal arrows (p. 1).
- phiid-taxonomy-double-counting (TR-S5-429) → verified: the paper claims "a complete information decomposition on groups of time series" (p. 2) and shows double-counting of Red → Red in summed information storage (p. 6) and in causal density (Fig 3).
- phiid-double-redundancy-no-consensus (TR-S5-430) and phiid-markovian-limitation (TR-S5-431) → verified (p. 14).
- teridentity-bounds-synergy-over-time (TR-S5-597–599) → refuted as a citation: ΦID says nothing about teridentity. No source found states these claims.

## Notes
- The paper's example "downward XOR" (X¹_{t+1} = X¹_t ⊕ X²_t) carries one bit in Syn → Un¹. The parity-preserving system carries one bit in Syn → Syn (Fig 4). These are the cleanest ΦID analogues of XOR-type synergy for a slide.
- The PNAS version differs in wording and numbering. Four of the eight loci above are **v1 only** (marked). Two quotations in the claims section are also v1 only: "neglect higher-order relationships that cannot be expressed in terms" (p. 1) and "a complete information decomposition on groups of time series" (p. 2); neither string occurs in the PNAS text. "the information conveyed by both sources together but none of them in isolation" (p. 2) and "Proposition 1 (15-for-free)" occur in both. Page numbers, figure numbers and Table 1 are v1's throughout.
- Title history: arXiv v1 "Towards an extended taxonomy…"; PNAS 2025 "Toward a unified taxonomy…". A slide that quotes a v1-only locus cites arXiv:2109.13186v1 (2021); one that cites the published paper quotes only lines marked "Also in PNAS".
