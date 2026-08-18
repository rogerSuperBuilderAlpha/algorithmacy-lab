# Chapter manuscript — "Algorithmacy and Sovereignty"

Full draft of the invited book chapter for the IGI Global Scientific Publishing edited volume *Organizational
Implications of Digital Sovereignty in the Age of AI* (ed. Samuel Fosso Wamba, TBS Education).

- **Authors:** Roger Hunt (Bentley University), Pierre Berthon (Bentley University), Sara Whitmer (University of
  Iowa).
- **Status:** abstract accepted; full chapter due 2026-08-30 (min. 10,000 words incl. references);
  double-anonymized review; academic APA.
- **Current draft:** `chapter.md`, and it is the only submittable one. Hard-wrapped for git diffs;
  references inline in APA 7, every in-text citation resolving to a reference-list entry.
- **`chapter_v2.md` is superseded.** It was a 2026-08-14 prose rewrite of the same argument against four
  published model essays (`HANDOFF.md` §0e), held at exact content parity with `chapter.md` so the author
  could pick either. The 2026-08-17 fix pass (`HANDOFF.md` §0g) broke that parity: `chapter.md` now carries
  the five-seat panel's corrections and `chapter_v2.md` does not. The evening cascade pass (`HANDOFF.md`
  §0j) is in `chapter.md` only. Keep `chapter_v2.md` for its sentence-merge patterns if a later prose
  pass wants them; do not submit it.
- **THE SUBMISSION FILE is `Full Paper - Alg & Sov.docx`.** Upload that to eEditorial Discovery. Times New
  Roman 12pt, double-spaced, US Letter with 1-inch margins, page numbers top right, APA 7 heading placement
  (level 1 centered bold, level 2 flush-left bold, level 3 bold italic), anonymized. No reflow needed.
- **Generated exports — never hand-edit.** `Full Paper - Alg & Sov.docx` and `chapter_grammarly.md`
  (soft-wrapped, §7's table flattened to a list because Grammarly does not read pipe tables) both derive from
  `chapter.md`. Regenerate with `python3 regen_exports.py` after any edit; `python3 regen_exports.py --check`
  fails if either has drifted, and the script also lints `chapter.md` for the structural faults that break a
  render. The Word styling comes from `reference.docx`, rebuilt by `build_reference_docx.py` — change the
  styling there, not in the output.
- Presentation materials (the SBE 2026 deck and poster) live in [`../presentations/`](../presentations/).
- **Length:** 15,261 words total, abstract 148 (measured 2026-08-17, after the cadence pass).
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
