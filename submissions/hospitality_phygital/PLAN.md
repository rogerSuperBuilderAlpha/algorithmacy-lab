# Project plan — hospitality phygital baseline and manuscript

Complete plan for the *Hospitality & Society* conceptual paper. This file is the authority for
sequencing work in this arm. Update status lines as milestones close; do not fork a second plan.

> **Calendar reality (2026-08-07).** The submission window closes **4 September 2026** — 28 days
> out — and `manuscript/DRAFT.md` is the paper. Section 5 below is a day-level schedule,
> not a recommendation. Anything that does not fit inside it is a post-submission item.

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

## 2. Journal constraints (binding on the draft)

**The Notes for Contributors were read on 2026-08-07. The web page's "5-8000 words" is wrong.**
Full extraction: [`manuscript/JOURNAL_SPEC.md`](manuscript/JOURNAL_SPEC.md), which is the authority
for format.

| constraint | value |
|---|---|
| Article length | **6,000–9,000 words including notes, references, contributor biography, keywords and abstract** |
| Ruled body budget | **6,800 words**, leaving ~1,620 for references and ~490 for the other required components |
| Abstract | 100–200 words |
| Keywords | exactly six, one or two words each |
| Referencing | **Intellect Harvard** — `(Bordwell 1989: 9)`; volume:number with a colon, `pp.` before extents, commas not full stops |
| Language | British English, **'ize'** endings |
| File | Word, Times New Roman 12 pt |
| Anonymity | strict, both directions; two referees |
| Also mandatory | Statement of Contribution (100–150 words, anonymised); **Highlights** (3–5 bullets, ≤85 characters, separate file); contributor biographies; **AI acknowledgment section** before the References |
| Submission system | Callisto (link in [`cfp/`](cfp/)) |

Three consequences. References sit **inside** the count, so every source added costs about 27 words
of body — the bibliography is now a budget line, not a free annex. The locked ~700-word abstract in
[`ABSTRACT.md`](ABSTRACT.md) is a pitch, and a 100–200-word journal abstract is a separate
deliverable. And the `.bib` file, stored in an APA-ish shape, must be rendered into Intellect Harvard
by hand.

## 3. Deliverables

| deliverable | location | status |
|---|---|---|
| Baseline library (this arm) | `org_frontier/hospitality_phygital/` | done |
| Locked abstract (pitch) | [`ABSTRACT.md`](ABSTRACT.md) | done |
| Construct glossary | [`CONSTRUCTS.md`](CONSTRUCTS.md) | frozen on the abstract; see §5.A |
| Lab ↔ hospitality bridge | [`BRIDGE.md`](BRIDGE.md) | draft |
| Design affordances | [`design_principles.md`](design_principles.md) | draft |
| CFP alignment | [`cfp/`](cfp/) | draft |
| Literature seed | [`literature/`](literature/) | 56 entries; CFP core and guest-side Crossref-verified |
| Manuscript outline + stubs | [`manuscript/`](manuscript/) | outline with word budget |
| Dissertation genealogy log | [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md) | **complete** — library and chapter passes both logged |
| Literature research passes | [`literature/FOUNDATION.md`](literature/FOUNDATION.md) | rounds 1a–1c done; round 2 specified |
| Round-2 research prompts | [`literature/RESEARCH_PROMPTS.md`](literature/RESEARCH_PROMPTS.md) | eight prompts, ready to run |
| Full manuscript draft | `manuscript/DRAFT.md` | **done; over length, see NOTES.md** |
| Compressed abstract + keywords | `manuscript/` | not started |
| Submission package | Callisto + cover note | not started |

## 4. Source corpus (two trees)

This arm draws on **two separate repositories**. Git directory decides the remote
([`../../REPO_LAYOUT.md`](../../REPO_LAYOUT.md)).

| corpus | where | remote | use in this paper |
|---|---|---|---|
| Public lab | everything except `dissertation/` | `algorithmacy-lab` | triad, algorithmacy, coordinative sovereignty, essays, probes as conceptual priors |
| Private dissertation | `dissertation/` (nested `.git`) | `algorithmacy-dissertation` | Paper 1 the standing series and the construct gap; Paper 2 the competency derivation and the individual/institutional division; Paper 3 designed and **unfielded** — future-research mention only. See [`BRIDGE.md`](BRIDGE.md) |

**The dissertation tree is often absent from a public clone.** Agents and collaborators working only
against `algorithmacy-lab` cannot run the genealogy pass in
[`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md); they draft from public lab sources and leave the
log open.

## 5. Workstreams

### A. Dissertation genealogy pass (timeboxed — one day, runs in parallel)

Earlier revisions of this plan made the construct freeze wait on this review. That gate cannot hold
against a 28-day window, and it is not load-bearing: [`CONSTRUCTS.md`](CONSTRUCTS.md) is already
fully specified from the locked abstract and the public lab. **Freeze the constructs on the
abstract; treat the dissertation pass as citation genealogy and Paper 1 gap-argument sharpening,
scheduled in parallel and finished in a day.**

1. Confirm `dissertation/` is present and which paper files are current.
2. Run the checklist in [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md).
3. Extract load-bearing claims for: mediated triad; algorithmacy vs neighbor constructs;
   irreducibility as a lens (not a consciousness claim); design/operations language that maps to
   augmentative vs substitutive hospitality.
4. Log what transfers, what must be paraphrased for a hospitality audience, and what stays private.
5. If the pass surfaces something that contradicts a frozen definition, amend
   [`CONSTRUCTS.md`](CONSTRUCTS.md) then — an amendment is cheap; a stalled draft is not.

### B. Literature deepening

The CFP core is verified with DOIs ([`literature/references.bib`](literature/references.bib), all
entries checked 2026-08-07). Remaining work is domain density, and it is where a desk rejection is
most likely to originate.

1. **Hospitality's own theorizing line.** Lashley's three domains and Derrida's conditional /
   unconditional distinction are seeded; add host–guest power and cultural scripts of welcome.
2. **Platform hospitality.** The literature that already asks *who hosts* — Airbnb and
   platform-mediated stays, ratings as access control, "host" as a platform-assigned role. A paper
   titled "Who Hosts the Guest?" cannot omit it.
3. **Algorithmic management of frontline hospitality work.** The evidence base for the
   employee-discretion half of the framework.
4. **Algorithmic exclusion at the threshold.** Facial recognition and identity matching at check-in;
   categorical exclusion as a hospitality failure.
5. Keep [`literature/field_map.md`](literature/field_map.md) current; every entry verified before it
   enters the manuscript.
6. Round 2 is specified as eight runnable prompts in
   [`literature/RESEARCH_PROMPTS.md`](literature/RESEARCH_PROMPTS.md), with venue discipline,
   verification rules, and a sequencing note. P1 and P2 are on the critical path; P3, P5, and P8 are
   the drop candidates if time runs short.

### C. Construct lock

1. Freeze definitions in [`CONSTRUCTS.md`](CONSTRUCTS.md) at the start of drafting (§5.A).
2. Keep augmentative / substitutive as the paper's outcome distinction.
3. Keep hospitality algorithmacy as competence; coordinative sovereignty as standing.
4. Refuse consciousness or "the hotel is Φ-conscious" framings.
5. **Enforce the pile-up mitigation in the draft, not only in this table.** Triad and
   augmentative/substitutive lead. Algorithmacy and coordinative sovereignty earn their keep once
   each and are not re-explained. See the word budget in
   [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md).

### D. Manuscript production

Follow [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md) and its per-section word budget:

1. Introduction and research question.
2. Hospitality beyond seamless service.
3. Phygital hospitality as triadic mediation.
4. Augmentative vs substitutive hospitality.
5. Hospitality algorithmacy and coordinative sovereignty.
6. Five affordances and design implications.
7. Against frictionless hospitality.
8. Contributions, limits, conclusion.

House style: [`../../CLAUDE.md`](../../CLAUDE.md). No first person. Cut antithesis-machine and
self-narrating rigor tics before any external share. Complying with "no first person" does not
license agentless passive — name the agent.

### E. Journal path

1. Align claims to the four special-issue aims in [`cfp/ALIGNMENT.md`](cfp/ALIGNMENT.md).
2. **CFP confirmed 2026-08-07** against the source PDF: editors, the 5 March – 4 September window,
   Callisto, and the four mission criteria all match. Summit attendance — the CFP's condition on the
   full-article route — is confirmed by the author. The schedule below rests on a real deadline.
3. Format to the Notes for Contributors (`HOSP_NFC_May_26.pdf`): length, reference style, anonymity.
4. Compress [`ABSTRACT.md`](ABSTRACT.md) to a ~150-word journal abstract and choose keywords.
5. APA Summit attendance is separate; this arm's critical path is the journal full paper.

## 6. Schedule (28 days)

Dates are 2026. Drafting runs against frozen constructs from day one; the literature pass feeds
sections as they are written rather than gating them.

| window | work | gate at the end |
|---|---|---|
| **Aug 7–8** | Re-confirm CFP from the PDF (§5.E.2). Freeze `CONSTRUCTS.md`. Dissertation pass in its one-day box. | Constructs frozen; deadline confirmed or plan re-cut |
| **Aug 9–14** | Run prompts P1 and P2 ([`literature/RESEARCH_PROMPTS.md`](literature/RESEARCH_PROMPTS.md)) — they gate §2 and §3. Draft both sections behind them. | ~1,800 words of continuous prose; gap citations verified |
| **Aug 15–22** | Run P4, P6, P7 alongside drafting. Draft §4 (augmentative/substitutive, with the diagnostic table), §5 (algorithmacy and sovereignty, one pass only), §6 (five affordances). | ~4,500 words total; send §2–§6 to the external hospitality reader |
| **Aug 23–29** | Draft §1, §7 (against frictionless hospitality), §8–§9. Internal lab read: style plus overclaim audit. | Full draft at or under 8,000 words |
| **Aug 30–Sep 2** | Absorb both reads. Compress the abstract, choose keywords, format to Notes for Contributors, final citation check. | Submission package complete |
| **Sep 3–4** | Buffer. Submit. | Submitted |

The external hospitality read starts on **22 August**, not after the full draft — a domain reader
who sees §2–§6 in time can still change the paper. A reader who sees it on 30 August can only
approve it.

If the CFP re-check on 7 August moves the deadline, re-cut this table before drafting rather than
carrying a schedule everyone privately knows is fiction.

## 7. Risks and mitigations

| risk | mitigation |
|---|---|
| **28 days, no draft** | Day-level schedule in §6; constructs frozen up front; dissertation pass timeboxed and parallel; external read starts mid-draft |
| ~~CFP unverifiable~~ — **closed 2026-08-07** | Confirmed against the source PDF; summit eligibility confirmed by the author |
| Domain grounding thin in §2 and §3 | Prompts P1 and P2 in [`literature/RESEARCH_PROMPTS.md`](literature/RESEARCH_PROMPTS.md) run before those sections are drafted |
| **8,000-word ceiling vs six named constructs** | Word budget per section in the outline; algorithmacy and sovereignty explained once; affordances carry the design load |
| **Desk rejection: outsider, conceptual, no hospitality empirics** | Domain-native citation density (§5.B); a reviewer-legible diagnostic that classifies a real touchpoint; the journal's own theorizing line cited as the frame |
| Φ / IIT overclaim for a hospitality journal | Conceptual paper; cite lab results only as model priors; state validation gap |
| Seamlessness critique read as anti-tech | Hold augmentative hospitality as the positive design path; ground the argument in seamful design, which is a design-theory position rather than a complaint |
| Construct pile-up (too many new names) | Lead with triad + augmentative/substitutive; algorithmacy and sovereignty earn their keep once — enforced by the outline's word budget, not by good intentions |
| Locked abstract mistaken for the journal abstract | Compression to ~150 words is its own deliverable (§3, §5.E.4) |
| Private dissertation prose leaked into public tree | Paraphrase and cite; never `git add -f dissertation/` |

## 8. Definition of Done (baseline library)

The baseline library is done when:

- [x] Arm exists under `org_frontier/hospitality_phygital/` with README and plan.
- [x] Abstract, constructs, bridge, design principles, CFP notes, literature seed, and outline exist.
- [x] Arm registered in `tools/build_map.py` / `MAP.md`.
- [x] Every bibliographic entry carries a verified DOI or publisher record.
- [x] Journal length constraint recorded and reflected in the outline.
- [ ] Construct definitions frozen (§5.A) — one line in [`CONSTRUCTS.md`](CONSTRUCTS.md) stating the
      freeze date.
- [ ] [`DISSERTATION_REVIEW.md`](DISSERTATION_REVIEW.md) genealogy pass logged on a machine that has
      `dissertation/` checked out. Post-freeze; amendments welcome.

The **manuscript** is done when the outline sections are continuous prose inside the word budget,
house-style clean, CFP-aligned, limits stated, and ready for journal upload — tracked separately in
[`manuscript/README.md`](manuscript/README.md).

## 9. Non-goals (this arm)

- New PyPhi probes or Φ numbers as hospitality evidence.
- Outreach emails or unsolicited contact with special-issue editors (maintainers only).
- Merging dissertation files into the public repo.
- Claiming empirical findings about real guests or hotels from in-silico priors alone.
