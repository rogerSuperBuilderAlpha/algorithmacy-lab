# Working in `org_frontier/reviews/`

Local operating rules for the literature-experiments arm. The root [`AGENTS.md`](../../AGENTS.md) still
governs — the map, the git trap (nearest `.git` decides the remote; never touch the nested
`dissertation/`), the land flow (branch off `contrib`, PR into `contrib`, never `main`), and the
done-checklist. This file adds what is specific here.

## What this arm does

Runs experiments on a body of literature: states falsifiable claims about a field and tests them with
a coded corpus and its citation graph. Read [`README.md`](README.md) for the paradigm,
[`RESEARCH_PLAYBOOK.md`](RESEARCH_PLAYBOOK.md) for the procedure, and
[`METHODS_FOUNDATIONS.md`](METHODS_FOUNDATIONS.md) for where the method comes from.

## The pipeline

Envision → Explicate → Execute → Encode → Evaluate → Exposit. The playbook is the long form. The
non-negotiables:

- **Commit `hypotheses.md` before any result.** In its own commit, before harvesting or coding. The
  git history is the pre-registration; a hypotheses file added in the same commit as the findings does
  not count.
- **At least three independent coders, and report Fleiss' κ.** The reliability figure is the point of
  the genre — it is the answer to "one reader coded it." Coders are LLM agents run in parallel on the
  same codebook, blind to one another (see [`lib/README.md`](lib/README.md)).
- **Measure, do not assert.** Any claim of the form "these literatures ignore each other" or "no one
  has done this" is a citation-graph test, not a sentence. Run it.
- **Report challenges.** A hypothesis the data contradict is a finding, written plainly. Do not quietly
  drop it.

## Starting a review

Copy [`template/`](template/) to `<slug>/` (`lower_snake_case`), fill `hypotheses.md`, commit it, then
work the pipeline. Each review is a directory with a `FINDINGS.md` — that file is the marker the index
generators count, so a review without one does not appear in `MAP.md` or the README directory.

## After adding or finishing a review

Run the done-checklist from the root `AGENTS.md`. Specifically:

```bash
python tools/build_map.py && python tools/build_index.py     # regenerate the indexes
python tools/build_map.py --check && python tools/build_index.py --check
python ci/reproduce.py                                        # if you registered numbers
```

Register any headline number a `FINDINGS.md` reports in `ci/reproduce.json` so CI can reproduce it.

## Copyright

Commit only open-access PDFs to `literature/pdfs/`. Paywalled sources get a `references.bib` entry with
the DOI and an OA-status note, never the PDF. The two method papers in
[`METHODS_FOUNDATIONS.md`](METHODS_FOUNDATIONS.md) are paywalled and are referenced, not stored.
