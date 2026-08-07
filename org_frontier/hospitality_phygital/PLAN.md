# Project plan — hospitality phygital baseline and manuscript

Complete plan for the *Hospitality & Society* conceptual paper. This file is the authority for
sequencing work in this arm. Update status lines as milestones close; do not fork a second plan.

## 1. Goal

Deliver a conceptual article that:

1. Theorizes phygital hospitality as **triadic coordination** among guest, algorithmic intermediary,
   and human/organizational host.
2. Distinguishes **augmentative** from **substitutive** hospitality.
3. Introduces **hospitality algorithmacy** and links it to **coordinative sovereignty**.
4. Specifies five design affordances that tilt mediation toward augmentation.
5. Challenges the assumption that seamlessness is inherently hospitable.
6. Speaks to *Hospitality & Society*'s social-science mission and the special issue's guest-centric
   phygital brief ([`cfp/`](cfp/)).

Primary audience: hospitality scholars, critical service researchers, and designers of phygital
guest experience. Secondary audience: the algorithmacy lab (construct reuse without Φ overclaim).

## 2. Deliverables

| deliverable | location | status |
|---|---|---|
| Baseline library (this arm) | `org_frontier/hospitality_phygital/` | scaffolded |
| Locked abstract | [`ABSTRACT.md`](ABSTRACT.md) | done |
| Construct glossary | [`CONSTRUCTS.md`](CONSTRUCTS.md) | draft |
| Lab ↔ hospitality bridge | [`BRIDGE.md`](BRIDGE.md) | draft |
| Design affordances | [`design_principles.md`](design_principles.md) | draft |
| CFP alignment | [`cfp/`](cfp/) | draft |
| Literature seed | [`literature/`](literature/) | seed |
| Manuscript outline + stubs | [`manuscript/`](manuscript/) | outline |
| Local dissertation review log | [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md) | **open — required** |
| Full manuscript draft | `manuscript/manuscript.md` | not started |
| Submission package | journal system + cover note | not started |

## 3. Source corpus (two trees)

This arm draws on **two separate repositories**. Git directory decides the remote
([`../../REPO_LAYOUT.md`](../../REPO_LAYOUT.md)).

| corpus | where | remote | use in this paper |
|---|---|---|---|
| Public lab | everything except `dissertation/` | `algorithmacy-lab` | triad, algorithmacy, coordinative sovereignty, essays, probes as conceptual priors |
| Private dissertation | `dissertation/` (nested `.git`) | `algorithmacy-dissertation` | Paper 1 construct gap; Paper 2 affirmative case for principled mediation analysis; Paper 3 experimental motifs only if they illustrate without claiming hospitality empirics |

**The dissertation tree is often absent from a public clone.** Agents and collaborators working only
against `algorithmacy-lab` must still follow [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md): clone
or mount the private repo locally, run the review checklist, and record findings in that file before
treating the construct bridge as complete.

## 4. Workstreams

### A. Local dissertation review (blocking for bridge completeness)

1. Confirm `dissertation/` is present and which paper files are current.
2. Run the checklist in [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md).
3. Extract load-bearing claims for: mediated triad; algorithmacy vs neighbor constructs;
   irreducibility as a lens (not a consciousness claim); design/operations language that maps to
   augmentative vs substitutive hospitality.
4. Log what transfers, what must be paraphrased for a hospitality audience, and what stays private.

### B. Literature deepening

1. Expand [`literature/references.bib`](literature/references.bib) from the CFP core (Batat PH-CX /
   PSR; Lynch et al. / Lugosi hospitality theorizing; Wirtz digital service / AI; Tlili metaverse).
2. Add hospitality-critical lines on welcome, recognition, care, presence, negotiated access.
3. Add algorithmic mediation / literacy / contestability neighbors already used in the sovereignty
   chapter — re-read for guest and frontline-employee positions, not only platform workers.
4. Keep [`literature/field_map.md`](literature/field_map.md) current; mark every citation verified.

### C. Construct lock

1. Freeze definitions in [`CONSTRUCTS.md`](CONSTRUCTS.md) after the dissertation pass.
2. Keep augmentative / substitutive as the paper's outcome distinction.
3. Keep hospitality algorithmacy as competence; coordinative sovereignty as standing.
4. Refuse consciousness or "the hotel is Φ-conscious" framings.

### D. Manuscript production

Follow [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md):

1. Introduction and research question.
2. Hospitality beyond seamless service.
3. Phygital hospitality as triadic mediation.
4. Augmentative vs substitutive hospitality.
5. Hospitality algorithmacy and coordinative sovereignty.
6. Five affordances and design implications.
7. Against frictionless hospitality.
8. Contributions, limits, conclusion.

House style: [`../../CLAUDE.md`](../../CLAUDE.md). No first person. Cut antithesis-machine and
self-narrating rigor tics before any external share.

### E. Journal path

1. Align claims to the four special-issue aims in [`cfp/ALIGNMENT.md`](cfp/ALIGNMENT.md).
2. Read Intellect *Hospitality & Society* Notes for Contributors before formatting.
3. Prepare abstract + keywords + manuscript for the March–September 2026 submission window.
4. APA Summit attendance is separate; this arm's critical path is the journal full paper.

## 5. Sequencing (recommended)

```
1. Dissertation local review  →  fill DISSERTATION_REVIEW.md log
2. Freeze CONSTRUCTS.md + BRIDGE.md from that log
3. Literature pass (hospitality + phygital + mediation)
4. Expand manuscript stubs section by section
5. Internal lab read (style + overclaim audit)
6. External hospitality read (domain fit)
7. Revise → submission package by 4 September 2026
```

Parallelizable after step 1: literature deepening and outline expansion can run together once
constructs are frozen.

## 6. Risks and mitigations

| risk | mitigation |
|---|---|
| Dissertation absent; bridge incomplete | Block construct freeze on [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md); lab-only sources are interim |
| Φ / IIT overclaim for a hospitality journal | Conceptual paper; cite lab results only as model priors; state validation gap |
| Seamlessness critique read as anti-tech | Hold augmentative hospitality as the positive design path |
| Construct pile-up (too many new names) | Lead with triad + augmentative/substitutive; algorithmacy and sovereignty earn their keep once |
| Deadline slip | Outline-first drafting; no new computational experiments on the critical path |
| Private dissertation prose leaked into public tree | Paraphrase and cite; never `git add -f dissertation/` |

## 7. Definition of Done (baseline library)

The baseline library is done when:

- [x] Arm exists under `org_frontier/hospitality_phygital/` with README and plan.
- [x] Abstract, constructs, bridge, design principles, CFP notes, literature seed, and outline exist.
- [x] Arm registered in `tools/build_map.py` / `MAP.md`.
- [ ] [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md) checklist completed on a machine that has
      `dissertation/` checked out.
- [ ] Construct definitions frozen after that review.
- [ ] Every bibliographic entry used in the manuscript verified (DOI / stable URL).

The **manuscript** is done when the outline sections are continuous prose, house-style clean,
CFP-aligned, limits stated, and ready for journal upload — tracked separately in
[`manuscript/README.md`](manuscript/README.md).

## 8. Non-goals (this arm)

- New PyPhi probes or Φ numbers as hospitality evidence.
- Outreach emails or unsolicited contact with special-issue editors (maintainers only).
- Merging dissertation files into the public repo.
- Claiming empirical findings about real guests or hotels from in-silico priors alone.
