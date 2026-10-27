# Argument: an exact test of triadic coordination as shared research infrastructure

[DRAFTED by Claude, 26 Oct 2026. For the author's ruling.]

**P1.** Organization science has no shared, exact test for whether a coordination form is irreducibly three-party or factors into two-party relations. Studies of platforms and algorithmic management decide this by description.
- *Warrant:* the triad is asserted in that literature, not computed. Curchod et al. name "triadic relationships", and Cameron draws an "Algorithmic Labor Triangle", but neither offers a test.
- *Sources:* `lima_pdw/literature/cards/curchod2020.md`; `lima_pdw/literature/models/cameron2024.md` (the triangle and Table 1); the OT claim-check addendum of 11 Oct 2026 (untracked, outside this repo: the author's `wt-algorithmacy-ot` worktree, `submissions/algorithmacy_ot/manuscript/gdoc_2026-10-10/CLAIM_CHECK_ADDENDUM_2026-10-11.md`) places the "Algorithmic Labor Triangle" at p. 466 and finds "irreducible", "triad" and "dyad" absent from the article.

**P2.** Integrated information computed over the minimum-information partition gives such a test for a formal model of a coordination form. Φ_MIP = 0 means some party-respecting cut factors the form; Φ_MIP > 0 means none does. The lab has built this as a classifier and run it under an AI-assisted pipeline that fixes hypotheses before computing.
- *Sources (repo files):*
  - `org_frontier/classifier/README.md`
  - `org_frontier/STRUCTURAL_FINDINGS.md`: in the complete 256-form strict-mediation family at n = 3, 24 forms (9.4%) are triadic (`ci/reproduce.json` checks 303 and 503); P(triadic | mediator reads both) = 15.0%; time-series proxies separate dyadic from triadic "only near chance (rank-AUC ≤ 0.63)" (`org_frontier/proxy_bridge/FINDINGS.md`: 0.563 and 0.629; no CI check yet).
  - `org_frontier/protocol/RESEARCH_PROTOCOL.md`

**C.** Released as open infrastructure, the classifier and pipeline let organization scientists turn a described arrangement into a formal model and get an exact, reproducible verdict on its structure. It also shows that the intuitive rule (the mediator reads both parties) over-calls triads: most forms that meet it still factor. That makes it a principled instrument for exploring which arrangements demand triadic competence.
- *Boundary:* the verdicts are about Boolean models. A validation gap separates them from claims about real organizations (`org_frontier/README.md`, line 19).
