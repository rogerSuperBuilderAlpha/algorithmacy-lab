---
citekey: tegmark2016improved
title: "Improved Measures of Integrated Information"
authors: "Tegmark, Max"
year: 2016
venue: "PLOS Computational Biology 12(11): e1005123 (published 21 Nov 2016)"
doi: "10.1371/journal.pcbi.1005123"
section: "S4, S5"
status: candidate
verified: verified
source_basis: "Publisher PDF (open access, CC BY; 34 pp., footer 'n / 34'), read via pdftotext -layout; DOI, volume, issue and article number confirmed in Crossref. The text layer renders capital Φ as 'F' in running text; quotations below restore Φ."
access_url: "https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005123"
retrieved: 2026-09-24
sha256: "d9742c2417eb790cf523ade3283a5ba9f4c5690044032b09ac0726f1005f8e39"
---

## What the talk may use it for
This is the paper Koshkin cites when he says that measures of "information integration" are studied in biology, so it is the literature's own hinge between S4 and S5. Tegmark builds a taxonomy of integration measures. Every Φ in it is defined in two steps: a measure ϕ of how much two parts of a system affect each other across a cut, then Φ as the ϕ-value of the "cruelest cut" that minimizes ϕ. Koshkin borrows that phrase in quotation marks. The taxonomy's objects, though, are *Markov processes*. Tegmark reads the joint distribution p(x0, x1) as one system at two times and measures how badly the best separable Markov process, one "that does not mix information between subsystems", approximates it. IIT 3.0's Φ is one of six measures he singles out.

The talk needs one distinction from this paper. The quantity Koshkin proposes is a single-distribution mutual information across a bipartition of a relation's places. Tegmark's taxonomy does contain the one-time analogue, ϕofs = I(xA1; xB1), and he rejects it and ϕots as integration measures because neither is guaranteed to vanish for a separable (non-interacting) system (p. 19). Koshkin's measure is therefore a static cousin of the family, not the family's approved member, and it is not IIT's Φ. (The ϕofs comparison is my reading. Koshkin does not name any of Tegmark's measures.)

## Loci
Page numbers are the PDF's own ("n / 34").
- p. 1 (abstract) — "A simple taxonomy of Φ-measures is presented where they are each characterized by their choice of factorization method (5 options), choice of probability distributions to compare (3 × 4 options) and choice of measure for comparing probability distributions (7 options)."
- p. 2 — "there is broad agreement that it needs to be able to store and process information in a way that is somehow integrated, not consisting of nearly independent parts." — the uncontroversial necessary condition. Tegmark calls IIT's sufficiency claim "bold and controversial" in the next sentence.
- p. 2 — "interest in measuring integration is growing, not only in neuroscience but also in other fields, ranging from physics [12] and evolution [19] to the study of collective intelligence in social networks [20]." — [20] is Engel & Malone, "Can groups be conscious? Integrated information as a metric for group interaction" (preprint, 2015), a possible S6 pointer.
- pp. 2–3 — "All measures of Φ aim to quantify the extent to which a system is interconnected, yielding Φ = 0 if the system consists of two independent parts, and a larger Φ the more the parts affect each other." (the sentence runs across the page break)
- p. 3 — "Define Φ as the ϕ-value for the “cruelest cut” that minimizes ϕ." — the source of Koshkin's quoted phrase.
- p. 3 — "Note that our analysis is focused only on integration, not on consciousness"
- p. 3 — "Consider two random vectors x0 and x1 whose joint probability distribution is p(x0, x1). We will interpret them as the state of a time-dependent system x(t) at two separate times t0 and t1."
- p. 5 — "The idea is to approximate the Markov process by a separable Markov process that does not mix information between subsystems, and to define the integration as a measure of how bad the best such approximation is."
- p. 6 — separability is defined on the dynamics: the process "is separable if the Markov matrix M is a tensor product" MA ⊗ MB (Eq 7).
- p. 4 (Table 2) — ϕofs is defined as I(xA1; xB1) and ϕots as I(xA, xB) (subscripts transcribed from the text layer).
- p. 17 — "the mutual information of a bivariate distribution is simply the KL-measure of how non-separable it is."
- p. 19 — "Neither ϕots and ϕofs are guaranteed to vanish for separable systems, which means that we cannot in good conscience interpret them as measures of integration." (sic, "Neither … and")
- p. 30 — "Φ3.0 is the measure advocated by IIT3.0 and has the many attractive features described in [11]." — one of the six measures that "stand out" (ΦM, ΦM_kk′, Φ3.0, Φ2.5, Φ2.5′, Φ2.5″); he calls it "the slowest of all the measures to evaluate numerically".

## What the preliminary sources claim about it
- no-prior-unification-peirce-quine-iit (TR-S5-009, -055, -109): the register's correction cites "Koshkin (2024) … citing Tegmark 2016". The Tegmark reference is real and is this paper. It appears in both Koshkin papers (koshkin2022reduction pp. 14–15; koshkin2024reduction pp. 23, 30), and the arXiv number 2406.14058 that the register gives belongs to the 2022 TCSPS paper. See koshkin2022reduction for the verdict.
- No preliminary source cites Tegmark 2016 directly.

## Notes
- The paper counts the distance measures inconsistently: "7 options" in the abstract (p. 1) and "5 options" in the Discussion (p. 30). The card quotes the abstract.
- Tegmark's measures take a transition (two-time) distribution. None of them applies unchanged to a static relation with the uniform distribution on its tuples, which is Koshkin's setting. To compute a Tegmark-style Φ on a relation, one would first have to read the relation as a dynamics. Koshkin does not do that, and neither paper says how.
- For the lab (S5): the lab computes IIT 4.0 Φ with PyPhi on transition probability matrices. That quantity belongs to the IIT line (Φ3.0 here, then IIT 4.0), not to the static mutual-information measure Koshkin sketches.
