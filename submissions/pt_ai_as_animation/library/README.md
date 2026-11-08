# pt_ai_as_animation library (run `pta-lib-2026-11`)

> **[Built by Claude, 2026-11-08.]** Every card here is drafted by Claude or a Claude subagent, not by
> the author. A card is a research note: it records what a source says, which version was read, and
> what the paper uses it for. It is not manuscript prose.

One card per work the paper (`../SKETCH.md`) may cite that no existing lab library already holds.
Works other libraries hold are not re-carded; `POINTERS.md` lists them by facet. The thesis is the
author's text in `../SOURCE.md`. The convention, card schema and tools are the dxd_animation library's
(`L/submissions/dxd_animation/library/`, run `dxda-lib-2026-11`, branch `research/dxd-animation-library`),
itself copied from the Peircean-triad library. The run plan was drafted by Fable on 2026-11-08.

Path prefixes: `L/` = `~/iit-playground/pyphi-experiments/` (public); `D/` = `L/dissertation/`
(**private** nested repo).

## Layout

| Path | What | Stage |
|---|---|---|
| `CITED_WORKS.md` | every work `../SKETCH.md` names: registry hit, verdict new / pointer / upgrade | S0 |
| `FACETS.md` | facets: claims served, queries, anchors (each confirmed by a record), targets | S1 |
| `SEARCH_LOG.md`, `search/F*.jsonl` | every query: date, facet, source, n, top ids | S2 |
| `triage/*.md`, `triage/DECISIONS.md` | shortlists and the approved list | S3 |
| `FETCH_LOG.tsv`, `HELD_COPIES.tsv`, `BROWSER_LIST.md` | fetch outcomes; works only the author can open | S4 |
| `cards/<key>.md` | one card per work, written by hand (Claude or a subagent), never by script | S5–S6 |
| `HAND_CHECK.md`, `hand_check/` | Fable's read of every card against its source, before indexing | S7 |
| `POINTERS.md`, `INDEX.md`, `TRACKER.tsv`, `references.bib`, `REFERENCES_APA.md`, `DOI_CHECK.md`, `QUOTE_CHECK.md` | index and checks | S8 |
| `CRITIC.md`, `GAP_CHECK.md` | coverage against the sketch; prior work that already makes the argument | S9 |
| `RUN_REPORT.md` | what ran, counts, what needs the author's decision | S10 |
| `tools/` | copied 2026-11-08 from the dxd_animation library; local paths point to `pt_ai_animation_local`; registry adds library `pta` | S0 |

Outside the repo, in `~/iit-playground/pt_ai_animation_local/`: `registry.tsv` (every key in the lab
libraries, for de-duplication; it names private paths, so it is never committed), `pdfs/<key>/`,
`inbox/` (the author's browser downloads), `consensus/`.

## Guards (author's ruling, 27 Oct 2026)

No card from model memory. Every quotation carries a locator. An independent verifier (writer ≠
verifier) re-checks every card. Fable reads every card against its source before it is indexed.
Paywalls are never bypassed; those works go to `BROWSER_LIST.md`.

## Claims

| tag | claim | § |
|---|---|---|
| c1 | a working AI is the LLM plus harnesses, VMs, efficiencies | §1, §4.1 |
| c2 | model-centrism misplaces where the intelligence sits | §1, §4.1 |
| c3 | neither life nor intelligence has a consensus definition; defend a theory | §2 |
| c4 | an organizational account of life fits the system around the LLM | §2 |
| c5 | intelligence frame versus life frame is a stance choice | §2, §6 |
| c6 | animation is the craft of composing a living character from inert parts | §3 |
| c7 | necessary opacity: no frame holds the motion, no component the intelligence | §4.2 |
| c8 | co-optation: dependency grows with use; the viewer is co-opted | §4.3 |
| c9 | triadicity: the studio determines what the viewer gets | §4.4 |
| c10 | the analogy breaks at liveness; puppetry; the LLM makes its own in-betweens | §5 |
| c11 | implementation and evaluation under the life frame | §6 |
| c12 | gap: no prior work frames AI development as animation craft or AI as life in the making | §1, §7 |

## Facets

F1 philosophy of life · F2 organizational/autopoietic accounts · F3 intelligence and the intentional
stance · F4 animation production pipeline · F5 puppetry, performance capture, liveness · F6 animacy
and apparent motion · F7 epistemic opacity · F8 compound AI vs model-centrism · F9 co-optation,
lock-in, suspension of disbelief · F10 triadicity · F11 LLMs as characters · F12 venue (*P&T*
2019–2026) · G gap check. Details in `FACETS.md`.
