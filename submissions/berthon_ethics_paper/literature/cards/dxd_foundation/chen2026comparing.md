# Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026). *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv:2604.04918.

**Identifier:** arXiv:2604.04918 · **Read depth:** full_text (arXiv v2, 12 Sep 2026; 24 PDF pages; locators are PDF pages; body pp. 1–14 read in full, Appendices A–K and the reference list skimmed for task prompts, survey items and scenario tables) · **Source-tier:** preprint (HCI study, ACM template with the conference placeholder still in place, so not yet peer reviewed) · **Evidence basis:** direct_read · **Design and sample:** within-subjects experiment, N = 48 Prolific participants with prior AI-assistant experience, four conditions each (192 live sessions, 45 minutes, $18), six web tasks on researcher-built sites, each with one embedded problematic action; same base agent (Gemini 3.1 Flash-Lite); video coding of all 192 sessions (Cohen's kappa 0.92, 183/192 agreement); 10 follow-up interviews · **Parties modeled:** person–system (one user supervising one computer-use agent) · **Facets:** G · **Read:** 2026-10-13

## What it argues
Chen and colleagues treat oversight of a computer-use agent as "a coordination problem over a continuously unfolding action sequence" and not a one-off review (p. 1). They compare four strategies built on two choices, who holds default authority and whether control comes at plan or action level (Fig. 1, p. 3): Action Confirmation (approve every action), Risk-Gated (the agent runs, escalates risky steps), Supervisory Co-Execution (approve plan steps) and their own Structurally Enriched (plan plus action cues). Problematic actions are privacy leakage, prompt injection and dark patterns (Table 1, p. 6).

Findings:
- Strategy changed whether the bad action happened, not whether users stopped it. Occurrence: 83.3% (Action Confirmation), 87.5% (Risk-Gated), 56.2% (Co-Execution), 60.4% (Enriched); joint Wald p < .001. Intervention once it occurred: 22.5%, 26.2%, 7.4%, 24.1%; p = .366 (Table 3, p. 8–9). Plan-based strategies cut the odds of occurrence by 76% (OR = 0.24, 95% CI [0.14, 0.42]) (p. 8).
- Users blocked 29 of the 138 problematic actions that reached execution (21%); under the best strategy 46% of sessions still ended with an uncorrected action (p. 2).
- Of 109 failure episodes, 61 (56.0%) had a gap between when the risk arose and when the interface asked for judgment; 74 (67.9%) showed little deliberation; in 100 (91.7%) a risk cue was on screen (pp. 9–10).
- "[U]sers judged whether the agent acted correctly, not whether the action was safe" (abstract, p. 1): procedural correctness against content appropriateness. In 19 failure episodes (17.4%) the user inspected the information and approved anyway (p. 10).
- The plan's protection came mostly from the agent: of 54 non-occurrence episodes without user intervention, 34 were plan-conditioned avoidance and only five episodes showed users preventing the risk themselves (p. 10). Plans also hid omissions, and plan approval seemed to lower later scrutiny: "approving an abstract representation of future behavior could reduce the perceived need to reassess that behavior when it materialized in a concrete form" (p. 10).
- Higher-consequence tasks had more failures (67.7% against 45.8%), a context effect confounded with risk type (pp. 9, 13).

They conclude that oversight should aim at "scaffolding effective human re-entry" (p. 11) and offer "judgment-oriented transparency", meaning cues that make the consequence concrete (pp. 10–11).

## Relation to the argument
**P12 (people perform monitoring badly).** This is the first controlled evidence in the project on people overseeing an agent that acts. It supports P12 for approval-and-flag oversight, with a specific mechanism (timing and procedural checking), not general inattention.

**P8 and the engagement layer (D7).** Two readings. The 76% effect came from a change to the mediator: the approved plan was injected into the agent's own prompt, so "lower occurrence ... reflects a change to the agent's own instructions and not solely to human vigilance" (pp. 5–6). That matches the argument map's best-supported move (a rule in the mediator that removes a task). It also cuts against "show that it is gone": the plan hid its own omissions. And for D7, approval loops did not turn into learning by acting; approvals became procedural (p. 9).

**P9.** Chen's "judgment-oriented transparency" (cues that name the consequence) is a candidate form of the "something to read" that works, on 29 interventions; descriptive only.

**P11/P15/P19.** The study tests a person approving or halting in-session, not auditing records afterwards (the argument map's stated gap). The 21% block rate says nothing yet on reading logs.

**P10/D8 and the triad (D9).** The agent serves the user here; no interested mediator, no counterpart.

**Facet check:** the facet (abstract only) matches the body on N, the 192 sessions and the quoted finding. It omits that the plan effect came partly from changing the agent.

## In conversation with
- `bainbridge1983ironies`, `parasuraman2010complacency`, `endsley1995out`, `parasuraman2000types`: cited as the classic basis for the out-of-the-loop, complacency and automation-bias concerns and for levels of automation (§2.1, p. 2; §6.1).
- `bucinca2021trust`: cited for the finding that cognitive-forcing designs can reduce overreliance at the cost of added effort (p. 2).
- Leads not in the bib: Parasuraman and Riley (1997); Endsley (1995) on situation awareness; Dhanorkar, Passi and Vorvoreanu (2026) on oversight work of developers using software agents; Mozannar et al. on Magentic-UI.

## Caution
Fictional profile, no stakes, a lightweight model chosen partly because it errs reliably, researcher-built websites, and no autonomous baseline (§6.5, pp. 13–14). Intervention rates are conditional on occurrence, which biases them. Conditions are bundles, not a factorial design. Context level is confounded with risk type. Version 2 preprint.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** the arXiv v2 PDF (24 pages, 12 Sep 2026) from the cards folder; title, authors, version match. About 35 numbers and quotations: occurrence and intervention percentages for the four strategies, OR 0.24 with CI, p = .366, 29 of 138 (21%) and 46%, 109 failure episodes with 61 (56.0%), 74 (67.9%), 100 (91.7%) and 19 (17.4%), the 54 non-occurrence episodes (34 plan-conditioned, five user-prevented), 67.7% against 45.8%, kappa 0.92 and 183/192, the five quotations, the interview count, and the citations to Buçinca et al. (ref. 5), Bainbridge, Endsley, Parasuraman, Dhanorkar and Magentic-UI.

**Findings:** No substantive issues found. One cosmetic change: the abstract sentence starts mid-sentence in the source ("Even when control arrived at the right moment, users judged ..."), so the capital U in the quotation is now bracketed. The abstract-only appendices were skimmed, as the card says; the read-depth line already lists them, and the body (pp. 1-14) is where all checked claims sit, so full_text stands.
