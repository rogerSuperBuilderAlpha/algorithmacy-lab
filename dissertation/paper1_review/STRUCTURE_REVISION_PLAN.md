# Structure revision plan — Paper 1 (post structural review)

Three structural reviews of the draft as an integrative literature review, read against the genre standards
the paper itself cites (Torraco 2005/2016; Cronin & George 2023; Post et al. 2020; Kunisch et al. 2023;
Rousseau 2024). The macro-structure is sound and the method section is exemplary; every flagged item is a
**consolidation** problem traceable to the same origin — the paper was assembled from independently drafted
section files. None touches the argument. Decisions locked with the author: **trim-and-rebalance §5** (not
dissolve); **keep "competency" + the sensibility footnote**; **keep the five-Cs intro, fix §1.4**.

Binding constraints for the whole pass: preserve the argument and the §4 charitable-representation; every
surviving citation stays and resolves; any citation removed must have its *only* appearance in a cut
paragraph (verify by grep before removing from the working reference list); re-run the bibliography dedup and
the slop scan after; `[N]` stays flagged for the author.

## Step 1 — The three conditions: specify once (§3 owns), reference elsewhere

All three reviewers flag that signal asymmetry / intent compression / opaque mediation are fully specified in
§1.4, again in §3.2–3.4, again in §6.2, and recapped in §8.

- **§1.4** (per the locked intro decision): pull the full naming-and-definition of the three conditions. Keep
  the course-of-action move (name algorithmacy; say the form imposes conditions that §3 will specify). The
  three condition-defining paragraphs (each ending `: *signal asymmetry*` / `*intent compression*` /
  `*opaque mediation*`) collapse to a single forward-gesturing paragraph. **§3 introduces them; §1.4 only
  points.**
- **§6.2**: the intro sentence currently re-states "Signal asymmetry calls for… intent compression calls
  for… opaque mediation calls for…". Replace with a reference: each dimension answers to one of the three
  conditions §3 set out. The dimension bodies stay.
- **§8**: the §8.2 recap keeps one brief mention (a conclusion may recap), phrased as reference, not
  re-specification.

## Step 2 — Foreclosure and recent-reviews evidence: each lands once

- **Recent-reviews "don't name the axis":** the *same* three reviews (Hillebrand, Murray, Raisch & Krakowski)
  currently appear in **both §3.5 and §4.7**. Remove the sentence from **§3.5** (let §3.5 end on the
  worker-competency question without the review roll-call); keep it in **§4.7**, the foreclosure synthesis,
  its natural home. The §2.2 saturation check (Kadolkar/Keegan/Bankins/Gagrčin/Dedema) is a *different* set
  doing a *different* job (search-completeness, not theoretical-synthesis absence) — keep it, and add one
  clause so the two reads are clearly distinct rather than the same move three times.
- **Foreclosure restatements:** trim the fully-argued restatements of "the limit is structural, not
  remediable" in §1.2/§1.5 and §8 to pointers. §1 may preview and §8 may recap, but cut any sentence that
  *re-argues* the structural limit; §4 does the work.
- **§4.7:** confirm it *synthesizes* (names the field-level dyadic-inheritance pattern) rather than re-listing
  what 4.1–4.6 already showed. (Closers were tightened in the rhythm pass; verify no residual re-assertion.)

## Step 3 — §5 trim-and-rebalance (the headline fix)

Goal: shift the synthesis center of gravity back to §4 by *reducing* §5, not expanding §4. §3 owns triadic
irreducibility (§3.1 already carries Simmel/Krackhardt/Peirce-via-Short/Battiston 2025/Siltaloppi & Vargo +
the brokerage tradition + co-optation).

- **§5.2 — cut the redundant irreducibility proofs.** Remove the two paragraphs that re-prove what §3.1
  already established:
  - the higher-order-network re-proof ("Mathematics confirms what Simmel argued… Battiston 2020/2021;
    Lambiotte, Rosvall & Scholtes; Burch's Peircean reduction thesis");
  - the correlation-device game-theory excursion ("Mathematical economics has independently identified…
    Aumann 1987; Myerson 1982; Bergemann & Morris 2016").
  Replace both with a one-sentence cross-reference to §3 ("the form's irreducibility, established in §3…").
  **Keep** the distinctive §5.2 material: Latour's intermediary/mediator distinction, the ANT / fractal-dyads
  limit, and the four-feature "platforms are not generic Latourian mediators" argument (with Burrell &
  Fourcade and Kockelman). *Citations leaving the paper if unused elsewhere:* Aumann, Myerson, Bergemann &
  Morris, Lambiotte/Rosvall/Scholtes, Burch — verify each appears nowhere else before removing from the
  working list.
- **§5.1 — keep the warrant, trim the excursions.** The oracy→literacy precedent is load-bearing (it
  justifies a *new* construct rather than an extension); keep it. Tighten the cognitive-neuroscience stretch
  (Dehaene/Wolf/Olson/Menary) and compress the contemporary-philosophy convergence name-list
  (Stiegler/Floridi/Hui/Hansen and Chun/Mackenzie/Bucher/Striphas) to its essential claim — these support but
  do not carry the coordinative argument. Ensure §1.3's brief precedent gesture does not pre-empt §5.1.
- **§5.3 — divide the labor with §3.** §3 owns co-optation-as-mechanism; §5.3 owns the differentiation of the
  platform from the *other* fourth-mechanism candidates (community / gift / commons-based peer production /
  platform co-op). Trim any co-optation re-statement that §3 already made.

Net: §5 contracts; §4 (foreclosure) becomes the proportional and structural center the genre expects.

## Step 4 — §1.4 (covered in Step 1) and the footnote

- §1.4 fix is in Step 1. The competency/sensibility footnote **stays** (author's decision); leave as is.

## Step 5 — Author-only item

- **§2.1 `[N]` corpus count** — replace the placeholder with the real screening yield. The author sets this;
  it is a factual claim about the search and is not to be fabricated.

## Step 6 — Finalize

Regenerate `DRAFT.md`; run the slop scan (no new agentless passives / em-dashes / contractions);
citation-integrity check on the entries that moved or left; confirm 229-minus-removed references resolve;
update `COMBINE_REPORT.md` with the structural pass; commit.

## Explicitly NOT doing (per locked decisions / scope)

- Not dissolving §5 or relocating Latour/Stark into §3 (chose trim-and-rebalance over Review 3's dissolve).
- Not renaming the construct to "sensibility" (keeping competency + footnote).
- Not collapsing the five-Cs intro subheadings (keeping the scaffold, fixing only §1.4).
- Not adding new argument, constructs, or citations — this is a structural-editing pass only.

## Already addressed before this plan (noted so reviewers' points are not re-litigated)

- §7's "tonally severed" register (contractions, cadence) — fixed in the de-slop rewrite; §7 now matches
  §3–§6.
- The construct-by-construct template rhythm in §4 and the dimension-paragraph isomorphism in §6 — fixed in
  the deeper rhythm passes.

---

## Execution status — COMPLETE

All steps run. Body **~21.5k → 20.1k words**; bibliography **229 → 221** (nine §5.2/§5.1 citations removed:
Aumann, Myerson, Bergemann & Morris, Lambiotte/Rosvall/Scholtes, Burch, Battiston 2020, Battiston 2021, Wolf,
Menary — each verified orphaned paper-wide before removal; Battiston 2025 and the brokerage/Simmel anchors
stay in §3). §4 is now the proportional center.

- **Step 1:** §1.4's three condition-defining paragraphs collapsed to one forward-gesture; §6.2 and §8 now
  reference §3's conditions rather than re-specify them.
- **Step 2:** the duplicate Hillebrand/Murray/Raisch roll-call removed from §3.5 (kept in §4.7, which now
  flags itself as the theoretical-synthesis complement to §2's search check); §8's construct-by-construct
  re-walk compressed to a three-sentence synthesis pointer.
- **Step 3:** §5.2's three redundant irreducibility proofs (Simmel restatement + higher-order networks +
  correlation-device game theory) replaced by a one-paragraph §3 cross-reference that keeps the
  divide-and-conquer point and bridges to the four-feature mediator argument; §5.1 cognitive-neuroscience
  tangents trimmed; §5.3's co-optation restatement referenced to §3 and two agentless passives fixed.
- **Step 5:** §2.1 `[N]` left as the flagged placeholder (author sets it).
- **Step 6:** regenerated; slop scan clean (em-dashes only the `[N]` placeholder, 0 contractions, 0
  agentless); touched citations confirmed to resolve; no bibliography orphans created.
