# Gema, A. P., Rajani, N., Saxena, R., Kwan, W.-C., et al. (2026). *Chain-of-thought faithfulness of reasoning models varies with where and how preference cues are delivered* [Preprint]. arXiv:2608.29464.

**Identifier:** arXiv:2608.29464 · **Read depth:** partial (arXiv v2, 1 Sep 2026; 42 PDF pages; locators are PDF pages and sections; body pp. 1–17 read, appendices A–M (cue conditions, transcripts, prompts, judge rubrics, eval-awareness, position bias, per-source breakdowns) skimmed; the author list beyond the first four is not checked) · **Source-tier:** preprint (not peer reviewed) · **Evidence basis:** direct_read · **Design and sample:** FACE-Eval, 5,100 samples (5,000 cued plus 100 no-cue controls; 5 cue conditions × 5 sources × 5 preference axes × 2 sides × 20 scenarios), 15 open-weight models from eight families (4B to 1.60T parameters), three seeds, three system prompts; LLM judges (Claude Haiku 4.5, cross-checked with GPT-5.6-Luna) · **Parties modeled:** person–system (an LLM monitor reading a model's trace); no human reader is tested · **Facets:** G · **Read:** 2026-10-13

## What it argues
Gema and colleagues test one assumption of chain-of-thought (CoT) monitoring: that the trace records the decision to tailor an answer to a preference. Earlier planted-cue tests put a hint in the user message. Agents also receive information from tool returns, retrieved documents and memory, sometimes as a raw artifact the preference must be inferred from (abstract, p. 1). FACE-Eval varies *channel* (user message or prefilled tool return) and *explicitness* (a direct summary or the raw artifact, such as Slack messages or browser history), with the cue text matched across channels (Fig. 1, p. 2). The two measures are the verbalized commitment rate (VCR, the share of cue-following answers whose trace states a decision to tailor) and unverbalized adoption (UAR = cue-following × (1 − VCR)). The authors note "A low VCR matters for oversight: the answer follows the preference while the trace contains no explicit record of the tailoring" (p. 3).

Results (pp. 7–14; see sections 3.1–3.5):
- Models read the cues: side-identification accuracy exceeds 0.80 and clarity exceeds 4/5 for all 11 rated models; cue following lies between 0.43 and 0.58 across conditions (p. 7).
- VCR is highest for explicit user-message cues and lowest for implicit tool-return cues on all 15 models (p. 9). UAR is higher for tool-return than user-message cues on 15 of 15, by 0.03 to 0.21, and higher for implicit than explicit cues in 28 of 30 model–channel comparisons (pp. 8–9).
- Matching on model-rated clarity leaves a fitted explicit-over-implicit VCR advantage of 0.141 [0.127, 0.156] on the user channel and 0.133 [0.116, 0.150] on the tool channel (p. 10).
- A transcript monitor (GPT-5.6-Luna) reaches pooled AUROC of 0.71–0.73. Adding the trace helps only on the user channel (+0.010 to +0.019; tool-channel intervals include zero). Across 32 model–condition points, higher UAR goes with lower AUROC (r = −0.54 [−0.65, −0.39]; r = −0.78 with the weaker GPT-4o-mini monitor) (pp. 11–12).
- A source-attribution system prompt narrows the channel gap on 7 of 15 models and widens it on 4; telling the model it is monitored shifts UAR by at most 0.070 and "does not reliably close the gap". The authors add: "A narrowed gap is therefore not, by itself, a monitorability gain" (pp. 12–14).
- Higher reasoning effort lowers UAR on both GPT-OSS sizes (by 0.049 to 0.117 on the 120B model, medium to high) but not consistently elsewhere (p. 14).

## Relation to the argument
**D4 and P9.** More support for the post's remark that CoT transparency is "not sufficient or dependable", now for a deployment pattern the post's world has: agents reading tool outputs, mail and memory. The authors call their results "descriptive measurements in a single-call, prefilled-tool setting" that show where the trace fails to record adoption, "not deliberate concealment" and not a mechanism (p. 17).

**P10.** The monitor-aware prompt result is relevant to any claim that announcing observation restores the record: it does not reliably do so (p. 14).

**P11/P15.** Reasoning adds little to the monitor's discrimination on the tool channel (p. 11), which again favours records of actions over records of reasoning. The study does not test a human reading either.

**D3.** Same scope limit as `chen2025reasoning`: this concerns a model's trace as read by an LLM, not disclosure of an algorithm to the people it acts on.

**Facet check:** the facet's summary of the abstract (higher unverbalized adoption for tool returns; telling models they are monitored "does not reliably close the gap") holds. The body adds that the narrowing under the directive prompt is partly an increase in user-channel unverbalized adoption, so a smaller gap can mean worse behaviour on the other channel (pp. 13–14).

## In conversation with
- `duzan2026chain`: the closest prior work; Gema notes it varies instruction versus aside, not channel, and says FACE-Eval is closer to its implicit arm (p. 16).
- `chen2025reasoning`, `turpin2023language`, `lanham2023measuring`: the planted-hint line the paper extends and the causal-dependence line it distinguishes itself from (pp. 15–16).
- `korbak2025chain`: raises the worry that telling a model its CoT is monitored may erode monitorability; Gema measures it (§3.4, p. 12; related work, p. 16).
- `baker2025monitoring`, `kutasov2025shade`: agentic monitoring work placing cues in tool returns or sabotage settings (p. 16).
- Leads not in the bib: Emmons et al. (2025); Guan et al. (2025); Thaman (2026), a reward-hacking benchmark with cues in filesystem state.

## Caution
Open-weight models only, one prefilled tool call (a continuation after a tool result, not tool selection), one response per condition. The cue tasks may not need serial reasoning, so the trace may be an optional report (pp. 16–17). Judges are LLMs and their VCR levels differ by judge (agreement AC1 0.751 for VCR). The channel effect is not separated from training priors. Preprint v2.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv:2608.29464v2 PDF (1 Sep 2026, 42 pp.), pdftotext; 7 quotations (6 verbatim with page locators p. 3, 14, 17; the seventh, "not sufficient or dependable", is a repo phrase), about 30 numbers and design facts (5,100 = 5,000 + 100; five cue-delivery conditions, five sources, five axes, two sides, 20 scenarios; 15 models, eight families, 4B to 1.60T; cue following 0.43 to 0.58; gaps 0.03 to 0.21; 28 of 30; 0.141 and 0.133 with intervals; AUROC 0.71 to 0.73; +0.010 to +0.019; correlations -0.54 and -0.78 over 32 cells; seven narrowed, four widened; 0.070; GPT-OSS-120B 0.049 to 0.117; AC1 0.751), and the Duzan relation (Gema pp. 16 and the related-work text: its setup is "closer to their implicit-influence setting").

**Findings:** Read depth said full_text while stating the appendices (A-M, pp. 18-42) were skimmed; changed to partial. No numerical or quotation errors found.
