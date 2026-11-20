<!-- DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026. Measured figures for v8's pacing. The counts come from tools/style_counts.py, which counts and writes no prose. The targets are guidance for Stage 5, not gates; the section weights in MODEL_BRIEF.md are the gate. -->

# Style profile: the model, v7, Pierre's original and the target for v8

## How the figures were made

- **The model** is measured on the 332 sentences transcribed by hand into `MODEL_FULL.md` (git-ignored), grouped into the 67 paragraphs found from the first-line indents of the typeset PDF. Displayed quotations are left out.
- **The drafts** are measured with a regex sentence splitter on the body, from the introduction to the acknowledgments or references, without headings, tables or comments.
- **The splitter was checked on the model before it was used on anything else.** Its first version matched abbreviations such as 'p.' and 's.' inside ordinary words and found 259 sentences against the hand count of 332. Fixed to match whole words, it finds 327 against 332, with equal counts in 58 of 67 paragraphs and a mean sentence length of 27.3 against 26.9. The remaining differences are lead-ins joined across a displayed quotation and quotations that hold two sentences. Splitter figures for the drafts therefore run slightly long, by about half a word in the mean.

Commands, from `manuscript/`:

```sh
python3 v8_2026-11/tools/style_counts.py model rewrite_2026-11/journal/corpus/germannmolz2018/MODEL_FULL.md
python3 v8_2026-11/tools/style_counts.py check rewrite_2026-11/journal/corpus/germannmolz2018/MODEL_FULL.md
python3 v8_2026-11/tools/style_counts.py draft DRAFT_v7.md
git show 3e6828b1:submissions/hospitality_phygital/manuscript/DRAFT.md > /tmp/pierre.md   # then: draft /tmp/pierre.md
```

## The figures

| | Model (hand) | v7 | Pierre, 3e6828b1 | v4 (`DRAFT.md`) | Target for v8 |
|---|---|---|---|---|---|
| Body words | 8,925 | 8,632 | 7,741 | 8,794 | ≤ 9,000 by `wordcount.py` |
| Sentences | 332 | 267 | 395 | 449 | ~330–370 |
| Mean sentence (words) | **26.9** | **32.3** | **19.6** | 19.6 | **24–27** |
| Median | 25 | 32 | 17 | 17 | 22–25 |
| Spread (sd) | 13.0 | 11.5 | 11.7 | 12.4 | ≥ 12 |
| 10th / 90th percentile | 11 / 45 | 17 / 46 | 7 / 35 | 7 / 35 | ~10 / ~45 |
| Sentences of 10 words or fewer | 8% | 3% | 25% | 26% | 8–15% |
| Sentences of 40 words or more | 18% | 27% | 6% | 6% | ≤ 18% |
| Paragraphs | 67 | 46 | 61 | 62 | ~62–70 |
| Mean paragraph (words) | **133** | **188** | **127** | 142 | **125–150** |
| Median paragraph / range | 120 / 53–261 | 179 / 10–433 | 118 / 11–281 | 128 / 14–313 | spread from ~50 to ~260 |
| Questions per 1,000 words | 1.3 (12) | 1.0 (9) | 2.1 (16) | 1.8 (16) | ~1, singly |
| 'I/my/me' per 1,000 | 5.4 | 0.2 | 0 | 0 | 0 (two authors) |
| 'We/our/us' per 1,000 | 5.3 | 7.1 | 5.2 | 5.1 | 4–8 |
| Dashes per 1,000 | 6.1 | 0 | 0 | 0 | 2–6, spaced en-dash |
| Semicolons per 1,000 | 4.8 | 2.9 | 8.8 | 6.5 | 3–6 |
| Parenthetical citations per 1,000 | 9.5 | 16.3 | 12.5 | 13.1 | ≤ 12 |
| 'In other words' | 4 | 0 | 0 | 0 | 2–4 |
| Scholar with first name and trade | 5 | 0 | 0 | 0 | 4–8, where the scholar carries a claim |
| Single / double quotation marks | 174 / 14 (nested) | 243 / 2 | 25 / 35 | 55 / 0 | single; double only nested |

## What the figures say

**v7 is too dense in both directions.** Its sentences run five words longer than the model's on average and its short sentences have nearly gone (3% at ten words or fewer, against her 8%). Its paragraphs average 188 words, with one of 433. It cites in parentheses at 16 per 1,000 words, against her 9.5, because chains of doctrine sit inside the sentences.

**Pierre's original runs short.** A quarter of his sentences have ten words or fewer, and his mean is seven words under hers. His paragraphs, at 127 words, already sit on the model's.

**Her pacing lies between them.** She writes a long sentence and then a short one: 'Both videos also hint at a discourse of scale' (GM.016, nine words) after 38 words; 'What do they owe each other?' (GM.135, six words) after 44. A v8 that carries Pierre's short sentences verbatim inside v7's argument, rewritten to her length, should land near her figures without forcing either. The targets above assume that mix.

**Two practical consequences.**

1. Pierre's sentences use double quotation marks (35 against 25 single). The journal asks for single. Converting his marks is a mechanical change, not a rewording, and the Pierre ledger records it once for all his sentences.
2. Parenthetical citations come down from 16 to 12 per 1,000 or fewer by two means the model uses: the scholar as subject of the sentence ('geographer Eugene McCann (2003: 160) puts it'), and grouping sources by type in one sentence (GM.154, GM.181). The plan's other means, moving case detail into Table 1, keeps every reference in the paper.

## The clarity floor: Roger's abstract

Roger's rewritten abstract (`USER_ABSTRACT_2026-11-13.md`) is 186 words in seven sentences: 22, 25, 23, 18, 25, 41 and 32 words, a mean of 26.6. That matches the model's mean almost exactly. It states the claim, then binds it, then extends it, then names the material, each in one sentence, with no figure of speech and no sentence about the paper's own care. It is the floor for the whole of v8: no sentence should be harder to read than its hardest, the 41-word sentence on the further duty.

The abstract leaves 14 words under the journal's limit of 200. The phygital positioning it needs (D1) will not fit in 14 words without a trim, so at Stage 5 any trim is proposed to Roger, not made.

## Headings

The journal's Notes for Contributors ask for bold Times New Roman 12 point (`JOURNAL_SPEC.md`). The typeset model sets main headings in capitals and subheadings in bold italic (p. 231), and Roger's review asks for capitals. v8 sets main headings in bold capitals and subheadings in bold italic, which meets both.
