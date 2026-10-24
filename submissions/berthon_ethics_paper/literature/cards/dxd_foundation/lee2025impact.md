# Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–22). ACM. https://doi.org/10.1145/3706598.3713778

**Identifier:** doi:10.1145/3706598.3713778 · **Read depth:** full_text (the authors' version posted by Microsoft Research, 23 pp., CC BY 4.0; it states that the definitive version is the CHI 2025 paper; its page breaks may differ from the ACM version, so I give section numbers with author-version pages; I read the body, Tables 1–4 and Figure captions; I did not read the appendix survey instrument or codebook line by line) · **Source-tier:** proceedings (CHI, peer-reviewed) · **Evidence basis:** direct_read · **Design and sample:** online survey on Prolific of 319 knowledge workers who use GenAI at work at least weekly, each describing three real tasks (936 examples retained); mixed-effects logistic and linear regressions on self-reported enaction of critical thinking and perceived effort on Bloom's six activities, with Benjamini–Hochberg correction; open coding of free text · **Parties modeled:** person–system (a worker and a GenAI tool) · **Facets:** none (cited only in DRAFT_v2 §2.1) · **Read:** 2026-10-14

## What it argues

Lee and colleagues ask when knowledge workers perceive that they think critically while using GenAI and when GenAI changes the effort of doing so (§1). Participants reported enacting critical thinking for 555 of 936 examples (about 60%) (§3.3.1, §4.2, p. 9). Confidence in the AI doing the task was negatively associated with enacting critical thinking (β = −0.69, p < 0.001); confidence in doing the task oneself (β = 0.26) and in evaluating AI output (β = 0.31) were positively associated (§4.2.1, Table 4). In most examples, workers rated critical-thinking activities as less effortful with GenAI: 72% of Knowledge examples, 79% Comprehension, 69% Application, 72% Analysis, 76% Synthesis and 55% Evaluation were rated "less" or "much less" effort (§5.1, p. 12).

Qualitatively, critical thinking shifts "from information gathering to information verification", from problem-solving to response integration, and from task execution to "task stewardship" (§5.2, §6.2). Workers who rely on the tool for tasks they think simple often skip checking: "I knew ChatGPT could do it without difficulty, so I just never thought about it" (P275, §4.3.2). The authors say GenAI "may also reduce critical engagement, particularly in routine or lower-stakes tasks in which users simply rely on AI" (§1, p. 2).

Limits the authors state: all measures are self-report; participants "occasionally conflated reduced effort in using GenAI with reduced effort in critical thinking" (§6.3, p. 15); self-confidence may be miscalibrated; the sample is English-speaking, younger and tech-skilled; and "Our analysis does not establish causation" (§6.1.1).

## Relation to the argument

**Ruling D7 and premise P9.** The paper fits the draft's picture of the output-inspection burden: with GenAI, effort moves to verifying and integrating output. It also shows that verification is the main form critical thinking takes, which is a reading task. That supports the draft's claim that LLM interfaces leave the user to check after the fact.

**What it cuts.** The paper's own design remedy is partly a literacy remedy: "providing explanations of AI reasoning, suggesting areas for user refinement, or offering guided critiques" (§6.1.2) and feedback that helps users gauge reliability, which it says "aligns with the goals of explainable AI" (§6.1.1). That runs against D3's position that disclosure is the weaker kind of intervention. The draft can cite the problem it documents without adopting its remedy, but should say so.

**Use in DRAFT_v2:** Line 35: "Operators must read through fluent, probabilistically generated text to catch subtle errors or misalignment, and knowledge workers report reduced critical engagement when they do (Lee et al., 2025)." **Partly supported.** The paper supports "knowledge workers report reduced critical engagement" in a hedged form: higher confidence in GenAI is associated with less self-reported critical thinking (§4.2.1), and GenAI "may also reduce critical engagement" in routine or low-stakes tasks (§1). "When they do" misplaces the finding. The reduction is associated with *not* reading closely, when workers trust the tool; workers more confident in their own ability reported more critical thinking and more effort in Evaluation (β = 0.10, §5.1.1), and participants described increased effort on "AI stewardship", including "assessing if the AI response meets their quality standards" (§5.2.3). Even so, 55% of Evaluation examples were rated less effortful with GenAI (§5.1). The measures are self-reports of perceived effort and enaction, not observed engagement. A closer wording would be "and knowledge workers who trust the tool more report less critical thinking."

## In conversation with

- `bucinca2021trust` — cited for cognitive forcing functions reducing overreliance compared with simple explanations (§2.2).
- `bainbridge1983ironies` — the "ironies of automation", cited in §1 and §4.3.2 for skill atrophy.
- `parasuraman2010complacency` — not cited here; the older automation-complacency account of the same confidence effect.
- Not in the bib, as leads: Simkute et al. (2024), "Ironies of generative AI" (cited §4.3.2; the draft cites Simkute et al. 2024 at line 35); Tankelevitch et al. (2024), the metacognitive demands of GenAI (§4.1); Sarkar (2023/2024) on "mechanised convergence" (§1); Brachman et al. (2024) on knowledge-worker GenAI task types (§3.1.1); Drosos et al. (2024) on goal–query workflows (§4.1.1).

## Caution

A cross-sectional self-report survey; the regressions are associations. "Critical thinking" is operationalised through Bloom's taxonomy and participants were primed with examples (§3). The paper concerns single users and a tool, not mediated coordination. The authors' version may paginate differently from the ACM PDF; section numbers are the safer locators.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the authors' version saved at dxd_foundation_local/pdfs/R4b/lee2025.pdf (23 pp.) and searched or read the passages behind every claim. Quotations checked word for word: "may also reduce critical engagement, particularly in routine or lower-stakes tasks in which users simply rely on AI" (pdf p. 2), P275's "I knew ChatGPT could do it…" (p. 11), the §5.2 headings ("From information gathering to information verification", "task stewardship"), "Our analysis does not establish causation" (§6.1.1, p. 14), "aligns with the goals of explainable AI" (§6.1.1, p. 14), "providing explanations of AI reasoning, suggesting areas for user refinement, or offering guided critiques" (§6.1.2, p. 15) and "occasionally conflated…" (§6.3, p. 15). Numbers checked: 555 of 936 (about 60%, p. 9); β = −0.69 (p < 0.001), 0.26 (p = 0.026), 0.31 (p = 0.046) in §4.2.1 and Table 4; the six "less/much less effort" percentages 72/79/69/72/76/55 (§5.1, p. 12). The record matches Crossref (seven authors, CHI 2025, pp. 1–22). I re-read DRAFT_v2.md line 35.

**Findings:**
1. All quotations, numbers and section locators match.
2. Corrected: the card's support for "workers who did inspect output reported more evaluation effort" cited §5.1.1 and §5.2.3 loosely. §5.1.1 is about self-confidence (higher self-confidence goes with more perceived effort in Application and Evaluation), and §5.2.3 describes more effort on "AI stewardship". The sentence now says exactly that and adds that 55% of Evaluation examples were still rated less effortful.
3. The "Use in DRAFT_v2" verdict (partly supported; "when they do" misplaces the finding, which is tied to confidence in the AI and is self-reported) stands. The point that the paper's own remedies include explanation features, which cut against D3, is accurate (§6.1.1, §6.1.2).
