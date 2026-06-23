# Daily refresh — the playbook the watch runs

The procedure a run follows, written so a fresh session can execute it without further context. The
autonomous cron fires the daily mode; a person can run either mode by hand the same way.

The watch has two modes. The **daily sweep** is the default the cron fires: it catches papers newer than
each program's last run and appends them to the bibliographies, leaving the reviews untouched. The **deep
refresh** re-researches every program and topic from scratch and rewrites the reviews. The genesis run on
2026-06-23 was a deep refresh; the daily cron runs the sweep.

## Daily sweep — the default mode

A light pass that only catches new work. Six recency-bounded searches, an adversarial check, and an append.
No review is rewritten and no topic is re-researched.

1. **Sync.** From the repo root, fetch and branch off `contrib`:
   `git fetch origin contrib && git checkout -b research/sweep-<date> origin/contrib`.
2. **Read each program's last run.** Every program report opens with `<!-- run: YYYY-MM-DD | sources: N |
   verified: M -->` in `literature/deep_research_report.md`. The `run` date sets the recency window: the
   sweep looks for work dated after it.
3. **Search for new work only.** For each of the six programs below, search its seed question for papers
   dated after that program's last run. Use WebSearch/WebFetch plus the Consensus and Semantic-Scholar /
   Scholar_Gateway MCP tools, with the date filter set to the window. The point is coverage of what is new,
   so the seed question stands; the ten topics are not re-run.
4. **Verify before writing.** Confirm each candidate's DOI / arXiv ID / URL resolves and the claim
   attributed to it holds. Drop anything that fails. Never fabricate a citation to fill a gap.
5. **Dedupe against what is already cited.** Match each survivor against the existing program
   `references.bib` by DOI, arXiv ID, then title. Keep only entries not already present.
6. **Append, do not rewrite.** Add the new entries to the program `references.bib`. Leave `REVIEW.md`, the
   topic reviews, and the report prose as they are. Update the report's metadata line in place: set `run`
   to today and `sources` / `verified` to the new bibliography count. If a new paper plainly belongs to one
   of the ten topics, append it to that topic's `references.bib` too.
7. **Log and index.** Append a dated entry to [`CHANGELOG.md`](CHANGELOG.md): per program, the count added
   and the new total. A program with no new work records `+0`. Regenerate the indexes:
   `python org_frontier/research/build_research_index.py`, then `python tools/build_index.py`.
8. **Land it.** Commit, push, open a PR into `contrib` with the changelog entry as the body, confirm CI is
   green (`directory-current`), admin-merge, then promote `contrib` to `main`. Delete the branch.

A sweep that finds nothing new still lands: it bumps the run dates, records `+0` across the board, and
leaves a dated changelog entry showing the watch ran. The history stays legible either way.

## Deep refresh — the periodic mode

A full re-research of every program and topic. It re-synthesizes the reviews and rebuilds the bibliographies
from scratch, so it catches reframings and displaced topics that an append-only sweep misses. Run it on a
long cadence (monthly is enough) or by hand when a program's framing has moved.

1. **Sync.** Branch off `contrib` as `research/refresh-<date>`.
2. **Research each program.** Run deep research on each seed question: real search across the web and the
   academic databases. Synthesize the program-level review and write its bibliography.
3. **Confirm the ten topics.** Each program holds ten topics (listed in its `README.md`). Re-research each,
   rewrite its `REVIEW.md` and `references.bib`. If the program-level research surfaces a topic that has
   displaced one of the ten, swap it and note the swap in the changelog.
4. **Verify before writing.** Pair every pass with an adversarial check: confirm each DOI / arXiv ID / URL
   resolves and each claim holds. Drop anything that fails.
5. **Write the outputs.** Overwrite each `REVIEW.md`, `literature/deep_research_report.md`, and
   `references.bib`. Open every program report with the metadata line `<!-- run: YYYY-MM-DD | sources: N |
   verified: M -->`. Dedupe each program `references.bib` as the union of its topic bibliographies and its
   program-level finds.
6. **Log and index.** Append a dated entry to [`CHANGELOG.md`](CHANGELOG.md): per program, the papers added
   and removed and the new counts. Regenerate both indexes as in the daily sweep.
7. **Land it.** Same as the daily sweep: PR into `contrib`, CI green, admin-merge, promote to `main`, delete
   the branch.

## The six seed questions

Both modes work from these.

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

The daily sweep is six recency-bounded searches and an append. It is cheap by design and safe to run every
day. The deep refresh is six program deep researches plus sixty topic deep researches: heavy, and meant for
a monthly or on-demand cadence. The daily cron runs the sweep; the deep refresh is triggered when a
program's framing has moved enough that an append no longer captures it.
