# Search notes: is there a peer-reviewed treatment of a client-side personal agent negotiating with a platform's agent on a user's behalf? (2026-09-18)

Not a literature card. A record of the search the Principle I brief asked for, so the next pass does not repeat it.

## Method

Web search was unavailable this session (budget exhausted before this cluster began). Two academic search tools were used instead: the Scholar Gateway semantic index (query: peer-reviewed work on personal AI agents or LLM-based user agents that negotiate or bargain with a platform's algorithm or agents on behalf of an individual user, 2019–), and Consensus (220M-paper index; query: LLM personal agent negotiating on behalf of user with platform agents, delegation). Twenty Consensus results and fifteen Scholar Gateway passages were inspected by title, venue and abstract. None was read in full; none is carded.

## Finding

The client-side counter-agent literature exists as *preprints* and *workshop papers*, not as peer-reviewed treatments, and the peer-reviewed items nearest to it are on the platform's or seller's side.

Preprints and workshop items that are on point (all arXiv unless noted; none opened beyond the abstract):
- Zhu, S., et al. (2025). The automated but risky game: Modeling agent-to-agent negotiations and transactions in consumer markets. arXiv:2506.00073. "a future setting where both consumers and merchants authorize AI agents to automate the negotiations and transactions"; finds "an inherently imbalanced game" between agents of different capability. The closest match to Principle I's setting; a preprint.
- Lin, J., et al. (2026). LLM agents enable user-governed personalization beyond platform boundaries. arXiv:2605.09794. Argues "a shift from platform-centric personalization to user-governed personalization" with an off-the-shelf agent over cross-platform exports; proof-of-concept only.
- Liu, D. (2026). SovereignNegotiation-Bench: Evaluating user-owned personal agents in delegated bargaining under privacy, consent, evidence, and institutional pressure. arXiv:2607.02814. A benchmark for "user-owned agent[s]" that "appeal[] platform decisions, escalat[e] support disputes"; the only item whose framing is a personal agent contesting a platform, and it is a benchmark preprint.
- Zhu, K., et al. (2026). Choose your agent: Tradeoffs in adopting AI advisors, coaches, and delegates in multi-party negotiation. arXiv:2602.12089. Behavioural experiment (N = 243); delegation raises surplus but is disliked; human–human bargaining, no platform.
- Bansal, G., et al. (2025). Magentic Marketplace. arXiv:2510.25779. Simulated two-sided market of "Assistant agents [that] represent consumers and Service agents [that] represent competing businesses"; Microsoft Research preprint.
- Lorenzoni, G., et al. (2026). LLM-X: A scalable negotiation-oriented exchange for communication among personal LLM agents. *Proceedings of the 2026 International Workshop on Agentic Engineering*, doi:10.1145/3786167.3788429. Workshop; agent-to-agent among personal agents, no platform counterpart.

Peer-reviewed items found, and why they are adjacent rather than on point:
- Vahidov, R., et al. (2025). Using negotiation and large language models in human-to-software agent negotiations. *International Journal of Human–Computer Interaction*, doi:10.1080/10447318.2025.2502981. The agent negotiates *for the seller* against human buyers; the mirror image of Principle I.
- Kong, D., et al. (2025). FishBargain. *Companion Proceedings of the ACM Web Conference 2025*, doi:10.1145/3701716.3715176. A bargaining agent for *sellers* on a flea-market platform, deployed at scale; again the platform-adjacent side.
- Lee, C. P., et al. (2025). MAP: Multi-user personalization with collaborative LLM-powered agents. *CHI EA '25*, doi:10.1145/3706599.3719853. Multi-user conflict resolution by agents; no platform counterpart.
- Mouri Zadeh Khaki, A., et al. (2026). Evaluating fairness in LLM negotiator agents. *Mathematics* 14(3), doi:10.3390/math14030458. Buyer–seller LLM games; bias, not parity.
- Chan, A., et al. (2023), FAccT — carded (chan2023.md): about the operator's agent and its harms; no user-side agent.
- Scholar Gateway surfaced "Designing ethical online dispute resolution systems: The rise of the fourth party" and "The promise and peril of automated negotiators" (venues not captured); both are about a neutral or platform-side automated party, on the titles and passages shown, and neither was pursued.

## Verdict for the memo

There is no peer-reviewed paper, as of this search, that studies a personal agent acting for one party against a platform's own agent inside a live coordination. The idea is present in 2025–2026 preprints (Zhu et al. 2025; Liu 2026; Lin et al. 2026), one of which (Liu 2026) frames "appealing platform decisions" as the agent's task — which is Principle I's "contest what it commits" in benchmark form. The peer-reviewed technical ground for the *mechanism* is the automated-negotiation literature (jennings2001.md); the peer-reviewed policy ground is middleware (fukuyama2021.md; keller2021.md); the peer-reviewed empirical ground is thin to absent. The paper should say so and cite the preprints as preprints.

## What to read next

Zhu et al. (2025) and Liu (2026) in full, to see whether either models the platform's agent as pursuing an objective neither party set; and the *Group Decision and Negotiation* and AAMAS literatures on "negotiation with a mediator" for a peer-reviewed formalisation of the three-party case.
