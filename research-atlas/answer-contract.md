# Research atlas answer contract

An answer is a JSON object with `question`, `answer`, and `claims`. Each claim has
`text`, `kind`, and one or more `evidence` entries. Evidence names a repo `path`,
the exact `quote` used, and the full Git commit `snapshot` where that quote appears.
The checker reads the quoted file at that commit, so a later edit cannot silently
change what an answer cited. Keep quotes short; the answer should explain them.

Claim kinds are `model_result`, `open_question`, and `research_target`.

- `model_result` states what a specified computation or synthetic panel found.
  It must say that the result is about a model or synthetic data, not a real
  workplace.
- `open_question` keeps the question open. A proposed test is not a finding.
- `research_target` describes a goal that has not been measured. It must not
  state the target score as an observed agreement score.

Every factual sentence in `answer` must be covered by a claim and its evidence.
Do not promote a catalog summary or a reproduction command into field evidence.
Run `python3 research-atlas/check_answers.py` to check the fixtures and their
snapshot quotes.
