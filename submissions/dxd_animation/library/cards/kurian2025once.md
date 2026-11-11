---
key: kurian2025once
apa: "Kurian, N. (2025). Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney. *International Journal of Child-Computer Interaction*, *46*, Article 100788. https://doi.org/10.1016/j.ijcci.2025.100788"
authors: "Kurian, Nomisha"
year: 2025
title: "Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney"
venue: "International Journal of Child-Computer Interaction"
volume: "46"
issue: ""
pages: "100788"
doi: "10.1016/j.ijcci.2025.100788"
url: "https://arxiv.org/abs/2504.08670"
type: article
facets: [F12, G2]
claims: [m1, m3, m4, m5, m6, m7]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "version: arXiv submitted version of the article, arXiv:2504.08670, NOT the Elsevier version of record; the arXiv API record fetched the same day lists v3 (updated 15 Aug 2025) as current and links the journal DOI, and the PDF itself carries no arXiv version stamp; 28 PDF pages made from a Google Docs file titled 'Arxiv Preprint Revised.docx'; all pages and section numbers on this card are the arXiv PDF's; place: ~/iit-playground/dxd_animation_local/pdfs/kurian2025once/kurian2025once.pdf (+ .txt, .readorder.txt), fetched with curl from https://arxiv.org/pdf/2504.08670 (provenance.txt); date: 2026-11-11; sha256: ab66164eb28bf0c887ab7eecf10679259dd2fcac57f67baf5c0302abff206403; metadata from crossref.json (sha256 dece88e0c7ff566cb0ab7f033e88e8df69088be13b206dd86af2de3cb02eb67e) and arxiv.xml, both fetched 2026-11-11"
verified: pending
verified_against: ""
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Nomisha Kurian argues that designers of AI for children aged about 2 to 11 should borrow a "design grammar" from children's animation, read through Piaget's stages of development (pp. 1–2). She draws the scope tightly. The paper does not endorse companion-style AI that fosters dependency (p. 1), covers functional AI for "tightly boundaried tasks" such as tutoring agents that children speak, gesture or play with, and excludes "non-interactive AI such as algorithmic recommendation systems" (pp. 1–2). She names the difference between the two media at the start: an animated film is fixed and identical for every viewer, while an AI must interpret ambiguous child input and adapt in real time (p. 2).

Her method is a qualitative reading of films. The paper reports phase one of a 2023–2025 project: a thematic analysis, after Braun and Clarke, of about 70 hours of footage from 52 Walt Disney Animation Studios films made between 1937 and 2021, 37 of them from 1937–1999 and 15 later (pp. 6–7). She built a first codebook in NVivo from a pilot set of 15 films and six child–computer interaction (CCI) works, with codes for expressiveness, narrative structure, audio and music cues, environment and visual style, sidekick dynamics, and play and agency (p. 7). Coding all 52 films refined the codebook, and axial coding grouped the codes into developmental patterns, each read through Piaget and the CCI literature (pp. 7–8). An interdisciplinary group reviewed the preliminary themes and a CCI colleague debriefed the coding; no children took part, and Kurian says the heuristics "require empirical validation" (p. 8). The paper gives no code counts, inter-rater figures or list of coded scenes.

The six scaffolds (listed pp. 2–3, developed in §§4.1–4.6, pp. 9–18, summarised in Table 1, p. 19):

1. **Signals**: bold, readable expressions and gestures with time to read them (slow eye movements, high-contrast posture changes, prolonged gaze, dwell time), and a stable mapping from internal states to visible cues (pp. 2, 9–10).
2. **Sound**: music and audio motifs that anchor attention, carry affect and mark transitions and turn-taking (pp. 2, 11–12).
3. **Synchrony**: consistent voice, movement and music, for "emotional legibility" and comfort (pp. 3, 13–14).
4. **Sidekicks**: a "collaborative, non-hierarchical persona", fallible and humble, rather than a directive instructor, with "selective anthropomorphism" and occasional reminders that the AI is not alive (pp. 3, 14–15).
5. **Storyplay**: generative co-construction of pretend play, bounded by content filtering and caregiver review (pp. 3, 15–17).
6. **Structure**: predictable routines and narrative arcs, with challenge adjusted to the child (pp. 3, 17–18).

Each section pairs Disney examples with a developmental claim and a design implication, and it supports the implication with other authors' child–robot and child–agent studies, not with new data. Her animation source is the finished film as an audience sees it. She names Disney's principles once, "exaggeration, appeal, and staging", citing Tremosa (2024), an Interaction Design Foundation article on applying Disney's twelve principles to UI animation (pp. 9, 26). She cites Johnston and Thomas (1981) once, as the "documented animation techniques" that limited bias (p. 8). Keys, in-betweens, timing charts and the animator's division of labour do not appear.

**Decisions, opacity and a third party, as the text has them.** The word "decision" appears once, for the AI's own "rapid decisions" (p. 2); no child's decision is studied or designed for. Opacity appears as "opaque feedback" in a list of faults of misaligned AI (p. 5), and as "unexplained errors" and cues that make it "difficult for children to interpret AI intentions" (p. 4); she treats it as a legibility problem inside the child–AI pair. The only other parties are caregivers, who set the intensity of cues and the pace of progression and review risky play (pp. 10, 12, 17, 18), and adults who mediate scaffolding (p. 5). No party evaluates or binds the child, and platforms and operators do not appear. On risk, she names over-reliance from anthropomorphic cues (p. 4), overtrust (p. 5), the "omniscient authority" persona (p. 14), privacy, which she handles by in-session adaptation without stored profiles (pp. 10, 12, 18), and unsafe suggestions in pretend play (p. 17).

## What the paper uses it for

- **m7 and G2 (contrast; narrows the gap).** Kurian is the closest prior work the library holds: she turns animation into design heuristics for AI, and she selects techniques through an account of the receiver, the child's Piagetian stage. A claim that no prior work turns animation into AI design guidance would therefore be false, and m7 must cite her. The gap survives in narrower form. She selects by developmental need (attention, comprehension, emotional comfort), not by decision competency; the child's decision never appears; her setting is a dyad of child and tutoring AI with caregivers adjusting settings; she excludes recommender systems (p. 2); and her craft source is finished Disney films plus a UI-animation web article, not the animator's working methods.
- **m4 (support, and a limit on novelty).** Her warrant for transfer is an account of the receiver: Piaget's stages decide which film technique carries over (pp. 7–8). She criticises teams that "imitate surface traits" of popular characters (p. 6) and says her paper offers developmental scaffolds "Rather than offering generic tips" (p. 18). That supports m4 and shows the principle itself is not new; the paper's addition is to replace developmental stage with decision competency as the account of the receiver. Her own output is still a list of six, with a summary table (p. 19).
- **m5 (cuts against).** Most of her craft goes into the character: expressiveness, persona, synchrony for comfort. She claims the right persona improves understanding: the sidekick persona "helps children develop more accurate mental models of AI" (p. 3), and selective anthropomorphism keeps engagement "while signalling the AI’s non-human nature" (p. 14). She also names the m5 risk: anthropomorphic cues "can lead to over-reliance" (p. 4), and an authoritative persona invites children to "over-rely on its judgments" (p. 14). She does not separate character craft from decision craft; she offers persona craft as the cure for misplaced reliance. The paper should meet that position directly, and can note that Kurian tests none of her persona claims.
- **m1 (supports the technique, not the competency).** Signals carries staging and readable pose into AI design: bold, readable gestures with dwell time (pp. 2, 10), and a camera that "holds a beat before or after speech" (p. 9). Stable mappings that children can "internalise" (p. 10) resemble a reading that a second look would not change. Her object, though, is the AI's emotion and intent, not an output with many possible causes. She also wants cues tuned to each child (p. 10), which could make one output read differently for different users.
- **m3 (thin support).** Sound and Structure mark change: leitmotifs, key changes and silences "cue narrative transitions" (p. 11), and voice-based AI can "signal mode changes" (p. 12). That is anticipation and change-marking applied to the system's own modes, not to a change in the rules a third party applies.
- **m6 (boundary, seen from outside).** Her scope is dyadic and leaves out algorithmic recommendation systems (p. 2). The most developed animation-to-AI framework found so far stops where the model begins, which supports drawing the boundary where m6 draws it.

## Loci

Matched against both text layers (`kurian2025once.txt`, `.readorder.txt`); every locus is found exactly. Pages are the arXiv PDF's printed page numbers, which equal PDF page numbers; section numbers are as printed in the arXiv PDF (see Caution). Inner double quotation marks are changed to single quotation marks in loci 1, 6 and 12.

1. "Pairing Piagetian developmental theory with design pattern extraction from 52 works of children’s animation, the paper presents a ‘six scaffold’ framework that integrates design insights transferable to child-centred AI design" Abstract, p. 1.
2. "An important ethical caveat: this paper does not endorse companion-style AI for children that fosters emotional dependency, unbounded intimacy, or other ethically problematic attachments." §1 Introduction, p. 1.
3. "This excludes non-interactive AI such as algorithmic recommendation systems." §1 Introduction, p. 2.
4. "Animation is fixed: all viewers receive the same scripted sequence, allowing precise control over pacing, tone, and framing. AI must operate in real time, interpreting ambiguous child input, making rapid decisions, and adapting to changing cognitive and emotional states." §1 Introduction, p. 2.
5. "Fourth, trust calibration is problematic: anthropomorphic cues can lead to over-reliance, while unexplained errors can erode trust (Mehrotra et al., 2024; Kurian, 2024)." §2.2 Affective Computing, p. 4.
6. "Lacking a structured bridge, teams may imitate surface traits from popular culture (‘make it friendly like Baymax’) without applying the narrative grammar and cross-modal logic that make such characters engaging and legible." §2.5 Gaps in Cross-Domain Translation, p. 6.
7. "This paper reports on phase one, which extracted developmentally appropriate strategies from ~70 hours of footage across 52 Walt Disney Animation Studios films (1937–2021), chosen for their historical breadth and culturally influential storytelling grammar." §2 Methods, p. 6.
8. "This study used a thematic analysis (Braun & Clarke, 2006) of the 52 films to identify media strategies that could inspire developmentally appropriate AI interaction design." §3.2 Thematic Analysis, p. 7.
9. "A key limitation is the absence of direct child involvement at this stage; these heuristics require empirical validation, but are rooted in Disney animation’s long-established capacity to engage children across developmental stages." §3.4 Study Limitations, p. 8.
10. "Disney’s animation style, built on principles like exaggeration, appeal, and staging (Tremosa, 2024), provides a blueprint for visual legibility." §4.1 Signals, p. 9.
11. "Crucially, the camera-work pairs these expressions with deliberate visual pacing: facial reactions linger, gestures resolve slowly, and the camera often holds a beat before or after speech." §4.1 Signals, p. 9.
12. "When children perceive an AI as an ‘omniscient authority,’ they may over-rely on its judgments, accept its outputs uncritically, or experience disproportionate disappointment and confusion when it makes mistakes." §4.4 Sidekick-Style Guidance, p. 14.
13. "Modelling AI personas on animated sidekicks also offers a route to selective anthropomorphism, a design strategy that maintains engagement while signalling the AI’s non-human nature." §4.4 Sidekick-Style Guidance, p. 14.
14. "Voice-based AI can similarly signal mode changes through coordinated voice and sound, improving understanding (Liu, 2018) and engagement (Chaspari & Lehman, 2016)." §4.2 Sound, p. 12.

## Caution

- **Version read.** The object held is the arXiv submitted version (arXiv:2504.08670), not the Elsevier version of record in *IJCCI* 46, article 100788 (issued December 2025 per Crossref). The APA string cites the published version. Every page and section locator on this card is the arXiv PDF's, and the wording may differ from the version of record. Crossref lists a CC BY 4.0 licence on the version of record from 7 Nov 2025, so an open copy may be obtainable; the loci should be re-matched against it before the paper quotes them with pages.
- **Section numbers.** The arXiv PDF numbers its sections inconsistently: "1. Introduction", an unnumbered "Background" holding §§2.1–2.5, "2. Methods" holding §§3.1, 3.2 and 3.4 (there is no 3.3), "3. Findings and Discussion" holding §§4.1–4.6, and "4. Conclusion". The loci give the numbers as printed.
- **Corpus label.** The paper calls the corpus 52 Walt Disney Animation Studios films (pp. 6–7), but footnote 2's pilot list (p. 7) includes Toy Story, Finding Nemo, The Incredibles, Up and Coco. [Unchecked: these titles are usually credited to Pixar, not WDAS; this rests on general knowledge, not on a source read this run.] Check the studio credits before the paper repeats that all 52 are WDAS films; "Disney films" is the safer label.
- **Evidence status.** The six scaffolds are one author's interpretive synthesis. The effects she reports (for example Faria and Ayrosa's percentages, pp. 11–12; Park et al. on Tega, p. 10) come from other studies, cited second-hand; none was tested here, and no children took part (p. 8).
- **Principles source.** Her one statement of Disney's principles rests on Tremosa (2024), an Interaction Design Foundation piece on UI animation (reference list, p. 26), not on an animator's text. Her reference list gives the craft book as "Johnston, O., & Thomas, F. (1981). The illusion of life: Disney animation" with Disney Editions (p. 23); Lewis et al. (`lewis2026invisible`, ref. [115]) give Thomas and Johnston, Abbeville Press. The paper should cite the book from the library's own card, not from Kurian's entry.
- **Self-citation.** Kurian grounds several claims in her own earlier work (Kurian 2023, 2024, 2025; Kurian & Sapsed 2025; Kurian & Saad 2024), including the term "developmentally aligned AI" (pp. 1–2). None of those works was read this run.
- The paper states its length as "Wordcount: 8127 excluding references" (p. 1).
