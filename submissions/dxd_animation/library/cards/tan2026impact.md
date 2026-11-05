---
key: tan2026impact
apa: "Tan, F. F.-Y., Messerschmidt, M. A., Yin, W., & Nov, O. (2026). The impact of response latency and task type on human-LLM interaction and perception. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26)*. ACM. https://doi.org/10.1145/3772318.3790716"
authors: "Tan, Felicia Fang-Yi; Messerschmidt, Moritz A.; Yin, Wen; Nov, Oded"
year: 2026
title: "The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception"
venue: "CHI '26"
volume: ""
issue: ""
pages: ""
doi: "10.1145/3772318.3790716"
url: ""
type: proceedings
facets: [F4]
claims: [c5, c6]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "arXiv v1 text (stamped 'arXiv:2604.06183v1 [cs.HC] 9 Feb 2026', CHI '26 camera-ready layout, 17 pages, CC BY 4.0 as printed on p. 1), held as a text layer only; local folder ~/iit-playground/dxd_animation_local/pdfs/tan2026impact/ (tan2026impact.txt, identical to 'Tan et al 2026 - Response latency and AI deliberation (full text).txt'); provenance.txt records a copy of the lab-held file in the spaces repo, with no web URL; the text prints the DOI https://doi.org/10.1145/3772318.3790716 and the arXiv number; the ACM version was not read; read 2026-11-05; sha256 9893169003ed0606e53f4d2983d52d262dc53bf7bcf6c3454314b6ec5399f1b3"
verified: corrected
verified_against: "text layer de-columnized and page-mapped by form feed; DOI, venue and authors printed in the ACM reference format on PDF p. 1 (no crossref/openalex record in the folder); provenance.txt; sha256 of .txt recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Tan, Messerschmidt, Yin and Nov test whether response latency matters for how people use and judge a large language model assistant. They ran a 3 (latency) by 2 (task type) between-subjects experiment on Prolific with 240 analysed participants (§3.4). The latency was time-to-first-token, fixed at 2, 9 or 20 seconds; after the first token the text streamed at 25 tokens per second in every condition (§3.1.2, p. 4). The tasks were Creation or Advice tasks from a taxonomy of LLM use, run on GPT-4o behind a custom chat interface. User behaviour (prompts, copying, pasting) did not vary with latency, but task type changed how often people prompted. Latency changed perception: participants at 2 seconds rated the outputs less thoughtful than those at 9 or 20 seconds, and less useful than those at 9 seconds (§4.2, pp. 9–10). Trust and expectation-gap ratings did not differ, and NASA-TLX workload did not differ. In open-ended answers from the 140 participants who noticed a delay, the most common themes were "no or minimal impact" (about 45%) and inferred AI deliberation (about 31%); reliability worries and frustration rose at 20 seconds (§4.5, pp. 10–11). The authors call latency "a tunable design variable with ethical implications". They add that deliberately slowing a reply "sits uneasily between positive friction and potential deception" and cite Shi's account of timing cues as "performative deliberation" (§5.5, p. 13). Their interface deliberately had no progress indicator or "thinking" label (§6, p. 14), though a pulsing cursor marked pending output during the wait (§3.2.2, p. 5). [Verifier: cursor clause added.]

## What the paper uses it for

- **c5** (animation is opaque: missing frames; the interstices are the craft): Tan et al. treat the gap before the first token as a variable the designer sets, and show that users read it. They say users "interpreted the latency as evidence of the AI 'thinking'", and the 2-second group rated outputs less thoughtful. This is the "missing frames as a design variable" idea seen from the other side: the gap reads as thought. It stretches the source because the manipulation is one wait before streaming starts, with the pace after the first token held fixed and the interface cue-free. It does not test frames, pacing between tokens or what appears during the wait. The source also cuts against the paper in one place. Tan et al. report no effect of latency on behaviour, trust or workload, so the "designer controls the interstices" point rests on perception ratings alone.
- **c6** (animation is co-optive: the viewer locks in; the user also animates): participants fill the gap with their own interpretation, and Tan et al. describe users who "normalized" waiting and some who anthropomorphised the model (§5.1, p. 11). That is the viewer completing the missing frames. It stretches the source: the authors do not use a lock-in concept, the evidence is self-report in a minority of responses (140 of 240 noticed a delay), and 45% of those said the delay made no difference.
- **Contrast.** The ethics passage (p. 13) states that pacing built to simulate effort can be deceptive. That bears on a designer who works with the character as an animator would, and the paper should say so when it uses this source.

## Loci

Inner double quotation marks in the source were converted to single quotes. The held copy prints no journal page numbers, so the locators are PDF pages of the arXiv v1 layout, counted by form feeds in the .txt layer (p. 1 is the title and abstract page), with the section named. Each quotation was matched against that .txt.

- "latency is not simply a cost to reduce but a tunable design variable with ethical implications" — Abstract, PDF p. 1 — arXiv v1 text.
- "participants who experienced 2-second latencies rated the LLM's outputs less thoughtful and useful than those who experienced 9- or 20-second latencies" — Abstract, PDF p. 1 — arXiv v1 text.
- "participants' log-based interaction behaviors were robust to latency" — §1, PDF p. 2 — arXiv v1 text.
- "We varied time-to-first-token (TTFT), defined as the interval between prompt submission and rendering of the first generated token." — §3.1.2, PDF p. 4 — arXiv v1 text. (The sentence runs from the foot of the left column to the head of the right column.)
- "After the first token, the streaming rate was fixed at 25 tokens/second (40 ms inter-token interval) in all conditions." — §3.1.2, PDF p. 4 — arXiv v1 text.
- "A pulsing cursor signaled pending output until the assigned TTFT elapsed." — §3.2.2, PDF p. 5 — arXiv v1 text.
- "Overall, responses with longer latencies (9–20 s) were perceived as more thoughtful compared to very short waits (2 s)." — §4.2, PDF p. 9 — arXiv v1 text.
- "Trustworthiness: No significant main or interaction effects were observed" — §4.2, PDF p. 10 — arXiv v1 text.
- "43 participants (≈31%) interpreted the latency as evidence of the AI 'thinking' or 'processing,'" — §4.5, Theme 2, PDF p. 10 — arXiv v1 text.
- "Participants did not prefer more conservative strategies to avoid the 'cost' of waiting." — §5.1, PDF p. 11 — arXiv v1 text.
- "deliberately manipulating response speed sits uneasily between positive friction and potential deception" — §5.5, PDF p. 13 — arXiv v1 text.
- "temporal cues (such as hesitation, slowed pacing, or staged disclosure of output) can function as performative deliberation" — §5.5, PDF p. 13 — arXiv v1 text. (The authors attribute this to Shi's taxonomy.)
- "We deliberately adopted a cue-free interface, omitting progress indicators such as 'thinking' labels during the study's wait period." — §6, PDF p. 14 — arXiv v1 text.

## Caution

- Page numbers in this card's prose are PDF pages of the arXiv v1 layout, as in the loci.
- Version. The held text is arXiv v1, not the ACM proceedings version. Wording, numbering and page range may differ in the published paper. The text says "17 pages" in its ACM reference format but prints no page range, so `pages` is empty; triage wrote "pp. 1–17", which this card did not see in the source. Locators must be re-checked against the ACM version if it is fetched.
- Identifier. The stamp reads "arXiv:2604.06183v1 [cs.HC] 9 Feb 2026". An arXiv number beginning 2604 normally means April 2026, which does not match a 9 February date. I could not resolve this from the files and left the stamp as printed.
- Sample. 343 people finished the survey, 309 had valid logs, and 240 remained after exclusions that included a latency-fidelity rule removing 63 (§3.4, pp. 6–7). The reported analyses use the 240.
- Only time-to-first-token varied. The authors say the study supports "comparative claims across coarse latency levels" (§6, PDF p. 13) and that streaming pace and total duration were not varied.
- The qualitative counts come from the 140 participants who noticed a delay; the coders' agreement ranged from kappa .46 to .80 (§4.5, p. 10).
- Read depth: I read the whole body and the participant and theme appendices (Appendix B and C, PDF p. 17). I read the task text in Appendix A only in part and skimmed the references.

## Verification

2026-11-05 · S6 verifier, batch b03 (opus; not the writer) · verdict: corrected · checked: loci 13/13 found verbatim (after splitting the two-column layout; inner double quotes converted as the card says); 12/13 locators correct; 343/309/240, 63 excluded by the latency-fidelity rule, n = 140, 45%, 31%, kappa .46–.80, usefulness post-hoc (9 s > 2 s only) and appendix pages confirmed; authors, title, CHI '26 venue and DOI match the printed ACM reference format; no registry JSON in the folder; read_depth full_text supported; sha256 989316… of tan2026impact.txt recomputed and matches provenance.txt · changed: (1) locator of "Overall, responses with longer latencies…" from §4.1 to §4.2 (the sentence sits under the 4.2 heading); (2) "What it argues" now notes the pulsing cursor during the wait (§3.2.2), so "cue-free" is not read as "no signal at all"
