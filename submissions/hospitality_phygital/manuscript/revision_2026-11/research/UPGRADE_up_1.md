# Full-text upgrade, label `up_1` (rr-2026-11, 2026-11-08)

All 13 PDFs are the right works: title, authors and DOI match each card. All 13 cards are now `read_depth: full-text`. `abstract-only-debt` was removed where it was set. Status is unchanged on every card. Quotations in each card's key facts were checked by script against the PDF text: all fragments found, except two that span a page header or a footnote numeral (Gursoy pp. 155–156; Bovens p. 453), which were checked by eye. Locators are printed journal pages, except Shabnam et al. (unpaginated, PDF pages). I did not regenerate `CARDS_INDEX.md`, which is now stale; `build_index.py` validation of the cards passes.

## Per card

| card | version read | verdicts changed |
|---|---|---|
| kropf2026blame | Springer VoR, OA, 18:30, 14 pp. | "role responsibility of a carer" YES→PARTLY; "challenge from care" not supported as opposition; Kropf et al. *support* human accountability staying put |
| kong2026delegation | Springer VoR, OA, 6:518, 14 pp. | principle and ground quoted (pp. 4–5); supports Transfer conclusion, contradicts role-based ground; hold_rationale updated |
| wilsonnash2025captivity | Wiley VoR, OA, 43:974–985, 12 pp. | exclusion/unengagement distinction confirmed (p. 976); "grounds the second condition" PARTLY |
| didomenico2007host | T&F VoR, 26(3) 321–338, 19 pp. incl. cover | "negotiated" use PARTLY; `swap-candidate` added |
| golubovskaya2017meaning | Emerald VoR, 29(5) 1282–1304, 24 pp. | displacement clause SUPPORTED; obligation content NOT SUPPORTED |
| lind1990voice | APA VoR scan, 59(5) 952–959, 9 pp. | v4 sentence PARTIAL→SUPPORTED; "limit" sentence contradicted; `claim-contradicted` added |
| beatty2016compliance | SAGE VoR, 19(2) 158–173, 16 pp. | §6 sentence YES→PARTLY (sample is oil-change and pest-control staff); §2 list PARTLY stands |
| gursoy2026reconceptualizing | T&F VoR, 35(2) 151–165, 16 pp. incl. cover | both uses SUPPORTED; `must-engage` kept with locator p. 160 |
| liu2026hospitableness | Elsevier VoR, OA, 135:104640, 11 pp. | "test" YES→PARTLY; perceive/owe contrast SUPPORTED (p. 9) |
| shabnam2026tpsr | Emerald published-online, OA, unpaginated, 17 pp. | opacity/rigidity SUPPORTED; seamlessness claim PARTLY; overlap with reachable-person principle found |
| bovens2007accountability | Blackwell VoR, 13(4) 447–468, 23 pp. | definition SUPPORTED; §7 roadmap use contradicted; §4 PARTLY; `claim-contradicted` added |
| hatherley2025moving | Springer VoR, OA, 27:20, 15 pp. | all three uses PARTLY |
| sharmamattila2025rights | SAGE VoR, 50(6) 904–920, 17 pp. | SUPPORTED; year confirmed 2026 (card frontmatter says 2025, bib is right) |

## For the authors

Ranked by how much the argument leans on the point. v4 text is quoted exactly; plan moves are paraphrased from REVISION_PLAN.md.

1. **Plan §2 *Transfer*: ownership "moves only with the role", and "Kropf et al.'s challenge from care".** Neither source supports the role premise, and Kropf et al. are no challenge to the conclusion. Kropf et al. let a scoped role pass to a machine ("can still hold role responsibility based on their social function", abstract) while keeping accountability human: "the answerability of care robots is currently inconceivable" (p. 9); "Holding robots to account is problematic, as it could lead to a diffusion thereof, allowing humans to evade moral responsibility" (p. 12). Kong reaches the plan's conclusion ("One who elects a delegate that cannot answer thereby elects to answer for it", p. 10; "a smaller quantity with an address", p. 10), but on a different ground: "A role matters derivatively rather than intrinsically" (p. 4). He also sets fiduciary duty aside as "a different matter again" (p. 4), so the trustee/successor comparison has no support there. If Transfer stays, Kong should be cited for the conclusion. The role-based ground then has to stand as the paper's own argument.

2. **v4 line 30: "Kropf et al. (2026) argue that a robot can hold the role responsibility of a carer without being a moral agent".** PARTLY. The robot's role is explicitly not a carer's: "A care robot in a nursing home does not have the same role obligations as a nurse" (p. 4); "not to confuse the role of Pepper in a care facility with that of a human nurse" (p. 6). The rest of the sentence ("narrows the responsibility gap without displacing human accountability") is supported (pp. 9, 10, 12).

3. **Plan §2 *Distinctness*, hospitality's content as "an obligation owed to this arrival", if Golubovskaya et al. is used for it.** NOT SUPPORTED. They define hospitality as "an essence, or spirit, and service as a process" (p. 1283), "an attitude and spirit with which service is performed" (p. 1287), and list obligation only among others (p. 1284). Use them only for displacement: "only the minority (6 of 22 participants) were able to define and describe hospitality" (p. 1296).

4. **Plan §3 and WS_C synthesis: Di Domenico and Lynch show host and guest "building 'negotiated normative practices' ... with the owner present to settle them".** PARTLY. "Negotiated normative practices" appears only in the abstract (p. 321). The findings show host rule-setting and guest deference instead: "The balance of power in the host/guest relationship is perceived by hosts to rest firmly with them" (p. 332); "in a hotel one might complain about the beds being uncomfortable, but as the guest in the home one does not, it's not the done thing" (p. 333); "decisions pertaining to access and behavioural conduct lie much more with host than guest" (p. 335). It is better used as the copresent-host baseline, and as a warning that copresence alone did not let guests press claims.

5. **v4 line 73: "constituting a forum that is required to answer challenges and making sure someone in that forum has real authority to act, and preserving a meaningful alternative for those who decline the automated route (Bovens 2007)."** CONTRADICTED. In Bovens the *actor* answers and the *forum* questions: "the actor has an obligation to explain and to justify his or her conduct, the forum can pose questions and pass judgement" (p. 450). The alternative route is not in Bovens. Wilson-Nash et al. carry it: "co‑existence (analogue retained but downgraded and more difficult to access)" is itself a captivity trigger (p. 978), and avoidance "may enhance vulnerability by restricting access to essential services" (p. 979).

6. **Plan §7: Wilson-Nash et al. "grounds the second" constitutional condition (a real alternative).** PARTLY. The paper shows why the alternative matters and names "allowing consumers to choose modes of access (e.g., digital, analogue)" as a mitigator (p. 981). It frames the stake as stress and vulnerability, not accountability: DTC is "the condition in which consumers feel constrained ... This state produces stress through felt entrapment" (p. 975). Date: the running foot reads "Psychology & Marketing, 2026; 43:974–985", so citing it as 2026 matches the version of record.

7. **v4 line 71: "The effect has a limit, and it runs the other way. An invitation to speak that was never going to bear on anything lowers those judgments instead of raising them, and the same research warns that a sense of fairness can be manufactured this way."** CONTRADICTED by Lind et al. Their never-going-to-bear condition (goal "would not be changed regardless of what the subject said", p. 954) *raised* both judgments: "for both fairness variables, all pairwise comparisons among the voice conditions were significant" (p. 955, note 3). Lowering is only "conceivable" (p. 953). The "manufactured" warning is real (p. 958), but it says hollow voice *raises* perceived fairness. The preceding v4 sentence is now fully SUPPORTED by Lind alone.

8. **v4 line 34: "the arrangement separates the power to make or shape decisions from the duty to answer for them (Bovens 2007)."** PARTLY. Bovens's nearest point is the problem of many hands, which is about finding *who* "can be brought to account" (p. 457), not about a separation of power from duty. His corporate accountability of "the organisation as actor" (p. 458) would support the *Holder* move.

9. **v4 Hatherley uses.** All three PARTLY.
   - Line 39 ("forecast the guest ever better while the rules ... change without warning"): nothing on forecasting.
   - Line 59 ("no one tells the employee or the guest"): Hatherley's problem is unintelligible change, not unannounced change.
   - Line 65 ("make significant rule changes visible"): Hatherley doubts the remedy. Informing users of updates "may not reduce the epistemic or safety risks of update opacity" (p. 11). The depreciation of learned knowledge is supported: "model updates have been found to disrupt users' mental models" (p. 5).

10. **v4 line 68: "But in these frameworks smoothness itself has stayed a goal, never a suspect."** PARTLY for Shabnam et al. They fault the field's "dominant emphasis on ... seamless channel integration and engagement optimisation" (PDF p. 2) while still treating friction as a cost to reduce (PDF p. 10). They also recommend that "algorithmic governance must remain contestable ... escalation pathways and human oversight" (PDF p. 14). That is a prior statement of v4's reachable-person principle and should be cited there.

11. **v4 line 59: "Frontline staff have always weighed and accommodated requests that fall outside the standard case (Beatty et al. 2016)."** PARTLY. The data are from "an oil-change company and a pest-control company" (pp. 160–161), not hospitality. Line 14 stays PARTLY: Beatty supports only the exception request, which customers make without knowing "whether the request falls inside or outside" the firm's parameters (p. 159).

12. **v4 line 29: "Studies of 'robotic hospitableness' test whether a robot can make guests feel welcomed, attended to, and reassured (Liu et al. 2026)".** PARTLY on the verb: "Future studies should test the framework" (p. 9). Usable for the next sentence: robotic hospitableness "is relationally experienced by guests rather than internally possessed by the machine" (p. 9).

Also: Gursoy's uses are supported, but p. 160 ("Algorithmic governance shifts authority from interpersonal judgment to computational logics, raising questions about accountability when harm, bias, or exclusion arise") is the nearest statement of the authority–answerability split in the field. §4 should engage it.
