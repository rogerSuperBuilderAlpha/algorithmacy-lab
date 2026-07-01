# Review-driven rewrite

Two peer reviews of the landed chapter. Both judged the core contribution strong and original — the
necessary/contingent bypass diagnostic, algorithmacy, coordinative sovereignty, and the digital-vs-coordinative
disaggregation — and both confirmed the references hold up with no fabrications. They converged on two fixable
weaknesses: AI-slop prose (defensive throat-clearing, explicit signposting, a listy "four foundations") and the
IIT move in §5, which read as borrowed math. They split on IIT: Review 1 said drop or de-center it; Review 2
praised it as a strength.

User decisions: **remove IIT from the chapter entirely** (the plain bypass/counterfactual test carries the
diagnostic; the companion paper owns the formalism), and do the full pass — prose de-slop plus three substantive
additions.

## What changed

- **IIT removed from §5.** Rewrote §5.1 to lead with and rely on the plain factoring/bypass logic; cut "the
  distinction is not a metaphor," "whether it factors can be computed," the integrated-information language and
  the "least damaging partition" phrasing; removed the two IIT references (Oizumi et al., 2014; Albantakis et
  al., 2023) — cited nowhere else. Softened "partition" to "division into parts," "read off the computation" to
  "follows from the same counterfactual," and simplified the §5 and §5.1 headings. No IIT residuals remain
  (grep clean). The companion paper keeps its formal apparatus; the chapter now points to it lightly.
  `instruments/formal_standing.md` is untouched — the removal is scoped to the chapter.
- **Prose de-slop.** Cut the specific throat-clearing both reviews flagged: §1 "the argument has three moves,"
  §2.1 "not antiquarian," §2.2 "has a lineage … is best stated as," §3.2 "not a failure of will," §5.1 "not a
  metaphor," §6 "not a diminished version" and "a new coinage must answer the charge." Humanized the §4
  from-within/from-outside passage. Wove §6's four foundations narratively ("takes from republican theory … It
  takes from relational autonomy … From Markell … And from Ostrom") instead of "The first is … The second is."
  Antithesis density fell from ~9.1 to ~7.5 per 1,000 words.
- **Three substantive additions.** A gritty algorithmacy-in-practice vignette in §4 (an unannounced ranking
  change halving a seller's orders, and how she detects, re-models, and recovers). A political-economy passage
  on the uneven distribution of algorithmacy (who can afford it; platforms' incentive to keep the rules opaque
  and the competence scarce; coordinative sovereignty concentrating where algorithmacy is already held). A
  verified worked bypass case in §5.4 — hotels vs. online travel agencies, where the OTA is a contingent
  rate-parity gate (bypassable by book-direct campaigns and the European parity bans) plus a necessary demand
  aggregation (the billboard effect a lone hotel cannot reproduce; direct-booking share plateaus near a third).

## Conformance held

~12,900 words (≥10,000); abstract 146 words (≤150, no citations); all sections intact; every in-text citation
resolves both ways after the two removals; double-anonymized. Prose only; `classifier/` untouched.
