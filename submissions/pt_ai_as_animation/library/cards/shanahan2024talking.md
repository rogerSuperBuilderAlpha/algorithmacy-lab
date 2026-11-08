---
key: shanahan2024talking
apa: "Shanahan, M. (2024). Talking about large language models. *Communications of the ACM, 67*(2), 68–79. https://doi.org/10.1145/3624724"
authors: "Shanahan, Murray"
year: 2024
title: "Talking about Large Language Models"
venue: "Communications of the ACM"
volume: "67"
issue: "2"
pages: "68–79"
doi: "10.1145/3624724"
url: ""
type: article
facets: [F11]
claims: [c10, c5]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "arXiv v5 (arXiv:2212.03551v5 [cs.CL], dated December 2022, revised 16 Feb 2023; 13 pp.), an author preprint, NOT the Communications of the ACM text of Feb 2024; and its text layer shanahan2024talking.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/shanahan2024talking/; fetched from https://arxiv.org/pdf/2212.03551 (FETCH_LOG.tsv, route openalex_location_pdf); no copy in inbox/; read 2026-11-08; sha256 bed3a50fc04e0bedf02193e508be2e6415079dd74386c9a87481bffe185304de (PDF, from sha256.txt). Read in full: PDF pp. 1–11 (abstract to conclusion). Not read: the reference list, pp. 11–13."
verified: corrected
verified_against: "crossref.json, openalex.json; sha256 re-hashed; per-page pdftotext (raw and layout) of the arXiv v5 PDF, 14 quotations traced (all verbatim; one section locator corrected); section numerals read from the layout text"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# M. Shanahan (2024), Talking about large language models

## What it argues

Murray Shanahan argues that people, and developers in particular, should keep in view what a large language
model actually does before they describe it in words like "knows", "believes" and "thinks". The bare model
is a generative mathematical model of the distribution of tokens in a large human-written corpus; asking
it a question amounts to asking which words are likely to follow a given text (§2). Shanahan separates the
"bare-bones" LLM (architecture plus trained parameters) from the dialogue system built around it, which
needs a larger system to take turns and a hidden prompt prefix to produce conversation (§4). He grants
that the intentional stance is harmless shorthand when everyone knows it is shorthand (§3), and he says
the paper does not claim that a system built on an LLM could never warrant such descriptions.

He then tests the stance against several cases. A bare model does not hold beliefs, because it has no
access to an external reality or to the means of judging truth (§§5–6). Adding external information
sources, vision-language models, or an embodied robot (SayCan) does not by itself change the verdict (§§7–9).
Reasoning from few-shot prompts is pattern completion, with no guarantee that it preserves truth (§§10–11).
Fine-tuning with human feedback leaves "a model of the distribution of tokens in human language, albeit one
that has been slightly skewed" (§12). His conclusion is that LLM-based agents give "a compelling illusion
of being in the presence of a thinking creature", that the shared "form of life" behind human trust is
absent, and that we should "resist the siren call of anthropomorphism" until new language has settled.

## What the paper uses it for

- **c5** (the intelligence frame versus the life frame is a stance choice): Shanahan hands the paper the
  vocabulary for this, because he names the intentional stance and treats talk of belief as a choice of
  description that carries consequences. He is also a contrast source, and here is what he would object
  to. He says the stance is safe only while users and developers hold it as shorthand, and that for LLMs
  "such licence can no longer safely be applied" (p. 11), since the systems are "so convincingly intelligent".
  A paper that asks developers to adopt a life frame, with animation as its craft, invites the
  anthropomorphism he warns against. The paper has to say either that animation's frame is held knowingly
  as a craft stance, which fits his shorthand condition, or that it differs in kind. His own remedy
  (repeatedly stepping back to recall how the systems "actually work", p. 1) is a competing discipline.
  Stretch: Shanahan has no account of life, only of belief, knowledge and reasoning, so "life frame" is
  the paper's extension.
- **c10** (the analogy breaks at liveness; the LLM makes its own in-betweens): Shanahan gives the plainest
  statement of what the LLM does at each step, namely pattern completion over a prompt (§§11–12). That is
  usable for the "makes its own in-betweens" half. His §4 also describes the hidden prompt prefix that
  scripts a dialogue and the choice of a play-script pattern ("numerous plays and film scripts", p. 4). That
  is a mechanism for the paper's system-prompt-as-key-pose mapping. He would object to any move from
  "in-betweens" to liveness: in his account the model has no communicative intent, no beliefs, and no
  stake in a shared world (pp. 4–6). The analogy "breaks at liveness" is therefore something he would
  accept, but he would resist the claim that the break is bridged by treating the system as alive.
  Stretch: he does not discuss puppetry, animation or liveness at all.
- Unlabelled by claim but relevant to **c1/c2** (the author may add them): his §2 and §4 separate the bare
  model from the system and warn that "large language model" is used for both. That is the model/system
  distinction the thesis depends on. He also writes that "what counts most" is "not so much the process by
  which it is produced ... but the nature of the final product" (p. 11), a direct counter to a paper that
  puts the making at the centre.

## Loci

Matched against shanahan2024talking.txt (arXiv v5 PDF text layer; ligatures such as "fi" were normalised).
Page numbers are the arXiv PDF's (13 pages), not the CACM pagination 68–79. Sections are located by their
heading; the PDF prints numerals §1–§13 (see Verification). Inner quotation marks are single quotes.

- p. 1, Abstract: "But it is a serious mistake to unreflectingly apply to AI systems the same intuitions that we deploy in our dealings with each other"
- p. 1, Abstract: "To mitigate this trend, this paper advocates the practice of repeatedly stepping back to remind ourselves of how LLMs, and the systems of which they form a part, actually work."
- p. 2, What LLMs Really Do: "The bare-bones LLM itself, the core component of an AI assistant, has a highly specific, well-defined function, which can be described in precise mathematical and engineering terms."
- p. 3, LLMs and the Intentional Stance: "These examples of what Dennett calls the intentional stance are harmless and useful forms of shorthand for complex processes whose details we don’t know or care about."
- p. 3, LLMs and the Intentional Stance: "To be clear, it is not the argument of this paper that a system based on a large language model could never, in principle, warrant description in terms of beliefs, intentions, reason, etc."
- p. 4, Humans and LLMs Compared: "First, it’s worth noting that a bare-bones LLM is, by itself, not a conversational agent."
- p. 4, Humans and LLMs Compared: "A more likely pattern, given that numerous plays and film scripts feature in the public corpus, would be something like the following."
- p. 4, Humans and LLMs Compared: "In the background, the LLM is invisibly prompted with a prefix along the following lines."
- p. 4, Do LLMs Really Know Anything?: "at the heart of every such application is a model doing just that one thing: generating statistically likely continuations of word sequences."
- p. 6, External Information Sources: "It is only with respect to the whole system that the intentional stance becomes more compelling in such a case."
- p. 10, What about Fine-Tuning?: "The result is still a model of the distribution of tokens in human language, albeit one that has been slightly skewed."
- p. 11, What about Fine-Tuning?: "what counts most when we think about the functionality of a large language model is not so much the process by which it is produced (although this is important too) but the nature of the final product."
- p. 11, Conclusion: "Interacting with a contemporary LLM-based conversational agent can create a compelling illusion of being in the presence of a thinking creature like ourselves."
- p. 11, Conclusion: "Meanwhile, we should try to resist the siren call of anthropomorphism."

## Caution

- **Version.** The copy is the arXiv v5 preprint (Feb 2023). The Crossref record gives *Communications of
  the ACM* 67(2), pp. 68–79, published online 2024-01-25. The journal text may differ in structure,
  wording and section numbers. All locators here are arXiv PDF pages; none is a CACM page. A verifier must
  relocate each quotation in the version of record before the paper cites page numbers, and DECISIONS
  routed this key to the ACM DL PDF, which was not the file fetched.
- **Homonym with another Shanahan work.** SKETCH names Shanahan, McDonell and Reynolds (2023), "Role play
  with large language models", *Nature*, for the claim that dialogue agents are best described as
  role-playing characters. That is a separate paper. The arXiv v5 text read here contains no role-play
  section, and the character claim must not be cited to this card.
- **Section map.** [Corrected by the S6 verifier.] The PDF prints section numerals (the layout text layer
  keeps them): §1 Introduction, §2 What LLMs Really Do, §3 LLMs and the Intentional Stance, §4 Humans and
  LLMs Compared, §5 Do LLMs Really Know Anything?, §6 What About Emergence?, §7 External Information
  Sources, §8 Vision-Language Models, §9 What About Embodiment?, §10 Can Language Models Reason?, §11 How Do
  LLMs Generalise?, §12 What about Fine-Tuning?, §13 Conclusion: Why This Matters. These are arXiv v5
  numerals; the CACM text may number differently.
- **Scope.** Shanahan writes about belief, knowledge, reasoning and anthropomorphism. He says he takes no
  position on meaning (fn. 6) or on any particular account of belief (fn. 3). He offers no account of
  liveness.
- **What the paper may not claim from it:** that Shanahan endorses a stance or frame for development
  work other than the shorthand he permits; that he discusses animation, puppetry or characters; the
  role-play claim.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 4
- verdict: corrected
- checked: frontmatter against crossref.json and openalex.json (Murray Shanahan; *Communications of the
  ACM* 67(2), pp. 68–79, online 2024-01-25, print Feb 2024, so year 2024; title; DOI; journal-article);
  sha256 of the PDF matches sha256.txt; all 14 quotations found verbatim on the stated arXiv pages, and
  each one placed against the two-column layout to check its section; the quotations behind the c5, c10
  and c1/c2 bullets ("no longer safely", "so convincingly intelligent", "form of life", p. 11; the
  "large language model" used for both models and systems, p. 2; fn. 6 on meaning, p. 4; the belief
  disclaimer with fn. 3, p. 3). read_depth full_text is honest for the arXiv text; the version caution
  stands, since no locus is checked against the CACM version of record.
- changed: (1) The p. 6 quotation "It is only with respect to the whole system ..." sits in the right
  column after the §7 heading, so its locator now reads "External Information Sources", not "What About
  Emergence?". (2) The writer said the text layer drops section numerals; the layout text shows them, so
  the §-references in What it argues were off by one in places: external sources, VLMs and embodiment are
  §§7–9 (not §§7–10), reasoning and few-shot pattern completion §§10–11 (not §§11–12), fine-tuning §12 (not
  §13). Corrected those, the Loci preamble, and the Caution "Section map" entry (now lists the printed
  numerals and headings).

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 14/14 loci found by per-page pdftotext of the arXiv v5 PDF (the .txt layer interleaves columns; sha256 recomputed, matches); the p. 11 phrases behind the c5 bullet ('no longer safely be applied', 'so convincingly intelligent') also found; frontmatter vs crossref.json and openalex.json (CACM 67(2), 68–79); claim uses, with the named stretches (no account of life, puppetry or liveness).
- Changed: nothing
- For the author: status is `cited`, but SKETCH.md names only Shanahan, McDonell & Reynolds (2023, *Nature*), a different paper; under README this card would be `candidate` unless the Checkpoint B approval counts as a ruling. All locators are arXiv pages, not CACM pages, as the card says
