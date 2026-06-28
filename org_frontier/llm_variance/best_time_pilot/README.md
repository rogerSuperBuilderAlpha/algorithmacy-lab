# best_time_pilot — four answers to one question

A class exercise. Each student opened a fresh, signed-out ChatGPT session and asked the identical prompt,
"what was the best time in history?", then submitted the answer. Four distinct answers came back. An earlier
collection pass also produced a byte-identical duplicate of one answer, kept here as an instrument control.

The pilot reads the four answers across three similarity layers and asks how much of their diversity is
real:

- **Lexical** — token-Jaccard and TF-IDF cosine on the raw text (wording).
- **Structural** — Ward clustering of layout features (the template).
- **Semantic** — Jaccard over a hand-coded claim/era taxonomy (content).

From the three kernels it computes an effective sample size per layer, n_eff = N² / (1ᵀ K 1), a
consensus-core analysis of which eras the answers name, and a pairwise integration reading of how claims
bundle. The headline: the answers diverge in wording, collapse to a few templates, and nearly agree in
content, so the four responses are far from four independent draws.

This is a pilot at N=4. It establishes the instrument and fixes the model; it is not a powered estimate. The
scaled study it motivates is specified in `FINDINGS.md` and `paper.md`.

## Files

- `HYPOTHESES.md` — the gate and H1–H5, fixed before the analysis.
- `data/responses.csv` — the four anonymized answers plus the duplicate control.
- `data/claims_coding.csv` — the hand-coded response×claim incidence matrix.
- `data/CODEBOOK.md` — the claim taxonomy and inclusion rules.
- `analyze_variance.py` — the analysis.
- `FINDINGS.md`, `paper.md` — results and write-up.

## Run

```
python org_frontier/llm_variance/best_time_pilot/analyze_variance.py
```
