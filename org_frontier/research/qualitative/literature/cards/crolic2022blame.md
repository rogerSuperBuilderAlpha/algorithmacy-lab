---
citekey: crolic2022blame
title: Blame the Bot: Anthropomorphism and Anger in Customer-Chatbot Interactions
authors: Crolic, Cammy and Thomaz, Felipe and Hadi, Rhonda and Stephen, Andrew T.
year: 2022
doi: 10.1177/00222429211045687
arxiv: null
journal: Journal of Marketing
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://ora.ox.ac.uk/objects/uuid:73d46bba-35d1-465c-be00-aa6f4f4ccb84/files/r5x21tf917
sha256: 5e00289536b1c44adba50f4aedb3cffcc9aa7551dd24922d55b42a8cae99b2c5
pdf_path: literature/pdfs/crolic2022blame.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how anthropomorphizing customer-service chatbots (giving them names, avatars, first-person language) affects customer responses, and whether this depends on the customer's emotional state. Across five studies — one analysis of a large real-world data set from an international mobile telecommunications company plus four MTurk experiments — the authors find that when customers enter a chatbot-led service interaction in an angry state, chatbot anthropomorphism has a negative effect on customer satisfaction, company evaluation, and purchase intentions, but this harm does not appear for customers in nonangry states. The proposed mechanism is an expectancy violation: anthropomorphism inflates pre-interaction expectations of chatbot efficacy, and when actual performance fails to meet those inflated expectations, angry customers (who are motivated to blame and respond punitively) react negatively. Study 3 shows the negative effect disappears when the chatbot effectively resolves the problem; Study 5 shows it disappears when the firm explicitly lowers customer expectations beforehand. The authors conclude firms should match chatbot anthropomorphism to emotional context, e.g., deploying non-anthropomorphic bots in complaint-handling roles or downplaying bot capabilities for angry customers.

## Key facts it relies on
- Study 1 real-world data set: 1,645,098 lines of customer text from 461,689 unique chatbot sessions, collected Sept 2016-Aug 2017 in one European country; only ~7.5% of sessions (34,639) received a 1-5 star satisfaction rating, mean (SD) = 2.16 (.79).
- Study 1 operationalized anger and "anthropomorphic treatment" via the LIWC dictionary; anthropomorphic treatment = count of times the customer used the chatbot's name (mean .032, SD .178, range 0-6). An extended ordinal probit model with sample-selection correction handled the 7.5% rating rate.
- Study 1 result: main effects of anthropomorphic treatment (β1 = -.055, n.s.) and anger (β2 = -.002, n.s.) were nonsignificant, but their interaction was significant and negative (β3 = -.167, p = .05); at high anger (+1 SD) the marginal effect of anthropomorphic treatment was -.350 (p = .02), and at zero anger it was nonsignificant (.011, p = .32), consistent with H1a.
- Study 2 (N = 197 after exclusions; 2x2 chatbot x scenario emotion): significant chatbot x emotion interaction on satisfaction (F(1,193) = 5.26, p = .02); angry customers were less satisfied with the anthropomorphic bot (M = 2.09) than the control (M = 2.58, F = 4.13, p = .04); no significant effect in the neutral scenario. A parallel sadness manipulation reversed the pattern (anthropomorphic bot rated higher: Mcontrol = 1.90 vs Manthro = 2.53, p < .01).
- Study 3 (N = 365; 3 anthropomorphism levels x 2 outcome): when the outcome was ambiguous, angry customers rated the company lower with a verbal+visual anthropomorphic bot (M = 4.28) than control (M = 5.06, t = 2.75, p < .01), supporting H1b; when the chatbot resolved the problem, no difference between conditions (F < 1).
- Study 4 (N = 171): significant chatbot x emotion interaction on purchase intentions (F(1,167) = 4.29, p = .04); angry customers reported lower purchase intent with the anthropomorphic bot (M = 2.73) vs control (M = 3.57, p = .02). Pre-interaction efficacy expectations were higher for the anthropomorphic bot (Mcontrol = 4.94 vs Manthro = 5.50, p = .01) but post-interaction assessments did not differ, producing a larger expectancy violation (Mcontrol = .85 vs Manthro = 1.62, p = .01). Moderated mediation (Hayes Model 15) confirmed the indirect effect of expectations on purchase intent was significant for angry customers (.0675, 95% CI [.0012, .1707]) but not neutral.
- Study 5 (N = 302): explicitly telling customers "please don't get your hopes too high" eliminated the negative effect — in baseline expectation the company was rated lower with the anthropomorphic bot (M = 3.90 vs 4.63, p = .04), but in the lowered-expectation condition there was no difference (Mcontrol = 4.25 vs Manthro = 4.32, F < 1).
- Definitions/framing: anthropomorphism is the attribution of humanlike properties to nonhuman agents (Epley, Waytz, and Cacioppo 2007); an expectancy violation is negative disconfirmation arising when pre-usage expectations are high or post-usage performance is poor (Cadotte, Woodruff, and Jenkins 1987). The chatbot market was forecast to exceed $1.34 billion by 2024, and ~20% of call-center interactions involve hostile/angry customers (Grandey, Dickter, and Sin 2004).

## Critical notes from the literature
- The authors flag that Study 1 anthropomorphism could not be experimentally varied (all customers saw the same highly anthropomorphic, clearly female, smiling bot), so they relied on customers' name-use as a proxy for anthropomorphic treatment, and both anger and anthropomorphic treatment were measured (not manipulated) behaviors — motivating the four follow-up experiments.
- The paper notes its session-level anger measure implicitly assumes anger is exogenous; robustness checks confirm anger is not strictly exogenous but also arises from the exchange itself (number of exchanges, language-recognition variance). A binary-treatment robustness model still supported the result (angry: β1b = -.573, p = .04; Wald χ2(2) = 6.62, p = .04).
- The Study 4 overall index of moderated mediation was not significant (indirect effect = .0279, 95% CI [-.0778, .1562]); support for mediation rests on the a-priori split indirect effect within the anger condition only.
- Several experiments used MTurk samples and scenario-based (imagined/simulated) chatbot interactions rather than naturally occurring anger, and the Study 2 chatbot interaction outcome was deliberately ambiguous; the authors acknowledge anger may not be the only relevant emotion and that future, more advanced AI could eliminate the expectancy-violation gap (which they note does not appear imminent, citing Shridhar 2017).

## Key topics covered
chatbot anthropomorphism; customer anger; expectancy violation theory; pre-interaction efficacy expectations; customer satisfaction; company evaluation; purchase intention; agency attribution; functionalist and appraisal theories of emotion; LIWC text analysis; NLP on chat transcripts; extended ordinal probit with sample-selection correction; moderated mediation; AI in customer service; managerial deployment of conversational agents
