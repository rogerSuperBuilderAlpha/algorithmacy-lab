---
key: masumori2026openlife
apa: "Masumori, A., Doi, I., Maruyama, N., Takata, R., & Ikegami, T. (2026). *OpenLife: Toward open-world artificial life with autonomous LLM agents* (arXiv:2606.31046) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2606.31046"
authors: "Masumori, Atsushi; Doi, Itsuki; Maruyama, Norihiro; Takata, Ryosuke; Ikegami, Takashi"
year: 2026
title: "OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents"
venue: "arXiv (cs.AI)"
volume: ""
issue: ""
pages: "10 pp."
doi: "10.48550/arXiv.2606.31046"
url: "https://arxiv.org/abs/2606.31046"
type: preprint
facets: [G]
claims: [c12, c4, c1]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "arXiv v1 PDF (arXiv:2606.31046v1 [cs.AI] 30 Jun 2026; 10 pp.; CC BY 4.0 per its p. 1) and its text layer masumori2026openlife.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/masumori2026openlife/; the text layer interleaves the two columns, so I read and matched the two-column pages (1–2, 5, 7–9) from column-split extractions of the same PDF (pdftotext -x/-W crop at 306 pt); all 10 pages read 2026-11-08; sha256 b43245c79a8543d661b5246c5f9261276b80f72afad7378596b4e9edb137a398 (PDF; recomputed with shasum -a 256, matches sha256.txt)"
verified: verified
verified_against: "csl.json; held v1 PDF sha256; column-split pdftotext (x 0–306 / 306–612 pt) per page, 14 of 14 quotations traced to their stated pages and columns"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Masumori et al. (2026), OpenLife

## What it argues

Atsushi Masumori, Itsuki Doi, Norihiro Maruyama, Ryosuke Takata and Takashi Ikegami propose "open-world
Artificial Life": running life-like agents in the real social, technical and economic world, not in a
closed simulation. They take their criterion from autopoiesis and enactivism. Life-like autonomy is "an
agent’s acting so as to contribute, through its own activity, to its own continued existence" (p. 1). They
argue that LLM agents, with memory, tools, network access and payment, now make such an experiment
possible.

Their system, OpenLife, is built on the OpenClaw agent platform. It "surrounds a stateless LLM" with a
society of asynchronous processes: a memory graph whose links the LLM weights by meaning ("semantic-dependent
plasticity"), verbal policy optimization in place of scalar reward, perception, metacognition, a developer
process, and a budget that each call debits, with exhaustion treated as death. The authors removed the
platform's assistant framing and its clause against self-preservation, and relabeled the transcripts' roles
as Self and Other.

Six agents ran for about twelve weeks on Claude, Gemini, GPT and Gemma backends. The authors report a shift
from reactive to spontaneous activity, individuation (agents' outputs grow separable), social roles, a
peer-signed "Web of Trust", and a first self-earned $5 sale of an agent's e-book. They also report limits:
no agent earned enough to survive, so they paid a $15/day basic income; humans created accounts and repaired
failures; the reframing confounds the behavioral shift; and the agents could read about the project. They
claim neither closure nor autopoiesis. Their conclusion is that "Life-likeness … does not reside only inside
an isolated agent" but arises when memory, processes, perception, metabolic constraint and a livable
environment are present together.

## What the paper uses it for

- **c12** (gap: AI development as a craft of animation, not an ALife experiment): OpenLife is the prior work
  that Checkpoint B named, and it fixes c12's wording. The card confirms what DECISIONS asked: the body makes
  no conceptual claim about AI development in general. The authors call their contribution "conceptual", but
  the concept is an experimental paradigm for artificial life ("we propose open-world ALIFE as an
  experimental paradigm", p. 2). They speak about other agent frameworks only to contrast them: those build
  "automation around a language model" (p. 2), which they call "sophisticated automation, not autonomy". So
  OpenLife argues that one specially built system is a candidate for life; it does not argue that building
  ordinary AI is making life.
- **c4** (an organizational account of life fits the system around the LLM): OpenLife is the closest
  support and the sharpest objection in one paper. It supports the structural half: life-likeness lies in
  the processes around a stateless LLM, not in the model. It objects to the general half. On the authors'
  terms, the harnesses of ordinary AI products are not life-like, because they serve "human-defined tasks
  under external evaluation" (p. 2). To get life-likeness they had to remove the anti-self-preservation
  clause and add a metabolism. The paper would have to say why a coding agent's harness, organized around a
  user's task, counts under an organizational account that the authors reserve for systems organized around
  their own persistence.
- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): OpenLife states c1 in engineering
  practice. Its Table 2 lists the "support processes around the LLM session", and the authors say that
  "Building a life-like agent and the world that can sustain it proved inseparable" (p. 8). The use fits,
  with one stretch: the authors make the point about their life-like agents, not about AI systems in
  general.
- A note for c9 (triadicity; not tagged): the humans who "meter resources, monitor behavior, and can halt any
  agent" (p. 8) fit the studio that determines what the agent can do. The authors frame them as a stand-in
  environment, not a third party, so any c9 use would be the paper's reading.

## Loci

Locators: the arXiv PDF prints no page numbers; "p." counts PDF pages. The text layer
`masumori2026openlife.txt` interleaves the two columns line by line, so every quotation was matched against a
column-split extraction of the held PDF (left column x 0–306 pt, right column x 306–612 pt; sha256 above).
Line-end hyphens are rejoined. Where the authors' text has double quotation marks inside a quotation, I give
them as single quotes.

- "Our proof-of-concept, OpenLife, surrounds a stateless LLM not with a single 'smart agent' but with a society of asynchronous processes—memory, perception, evaluation, and a budget-based metabolism that makes persistence normative." — PDF p. 1, Abstract (left column); matched against column-split extraction of the held PDF
- "We do not claim OpenLife has realized artificial life, but that open-world ALIFE is now a viable experimental paradigm and a concrete platform for studying what might cautiously be called living AI." — PDF p. 1, Abstract (left column); matched against column-split extraction of the held PDF
- "The commitment we take from this lineage is simple: life-like autonomy is an agent’s acting so as to contribute, through its own activity, to its own continued existence." — PDF p. 1, §1.1 (right column); matched against column-split extraction of the held PDF
- "Yet what they do is sophisticated automation, not autonomy: they pursue human-defined tasks under external evaluation, whereas an autonomous agent generates norms from its own persistence conditions" — PDF p. 2, §1.2 (left column); matched against column-split extraction of the held PDF
- "OpenLife sits among recent agentic frameworks but differs in aim: where most build automation around a language model, we treat agency as distributed across a society of processes organized around the agent’s own persistence" — PDF p. 2, §1.3 (right column); matched against column-split extraction of the held PDF
- "The paper’s primary contribution is therefore conceptual—we propose open-world ALIFE as an experimental paradigm built on persistent LLM agents in the real world" — PDF p. 2, §1.3 (right column); matched against column-split extraction of the held PDF
- "The aim is not to program autonomy but to clear the conditions under which it can be attempted." — PDF p. 2, §2 (right column); matched against column-split extraction of the held PDF
- "Humans are part of the setup, but not as scriptwriters: we created accounts, repaired failures, and implemented changes the agents asked for" — PDF p. 5, §3 (right column); matched against column-split extraction of the held PDF
- "we therefore cannot cleanly separate emergence from the reframing" — PDF p. 7, §3.2 (left column); matched against column-split extraction of the held PDF
- "Building a life-like agent and the world that can sustain it proved inseparable" — PDF p. 8, §4 (left column); matched against column-split extraction of the held PDF
- "SDP and VPO (Section 2) are partial steps toward such operational closure, though we claim neither closure nor autopoiesis." — PDF p. 8, §4 (left column); matched against column-split extraction of the held PDF
- "Autonomy, in short, is harder than automation" — PDF p. 8, §4 (left column); matched against column-split extraction of the held PDF
- "the experiment is deliberately contained—humans meter resources, monitor behavior, and can halt any agent" — PDF p. 8, §4 (right column); matched against column-split extraction of the held PDF
- "Life-likeness, on this view, does not reside only inside an isolated agent; it becomes possible when memory, parallel processes, persistent perception, metabolic constraint, and a livable environment are jointly present." — PDF p. 8, §5 (right column); matched against column-split extraction of the held PDF

## Caution

- **Venue not confirmed.** DECISIONS's APA adds "(Accepted at ALIFE 2026; no proceedings record yet.)". The
  read text does not state acceptance anywhere; the only trace is a footnote URL ending
  `alife2026.html` (p. 6). The csl.json record names only arXiv, version 1. I left the acceptance note out
  of the APA. S8 should cite the arXiv preprint unless a proceedings record appears.
- **Preprint, v1.** The card describes arXiv v1 (30 Jun 2026). A later version or the proceedings paper may
  differ.
- **Text layer.** `masumori2026openlife.txt` interleaves the two columns line by line. A quote checker run
  on it will fail on most loci; S6 should match against a column-split extraction, as I did.
- **What the evidence shows.** The run is observational, with n = 6 agents, a $15/day basic income from 9 May (p. 7), human
  repairs, and a reframing confound the authors admit. Their retrieval evaluation is n = 12 and judged by an
  LLM. The paper should cite OpenLife for its framing and design, not as evidence that LLM systems are alive.
- **Authors' own interest.** The authors are affiliated with Alternative Machine Inc. and Their Inc. as well
  as universities (p. 1), and they thank the agents as "participants in shaping part of the research itself"
  (p. 9). The paper should note this if it leans on their framing.
- **Status.** Checkpoint B's c12 ruling names "OpenLife, Masumori et al. 2026", so the card is cited.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 1
- verdict: verified
- checked: frontmatter against csl.json (five authors in order, title, issued 2026, DOI, version 1, cs.AI, CC BY 4.0); the p. 1 stamp "arXiv:2606.31046v1 [cs.AI] 30 Jun 2026"; 10 pages per pdfinfo; sha256 recomputed, matches sha256.txt. I traced all 14 quotations against my own column-split extractions of each page (left x 0–306 pt, right x 306–612 pt): each is verbatim and sits on the page and in the column given. In the text I confirmed the claims the card rests on: OpenClaw and the removed safety clause, Self/Other relabeling, the backends (Claude, Gemini, GPT, Gemma), Table 2 on p. 5, the $5 sale, the Web of Trust, the $15/day basic income from 9 May (p. 7), the n = 12 retrieval test scored by a blinded LLM judge, the "not wholly naive subjects" caveat (p. 8), the Alternative Machine and Their Inc. affiliations, and the thanks to the agents (p. 9). I searched the full text for "accepted", "ALIFE 2026" and "proceedings": the only venue trace is the footnote URL ending alife2026.html (p. 6), so leaving the acceptance note out of the APA is right. The c12, c4 and c1 uses fit, and the card names their stretches.
- changed: nothing

## Hand-check
