# FABLE — fable_2 (rr-2026-11)

Reader: fable_2. Date: 2026-11-08. Cards: 30, verified by verifier_2.

Method. For each card I read the card, verifier_2's section, and the saved source (full text where present under `sources/<citekey>/`, including the four `verifier2/` copies; otherwise the Crossref or OpenAlex abstract fetched today). I re-ran a normalised quote search over every quoted string and resolved the misses by hand (two-column layouts, dropped ligatures, line numbers). Page locators were re-derived from form-feed counts and running heads. I read the four verifier_2 full texts (Martin and Waldman; Pijls et al.; Spektor et al. 2023; Spektor et al. 2025) in full before upgrading `read_depth`. The validator (`library/build_index.py --check`) reports the same errors after my edits as before: five held cards still lack a references.bib entry (lugosi2014, lyons2021, nissenbaum1996, slattery2002, xiang2022). No new errors.

## Per card

| citekey | result |
|---|---|
| lugosi2009critical | no change |
| lugosi2014hospitality | no change (abstract re-checked against Crossref) |
| lynch2017mundane | no change (metadata only; NOT CHECKABLE stands) |
| lyons2021conceptualising | no change |
| martinwaldman2022legitimate | **changed**: abstract → full-text; six located key facts; v4 verdict rewritten to PARTIAL (five mechanisms, not three; lowering is against mere notice in the no-outcome survey; the bad-outcome test is appeal-only); debt flag removed |
| metcalf2023courts | no change (bib given-name defect Tafesse, Emnet confirmed) |
| odekerken2021service | no change |
| okhuysenbechky2009 | **changed**: stale "read full text before submission" bullet retired; p. 493 paraphrase made exact |
| nissenbaum1996accountability | no change |
| papadopoulos2021violation | no change |
| parkinson2022online | no change |
| pan2025dark | no change (no abstract exists in Crossref or OpenAlex) |
| parasuraman2000types | no change |
| pijls2017measuring | **changed**: abstract → full-text; seven located key facts (pp. 128-132); v4 verdict NOT CHECKABLE → YES with cautions (source says "autonomy"; a third autonomy item survived); debt flag removed |
| phillips2024physical | **changed**: abstract-quote locator PDF p. 1 → p. 2 |
| riordan2024digitally | no change |
| raisch2021paradox | **changed**: note added that the full-text label rests on abstract and introduction read closely, body skimmed |
| rihova2018customer | no change |
| santonidesio2021gaps | **changed**: locator §3.2 ¶9 → §3.2.2 ¶3; flag `claim-contradicted` added for the v4 §4 need/trust/risk attribution |
| shryock2012breaking | no change |
| spektor2023designing | **changed**: abstract → full-text; five located key facts (pp. 628-635); v4 verdict NOT CHECKABLE → YES with cautions; debt flag removed |
| shabnam2026tpsr | no change |
| slattery2002finding | no change |
| spektor2025working | **changed**: abstract → full-text; eight located key facts (section loci); first v4 verdict → PARTIAL, second → YES as configuration space, study hotel is the counter-case; debt flag removed |
| vandoorn2017domo | **changed**: hospitality-sentence locator p. 44 → p. 46 (verifier_2 said pp. 45-46; the running head "46" precedes it) |
| wilsonnash2025captivity | **changed**: Summary cut back to the abstract's content; `verified_date` → 2026-11-08; `abstract-only-debt` flag added |
| xing2026algorithmic | no change |
| xiang2022covid | **changed**: "negotiated exception" gloss → "compensation approved by management"; the testing rule was not waived |
| yurrita2023disentangling | no change |
| zientara2023unpicking | no change |

Verifier_2 notes: all accepted. One refinement: van Doorn's hospitality sentence is on p. 46 alone, not pp. 45-46.

## For the authors

Ranked by how much the argument leans on the sentence.

**1. Santoni de Sio and Mecacci (2021) do not supply the duty-trigger typology. v4 §4 (submitted.md line 30):** "Duties differ in what triggers them. Care is owed because someone is in need. Fiduciary duties are owed because someone has been trusted. Governance duties exist because a system creates risk (Santoni de Sio and Mecacci 2021)." REVISION_PLAN §2 *Origin* repeats the attribution. The full article (sources/santonidesio2021gaps/article.txt) contains no "fiduciary", "governance" only inside a cited title, "trust" twice and never as a duty trigger, and no need/trust/risk scheme. It breaks the responsibility gap into culpability, moral accountability, public accountability and active responsibility (§1, §2). This sentence sets up the paper's *Origin* move (arrival as the trigger), so the contrast needs another source or must stand as the authors' own argument. Card flagged `claim-contradicted`.

**2. Martin and Waldman (2023) tested five mechanisms, and "lowered" is relative to notice. v4 §7 (line 67):** "One study compared appeal, oversight, and audit as remedies for an adverse algorithmic outcome: an appeal that reached the decision raised its perceived legitimacy, while oversight and audit lowered it." The study compared notice, impact assessment, external audit, human in the loop and appeal to an internal review board (Study Design, 'Governance'). Appeal was the only mechanism with a legitimacy dividend, and for bad outcomes it "does provide a legitimacy dividend (t = −12.53)" but "did not 'make up' for the penalty" (Results, 'Outcomes and Governance'). Impact assessment, human in the loop and audit "lower the legitimacy of the decision compared to mere notice" in the survey without outcomes (Results, 'Governance and Legitimacy'); no bad-outcome result is reported for them. Faithful wording: "of five governance mechanisms, only an appeal to a human review board raised perceived legitimacy, and it softened the penalty of a bad outcome; impact assessment, a human in the loop and an external audit scored below mere notice." The sentence carries the fourth principle's empirical warrant, so the fix matters.

**3. Yurrita et al. (2023) do not isolate a reachable person. v4 §7 (line 66):** "a person must stay reachable who can actually reverse or revise the decision (Yurrita et al. 2023; Lee et al. 2019)." Contestability raised procedural fairness, but appeal to a different human and appeal back to the same system did not differ (Tukey-adjusted p = 0.45, §5.2, p. 10), and human oversight had no effect. The 75/267 qualitative requests for more human involvement (p. 11) point the right way without carrying the "person" claim. Rest the sentence on "an appeal route that reaches a real re-decision", or on Lee et al.

**4. Spektor et al. 2025 is the counter-case, not the evidence. v4 §4 (line 33):** "housekeeping systems lock task order and, in their most limited configurations, withhold the day's full task list from the very workers carrying it out (Spektor et al. 2023, 2025)." The 2023 paper supports this near-verbatim (pp. 628-629). The 2025 paper describes the one-at-a-time list as a possible configuration (§5.1.1) but studies a hotel where the union contract secured self-sequencing. Both papers also say the restriction is a configuration the property chooses, and 2023 reports many workers negotiated it away (p. 629). Keep the pair but write "configured to lock" rather than "systems lock", and do not lean on 2025 for the restriction. The first 2025 use (line 31, "more and more of their day goes to reading decisions made elsewhere") is PARTIAL: the paper's time cost is documentation labour (§5.3), not reading decisions; Pedersen and Pors must carry that half.

**5. Pijls et al. (2017) kept one autonomy item. v4 §2 (line 19):** "It also tried two questions about agency, whether the guest had a choice and whether they felt independent, and dropped both when the scale was tested." Supported: "feeling independent" and "having choice" were removed at the CFA (§5.2, pp. 130-131). But the source's word is "autonomy", a third autonomy item, "During my visit I experience freedom", is item 3 of the final inviting factor (Appendix A, p. 132), and the authors call the autonomy dimension "new" (p. 129). The follow-on "the questions did not survive" overstates; say the scale folded autonomy into inviting and dropped choice and independence.

**6. Xiang et al. (2022): a compensation, not an exception.** Held card, proposed for §3. The front-office employee, "after checking with hotel management", had the hotel pay for the guest's nucleic acid test and arranged transport (Findings, Stage II). The state-imposed testing rule was not waived; the authors call it a "compensatory measure". Write "a management-approved compensation", not "a negotiated exception".

**7. Zientara et al. (2023) measure intentions. v4 §6 (line 62):** "workers in the sector often prefer to leave quietly rather than speak up." The abstract reports that job dissatisfaction predicts intention to quit and not intention to join a union. Nothing on preference, quietness or behaviour. Soften to "intend to leave rather than join a union".

**8. Odekerken-Schröder et al. (2022) never mention a host. v4 §1 (line 9):** "Service research has quietly handed the host's role to the employee." Zero hits for "host"; the paper frames a technology–customer–employee triad. The host reading and "quietly" are the authors' gloss; fine if marked as such.

**9. Raisch and Krakowski (2021) and Parasuraman et al. (2000) are argued past, not support. v4 §5 (line 38):** "You cannot answer by asking how advanced it is." Raisch says automation and augmentation cannot be neatly separated (p. 192); nothing on advancement. Parasuraman builds the levels-of-automation scale the sentence rejects. Cite them as the positions answered.

**10. Wilson-Nash et al. (rejected card):** the earlier card Summary attributed distinctions from digital exclusion and voluntary unengagement, and named groups (older, disabled, low-income, unbanked), that are not in the abstract. Removed from the card. If the paper is admitted for section 7, nothing beyond the abstract can be quoted until someone reads pp. 974-985.

**Bibliographic.** references.bib gives Metcalf et al.'s fourth author as "Tafesse, Elizabeth"; Crossref and the paper's title block give Emnet Tafesse (card records it; bib not edited). Five held cards (lugosi2014, lyons2021, nissenbaum1996, slattery2002, xiang2022) still need bib entries before `build_index.py --check` passes.
