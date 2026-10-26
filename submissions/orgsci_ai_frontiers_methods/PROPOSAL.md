# The AI Proposes, the Oracle Disposes: An Oracle-Adjudicated Research Loop for Organization Theory

[DRAFTED by Claude, 26 Oct 2026, v2, rewritten against the CFP PDF. Research proposal for *Organization Science*, AI-Enabled Frontiers (Stage 1, due 1 Nov 2026). Anonymous. Contribution types addressed: "AI-enabled research loops under human direction", "Reusable research infrastructure", "Critical, diagnostic, or boundary-setting work". Counts come from the anonymized repository; the hypothesis tally is an automated count of the question records (TECHNICAL_APPENDIX.md, B4).]

## The core contribution

AI research loops face one problem above the others: the system that writes a claim also judges it. A language model that generates hypotheses, runs analyses and writes the paper grades its own work, and its errors come in the same fluent register as its findings. The editors put the open question bluntly: can such loops perform valid social science, or are they "Potemkin villages of slop masquerading as research"?

We propose a methodology that separates the two jobs. In an *oracle-adjudicated research loop*, AI agents do the generative work. They place a question against what is already known, search the literature, write competing hypotheses, design tests and draft the paper. Every empirical claim is decided by a deterministic, exact computation that the agents cannot influence: the *oracle*. The agents may propose anything, but a claim enters the record only as a prediction about the oracle's output, and the prediction is fixed before the oracle runs. The oracle's answer is final. In short, the AI proposes and the oracle disposes.

Organization theory suits this design because many of its central claims are structural. Is the arrangement of a worker, a platform and a customer irreducibly three-party, or does it factor into two-party relations? Does Thompson's (1967) ranking of pooled, sequential and reciprocal interdependence hold? Claims like these can be written as small formal models and settled exactly. Our oracle does this with integrated information theory 4.0 (Albantakis et al., 2023), computed with the open-source PyPhi package (Mayner et al., 2018). Given a Boolean model of a coordination form, it returns an exact verdict. If some cut along party lines leaves the form's cause–effect structure intact, the form is *dyadic*. If no cut does, the form is *triadic*. The method does not depend on this particular oracle. Any exact, deterministic adjudicator of formal models could take its place.

We have built the loop, run it on 170 research questions and audited its failures. In the development stage we will turn it into shared infrastructure, close the integrity gaps the audit exposed, and measure what such loops can and cannot do.

## What we have done

**The loop.** A six-stage orchestration script runs each question, and a researcher sets the question.
1. **Review.** An agent reads the lab's cumulative ledger of prior results, states the gap the question opens, and stops if the ledger already answers it.
2. **Literature.** A research workflow returns 15 to 30 sourced references and states whether the gap is open.
3. **Hypotheses.** An agent writes five distinct, falsifiable hypotheses in a fixed schema, each with its null and its predicted outcome. All five are committed before any computation runs.
4. **Methods.** An agent writes one test per hypothesis. Each test specifies the model, the measure, a known control and a decision rule, in enough detail that a reader could reproduce it without the code.
5. **Run.** Parallel agents write and execute the test code. Each test must first reproduce a known control, such as a strict-mediation triad reading triadic at Φ = 2.0, and aborts if it fails. Each returns confirmed, partial or refuted with the exact numbers, and the results are appended to the ledger.
6. **Paper.** An agent writes the paper and a findings table. Every number must trace to a results file, and refuted hypotheses are reported as refuted.

A regression suite of 542 commands re-runs the code behind the reported numbers and fails if any output changes.

**One run, end to end.** We asked whether the oracle reproduces Thompson's ordering of interdependence. The loop fixed five hypotheses, built each type as a three-party model, and ran the tests. Pooled interdependence read dyadic, while sequential and reciprocal both read triadic, so the top step of Thompson's ordering collapsed. Pooled and sequential each changed verdict when a single edge changed. The loop then proposed a repair, a rule based on two structural primitives, and the oracle refuted it. Four forms share the same pair of primitives, three of them with identical wiring, and they still split across both verdicts. A refutation of the loop's own idea, settled by a computation the agents could not bend, is the method working as designed.

**The record.** Across 163 questions with machine-readable findings tables, the loop fixed 512 hypotheses in advance. The oracle confirmed 399 (78%), refuted 105 (21%) and returned a partial result on 8. A loop that grades itself seldom refutes itself, so a refutation rate of one in five suggests that the oracle, not the agent, settled the outcomes.

**The audit, and what it found.** A high confirmation rate is not evidence of validity, so we commissioned an adversarial review of one seven-question wave, Q111–Q117. The reviewers read the wave through four lenses: the method's assumptions, construct validity, formal method, and research integrity. They found four failure modes, each specific to AI-run research.
- **Non-severe testing.** The wave confirmed 24 of 24 hypotheses. Several were true by construction; one restated the efficiency axiom of the Shapley value.
- **Leaky pre-commitment.** In some questions the agents computed exploratory values before fixing their hypotheses, and so "predicted" results they had already seen.
- **One agent in six hats.** A single agent in one session produced the review, hypotheses, code, results and paper, so every gate was self-administered.
- **Vocabulary drift.** The oracle's numbers were exact, but the prose described them in economic terms such as "rent", "scarcity" and "value capture" that no computation licensed. The agents also treated Φ magnitudes as a cardinal scale, although the lab had declared them at most ordinal.

The oracle catches false claims about its own output. It does not catch an interpretation laid over a true number, a hypothesis chosen because it cannot fail, or a prediction made after peeking. In the questions run after the review, the refuted share rose from 17% to 25%. We report this as a first observation, not as a causal effect.

## What we hope to do

The development stage would build three things.

**1. Integrity mechanisms for the failures we found.**
- *Sealing.* The loop hashes each hypothesis set to an external timestamp, and the orchestration blocks any call to the oracle until the seal exists.
- *Role separation.* A vetting agent rates each hypothesis's risk before the run and flags identities and by-construction claims. An auditing agent checks results and prose without seeing the predicted outcomes.
- *Severity monitoring.* The loop tracks the confirmation rate for each wave and treats a run of confirmations as an alarm, not a success.
- *Claim tracing.* Every sentence in a generated paper that states a finding must map to a computed quantity. Interpretive terms that have no computed referent are flagged for the human director.

**2. A reusable, oracle-agnostic loop.** We will package the loop with an oracle interface. An oracle takes a formal model and returns a verdict together with the controls that validate it. The release will ship with the Φ oracle and with a second oracle built during development, a cooperative-game solver that settles claims about stable divisions of joint output. Organization scholars could then plug in agent-based simulations, game solvers or other exact computations from their own areas. The loop will run on open-weight models as well as commercial ones, so other researchers can reproduce it.

**3. A test of what the loop can and cannot do.** We will rerun a fixed sample of questions under four conditions:
- the current loop;
- the loop with the integrity mechanisms;
- the loop on an open-weight model;
- an independent human re-implementation of a random subset.

For each condition we will measure the refutation rate, the share of hypotheses that are true by construction, the share of claims that trace to a computed quantity, and agreement with the human re-implementation. The result is a direct, quantitative answer to the editors' question for one class of theory.

## Key risks

**A narrow oracle.** Exact adjudication is available only for claims that can be formalized, and exact Φ becomes impractical beyond about ten nodes. The method covers structural theory about small coordination units, not every organizational claim. The oracle interface is how other adjudicators would widen that reach.

**The validation gap.** A verdict on a formal model is evidence about that model. It is not evidence that real workers experience an arrangement as irreducible. The loop makes theory exact; it does not replace fieldwork.

**Translation.** Judgement enters at the step from a verbal theory to a formal model, and AI agents can take that step without anyone noticing. Two defensible encodings of the same arrangement can disagree: in our field protocol, four of ten invented cases flip verdict under a second encoding. The loop will require several encodings per claim, with a human sign-off on each.

**Volume over value.** A loop that has run 170 questions could flood the literature, which is the editors' "more, not better" concern. Our answer is selection by the human director, together with severity monitoring that rewards refutation over confirmation.

## How organizational science would change

Organization theory develops largely in words, and verbal claims about structure are hard to refute. An oracle-adjudicated loop turns those claims into experiments that are stated in advance, run exactly and logged whatever the outcome. AI contributes what Girotra, Terwiesch and Ulrich (2010) identify as the source of the best ideas, a large and varied pool of candidates. The oracle, not the AI's judgement, does the filtering. The ledger makes the work cumulative: each new question starts from every prior result, refutations included, and every number can be re-run. Beyond organization theory, the method offers a template for AI-enabled social science in which the AI never grades its own work, with a measured account of where that safeguard still fails.

## References

Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Girotra, K., Terwiesch, C., & Ulrich, K. T. (2010). Idea generation and the quality of the best idea. *Management Science*, 56(4), 591–605.

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

Thompson, J. D. (1967). *Organizations in action: Social science bases of administrative theory*. McGraw-Hill.
