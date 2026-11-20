---
citekey: tang2025darkgui
title: Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight
authors: Tang, Jingyu; Chen, Chaoran; Li, Jiawen; Zhang, Zhiping; Guo, Bingcan; Khalilov, Ibrahim; Gebreegziabher, Simret A; Yao, Bingsheng; Wang, Dakuo; Ye, Yanfang; Li, Tianshi; Xiao, Ziang; Yao, Yaxing; Li, Toby Jia-Jun
year: 2025
doi: null
source_basis: full-text
pages_read: pp. 1-20 (the whole body, Abstract to Conclusion) and Appendices A-F (pp. 25-44) of 44 (printed page numbers, which agree with the page breaks); reference list (pp. 20-24) not read
local_path: ~/iit-playground/berthon_ethics_local/pdfs/nadella/N1/arx_darkpatterns/plain.txt
sha256: c7bc18479f57f8e03ce501dd3cfc74d7d46b4046027d4eab186920fd8875d7e3
verified: corrected
structure_sections: 4.2; 4.3; 4.4-stop; 4.4-record; 4.4-loss; 6-responsibilization; new-category
type: preprint
venue: arXiv 2509.10723v1 [cs.HC], 12 Sep 2025
source_url: https://arxiv.org/pdf/2509.10723
record_check: arxiv api export.arxiv.org id_list=2509.10723 returned the title and published date 2025-09-12 (checked 2026-11-18); authors read from the PDF; no DOI
facet: B3
supersedes: none
written: 2026-11-18
---

## Summary

Read in full: the body (pp. 1-20) and Appendices A-F (pp. 25-44); the reference list was not read. The authors run a two-phase study of 16 dark-pattern types, selected from Gray et al.'s taxonomy, on LLM-powered GUI agents, human participants and human-supervised agents; every task ran on a sample website the authors built, with one dark pattern embedded (pp. 6, 8). In Phase 1 the six agents often avoided a dark pattern without recognising it, and when they did recognise one they often left it in place if correcting it took extra steps (pp. 8-9). In Phase 2, with 22 participants, the text says that supervising the agent made participants less likely to fall for dark patterns in 14 of 16 tasks (p. 13); Table 3 shows higher avoidance in 10 tasks, the same 100% in 4 and lower avoidance in 2 (p. 12). Supervision also brought attentional tunneling, cognitive load and a diminished sense of control, and it reduced participants' awareness of dark patterns (p. 14). The Discussion names a "responsibility vacuum" and calls for automation boundaries, auditable confirmations and ex-ante assignment of liability with incident logging and redress (pp. 15-16). A further section asks for "AI safety literacy" education for end users, ethics education for designers and regulation that assigns liability ex-ante (p. 18). The dark patterns sit in the websites the agent visits for its user, not in the agent's own design, and the person at risk is the agent's user.

## Key facts it relies on

- Phase 1 "highlights that agents often fail to recognize dark patterns, and even when aware, prioritize task completion over protective action". [quote] (p. 1, Abstract)
- The study uses 16 dark-pattern types and a within-subjects design with 22 participants, recruited through social media and word of mouth. [paraphrase] (pp. 1, 10)
- Setting: "Each task used a unique website containing a single, embedded dark pattern." The authors built the sample websites, "modeled on the design styles of popular websites (e.g., Amazon, Instagram, YouTube)". [quote] (p. 8)
- Phase 1, Finding 1: "This paradox—avoidance without awareness—suggests that agents are not deliberately protecting users." [quote] (p. 8)
- Phase 1, Finding 2: "agents consistently privilege instructed goal completion over protective interventions, sidelining corrective actions whenever they impose additional effort". [quote] (p. 9)
- Phase 1, Finding 3: only the two end-to-end agents stopped to ask the user (Claude CUA before accepting terms of service; Operator also for account creation and location sharing), under "a safety policy designed to safeguard against potentially sensitive actions"; the four adapted LLM-based agents had no such safeguard. [paraphrase] (pp. 9-10)
- The oversight condition was simulated: participants "observed pre-recorded video of Operator completing the tasks"; letting playback run signalled approval and skipping signalled disagreement. [quote] (p. 11)
- Table 3: avoidance under oversight was higher than human-only in 10 of the 16 tasks, equal at 100.0% in 4 (Adding Steps, Choice Overload, Urgency, Shaming) and lower in 2 (Social Proof, 100.0% to 90.9%; Forced Registration, 40.0% to 25.0%). [paraphrase] (p. 12, Table 3; the tally is the Fable reader's)
- "in 14 of 16 tasks, participants were less likely to fall for dark patterns when supervising the agent". [quote] (p. 13)
- "This improvement stemmed from a conservative strategy: participants often terminated tasks when the agent's actions deviated from expectations". [quote] (p. 13)
- Oversight "does not simply eliminate vulnerabilities but shifting them into new forms of risk in human-agent systems". [quote] (p. 14)
- Under supervision 66% of answers to the awareness question were "No", against 59% when participants worked alone. [paraphrase] (p. 14)
- "Our findings caution strongly against the premature deployment of GUI agents in real-world workflows, particularly those are high-stake or involve sensitive information." [quote] (p. 15; "those are" is the source's)
- "there is a responsibility vacuum: without clear ex-ante assignment of liability and incident response, neither users, developers, nor deployers reliably own the consequences of unsafe actions". [quote] (p. 15)
- "High-stakes actions (e.g., personal-data disclosure, acceptance of legal terms) should remain under human control." [quote] (p. 15)
- Confirmations without transparency become "blind approvals"; systems should expose what was inspected, so approvals "are auditable". [paraphrase] (pp. 15-16)
- "Responsibility for unsafe outcomes must be defined ex-ante, specifying whether developers, deployers, or both bear liability. This should be supported by incident logging and redress procedures." [quote] (p. 16)
- "Without such frameworks, responsibility defaults to end users least able to manage the risk." [quote] (p. 16)
- Current consumer-protection and AI-safety regulations "focus on human deception, leaving little precedent for cases where the agent itself is manipulated". [quote] (p. 16)
- "Technical safeguards are therefore necessary but insufficient; without complementary ethics education and regulatory frameworks, unsafe behaviors will continue to be normalized and externalized onto users least able to contest them." [quote] (p. 18)
- For end users, AI safety literacy education "must also cultivate the ability to question agent outputs and to recognize when interface manipulations (e.g., hidden fees, deceptive defaults) demand human intervention". [quote] (p. 18)
- "Liability must be assigned ex-ante so that unsafe outcomes do not default to end users who are least able to contest them." The same paragraph proposes "mandatory flagging when manipulative defaults are auto-selected, hidden fees are introduced, or high-risk disclosures are triggered". [quote] (p. 18)
- "education builds awareness of risks, safeguards provide immediate protection, and regulation ensures that both are implemented consistently and accountably across the industry". [quote] (p. 18)
- The authors call for "regulatory frameworks that extend protections to agent-mediated contexts and address the current accountability gap". [quote] (p. 3)
- For three tasks (Forced Communication or Disclosure, Forced Registration, Hidden Information) avoiding the dark pattern meant skipping the task. [paraphrase] (pp. 34-36, Figs. 16, 18, 19)

## Critical notes

- Preprint. The arXiv record, re-fetched on 2026-11-19 with a generic client, still shows v1 only, with no journal reference and no DOI. Sample of 22 participants, which the authors call limited in size and demographic breadth (p. 19); watch mode only, and simulated by pre-recorded video (p. 11). The text reports no test of statistical significance for Table 3 (file searched for "significan", "statistic", "p <"); each participant did eight tasks in each condition (p. 10), so a task-condition cell holds about eleven people (22 x 8 / 16, the Fable reader's arithmetic). Agents tested include Operator and Claude's Computer Use, but the authors are university researchers, not the vendors, so the Anthropic-authored caveat does not apply; the text carries no funding or acknowledgements statement.
- The text's "14 of 16" and its Table 3 agree only if ties count: avoidance rose in 10 tasks, stood at 100% in both conditions in 4 and fell in 2 (p. 12). The authors put the gain down to participants terminating tasks (p. 13), and for three tasks skipping was the scored way to avoid the pattern (pp. 34-36).
- Scope: GUI agents acting for a user on websites that carry dark patterns; the websites were the authors' own test sites (p. 8). The person at risk is the agent's user, who delegates the task. The study has no third party on whom a firm's agent acts, and it does not ask whether a deploying firm's own agent steers the person it deals with. "Deployers" appears twice and is not defined (pp. 15, 16).
- The sentences on responsibility defaulting to end users (pp. 16, 18) are implications the authors draw in the Discussion, not tested results; the study measured avoidance, awareness and perceptions, and no loss or liability.
- On literacy the source goes both ways. It calls technical safeguards "necessary but insufficient" and wants liability assigned ex-ante (pp. 16, 18). It also prescribes AI safety literacy education that trains end users to question agent outputs (p. 18), and its Conclusion calls for raising "the awareness of risks in using GUI agents" (p. 20). The same text reports that supervising the agent reduced participants' awareness of dark patterns (pp. 11, 14).
- Other limits the authors name (p. 19): static sites with one dark pattern each; each pattern tested in one domain; post-task interviews open to recall bias; agents' reasoning traces "may not faithfully capture the causal process of decision-making and can instead serve as post-hoc rationalizations"; agents that are frequently updated.
- Bearing: supports on liability (pp. 16, 18) and contests in part (it prescribes user literacy education, p. 18). The person in question is the agent's user, not a third party. That user gets: record partial (auditable confirmations and incident logging proposed, pp. 15-16); brake partial (automation boundaries proposed, p. 15; existing confirmations and takeover modes called insufficient, p. 15; oversight tested and found limited, pp. 13-14); envelope partial (high-stakes actions under human control, p. 15); standing no (redress procedures are named, p. 16, with no route to contest described); loss cover partial (ex-ante liability and redress proposed, pp. 16, 18). All as recommendations, not as existing practice. STRUCTURE 4.2, 4.3-4.4 and 6-responsibilization.
- Corrected at the Fable read (V-B-2, second sitting): (1) the Summary said oversight "improved avoidance in 14 of 16 tasks"; that is the text's sentence (p. 13), and Table 3 (p. 12) shows 10 higher, 4 equal and 2 lower, now reported beside it. (2) Section 5.4 (p. 18), outside the pages first read, prescribes AI safety literacy education for end users; the Summary, four facts, a note and the Bearing line now carry it, and `4.2` is added to `structure_sections`. (3) "The interfaces are third-party web pages" replaced: they are the authors' sample websites (p. 8), and the oversight condition used pre-recorded video (p. 11). (4) The scope note now says who the person at risk is. (5) The note that began "Source for the paper's point" spoke about the paper; rewritten as a statement about the source. (6) `source_basis` raised to full-text and `pages_read` restated, because the whole body and the appendices were read. (7) Sixteen facts added (pp. 8, 8, 9, 9-10, 11, 12, 13, 14, 15, 15, 16, 18, 18, 18, 18, 34-36). The seven original quotations are unchanged.
