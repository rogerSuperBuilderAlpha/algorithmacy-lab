---
citekey: barbosa2020measure
title: "A measure for intrinsic information"
authors: "Barbosa, Leonardo S.; Marshall, William; Streipert, Sabrina; Albantakis, Larissa; Tononi, Giulio"
year: 2020
venue: "Scientific Reports 10: 18803"
doi: "10.1038/s41598-020-75943-4"
section: "S5"
status: candidate
verified: corrected
source_basis: "Publisher PDF (open access), main text read via pdftotext -layout; supplementary proof not read"
access_url: "https://www.nature.com/articles/s41598-020-75943-4"
retrieved: 2026-09-24
sha256: "d05770af15e50b492f81a647907a743e75232bcf8ed0a76821dc3f9bc76c44fe"
---

## What the talk may use it for
Barbosa and co-authors derive the intrinsic difference (ID), the measure that IIT 4.0 builds intrinsic information on. They require causality, specificity and intrinsicality, the last meaning expansion without noise and dilution with noise, and they prove that one function, up to a constant, satisfies all three: ID(P, Q) = max_α p_α log(p_α / q_α). ID is the maximum, over states, of selectivity (p_α) times informativeness (log p_α/q_α). It is not an absolute difference |p − q| times a log. This is the formula to use when checking Gemini's worked XOR example.

## Loci
- p. 3 — "Our main result is the existence of a unique function (up to a multiplicative constant k > 0)" — followed by Eq 1, D(P^n, Q^n) = k max_α p_α log(p_α/q_α) (equation typeset; read from the PDF, flattened in the text layer).
- p. 3 — "We set k = 1 without loss of generality and call this function intrinsic difference (ID)." — the name.

## What the preliminary sources claim about it
- iit4-intrinsic-difference-formula (TR-S5-021) → refuted: ID has no |p(e) − p^P(e)| factor. With p = 1 and q = 1/2 it gives 1 · log2 2 = 1 ibit, where Gemini's |p − q| form gives 0.5 (carder's arithmetic; see Notes).
- xor-mechanism-id-value, xor-repertoire-arithmetic (TR-S5-099, -619) → refuted on the same ground (see albantakis2023information for the φ form).
- iit4-current-standard (TR-S5-407) → corrected: this paper introduced ID in 2020. IIT 4.0 adopted it and did not "refine" it.

## Notes
- NOT FOR SLIDES: carder's own arithmetic. The paper does not treat XOR. The "1 ibit" for p = 1, q = 1/2 is the carder's evaluation of Eq 1. The paper's own printed values are for its channel examples: the KL and ID measures assign "1 bit and 1 intrinsic bit" to the noiseless bit-size channel and "8 bits and 8 ibits" to the noiseless byte-size channel (p. 4, Fig. 2A–B). Only those may be quoted as the paper's numbers.
- IIT 4.0 cites this paper as [14] and a companion on mechanism integrated information (Barbosa et al. 2021, Entropy) as [12]; the 2021 paper was not read.
