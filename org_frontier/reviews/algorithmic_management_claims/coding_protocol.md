# Coding protocol (codebook) — algorithmic-management knowledge claims

Code each source from its title + abstract only. Code what the SOURCE does and claims, not what this
review predicts. You are one of several independent coders; do not consult another coder's output. Use
`na` where a variable genuinely does not apply. When unsure between two values, pick the better fit —
disagreement is expected and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id (copy verbatim from the corpus record).

- **claim_type** — the knowledge-weaving type of the source's central claim about algorithmic management
  (tests H3):
  - `stylized_fact` — asserts, as established, that algorithmic management is a (new) form of control
    over workers, or otherwise treats a control/domination effect as a settled fact the paper builds on.
  - `assumption` — takes the control/reconfiguration framing for granted to motivate a study of
    something else (an antecedent, a coping response, a design feature), without itself asserting the
    control claim as its headline.
  - `critique` — disputes, complicates, or bounds a prevailing claim about algorithmic management (e.g.
    argues control is partial, resisted, negotiated, or overstated; challenges the "new" in new control).
  - `omission` — its central move is to note a gap, call for research, or flag what the field has not
    addressed.
  - `na` — not codable as any of these (rare; use sparingly).

- **evidence** — the source's evidentiary base (tests H2):
  - `conceptual` — theory, review, essay, framework, or agenda; no new primary data analyzed.
  - `qualitative` — interviews, ethnography, case study, netnography, document/interview analysis.
  - `quantitative` — survey, field/lab experiment, platform log or trace data, statistical modeling as
    the primary evidence.
  - `mixed` — combines qualitative and quantitative primary data in one study.
  - `na` — indeterminable from title + abstract.

- **outcome** — the source's primary outcome or focal phenomenon (tests H1):
  - `control` — control, surveillance, monitoring, discipline, power, domination, datafication of work,
    managerial authority, algorithmic direction/evaluation of workers.
  - `worker_experience` — workers' experience, wellbeing, meaning, identity, autonomy-as-felt,
    resistance, coping, emotion, fairness perceptions, job quality as experienced.
  - `performance` — productivity, efficiency, firm/operational performance, service quality, task or
    platform performance outcomes.
  - `other` — anything else (labor law/regulation, market/matching design, ethics-in-the-abstract,
    methods, consumer-side effects).
  - `na` — indeterminable.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"kellogg2020","claim_type":"stylized_fact","evidence":"conceptual","outcome":"control"}`

Code every source in the corpus (`literature/corpus.jsonl`), in list order. If capacity runs low, code
in order and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts `performance` is rare. A source whose focal outcome genuinely is productivity or firm
  performance is a real datum — code it `performance` even though the review expects few.
- H2 predicts `quantitative` is a minority. A survey or log-data study is a real disconfirming datum —
  code it `quantitative`.
- H3 predicts control-stylized-fact sources are conceptual/qualitative. If a source both asserts the
  control claim as established AND tests it with quantitative data, that is exactly the disconfirming
  case — code it honestly (`stylized_fact` + `quantitative`).
