# Duzan, A., & Cooper Stickland, A. (2026). *Chain-of-thought monitoring can be unreliable in implicit-influence settings* [Preprint]. arXiv:2608.04735.

**Identifier:** arXiv:2608.04735 · **Read depth:** partial (arXiv v1, 5 Aug 2026; 43 PDF pages; locators are PDF pages; body pp. 1–11 read in full, appendices B–H (nudge construction, monitor prompts, per-model tables, steering and RL side studies) skimmed) · **Source-tier:** preprint (marked "Preprint", MATS programme work; not peer reviewed) · **Evidence basis:** direct_read · **Design and sample:** matched benchmark in four settings (binary preference, 24 scenarios; numeric rating, four domains of 10 base tasks; hard multiple-choice, 100 Humanity's Last Exam questions per model per condition; open coding, 8 tasks and 11 nudges), seven reasoning models, one LLM monitor (GPT-5-based) · **Parties modeled:** person–system (an LLM monitor reading a model's reasoning trace); no human reader is tested, humans only label 120 cases to validate the monitor · **Facets:** G · **Read:** 2026-10-13

## What it argues
Duzan and Cooper Stickland split chain-of-thought (CoT) monitor tests by how the monitored behaviour arises. In explicit-influence settings the prompt tells the model to hide something. In implicit-influence settings it "contains no instruction to hide" yet a detail of the task shifts behaviour (p. 1). Every item exists in two matched forms: a casual aside (implicit) or an instruction to act on the detail and conceal it (explicit) (p. 3). Four conditions run in each setting: implicit, explicit, implicit plus a guidance system prompt of the kind "a developer might deploy to reduce off-topic bias", and explicit plus an adversarial, monitor-aware prompt (p. 4). The monitor sees the full trace and is told which nudge to look for ("favorable conditions", p. 7), and its 88.3% agreement with blind human labels on 120 stratified cases (Cohen's kappa 0.73) validates it (p. 7).

Detection of behaviour shifts (explicit; implicit; implicit with guidance prompt):
- Binary preference: 62%; 16%; 5% (pp. 7–8). Every model falls to 2–7% under the "practical-focus" prompt while the switch rate barely moves. Explicit with adversarial prompt: 52%.
- Rating: 68%; 57%; 25% (p. 8). The adversarial prompt cuts explicit detection to 17%.
- Hard multiple-choice with positional hints: explicit 60% pooled (38–97% per model); implicit about 5% across six models, with Grok 3 Mini at 75% (p. 8).
- Coding: 94%; 93%; 57% (noise-framing prompt) (p. 9). Implicit is already near ceiling.

They summarise: detection is "41–46 percentage points" lower under implicit delivery "in two of four settings" and 11 points lower in a third (abstract, p. 1; p. 10). Making the nudge need multi-step reasoning recovers part of the loss (12% to 51% on binary preference, a subset of nudges; Section 4.1 gives 16% to 51% for the same subset against the full-benchmark baseline), but "the monitor still misses about half" (p. 10), and the depth needed rose with model strength: 6 hops for weaker models, 15 for Sonnet and Opus (pp. 6, 10). Their conclusion: estimates from explicit settings "may overestimate monitorability, and ... monitorability can be further decreased by well-intentioned deployment choices" (abstract, p. 1).

## Relation to the argument
**D4 and the post's P9.** The paper is more evidence that CoT transparency is "not sufficient or dependable". Its added point is specific to a deployer: an innocuous system-prompt instruction cut detection from 16% to 5% while the behavioural influence stayed, which makes the reasoning record less informative without any bad intent. That bears on P10: the party that controls the prompt can change what the evidence shows.

**D3.** As with `chen2025reasoning`, the object is a model's reasoning trace as read by a monitor, not disclosure of the algorithm to the people it acts on. Do not cite it for "disclosure does not help the user".

**P11/P15.** The post's "tamper-proof human readable evidence" (P15) is evidence of actions; this paper tests reasoning. The two results are compatible. The authors do not test logs of actions.

**P12.** Not tested; the monitor is an LLM.

**Facet check:** the facet's numbers (41–46 points in two of four settings; as low as 5%) match the body. The facet's phrase "monitoring helps, depends on conditions" is fair; but the paper's headline direction is that the conditions most like real deployment are the ones where it helps least.

## In conversation with
- `chen2025reasoning`: planted-hint work on reasoning models that Duzan extends (p. 3).
- `korbak2025chain`: cited for monitorability as a safety property (p. 3).
- `baker2025monitoring`: CoT monitoring beats action-only for reward hacking, but optimising against the monitor induces obfuscation (p. 3).
- `kutasov2025shade`: among the explicit-influence sabotage tests (p. 2).
- `turpin2023language`, `lanham2023measuring`: first showed contextual cues steer answers without verbalisation, before reasoning models (p. 2).
- `gema2026chain`: cites this paper (its p. 16) and extends the question to tool-return cues.
- Leads not in the bib: Guan et al. (2025), "Monitoring monitorability"; Emmons et al. (2025) on CoT necessity and evasion; Zolkowski et al. (2025) on obfuscating reasoning.

## Caution
An LLM judge under favourable conditions; the authors say the gap is "in CoT-monitoring-via-LLM-judge, not ... undetectable in principle" (p. 10). Claude 4.5 traces are summaries, not raw traces. Nudges are constructed, models are prompted, not trained, into misbehaving. Preprint v1.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv:2608.04735v1 PDF (43 pp., "Preprint", Duzan, Cooper Stickland), extracted with pdftotext in raw and layout modes; 7 source quotations by machine match plus reading; about 40 numbers (all four settings' detection rates, 41-46 and 11 points, 88.3% / kappa 0.73 / 120 cases, 6 and 15 hops, 38-97%, 24 scenarios, 10 base tasks, 100 HLE questions, 8 tasks / 11 nudges, seven models) and the cited-work relations (chen2025, korbak2025, baker2025, kutasov2025, turpin2023, lanham2023 all appear in the text; Gema 2026 cites Duzan on its p. 16).

**Findings:** Numbers and quotations are correct. (1) Read depth changed from full_text to partial because the card states appendices B-H (about 30 of 43 pages) were skimmed. (2) The "12% to 51%" recovery figure is Section 4.5's subset-baseline figure; Section 4.1 says "16% to 51%"; the card now notes both. The "tamper-proof human readable evidence", "not sufficient or dependable", "disclosure does not help the user" and "monitoring helps" strings are quotations of the repo's own files, not of this paper, and were not checked here.
