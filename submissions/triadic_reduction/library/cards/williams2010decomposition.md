---
citekey: williams2010decomposition
title: "Nonnegative Decomposition of Multivariate Information"
authors: "Williams, Paul L.; Beer, Randall D."
year: 2010
venue: "arXiv:1004.2515 [cs.IT] (preprint, v1 14 Apr 2010; never published in a journal)"
doi: "10.48550/arXiv.1004.2515"
section: "S5"
status: candidate
verified: corrected
source_basis: "arXiv PDF of 1004.2515v1 (14 pp.), read in full via pdftotext -layout"
access_url: "https://arxiv.org/abs/1004.2515"
retrieved: 2026-09-24
sha256: "5654e8083b45f1c4fc92669996f647712322a3563a56252dbeb1d0ec46b24678"
---

## What the talk may use it for
Williams and Beer introduce partial information decomposition (PID). They define redundancy I_min as the expected minimum specific information that any source gives about each outcome of the target (Eq 3). They order collections of sources as a lattice of antichains, where α ≼ β iff every source in β contains some source in α (Eqs 4–5), and they take partial-information atoms Π_R as the Möbius inverse of I_min over that lattice (Eqs 6–7). For two sources, I(S; R1, R2) splits into redundancy, two unique terms and synergy (Eq 11). They prove that every atom is non-negative for any number of sources (Theorem 5), and that I_min never exceeds any single source's mutual information (p. 3). For XOR the paper says only that the sources "individually provide no information but together provide complete information". The numerical split follows from Eqs 10–11 and non-negativity: redundancy and both unique atoms are 0, and synergy is I(S; R1, R2). That makes synergy 1 bit for independent uniform inputs, an assumption the paper states only for 3-parity (the carder's arithmetic, not a printed value; see Notes). The paper also shows that three-variable interaction information equals synergy minus redundancy (Eq 14) and so confounds the two.

## Loci
Pages are those of the arXiv v1 PDF. Quotations were matched against its pdftotext layer. The text layer spaces subscripts ("I(S; Ai )"), and I normalised that spacing.
- p. 1 (abstract) — "Unlike interaction information, the atoms of our partial information decomposition are never negative and always support a clear interpretation as informational quantities." — the non-negativity claim.
- p. 2 — "A well-known example for binary variables is the exclusive-OR function S = R1 ⊕ R2, in which case R1 and R2 individually provide no information but together provide complete information." — XOR as the example of synergy.
- p. 3 — "Imin is less than or equal to I(S; Ai) for all Ai’s, with equality if and only if I(S = s; Ai) = I(S = s; Aj) for all i and j and all s ∈ S." — redundancy is bounded by each source's MI.
- p. 6 — "Thus, it is indeed the case that positive values indicate synergy and negative values indicate redundancy." — W&B's sign convention for I(S; R1; R2) = I(S; R1|R2) − I(S; R1) (Eq 12).
- p. 6 — "PI-decomposition also makes clear that I(S; R1; R2) confounds redundancy and synergy" — the motivation for PID.
- p. 11 — "Theorem 5. ΠR is nonnegative." — proved for I_min on the full lattice, for any number of sources.

## What the preliminary sources claim about it
- pid-williams-beer-2010, pid-citation, williams-beer-2010-pid-citation (TR-S5-004, -025, -050, -229, -251, -302, -409, -464, -512) → verified: W&B 2010, arXiv:1004.2515, introduce PID over a redundancy lattice of antichains. Supply author, year and full title where the sources omit them.
- xor-canonical-synergy, xor-pure-synergy, xor-info-in-triple (TR-S5-006, -032, -304, -234, -255, -473, -519, -038, -392) → verified with a condition: XOR is W&B's example of synergy, in which the sources "individually provide no information but together provide complete information" (p. 2). It is pure synergy for independent, uniform inputs, which the paper assumes explicitly only for 3-parity (p. 6).
- xor-synergy-one-bit, xor-pid-atoms (TR-S5-257, -035, -036, -087, -088, -089) → corrected: the values Red = Unq1 = Unq2 = 0 and Syn = 1 bit follow from Eqs 10–11, non-negativity and I(S; Ri) = 0 under independent uniform inputs, but W&B do not print them. They are the carder's arithmetic (NOT FOR SLIDES as W&B's numbers; see Notes).
- pid-four-atoms, pid-four-atom-decomposition (TR-S5-028, -249, -250, -480, -515) → corrected: Eq 11 is the bivariate identity. The register note that non-negativity fails "in the multivariate case" is wrong for I_min, since Theorem 5 covers every lattice. Other redundancy measures can yield negative atoms. "Non-negative information theory" is not W&B's phrase.
- pid-atom-definitions, pid-motivation, shannon-mi-redundancy-synergy-blind (TR-S5-029–031, -514, -516–518, -513, -027, -118) → verified as glosses of pp. 1–2. W&B define the atoms through I_min and the lattice, not by these verbal glosses.
- pid-atoms-bounded-by-pairwise-mi (TR-S5-086) → verified: I_min ≤ I(S; Ai) (p. 3), and Π_R ≥ 0 (Theorem 5). W&B list these as properties of I_min. The "Williams–Beer axioms" (symmetry, self-redundancy, monotonicity) are a later framing of their Theorem 2 and p. 3 properties.
- williams-beer-synergy-definition (TR-S5-252) → corrected: W&B define synergy as the lattice-top atom Π_R(S; {12}). They prove nothing about what it "represents".
- williams-beer-imin (TR-S5-450) → verified (Eq 3, p. 2).
- pid-redundancy-lattice-mobius (TR-S5-452, -520–523) → corrected: Möbius inversion (Eqs 6–7) and I(S; A) as the sum of atoms below {A} (Eq 9) are verified. The lattice is not ordered "by set inclusion". The order is Eq 5. Its top is the self-redundancy of the whole source set, and its bottom is the redundancy of all single sources (p. 3).
- williams-beer-2010-pid-nonnegativity (TR-S5-402, -448, -451, -453) → corrected: W&B do claim non-negative atoms that "exhaustively decompose" the information (abstract), and they explain the negativity of interaction information (Section V). "Resolved" overstates it, because Harder, Salge & Polani 2013 (Phys Rev E 87:012130) and Bertschinger et al. 2014 (Entropy 16(4): 2161–2183) went on to contest I_min as a redundancy measure.
- interaction-information and interaction-information-negative (TR-S5-043–045, -449) → corrected: I(X1;X2;Y) = I(X1;Y) − I(X1;Y|X2) is the co-information (McGill) sign convention, in which positive values mean redundancy. W&B use the opposite sign (Eq 12), in which positive values mean synergy. Negativity and confounding are verified (p. 6, Eq 14).
- xor-pairwise-independence, xor-single-input-zero-mi, xor-inputs-uncorrelated, xor-pairwise-model-noise, pairwise-independent-synergy, n-parity-synergy (TR-S5-034, -037, -083–085, -393, -256, -295, -584, -585, -623, -586, -588, -276, -272) → verified as elementary arithmetic under independent uniform inputs (the carder's, not W&B's; W&B print none of it). Full-support projections do not in general imply zero MI. A non-uniform distribution on the XOR relation has the same projections and non-zero pairwise MI. Parity with n inputs is W&B's pure-synergy case for n = 3 (p. 6).
- synergy-hypergraph-zero-dyadic-projection (TR-S5-048), synergy-iff-trivial-projections (TR-S5-254, -294), synergistic-teridentity-theorem (TR-S5-090, -119, -303) → refuted: nothing in W&B, or in any source found, states the biconditional, and it is false. Noisy XOR has full support F2^3 yet is purely synergistic. AND under I_min with uniform inputs has I(Y; Xi) ≈ 0.311 bit = Red and Syn = 0.5 bit (my arithmetic from Eqs 2–3, 11), so synergy coexists with informative single inputs.
- modern-proofs-triadic-irreducibility (TR-S5-558) → refuted: W&B say nothing about Peirce's thesis.
- xor-canonical-synergy-teridentity (TR-S5-640) → refuted: XOR as the canonical case of synergy is W&B's (p. 2), but "synergistic teridentity" occurs in no source found. W&B never mention teridentity.

## Notes
- The compiled arXiv PDF prints "Dated: November 26, 2024" (a LaTeX \today artifact of arXiv's rebuild); the submission is v1, 14 Apr 2010.
- NOT FOR SLIDES: carder's own arithmetic. W&B print no PID values for XOR or AND. Red = Unq1 = Unq2 = 0 and Syn = 1 bit for XOR, and I(Y; Xi) ≈ 0.311 bit = Red with Syn = 0.5 bit for AND, are the carder's calculations from Eqs 2–3 and 10–11 under independent uniform inputs. A slide may say that W&B use XOR as their example of synergy (p. 2); it may not attribute "1 bit" or "0.311" to W&B. The only numbers W&B print for worked examples are those for the FIG. 4A–B distributions (pp. 4–6).
- The lab card williams2010nonnegative.md (org_frontier/research/computational/literature/cards/) uses a different citekey for the same work.
