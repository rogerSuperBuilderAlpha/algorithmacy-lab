---
key: bhat2025dynamic
apa: "Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *30th International Conference on Intelligent User Interfaces (IUI '25)* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131"
authors: "Bhat, Maalvika"
year: 2025
title: "How Dynamic vs. Static Presentation Shapes User Perception and Emotional Connection to Text-Based AI"
venue: "IUI '25"
volume: ""
issue: ""
pages: "846–860"
doi: "10.1145/3708359.3712131"
url: ""
type: proceedings
facets: [F3, F4]
claims: [c4, c5]
role: support
load: load-bearing
read_depth: full_text
object_read: "ACM published PDF (IUI '25, 15 pages, CC BY 4.0 as printed on p. 846) and its text layer; local folder ~/iit-playground/dxd_animation_local/pdfs/bhat2025dynamic/ ('Bhat 2025 - Dynamic vs static presentation.pdf', bhat2025dynamic.txt); provenance.txt records a copy of the lab-held file in the spaces repo, with no web URL; the PDF prints https://doi.org/10.1145/3708359.3712131; read 2026-11-05; sha256 714377dced73385ff18a1707e44672d6a8c568cbb173a32336599ac32927dc18 (PDF)"
verified: verified
verified_against: "PDF text layer re-extracted with pdftotext and page-mapped by form feed from p. 846; ACM reference format and DOI printed on p. 846 (no crossref/openalex record in the folder); provenance.txt; sha256 of PDF recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Bhat asks how the way a text chatbot shows its answer changes what users think of it. In a within-subjects experiment (N = 103 non-technical adults) each participant used GPT-3.5 Turbo in two sessions: a "dynamic" mode with a simulated typing display and a "static" mode where the whole answer appeared at once after submission (§3). The dynamic mode used "a simulated typing delay, which typically ranged from 2–3 seconds per sentence" (§3.1, p. 849). After each session participants rated the AI on 16 dimensions. Dynamic presentation scored higher on competence, warmth, trustworthiness, engagement, adaptive behaviour, supportiveness, personal connection, empathy, bias awareness, accountability, emotional expressiveness, transparency and persuasiveness. It made no significant difference to perceived effectiveness, bias or learning support (Table 2, p. 853). Bhat reads the pattern as users treating real-time typing as a sign of thought and presence. Bhat also warns of over-attribution, over-reliance and manipulation, recommends transparency cues and user control over the mode, and suggests static display may suit high-stakes uses (§5.2, pp. 853–856).

## What the paper uses it for

- **c4** (an LLM interface is an animation): Bhat describes the typing display as something that "mimics the illusion that someone is typing in real-time" and compares it to gradual text reveal in video-game dialogue with non-player characters (§5.3, p. 857). That puts a staged reveal inside the character-making of the interface, which is the paper's point. It stretches the source: Bhat uses the language of anthropomorphism and presence, not animation, and no animation scholarship appears.
- **c5** (animation is opaque: missing frames; the interstices are the craft): the study varies only whether text arrives frame by frame or all at once, and shows that the frames change perceived character even though perceived effectiveness stays flat. This supports "the stream's frames are doing work". It stretches the source: the typing display is a simulated delay of 2–3 seconds per sentence, not token pacing, and Bhat does not talk about what is hidden between frames. Several of Bhat's mechanisms ("signals deliberation") are interpretations, not measurements (see Caution).

## Loci

No inner quotation marks were converted. Locators are the proceedings page numbers printed in the page headers and footers (p. 846 is the first page). Each quotation was matched against the PDF's text layer (the PDF, extracted with pdftotext, and the .txt layer).

- "dynamic interactions improved perceptions of AI's competence, warmth, trustworthiness, engagement, adaptive behavior, supportiveness, personal connection, empathy, bias awareness, accountability, and emotional expressiveness" — Abstract, p. 846 — PDF text layer.
- "no significant differences were found in perceived effectiveness, bias, and learning support" — Abstract, p. 846 — PDF text layer.
- "In the first session, participants interacted with GPT-3.5 Turbo in a dynamic presentation mode, where the AI typed responses in real-time." — §3.1, p. 849 — PDF text layer.
- "Group A experienced the dynamic presentation mode first, followed by the static mode, while Group B experienced the static mode first" — §3.1, p. 849 — PDF text layer.
- "AI responses were displayed to mimic real-time typing" — §3.1, Interface Description, p. 849 — PDF text layer.
- "This mode involved a simulated typing delay, which typically ranged from 2–3 seconds per sentence, creating the impression that the AI was actively formulating its responses." — §3.1, p. 849 — PDF text layer.
- "where AI responses were displayed with all text appearing at once after the user submitted their input" — §3.1, p. 849 — PDF text layer.
- "participants who experienced dynamic presentations first rated static presentations slightly lower on engagement (F = 3.12, p = 0.041)" — §4, p. 852 — PDF text layer.
- "Real-time typing appeared to signal deliberation and thoughtfulness, leading users to perceive the AI as more knowledgeable and reliable" — §5.1.1, p. 852 — PDF text layer.
- "Static formats reduce the risk of anthropomorphism and emotional manipulation" — §5.2, p. 854 — PDF text layer.
- "the dynamic presentation of AI doesn't fully replicate real-time human conversation; rather, it mimics the illusion that someone is typing in real-time, fostering a sense of presence and thoughtfulness." — §5.3, p. 857 — PDF text layer.
- "GPT-3.5 Turbo may generate different responses to the same prompts across dynamic and static conditions, which could have influenced participants' perceptions independently of the presentation mode" — §5.5, p. 858 — PDF text layer.

## Caution

- Procedure inconsistency. §3.1 says that in the first session participants used the dynamic mode and in the second the static mode, then says they were randomly split into Group A (dynamic first) and Group B (static first) (p. 849). Both cannot hold. I report the text as printed and did not resolve it. The order effect the paper reports (p. 852) was on engagement only.
- Confounds the author lists or the design leaves open. The static mode was "specially developed", so the two interfaces differ in more than display; GPT-3.5 Turbo may have produced different answers in the two sessions (p. 858). Bhat's ANOVA results carry F and p values but no degrees of freedom, and the means, t-tests and Cohen's d appear in figures (Figures 2 to 4), which are not in the text layer. I did not see them.
- The mechanism is interpretation. "Real-time typing appeared to signal deliberation" is not measured; no item asks participants why they rated as they did. The same holds for "static formats reduce the risk of anthropomorphism", which no part of the study tests, and for the section on search engines and customer bots (§5.4), which extends the findings beyond the tasks used.
- Pairing with Anderl et al. (2024), another card in this batch. The triage note joins Bhat's trust result to Anderl's discernment result. Bhat measured perceptions after a conversation task with a live typing display; Anderl measured credibility judgements of planted errors after watching screencasts. The two do not measure the same thing, and Bhat reports no discernment measure.
- Pace is not the variable. The typing delay was 2–3 seconds per sentence and the static mode had no incremental reveal, so the study cannot say how typing speed or token pacing would matter.
- Persuasiveness is analysed and reported (Table 2, F = 76.8881) but does not appear in the abstract's list.
- Read depth: I read the whole body (pp. 846–858) and the conclusion. I skimmed the reference list (pp. 858–860) only.

## Verification

2026-11-05 · S6 verifier, batch b03 (opus; not the writer) · verdict: verified · checked: loci 12/12 found verbatim, all page and section locators correct (§3.1, §4, §5.1.1, §5.2, §5.3, §5.5 confirmed); Table 2 on p. 853 lists 16 dimensions, 13 significant, persuasiveness F = 76.8881; the session-order contradiction in §3.1 confirmed; NPC comparison on p. 857 confirmed ("non-playable characters"); author, 2025, title, IUI '25, 15 pages (pp. 846–860) and DOI match the printed ACM reference format; no registry JSON in the folder; read_depth full_text supported; sha256 714377… of the PDF recomputed and matches provenance.txt · changed: nothing
