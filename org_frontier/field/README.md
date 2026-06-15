# Field — reading real organizations with exact Φ

The lab's verdicts are in-silico: exact Φ on small Boolean models, evidence about the models, with a
validation gap to real organizations. This directory opens the bridge across that gap. It develops a
**field protocol** for taking one real coordination arrangement — a dispatch, a handoff, a review
gate — to a dyadic/triadic verdict on an explicit, falsifiable model of it, and demonstrates the
protocol on ten mock organizations.

It is **version 0**: a discipline for honest modeling, not a validated field instrument. The mocks
are stipulated, not observed; they show the mechanics. Running the protocol on real organizations is
what will find its limits and turn it into a field-tested method.

## Read first

- [`PROTOCOL.md`](PROTOCOL.md) — the nine-step field protocol: bound one arrangement, model the
  parties, elicit the rules from evidence, pre-register, validate the instrument, compute, run the
  sensitivity step, and state the claim with what would falsify it.
- [`FINDINGS.md`](FINDINGS.md) — what the ten mocks show: a system in the middle is not enough; the
  verdict turns on the encoding; compute rather than assert; a triadic verdict still needs the
  complex to name who binds.

## Run the demo

From the repo root, with the venv active (see [`../../GETTING_STARTED.md`](../../GETTING_STARTED.md)):

```bash
python -m org_frontier.field.run
```

The run validates the instrument controls, classifies all ten mocks, reports the sensitivity flips,
and writes [`results/field_mocks.csv`](results/field_mocks.csv).

## The ten mocks

| id | organization | demonstrates |
|----|--------------|--------------|
| M1 | Ride-hail dispatch | a platform that commits a match — triadic; pooled drivers flip it dyadic |
| M2 | Relay manager | a manager who forwards is dyadic; one who synthesizes is triadic |
| M3 | Substitutable-seller marketplace | interchangeable sellers make a broadcast — dyadic |
| M4 | CI code-review gate | a gate is triadic, but its core is author–maintainer |
| M5 | EHR shift handoff | a store is dyadic; a checklist that gates is triadic |
| M6 | Franchise with ratings feedback | a closed standard–operation–rating loop is triadic |
| M7 | Algorithmic ranking | a ranking that reads creator and advertiser is triadic |
| M8 | Support-ticket triage | "just routing" reads triadic — the cycle is irreducible |
| M9 | Grievance arbitration | a ruling neither party controls is triadic |
| M10 | ERP / EDI supply link | a transparent pipe is dyadic; the system is a spectator |

These are inventions. They are a starting template for fieldwork, meant to break in contact with a
real case.

## Threads

Deep single-question dives that grow out of the mocks.

- [`threads/THREAD.md`](threads/THREAD.md) — **is the mediator in the irreducible core?** Twenty
  steps from the M4 anomaly to a structural theory of platform disintermediation: a mediating system
  is a bottleneck, an enricher, or bypassed, and which one is a property of the whole arrangement,
  not the platform. Reproduce with `python -m org_frontier.field.threads.mediator_in_core`.
- [`threads/THREAD_enricher.md`](threads/THREAD_enricher.md) — **the enricher regime, twenty deeper.**
  Genuine enrichment turns out rare (6%) and fragile, capture dominates (28%), and an outside-option
  theory falls out: a platform's irreducible core is itself plus exactly the parties with no outside
  option. Reproduce with `python -m org_frontier.field.threads.enricher_regime`.
