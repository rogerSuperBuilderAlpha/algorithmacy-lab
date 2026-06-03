# org_frontier — an aggressive, collaborative pyphi applications lab

This directory is the companion to [`../dissertation/`](../dissertation/), run without the
dissertation's constraints. The dissertation develops a measurement methodology through case
studies and lets that play out carefully. This lab moves faster. It exists to do two things:

1. **Map how the world uses PyPhi.** Understand who runs IIT computations, in what fields, on
   what systems, with what code and what open problems. The survey lives in
   [`landscape/`](landscape/).
2. **Build new organizational-theory applications of exact IIT-4.0 Φ**, and contribute the tools
   and findings back to the PyPhi research community.

The repo's [`../RESEARCH_PLAYBOOK.md`](../RESEARCH_PLAYBOOK.md) governs every sub-project here: run
the full deep-research harness, validate the instrument on its own controls before any comparison,
compute rather than assert, and write in the house style in [`../CLAUDE.md`](../CLAUDE.md).

## Sub-projects

- [`landscape/`](landscape/) — a worldwide survey of PyPhi usage. Who uses it, for what, and where
  the open application gaps are, with organizational and social-system applications flagged.
  *Complete: report, bibliography, and synthesis in [`landscape/`](landscape/).*
- [`classifier/`](classifier/) — the literacy-or-algorithmacy classifier. Drop in a coordination
  model, get a structural verdict: Φ_MIP = 0 → dyadic → literacy; Φ_MIP > 0 → triadic →
  algorithmacy. *Scaffolded and validated; reuses the dissertation's proven 3-node oracle.*
- [`corpus/`](corpus/) — a curated, reusable library of named coordination forms with exact
  IIT-4.0 Φ, the verdict, and structural tags, plus a single-edge ablation table. *Built; 8 forms,
  0 mismatches.*
- [`essays/`](essays/) — public-facing writeups. First essay:
  [`literacy_or_algorithmacy.md`](essays/literacy_or_algorithmacy.md) — how the world uses PyPhi, and
  the theory that exact Φ decides whether a coordination form demands literacy or algorithmacy.

## Contributing back to the PyPhi community

The framing is **two layers, explicit**: lead with the domain-neutral structural result for the
PyPhi audience, keep the organizational application as a clearly-marked second layer.

- [`COMMUNITY_NOTE.md`](COMMUNITY_NOTE.md) — the two-layer writeup: the structural finding
  (topology does not decide irreducibility), the reusable artifacts, and the org application.
- [`ANNOUNCEMENT_DRAFT.md`](ANNOUNCEMENT_DRAFT.md) — a `pyphi-users` post **staged for the human to
  send** (outward correspondence is the human's call; see its pre-send checklist). Not sent
  automatically.

Further sub-experiments are added as the survey surfaces opportunities. Each gets its own folder
following the playbook's reusable layout. The survey's shortlist of next builds is in
[`landscape/SURVEY_FINDINGS.md`](landscape/SURVEY_FINDINGS.md): a public classifier, a proxy bridge
for organizational time-series data, and a reusable coordination-form TPM library.
