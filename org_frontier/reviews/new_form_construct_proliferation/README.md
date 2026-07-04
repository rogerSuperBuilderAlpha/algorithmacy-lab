# new_form_construct_proliferation

**Question.** How many distinct construct labels does organization theory give the "new organizational
form," and do the label-camps cite each other or proliferate in isolation? A jangle-fallacy metascience
study, in the style of Simsek, Fox & Heavey (2023) and Simsek, Heavey, Fox & Yu (2022).

**Where it stands.** Complete. Corpus N = 67 (screened from 108). Three independent agent coders;
Fleiss' k = 0.966 on the construct label. Full citation graph harvested (67 seeds).

| # | Hypothesis | Verdict |
|---|---|---|
| H1 | >8 distinct labels for overlapping "new form" phenomena | **Supported** — 8 closed-set labels in use + ~10 in the `other` tail (about 18 total) |
| H2 | Form defined by contrast to hierarchy/market, not positive mechanism | **Challenged** — positive_mechanism 60% vs by_contrast 40% |
| H3 | Label-camps cite within-camp far more than across (block-diagonal) | **Qualified** — within 19 / cross 20 links; hub-and-spoke via meta-organization; 7,082 of ~7,400 external citers span one camp |

**Files.**
- `hypotheses.md` — pre-registered (committed before harvest/coding).
- `coding_protocol.md`, `methods.md` — codebook and procedure.
- `literature/corpus.jsonl` (67), `literature/screened_out.jsonl` (41), `literature/references.bib`.
- `seeds.json`, `clusters.json` (slug -> adjudicated label), `edges/` (per-seed citation graph).
- `coding/coder{A,B,C}.jsonl`, `results/frozen.json` (adjudicated), `results/bibliometrics.txt`.
- `FINDINGS.md` (verdicts + k + limitations), `paper.md` (~2,800w, ORM register), `ci/reproduce.json`.

**Reproduce.** See `FINDINGS.md` "Reproduce" or `ci/reproduce.json`.
