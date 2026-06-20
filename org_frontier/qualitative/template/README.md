# Qualitative study template

A study lands in `org_frontier/qualitative/<slug>/` as its own subdirectory, built from this template. Copy
the two files into the new directory and fill them.

## Files

- `coding_scheme.md` — the interview guide, coding scheme, and bit calibration. **Commit this before the
  fieldwork**, so the git history shows the questions were fixed before the answers. This is the qualitative
  form of the lab's hypotheses-before-results discipline.
- `STUDY.md` — the writeup. Its first heading is the study title and its first paragraph is the summary the
  directory builder shows, so open with a one-line statement of the setting and the finding.

## The two modes

- **Stand-alone.** A thick description of a coordination setting, valued on its own. No verdict is computed.
  Fill the setting, parties, methods, and findings sections of `STUDY.md`; leave the model and verdict
  sections marked not applicable.
- **Model-bound.** A study that takes the arrangement through the [field protocol](../../field/PROTOCOL.md)
  to a dyadic or triadic verdict. Fill every section, including the elicited rules and the verdict
  pre-registered before computing.

## Discipline

Name the prior the setting is read against, from [TOPICS.md](../TOPICS.md) or the catalog. Ground each rule
in evidence and record one alternative the evidence does not rule out. Where the parties disagree about what
determines an action, model both readings and report the finding under each. Follow the house style in the
repo `CLAUDE.md`.

For work aimed at a real journal, [PUBLISHING.md](../PUBLISHING.md) sets the bar — fit, authenticity,
trustworthiness, a transparent path from data to theory, and a theoretical contribution — grounded in Bansal
and Corley's 2012 AMJ editorial. The `STUDY.md` sections carry those elements.

## Indexing and review

Run `python tools/build_index.py` so the study appears in the README directory. A qualitative study registers
no number in `ci/reproduce.json`, since it computes none; the `directory-current` check confirms it is
indexed. Open a pull request into `contrib`; a maintainer reviews the argument, the evidence per rule, and
the prose.
