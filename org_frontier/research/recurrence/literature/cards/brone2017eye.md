---
citekey: brone2017eye
title: Eye gaze and viewpoint in multimodal interaction management
authors: Br{\^o}ne, Geert and Oben, Bert and Jehoul, Annelies and Vranjes, Jelena and Feyaerts, Kurt
year: 2017
doi: 10.1515/cog-2016-0119
arxiv: null
journal: Cognitive Linguistics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://lirias.kuleuven.be/retrieve/8a922e20-a727-464e-a051-8678774eedc2
sha256: 1e3b0429b86614ee740c7225ef4d58e5b90c406c4b9f79410a2cdbe8e66661c6
pdf_path: literature/pdfs/brone2017eye.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper presents an embodied, multimodal account of viewpoint in face-to-face conversation, asking how measurable eye-gaze events by speakers and hearers relate to verbal turn-management strategies. Using the InSight Interaction Corpus — Dutch face-to-face dyads and triads recorded with head-mounted scene cameras and mobile eye-trackers giving a "speaker-internal" perspective — the authors run two analyses on a subset (5 dyads in the brainstorming task, 4 triads). A distributional analysis links intonation-unit-level turn-management codes (turn-hold, -conclude, -yield, -take, -elicit) to gaze patterns (face / not-face / face-shift), finding that turn-holding units are more strongly associated with gaze aversion than other dialogue acts. A time-sensitive analysis uses cross-recurrence quantification to show that brief gaze aversions and verbal fillers (e.g. "uhm") are tightly synchronized, with near-perfect simultaneity in dyads and a ~200 ms lead of gaze aversion in triads, both significantly above a random baseline. The authors interpret these recurrent gaze–speech couplings as evidence for Clark's composite signals / McNeill's multimodal packages, and as candidate multimodal constructions in Construction Grammar.

## Key facts it relies on
- Data source is the InSight Interaction Corpus: Dutch face-to-face interactions, 15 dyads (~30 min each) and 10 three-party interactions (~15 min each); participants were well-acquainted students aged 18–23, all native Dutch speakers; dyadic sessions had storytelling, brainstorming, and collaborative spatial tasks, triads were free-range.
- The analyzed subset was 5 randomly selected dyads (brainstorming task) and 4 triads; recordings used Arrington Gig-E60 eye-tracking glasses (dyads) and Pupil Pro glasses (triads), annotated in ELAN with speech segmented into intonation units (Chafe 1994) and GAT transcription (Selting et al. 1998).
- Minimum gaze-fixation duration for a reliable gaze event was set at 120 ms; turn-management coding used the MUMIN scheme (Allwood et al. 2007: turn take, accept, hold, yield, elicit, complete), coded by three independent annotators reconciled to consensus.
- Dyadic distribution (Table 1a, face vs not-face, ratio = face/total): Turn-H 130/181 ratio 0.418; Turn-C 64/47 ratio 0.576; Turn-Y 38/20 ratio 0.655; Turn-T 59/38 ratio 0.608; Turn-E 20/8 ratio 0.714 — turn-holding has the lowest face ratio.
- Triadic distribution (Table 1b, face / face-shift / not-face, ratio): Turn-H 29/53/83 ratio 0.176; Turn-C 98/75/45 ratio 0.449; Turn-Y 18/21/8 ratio 0.383; Turn-T 39/29/12 ratio 0.487; Turn-E 89/13/2 ratio 0.856 — turn-holding again lowest.
- For Turn-conclusion "not face" dyadic units, 42 of 47 TCUs had speaker gaze toward the addressee at the end of the turn; the 5 exceptions all involved the speaker laughing, illustrating end-of-turn visual grounding.
- For turn-taking, only 2 of 38 "non-face" dyadic cases had gaze aversion at unit onset; in triads the new speaker gazed at the previous speaker at onset in 68 of 80 cases (6 gazed at the third participant) — supporting a rule that turn-takers obtain recipient gaze at onset.
- Hearers looked at their speaking partner slightly over 92% of the time (red baseline); at turn-taking onset (T=0) intervening speakers looked at the partner over 96% of the time, with a drop in eye contact ~0.5 s before onset (T=-0.5).
- Of micro gaze aversions ≤500 ms (n=69), 45 co-occurred with a verbal filler; of 74 hesitation markers in the corpus, 56 (76%) occurred with a brief gaze aversion; gaze aversion at turn-taking beginnings occurred in only 8 of 118 cases.
- Cross-recurrence analysis (R package of Coco & Dale 2014) of gaze aversion and fillers showed a bell curve peaking near T0: near-perfect synchronization in dyads, ~200 ms lead of gaze aversion before fillers in triads; a 200-random-pair baseline plus a mixed-effects model (dyad/triad as random factor) confirmed synchronization above chance for dyads (t=5.37, p<0.001) and triads (t=16.64, p<0.001).

## Critical notes from the literature
- The authors explicitly call their MUMIN-based, intonation-unit-level annotation scheme "relatively coarse-grained," especially relative to fine-grained conversation-analytic descriptions, and frame it only as a starting point for quantitative multimodal corpus work.
- Scope is deliberately limited: the study analyzes "a small set of micro-phenomena" on a small subset (5 dyads, 4 triads) of the corpus; the authors present it as exploratory and as a "general plea" rather than a definitive account.
- Each intonation unit could carry only one value per turn-management category (to avoid data conflation), so repeated cues within a unit (e.g. two filled pauses) were annotated once, potentially undercounting.
- The authors note that video-based gaze estimation (the standard conversation-analytic method) is "notoriously coarse-grained and unreliable" for short fixations (≤200 ms), saccades, and scan paths, motivating eye-tracking; they cite Jokinen et al. that gaze's turn-taking role is less outspoken in triads than dyads, consistent with their weaker/lagged triadic effects.
- The proposed extension to a "multimodal constructicon" / multimodal Construction Grammar is flagged as theoretical; the paper states it "cannot discuss the scope and limitations" of multimodal CxG here.

## Key topics covered
Eye gaze in face-to-face interaction; mobile/wearable eye-tracking; viewpoint and intersubjectivity; turn management and turn-taking (CA); multimodal interaction; gaze aversion and turn-holding; verbal fillers / hesitation markers; mutual gaze and grounding; cross-recurrence quantification analysis (CRQA); InSight Interaction Corpus; ELAN annotation; MUMIN coding scheme; intonation units / TCUs; composite signals (Clark); multimodal packages (McNeill); multimodal Construction Grammar; dyads vs triads; random baseline / mixed-effects modeling.
