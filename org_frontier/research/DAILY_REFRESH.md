# Daily refresh — the playbook the watch runs

The procedure a daily run follows, written so a fresh session can execute it without further context. The
autonomous cron fires this; a person can run it by hand the same way. It does a full re-research of every
program and every topic, rewrites the reviews and bibliographies, logs what changed, and lands the result.

## Procedure

1. **Sync.** From the repo root, fetch and branch off `contrib`:
   `git fetch origin contrib && git checkout -b research/refresh-<date> origin/contrib`.
2. **Research each program.** For each of the six programs below, run deep research on its seed question:
   real search across the web and the academic databases (WebSearch/WebFetch plus the Consensus and
   Semantic-Scholar / Scholar_Gateway MCP tools), restricted to work newer than is already cited where the
   point is to catch new papers. Synthesize the program-level review and write its bibliography.
3. **Confirm the ten topics.** Each program holds ten topics (listed in its `README.md`). Re-research each
   topic the same way and rewrite its `REVIEW.md` and `references.bib`. If the program-level research surfaces
   a topic that has displaced one of the ten, swap it and note the swap in the changelog.
4. **Verify before writing.** Pair every research pass with an adversarial check: confirm each DOI / arXiv ID /
   URL resolves and each claim attributed to a source holds. Drop anything that fails; never fabricate a
   citation to fill a gap.
5. **Write the outputs.** Overwrite each `REVIEW.md`, `literature/deep_research_report.md`, and `references.bib`.
   Open every program report with the metadata line `<!-- run: YYYY-MM-DD | sources: N | verified: M -->`.
   Dedupe each program `references.bib` as the union of its topic bibliographies plus the program-level finds.
6. **Log and index.** Append a dated entry to [`CHANGELOG.md`](CHANGELOG.md): per program, the papers added and
   removed and the new source counts. Regenerate the index: `python org_frontier/research/build_research_index.py`,
   then `python tools/build_index.py`.
7. **Land it.** Commit, push, open a PR into `contrib` with the changelog entry as the body, confirm CI is
   green (`directory-current`), admin-merge, then promote `contrib` to `main`. Delete the branch.

## The six seed questions

- **computational** — exact integrated information and IIT 4.0 applied to coordination; integrated information
  beyond neuroscience; organizational coordination theory; cooperative-game structure of joint action; the
  size ceiling on exact Φ and proxies for it.
- **field** — organizational ethnography and field methods for sociotechnical systems; platform and gig-work
  fieldwork; eliciting decision or determination rules from interviews, observation, and documents;
  inter-rater reliability and bit calibration in coding real coordination.
- **qualitative** — qualitative methods for organizations (Gioia methodology, trustworthiness criteria,
  disagreement as data); sensemaking; qualitative studies of algorithmic management and worker experience of
  opaque systems.
- **recurrence** — cross-recurrence quantification analysis and recurrence plots; coordination and interpersonal
  dynamics from time series; lead-lag, coupling, and synchrony measures; comparison with Granger causality,
  transfer entropy, and convergent cross mapping.
- **survey** — scale development and psychometrics (CFA, measurement invariance, McDonald's omega, latent
  growth); algorithmic literacy, competence, and awareness measures; panel designs for skill acquisition in
  workers coordinating through systems.
- **cognition** — theories of mind and coordination (computationalism, ecological/direct perception,
  embodiment, theory of mind, the extended mind, predictive processing); human-machine, computer-mediated,
  and AI-mediated communication; how people model an opaque, interested third party.

## Cost and cadence

A full refresh is six program deep researches plus sixty topic deep researches. It is heavy by design. To
make the watch lighter — an incremental sweep that only catches papers newer than the last run, without
re-synthesizing every review — change step 2 to search only for work dated after the previous run and append
new hits to the bibliographies, and skip steps 3 and 5's full rewrite. That change lives entirely in this
file.
