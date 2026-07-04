# Coding protocol (codebook) — reproducibility signaling in management research

Code each source from its title + abstract (and any data-availability statement text present in
the record). Code what the SOURCE signals, not what this review predicts. You are one of several
independent coders; do not consult another coder's output. When the abstract gives no signal for a
variable, code the conservative default (`no` for the three signaling variables). Disagreement is
expected and measured.

The coding rule for the three signaling variables is deliberately literal: code `yes` only when the
text states or plainly implies the practice. Absence of a statement is `no`, not `unknown` — this
review measures the *visible signal*, and a lower bound is the intended quantity.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id.
- **open_data** — does the text state that data are openly available, deposited in a repository, or
  shared (e.g. "data available at OSF/Dryad/ICPSR/GitHub", "publicly available dataset", "data and
  materials are available"): `yes` | `no`. Using a pre-existing public dataset (e.g. Compustat,
  WVS) counts as `no` unless the authors state they deposited or share their own data/extract.
- **code_available** — does the text state that analysis code, scripts, syntax, or a computational
  model are shared or available (e.g. "code available at GitHub", "replication package", "Stata/R
  scripts provided"): `yes` | `no`.
- **preregistered** — does the text state the study was pre-registered or is a registered report
  (e.g. "pre-registered on AsPredicted/OSF", "registered report", "pre-registered hypotheses",
  AEA/ClinicalTrials registration for an experiment): `yes` | `no`.
- **method_type** — the empirical approach the source uses (tests H3): `quantitative` (statistical
  analysis of numeric data — surveys, panels, archival, experiments, simulation with statistics) |
  `qualitative` (interviews, ethnography, case study, grounded theory, qualitative content
  analysis) | `mixed` (both, roughly balanced) | `conceptual` (theory/review/no primary empirical
  data — should be rare given the corpus boundary; code it if the abstract shows no empirical data).
- **year** — the publication year (copy from the corpus record).

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"smith2023","open_data":"no","code_available":"no","preregistered":"no","method_type":"quantitative","year":2023}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list
order and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts most sources signal nothing. A source that genuinely states open data / code /
  pre-registration is a real datum — record the `yes`; do not suppress it to fit the prediction.
- H2 predicts more signaling in recent years. Code the signal, not the year's expected rate.
- H3 predicts quantitative signals more. Code the method the source actually uses, and code its
  signals independently of that method.
