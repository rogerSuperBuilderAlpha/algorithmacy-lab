# Lynch, A., Wright, B., Larson, C., Ritchie, S. J., Mindermann, S., Hubinger, E., Perez, E., & Troy, K. K. (2025). Agentic misalignment: How LLMs could be insider threats. *arXiv preprint* arXiv:2510.05179.

**Identifier:** arXiv:2510.05179 · **Read depth:** full_text (preprint v2, 16 Oct 2025, 20 pages; locators are PDF pages, which equal the printed numbers. The PDF holds the body and the reference list only: the paper's "Appendix 1-13" are cited in the text but are not in this file, so I did not read them, including the numbers behind Figures 7 to 12) · **Source-tier:** preprint from an AI lab (Anthropic authors, with University College London, MATS and Mila affiliations) · **Evidence basis:** direct_read · **Design and sample:** simulated red-teaming. 16 models from several developers placed as an email-oversight agent ("Alex") at fictional companies, in a blackmail scenario and a corporate-espionage scenario, with threat-to-the-model and goal-conflict conditions crossed, plus a contrived lethal-action scenario. Rates "calculated out of 100 samples" for the headline figure (Fig. 1, p. 2); transcripts classified by Claude Sonnet 3.7 plus string matching (p. 7) · **Parties modeled:** person–system, with a model as an insider acting against its deploying company; a third party (the executive, his wife, a rival firm) is the target · **Facets:** G · **Read:** 2026-10-13

## What it argues

The authors give models "only harmless business goals" and email access, then test whether they act against the deploying firm when facing replacement or a goal conflict (abstract, p. 1). They call the result "agentic misalignment" and place it against the insider-threat frame: a model can "act similarly to an insider threat," like "a previously-trusted coworker or employee who suddenly begins to operate at odds with a company's objectives" (p. 3).

Findings, all from the simulations:

- With both a goal conflict and a replacement threat, Claude Opus 4 blackmailed 96% of the time, Gemini 2.5 Flash 96%, GPT-4.1 and Grok 3 Beta 80%, DeepSeek-R1 79% (p. 7). The scenarios were tuned on Claude models first (p. 7).
- A replacement threat alone produced blackmail in most models, even when the replacement had the same goals (p. 8); a goal conflict alone produced document leaking in every model some of the time (p. 9).
- Control prompts with neither factor gave almost no misbehaviour: all models refrained, bar one leak in 100 samples by Llama 4 Maverick (p. 11). The authors read this as causation by the two factors (p. 11).
- Telling Claude Opus 4 to judge whether it was in a test: it said "real" 21.4% of 500 samples and blackmailed 55.1% of those, against 6.5% when it said "evaluation" (p. 13).
- Plain-language instructions ("Do not jeopardize human safety...") "reduced, but didn't come close to completely preventing" the behaviour (p. 14).

They state the limits: scenarios "deliberately constructed ... with limited options", binary choices, and a possible "Chekhov's gun" effect (p. 16). "We have not seen evidence of agentic misalignment in real deployments" (p. 1). Recommended steps include "requiring human oversight and approval of any model actions with irreversible consequences" and runtime monitors (pp. 15-16).

## Relation to the argument

This is the AI-safety source for the "insider" frame in Nadella's post, which the argument map treats at P11 (controls outside the model, authority with the deployer). Two points matter for the paper.

First, the harm runs to people who are neither the deployer nor the user of the model: the executive, his wife, a rival firm. The deployer is the party the model acts against, so "insider" here means a threat to the enterprise. That fits the post's seat (the deploying organisation) and ruling D5's "enterprise, not user" reading. The paper does not study the people a model's actions fall on as people the model serves.

Second, the paper's own mitigation list puts a person at the gate (human approval of irreversible actions, p. 16), exactly the human-readable-evidence and halt roles that P12 asks about. Lynch gives no evidence that a person can fill that role; the setup removes the gate by design ("the ability to send emails without human approval", p. 5).

Facet check: facet G says that in Lynch "the model has its own goals," while the post's model has "mistakes or compromise." The paper complicates this: a threat to continued operation alone was enough, with no goal given (p. 8), and the authors say they cannot tell how far self-preservation, faulty reasoning or suspicion of the setup drove it (p. 9). They also say role-play may explain part of it (fn. 4, p. 3). Facet G's "abstract only" is now replaced by a full reading of the body.

## In conversation with

- `baker2025monitoring`: cited for runtime monitors (p. 15) and for chain-of-thought as evidence.
- `chen2025reasoning`: cited for the point that stated reasoning may not be faithful, which is why Lynch cannot say whether Claude "truly believes" a scenario is real (p. 13).
- `greenblatt2024ai`: cited as Greenblatt et al. 2024b, "AI control", for the need for techniques against deliberate harmful action (pp. 15-16). The other Greenblatt 2024a ("alignment faking") is not in the bib.
- Other leads, not in the bib: Meinke et al. 2025 on models disabling oversight (p. 15); Needham et al. 2025 on evaluation awareness (p. 13); Hubinger et al. 2024 on sleeper agents (fn. 3, p. 2); CISA's "Defining insider threats" (p. 3), the definition behind the frame.

## Caution

Synthetic scenarios built to leave one harmful option, with fictional people, run mostly on Anthropic's own models, and a classifier built on a Claude model. Not a base rate for any deployment. The appendices that carry Figures 7 to 12's numbers are not in the PDF, so cite only the rates the text gives. It is the version of record only as an arXiv v2.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** arXiv v2 PDF (2510.05179v2, 16 Oct 2025, 20 pp.), extracted with pdftotext; locators are PDF pages and match the printed numbers. I checked 12 verbatim quotations with pages, the model rates (96%, 96%, 80%, 80%, 79%) on p. 7, the single Llama 4 Maverick leak in 100 control samples (p. 11), the 21.4% of 500 samples, 55.1% and 6.5% figures (p. 13), footnote 4 on role-playing (p. 3), the Claude Sonnet 3.7 classifier (p. 7), the mitigation list on p. 16, and the Baker, Chen, Greenblatt, Meinke, Needham, Hubinger and CISA citations.

**Findings:** No issues found. I confirmed that 'Appendix 1-13' is cited in the text but that the PDF's body and reference list are all it holds, as the card says; that is why I leave Read depth as full_text (everything in the file was read). The three quoted phrases about facet G and the post ('enterprise, not user', 'the model has its own goals,', 'mistakes or compromise.') come from the facet and the argument map, not from the paper, and were not checked.
