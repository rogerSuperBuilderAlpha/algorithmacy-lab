---
key: subramonyam2024bridging
apa: "Subramonyam, H., Pea, R., Pondoc, C. L., Agrawala, M., & Seifert, C. (2024). Bridging the gulf of envisioning: Cognitive challenges in prompt based interactions with LLMs. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)* (pp. 1–19). ACM. https://doi.org/10.1145/3613904.3642754"
authors: "Subramonyam, Hari; Pea, Roy; Pondoc, Christopher Lawrence; Agrawala, Maneesh; Seifert, Colleen"
year: 2024
title: "Bridging the Gulf of Envisioning: Cognitive Challenges in Prompt Based Interactions with LLMs"
venue: "CHI '24"
volume: ""
issue: ""
pages: "1–19"
doi: "10.1145/3613904.3642754"
url: "https://arxiv.org/abs/2309.14459"
type: proceedings
facets: [F5]
claims: [c1, c2]
role: support
load: load-bearing
read_depth: partial
object_read: "arXiv 2309.14459v2 (cs.HC, 18 Mar 2024), the author copy with the CHI '24 header; not the ACM version of record; local copy ~/iit-playground/dxd_animation_local/pdfs/subramonyam2024bridging/subramonyam2024bridging.pdf, text layer subramonyam2024bridging.txt; original URL https://arxiv.org/pdf/2309.14459 (FETCH_LOG.tsv row subramonyam2024bridging); read 2026-11-05; sha256 a64068cce89ec7d08029e1fc3d4517a65627d5f8d903d0c92b667965f176c6d0"
verified: corrected
verified_against: "arXiv 2309.14459v2 PDF (pdftotext reading-order extraction and the .txt layer), crossref.json, openalex.json; sha256 recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Partial read. Read: abstract; sections 1, 2 and 3 in full; section 4 opening, 4.1 and 4.3.2–4.3.3; design patterns 2–6 and their tenets in section 5; the opening of section 6, the openings of 6.1.1 and 6.1.2, and the end of 6.1 and 6.2; the openings of 7.1 and 7.3; the first paragraph of section 8. Not read: 4.2, 4.3.1, the opening of section 5 and design pattern 1, most of 6.1 and 7, and the reference list.

Subramonyam, Pea, Pondoc, Agrawala and Seifert start from Norman's seven-stage model of action and say HCI usually treats stage two, forming the intention, "as given" (p. 3). Conventional interfaces hide the gap because their buttons and menus let a designer line each action up with a user's intention. A large language model removes those fixed actions. The user must now turn a goal into a prompt without any menu to help. The authors call the distance between a user's initial intentions and a prompt that makes good use of the model "the gulf of envisioning" (p. 3).

They split the gulf into three gaps (pp. 3, 6–8). The capability gap is about what the user can ask the model to do and how to set goals the model can meet. The instruction gap is about how to word the request. The intentionality gap is about judging the output when the user skipped the planning that would give a benchmark for judging it. Their model of interaction has "intentions are the actions" (p. 3). They draw on cognitive models of writing (Hayes and Flower) and of problem solving (Newell and Simon, Duncker) to argue that people plan and revise their intentions as they work, and they offer design patterns and tenets for interfaces that scaffold the user's intention formation (section 5).

## What the paper uses it for

- c1: the bridge from Norman to the LLM interface. Subramonyam and colleagues say the second stage of Norman's model, intention, is a blind spot in established interaction models, and that LLMs make it the main problem. The paper can cite this for "HCI's own models start after the goal or intention is set". It also supports the claim that users adapt their intentions during the interaction (p. 4).
- c1, where the use stretches the source: the authors keep the goal fixed and study the step from goal to intention. Figure 2 (p. 4) and the Taylor-toast running example (introduction, p. 2; Figure 3, p. 7) start from a stated goal. Their abstract's "what the task should be" is the first of three misalignments, but the body defines the matching capability gap as the user's inability to formulate "how to" procedures (p. 6). A goal that changes mid-task, such as raincoat to umbrella, is not their subject. They come closest in two places: intentions change as people work (p. 4), and Duncker's "continual restructuring of a problem" (p. 8). The paper should cite them for the intention-stage gap and argue the moving goal itself.
- c1, trap: the phrase "moving target" in section 6.1 (p. 14) refers to the sweet spot for AI and interface design shifting as users and technology advance. It does not refer to a user's goal. The paper must not cite it for a moving goal.
- c2: the paper supports the cognitive side of the human user only. The authors model planning, mental simulation, system mental models and fixation (pp. 3–7). Emotion appears once in the text I searched, in passing, about iteration on personal writing (§3.2, p. 7). They say nothing on the biological side. The card does not support the claim that the user is biological, cognitive and emotional.

## Loci

Quotations are verbatim, with inner double quotation marks changed to single quotes. Locators are PDF pages of the arXiv v2 file, counted by form feeds (page 1 is the title and abstract page), with the section number. The arXiv copy carries no printed page numbers, so these may differ from the ACM version's 1–19 pagination. Each line was matched against the PDF's pdftotext extraction (the .txt is column-interleaved, so I matched in the extraction that keeps column order).

- "a blindspot even in established interaction models such as Norman’s gulfs of execution and evaluation" — PDF pp. 1–2, abstract. Matched against the local PDF text.
- "(1) what the task should be, (2) how to instruct the LLM to do the task, and (3) what to expect for the LLM’s output in meeting the goal" — PDF p. 2, abstract. Matched against the local PDF text.
- "In much of HCI work, stage two – forming the intention – is assumed as given" — PDF p. 3, §2. Matched against the local PDF text.
- "In reality, users constantly adapt their intentions based on both their dynamic cognitive task processes (what they want to accomplish) and their system mental model (what they believe can be accomplished through system actions)." — PDF p. 4, §2.2. Matched against the local PDF text.
- "Defining a problem is far from a determinate process yet central to success." — PDF p. 5, §3.1. Matched against the local PDF text.
- "The capability gap concerns the users’ inability to formulate ‘how to’ procedures to implement their intentions." — PDF p. 6, §3.2.1. Matched against the local PDF text.
- "Those with less developed intentions may be more likely to show a stronger fixation on an initial LLM output due to a lack of knowledge about desirable outcomes." — PDF p. 7, §3.2. Matched against the local PDF text.
- "the intentionality gap lies at the cognitive level due to the user’s failure to create clear intentions" — PDF p. 8, §3.2.3. Matched against the local PDF text.
- "the ‘sweet spot’ for AI and interface design remains a moving target that adapts to the growing sophistication of both users and technology" — PDF p. 14, §6.1. Matched against the local PDF text. Recorded as a trap; see the c1 bullet.

## Caution

- The object read is the arXiv v2 author copy, not the ACM version of record. The ACM version may differ in wording and pagination. Locators here are PDF pages and sections.
- The abstract's three "misalignments" and the body's three gaps do not line up one to one. The abstract lists what the task should be, how to instruct, and what to expect from the output. The body names them the capability, instruction and intentionality gaps, and the capability gap is defined as "how to" procedures for the model to carry out (p. 6), while the introduction glosses it as setting "goals and intentions such that the LLM can accomplish the task" (p. 3). The triage note maps "what the task should be" onto c1's moving goal. That mapping is generous. The source's first gap is about fitting the goal to what the LLM can do.
- The triage records 169 OpenAlex citations for this paper. I did not check that figure this run, so it stays out.
- The paper is theory plus an analysis of three existing interfaces: ChatGPT, Spellburst (a creative-coding research tool) and Cursor (§4.1–4.3). It runs no user study, and its claims about users come from cited cognitive science.
- The Norman seven-stage model and the gulfs: the paper credits the gulfs to Hutchins et al. (its ref [68]) and the seven stages to Norman (ref [120]). The paper's own OUTLINE §1 attributes the seven stages and the gulfs to Norman and to Hutchins, Hollan and Norman. Both are consistent with this source.

## Verification

2026-11-05 · S6 verifier, batch b04 (opus; not the writer) · verdict: corrected · checked: loci 9/9 found at the stated PDF pages (quote 1 starts p. 1 and runs to p. 2, as located); metadata vs crossref/openalex (authors per the PDF byline; Crossref gives Pondoc's given name as 'Christopher' only), year, pages 1–19, DOI match; partial depth honest (19-page PDF, parts listed); sha256 matches; four sections in order · changed: Caution: the second interface analysed in §4 is Spellburst, not 'a design-pattern survey' (§4 heading 'Examining the envisioning gap in three LLM interfaces'; §4.2 'Creative Coding using Spellburst')
