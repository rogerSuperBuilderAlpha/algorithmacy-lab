# corpus — a curated coordination-form library with exact IIT-4.0 Φ

A small, documented, reusable set of named coordination forms, each rendered as an
application-layer discrete system and labeled with exact IIT-4.0 Φ over the minimum-information
partition, the dyadic/triadic verdict, and structural tags. Built on the
[`classifier/`](../classifier/) and the repo's exact-Φ oracle.

This is the curated companion to the dissertation's complete 4,096-wiring enumeration
(`dissertation/paper3_baseline/catalog.py`), which is a coverage/null check over every Boolean
coupling. This library is the opposite: a few *recognizable* forms, each with a documented
rationale, meant to be reused and extended. Five forms are validated in the dissertation's
Paper 2; three are first-pass models, flagged `validated=False`.

## Run

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.build
```

Writes `results/corpus.csv` (every form: Φ, verdict, structural tags) and `results/toggles.csv`
(single-feature ablations on the triadic forms).

## What it shows

See [`FINDINGS.md`](FINDINGS.md). The structure-first result: irreducibility of a small mediated
system is **not** decided by topology. Strict mediation (no direct worker–counterpart channel) is
necessary but not sufficient, and even "the mediator reads both parties" is not sufficient — the
parties' own read functions have to keep them live to the mediator's commit. The ablations confirm
it: dropping the mediator's dependence on the counterpart flips every triadic form to dyadic.

## Files

- `forms_library.py` — the forms, each with rationale, validation flag, and structural tags.
- `build.py` — computes Φ for every form; runs the toggle ablations; writes the CSVs.
- `results/corpus.csv`, `results/toggles.csv` — the labeled dataset and the ablation table.
- `FINDINGS.md` — numbers and the structure-first reading.

## Extending it

Add a `Form(...)` to `forms_library.FORMS` with per-party Boolean rules and a one-line rationale.
Keep the TPM derived from the form's actual coupling, never tuned to a target Φ. Next forms to add
defensibly: a two-sided market with prices, a multi-level hierarchy (n>3), a commons. Each needs a
justified application-layer coupling before it earns `validated` status.
