---
key: shanahan2023role
apa: "Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role play with large language models. *Nature*, *623*(7987), 493–498. https://doi.org/10.1038/s41586-023-06647-8"
authors: "Shanahan, Murray; McDonell, Kyle; Reynolds, Laria"
year: 2023
title: "Role play with large language models"
venue: "Nature"
volume: "623"
issue: "7987"
pages: "493–498"
doi: "10.1038/s41586-023-06647-8"
url: ""
type: article
facets: [F3, G]
claims: [c4, c7, c9]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "Publisher PDF of the Nature Perspective (open, bronze), 6 pages with journal pagination 493–498; local folder ~/iit-playground/dxd_animation_local/pdfs/shanahan2023role/ (shanahan2023role.pdf and .txt); original URL https://www.nature.com/articles/s41586-023-06647-8.pdf (FETCH_LOG.tsv records it with a cookie-check query string); read 2026-11-05; sha256 a2d447b85abd5c9e3630b6a4b682d0daccd90fbe48b67cff6a6d49e1e9e218b2"
verified: corrected
verified_against: "shanahan2023role.txt (publisher PDF, page-split by form feed); crossref.json; openalex.json; FETCH_LOG.tsv; sha256 of shanahan2023role.pdf recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Murray Shanahan, Kyle McDonell and Laria Reynolds want a way to talk about LLM dialogue agents in everyday psychological terms without falling into anthropomorphism. They offer role play. A dialogue prompt, invisibly prepended to the conversation, sets a character, and the model does its best to continue as that character (p. 493). They add a second metaphor: the model is a 'simulator' that keeps a superposition of possible characters ('simulacra') and does not commit to one (pp. 494–495). They apply the frame to apparent deception, where the agent can confabulate, speak 'in good faith' from stale data, or role-play a deceptive character (pp. 496–497), and to apparent self-preservation, where 'no-one at home' stands behind the words (p. 497).

The authors say the role-play metaphor is 'not a perfect fit', because the agent is closer to an improvising performer than to an actor in a scripted play (p. 494). Their parties are the user, the character the model plays, the underlying simulator, and the designers or companies that set the prompt and fine-tune the model (pp. 494, 496). They treat the simulator as passive with no agency of its own, and they do not describe any party standing behind the character with interests that act on the user. They do not mention animation.

## What the paper uses it for

- c4 (an LLM interface is an animation): Shanahan et al. give the closest non-animation statement of c4, a chatbot read as a character that something else voices. This is the rival frame the paper has to answer. It is a stretch to say the source supports the animation reading; the authors choose theatre and simulation, and use the word 'role play' for a purpose the paper's frame does not share, which is to keep users from ascribing human traits.
- c7 (animation is triadic: viewer, character, animator): the source offers a user, a character and a simulator, which looks triadic. But the simulator 'has no agency of its own' (p. 496), unlike an animator who decides frames to produce an effect on a viewer. The source also names designers who prompt and fine-tune (pp. 494, 496) without making them a modelled party. The paper can use this as a contrast: role play yields a character and a passive generator, and the work of an author-animator drops out.
- c9 (gap: no prior work frames LLM interfaces as animation for decision design): the source is a prior performance frame for LLM dialogue, and it does not use animation or address decisions. It supports the gap claim only in the narrow sense that a closely related frame exists and does not take the animation route. It is not evidence that no one has made the animation argument.

## Loci

Quotations are verbatim; inner quotation marks are rendered as single quotes. Locator: journal pagination printed in the footer of each page (Nature 623, 493–498). Matched against: shanahan2023role.txt (publisher PDF).

- "As dialogue agents become increasingly human-like in their performance, we must develop effective ways to describe their behaviour in high-level terms without falling into the trap of anthropomorphism." — abstract, p. 493 — publisher PDF.
- "we can see a dialogue agent as role-playing a single character" — p. 493 — publisher PDF.
- "we can see a dialogue agent as a superposition of simulacra within a multiverse of possible characters" — p. 493 — publisher PDF.
- "the dialogue prompt that is invisibly prepended to the context before the actual dialogue with the user commences" — p. 493 — publisher PDF.
- "This allows the user, deliberately or unwittingly, to coax the agent into playing a part quite different from that intended by its designers." — p. 494 — publisher PDF.
- "However, the role-play metaphor, while intuitive, is not a perfect fit." — p. 494 — publisher PDF.
- "The dialogue agent is more like a performer in improvisational theatre than an actor in a conventional, scripted play." — p. 494 — publisher PDF.
- "As for the underlying simulator, it has no agency of its own, not even in a mimetic sense." — p. 496 — publisher PDF.
- "With an LLM-based dialogue agent, it is role play all the way down." — p. 496 — publisher PDF.
- "There is, however, 'no-one at home', no conscious entity with its own agenda and need for self-preservation." — p. 497 — publisher PDF.

## Caution

- OpenAlex types the work 'review' and Crossref 'journal-article'; the PDF heads it 'Perspective'. The card uses type article.
- Triage F3 quoted the abstract from a Semantic Scholar record; the abstract here is the one on the Nature PDF, checked against it.
- Shanahan's later 'Talking about large language models' (Communications of the ACM) overlaps; it is not carded separately (triage note).
- The role-play frame is Shanahan's attempt to avoid anthropomorphism for explanation, not a design proposal. The paper should not describe it as rejected by the authors or as an account of interface design.
- The authors focus on base models before fine-tuning (p. 494). They say the simulator–simulacrum distinction is starkest for base models (p. 495) but that the role-play framing still applies after fine-tuning (p. 496).
- The reference list was scanned, not read in detail.

## Verification

2026-11-05 · S6 verifier, batch b02 (opus; not the writer) · verdict: corrected · checked: loci 10/10 found on the stated pages; metadata vs crossref (authors, title, Nature 623(7987) 493–498, 2023, journal-article, DOI) and openalex (review, bronze OA) match; depth full_text honest; sha256 matches · changed: deception locator p. 496 → pp. 496–497; rewrote the fine-tuning Caution line, which said fine-tuned systems 'differ' where the authors say the framing still applies (pp. 494–496)

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 10/10 loci found in shanahan2023role.txt (two-column layer, columns interleaved) on the stated pages, confirmed by the printed footers 493–497; frontmatter vs crossref.json and openalex.json (Shanahan, McDonell, Reynolds; Nature 623(7987), 493–498; online 2023-11-08, print 2023-11-16; DOI); sha256 recomputed; full_text depth honest; the c4/c7/c9 contrast uses follow the source and name the passive-simulator point with its locus.
- Changed: nothing.
- For the author: nothing.
