# Who Holds the Decision: How a Poster, an Automated Moderator, and a Trust-and-Safety Team Settle a Takedown

A takedown decision is settled by three parties: a poster who writes, an automated system that flags and acts, and a policy team that sets the rules and hears appeals. Catalog priors predict that the system, because it keeps a record of each poster, takes the larger share of the coordination, and that the policy team above it joins the top of the arrangement and adds its own share, while the poster is squeezed toward nothing. This study uses interviews and document analysis with trust-and-safety staff to find how the three actually coordinate a keep-or-remove decision, and where the priors break.

For work aimed at publication, follow [PUBLISHING.md](../PUBLISHING.md). The sections below carry the elements a reviewer looks for.

## Fit

A takedown decision leaves a paper trail of flags, scores, and appeal logs, but the trail records outcomes and hides the coordination that produced them. How the automated system, the policy team, and the poster divide the work of a decision, and who the people inside the system take to be holding it, can be reached only by asking them and reading what they write to one another. This is a question about felt authority and accomplished practice, and fieldwork is the way to it.

## The prior

The nearest priors in this lab's catalog are two, layered. The first is the mediator with memory ([../../threads/memory/THREAD.md](../../threads/memory/THREAD.md)): a mediator that accumulates a state of its own, a record that carries from one step to the next, takes a far larger share of the coordination's credit than a memoryless one, 0.88 against 0.55, without changing whether the coordination commits or who holds the bottleneck. The automated moderator is exactly such a mediator. It keeps a history on each poster, a strike count, a reputation score, a model of past behavior, and that accumulated state is the self-loop the thread varies. The prior predicts that the system's memory concentrates credit on the system, and that a poster recovers ground only by keeping a record of its own, an account, an appeal history, a paper trail it can produce.

The second prior is oversight ([../../threads/oversight/THREAD.md](../../threads/oversight/THREAD.md)): a principal placed over the mediator and genuinely coupled to it joins the major complex, becomes a co-bottleneck in some forms, and takes a substantial share of the credit, while the mediator's own share rises and the two parties below are squeezed toward a negative remainder. The policy team is that principal. It sits above the automated system, writes the rules the system applies, and hears the appeals the system's decisions generate. The prior predicts that a team coupled to the system both ways reads as a second party at the top of the irreducible core, raising the system's share and leaving the poster unrelieved. A team that only watches the system reads as outside the coordination, an audience.

Layered, the two priors set a sharp expectation. A takedown is coordinated by a system that remembers and a team that oversees, both at the top, the system holding the bottleneck and the larger credit, the team holding a co-bottleneck and a credit of its own, the poster squeezed toward nothing.

The expectation is held open, because the contribution is built where the field departs from it. Three departures are live, and the study is designed to find which one the setting shows. The policy team may turn out to be a spectator the moderators never actually read, a body that writes rules into a document no one at the decision consults and hears appeals long after the outcome is fixed, in which case the oversight prior's observing-principal case holds and the team is outside the coordination, not at its top. The automated system may convey where the prior expects it to commit, flagging and queuing a decision that a human always finalizes, in which case the system is a channel and the bottleneck sits with whoever signs the removal. The poster may keep enough of a record, a documented edit history, a public audience, an appeal it can escalate, to hold real ground against the system's memory where the prior expects it squeezed out. Each departure is a different finding, and each refines a different prior.

## Setting and boundary

The recurring act is one keep-or-remove decision on one piece of posted content. A poster publishes something. The automated system scores it against a policy, flags it, and either removes it, restricts its reach, or routes it to a queue. A trust-and-safety reviewer or policy owner resolves what the system routes, and hears the appeal if the poster files one. The decision closes when the content stays up, comes down, or is reinstated.

Inside the boundary: the poster, the automated moderation system, and the trust-and-safety function that owns the policy and the appeal. Outside: the audience that reports content but does not decide it, the legal and government bodies that set external constraints, and the engineering team that builds the classifier but does not run a given case. The audience report enters the boundary only as an input the system scores. The unit stays at three parties, with the fourth, the wider platform, present only as the source of the rules.

## Parties

**The poster.** Holds a state: an account, a posting history, a strike or reputation record visible to the platform, and whatever record the poster keeps independently, screenshots, drafts, a following that can be mobilized. Updates that state with each post and each appeal. A candidate for the squeezed party the priors predict, and a candidate for the party that holds ground if its independent record is real.

**The automated moderation system.** Holds the largest state: the policy thresholds, the classifier's score on the content, and the accumulated history on the poster, the strike count and reputation the system reads back in on the next decision. This is the memory the mediator-with-memory prior turns on. Updates with each decision. The candidate veto player and credit-holder.

**The trust-and-safety team.** Holds the policy text, the queue of routed cases, and the appeal record. Writes the rules the system applies and rules on the appeals the system generates. The candidate for the coupled principal at the top, or, if the moderators never read what it writes and it only ratifies outcomes after the fact, the candidate spectator.

## Methods

The study draws on the interview and document methods in [METHODS.md](../METHODS.md), with interviews as the primary source and policy and log documents providing triangulation.

Semi-structured interviews with 20 to 25 trust-and-safety practitioners, recruited through professional networks and sampled for variation in role, frontline reviewers who resolve queued cases, policy owners who write the rules, and appeals specialists who handle escalations, and for variation in platform size, since a large platform's reliance on automation differs from a small one's. Interviews run 60 to 90 minutes, audio-recorded with consent, transcribed verbatim. A draft guide appears in Exhibit A. Sampling continues until interviews stop yielding new second-order themes.

Document and log analysis, covering the public policy text each platform publishes, the internal enforcement guidance reviewers actually apply where it can be obtained, and de-identified samples of appeal correspondence and case logs that show how a decision moved among the system, the reviewer, and the poster. Documents corroborate what interviews report about where a decision is fixed and who reads whose record. Folk-theory elicitation runs inside the interviews, asking practitioners to narrate, in their own terms, what the automated system is doing and where the real decision sits.

Coding uses two coders on the interview transcripts, with inter-rater reliability reported on the second-order themes. The study proceeds under institutional review board approval, obtains informed consent, and excludes any content or correspondence that could identify a poster.

## Data structure

The path from raw material to claim follows Gioia, Corley, and Hamilton (2013). Open coding builds first-order categories in the practitioners' own terms, the language they use for what the system does and what they do. Constant comparison groups these into second-order themes that name the practices analytically. The themes compose the aggregate dimensions the finding turns on, which are allowed to take whatever shape the data support. The product is a data structure tracing each step, with a table of representative quotations so a reader can audit the move from evidence to claim (Pratt, 2009). The illustrative rows below show the intended form.

| Representative quote (first-order) | Second-order theme | Aggregate dimension |
| --- | --- | --- |
| "The score already knows the account. A clean account and a repeat offender get read completely differently on the same post." | The system reads its own record back in | Accumulated state shapes the decision |
| "I sign the removal, but by the time it reaches me the system has decided. I'm confirming." | The reviewer ratifies what the system routed | Where the decision is fixed |
| "Policy writes the rule and never sees the case. We apply a document; they don't watch us apply it." | The policy team is read once, then absent | Coupling versus spectating at the top |
| "A poster who screenshots everything and has a following gets a different appeal than one who doesn't." | The poster's own record buys leverage | What the squeezed party holds back |

## Findings

For a stand-alone study, the findings are the thick description: how practitioners experience the arrangement, what they take the automated system to be doing, where authority over the keep-or-remove outcome is felt to sit, and where their accounts diverge. The study expects to report whether the system's accumulated record on a poster is felt to drive the decision or merely to inform a human who decides, whether the policy team is read at the moment of decision or only writes a document consulted earlier, and whether posters who keep their own record are experienced as holding real ground. Each claim is grounded in concrete evidence from a named role.

## Contribution

The theoretical idea is a refinement of the two priors, stated so another study can build on it. The mediator-with-memory prior predicts that an automated moderator's accumulated record on a poster concentrates the coordination's credit on the system. The oversight prior predicts that a policy team coupled to the system joins the top and raises the system's share. This study finds the conditions under which those predictions hold in lived practice, and the conditions under which they break: when the policy team is read at the moment of decision versus consulted once and then absent, when the system commits the outcome versus conveys it to a human who commits, and when a poster's independent record buys back enough leverage to resist the system's memory. The departure, wherever it falls, names a boundary condition the in-silico priors could not see, and gives the catalog a field case of memory and oversight in a setting that keeps both.

## Trustworthiness

The study pursues the four criteria of Lincoln and Guba (1985). For credibility, it triangulates interviews against policy documents and case logs, returns emerging themes to a subset of participants for correction through member checks, and engages each site over a sustained period. For transferability, it provides thick description of the platforms, the roles, and the enforcement context, so a reader can judge where the findings travel. For dependability, it commits the interview guide and the initial coding scheme to a dated record before fieldwork and maintains an audit trail of analytic decisions. For confirmability, the data structure and quotation table tie each claim to evidence. A reflexive memo tracks the specific risk that the priors lead the analysis to see a system holding the decision where practitioners experience a human holding it, and the memo logs instances that cut against the priors as well as instances that fit.

## Limits and what would falsify this

A finding that the automated system holds the decision would be overturned by evidence that a human reviewer routinely overrides it and that the system's record functions as advice a reviewer is free to discard. A finding that the policy team sits at the top would be overturned by evidence that no one at the decision consults the policy in real time and that appeals are ratified without being re-decided. The reliance on practitioner accounts is a limit: what a reviewer reports about where the decision sits may differ from where a full trace of the system's logs would place it, and closing that gap would require log access this study does not assume. The priors are in-silico baselines at one seed, and a field departure refines them; it does not validate the simulation.

## Literature review

Four conversations bear on this study, and reading them together locates what it can add.

*Studying the opaque algorithmic third.* The interpretation and enforcement that automated systems perform have become central to organization theory, which has mapped how such systems direct and evaluate the people who work through them while keeping their operations out of view (Kellogg, Valentine, & Christin, 2020). The methodological problem, that the algorithm cannot be watched deciding, has drawn the argument that ethnographers can study algorithms by comparing systems and triangulating the traces they leave in the practices of the people around them (Christin, 2020). Moderation is a hard case of this opacity, because the system acts on content at a scale and speed no observer can follow, and the people who run it see only what the system surfaces to them. The present study works around the opacity by asking the practitioners who sit beside the system what they take it to be doing and where they feel the decision is fixed, treating their folk theory of the system as data.

*The third party in social and organization theory.* A relationship among three differs in kind from a relationship between two, Simmel (1950) argued, and the third can take distinct positions, profiting from the other two's division, dividing them, or mediating between them. Work on brokerage kept the structural insight while turning to the third who connects parties (Obstfeld, 2005). The service-work literature carried the triadic frame into the workplace, analyzing the worker caught among an employer and a customer whose demands pull against each other (Bélanger & Edwards, 2013). Across these accounts the third is an addition to a relationship two parties could sustain without it. Moderation presents a third of a less familiar kind, an automated party that both parties must route through and that keeps a record neither fully sees, and the question of how a fourth party, the policy team above the third, changes the arrangement is the question the oversight prior poses and this study takes to the field.

*Coordination and articulation work.* How parties accomplish joint work through intermediaries, artifacts, and one another's records has been studied closely in the sociology of work and in computer-supported cooperative work. Strauss (1988) named the articulation work by which interdependent tasks are meshed into a functioning whole, the often invisible labor of arranging and aligning that makes visible production possible, and later work developed the analysis of such labor as routinely unrecognized (Star & Strauss, 1999). Suchman (1987) showed that a plan is a resource for situated action rather than a script that determines it, which bears directly on whether a moderation policy governs a decision or is reinterpreted at the moment of enforcement. The computer-supported cooperative work tradition extended the analysis to coordination through shared information spaces, where interdependent actors coordinate by way of a common artifact (Schmidt & Bannon, 1992). The moderation queue, the strike record, and the appeal log are such artifacts, and the study reads them as the medium through which the three parties coordinate.

*Content moderation.* A specific literature describes moderation as organized work. Gillespie (2018) argues that platforms are constituted by the moderation they perform, that the custodial work of deciding what stays up is central to what a platform is rather than incidental to it. Roberts (2019) documents the human labor behind automated-seeming systems, the commercial content moderators who review what the machine routes, often under conditions that hide their work from view. Gorwa, Binns, and Katzenbach (2020) analyze algorithmic moderation directly, mapping how automated tools classify and act on content and where human judgment remains in the loop, and they name the governance and accountability problems the automation raises. This literature establishes that moderation is a coordinated accomplishment of automated tools and human reviewers under a written policy, and it supplies the study's setting. What it has not done is read that coordination through the question of who holds the decision when the system keeps a record and a policy team sits above it, which is the opening the catalog priors define.

*The opening.* The four conversations leave a specific gap. Work on the opaque algorithmic third works around opacity but has not asked who holds a moderation decision among the three parties that settle it. Social theory on the third assumes two relatable parties and has not taken up the automated third that remembers. The coordination literature analyzes joint work through artifacts but has not measured how memory and oversight divide a takedown. The moderation literature describes the work but has not read it for the felt locus of the decision. This study enters that opening to find how a poster, an automated system, and a policy team coordinate a keep-or-remove decision, and where the lived arrangement departs from the priors that memory and oversight set.

## Exhibit A — Draft interview guide

*Opening (rapport, context)*

1. Walk me through what happens to a piece of content from the moment it is posted to the moment a decision is final. What are the steps, and who touches it?
2. How did you come to do this work? How did you learn to do it well?

*The automated system and what it does*

3. When the system flags something, what exactly has it done, and what is left for a person to do? Walk me through a recent case.
4. The system keeps a record on an account, a history, a score, a strike count. How does what it already knows about a poster change how a new post is handled?
5. Tell me about a time you agreed with what the system did, and a time you did not. What happened in each?

*Where the decision sits*

6. When a piece of content comes down, who decided it? Walk me through who actually made the call on a recent removal.
7. Some people might say the system decides and a person confirms. Others might say the person decides and the system advises. From your own experience, which is closer, and when?
8. Tell me about a time you overrode the system, and a time you felt you could not.

*The policy team and the rules*

9. When you apply a policy, where does that policy come from, and do the people who wrote it ever see how a given case turns out?
10. Walk me through an appeal. Who hears it, what do they look at, and how often does the outcome change?
11. Does the team that writes the rules and hears appeals feel like part of the decision as it happens, or like something that comes before and after it?

*The poster*

12. What can a poster do to affect how their case turns out? Does it matter whether they keep their own records, have a following, or know how to escalate?
13. Tell me about a poster who got a different outcome because of something they did or held onto.

*Contrast and closing*

14. How is moderating content for an account the system already has a history on different from moderating a brand-new account? What changes for you?
15. What do you wish people understood about how these decisions actually get made? Anything I should have asked but did not?

## References

Bélanger, J., & Edwards, P. (2013). The nature of front-line service work: Distinctive features and continuity in the employment relationship. *Work, Employment and Society, 27*(3), 433–450. https://doi.org/10.1177/0950017013481877

Christin, A. (2020). The ethnographer and the algorithm: Beyond the black box. *Theory and Society, 49*(5), 897–918. https://doi.org/10.1007/s11186-020-09411-3

Gillespie, T. (2018). *Custodians of the Internet: Platforms, content moderation, and the hidden decisions that shape social media*. Yale University Press.

Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. *Organizational Research Methods, 16*(1), 15–31. https://doi.org/10.1177/1094428112452151

Gorwa, R., Binns, R., & Katzenbach, C. (2020). Algorithmic content moderation: Technical and political challenges in the automation of platform governance. *Big Data & Society, 7*(1). https://doi.org/10.1177/2053951719897945

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. *Academy of Management Annals, 14*(1), 366–410. https://doi.org/10.5465/annals.2018.0174

Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic inquiry*. Sage.

Obstfeld, D. (2005). Social networks, the tertius iungens orientation, and involvement in innovation. *Administrative Science Quarterly, 50*(1), 100–130. https://doi.org/10.2189/asqu.2005.50.1.100

Pratt, M. G. (2009). For the lack of a boilerplate: Tips on writing up (and reviewing) qualitative research. *Academy of Management Journal, 52*(5), 856–862. https://doi.org/10.5465/amj.2009.44632557

Roberts, S. T. (2019). *Behind the screen: Content moderation in the shadows of social media*. Yale University Press.

Schmidt, K., & Bannon, L. (1992). Taking CSCW seriously: Supporting articulation work. *Computer Supported Cooperative Work (CSCW), 1*(1–2), 7–40. https://doi.org/10.1007/BF00752449

Simmel, G. (1950). *The sociology of Georg Simmel* (K. H. Wolff, Ed. & Trans.). Free Press.

Star, S. L., & Strauss, A. (1999). Layers of silence, arenas of voice: The ecology of visible and invisible work. *Computer Supported Cooperative Work (CSCW), 8*(1–2), 9–30. https://doi.org/10.1023/A:1008651105359

Strauss, A. (1988). The articulation of project work: An organizational process. *The Sociological Quarterly, 29*(2), 163–178. https://doi.org/10.1111/j.1533-8525.1988.tb01249.x

Suchman, L. A. (1987). *Plans and situated actions: The problem of human-machine communication*. Cambridge University Press.
