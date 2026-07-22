# algorithmic_management_claims

**Question.** What does the algorithmic-management literature assert versus test — the structure of its
knowledge claims and its empirical grounding? A descriptive review in the style of Simsek, Fox & Heavey
(2023) and Simsek, Heavey, Fox & Yu (2022): a body of scholarship coded as a dataset, with independent
coders and reported reliability.

**Corpus.** 66 sources on the algorithmic management of workers, 2019–2026, harvested through two
academic semantic-search connectors (Scholar Gateway + Consensus), deduplicated and screened to an
algorithm-signal-plus-work-signal boundary. See `literature/corpus.jsonl` and `literature/screened_out.jsonl`.

**Coding.** Three independent agent coders on a fixed codebook (`coding_protocol.md`), title + abstract
only, blind to one another. Variables: `claim_type`, `evidence`, `outcome`. Reliability (Fleiss' κ):
claim_type 0.747, evidence 1.000, outcome 0.895.

**Where it stands.** All three pre-registered hypotheses supported.
- H1 — outcomes skew to control + worker experience (74.2%); performance rare (4.5%). Supported.
- H2 — mostly conceptual/qualitative (69.7%); quantitative a minority (24.2%, 30.3% with mixed). Supported.
- H3 — the "algorithm controls workers" claim is a stylized fact: control-outcome sources are 0/22
  quantitative; the field's quantitative work measures worker reactions, not the control claim. Supported.

**Read next.** `hypotheses.md` (pre-registered), `FINDINGS.md` (verdicts + κ + limitations), `paper.md`
(ORM-register writeup), `results/summary.json` (registered numbers).

**Reproduce.**
```bash
python3 -m org_frontier.reviews.algorithmic_management_claims.build_corpus --sg-dir <scholar_gateway_txt_dir>
python3 -m org_frontier.reviews.lib.reliability algorithmic_management_claims/coding \
    --categorical claim_type,evidence,outcome --out algorithmic_management_claims/results/frozen.json
python3 -m org_frontier.reviews.algorithmic_management_claims.run
```
