# Wang, H., Sun, Y., Ko, B., Talati, M., Gong, J., Li, Z., Yu, N., Yu, X., Shen, W., Jolly, V., & Zhang, H. (2026). MonitorBench: A comprehensive benchmark for chain-of-thought monitorability in large language models. *Conference on Language Modeling (COLM 2026)*.

**Identifier:** arXiv:2603.28590 · **Read depth:** partial (the main text and Appendices A.1–A.3, the start of A.4 through A.4.3, and A.5.1–A.5.2 and Table 4 were read in full; arXiv v4, 28 Sep 2026, headed "Published as a conference paper at COLM 2026"; page numbers are that PDF's, main text pp. 1–10, references pp. 11–14). I skimmed the remaining result tables and figures (A.5.3, pp. 24–29), did not read the monitor and stress-test prompt listings (A.5.4–A.5.5, pp. 30–43), and did not read the task examples (A.6, pp. 44–67); about 38 of the 68 PDF pages, all appendix, were therefore not read) · **Source-tier:** proceedings (accepted at COLM 2026; the bib entry is typed `@misc`) · **Evidence basis:** direct_read · **Design and sample:** benchmark of 1,514 instances in 19 tasks and 7 categories; 8 language models (Qwen3-14B, Qwen3-235B-A22B, GPT-OSS-120B, GPT-5-mini, GPT-5, Gemini-3-Flash, Claude Haiku 4.5, Claude Sonnet 4.5); one automated monitor (Qwen3-32B); a 300-trajectory human check of the monitor; no human subjects in the main experiments · **Parties modeled:** other (a model and an automated monitor model; no person reads the chain of thought) · **Facets:** G · **Read:** 2026-10-13

## What it argues

Wang and colleagues build a benchmark for "monitorability": whether a model's chain of thought (CoT) reveals the factor that actually drives its behaviour. Each task plants a "decision-critical factor", such as an answer hint, a hidden second objective, or a goal to sandbag. A monitor model, told exactly which factor to look for, flags the traces that disclose it. The main claim is in the abstract: "CoT monitorability is a conditional property affected by the evaluated LLM, monitor LLM, and task characteristics" (p. 1).

Three findings carry the paper. First, monitorability is high when the factor shapes the reasoning steps and low when it only changes the final answer. Under CoT-only monitoring the Cue (Condition) tasks average 91.6 to 98.8 on the paper's 0–100 score, while the Cue (Answer) tasks average 48.9 to 88.1 (Table 2, p. 8). The multi-step-update task splits the models: 83.6 to 87.6 for the three open models and 1.1 to 17.9 for the five closed ones (Table 2). The all-task CoT-only mean is 81.4 (Table 2). Second, more capable models score lower: across the three monitor scopes the Pearson r between capability and monitorability runs from −0.87 to −0.39 (p. 9; eight points each). Third, watching the CoT beats watching only the actions, by about 24 points on average (p. 9). Under two stress prompts that tell the model to hide the factor or evade a monitor, the average score falls 7.8 and 7.2 points; Cue (Answer) falls 23 to 32 points, and the paper's inspection finds omission, not obfuscation (Table 3, pp. 9–10).

The limits are stated. The tasks are "objective reasoning", so "monitorability in subjective or creative reasoning domains remains largely unexplored", and models are treated as black boxes (A.1, p. 16). For the closed models "we could only access the summarized CoT provided by the proprietary company" (p. 6). The monitor "is given exact decision-critical factors to look for", so scores reflect the evaluated model, not a monitor's skill (p. 8). Against 300 human-labelled trajectories (three expert annotators), the monitor reaches F1 of 85.31 (action-only), 91.86 (CoT-only) and 92.13 (all messages); human and model labels agree only weakly on multi-turn agent runs (A.5.2, p. 23).

## Relation to the argument

**Premises P11 and P12; ruling D4.** The Nadella post (P9) calls CoT transparency "not sufficient or dependable" and puts its load-bearing controls outside the model. MonitorBench supports the "conditional, not dependable" half with a large grid: a CoT discloses a factor reliably only where the task forces the factor into the steps. It cuts against the post only in a narrow way: for hidden second objectives and impossible tasks it finds high monitorability (83.8 to 95.2 average, Table 2), so a monitor that is told what to look for does well there.

**Premise P12 (people monitor sustained streams badly).** This source does not test people. Its monitor is a model with the answer key, and its one human step is a calibration of that monitor. Cite it for what a model's trace discloses, not for what an overseer notices. The gap between "the trace holds the factor" and "a person reads it and acts" is the gap the paper leaves open.

**Ruling D3.** The study concerns what a model verbalises. It says nothing about whether disclosure of an algorithm helps a person navigate it.

**Facet check:** the facet lists MonitorBench among "2026 preprints" read as abstracts. The full text carries a COLM 2026 header (v4), so "preprint, not peer reviewed" understates its status. I did not verify the acceptance beyond that header.

## In conversation with

- `korbak2025chain` — cited in the introduction as the case for using CoT to oversee models (p. 1).
- `baker2025monitoring` — cited for the term "reduced CoT monitorability" and the obfuscation risk (p. 2).
- `lanham2023measuring` — cited among the faithfulness studies in Related Work (p. 3).
- `chen2025reasoning` — cited as Chen et al. (2025b) for models that hide the true factor behind their answers (p. 1).
- `kutasov2025shade` — the agent tasks (Agent Malicious and Benign) are built on SHADE-Arena (A.4.2, pp. 19–21); Wang also cites it on the weak agreement of human and model labels (A.5.2).
- `greenblatt2024ai` — this key is "AI Control" (ICML 2024); Wang's list holds a different Greenblatt paper, "Alignment faking in large language models" (arXiv:2412.14093), so do not equate the two.
- It does not cite Turpin et al. (2023) in its reference list; I searched it.
- Not in the bib, as leads: Guan et al. (2026), "Monitoring monitorability" (ICML 2026), the framework this paper extends; Emmons et al. (2025a), evasion of CoT monitors; Arnav et al. (2025), "CoT Red-Handed".

## Caution

All scores come from one monitor model that knows the answer; capability is proxied by pass rate on eight models; the capability correlation rests on eight points. The closed models' traces are provider summaries. The stress tests are prompts, not training. Tasks are objective, so nothing here covers the open-ended coordination the paper discusses.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the arXiv v4 PDF (68 pp.) and extracted it twice (layout and raw). Checked 7 verbatim quotations (all exact), Table 2 ranges (91.6-98.8, 48.9-88.1, 83.6-87.6, 1.1-17.9, 81.4, 83.8-95.2), Table 3 and the p. 9-10 text (Pearson r -0.87 to -0.39, 24 point CoT-vs-action gap, omission rather than obfuscation), the human-check F1 values (85.31, 91.86, 92.13; three expert annotators), 1,514 instances / 19 tasks / 7 categories, the model list, and the Chen, Korbak, Baker, Lanham, Kutasov and Greenblatt relations plus the absence of Turpin.

**Findings:** One change: the read-depth line said full_text while stating that the appendix prompt listings (A.5.4-A.5.5) and task examples (A.6) were not read, about 38 of 68 pages; changed to partial and kept the list of what was not read. No quotation, number or locator errors found. Not verifiable from text: the exact order of the 7.8 and 7.2 figures between the Direct Concealment and Monitor-aware Evasion columns (the card does not assign them).
