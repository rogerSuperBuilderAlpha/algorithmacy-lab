# best_time_themes — the values in four answers

The second reading of the class exercise. best_time_pilot measured how far apart the four ChatGPT answers to
"what was the best time in history?" are in wording and which eras they name. This study asks a different
question: what values and worldview do the answers carry, and do they lean a consistent direction?

The four answers are rated on five value axes — progress, equity critique, material vs. cultural, Western vs.
global, committed vs. relativist — and two framing flags, by three coders blind to the hypothesis and to each
other. The aggregated coding is frozen; `analyze_themes.py` computes the value statistics and tests whether
the four share a directional worldview, whether the push is overt or subtle, and where the values genuinely
diverge.

Inter-coder reliability is the gate. A slant that independent readers do not converge on is not in the text.

The study reports structure, not intent: a consistent lean may reflect evidence and consensus rather than
bias, and that normative question is flagged, not resolved.

## Files

- `HYPOTHESES.md` — the gate and H1–H5, fixed before any coding.
- `data/CODEBOOK.md` — the five value axes, two framing flags, and the coding procedure.
- `data/values_coding.csv` — the frozen aggregated (median-of-three) coding.
- `data/coder_raw.csv` — the three coders' raw scores, for the reliability gate.
- `analyze_themes.py` — the analysis.
- `FINDINGS.md`, `paper.md` — results and write-up.

The raw responses are the canonical anonymized set in `../best_time_pilot/data/responses.csv`.

## Run

```
python org_frontier/llm_variance/best_time_themes/analyze_themes.py
```
