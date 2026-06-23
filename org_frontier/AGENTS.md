# AGENTS.md — org_frontier (the lab and its computational program)

The hub of the lab and the home of the **computational program**: exact Φ on small Boolean models, run
through the six-stage protocol. The shared rules — git, verify, land, the done-checklist — live in the
root [`../AGENTS.md`](../AGENTS.md). This note covers what is local here.

## Where things are

- [`protocol/`](protocol/) — the six-stage pipeline (review → research → fix five hypotheses → methods →
  run against exact Φ → paper). `RESEARCH_PROTOCOL.md` is the spec; `question_pipeline.js` runs it.
- [`probes/`](probes/) — `probe_<slug>.py` scripts, each a self-contained exact-Φ experiment, logged in
  `PROBES.md` under one global numbering.
- [`questions/`](questions/) — each question taken end to end, under `q<NN>_<slug>/`.
- [`classifier/`](classifier/), [`corpus/`](corpus/), [`multiparty/`](multiparty/),
  [`principal/`](principal/), [`proxy_bridge/`](proxy_bridge/) — the shared instrument and sub-studies.
- [`STRUCTURAL_FINDINGS.md`](STRUCTURAL_FINDINGS.md) — the standing synthesis. The empirical and bridge
  arms (`qualitative/`, `recurrence/`, `survey/`, `field/`, `cognition/`) carry their own nested notes.

## Add work here

- **A probe:** write `probes/probe_<slug>.py` whose docstring states question, hypothesis, method, and run
  command; print exact numbers; add a row to `probes/PROBES.md`. Reuse `probes/lib.py`, `probes/_info.py`,
  `classifier/`, and `foundations/proxy_audit/exact_phi.py` rather than rebuilding.
- **A full question:** copy `protocol/template/` (or run the pipeline) into `questions/q<NN>_<slug>/`.

## Verify

- Validate the instrument on a known control before any comparison; compute, do not assert; report nulls.
- Register every reported number in [`../ci/reproduce.json`](../ci/reproduce.json) and run
  `python ci/reproduce.py` from the repo root.
- Run `python tools/build_index.py` so the new probe or question is indexed, then the `--check`.
