---
key: park2023generative
apa: "Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–22). ACM. https://doi.org/10.1145/3586183.3606763"
authors: "Park, Joon Sung; O'Brien, Joseph; Cai, Carrie Jun; Morris, Meredith Ringel; Liang, Percy; Bernstein, Michael S."
year: 2023
title: "Generative Agents: Interactive Simulacra of Human Behavior"
venue: "UIST '23"
volume: ""
issue: ""
pages: "1–22"
doi: "10.1145/3586183.3606763"
url: ""
type: proceedings
facets: [F8]
claims: [c1, c6, c11]
role: support
load: load-bearing
read_depth: partial
object_read: "arXiv v2 (6 Aug 2023) PDF, set in the UIST '23 ACM format (its first page carries the UIST '23 line, the ACM ISBN and the DOI; the ACM reference line says 22 pages), and its text layer park2023generative.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/park2023generative/; fetched from https://arxiv.org/pdf/2304.03442 (FETCH_LOG.tsv, route openalex_location_pdf); no copy in inbox/; read 2026-11-08; sha256 1b31e77fb24d25d7598f2c49e955d12a28b95a6dabad34acdac40f44bfb7a139 (PDF, from sha256.txt). Parts read: PDF pp. 1–18 (abstract, §1–§9, acknowledgements) in full. Parts not read: the reference list (pp. 18–20 beyond a check of ref. [10]) and Appendices A (architecture optimizations) and B (interview questions and sample answers), pp. 20–22."
verified: corrected
verified_against: "crossref.json, openalex.json; sha256 re-hashed; per-page pdftotext of the arXiv v2 PDF, 15 quotations traced (all verbatim, all page and section locators correct); numbers in What it argues checked against the text"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# J. S. Park et al. (2023), Generative agents

## What it argues

Park, O'Brien, Cai, Morris, Liang and Bernstein build "generative agents": software characters that
simulate believable human behaviour by wrapping a large language model (ChatGPT, `gpt3.5-turbo`, §4) in
an architecture. The architecture has three parts. A *memory stream* records every observation in plain
language, and a retrieval function scores memories by recency, importance and relevance (§4.1).
*Reflection* periodically asks the model to draw higher-level conclusions from recent memories and stores
them as new memories (§4.2). *Planning* has the model write a day's plan "in broad strokes", then break it
down recursively into hour-long and then 5–15-minute actions, and re-plan when the agent reacts to
something it perceives (§4.3). A game server (Phaser) and a tree of places and objects, translated to and
from natural language, tie the agents to a Sims-style town of 25 characters (§5).

The authors argue that the model alone is not enough. Used on its own, it can output behaviour but cannot
keep an agent coherent over time. They test this with an "interview" evaluation of five question categories,
comparing the full architecture with three ablations (no reflection; no reflection or planning; no access
to the memory stream at all) and a crowdworker-authored baseline.
One hundred Prolific raters ranked the conditions by believability. The full architecture ranked first
(TrueSkill mean 29.89), and each removed component lowered the rating (§6). A two-day run of all 25 agents
then shows information spreading from one agent to 13 (the Valentine's Day party), network density rising
from 0.167 to 0.74, and five of twelve invited agents turning up (§7). The authors also list failures:
bad memory retrieval, embellished memories, over-formal and over-cooperative speech inherited from
instruction tuning. The ethics section (§8.3) names parasocial attachment, error, deepfakes and
over-reliance on agents in place of human participants as risks, and proposes disclosure and audit logs.

The paper is a systems-and-evaluation paper from human-computer interaction. It does not discuss life,
animation theory or the nature of intelligence. It touches animation only in two places: a footnote and a
related-work sentence that both liken believable agents to Disney characters.

## What the paper uses it for

- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the use fits well. Park et al. state
  that the model needs "mechanisms" around it to keep an agent coherent, and they spend most of the paper
  on those mechanisms: memory store, retrieval scoring, reflection, planning, an environment tree, a game
  server. This is a worked example of a system that people would call "an AI character" and that is
  mostly not the model. It stretches in two ways. First, the authors never say the intelligence sits
  outside the model; they say the model is "not sufficient by themselves" (p. 3) and keep it as the
  generator of every step. Second, c1 names "efficiencies"; the body speaks only of cost ("thousands of
  dollars in token credits", p. 17), and the one section that may deal with optimisation (Appendix A) was
  not read.
- **c6** (animation is the craft of composing a living character from inert parts): the one place in this
  group where the builders compare their own work to character animation. Footnote 1 (p. 2) says the
  agents' behaviour is "akin to animated Disney characters", and §2.2 (p. 3) defines believable agents by
  an "illusion of life". The use stretches the source. Both passages are similes, and the footnote uses
  the Disney comparison to disclaim "genuine agency", which is the opposite of treating the build as
  bringing something to life. Park et al. use no pipeline vocabulary (rig, key pose, in-between). The
  mapping of their day plan ("broad strokes", then recursive detail, p. 11) onto key poses and in-betweens
  is the paper's reading, not Park et al.'s.
- **c11** (implementation and evaluation under the life frame): Park et al. give a concrete way to evaluate
  an agent as a character. Their dependent variable is "the believability of the behavior" (p. 13), judged
  by observers who rank conditions, and they say why: "Optimizing for believability in the moment
  sacrifices believability over time" (p. 11), which is the consistency-over-time criterion of SKETCH §6.
  It stretches the source because Park et al. take believability from the believable-agents tradition
  (their ref. [10], Bates 1994), not from a life frame, and their footnote 1 denies agency. The
  implementation side (a rehearsal of persona seeds, a plan, a replan loop) fits "casting, rigging,
  rehearsal" only by analogy.

## Loci

Matched against park2023generative.txt (arXiv v2 PDF, text layer, run through a whitespace-and-hyphen
normaliser). Page numbers are PDF pages; the PDF has 22 pages and the Crossref range is 1–22, so PDF page n
is taken to be page n of the article (not checked against the ACM Digital Library file). Inner quotation
marks are changed to single quotes.

- p. 2, fn. 1: "The behaviors of our agents, akin to animated Disney characters, aim to create a sense of believability, but they do not imply genuine agency."
- p. 3, §2.2: "Believable agents are designed to provide an illusion of life and present a facade of realism in the way they appear to make decisions and act on their own volition, similar to the characters in Disney movies [10, 96]."
- p. 3, §2: "large language models, though not sufficient by themselves, open up a new angle for creating believable agents when leveraged using the appropriate architecture."
- p. 2, §1: "We demonstrate that, with generative agents, it is sufficient to simply tell one agent that she wants to throw a party."
- p. 6, §3.1.2: "To directly command one of the agents, the user takes on the persona of the agent’s ‘inner voice’—this makes the agent more likely to treat the statement as a directive."
- p. 8, §4: "Underlying this behavior is a novel agent architecture that combines a large language model with mechanisms for synthesizing and retrieving relevant information to condition the language model’s output."
- p. 8, §4: "Without these mechanisms, large language models can output behavior, but the resulting agents may not react based on the agent’s past experiences, may not make important inferences, and may not maintain long-term coherence."
- p. 11, §4.3: "Optimizing for believability in the moment sacrifices believability over time."
- p. 11, §4.3: "To create such plans, our approach starts top-down and then recursively generates more detail."
- p. 11, §4.3: "The agent saves this plan in the memory stream and then recursively decomposes it to create finer-grained actions"
- p. 13, §6.1: "Our dependent variable is the believability of the behavior, a central dependent variable in prior work on agents (e.g., [10])."
- p. 13, §6.1: "The evaluators ranked the believability of the conditions from most to least believable."
- p. 17, §7.2: "we observed that the instruction tuning also seemed to make the agents overly cooperative with one another."
- p. 17, §8.2: "In general, any imperfections in the underlying large language models will be inherited by generative agents."
- p. 18, §8.3: "Despite being aware that generative agents are computational entities, users may anthropomorphize them or attach human emotions to them [43, 84]."

## Caution

- **Version.** The copy is the arXiv v2 PDF, which is typeset as the UIST '23 paper. The Crossref record
  gives the proceedings as the version of record; I have not seen the ACM Digital Library file, so a
  verifier should confirm that the wording of the loci and the page breaks match it. DECISIONS routes this
  key to the ACM DL PDF; the arXiv copy is what FETCH_LOG fetched.
- **Author names.** Crossref gives "Joseph O'Brien" and "Carrie Jun Cai"; the PDF byline prints "Joseph C.
  O'Brien" and "Carrie J. Cai". The APA string follows Crossref's given names, as the DECISIONS row does.
  The author decides whether to use the byline's middle initial.
- **Dates.** Crossref gives 2023-10-29 (the conference opening); OpenAlex gives 2023-10-20. Both are 2023,
  so no `registered_year`. The arXiv v2 date is 6 Aug 2023.
- **Disney reference.** The "illusion of life ... Disney" sentence cites refs. [10, 96]. Ref. [10] is
  Bates 1994 (read in the reference list); I did not look up [96]. Park et al. are not the source of the
  Disney comparison, only of its use in HCI. Check Bates before the paper credits the idea to Park.
  [Verifier, S6:] ref. [96] is "Frank Thomas and Ollie Johnston. 1981. Disney Animation: The Illusion of
  Life." (reference list, PDF p. 20, seen this run). The phrase "illusion of life" therefore comes from the
  animators' own book, which Park et al. cite; the paper should credit it there, not to Park.
- **The disclaimer cuts against the paper.** Footnote 1 uses the animation comparison to deny agency. The
  paper cannot cite Park for the claim that building an agent is bringing it to life; it can cite Park for
  a team that compares its characters to animation while denying that they are alive.
- **Relevance to c8, not tagged.** §8.3 (p. 18) names parasocial attachment and over-reliance as risks of
  these agents. That is a developer's warning about the user-side dependency that c8 describes. The author
  can add c8 to this card if the use is wanted.
- **Not read.** Appendices A and B and the reference list (see `object_read`).
- **What the paper may not claim from it:** that Park et al. treat intelligence as living or composed
  outside the model; any account of apparent motion or liveness; any claim that their raters judged
  "aliveness" (they judged believability).

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 4
- verdict: corrected
- checked: frontmatter against crossref.json and openalex.json (authors, 2023, title, UIST '23, pp. 1–22, DOI,
  proceedings; dates 2023-10-29 and 2023-10-20, so no registered_year); sha256 of the PDF matches
  sha256.txt; all 15 quotations found verbatim on the stated PDF page (the p. 18 one matches once the
  raw text layer's dropped word spaces are ignored; the default layer reads it intact), and each section
  locator matches the headings on that page; the figures in What it argues (gpt3.5-turbo, Phaser, 100
  Prolific evaluators, TrueSkill 29.89, one to thirteen agents, density 0.167 to 0.74, five of twelve) and
  the four risks in §8.3. read_depth partial is honest; the stretches on c1, c6 and c11 are named.
- changed: What it argues said "four ablations (remove observation, planning or reflection)"; the paper
  (§6.1, p. 13) has three ablated architectures plus the crowdworker condition, five conditions in all.
  Rewrote that sentence. Added ref. [96] (Thomas & Johnston 1981, *Disney Animation: The Illusion of
  Life*, seen in the reference list, PDF p. 20) under Caution, marked as the verifier's addition. The
  version caution stands: the loci are not checked against the ACM DL file.
