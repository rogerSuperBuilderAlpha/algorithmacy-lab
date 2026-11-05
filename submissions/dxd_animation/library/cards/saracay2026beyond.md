---
key: saracay2026beyond
apa: "Saracay, I., Schmidt, L., & Guestrin, C. (2026). *Beyond expert users: Agents should help users construct preferences, not just elicit them* (arXiv:2606.30863v2). arXiv. https://doi.org/10.48550/arXiv.2606.30863"
authors: "Saracay, Irena; Schmidt, Ludwig; Guestrin, Carlos"
year: 2026
title: "Beyond expert users: agents should help users construct preferences, not just elicit them"
venue: "arXiv preprint (marked 'Preprint. Under review.')"
volume: ""
issue: ""
pages: ""
doi: "10.48550/arxiv.2606.30863"
url: "https://arxiv.org/abs/2606.30863"
type: preprint
facets: [F5]
claims: [c1]
role: support
load: load-bearing
read_depth: partial
object_read: "arXiv 2606.30863v2 (cs.AI, 1 Jul 2026), 61 pages; local copy ~/iit-playground/dxd_animation_local/pdfs/saracay2026beyond/saracay2026beyond.pdf, text layer saracay2026beyond.txt, registry record csl.json; original URL https://arxiv.org/pdf/2606.30863 (FETCH_LOG.tsv row saracay2026beyond); read 2026-11-05; sha256 5b98d6da00e3786d38e8383679a3627595690f07bec4f428dc822b969e1c8a6e"
verified: corrected
verified_against: "arXiv 2606.30863v2 PDF and its .txt layer, csl.json, openalex.json; sha256 recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Partial read. Read in full: the abstract and the 12-page main text (sections 1 to 6, printed pages 1 to 12), including Tables 1 to 4 and the figure captions. Not read: the acknowledgements, the reference list, and the appendices (A to G, printed pages 19 to 61: human-study detail, dataset construction, user-simulator and agent prompts, extra results, transcripts, extra related work). I saw only the appendix headings.

Saracay, Schmidt and Guestrin say that LLM agents and the benchmarks that test them assume an expert user, one who "can specify their preferences fully when pressed" (p. 1). They argue that real users often lack the domain knowledge to hold such preferences, so an agent that only asks clarifying questions cannot help. The agent has to teach: show examples and give explanations that let the user form a preference they did not have.

They model this as CoPref. A user has a preference state, the set of features they have formed a preference over, and it starts sparse and grows with what the agent says (p. 3). Following the Search-Experience-Credence typology from information economics, they split features by what the user needs to form a view: a question suffices for search features, example items for experience features, an explanation for credence features (p. 4). A small human study (n = 25, clothing shopping) supports the model: every participant asked for examples or an explanation on at least one feature, and the share of such requests followed by a stated preference was 85 percent for examples and 75 percent for explanations (p. 5). They then build CoShop, a shopping benchmark with simulated CoPref users, and test five frontier models. No model exceeds 56 percent team accuracy in any domain (p. 3), and no model recovers more than 54 percent of the user's preferences (p. 9). The failure lies in how little the conversation teaches the user. Search ability is not the problem. Giving the agent the user's history does not help much, while richer item descriptions help (p. 10).

## What the paper uses it for

- c1: an agent-side statement of constructed preference. Saracay and colleagues say users build preferences during the interaction, drawing on Bettman et al. (1998) and Fischhoff (1991) (p. 3), and that agents built for an expert user fail. The paper can cite them for "what the user wants is formed during the dialogue, and an agent that treats it as fixed performs badly", with a number from the benchmark.
- c1, where the use stretches the source: CoPref does not move the goal. It states that the user has "some latent target item" in mind and that preferences follow from the target's feature values (p. 3). The user only becomes aware of more features of a target that stays put. The authors say real construction "may be more iterative and less stable than this model assumes" and that CoPref assumes preferences are "stable and never forgotten" (p. 6). So the source supports "preference is constructed" and cuts against the strong version of the paper's c1, a goal that changes (raincoat to umbrella). The paper should cite it for the first and not for the second.
- The result is simulated: users are gpt-oss-120b conditioned on a preference state, and the dialogue-action parsing has 74 percent accuracy on questions (p. 8). Human users appear only in the n = 25 validation study. The paper should not cite the 56 percent figure as a measure of human behaviour.

## Loci

Quotations are verbatim. Where the source uses double quotation marks inside a quoted passage, I changed them to single quotes. Locators are the page numbers printed in the preprint, which match the PDF page counted by form feeds. Each line was matched against the local .txt text layer.

- "Failures stem not from agents’ ability to find items, but from how little the interaction expands what users know about what they want." — p. 1, abstract. Matched against the local .txt.
- "A quiet assumption underlying most such systems — and the interactive benchmarks that evaluate them — is that agents are interacting with expert users: users who can specify their preferences fully when pressed" — p. 1, §1. Matched against the local .txt.
- "We assume the user has some latent target item" — p. 3, §2. Matched against the local .txt.
- "preferences are not pre-formed and waiting to be retrieved — they are constructed through interaction, shaped by what the user encounters and learns from the agent" — p. 3, §2. This is the authors' report of Bettman et al. (1998) and Fischhoff (1991). Matched against the local .txt.
- "We recruited n = 25 participants for a simulated clothing shopping task." — p. 5, §2.1. Matched against the local .txt.
- "Real preference construction may be more iterative and less stable than this model assumes" — p. 6, §2.2. Matched against the local .txt.
- "once formed, preferences are stable and never forgotten" — p. 6, §2.2. Matched against the local .txt.
- "no model recovers more than 54% of the user’s preferences over the course of the conversation" — p. 9, §4.2. Matched against the local .txt.
- "a well-informed user is a better selector than the original agent" — p. 10, §4.2. Matched against the local .txt.

## Caution

- This is a preprint marked "Preprint. Under review." Crossref has no record, and the DOI is an arXiv DOI. The result, version and numbers may change in review. The card pins v2 (1 Jul 2026).
- The triage row quotes the abstract's "typically assume an expert user -- one with well-formed preferences" and calls the assumption "unrealistic". Both are in the abstract (p. 1) and the csl.json record. The abstract's "no frontier agent exceeds 56% accuracy" agrees with the body's "No model exceeds 56% on any domain" (p. 3). The introduction also gives claude-sonnet-4.6 at 94.3 percent with fully specified preferences and 27.6 percent after five turns (p. 3). The text on p. 9, reporting Figure 4A, gives gpt-5.2 at 27.7 percent in a related condition, so the headline numbers depend on the condition. The paper should name the condition when it quotes a number.
- Domains are fashion (H&M), films (MovieLens) and books (Goodreads) (p. 7). Nothing in the main text concerns decision interfaces outside recommendation. The authors list extending CoPref beyond recommendation as future work (§6).
- One author name differs across records. The preprint prints "Irena Saracay, Ludwig Schmidt, and Carlos Guestrin" (p. 1), matching csl.json. The triage row uses initials only.
- Claim fit: it is also a candidate prior-work check for c9 (G may want it near the gap claim), because it frames agent design around constructed preference. It does not frame interfaces as animation.

## Verification

2026-11-05 · S6 verifier, batch b04 (opus; not the writer) · verdict: corrected · checked: loci 9/9 found at the stated pages; numbers in body checked (n = 25, 85/75 %, 56 %, 54 %, 74.0 % parsing, 94.3/27.6 %, Appendix A at p. 19); metadata vs csl.json/openalex (authors, 2026, title, arXiv DOI) match; partial depth honest; sha256 matches; four sections in order · changed: object_read and What it argues: page count 62 → 61 (pdfinfo; last printed page 61); Caution: the 27.7 % gpt-5.2 figure comes from the p. 9 text on Figure 4A, not from Table 3
