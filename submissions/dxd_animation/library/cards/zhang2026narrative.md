---
key: zhang2026narrative
apa: "Zhang, C., & Davis, A. (2026). Narrative keyframing for generative creative writing. In *Proceedings of the 39th Annual ACM Symposium on User Interface Software and Technology (UIST '26)* (pp. 1–19). ACM. https://doi.org/10.1145/3830398.3830586"
authors: "Zhang, Chao; Davis, Abe"
year: 2026
title: "Narrative Keyframing for Generative Creative Writing"
venue: "UIST '26"
volume: ""
issue: ""
pages: "1–19"
doi: "10.1145/3830398.3830586"
url: "https://arxiv.org/abs/2608.10337"
type: proceedings
facets: [F12, G2]
claims: [m2, m4, m7]
role: contrast
load: load-bearing
read_depth: partial
object_read: "arXiv v1 (arXiv:2608.10337, 11 Aug 2026; 19 pp., CC BY 4.0; the UIST '26 paper), obtained 2026-11-11 by the run-2 gap-check subagent and copied by the lead to ~/iit-playground/dxd_animation_local/pdfs/zhang2026narrative/zhang2026narrative.pdf; sha256 in sha256.txt; parts read: abstract, §1, §2, design goals DG1–DG3, system sections on character keyframes and narratives (§5), study method (§6.2.1, participants), discussion and limitations (§7.1–7.2); results tables and qualitative findings skimmed only; Crossref record crossref.json"
verified: corrected
verified_against: "both text layers split by form feed; pdfinfo (19 pages, arXiv GenPDF); section headings mapped from the layout layer; crossref.json; provenance.txt; sha256 of PDF recomputed"
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Chao Zhang and Abe Davis introduce **narrative keyframing**, "an interaction technique for AI-assisted creative writing that lets writers specify different types of narrative constraints at selected moments in a story, then use AI to generate intervening prose" (abstract). They take the idea from animation: "In animation, the practice of keyframing offers an incredibly flexible and efficient way to balance automation with creative control", because "most of the important details in an animation can be derived from constraints on a sparse set of key moments, from which the rest of the animation can be interpolated" (§1, citing Lasseter 1987).

Their system offers plot, character and perspective keyframes; GPT-4.1 generates prose between them and can also interpolate character keyframes, which "remain fully editable" (§5). One design goal, DG3, is "Tracing how characterization decisions propagate into generated story text": writers "should be able to inspect how earlier decisions influence later generations" (§4). A technical evaluation against a standard LLM baseline and a study with 12 writers against a chatbot-and-outline baseline found stories of "higher overall quality and richer characterization" and "a more controllable, transparent, and engaging writing experience" (§1). They concede the workflow "may feel restrictive for writers who prefer to develop stories in a more fluid or improvisational way" (§7.2).

## What the paper uses it for

- **m2 (contrast, nearest precedent).** Zhang and Davis already carry animation keyframing — the person fixes key moments, the model generates what lies between — into an LLM interface, and their DG3 asks that the person be able to trace how their keys propagate into generated text. Row 2's key-pose move must cite them. Their setting differs from the model's in three ways: the person is a writer working alone, not a party deciding through an intermediary that binds a counterpart; the keys serve creative control, not a decision; and they select the technique for control, not through a competency.
- **m4 (support).** They borrow one technique for a stated purpose (balance automation and control) and test it against a baseline, an example of selecting craft for a job.
- **m7 (contrast).** "Keyframes with LLM in-betweens" is not new as an interface technique. The paper's novelty must rest on the selection through decision competencies and on the triadic setting.
- **Straight-ahead versus pose-to-pose.** Their limitation (locus 9) is Lasseter's distinction in a writer's words: keyframing suits planned work and constrains improvisation. That supports the model's split — explore straight-ahead, commit pose-to-pose.

## Loci

Matched against the reading-order text layer of the arXiv PDF (page numbers are the PDF's, which match the article's 19 pages). Inner double quotation marks are changed to single.

1. "lets writers specify different types of narrative constraints at selected moments in a story, then use AI to generate intervening prose." Abstract, p. 1.
2. "In animation, the practice of keyframing offers an incredibly flexible and efficient way to balance automation with creative control." §1, p. 1.
3. "most of the important details in an animation can be derived from constraints on a sparse set of key moments, from which the rest of the animation can be interpolated" §1, p. 1 (they cite [29], Lasseter 1987).
4. "Results show that our system produces stories with higher overall quality and richer characterization than a standard LLM baseline, and supports a more controllable, transparent, and engaging writing experience." §1, p. 2.
5. "Tracing how characterization decisions propagate into generated story text." §4, DG3, p. 4.
6. "writers should be able to inspect how earlier decisions influence later generations." §4, DG3, p. 4.
7. "These generated keyframes remain fully editable, allowing users to revise, add, or remove traits as needed." §5, p. 6.
8. "We recruited 12 participants" §6.2.1, p. 8.
9. "It may feel restrictive for writers who prefer to develop stories in a more fluid or improvisational way." §7.2, p. 11.

## Caution

- **Partial read.** The results tables and the qualitative findings were skimmed, not read; the card states the study's results only as the authors summarise them in §1.
- **Version.** The object read is arXiv v1, which carries the UIST '26 ACM reference and a CC BY 4.0 licence; Crossref gives the proceedings record (pp. 1–19, issued November 2026). Page numbers are the arXiv PDF's.
- **Small study.** Twelve writers, a creative task, a chatbot baseline; no decision, no counterpart.
- Found by the run-2 gap check (`../GAP_CHECK_2.md`).

## Verification

2026-11-11 · S6 verifier, batch C (Opus 5.5; not the writer) · verdict: corrected · checked: 9/9 loci found verbatim in the reading-order text layer on the stated PDF pages (pp. 1, 1, 1, 2, 4, 4, 6, 8, 11); section locators checked against the headings in the layout layer (§2 Narratological Foundations, §3 Related Work, §4 Design Goals, §5 System Design with §§5.1–5.6, §6 System Evaluation, §7 Discussion with §§7.1–7.2); reference [29] is "John Lasseter. 1987. Principles of traditional animation applied to 3D computer…"; frontmatter vs crossref.json (Chao Zhang and Abe Davis, UIST '26 proceedings, pp. 1–19, issued 2026-11, ACM, DOI) and the PDF's own ACM reference block (19 pages, same DOI); arXiv stamp "arXiv:2608.10337v1 [cs.HC] 11 Aug 2026" and CC BY 4.0 licence line on p. 1; pdfinfo gives 19 pages; sha256 of the PDF recomputed (2a2bb9…), matches sha256.txt; read_depth partial honest, and the body stays within the listed parts (GPT-4.1 from §5.6, the baseline from §6.2.1); body quotations; claim uses · changed: (1) loci 5–6 and What it argues, DG3 "§3" → "§4": the design goals sit under §4 "Design Goals"; §3 is Related Work; (2) What it argues: "A study with 12 writers against a chatbot-and-outline baseline found stories of 'higher overall quality and richer characterization'…" → "A technical evaluation against a standard LLM baseline and a study with 12 writers against a chatbot-and-outline baseline found…", because §1 reports the results of both evaluations together ("a technical assessment … as well as a user study with 12 writers", p. 2) and the card had given both results to the writers' study · for the lead: (1) The quality and characterization result comes from the technical evaluation, Study 1 (§6.1.2, p. 7: GPT-4.1 stories scored by the WQRM-PRE model, preferred in 72 of 100 pairs; three Prolific raters' majority vote favoured the system in 29 of 30 pairs for characterization and 25 of 30 for overall quality). The 12 writers (Study 2) are the source of the controllability, transparency and engagement findings, and the authors call those results "promising but preliminary" (§7.2, p. 11). The paper should not credit the 12-writer study with better stories. §6.1 lies outside the card's parts read; I read it to place the correction. (2) The "Straight-ahead versus pose-to-pose" bullet is the card's own reading: Zhang and Davis never name Lasseter's two approaches, and the bullet carries no claim tag. (3) object_read gives the hash only as "sha256 in sha256.txt"; README rule 2 asks for the sha256 itself. (4) Two unread passages bear on m7: §3.1 "Keyframing in Animation" (p. 3), their account of the animation source, and their novelty claim in §3.2 ("Uniquely, our keyframing interaction allows authors to control different types of narrative constraints … at selected moments in a story", p. 4).

## Hand-check

- 2026-11-11, Claude (Opus 5.5, lead; S7). Verdict: **index**. Writer: the lead; check: S6 verifier, batch C (corrected: DG3 is in §4; the quality result belongs to the technical evaluation, not the 12-writer study). Checked: the corrections against the text. Changed: nothing further; DRAFT_v1 cites only the abstract, DG3 and the limitation. For the author: §§3.1–3.2 (their account of keyframing) are unread and bear on the gap claim.
