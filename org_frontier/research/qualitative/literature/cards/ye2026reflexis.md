---
citekey: ye2026reflexis
title: Reflexis: Supporting Reflexivity and Rigor in Collaborative Qualitative Analysis through Design for Deliberation
authors: Ye, Runlong and others
year: 2026
doi: 10.1145/3772318.3791275
arxiv: null
journal: 
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2601.15445
sha256: ea5929cc8f341e93084d074086067cc14046c8c63c5d0017935d2ea1824ec9cd
pdf_path: literature/pdfs/ye2026reflexis.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Reflexis is a web-based collaborative workspace (CHI '26) for Reflexive Thematic Analysis (RTA) that, instead of automating coding for speed or enforcing inter-coder reliability, deliberately "designs for deliberation" by embedding researcher reflexivity, transparent code evolution, and principled disagreement into the analysis loop. The authors argue prevailing QDA tools (NVivo, ATLAS.ti) and recent LLM "auto-coder" systems optimize for speed and convergence, shrinking the interpretive space that makes RTA rigorous. Reflexis operationalizes three mechanisms tied to design goals from a formative study (survey N=55 + interviews N=3): in-situ reflexivity prompts (ReflexiveLens), automated code-evolution tracking with a Code Drift Alert and analysis-history provenance views, and positionality-aware discussion scaffolds (Discussion Focus). AI assistance is deliberately narrow and advisory (assist reflection/discussion, never generate or suggest codes), using OpenAI GPT-5 and GPT-5-mini. A single-condition paired-analyst study with 12 experienced qualitative researchers (6 pairs) using Reflexis as a conceptual probe found it shifted reflection from delayed, high-level habits toward granular in-situ practice, made code evolution transparent and auditable (universally valued), and reframed disagreements as productive, positionality-grounded dialogue. The evaluation also surfaced design tensions: desire for higher-level/networked memos, more user control over the timing of proactive drift alerts, and epistemic risks of "algorithmic essentialism" when operationalizing positionality.

## Key facts it relies on
- Formative study: survey of N=55 postgraduate researchers on Prolific (S1-S55, retained 55 valid responses, $16/hour ~ $8 for 30 min) plus N=3 semi-structured interviews with experienced RTA practitioners (2 PhD students, 1 professor; I1-I3, $20 each); IRB protocol #49033.
- Three formative challenges mapped to three design goals and five system features (Table 1): C1 Inconsistent Reflection Support to DG1 (in-situ reflexive exercises); C2 Untracked Code Evolution to DG2 (analytical history + code drift alert); C3 Inaccessible Collaboration Perspectives to DG3 (positionality-aware discussion prompts + discussion focus).
- Formative survey numbers cited: 40/55 "often"/"always" considered how experience shaped interpretation; 32/55 rely on a separate research journal; 37/55 update definitions and 31/55 split codes to manage drift, 29/55 relying on memory; 35/55 valued a partner's disciplinary perspective and 37/55 relevant lived experiences.
- Discussion Focus agreement metric uses percentage agreement = (count of highlights agreed by at least one other coder) / (total highlights contributed by all coders), chosen over Cohen's Kappa because Kappa can be statistically unsound for more than two coders; the metric is used to route attention, not to optimize agreement.
- Evaluation study: single-condition, 12 participants (P1-P12, 6 pairs), recruited via social media/Slack; 10/12 graduate students, 1 professor, 1 data analyst; 10/12 HCI background; mean 3.75 years QDA experience (min 1, max 7, median 4); sessions ~1.5-2 hours at $20/hour; IRB protocol #49033. No baseline condition; no task time, accuracy, or inter-rater reliability measured.
- Study used a synthetic, context-faithful corpus of three interview transcripts generated (via gemini-2.5-pro, chosen over gpt-5) from the prior CHI paper "Contestable Camera Cars" [Alfrink et al. 2023]; participants were not told the transcripts were synthetic. Protocol followed O'Connor and Joffe sequential coding (Coder 1 then Coder 2 blinded to Coder 1's assignments) then mediated discussion.
- Survey/observation findings: 10/12 agreed prompts encouraged articulating code rationale; 10/12 had neutral-to-positive in-flow prompt experience; 8/12 would keep reflective prompts enabled; 11/12 agreed Analysis History increased transparency; 7/12 said Code Drift Alert helped articulate code boundaries; 11/12 agreed Discussion Focus helped notice meaningful disagreements; 12/12 felt "in control of analytic decisions" and agreed the system "supported an iterative research process."
- LLM technical analysis: two co-authors post-hoc binary-coded every triggered Code Drift Alert (N=7) and Positionality-aware Discussion Prompt (N=18) as Relevant vs Irrelevant; raters reached perfect consensus and 100% of displayed drift alerts were judged relevant. They evaluated "relevance" (grounded, not hallucinated) rather than "correctness," per the interpretivist stance.
- Implementation: Next.js + Tailwind CSS frontend, React Flow for project-level history visualization, Firebase/Firestore for real-time collaboration and anonymous auth, immutable event log for every analytic action; uses OpenAI GPT-5 and GPT-5-mini at low-to-medium reasoning effort. Open-sourced at https://github.com/harryye930/reflexis.

## Critical notes from the literature
- Single-condition, time-limited (1.5-hour) single-session design on a synthetic dataset with 12 experienced researchers in pairs; the authors state findings speak to "initial use and perceived affordances rather than long-term change in practice," cannot capture longitudinal/non-linear project dynamics, and that synthetic data may narrow variability and "subtly steer theme salience."
- No baseline tool and no quantitative efficiency/reliability metrics; the authors justify this on interpretivist grounds (RTA is an "adventure, not a recipe"; no standard RTA toolchain) but acknowledge it limits claims about comparative effectiveness.
- The Code Drift Alert was polarizing: valued for sparking critical reflection and combating fatigue (P11), but its interruptive, proactive timing created friction (P9 asked it to "stop interrupting me"; P2 wanted it as an end-of-session review tool).
- Operationalizing positionality carries acknowledged epistemic risks: brief self-authored profiles risk "algorithmic essentialism" / flattening complex, intersectional, evolving positions; some participants found the Positionality-Aware Discussion Prompt "too long and too generic" (P2) or failing to incorporate their positionality (P4), and pairs often bypassed it for direct conversation. Authors did not study potential harms to marginalized researchers and frame results as "promise and risk" rather than validation.
- Not studied: larger teams (3+ lenses) or strong power asymmetries; the per-passage reflection scope did not fit participants (P1, P5, P6, P9) who reflect at higher/theme-level abstraction and wanted networked memos.

## Key topics covered
Reflexive Thematic Analysis (RTA); design for deliberation; researcher reflexivity; positionality; collaborative/team qualitative coding; in-situ reflection prompts (ReflexiveLens); analytical provenance (interaction vs insight/rationale provenance); code drift detection; codebook evolution (splits/merges/renames); principled disagreement; inter-coder reliability debate and percentage agreement vs Cohen's Kappa; positivism creep / "Big-Q" methods; human-AI collaboration; LLMs in QDA; advisory/non-prescriptive AI; algorithmic essentialism; conceptual probe / single-condition HCI evaluation; CHI/CSCW qualitative tooling.
