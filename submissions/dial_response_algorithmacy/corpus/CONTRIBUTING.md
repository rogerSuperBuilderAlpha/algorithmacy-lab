# Contributing to the sci-fi interfaces catalog

This track is meant to grow by contribution. Speculative fiction and adjacent HCI tropes are a shared laboratory for reading algorithmacy; competing takes are welcome. You do not need permission or a lab appointment to add a work or an alternative interpretation.

## What this packet is

| Object | Role |
| --- | --- |
| [`essay.md`](essay.md) | Seed narrative (imported manuscript). Stable reference; do not rewrite the argument lightly. |
| [`works/`](works/) | **Living research object** — one file per show or paradigm. Expand here. |
| [`CLAIM.md`](CLAIM.md) | Locked claim for the arm as a whole. |
| Research stub | [`../../../org_frontier/essays/scifi_interfaces_and_algorithmacy.md`](../../../org_frontier/essays/scifi_interfaces_and_algorithmacy.md) |

No Φ numbers and no fake empirical results in this folder. Fiction is taxonomy and motive. Exact-Φ probes belong under `org_frontier/` with hypotheses registered before compute.

## Add a new sci-fi work or paradigm

1. Copy [`works/_TEMPLATE.md`](works/_TEMPLATE.md) to `works/<slug>.md` (lowercase, underscores; e.g. `works/black_mirror_nosedive.md`).
2. Fill every section: interface paradigm, algorithmacy / triadic coordination, cognitive integration, historical analogy, modes of resistance, open questions.
3. Keep **Alternative interpretations** as a heading even if empty, so others can append.
4. Add a row to the catalog table in [`README.md`](README.md).
5. Open a PR into **`contrib`** (see below).

## Add an alternative interpretation

1. Open the existing `works/<slug>.md`.
2. Append under **Alternative interpretations** — do **not** delete or overwrite prior readings (including the seed).
3. Use a short `###` heading, then **Author:** Name · **Date:** YYYY-MM-DD, then one or two paragraphs stating where the reading differs.
4. Cite scenes, UI details, or design moves. Do not invent integrated-information numbers.
5. Open a PR into **`contrib`**.

Alternative interpretations are first-class. Disagreement is a feature of the catalog.

## Propose a pull request

The lab integrates on **`contrib`** (not direct pushes to `main`).

```bash
git fetch origin contrib
git checkout -b cultural/scifi-<short-slug> origin/contrib
# edit works/… and README catalog table
git add submissions/dial_response_algorithmacy/corpus/
git commit -m "docs(scifi): add <work or alternative>"
git push -u origin cultural/scifi-<short-slug>
# open a PR with base = contrib
```

House operating rules (instrument, reproduce, no outreach on the project's behalf) live in root [`AGENTS.md`](../../../AGENTS.md) and [`PUBLISHING.md`](../../../PUBLISHING.md). For this cultural arm, the bar is: clear prose, signed alternatives, no fabricated results.

## Tone of review

Reviewers check structure and scope (template filled; no fake Φ; alternatives appended not replaced). They do not gatekeep taste in franchises. A thin first entry that invites alternatives is better than waiting for a perfect monograph.
