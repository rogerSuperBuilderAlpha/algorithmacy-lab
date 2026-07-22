# Coding protocol (codebook) — <review title>

Code each source from its note or abstract. Code what the SOURCE argues, not what this review predicts.
You are one of several independent coders; do not consult another coder's output. When a variable does
not apply, use `na`. When genuinely unsure between two values, pick the better fit — disagreement is
expected and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id.
- **<categorical_var>** — <closed set of values>: `<v1>` (rule) | `<v2>` (rule) | `na`.
- **<categorical_var>** — <...>.
- **<set_var>** — the list of <dimensions> the source SUBSTANTIVELY develops, from: `<a>`, `<b>`, `<c>`.
  Empty list `[]` if none.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"...","<var>":"...","<set_var>":["a","b"]}`

Code every source in the corpus. If capacity runs low, code in list order and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- <H_x predicts ...>. A source that genuinely reads the other way is a real disconfirming datum;
  record it.
