# Chapter manuscript — "Algorithmacy and Sovereignty"

Full draft of the invited book chapter for the IGI Global Scientific Publishing edited volume *Organizational
Implications of Digital Sovereignty in the Age of AI* (ed. Samuel Fosso Wamba, TBS Education).

- **Authors:** Roger Hunt (Bentley University), Pierre Berthon (Bentley University), Sara Whitmer (University of
  Iowa).
- **Status:** abstract accepted; full chapter due 2026-08-30 (min. 10,000 words incl. references);
  double-anonymized review; academic APA.
- **The draft question is settled: `chapter.md` ships.** The 2026-08-15 persona panel measured
  [`chapter_v2.md`](chapter_v2.md) against its own objective and it failed — the coefficient of variation
  fell rather than rose, and the pass made roughly seventy merges and zero splits. v2 is also **not
  prose-only**, correcting `HANDOFF.md` §0e: it swaps the defined term *mediator* for undefined *third
  party* in two of §5.3's definitional sentences. v2 is kept for the record and is not the manuscript.
- **Current draft:** `chapter.md`. This is the canonical manuscript (hard-wrapped for git diffs). References are
  inline in APA 7 style, and every in-text citation resolves to a reference-list entry.
- **Both artifacts build from `chapter.md`:** `python3 build_artifacts.py`, and
  `python3 build_artifacts.py --check` reports whether either has gone stale. Never edit either by hand.
  The build aborts rather than writing if the unwrap would change a single word of prose.
  - [`chapter_grammarly.md`](chapter_grammarly.md) — the whole chapter, Abstract through Key Terms and
    including the bibliography, with every paragraph unwrapped to one line. Grammarly reads a hard line
    break as a sentence boundary and reports false fragments otherwise; the §7 table is linearized to
    labelled bullets for the same reason. Paste this file into Grammarly.
  - `Full Paper - Alg & Sov.docx` — pandoc, no table of contents, since the IGI template supplies its own
    front matter. Reflow into that template at submission.
- Presentation materials (the SBE 2026 deck and poster) live in [`../presentations/`](../presentations/).
- **Length:** 19,381 words total, 15,796 body, abstract 149, 117 references, 14 Key Terms (measured
  2026-08-15, after the persona panel). The body grew from 11,703 words across that panel's four passes,
  against a plan of roughly 12,600 and a floor of 10,000; `HANDOFF.md` §0j records where the growth went
  and what is safe to cut.
- **Literature-gap pass (2026-07-01):** a fresh Consensus sweep over the chapter's concept clusters added 12
  verified references closing three gaps flagged as reviewer-exploitable: the brokerage literature behind the
  mediated triad (Burt; Obstfeld; Hahl et al. on disintermediation), the two-sided-market economics behind the
  bottleneck and multihoming (Rochet & Tirole; Armstrong & Wright; Eisenmann et al.), and the folk-theory /
  algorithmic-management evidence base under algorithmacy (Eslami et al.; DeVito; Bucher et al.; Wood et al.),
  plus Lei on platform architecture and collective contention and Micheli et al. on data-governance models. All
  entries verified against primary records (issue years, DOIs).
- **Review-driven rewrite:** two peer reviews (recorded in [`../research/findings/review_rewrite.md`](../research/findings/review_rewrite.md))
  drove a pass that **removed IIT from the chapter** (the plain bypass/counterfactual test now carries the
  diagnostic; the companion paper owns the formalism), cut the flagged AI-slop prose, wove §6's foundations
  narratively, and added three substantive pieces (a gritty algorithmacy vignette, the political economy of
  algorithmacy's uneven distribution, and a hotels-vs-OTA worked bypass case).
- **IGI template conformance:** Abstract (148 words, no citations) · Keywords · numbered sections §1 Introduction
  through §10 Conclusion · References (APA, incl. masked "Author (2026)" entry for the anonymized companion
  work) · Additional Reading · Key Terms and Definitions (14 terms). Meets the ≥10,000-word minimum, the
  ≤150-word abstract limit, and the double-anonymized requirement.
- **Final submission-readiness review (2026-07-01):** four parallel reviewers (template/anonymization, citation
  integrity, argument coherence, prose). All findings fixed: abstract re-trimmed under the 150 limit after the
  prose rewrite had inflated it; §2.3's nesting paragraph no longer calls literacy→digital a change in kind
  (the chapter's architecture has exactly two — oral→literate and literate→algorithmic); §5.3's dangling
  "next section" cross-reference now points at §6; the §7 directive wording matches §6/§8 (adopted, in
  transposition); irreducible-vs-necessary usage disentangled (§7, §10, Key Terms); abstract/§1 now carry the
  full three-part definition; plus APA nits ("et al." forms, group-author full form, misplaced Cutolo & Kenney
  citation) and a prose pass (broken parallelism in §9, three overlong sentences split, competences/competencies
  standardized).
- **Scope on measurement:** the chapter *argues* that algorithmacy and coordinative sovereignty need validated
  instruments and sketches the paths in a "Future research directions" section (§9); it does not develop the
  instruments. The actual instrument development lives in `../instruments/` (the follow-on paper's material).
- **Grounding:** every load-bearing claim has been adversarially deep-researched; verdicts and the sources that
  would otherwise be raised against the chapter are recorded in [`../research/`](../research/). The manuscript
  incorporates the pass-1 revisions (co-optation reframed from a "fourth mechanism" to the governance challenge
  of opaque interested mediation; algorithmacy positioned against the algorithmic-literacy literature; the
  change-in-kind claim pinned to coordination not cognition; coordinative sovereignty positioned against the
  concept-stretching critique and its nearest neighbors; the exit/voice bridge pitched as an actionable
  formalization).

## The pivot from the accepted abstract

The accepted abstract set up a typology of three sovereignties and named *algorithmacy* as the competency for
the platform era. This full draft takes the agreed larger pivot: it organizes the argument around three
communicative sensibilities — **oracy → literacy → algorithmacy**, each enabling a form of sovereignty — and
makes the constructive contribution a positive definition of **coordinative sovereignty**, the algorithmacy-era
form. It foregrounds a formal diagnostic (the necessary/contingent bypass test, mapped to exit/voice) as the
methodological core, and sets out the institutions that could realize coordinative sovereignty.

## Review note

For double-anonymized review, the authors' companion computational work (the integrated-information account of
mediated coordination and the necessary/contingent classifier) is cited as "Author, 2026." That apparatus is
presented self-containedly in §5; no code or formal derivations appear in the body.
