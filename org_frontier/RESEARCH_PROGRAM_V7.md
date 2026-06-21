# Research program v7 — the qualitative and recurrence wave

v6 closed the computational probe line at 134. Connectivity decides the verdict, the holistic residual is
settled as a near-boundary tail, the commit topologies form a scaling zoo, and the cheap surrogate is
family-bound in principle. The single computational line had answered its standing questions. This wave
broadens the lab from that one line into three programs, each a different lens on the same arrangement.
It adds a **qualitative** program that reads real coordination settings against the prior catalog, and a
**recurrence** program that pairs exact Φ with a behavioral measure of coordination. The probe counter
stays at 134; this wave is numbered in its own arms — studies under `qualitative/`, and the E and C
experiment series under `recurrence/`. Φ stays the instrument the other two are built around.

## S. The qualitative program

- **S1 — qualitative-arm** `[qual]` — built [`qualitative/`](qualitative/): a charter, a methods guide of
  eight qualitative methods tied to the field protocol, a topic agenda of twelve coordination settings each
  paired with a catalog prior, and a publishing guide grounded in Bansal and Corley (2012). A study reads a
  real setting against the nearest prior and holds the prior open; the departure is where the contribution
  is built. Out: `qualitative/{README,METHODS,TOPICS,PUBLISHING}.md`, `qualitative/template/`.
- **S2 — neonatal-third** `[qual]` — the first worked study: how neonatal nurses coordinate between parents
  and an infant who cannot take up a message. Its prior analysis runs the structure through exact Φ — the
  apparatus is a veto player in every integrating coalition, a pure observer is excluded from the core, and
  the infant, read by the apparatus, sits in the core a third of the time. The finding is the
  causal-versus-communicative boundary: Φ measures causal irreducibility, the construct's claim is
  communicative, and the infant pries the two apart. Out: `qualitative/neonatal_third/`.
- **S3 — five-proposals** `[qual]` — five Bansal-and-Corley-grade proposals, each reading a setting against
  a named prior: content moderation (memory and oversight), clinical handoff (interdependence), peer review
  (veto player), customer-service triage (observer), agents and brokers (delegation). Out:
  `qualitative/{moderation_memory,clinical_handoff,peer_review_gate,triage_spectator,broker_delegation}/`.

## T. The recurrence program

- **T1 — the-bridge** `[recur]` — built [`recurrence/`](recurrence/): categorical cross-recurrence (RR,
  DET, line length, the diagonal profile and its peak lag) and a trajectory generator that runs a Boolean
  form as a stochastic dynamical system. One model yields a Φ verdict from its transition matrix and a CRQA
  reading from a run of it. The two instruments partition the coupling regimes between them: Φ marks a
  mutual wiring irreducible and reads a relay as no different from independence, while the profile lag reads
  the relay's direction and the independent pair as flat. Out: `recurrence/crqa.py`, `bridge_demo.py`,
  `CONCEPTS.md`, `FINDINGS.md`. The pairing is unclaimed in the literature.
- **T2 — corpus-sweep** `[recur]` — every named form read by both instruments, plus a random ensemble.
  Structure and behavior agree on most forms and part on three: the false dyad hides its tight coupling
  (the hidden S-C tie dominates the presented W-S pair), the relay couples strongly with Φ of zero, the
  back-channel agrees. Ensemble: the profile lag recovers 40% of directed edges at a 6% false-positive
  rate; 80% of irreducible forms couple synchronously. Out: `recurrence/sweep.py`, `SWEEP.md`.
- **T3 — twenty-experiments** `[recur]` — ten Φ experiments and ten CRQA experiments seeded by the sweep.
  Whole-system Φ detects the false dyad; reciprocity drives irreducibility (95% with a two-cycle, 60%
  without); the cooperative-game veto player sits in the IIT core only 38% of the time; Φ and determinism
  dissociate. The profile lag tracks path length, prominence separates coupling from chance, and a
  continuous variant recovers a graded delay. Out: `recurrence/{iit,crqa}_experiments.py`,
  `{IIT,CRQA}_EXPERIMENTS.md`.
- **T4 — four-party-bridge** `[recur]` — the pairing at four and five parties. The lead-lag matrix reads
  several lags at once, recovering a chain's hop distance (neighbors at one, ends at three) and locating a
  star's hub. Φ resolves the major complex at n=4 and n=5, including a chain whose core is its tail pair.
  Structure and behavior agree less as parties multiply (33% edge recovery, 36% core separation), which
  keeps the two instruments complementary. Out: `recurrence/bridge_four.py`, `BRIDGE_FOUR.md`.

## U. The three-program framing

- **U1 — entry-points** `[docs]` — aligned the entry points and the agent-discoverability files to name the
  three programs: the README and OVERVIEW, `llms.txt` (canonical memory block, framing rules, key
  documents), the lab front door (`org_frontier/README.md`), CONTRIBUTING, and GETTING_STARTED. Out: the
  six entry-point documents.

## Waves and status

| Wave | Projects | Lane | Status |
|------|----------|------|--------|
| W1 | S1 S2 S3 | qual | **done** (the qualitative arm, the neonatal study and its prior analysis, five proposals) |
| W2 | T1 T2 T3 T4 | recur | **done** (the bridge, the corpus sweep, twenty experiments, the four-party bridge) |
| W3 | U1 | docs | **done** (six entry points name the three programs) |

**Program v7 complete.** The lab is three programs: computational, qualitative, recurrence — structure,
fieldwork, behavior, on one arrangement. The qualitative arm carries a methods guide, a worked study with
an exact-Φ prior analysis, and five proposals. The recurrence arm pairs Φ with cross-recurrence across a
corpus sweep, twenty experiments, and the bridge at four and five parties, with the structure-behavior
dissociation as its recurring finding. The probe logbook stands at 134.

Stop rule: both new programs are in-silico or pre-fieldwork. The open edge for each is the same one — a
first real recorded series, read through the field protocol, the first time either instrument runs on data
the lab did not generate. That is the v8 question.
