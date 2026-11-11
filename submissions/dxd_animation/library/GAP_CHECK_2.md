[Built by Claude (Opus 5.5 subagent), 2026-11-11, run dxda-lib-2026-11b, stage S9 gap check G2.]

# GAP_CHECK_2 — claim m7

## Claim tested

Claim m7 says the DXD model does three things at once: (a) it reads the LLM or agent interface as an animation,
after L. Stark (2024); (b) it names the competencies a person needs to decide through an opaque, binding,
adaptive intermediary (algorithmacy; idempotent interpretation, intent specification, intuitive governance
tracking); and (c) it uses those competencies to select professional animation techniques (staging, key poses
and in-betweens, timing charts, anticipation, placing a change between moves) as testable propositions. A work
pre-empts m7 only if it does (c) through something like (b). I logged a hit as close if it did two of (a)–(c),
or if it turned animation craft into a design method for AI or agent interfaces.

I read `GAP_CHECK.md` (run 1) first and did not repeat its queries. Every reference below comes from a record
I opened this run; "full" means I read the full text, "abstract" means abstract or excerpt only.

## Sources and queries

All queries ran on 2026-11-11. Consensus used no filters and the default page of 20.

| # | source | exact query | n | top relevant hits (ids as given) |
|---|---|---|---|---|
| C1 | Consensus | `applying traditional animation principles to the design of conversational agent and large language model interfaces` | 20 | So, Cheng & Murthy 2026, 10.1145/3772363.3798591; Stark 2024; Jones 2026; Wu & Masson 2026, 10.48550/arxiv.2607.18507; Xiao et al. 2025, 10.18653/v1/2025.emnlp-main.164 |
| C2 | Consensus | `animation principles staging timing anticipation in decision support interface design` | 20 | González & Kasper 1995, 1997; González 1996; Chang & Ungar 1993; Thomas & Calder 2001; Clanton & Young 1994; Liddle 2016, 10.1145/2987592.2987614. All pre-LLM. |
| C3 | Consensus | `illusion of life principles applied to AI agent interface design` | 20 | Curtis et al. 2022, 10.1145/3561975.3562941; Lupetti & Murray-Rust 2024, 10.1145/3613904.3641954; Bernini 2025, 10.5325/style.59.3.0466; Schulz et al. 2019 |
| C4 | Consensus | `puppetry or animation craft as a design method for AI agents and chatbots` | 20 | Lewis et al. 2026, 10.48550/arxiv.2607.03289; Weir, Leonards & Roudaut 2026, 10.1145/3800645.3812869; **Pinhanez 2017, 10.5220/0006487500270038**; Kurian 2025; Hau 2026, 10.1080/15358593.2026.2619407 |
| C5 | Consensus | `user competencies for navigating opaque algorithmic intermediaries and implications for interface design algorithmic literacy` | 20 | Oeldorf-Hirsch & Neubaum 2023; Long & Magerko 2020; König 2022; DeVito 2021, 10.1145/3476080. No animation. |
| C6 | Consensus | `animation techniques to make AI agent actions and state changes legible to users keyframes timing` | 20 | Wu & Masson 2026; Zhou et al. 2017, 10.1145/2909824.3020221; Takayama et al. 2011; Sengers 1998, 10.1145/280765.280770; **Zhang & Davis 2026, 10.1145/3830398.3830586** |
| C7 | Consensus | `deriving interface design techniques from the competencies users need to coordinate through opaque AI agents or algorithmic platforms` | 20 | Pierce et al. 2026, 10.48550/arxiv.2606.09848; Andru & Saksena 2026; Feng et al. 2025, 10.48550/arxiv.2512.00742; Liu & Almeda 2025. No animation. |
| C8 | Consensus | `performance or animation frame as a critical competency for engaging with chatbots and AI literacy` | 20 | Hau 2026; Gupta et al. 2024 (Open Praxis); Stark 2024; Jones 2026. Rest: AI-literacy scales. |
| SG1–3 | Scholar Gateway | three natural-language questions on animation principles for LLM/agent interfaces | — | **Failed:** `ACCESS_DENIED` on all three calls (two at start, one retry at end). |
| O1–3 | OpenAlex | `search=animation principles large language model` (from 2022); `title_and_abstract.search:"animation principles" AND (chatbot OR "conversational agent" OR "AI agent")`; same with `"principles of animation" OR "cartoon animation"` × `LLM OR generative OR chatbot` | — | **Failed:** HTTP 429, unkeyed daily budget used up (a key needs the user's email, which I did not send). Snowballs moved to OC1–2. |
| S1–3 | Semantic Scholar | `animation principles large language model interface`; `animation principles conversational agent chatbot design`; `animation principles chatbot interface design` | — | **Failed:** 429 on all 11 attempts, with backoff. |
| CR1–4 | Crossref (OpenAlex stand-in) | `query.bibliographic=` `animation principles large language model interface`; `animation principles chatbot conversational agent design`; `cartoon animation techniques AI agent user interface`; `animation decision making generative AI interface design` (from 2022, 25 rows) | ~1–2 M each | Unranked token matches; nothing relevant in the top 25 of any. |
| OC1 | OpenCitations v2 | works citing Chang & Ungar 1993 (10.1145/168642.168647) | 107; 11 from 2022 | All 11 resolved via Crossref; none concerns LLMs, chatbots, agents or decisions. |
| OC2 | OpenCitations v2 | works citing Thomas & Calder 2001 (10.1145/502907.502909) | 37; 6 from 2022 | One touches AI: "Enhancing engagement … by animated prompts in AI-assisted drawing" (older adults), 2026, 10.1007/s10209-025-01285-5 (title only). OpenCitations coverage is partial. |
| A1–10 | arXiv API | `abs:"animation principles" AND (LLM OR "language model" OR agent OR chatbot)`; `("principles of animation" OR "animation techniques") AND (AI OR agent)`; `animation AND "large language model" AND interface AND user`; `keyframing AND (LLM OR "language model")`; `animation AND decision AND (LLM OR agent) AND interface`; `"animated transitions" AND (LLM OR AI OR generative)`; `Disney AND (LLM OR chatbot OR "AI agent" OR "conversational agent")`; `ti:"narrative keyframing"`; `"intent specification" AND (LLM OR "language model" OR agent)`; `"idempotent interpretation"` | 0; 1; 5; 213; 0; 8; 1; 1; 40; 2 | A6: Wu & Masson 2026. A8: Zhang & Davis 2026 (arXiv 2608.10337). A9: **Vaithilingam et al. 2025, arXiv 2504.09283**. A1 and A5 returned nothing. A4 is video keyframe selection. |
| Z1–3 | Zenodo API | `Disney principles animation AI architecture`; `creators.name:Reddy AND animation`; `"Govind Reddy"` | 433,579; 2; 44 | Govind Reddy 2026, 10.5281/zenodo.18859162; Sloan, Martinez & Scott-Brown 2012, 10.5281/zenodo.811678. |
| W1 | WebSearch | `"animation principles" "AI agent" UX interface design` | 10 | Microsoft "UX design for agents"; Atlassian Rovo motion page (fetched, below); agent "animation principles" skills. |
| W2 | WebSearch | `"Decision Experience Design"` | 19 | No use as a named framework. |
| W3 | WebSearch | `"algorithmacy"` | 10 | Only the author's own Substack essay and talk page. |
| W4 | WebSearch | `"idempotent interpretation"` | 20 | Das, De & Kuznetsov, arXiv 2512.19401; general "idempotence" pages. |
| W5 | WebSearch | `"intent specification" LLM agents users human-AI interaction` | 10 | Kim et al. arXiv 2507.22134; Kim et al. CHI 2024 workshop paper; arXiv 2309.14459. |
| W6 | WebSearch | `"governance tracking" algorithm platform rule changes users` | 10 | No use as a term; Platform Governance Archive; Ranking Digital Rights. |
| W7 | WebSearch | `"12 principles of animation" LLM chatbot interface anticipation staging timing design` | 18 | Practitioner UI-animation posts; none on LLM interfaces. |
| W8 | WebSearch | `"intent specifications" Leveson human-centered specifications` | 10 | Leveson 2000 (dblp, MIT OCW). |
| L1–4 | Crossref | `Leveson intent specifications`; `algorithmacy`; `"governance tracking"`; `"decision experience design"` | 3 rows; 0; 10 rows; 10 rows | Leveson 2000, 10.1109/32.825764 (and 1998 ICRE, 10.1109/icre.1998.667827). `algorithmacy`: zero records. The rest are below. |
| F1 | WebFetch | atlassian.design/rovo-ui/motion | 1 | Motion signals "listening, adapting"; a "generative border" signals generation; no animation principles named, no decisions. |

## Close hits

| reference | seen as | (a) | (b) | (c) | what it does; what it lacks |
|---|---|---|---|---|---|
| Pinhanez, C. S. (2017). Design methods for personified interfaces. *CHIRA 2017*, 27–38. 10.5220/0006487500270038 | **full** (Consensus OA copy; opening paragraphs skimmed) | partial | no | **partial** | Turns puppetry and "movie animation" into design methods for chatbots ("puppet prototyping"). It applies Thomas & Johnston's anticipation to a binding act: before "charging a credit card," the interface depicts "the preparation for charging which allows one more chance for the user to change her mind." It also borrows bunraku's exposed puppeteer: a chatbot "displays alternative understandings of an utterance" and lets the user choose. **Lacks:** competencies (it selects by designer requirements: coherent traits, conflict, drama); LLMs; propositions (workshops are "not as validation"). Staging, timing and the other principles "may also be applied … We do not explore them further … due to space restrictions." |
| Kurian, N. (2025). Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney. *IJCCI*, 46, 100788. 10.1016/j.ijcci.2025.100788 | **full** (to char 77,833 of 79,523) | no | analogue | partial | Extracts techniques from 52 Disney films and **selects them through a user-capacity lens** (Piagetian stages) into six design scaffolds. It names exaggeration, appeal and staging, and "visual pacing" where "the camera often holds a beat." **Lacks:** the animation reading of the AI; deciding, opacity, binding or a triad (it excludes "algorithmic recommendation systems"); adult users; propositions ("these heuristics require empirical validation"). |
| Zhang, C., & Davis, A. (2026). Narrative keyframing for generative creative writing. *UIST '26*. 10.1145/3830398.3830586 (arXiv 2608.10337) | **full** (§3.1, design goals, system, discussion and limitations read; study detail skimmed) | no | no | partial | Carries animation **keyframing and interpolation** into an LLM interface: writers set plot, character and perspective keyframes, and the model generates the prose between them. It chooses the technique to "balance automation with creative control"; design goal DG3 traces "how characterization decisions propagate into generated story text." **Lacks:** the animation reading, competencies, a binding intermediary, and any second technique. |
| Wu, J., & Masson, D. (2026). AInimation. arXiv 2607.18507 | abstract this run; full via card `wu2026ainimation` | no | no | partial | Animated prompt-to-response transitions help users review outputs; crafted, slower animation beats instant display. **Lacks** (per card): any animation-craft source (no Thomas & Johnston or Lasseter; slow-in/out is cited to Dragicevic), the character reading, and the word "decision." |
| So, J., Cheng, C., & Murthy, S. K. (2026). Beyond anthropomorphism: A spectrum of interface metaphors for LLMs. *CHI EA '26*, 1–7. 10.1145/3772363.3798591 | **full** (29,980 of 29,980 chars) | no | no | partial | Names "motion and animations" as one level at which LLM interfaces instantiate a metaphor. It sketches "[a]nimations designed to build user understanding of LLM processes during natural loading pause" (Fig. 3), chosen against desiderata such as "[s]upport for understanding constituent functions" and "[p]romoting user agency." **Lacks:** animation theory or craft, competencies, decisions and propositions. |
| Hau, M. F. (2026). Prosopopoeia. *Review of Communication*, 26, 292–305. 10.1080/15358593.2026.2619407 | abstract | near (performance, not animation) | **yes in kind** | no | Treats the chatbot "as a performance to be managed rather than a subject to be believed" and proposes prosopopoeic frameworks "as a critical competency." **Lacks:** an animation frame and any interface design. |
| Govind Reddy (2026). The illusion of mind: What Disney animation teaches us about AI's missing inbetween frames. Zenodo preprint. 10.5281/zenodo.18859162 | abstract + full text skimmed (headings, §5.2) | analogy | no | no | An essay mapping Disney keyframes and in-betweens onto AI architecture. **Lacks:** any interface, design method or user. |

**Further neighbours, not close** (abstracts only): puppetry for robots (Weir et al., 2026, who reuse the
name "puppet prototyping" for a different method; Lewis et al., 2026); animation-derived believability
principles (Curtis et al., 2022); the agent "action-expression problem" (Sengers, 1998); robot motion timing
(Zhou et al., 2017); mobile animation guidelines mapped to anticipation (Liddle, 2016). None concerns LLM
interfaces or decisions. Atlassian's Rovo page (F1) animates agent states without animation principles.

**A date to check.** Run 1 dates Kurian "2025-04-11"; Crossref gives vol. 46, art. 100788, issued December 2025. I left run 1 unchanged.

## Label checks

- **"Algorithmacy" — clear.** Crossref returns zero records; the web finds only the author's own essay and
  talk page (not Oberschelp 1995, which the lab already knows).
- **"Idempotent interpretation" — used elsewhere, in another field.** Das, De & Kuznetsov (arXiv
  2512.19401, §5.2) title a subsection "An idempotent interpretation of productive expressions" and state
  "Definition 30 (Idempotent interpretation)," a map on semiring terms. A second risk is the word itself:
  the W4 results give *idempotent* its standard sense, an operation that yields the same result when
  repeated. The gloss "one output, many possible causes" describes a many-to-one mapping instead, so a
  mathematician or programmer may misread the label. The author should decide.
- **"Intent specification" — taken, twice.** Leveson (2000), *IEEE TSE* 26(1), 10.1109/32.825764, is
  titled "Intent specifications: An approach to building human-centered specifications." In HCI/LLM work, Vaithilingam et al. (2025, arXiv 2504.09283) call a store of
  natural-language user intent held by an AI (Cursor Rules, ChatGPT-style memories) "an 'intent
  specification.'" That is the user-to-AI, prompting-adjacent sense m7 disclaims. W5 shows more LLM uses
  (Kim et al., arXiv 2507.22134; search summary only). The term needs a contrast with both senses, or a new
  name.
- **"(Intuitive) governance tracking" — clear as a term** (web, Crossref top 10, arXiv). The idea sits close
  to DeVito's (2021) "adaptive folk theorization": "[b]ecause platforms constantly change, users must
  constantly re-evaluate their folk theories" (abstract).
- **"Decision Experience Design" — clear** (web, Crossref top 10). Nearest: Card (2023), "Deliberative
  Experience Design for Environmental Decision Making," 10.1515/9781438491301-005 (title only).

## Verdict

The gap holds, but m7 is narrower than its parts. **I found no work that selects professional animation
techniques through the competencies a person needs to decide through an opaque, binding, adaptive
intermediary,** in eight Consensus queries, ten arXiv queries, four Crossref queries, OpenCitations
snowballs on Chang & Ungar (1993) and Thomas & Calder (2001), three Zenodo queries, eight web searches, one
practitioner page and four Crossref label queries. Scholar Gateway, OpenAlex and Semantic Scholar all
failed, so the sentence holds for these sources only. [Claude's wording, for the author to keep, rewrite or
reject.]

Each part of the move has a prior the paper must cite and set apart:

1. **Anticipation before a binding act is taken in part.** Pinhanez (2017) applies anticipation so a chatbot
   user gets "one more chance … to change her mind" before a charge. He also turns puppetry into a design
   method for chatbots. A proposition on anticipation or on placing a change between moves must cite him.
2. **Selecting animation techniques through a user-capacity lens is taken for children.** Kurian (2025)
   filters Disney technique through Piagetian development. DXD's novelty is the lens and the propositions, not
   the selection move.
3. **Single techniques carried into LLM interfaces are taken.** Zhang & Davis (2026) transfer keyframes and
   in-betweens; Wu & Masson (2026) animate prompt-to-response transitions; So et al. (2026) design LLM
   loading animations. None selects among techniques or aims at a decision.
4. **(a) is Stark's (run 1), and a competency framing of chatbot-as-performance exists** (Hau, 2026).
5. **"Intent specification" collides** with Leveson (2000) and with Vaithilingam et al. (2025).

## Candidates the library should card

1. **Pinhanez 2017** — the closest prior to (c): anticipation before a binding chatbot act; puppetry as a
   chatbot design method. Open full text.
2. **Kurian 2025** — the precedent for selecting animation technique through users' capacities. Open; fix the
   run-1 date.
3. **Zhang & Davis 2026** — keyframes and in-betweens in an LLM interface; decision traceability (DG3).
4. **Vaithilingam et al. 2025** — the HCI/LLM owner of "intent specification."
5. **So, Cheng & Murthy 2026** — LLM loading-pause animations (G reserve R1). Open full text.
6. **Hau 2026** — chatbot-as-performance as a competency; nearest (b)-side neighbour (G reserve).
7. **DeVito 2021** — adaptive folk theorization; the nearest prior idea to intuitive governance tracking.
8. **Leveson 2000** — first owner of "intent specifications"; cite it or rename the competency.
