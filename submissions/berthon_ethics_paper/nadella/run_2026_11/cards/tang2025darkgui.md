---
citekey: tang2025darkgui
title: Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight
authors: Tang, Jingyu; Chen, Chaoran; Li, Jiawen; Zhang, Zhiping; Guo, Bingcan; Khalilov, Ibrahim; Gebreegziabher, Simret A; Yao, Bingsheng; Wang, Dakuo; Ye, Yanfang; Li, Tianshi; Xiao, Ziang; Yao, Yaxing; Li, Toby Jia-Jun
year: 2025
doi: null
source_basis: partial-text
pages_read: pp. 1, 3, 10, 13-16 and 19 of 44 (arXiv PDF pagination by page break); other pages searched by keyword
local_path: ~/iit-playground/berthon_ethics_local/pdfs/nadella/N1/arx_darkpatterns/plain.txt
sha256: c7bc18479f57f8e03ce501dd3cfc74d7d46b4046027d4eab186920fd8875d7e3
verified: pending
structure_sections: 4.3; 4.4-stop; 4.4-record; 4.4-loss; 6-responsibilization; new-category
type: preprint
venue: arXiv 2509.10723v1 [cs.HC], 12 Sep 2025
source_url: https://arxiv.org/pdf/2509.10723
record_check: arxiv api export.arxiv.org id_list=2509.10723 returned the title and published date 2025-09-12 (checked 2026-11-18); authors read from the PDF; no DOI
facet: B3
supersedes: none
written: 2026-11-18
---

## Summary

Read: pp. 1, 3, 10, 13-16 and 19; other pages searched by keyword. The authors run a two-phase study of 16 dark-pattern types (selected from Gray et al.'s taxonomy) on LLM-powered GUI agents, human participants and human-supervised agents. In Phase 1 agents often fail to recognise dark patterns and, even when aware, put task completion ahead of protective action. In Phase 2, with 22 participants, human oversight improved avoidance in 14 of 16 tasks but brought attentional tunneling, cognitive load and loss of control. The discussion names a "responsibility vacuum" and calls for automation boundaries, auditable confirmations and ex-ante assignment of liability with incident logging and redress. This extends the dark-patterns concept to agents that act for the user on interfaces, not to conversational AI; the interfaces are third-party web pages, not the agent's own design.

## Key facts it relies on

- Phase 1 "highlights that agents often fail to recognize dark patterns, and even when aware, prioritize task completion over protective action". [quote] (p. 1, Abstract)
- The study uses 16 dark-pattern types and a within-subjects design with 22 participants, recruited through social media and word of mouth. [paraphrase] (pp. 1, 10)
- "in 14 of 16 tasks, participants were less likely to fall for dark patterns when supervising the agent". [quote] (p. 13)
- Oversight "does not simply eliminate vulnerabilities but shifting them into new forms of risk in human-agent systems". [quote] (p. 14)
- "there is a responsibility vacuum: without clear ex-ante assignment of liability and incident response, neither users, developers, nor deployers reliably own the consequences of unsafe actions". [quote] (p. 15)
- Confirmations without transparency become "blind approvals"; systems should expose what was inspected, so approvals "are auditable". [paraphrase] (pp. 15-16)
- "Without such frameworks, responsibility defaults to end users least able to manage the risk." [quote] (p. 16)
- Current consumer-protection and AI-safety regulations "focus on human deception, leaving little precedent for cases where the agent itself is manipulated". [quote] (p. 16)
- The authors call for "regulatory frameworks that extend protections to agent-mediated contexts and address the current accountability gap". [quote] (p. 3)

## Critical notes

- Preprint, not peer reviewed on the evidence in hand. Sample of 22 participants, which the authors call limited in size and demographic breadth (p. 19); watch mode only; agents tested include Operator and Claude's Computer Use, but the authors are university researchers, not the vendors, so the Anthropic-authored caveat does not apply.
- Scope is GUI agents facing third-party interfaces, not conversational AI and not an agent's own dark design. The paper does not ask whether a deploying firm's own agent steers the user.
- Source for the paper's point that, without an assigned liability, responsibility falls on the person least able to bear it (p. 16); this is a statement of a design implication from the study, not a tested result.
- Bearing: supports. Person acted on gets: record partial (audit trails proposed, p. 16); brake partial (automation boundaries proposed, p. 15; human oversight tested and found limited, pp. 13-14); envelope partial (high-stakes actions under human control, p. 15); standing no; loss cover partial (ex-ante liability and redress proposed, p. 16). All as recommendations, not as existing practice. STRUCTURE 4.3-4.4 and 6-responsibilization.
