# Open questions — the threads waiting for someone

The written agendas (`RESEARCH_AGENDA_50_V2.md`, `RESEARCH_AGENDA_V4.md`, the Q74–Q117 agendas) are
answered. This table is what is still open, in one place, with a status an assistant can read. It is
the registry `tools/build_catalog.py` folds into `catalog.json` and `MAP.md` counts.

To take one: edit its status to `claimed` in the same pull request that adds your scaffold or packet,
so two people do not run the same thread. When it lands, set it to `answered` and name the study.
To add one: a new `O<nn>` row; keep the id stable.

Status is one of `open`, `claimed`, `answered`. Needs is what the thread is waiting on: `compute`
(runs now on the venv), `data` (a real series, cohort, or site), `tooling`, or `review`.

| id | question | status | needs | where | first command |
|---|---|---|---|---|---|
| O01 | Does the extremes-only quorum law survive weighted or noisy quorums? | open | compute | `org_frontier/probes/weighted_quorum/`, study D in `org_frontier/STRUCTURAL_FINDINGS.md` | `python -m org_frontier.protocol.new_question --slug weighted_quorum_law` |
| O02 | Does exact Shapley pivotality sharpen the membership law past the null-player corner at larger forms, with a coalition-formation account? | open | compute | `org_frontier/threads/shapley_membership/THREAD.md` | `python -m org_frontier.threads.shapley_membership.shapley_membership` |
| O03 | Is there a coordination arrangement that is algorithmacy but not directive algorithmic management, or does none exist? | open | compute | `org_frontier/designs/O03_CONSTRUCT_BOUNDARY.md` (source review and proposed test); the committee review, `org_frontier/essays/committed_determination_committee_review.md` | `python tools/build_catalog.py --find "algorithmic management directive"` |
| O04 | Does the two-condition membership account hold when a party has more than two states? | open | compute | `org_frontier/designs/WAVE10_PARKED_DESIGNS.md` #5; the multivalued overlay in `third_party/pyphi_iit4_mv/` now supplies the tooling | `python third_party/pyphi_iit4_mv/smoke_m2.py` |
| O05 | Does the dyadic/triadic verdict depend on the IIT version (3.0 big-Φ vs the 4.0 SIA)? | open | tooling | `org_frontier/designs/WAVE10_PARKED_DESIGNS.md` #8 | read the design; an IIT-3.0 configuration is the missing piece |
| O06 | Can a cheap proxy recover the verdict past the exact-Φ size ceiling (~10–12 nodes)? | open | compute | `foundations/learned_surrogate/`, `org_frontier/proxy_bridge/`, `org_frontier/cascade/` | `python -m org_frontier.cascade.run --panel org_frontier/cascade/residual_panel_n4_unconstrained.csv --smoke` |
| O07 | One real coordination arrangement, modeled from interview and observation evidence to an exact-Φ verdict, with inter-rater reliability on the encoding. | open | data | `org_frontier/field/PROTOCOL.md`; packet `org_frontier/field/packets/gig_dispatch/` | `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/field/packets/gig_dispatch/analysis.py` |
| O08 | One qualitative study run as fieldwork: a real setting read against a named prior, reporting where it departs from the catalog. | open | data | `org_frontier/qualitative/TOPICS.md`; template `org_frontier/qualitative/template/` | `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/qualitative/template/analyze.py` |
| O09 | A recorded coordination series the recurrence instrument has not read, where the determination actor is logged (bot-merged project, dispatch log, physiological series). | open | data | `org_frontier/recurrence/`; verified open datasets in `org_frontier/research/DATA_SOURCES.md` | `PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/recurrence/packets/template/run_study.py` |
| O10 | Field the pre-registered three-wave algorithmacy panel with a real cohort. | open | data | `org_frontier/survey/cohort_algorithmacy/` | `PYTHONPATH=. python org_frontier/survey/cohort_algorithmacy/analysis.py` |
| O11 | Can trained coders look at a real arrangement and agree on dyadic vs triadic reliably enough to use the construct as an instrument? | open | data | `org_frontier/designs/WAVE10_PARKED_DESIGNS.md` #42 | read the design, then the field protocol's step 4 |
| O12 | Do human triads on a joint-commit interface show the difficulty gap the verdict predicts, where selfish bandit agents did not (Probe 98)? | open | data | `org_frontier/designs/WAVE10_PARKED_DESIGNS.md` #41 | read the design sketch and its pre-registration outline |
| O13 | Can the verdict be read from a real interaction log, estimating the TPM over a few discrete units? | open | data | `org_frontier/designs/WAVE10_PARKED_DESIGNS.md` #24; runnable-now datasets in `org_frontier/research/DATA_SOURCES.md` | `python tools/build_catalog.py --find "interaction log TPM estimate"` |
| O14 | Why does the ergodic-components gap stay unexplained by phase, path, observable, or panel mechanisms (`GAP_UNEXPLAINED`)? | open | compute | `org_frontier/ergodicity/AGENDA.md`, `org_frontier/studies/ergodic_gap_decomposition/` | `python tools/build_catalog.py --find "ergodic gap"` |
| O15 | Review a submission: reproduce its numbers, audit its pre-commitment, judge its argument. The board needs reviewers. | open | review | `MAINTAINERS.md`, `PUBLISHING.md` | `python ci/reproduce.py <check-name>` on an open pull request |

Pick a `compute` row to work from the venv today, a `data` row if you can bring a real series, cohort,
or site, and the `review` row if you would rather check work than add it. `START_HERE.md` Phase 3.5
is how an assistant routes a newcomer's own question to one of these or to a fresh scaffold.
