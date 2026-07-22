# reproducibility_signaling

**Question.** How often do recent management and organization empirical papers signal reproducibility
practices — open data, code availability, pre-registration, or shared materials — and is that
signaling rising over 2015–2025? A descriptive review in the style of Simsek, Fox & Heavey (2023).

**Corpus.** 88 empirical management/OB/strategy/HR papers, 8 per year across 2015–2025, harvested via
the Scholar Gateway semantic-search connector and screened to empirical work (`literature/corpus.jsonl`).

**Design.** Three independent agent coders apply `coding_protocol.md` to each title + abstract, coding
`open_data`, `code_available`, `preregistered` (each yes/no), and `method_type`. Reliability is Fleiss'
κ via `lib/reliability.py`; the adjudicated dataset is `results/frozen.json`.

**Hypotheses** (pre-registered in `hypotheses.md`):
- **H1** — signaling is uncommon overall (any-signal a minority).
- **H2** — signaling rose 2015–2019 → 2020–2025.
- **H3** — quantitative papers signal more than qualitative ones.

**Findings** live in `FINDINGS.md`; the write-up is `paper.md`.

**Load-bearing limitation.** Coding is abstract-only. Data-availability statements that live in the
paper body are invisible to it, so every reported rate is a **lower bound**.

**Reproduce.** See the block at the foot of `methods.md`.
