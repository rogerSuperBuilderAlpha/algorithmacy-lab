# Discriminant boundaries — methods

## Shared infrastructure
- Verdict / Φ: `org_frontier/classifier/classifier.py` (`classify_rules`); major complex:
  `org_frontier/probes/lib.py` (`major_complex`); controls: `classifier/validate.py`.
- Python: run from the repo root with the project venv active.

## Instrument control (run first)
The battery validates the two canonical controls before any verdict.

## Construct models (fixed before the run; full rules in `discriminant.py`)
Nodes are W (worker/sender), S (system/technology), C (counterpart/receiver). Each construct is
modeled faithfully to its literature definition:
- **CMC** — parties coordinate with each other; S transmits and is a spectator. `W'=C, C'=W, S'=W`.
- **AI-MC** — S transforms the sender's message on the sender's behalf (an invertible transform); the
  recipient still coordinates with the sender's intent. `W'=C, C'=W, S'=¬W`.
- **HMC** — a two-party human-machine dyad. `W'=S, S'=W`.
- **Algorithmic management, directive** — S commits a determination reading both parties, both read it.
  `W'=S, S'=W∧C, C'=S`.
- **Algorithmic management, advisory** — S recommends to W based on W; W decides; C reads W.
  `W'=S, S'=W, C'=W`.
- **Sensemaking** — parties construct shared interpretation; S observes, does not commit. `W'=C,
  S'=W∧C, C'=W`.

## Decision rule
Convey constructs are predicted dyadic, the commit construct triadic (`hypotheses.md`). A sensitivity
construct re-models the CMC channel as committing (`W'=S, S'=W∧C, C'=S`) to test whether the verdict
flips, isolating commit-versus-convey as the operative axis.

## Reproduction
```
python -m org_frontier.studies.discriminant_boundaries.discriminant
```
Deterministic; exact Φ has no sampling. Headline numbers registered in `ci/reproduce.json`.
