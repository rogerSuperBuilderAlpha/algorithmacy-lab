# GAP_CHECK — claim c9 (S9, run dxda-lib-2026-11)

> [Built by Claude (opus subagent), 2026-11-05, stage S9.]

**Claim c9 (README):** no prior work frames LLM interfaces as animation for decision design (OUTLINE §6).

Following `triage/G.md`, I split c9 into two halves. **(A)** reads an LLM interface as an animation; **(B)**
draws from that reading a design method that surfaces a user's decisions in the missing frames. A work
pre-empts c9 only if it does both. Everything said below about a carded work comes from its card in
`cards/`. Everything said about an uncarded search hit comes from the search result alone, as the result
printed it.

## Part 1. The nearest priors in the library

| work (card) | depth | (A) | (B) | what it does | what it does not do |
|---|---|---|---|---|---|
| L. Stark 2024 (`stark2024animation`) | full | **Yes** | No | Argues "ChatGPT and similar chatbots… can be best understood as animated characters" (p. 1663), on Silvio's definition (p. 1664); says the frame "lays ground for a new framework to conceptualize the design and regulation of interactive AI systems" (p. 1663). | "he develops only the regulation side. Nothing here concerns decisions or decision design." His §4 is consumer protection, disclosure and "AI iconoclasm," which asks "whether design measures intended to encourage the projection of human attributes onto an AI system might be deemed unethical" (p. 1669). No frames, no apparent motion, no method. |
| Maeda & L. Stark 2025 (`maeda2025anthropomorphism`) | full | **Yes, extended** | No (governance) | A "network of distributed human agents… collectively 'animate'" anthropomorphic features (p. 1661), sorted into primary agents, secondary agents and mediators (p. 1663); the response is "distributed governance" (p. 1661). | "They treat no decisions and offer no interface craft." Their direction cuts against c8: "technical guardrails are needed to prevent excessive animation in high-risk contexts" (p. 1670); "the best course of action may be to eschew anthropomorphic AI altogether" (p. 1670). Stark is second author, so it is not independent of Stark 2024. |
| Jones 2026 (`jones2026animating`) | full | **Yes** (voice) | No | Calls AI chatbots "technologies of 'animation'" (p. 52), joining Silvio with Blommaert's enoughness; users "'fill in the blanks'" (p. 41); designers "should also consider what kinds of characterological figures are invoked by the voice interface" (p. 52). | Voice interfaces and social identity (accent, stance), not text LLM interfaces and not decisions. Not fully independent of Stark: "Luke Stark (2023) makes the same argument about LLMs" (p. 42), citing the Daily Nous blog post. |
| Silvio 2010 (`silvio2010animation`) | abs | No | No | Proposes animation "as a trope for human action on/in the world" and "a general animation model" (abstract). | Pre-LLM; no interface, no decisions. Every page locus the paper uses reaches the lab through Stark. |
| Silvio 2019 (`silvio2019puppets`) | meta | unread | unread | Record only (University of Hawaii Press). | The card cannot say. The p. 52 definition is quoted only through Stark (p. 1664). |
| Abercrombie et al. 2023 (`abercrombie2023mirages`) | full | No | Design, not decisions | Argues "against gratuitous anthropomorphic features" (p. 4777); notes "ChatGPT's animated 'three dots' and word-by-word staggered outputs, which give an impression that the system is thinking" (p. 4778). | "It has no theory of animation and uses 'animated' once, for the three dots in ChatGPT." Its design stance, per the card, is to choose cues by context rather than remove them all (p. 4783). No decisions. |
| Tan et al. 2026 (`tan2026impact`) | full | No | Design variable, not decision method | Treats time-to-first-token as "a tunable design variable with ethical implications" (abstract); 31% of noticing participants read the wait as the AI "'thinking'" (§4.5). | No animation frame; one wait before streaming, pace fixed after the first token; no effect on behaviour, trust or workload; warns that slowing a reply "sits uneasily between positive friction and potential deception" (§5.5). |
| Shi et al. 2026 (`shi2026siren`) | part | No | Dark patterns in dialogue | Defines LLM dark patterns as "manipulative or deceptive behaviors enacted in dialogue" (abstract); participants recognised 310 of 374 (§5). | No animation frame and no moving goal; participants "evaluated pre-selected outputs rather than relying on an LLM for real decisions" (p. 18); authorship "diffuse" (p. 5). |

The G facet adds three more cards.

- **Shanahan et al. 2023** (`shanahan2023role`, full) is the rival frame: role play, not animation. The
  simulator "'has no agency of its own'" (p. 496), and the work has no design programme for decisions.
- **Siskind et al. 2024** (`siskind2024would`, full) makes c8's structural move with another craft: magic's
  principles applied to chatbot conversation. The aim runs the other way — concealment ("The user hopefully
  overestimates Haru's abilities," §4.4) and "forcing" decisions "while giving the illusion of free choice"
  (§4.8) — and the test system is a scripted social robot, not an LLM.
- **Cameron et al. 2024** (`cameron2024social`, full) frames a robot as a depicted character with an unseen
  authority behind it, following Clark and Fischer, who compare robots to "ventriloquist dummies or puppets"
  (pp. 1406–1407). It concerns trust in HRI, not LLMs, animation or decisions. The card names Clark and Fischer
  (BBS; cited as 2022 in Cameron, 2023 in Abercrombie) as the work to check next for the depicted-character
  move. It is not carded.

`gonzalez1996does` (meta) shares the words "animation" and "decision" — moving imagery in a decision-support
interface before LLMs — and the card keeps that sense apart from the character sense. Triage also reserved
So et al. 2026, Maeda & Quan-Haase 2024, Hau 2026, Bernini 2025 and Keane 2026 at abstract depth
(`triage/G.md`); none is carded.

**In short, the library holds (A) three times and (B) never.** Stark, Maeda & L. Stark and Jones each read the
chatbot as an animated character. Their consequences stop at critique, governance and the sociolinguistics of
voice. Siskind et al. make (B)'s move in form, borrowing a craft for conversation design, but without
animation and toward concealment.

## Part 2. The fresh check (2026-11-05)

### Maeda & Buening 2026, opened as DECISIONS required

DECISIONS ("G — approved") asks S9 to open the abstract of Maeda & Buening 2026 before this file closes. I
fetched both records on 2026-11-05 and saved them as `crossref_maeda_buening.json` and
`openalex_maeda_buening.json` in this session's scratchpad, outside the repo. Crossref gives: "Safety Theater in
Anthropomorphic AI: Why We Need to Shift from Safety to Accountability Narratives"; Takuya Maeda, Rebecca
Buening; *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency*; 2026-06-25;
pp. 2225–2252; DOI 10.1145/3805689.3812282; no abstract. OpenAlex (W7166522104) carries the abstract. On the
abstract alone, the authors compare "AI safety" with "AI accountability" narratives, call anthropomorphic
features "both social cues that instigate parasocial dynamics and engagement capture mechanisms," and propose
"accountability interventions that constrain extraction incentives through external monitoring and power
redistribution." The abstract does not use the word "animation" and says nothing about decisions or interface
craft. **It does not pre-empt c9.** It is not carded and not in the registry.

### Search log

Consensus: six calls, query only, no filters (default page size 20). WebSearch: three calls, standard mode.
"Carded?" checks `cards/`; "registry" means `~/iit-playground/dxd_animation_local/registry.tsv`, searched by
title and DOI on 2026-11-05.

| # | date | tool | query | n | top hits (as the result gave them) |
|---|---|---|---|---|---|
| 1 | 2026-11-05 | Consensus | `LLM chatbot as animation or animated character` | 20 | [1] Stark 2024, "Animation and Artificial Intelligence" (carded); [2] Normoyle, Sedoc & Durupinar 2024, "Using LLMs to Animate Interactive Story Characters with Emotions and Personality"; [4] Sonlu et al. 2025, "Effects of Embodiment and Personality in LLM-Based Conversational Agents"; [5] Qin et al. 2024, "CharacterMeet". The rest are avatar, gesture and role-play systems. |
| 2 | 2026-11-05 | Consensus | `animation theory applied to AI interface design` | 20 | [1] Kurian 2025, "Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney"; [2] Stark 2024 (carded); [6] Wu & Masson 2026, "AInimation: Animating from Prompt to AI-Generated Responses"; [8] Schulz, Tørresen & Herstad 2018, "Animation Techniques in Human-Robot Interaction User Studies"; [9] Takayama, Dooley & Ju 2011, "Expressing thought: Improving robot readability with animation principles"; [15] Dehn & van Mulken 2000 (F9 reserve). |
| 3 | 2026-11-05 | Consensus | `Silvio animation artificial intelligence` | 20 | [3] Stark 2024 (carded). No Teri Silvio work returned; [1] is about Silvio Ceccato, a homonym. The rest concern AI in animation production. |
| 4 | 2026-11-05 | Consensus | `decision support interface animation large language model streaming output user decisions` | 19 | [1] Handler, Larsen & Hackathorn 2024, "Large language models present new questions for decision support"; [3] Lawless et al. 2023, "'I Want It That Way'"; [8] Lin et al. 2023, "Decision-Oriented Dialogue for Human-AI Collaboration"; [14] Pang et al. 2025, "Interactive Reasoning"; [18] González & Kasper 1997, "Animation in User Interfaces Designed for Decision Support Systems" (F9 reserve R4). None reads the interface as animation. |
| 5 | 2026-11-05 | Consensus | `animator principles for designing conversational AI interfaces timing staging` | 20 | [2] Wu & Masson 2026, "AInimation" (again); [3] Chen & He 2025, "Integrating Waiting into the Experience: A Study on Visual Feedback Design for AI Doctor Agents"; [6] Jones 2026 (carded); [11] Kurian 2025 (again); [18] Klowait & Erofeeva 2025, "Nonhuman situational enmeshments—How participants build temporal infrastructures for ChatGPT". |
| 6 | 2026-11-05 | Consensus | `chatbot puppet animator character triad user platform opacity design` | 20 | [11] So, Cheng & Krishna Murthy 2026, "Beyond Anthropomorphism: a Spectrum of Interface Metaphors for LLMs" (G reserve R1); [14] Stark 2024 (carded); [18] Maeda & Quan-Haase 2024 (G reserve R2); [20] Yun, Taranova & Wang 2026, "Does My Chatbot Have an Agenda?". The rest are anthropomorphism experiments. |
| 7 | 2026-11-05 | WebSearch | `LLM interface as animation "missing frames" decision design` | 10 | No scholarly hit on the phrase. Nearest: the TDL repository record "Animation in user interface design for decision making: a research framework and empirical analysis" (González's line, pre-LLM); Keyframer (Tseng et al.); a design blog. |
| 8 | 2026-11-05 | WebSearch | `Teri Silvio animation chatbot generative AI interface design decision-making` | 10 | No Silvio hit. Stock images and vendor pages; one arXiv survey of generative-AI UI techniques (arXiv 2410.22370). |
| 9 | 2026-11-05 | WebSearch | `"animation" "large language model" chatbot animated character design implications Stark Silvio 2025 2026` | 10 | No Stark or Silvio hit. LLM text-animation tools, patents for AI characters, a Frontiers paper on animation-scene design. |
| — | 2026-11-05 | Crossref + OpenAlex | DOI `10.1145/3805689.3812282` | 1 | Maeda & Buening 2026, above. |

Earlier searches this run, not repeated: `tools/search.py G` (OpenAlex 25, Crossref 20, arXiv 10 per query;
Semantic Scholar 429 on all five), two Consensus queries of 50, OpenAlex snowballs of the 19 works citing
Stark 2024 and the 2 citing Maeda & L. Stark 2025, two OpenAlex title-and-abstract filters, and the prior DXD
term search (`triage/G.md`, "Sources searched").

### Hits that might bear on c9

I record each as the search result gave it and say no more about its argument than the result shows.

| hit (as given) | why it might bear on c9 | carded? |
|---|---|---|
| Jia-Qi Wu and Damien Masson, 2026-07-20, "AInimation: Animating from Prompt to AI-Generated Responses," ArXiv, DOI 10.48550/arxiv.2607.18507 (preprint) | The closest to (B) in this check. The abstract describes "animated transitions between a prompt and an AI-generated response," a taxonomy from 800 examples, and a study in which transitions helped users "review the response" (43% better at locating elements, 153% better at identifying changes, 20% better at verifying the prompt was interpreted), concluding that "well-crafted, slower animations are preferable to instant AI responses." It is interface animation for reviewing LLM output. The abstract does not read the LLM as an animated character, does not cite animation theory and does not name decisions. | **No.** Not in the registry. It appears in `search/F9.jsonl` (OpenAlex rank 17, W7170082640) but was not triaged. |
| Nomisha Kurian, 2025-04-11, "Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney," Int. J. Child Comput. Interact., DOI 10.1016/j.ijcci.2025.100788 | Transfers design patterns from "52 works of animation" into child-centred AI design as a "design grammar" (abstract): a craft-to-AI transfer like c8. The abstract names children's understanding and learning, not decisions, and does not say the AI interface is an animation. | **No.** Not in the registry. |
| Chien-Hsiung Chen and Jiwei He, 2025-07-10, "Integrating Waiting into the Experience: A Study on Visual Feedback Design for AI Doctor Agents," International Journal of Human–Computer Interaction, DOI 10.1080/10447318.2025.2527847 | A c5 neighbour: "animated delays signaled 'thinking'" and gradual versus instant content changed pleasure and arousal (abstract, n = 60). No animation-theory frame and no decision design in the abstract. | **No.** |
| Takuya Maeda and Rebecca Buening, 2026, "Safety Theater in Anthropomorphic AI…," FAccT '26, DOI 10.1145/3805689.3812282 | Same first author as the closest prior. Governance, not animation or decisions (above). | **No.** |

The other hits are F9 or F3 territory the library already holds in reserve (González & Kasper 1997, So et al.
2026, Maeda & Quan-Haase 2024, Dehn & van Mulken 2000) or HRI work on animation principles for robots
(Takayama et al. 2011; Schulz et al. 2018), which bear on c8's transfer of principles, not on c9.

## Verdict: c9 is open, but narrowed

**I found no work that frames an LLM interface as an animation and draws from that frame a design method for
surfacing a user's decisions,** in the eight cards above, the G triage sources, six Consensus queries, three web
searches and the Maeda & Buening record. The Semantic Scholar leg of the earlier API search failed (429), so
the verdict holds for these sources only, and most of this check rests on abstracts.

c9 is **narrowed** on three sides:

1. **(A) is taken.** L. Stark (2024) states it, Maeda & L. Stark (2025) extend it to a network of animators,
   and Jones (2026) applies Silvio to voice interfaces. §6 must not claim the animation reading.
2. **Interface animation for LLM output is taken in part.** Wu & Masson (2026) animate the transition from
   prompt to response and measure review. Their abstract stops short of decisions and of the character
   reading, but a reviewer will raise it. Card it before §6 is drafted.
3. **A triadic, depicted-character frame exists outside LLMs.** Cameron et al. (2024), via Clark and Fischer,
   give HRI a character–audience–authority triad. Ruling 4 holds that it is not a real triad; the paper must
   still cite it.

**How §6 should word it** [suggested wording, Claude's, for the author to keep, rewrite or reject]:

> "L. Stark (2024) and Maeda and L. Stark (2025) read LLM chatbots as animated characters and answer with
> regulation and distributed governance; Jones (2026) carries the reading to voice interfaces. Interface
> research animates LLM output to help users review it (Wu & Masson, 2026). I found no work that takes the
> animation reading as a design method for the user's decision — one that works in the missing frames to
> surface where a decision is being made. That is the move this paper proposes."

Three guards for that sentence. It should say "I found no work… in [sources]," not "no prior work." It should
not count Jones or Maeda & L. Stark as independent of Stark. And it should set DXD against Maeda & L. Stark's
"prevent excessive animation," since both Stark papers treat more animation as the harm and DXD proposes
better animation.

## For the author

- Card `wu2026ainimation` (preprint, open arXiv) before §6 and §5 are drafted; it bears on c8 as much as c9.
- Consider carding Clark and Fischer (BBS) on the depicted-character triad; Cameron's card names it, and two
  cards give it two different years.
- Kurian (2025) is a candidate F9 card for craft-to-AI transfer; Chen & He (2025) a candidate F4 card.
