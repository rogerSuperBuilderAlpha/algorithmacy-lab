# llm_variance — the variance problem of language-model outputs

When N people ask one language model the same question, or one person asks N times, the answers look
diverse. This program measures how much of that diversity is real. The answers vary in wording, vary less in
layout, and often barely vary in content, so the effective number of independent answers is far below N.
Treating N model responses as N independent observations overstates the sample. That gap is the variance
problem.

The program builds an instrument for it: a layered similarity decomposition (lexical, structural, semantic)
that yields an effective sample size per layer, a consensus-core analysis over a coded claim taxonomy, and a
modest integrated-information reading of how claims bundle. Each study pre-registers its hypotheses, commits
its data, and registers a reproduce check, following the lab protocol.

## Studies

- **[best_time_pilot](best_time_pilot/README.md)** — the first pilot. Four student ChatGPT answers to "what
  was the best time in history?", read across the three layers. Establishes the instrument on N=4 and
  specifies the scaled study (full class N, re-run vs. vary-the-prompt, temperature sweep).

## Run

```
python org_frontier/llm_variance/best_time_pilot/analyze_variance.py
```
