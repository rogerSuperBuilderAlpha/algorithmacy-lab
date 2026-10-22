[DRAFTED — Claude, 22 October 2026. Evaluation of the three AI-generated reviews of "Spaces in the Stream" against the current Doc (pulled 22 Oct 16:51 → `gdoc_full_2026-10-22d.md`). Evidence is in `RESEARCH_NOTES_2026-10-22.md` and `APPENDIX_A_changelog_verbatim.md`. Line numbers (L###) refer to `gdoc_full_2026-10-22d.md`.]

# Evaluation of Reviews R1, R2 and R3

**R1** is skeptical and substantive. It includes a stylistic audit and line edits. **R2** is positive and mostly stylistic. **R3** is detailed and formal, with tables for the stylistic audit.

## Summary verdict

- **R1 is the most useful review.** Its four structural objections hold up against the text and the sources: Criterion 4, the H conflation, the missing third party, and the study's coverage of its predictions. Research supports each of them. A few of R1's factual claims describe an earlier version of the abstract, and some of its style rules contradict your own.
- **R3 makes the best formal and mechanical catches.** It found the "while → In contrast" corruption, the Criterion 2 endogeneity, the Criterion 3 / seeded-error contradiction, and the negative-G problem. But it keeps H as a single construct, and its suggested rewrites add jargon and fresh em-dashes.
- **R2 is the weakest of the three.** It says the paper "does not over-extend the scriptio continua analogy" (wrong; see OPEN_ISSUES B1.5) and that it is "publishable after a focused stylistic revision" (wrong; see the structural problems below). It also wants every em-dash removed, which contradicts `writing-style.md`.
- **Every reviewer missed several problems**, found by the independent analysis:
  - **P12 contradicts the formula.** Under G = F × MI, marking raises G by ΔF·MI, so the gain is *larger* for experts and the gap *widens*. P12 predicts the gap narrows.
  - **Film-cut evidence cuts against Proposition 4.** Zacks et al. (2009) found that cuts *reduce* segmentation once situation changes are controlled: "cuts, by themselves, do not cause people to perceive event boundaries."
  - **The novelty claim has close prior art:** Hippo (Pang et al., 2025), HiLDe (Anaya González et al., 2025) and Glassman et al. (2024, "AI-Resilient Interfaces").
  - **The power analysis is wrong.** With f = .22, the target power .85 needs N = 40; N = 32 gives power .763 (I recomputed this).
  - **Several sources are misreported:** Tsoukala, Buçinca, Metzner, Prajod, Gould, Johnson p. 608, Gal et al., Stark & Vanden Broeck's wording, and Cox's quotation.

Verdict key: ✔ correct · ◐ partly correct · ✘ wrong · ⟲ superseded (it describes an older version) · ≡ already logged in OPEN_ISSUES (ID given).

---

## R1

| # | Claim | Check | Verdict | Action in v2 |
|---|---|---|---|---|
| 1.1 | The paper is neither Paper 1 nor Paper 2 of the dissertation plan, and §5.3 imports Paper 2 material | Memory and the dissertation plan; §5.3 Marks 1–4 | ◐ (a placement call that is yours to make) | Flagged as [DECISION D7]. §5.3 cut back (D3). |
| 1.2 | Cut the pre-title structured summary; its Contributions paragraph should replace the end of §1 | L1–21 | ✔ | Summary cut; Contributions moved to the end of §1 [DECISION D6]. |
| 1.3 | Abstract is "330 words, eleven em-dashes" → cut to 200 | Current abstract: 286 words, 1 em-dash | ⟲ (counts) / ✔ (target) | The 200-word target stands because *HCI*'s instructions require "an unstructured abstract of 200 words" (tandfonline author instructions, read 22 Oct 2026). |
| 1.4 | Two bracketed placeholders in propositions (4) and (6) | L49 | ✔ ≡ A5 | Replaced with "interface marks" / "interface marking". |
| 1.5 | The triad needs its third party named for the coding case: the vendor (Simmel's tertius) | L39, L43, Prop 1; §5.3 names worker, platform, consumer | ✔ (substantive) | [DECISION D4]. Drafted option offered, clearly marked. Simmel's tertius is in Part II, pp. 174–182 (verified). |
| 1.6 | "Idempotent" is misused | L43, L45, L47, L49, L65 | ✔ ≡ A8 | Replaced with "non-binding" or "inconsequential" in the generation sense. L65's "no-op" sense is kept and reworded. |
| 1.7 | §3 numbering is off by one; >20 cross-references are wrong | Headings unnumbered for the case; cross-references follow the roadmap | ◐ (the cross-references are internally consistent; the *headings* are wrong) | Case numbered 3.1, the rest renumbered 3.2–3.6. About 25 cross-references now resolve without being edited. |
| 1.8 | §4.6 cites §2.2 for Rayner et al. (1998) figures that are in §2.1 | L276 ×2, L280, L316 | ✔ (four sites, not one) | Fixed. |
| 1.9 | §2's opening buries its claim | L55 | ✔ | Claim sentence moved to the front, your wording kept. |
| 1.10 | §2.1 objection paragraph uses "idempotent" | L65 | ✔ | Reworded (see 1.6). |
| 1.11 | §2.5 leans on a non-significant Delgado moderator | L93 discloses non-significance, then uses the authors' interpretation | ◐ | Kept, softened to the source's "may add". Delgado = 54 studies / 76 comparisons. |
| 1.12 | Mangen statistic "η = .08 2" | L93 shows "2‬ = .08"; source t(48) = 2.03, η² = .08 | ✔ (export loss) | Restored as η² = .08. |
| 1.13 | Cite Rayner (1998) directly, not "as cited in Schotter" | L294 | ✔ | Fixed. |
| 1.14 | Verify each changelog claim; add a verbatim appendix | Done (Appendix A) | ✔ | 6 of 8 verify. **v2.1.283 is wrong:** the auto default reached every plan in v2.1.283–2.1.284 and was earlier on Pro, Max and Team, not "enterprise and team". "Sixteen months" → "nearly seventeen". v1.0.33 is "Improvements to plan mode" (≡ G12). |
| 1.15 | Timeout until July 2026 vs "never auto-resolve on idle" (2026d) | tools-reference.md L138 | ◐ (no contradiction: the timeout governed AskUserQuestion only) | One clause added saying so. |
| 1.16 | /rewind passage is a fragment | L107–109 | ✔ ≡ G29 | Rejoined with the original "and" (from `SECTION3_1_claude_code.md`). |
| 1.17 | Governing-question paragraph repeated three times | L127, L135, L141 | ✔ | Kept once in full; the other two compressed. |
| 1.18 | Gap stated three times | Seven instances | ✔ (understated) | One gap statement in §3.6, narrowed (see the novelty row below). |
| 1.19 | Criterion 3 is relational; Criterion 4 is reader-side and fails the definition → drop C4; rename Prop 1 "Representation Independence" | Formal audit; R-D research (Bailey et al., 2017; Zacks et al., 2009) | ✔ (Criterion 4 is also circular with P4 and contaminates the Condition 2 control) | [DECISION D1]. C4 moves from the rule to the alignment moderator; Prop 1 renamed. Criterion 3's task-dependence is conceded in one sentence. |
| 1.20 | The formula omits H | L346, Fig 4.1 | ✔ | Full specification written once (see R3.1). |
| 1.21 | H conflates structural co-optation with overreliance → split | Stark & Vanden Broeck read in full: their co-optation is structural ("leverages rather than delegates", p. 14), and "fluency", "persuasion" and "ratify" do not occur. The H evidence (Kim 2025, Steyvers 2025) is overreliance. | ✔ (substantive) | [DECISION D2]. Split into co-optation (C, structural: who places the point, writes the options, sets the default) and overreliance (O, epistemic). Prop 3 renamed. |
| 1.22 | Condition 2 doesn't test P7; RQ3 is a hidden fourth condition | L357, L368 | ✔ | [DECISION D5]. P7 declared not tested here; RQ3 cut to a follow-up. |
| 1.23 | P13 is untestable with N = 42 | The paper never states the sample is AI-literate | ◐ | P13 restated as a boundary condition. |
| 1.24 | f = 0.22 is not "medium" (Cohen: .25) | Recomputed | ✔ | Power corrected (N = 40 for .85; recruit 50). |
| 1.25 | I/we inconsistent | 5 sites | ✔ ≡ G7 | "I" throughout. |
| 1.26 | Prop 2's broken sentence; Prop 3's dash; "algorithmate"; bold sentence in §5.2 | L212, L214, L384, L379 | ✔ | Fixed. |
| 1.27 | §5.3 is a detour: "mark" has two meanings; Simmel 1902b is not in the reference list | L403–410 | ✔ (the 1902b point is half right: Part II is listed under "1902"; the "b" is the problem) | [DECISION D3]. Platform-labour half reduced to one deferral paragraph; "b" dropped. |
| 1.28 | §5.4 is polemical; reframe with Braverman, Bainbridge, Endsley, reactance | Research R-H | ◐ (tone correct; Braverman unverifiable and outside the paper's scope) | Counterpoint 1 reframed on Bainbridge (1983, verified) and Lee et al. (2025); reactance named as a measurable construct. No Braverman. |
| 1.29 | Scribner & Cole "proved" → "found" | L432 | ✔ | Fixed (also "established" at L190). |
| 1.30 | §6 is repetitive | L446–450 | ◐ | Tightened; the last sentence realigned with Prop 1 (see R3.9). |
| 1.31 | Citation items: Simmel b, Manzey 2008, Zhu initials, Street page, Yang 2027, Kurby & Zacks mapping, Metzner, Oberschelp | Audit | ✔ (all real); additional items found | Street p. 77. Yang 2027 is correct (vol. 217, issued Jan 2027). Manzey via "as cited in Parasuraman & Manzey (2010, p. 401)". Metzner overstated (87% accuracy without regression). **Oberschelp (1995, p. 121) does use "algorithmacy", beside literacy and numeracy.** Leese & Matzner (2016) is a second, unpublished use. |
| 1.32 | Style lists (crucially, fundamentally, merely, essential, decisive, foster; filler transitions; em-dashes; passives) | `writing-style.md` | ◐ | Emphasis markers cut. **"Furthermore/Moreover" are kept where they mark a real relation; your style file says they are ordinary venue usage.** Em-dashes triaged, not removed (86 → paired bolt-ins recast, gloss-welds kept). |
| 1.33 | Line rewrites | — | not adopted verbatim | Your wording kept; the reviewers' sentences were used only to locate problems. |

## R2

| # | Claim | Verdict | Note |
|---|---|---|---|
| 2.1 | "Publishable … after a focused stylistic revision" | ✘ | The structural problems in R1.19–1.24 and the misreported sources come first. |
| 2.2 | "Does not over-extend the scriptio continua analogy" | ✘ ≡ B1.5, B1.7 | Johnson (2000, pp. 593, 608–609) contradicts §1 ¶3 and the abstract (silent reading was ordinary; early Roman texts separated words). R2 read only the §2.1 limits paragraph. |
| 2.3 | Stark & Vanden Broeck "used precisely" | ✘ | L169's "platforms co-opt and enroll them" splices p. 5 and p. 14, and turns their passive "are co-opted" into an active verb. "Coordinative co-optation" is your term. |
| 2.4 | Hirschman "applied cleanly" | ◐ | Asserted, not traced through the mechanism. Moot if §5.3 is cut (D3). |
| 2.5 | Remove all em-dashes | ✘ | `writing-style.md`: "do not ration below roughly 3 per 1,000." |
| 2.6 | Soften "fundamental category error", "interface pathology", "tyranny of convenience" | ✔ | Done. "Category error" is kept. |
| 2.7 | Praises the four-part rule as a strength | ✘ | Criterion 4 fails the definition (R1.19). |
| 2.8 | "Crucially" in §4.6 and §5.2 | ✔ | Cut. |

## R3

| # | Claim | Check | Verdict | Action |
|---|---|---|---|---|
| 3.1 | Additive H gives negative G and violates P13; use G = (F×MI)·(1−H), H ∈ [0,1] | Formal audit: the multiplicative form fits Prop 5, P9, P13 and L438. The additive form fits P8's "independently" and the figure. | ◐ (corrects a formula the paper never writes, but the multiplicative specification is the better default) | Adopted for **overreliance O**: G = F × MI × (1 − O), O ∈ [0,1], stated as ordinal. Co-optation C enters upstream, through who places the points (A and M). P8 reworded to "controlling for dwell". |
| 3.2 | Criterion 2 endogeneity: lexical markers or unfaithful reasoning traces reintroduce representation dependence → define at the task-structural level, with domain-expert coding | L266; R-J research (reported once the agent finishes) | ✔ (important) | C2 redefined as a non-unique specification where a domain expert would name more than one viable alternative. Lexical markers kept as cues only. |
| 3.3 | Criterion 3 vs seeded errors at "non-decision intervals" → distinguish load-bearing from local errors; split P6/RQ2 | L267 vs L360 | ✔ | P6 split into P6a (load-bearing) and P6b (local, upstream). The error-balancing sentence rewritten. |
| 3.4 | §5.3: rename "Marks" to "Institutional Conditions"; tie voice and exit to G | — | ◐ | Superseded by D3 (the platform-labour material is deferred). |
| 3.5 | An automated editing pass corrupted "while" into ". In contrast," (§4.6, §3 /rewind) | Style audit: 17 sites; originals recovered from earlier drafts | ✔ (5 sites change the logic: L75, L109, L280, L296, L316) | All five restored to the recovered original conjunctions. |
| 3.6 | "Evaluate the issue" is a dangling imperative | L111 | ✔ | Fixed. |
| 3.7 | The Metzner citation is orphaned in §2.2 | L73–75 | ✔ (and the content is overstated; see the audit) | Rejoined and corrected to the source's wording. |
| 3.8 | Cohen's κ dropped; Tatasciore run-on | L272, L125 | ✔ | Fixed. |
| 3.9 | The conclusion's last sentence contradicts Prop 1 ("where decision points are *presented*") | L450 | ✔ | Realigned. |
| 3.10 | De-polemicising table (e.g., "compliance ratifications", "transaction cost of passive ratification") | — | ◐ | Polemic cut. R3's replacement jargon not adopted. |
| 3.11 | Claim-first rewrites of the §2.x openings | — | ◐ | Claim-first applied, your wording kept. |
| 3.12 | Em-dash audit: remove all | — | ✘ | As R2.5. |

## Problems no reviewer raised

| # | Problem | Evidence | Action in v2 |
|---|---|---|---|
| N1 | P12 contradicts G = F × MI (the gap widens) | Formal audit | P12 restated with its assumption explicit: experts already fixate decision spaces in unmarked streams (a ceiling on F), so ΔF is larger for novices. [VERIFY: no direct evidence; flagged as an assumption.] |
| N2 | Marks alone may not induce boundaries | Zacks et al. (2009): cuts *reduce* segmentation (OR .70); Schwan et al. (2000); Gold et al. (2017) | Prop 4 / P4 restated: marks *aligned* with process transitions facilitate segmentation, misaligned marks do not (moderated by alignment). |
| N3 | Boundary costs | Swallow et al. (2009); Speer & Zacks (2005); Zacks (2020) via Huff et al. (2012) | One sentence in §4.7 and §4.9 (≡ A18). |
| N4 | Closest prior art missing | Hippo; HiLDe; Glassman et al. (2024); Spatharioti et al. (2025, uncertainty highlighting); Si et al. (2024) | Added to §3; gap narrowed to the typology plus supervisor-directed marking in agent output. [VERIFY-READ] on the preprints. |
| N5 | "Only two streaming studies" is outdated | Su et al. (2026, arXiv 2609.24616): eye tracking, N = 53, code rendering (abstract read) | §5.1 caveat updated. |
| N6 | The algorithmacy / algorithmic-literacy distinction is threatened | Tankelevitch et al. (2024, CHI): "metacognitive monitoring and control" | §4.1 adds Tankelevitch; the distinction rests on triadic co-optation, not on steering alone. |
| N7 | Prior use of "algorithmacy" | Oberschelp (1995, p. 121); Leese & Matzner (2016) | §4 acknowledgement rewritten [DRAFTED]. **Your Substack says the term "has never appeared in a published academic text"; that is wrong.** |
| N8 | Misreported sources | Tsoukala (the caveat belongs to the interaction); Buçinca (carb-source detection only; trust and preference not significant); Metzner; Prajod (reversed at L388); Gould (L310 contradicts the title); Johnson p. 608 (cited at L61 for the opposite of his argument); Gal et al. (first quote cites Marr & Hagston); Cox ("prior to"); P&M pages 401/402; Ridley p. 4; Zacks 2009 Exp. 1, not Exp. 3; Rayner 54%/44% (≡ B2.1) | Each flagged inline `[FLAG …]` with the source value. Fixed only where the fix is mechanical (pages, quotation wording). |
| N9 | Missing reference entries | Zwaan & Radvansky (1998); Manzey (2008) | Added (Zwaan & Radvansky record verified by the agent [REC]). |
| N10 | Outdated Claude Code claims | v2.1.275 send-now key interrupts the turn (17 Sep 2026); "nudges" misattributed to the classifier (L111); "the default choice" (L65): the docs do not say the first option is preselected | Fixed or flagged. |
| N11 | Vendor evidence for the throughput thesis exists | Anthropic auto-mode posts (25 Mar 2026; 7 Aug 2026): users reject 39% of plans and 3% of individual prompts; the classifier caught 89% of dangerous commands against 13.6% for human reviewers | Offered for §3.1 and Counterpoint 1 as [VERIFY-READ]. The posts must be read before citing. |
| N12 | Costs of interrupting | Wu et al. (ICML 2026): late interruptions cut reasoning accuracy by up to 60% (record) | Named in Counterpoint 1 as [VERIFY-READ]. |

## Cross-review conflicts: how they were settled

| Conflict | Resolution | Basis |
|---|---|---|
| Drop Criterion 4 (R1) vs keep four criteria (R2, R3) | Move C4 out of the locating rule into the alignment moderator and the mechanism (§4.7). The rule has three criteria. | Definition test plus Bailey et al. (2017), Zacks et al. (2009) and Schwan et al. (2000). |
| Split H (R1) vs one multiplicative H (R3) | Split the constructs. Apply R3's multiplicative form to overreliance only. | Stark & Vanden Broeck read in full; no study separates default effects from fluency effects (a testable gap). |
| Cut §5.3 (R1) vs rename and expand it (R3) | Keep the coding-agent scope paragraph; defer platform labour to the dissertation. | §1 brackets labour governance; "mark" collision. |
| Analogy fine (R2) vs overstated (OPEN_ISSUES) | OPEN_ISSUES B1.5 stands. | Johnson (2000). |
| Remove all em-dashes (R2, R3) vs your rules | Your rules win: recast the paired bolt-ins, keep the gloss-welds. | `writing-style.md`. |
