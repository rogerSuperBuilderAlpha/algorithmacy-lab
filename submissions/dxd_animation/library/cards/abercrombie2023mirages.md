---
key: abercrombie2023mirages
apa: "Abercrombie, G., Cercas Curry, A., Dinkar, T., Rieser, V., & Talat, Z. (2023). Mirages. On anthropomorphism in dialogue systems. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (pp. 4776–4790). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-main.290"
authors: "Abercrombie, Gavin; Cercas Curry, Amanda; Dinkar, Tanvi; Rieser, Verena; Talat, Zeerak"
year: 2023
title: "Mirages. On Anthropomorphism in Dialogue Systems"
venue: "EMNLP 2023"
volume: ""
issue: ""
pages: "4776–4790"
doi: "10.18653/v1/2023.emnlp-main.290"
url: "https://aclanthology.org/2023.emnlp-main.290.pdf"
type: proceedings
facets: [F3]
claims: [c4, c8]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "ACL Anthology published PDF (EMNLP 2023 main-conference paper, 15 pages) and its text layer; local folder ~/iit-playground/dxd_animation_local/pdfs/abercrombie2023mirages/ (abercrombie2023mirages.pdf, .txt, crossref.json, openalex.json); original https://aclanthology.org/2023.emnlp-main.290.pdf (FETCH_LOG.tsv); read 2026-11-05; sha256 30e1a49b23ddd63b7677e77324d10abde6de86ba7e73d216ad231b9935b765ab (PDF)"
verified: verified
verified_against: "text layer re-extracted with pdftotext and page-mapped by form feed; crossref.json; openalex.json; sha256 of PDF recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Abercrombie, Cercas Curry, Dinkar, Rieser and Talat write a position paper. They argue that developers anthropomorphise dialogue systems and users personify them, and that design choices decide how far this goes. The authors name the problem "gratuitous" anthropomorphic features: cues that make a system seem human without any need for them. They sort the cues into voice, content (answers to "are you human?", claims of thought, empathy, activities, pronouns), register and style, and roles (§3). They list harms: misplaced trust and over-reliance, gendered stereotypes, and the erasure of marginalised language varieties (§4). Their recommendations (§5) are to recognise people's tendency to personify, to ask which anthropomorphic tools suit a given use, to reassess research goals, and to stop describing systems in anthropomorphic terms. The authors say plainly that avoiding cues does not remove the tendency: people may personify a system anyway. They also note that the paper "could also be used as a guide to creating anthropomorphic systems". The paper treats the personifying user as the problem to design around. It has no theory of animation and uses "animated" once, for the three dots in ChatGPT.

## What the paper uses it for

- **c4** (an LLM interface is an animation): the paper can cite Abercrombie et al. for the claim that the character the user meets is partly built by the interface and that interface timing is one of its cues. The text names "ChatGPT's animated 'three dots' and word-by-word staggered outputs" as cues that the system is thinking (p. 4778). That is a passing remark taken from a news item, not a tested claim, and the paper never frames the interface as animation. This stretches the source: the animation reading is the author's.
- **c8** (DXD applies the animator's methods rather than hiding frames or exposing the backend): Abercrombie et al. state the opposing design stance, which §5 needs: reduce or choose carefully among the cues that make the character, and describe systems without human terms. The source cuts against any simple reading of "damp the character" as a fix, because the authors concede that people personify systems even when developers avoid every cue (p. 4784), and they argue for choosing cues by context, not for removing them all (p. 4783). The contrast with the animator's method is therefore narrower than a flat "reduce versus work with" opposition.
- Possible but not approved: **c6** (the viewer locks in). The authors' point that people reflexively attribute meaning and personify without being asked (pp. 4777, 4783) fits a lock-in reading. DECISIONS lists only c4 and c8 for this card.

## Loci

Quotation marks inside quotations are already single quotes in the source or were converted to single quotes. Locators are the proceedings page numbers printed on the page. Each quotation was matched against the PDF's text layer (abercrombie2023mirages.pdf, extracted with pdftotext, and the .txt layer).

- "conscious and unconscious design choices can guide users to personify such systems to varying degrees" — Abstract, p. 4776 — PDF text layer.
- "Encouraging users to relate to automated systems as if they were human can lead to high risk scenarios caused by over-reliance on their outputs." — Abstract, p. 4776 — PDF text layer.
- "In this position paper, we make a normative argument against gratuitous anthropomorphic features" — §1, p. 4777 — PDF text layer.
- "Research has shown that the process of anthropomorphising is mostly mindless" — §2.1, p. 4777 — PDF text layer.
- "ChatGPT's animated 'three dots' and word-by-word staggered outputs, which give an impression that the system is thinking" — §3, p. 4778 — PDF text layer. (The source prints 'three dots' in single quotes. The authors cite a news item, Venkatasubramonian in Goldman 2023, for it.)
- "designers should recognise people's tendency to personify, consider which, if any, anthropomorphic tools are appropriate" — §5, p. 4783 — PDF text layer.
- "it is infeasible to comprehensively map which linguistic cues to use or avoid" — §5, p. 4783 — PDF text layer.
- "Even if developers and designers attempt to avoid including any anthropomorphic signals, humans may still personify systems and perceive them as anthropomorphic entities." — §6 Conclusion, p. 4784 — PDF text layer.
- "it could also be used as a guide to creating anthropomorphic systems" — Ethical Considerations, p. 4784 — PDF text layer.

## Caution

- The triage row says the paper holds that "the designer should reduce" the character. The text is narrower: it argues against gratuitous cues and asks designers to weigh which cues are appropriate by context (p. 4783). A card use that says "Abercrombie et al. say damp the character" overstates it.
- The paper is about dialogue systems in general, with a focus on language, voice and pronouns. It reports no experiment of its own and says it does not cover physically embodied robots (§3, note 3). Its claims about harm rest on prior studies it cites, which this card did not read.
- Read depth: I read the whole body (pp. 4776–4784) and the limitations and ethics statements. I skimmed the reference list (pp. 4785–4790) only to confirm it holds nothing else.
- Anderl et al. (2024), a card in this batch, cites this paper as an arXiv preprint (arXiv:2305.09800), as seen in Anderl's reference list; the proceedings version is the one read here.
- Crossref and OpenAlex both give 2023 as the year and pages 4776–4790, matching the printed pagination.
- Author name. Crossref lists the second author as given name "Amanda", family name "Curry", and OpenAlex's raw author string is "Amanda Curry". The paper prints "Amanda Cercas Curry" and OpenAlex's display name agrees, so the card uses Cercas Curry. [Added by the S6 verifier.]

## Verification

2026-11-05 · S6 verifier, batch b03 (opus; not the writer) · verdict: verified · checked: loci 9/9 found verbatim, all page and section locators correct (pages mapped by form feed from p. 4776); "animated" occurs once as claimed; authors, year, title, venue, pages 4776–4790 and DOI match crossref.json and openalex.json; read_depth full_text supported by the 15-page PDF; sha256 30e1a4… of the PDF recomputed and matches sha256.txt and FETCH_LOG.tsv · changed: added one Caution line on the Crossref/OpenAlex raw author string "Amanda Curry" against the printed "Amanda Cercas Curry"
