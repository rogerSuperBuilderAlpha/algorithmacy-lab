# Triage: G (gap check)

> **[Drafted by Claude, 2026-11-05; run `dxda-lib-2026-11`, stage S3 (triage), facet G.]** This note tests
> claim c9, that no prior work frames LLM interfaces as animation for decision design. For each near miss it
> states how close the work comes to the paper's claim, and it shortlists only the near misses the paper must
> engage. I opened every record named here on Crossref and OpenAlex on 2026-11-05 (1 s between calls) and read
> abstracts only; the JSON sits in this session's scratchpad. Words quoted from an abstract are the registry
> abstract's. I checked every proposed key against `registry.tsv` and `cards/`; none collides. `GAP_CHECK.md`
> (S9) carries the logged negative result.

Run `dxda-lib-2026-11` · date 2026-11-05 · stage S3 · drafted by Claude.

**The claim tested.** The paper argues two things together: an LLM interface is an animation (c4–c7), and
therefore Decision Experience Design should apply the animator's methods to surface decisions in the missing
frames, rather than hide those frames or expose the backend (c8). A work anticipates c9 only if it makes the
second move from the first.

**Counts.** Shortlist 4 new (Maeda & Stark 2025, Shanahan et al. 2023, Jones 2026, Siskind et al. 2024); reserve
5; 7 more near misses assessed and left out. FACETS sets G at 2 new (stretch 3). The brief allows 4, and G goes
one past FACETS' stretch. F10 stays at its core 2 (F9-F10.md), so F9 + F10 + G propose 12 new cards, the same
total as FACETS' stretch for the three facets (6 + 3 + 3), inside the run-wide ceiling of 60. If the lead must
cut, cut #4 (Siskind) first. Every shortlisted work is open; none needs the author's browser.

## Sources searched

- `tools/search.py G` (SEARCH_LOG, 2026-11-05): five queries each on OpenAlex (25 hits), Crossref (20) and arXiv
  (10). Semantic Scholar answered HTTP 429 on all five, so that leg is missing.
- Consensus, two queries of 50 (`G_llm_as_animation.txt`, `G_F9_animation_principles_agents.txt`).
- OpenAlex snowball, run today: all 19 works citing L. Stark 2024 (W4399363127) and both works citing Maeda &
  Stark 2025 (W4415230638).
- OpenAlex `title_and_abstract.search`, run today: `animation AND ("large language model" OR chatbot OR LLM) AND
  (decision OR "decision-making")` (21 hits) and `Silvio AND animation` (24 hits).
- The prior DXD term search (`decision_experience_design/literature/facets/F1_term_and_gap.md`, 2026-09-30):
  "decision experience design" has no scholarly use in OpenAlex, arXiv, Consensus or the Semantic Scholar
  queries that completed.

## Near misses, one by one

Distance is measured against both halves: (A) LLM interface as animation, and (B) from that, a method of design
that surfaces the user's decisions in the gaps.

| Work (record opened today) | (A) LLM as animation? | (B) design for decisions? | How close it comes |
|---|---|---|---|
| L. Stark (2024), FAccT, 10.1145/3630106.3658995 | **Yes.** Chatbots "can be best understood as animated characters" (abstract), via Silvio. | No. The traits of animation "help us both analyze and respond appropriately" to AI and to "hyperbolic claims" (abstract): critique, not a design method. | The nearest prior on (A); already the library's anchor `stark2024animation`. |
| **Maeda & Stark (2025)**, AIES 8(2), 1661–1673, 10.1609/aies.v8i2.36664 | **Yes, extended.** A "network of distributed human agents" collectively "animate" anthropomorphic features (abstract): the animator is plural, which is c7's triad. | Partly. They argue for "distributed governance" and adapting "existing models" of intervention (abstract), so the consequence is governance of harms, not an interface method, and decisions are not its object. | **The closest work found.** Stark's own sequel takes the animation reading toward intervention. The paper must say that its move differs: a designer's craft inside the interface, not governance across the network. Shortlist #1. |
| **Shanahan, McDonell & Reynolds (2023)**, *Nature* 623, 493–498, 10.1038/s41586-023-06647-8 | No: **role play**, not animation. They cast "dialogue-agent behaviour in terms of role play" to avoid anthropomorphism (abstract, Consensus listing; OpenAlex holds none). | No design programme. | Far on (B), but it is the rival frame a reviewer will raise (543 OpenAlex citations). Role play is a performance frame, which Silvio sets against animation (introjection versus projection, CHECK F4). The paper uses it as the dyadic alternative c7 argues past. Shortlist #2. |
| **Jones (2026)**, *Annual Review of Applied Linguistics* 46, 34–55, 10.1017/s0267190526100312 | **Yes.** Jones brings together "Silvio's notion of animation" and Blommaert's "enoughness" for ChatGPT's voice mode and Sesame.ai (abstract). | No. "Designers, users and AI systems co-produce boundaries of authenticity" (abstract), and identity is the object, not decisions. | Shows that the Silvio reading of AI interfaces is not Stark's alone and names designers as co-animators (c6, c7). Nothing on decision design. Shortlist #3. |
| **Siskind, Nichols & Gómez (2024)**, *Frontiers in Robotics and AI* 11, 1256937, 10.3389/frobt.2024.1256937 | No: **stage magic**, not animation. | **Yes in form, opposite in aim.** They borrow a performance craft's principles for chatbot conversation and model communication "centered on controlling the user's attention, expectations, decisions, and memory" (abstract), tested on a social robot; the aim is engagement and "character likability". | The nearest work on (B): it makes c8's structural move (learn a craft's methods for the conversational interface) with another craft and toward steering decisions rather than surfacing them. A strong contrast for §5. Shortlist #4 (stretch). |
| So, Cheng & Krishna Murthy (2026), CHI EA, 10.1145/3772363.3798591 | No: interface **metaphors**; anthropomorphism becomes "a design variable" (abstract). | Yes for design, not for decisions. Their spectrum runs to "anti-anthropomorphism" that exposes "human labor, infrastructure, and data" (abstract). | Close on design for LLM interfaces, and its pole is the "expose the backend" option §5 rejects. Ananny & Crawford already carry that option, so it waits in reserve (R1). |
| González (1996), CHI, 10.1145/238386.238396 | No. Animation means moving imagery in decision-support interfaces, pre-LLM. | **Yes, empirically**: smooth transitions made subjects "more accurate" (CHI abstract, Consensus listing). | Shares the words "animation" and "decision" and nothing of the LLM-as-character reading. It is an F9 precedent for c8 (shortlisted there as `gonzalez1996does`), not a prior statement of c9. |
| Maeda & Quan-Haase (2024), FAccT, 10.1145/3630106.3658956 | Near. Chatbot "roleplaying" and "user role projection co-produce a pseudo-interactive" space (abstract); it cites Stark 2024. | Ethical concerns, not a design method. | Parasociality framing; F3 territory. Reserve R2. |
| Hau (2026), *Review of Communication* 26(4), 292–305, 10.1080/15358593.2026.2619407 | Near. Deliberate prosopopoeia "treats the machine as a performance to be managed" (abstract). | No: a user's "critical competency" and AI literacy, not a designer's method. | The user-side twin of c8: the user, not the designer, manages the gaps. Reserve R3. |
| Bernini (2025), *Style* 59(3), 466–507, 10.5325/style.59.3.0466 | Near. LLMs as "fictional objects of relation", "four illusions" of character engagement (abstract). | No. Fictionality as "a training ground for double exposure" (abstract): a reader's skill. | Narrative theory of character, not animation; no design. Reserve R4. |
| Keane (2026), *JRAI* 32(3), 1022–1039, 10.1111/1467-9655.70133 | No. Chatbots as "metahumans" whose authority endows "the profit-seeking strategies of their corporate owners" with "a supernatural aura" (abstract). | No. | Supports c3 and c7 (an owner behind the interlocutor) without animation or design. Reserve R5. |
| Sun & Gualeni (2025), in Springer Series on Cultural Computing, pp. 49–63, 10.1007/978-3-031-89037-6_3 (preprint 10.48550/arxiv.2501.15346) | Near. AI agency lies "between that of an inanimate puppet and a performing actor" (arXiv abstract). | No. The question is creative **authorship**. | Puppet imagery for LLMs, aimed at authorship in storytelling, not interfaces or decisions. Left out. |
| Lewis, Collins, Hanson, Smith & Williams (2026), arXiv:2607.03289 (OpenAlex W7167590569; no Crossref record) | No. Robots, not LLM interfaces. | Yes for design. Puppetry principles for "robot behavior design", because Disney's principles are "inherently limited" for embodied characters (abstract). | A limit on transferring animation principles, relevant to F9 (reserve R7 there), not to c9. Left out here. |
| Ávila-Muñoz, Clemente-Mediavilla & Perez-Luque (2021), *Review of Communication Research* 9, 119–146, 10.12840/issn.2255-4165.030 | No. Functional animation in GUIs. | No. A taxonomy of functions (abstract). | F9 territory (reserve R5 there). Left out here. |
| Markov & Shtayn (2026), "The puppet's voice", CyberLeninka (OpenAlex W7166720725; DOI 10.48417/technolang.2026.02.02 has no Crossref record) | Near. The puppet's voice as "an interface", ending in "an algorithmic agent" (abstract). | No. | Media philosophy of voice; no design. Left out (no Crossref record). |
| Maeda & Buening (2026), FAccT, 10.1145/3805689.3812282 | Unknown: title only ("Safety theater in anthropomorphic AI"), seen as a Stark 2024 citer. | Unknown. | Theatre metaphor aimed at accountability narratives, by title. Abstract not opened; S9 checks it before `GAP_CHECK.md` closes. |

The other Stark 2024 citers are animation-production studies (Rall et al. 2025; Wright et al. 2025; the 2026
Spanish-language reviews), AI-evaluation history (Becerra Sandoval & Jing 2025, two papers), a child-robot system
(Wang et al. 2025), puppetry activism (Opel & Schrock 2025) and LLM discourse analysis (Zhang et al. 2026). None
draws a design consequence from the animation reading. The two Maeda & Stark 2025 citers concern a literary
Turing test and algorithmic advice in education.

## Verdict

L. Stark (2024) and Maeda and Stark (2025) make the first half of the argument (an LLM chatbot is an animated
character, animated by many hands), and Jones (2026) extends it to voice interfaces. Their consequences stop at
critique and governance. Siskind et al. (2024) make the second half's move in form, borrowing a performance
craft to design chatbot conversation, but the craft is magic and the aim is to steer the user's attention and
decisions toward engagement. González (1996) ties interface animation to decision quality, before LLMs and
without the character reading. No single work joins the two halves.

**I found no work that frames an LLM interface as an animation and draws from that frame a design method for
surfacing a user's decisions in the missing frames, in OpenAlex, Crossref and arXiv (five queries each),
Consensus (two queries of 50), OpenAlex snowballs of the works citing Stark 2024 (19) and Maeda & Stark 2025 (2),
two OpenAlex title-and-abstract filters, and the prior DXD term search.** The Semantic Scholar leg failed (429 on
all five G queries), so the verdict holds for these sources only. Abstracts were read, not full texts; the cards
for #1 and #3 must confirm that neither paper proposes an interface method in its body.

## G shortlist

| # | key | work (APA) | why | claims | role | doi or id | OA route | expected read_depth |
|---|---|---|---|---|---|---|---|---|
| 1 | `maeda2025anthropomorphism` | Maeda, T., & Stark, L. (2025). Anthropomorphism as social affordance: Charting the co-animation of chatbots into social "agents". *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 8(2), 1661–1673. | The closest prior: a distributed network "animate[s]" chatbots, and the response is "distributed governance" (abstract). The paper's c9 must differ from it explicitly, and its plural animator supports c7. Missing from FACETS and from the brief's list; found in the G search (OpenAlex). | c9, c7, c4 | contrast | 10.1609/aies.v8i2.36664; OpenAlex W4415230638 | open (bronze): https://ojs.aaai.org/index.php/AIES/article/download/36664/38802 | full_text |
| 2 | `shanahan2023role` | Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role play with large language models. *Nature*, 623(7987), 493–498. | The dominant rival frame: role play, a performance reading that Silvio's projection/introjection split sets against animation. §3.3 or §4.3 must say why animation, not role play, fits a triad. F3 could also claim it as its "LLM persona" hit; card it once, tagged G and F3. | c9, c7, c4 | contrast | 10.1038/s41586-023-06647-8; OpenAlex W4388488609 | open (bronze): https://www.nature.com/articles/s41586-023-06647-8.pdf | full_text |
| 3 | `jones2026animating` | Jones, R. H. (2026). Animating AI: Language variation and "enoughness" in voice user interfaces. *Annual Review of Applied Linguistics*, 46, 34–55. | A second, independent use of Silvio's animation for AI interfaces, with designers named among the co-producers. It shows that c4 does not rest on Stark alone, and that nobody yet draws a decision consequence from it. | c4, c6, c9 | support | 10.1017/s0267190526100312; OpenAlex W7167928003 | open (hybrid): Cambridge Core PDF via OpenAlex oa_url | full_text |
| 4 | `siskind2024would` | Siskind, S. R., Nichols, E., & Gómez, R. (2024). Would you be impressed: Applying principles of magic to chatbot conversations. *Frontiers in Robotics and AI*, 11, 1256937. | **Stretch.** The structural twin of c8 with the opposite aim: a craft's principles used to control "attention, expectations, decisions, and memory" (abstract). §5 can set the animator's surfacing against the magician's misdirection. Tested on a social robot, which the card notes. | c8, c9 | contrast | 10.3389/frobt.2024.1256937; OpenAlex W4395078800 | open (gold): https://doi.org/10.3389/frobt.2024.1256937 | full_text |

## G reserve

| # | key | work | why not now | claims | role | doi or id | OA route | expected read_depth |
|---|---|---|---|---|---|---|---|---|
| R1 | `so2026beyond` | So, J., Cheng, C., & Krishna Murthy, S. (2026). Beyond anthropomorphism: A spectrum of interface metaphors for LLMs. *CHI EA '26* (pp. 1–7). | Design for LLM interfaces whose transparency pole is §5's rejected "expose the backend" option. Promote it over #4 if §5 wants an LLM-specific contrast instead of a craft-transfer one. | c8, c9 | contrast | 10.1145/3772363.3798591; W7153736380 | open (hybrid) | full_text |
| R2 | `maeda2024when` | Maeda, T., & Quan-Haase, A. (2024). When human-AI interactions become parasocial: Agency and anthropomorphism in affective design. *FAccT '24* (pp. 1068–1077). | Parasocial framing of chatbot role play; F3 if anywhere. | c4, c6 | support | 10.1145/3630106.3658956; W4399362852 | open (hybrid) | abstract |
| R3 | `hau2026prosopopoeia` | Hau, M. F. (2026). Prosopopoeia: Metacommunication and "as-if" in human–AI communication. *Review of Communication*, 26(4), 292–305. | Puts gap management on the user's side as a literacy; useful only if §6 discusses user-side alternatives. | c6, c9 | contrast | 10.1080/15358593.2026.2619407; W7128485089 | open (hybrid) | abstract |
| R4 | `bernini2025ai` | Bernini, M. (2025). AI as character: Real patterns in fictive interactions. *Style*, 59(3), 466–507. | Character theory without animation or design. | c4 | support | 10.5325/style.59.3.0466; W7155074459 | open (green, per OpenAlex) | abstract |
| R5 | `keane2026talking` | Keane, W. (2026). From talking tools to metahumans: Social interaction, semiotic skill, and the authority of AI chatbots. *Journal of the Royal Anthropological Institute*, 32(3), 1022–1039. | Supports c3 and c7 (the corporate owner behind the interlocutor) but makes no animation or design claim; F7 could take it. | c3, c7 | support | 10.1111/1467-9655.70133; W7153312482 | open (hybrid) | abstract |

## Key notes

- `maeda2025anthropomorphism`: Crossref types it `journal-article` (AIES proceedings published as a volume, 8(2));
  the card uses `type: proceedings` and keeps volume and issue. Luke Stark is the second author, so the card's
  Caution separates this paper from `stark2024animation` and from D. Stark (CHECK F8).
- `shanahan2023role`: OpenAlex types it `review`; Crossref `journal-article`. Shanahan's *Talking about large
  language models* (CACM 67(2), 68–79, 10.1145/3624724) is dated 2022 in Consensus (the arXiv year) and 2024 by
  Crossref, the volume year. It stays out; #2 carries the role-play frame.
- `jones2026animating`: volume 46 is the 2026 volume; OpenAlex and Crossref agree.
- `siskind2024would`: Crossref spells the third author "Gomez", OpenAlex "Gómez"; the card follows the byline.
- The brief's "Sun et al. 2025" has two authors (Sun & Gualeni), and its DOI 10.48550/arxiv.2501.15346 is the
  preprint. The version of record is the Springer chapter 10.1007/978-3-031-89037-6_3, pp. 49–63, which OpenAlex
  merges with the preprint (W4412732348).
- The brief's "Lewis et al. 2026" and "Ávila-Muñoz et al. 2021" match their records; González 1996 is
  single-authored, and its journal version (González & Kasper 1997) is F9 reserve R4.
