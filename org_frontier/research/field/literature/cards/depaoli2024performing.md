---
citekey: depaoli2024performing
title: Performing an Inductive Thematic Analysis of Semi-Structured Interviews With a Large Language Model: An Exploration and Provocation on the Limits of the Approach
authors: De Paoli, Stefano
year: 2024
doi: 10.1177/08944393231220483
arxiv: null
journal: Social Science Computer Review
programs: [field]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://rke.abertay.ac.uk/ws/files/81658175/DePaoli_PerformingAnInductiveThematicAnalysis_Published_2024.pdf
sha256: 5d7298f03029e4604c6d2844d59a4c9dfb27d55909cf4da5948a76a54f5cfc54
pdf_path: literature/pdfs/depaoli2024performing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper investigates whether the LLM GPT-3.5-Turbo can perform an *inductive* Thematic Analysis (TA) of semi-structured interviews, framed as both an exploration and a "provocation" aimed mainly at social scientists (prior work had focused on deductive coding). De Paoli re-analyses two open-access interview datasets previously analysed by other researchers — a "gaming" dataset (13 videogame-player interviews) and a "teaching" dataset (10 interviews with university instructors using quantitative data) — using the OpenAI API and Python scripts. He maps Braun and Clarke's (2006) six TA phases onto the LLM, arguing only Phases 2–5 are reasonably approachable (Phase 1 familiarisation and Phase 6 write-up are excluded). Codes and themes are generated entirely inductively (no pre-defined codebook), then compared with the original researchers' themes by name and description. The model inferred most main themes: for the gaming dataset it inferred 9 of the 13 original themes at Phase 3, while it never inferred "psychological perspective" or "violence and aggression," and it surfaced some themes (e.g., student collaboration) the original analysts had not considered. De Paoli concludes that inductive TA with LLMs is viable and offers "a good degree of validity," but stresses the need for methodological procedures, attention to prompting, temperature, hallucination, ethics, and Human-AI collaboration rather than uncritical tool-building.

## Key facts it relies on
- The experiment used GPT-3.5-Turbo via the OpenAI API and Python scripts; the model's token limit at the time was 4097 tokens including both prompt and response, and the model has no memory of past prompts.
- Two datasets: the "gaming" dataset = 13 player interviews (young people aged 18–26) from the EU "gaming-horizons" project; the "teaching" dataset = 10 interviews with instructors at UC Santa Barbara who use quantitative data to teach undergraduates.
- Interviews were chunked at roughly 2500 tokens each (3000 occasionally hit the limit), yielding 56 chunks for the gaming dataset and 35 chunks for the teaching dataset.
- Phase 2 (initial codes): the model was prompted to infer 3 codes per chunk, each with a 3-word name, a 4-line description, and one quote; this produced 161 codes from the gaming dataset and 101 from the teaching dataset.
- A code-reduction prompt (merging similar codes) reduced the gaming codebook from 161 to 89 codes and the teaching codebook from 101 to 63 codes.
- Phase 3 (themes): using 89 gaming codes the model was asked for 11 themes (original researchers had 10 themes plus 3 sub-themes); using 63 teaching codes the model was asked for 7 themes (original had 5 themes plus 3 sub-themes).
- Comparison criteria were (1) similarity of LLM theme names to original theme names and (2) similarity of theme descriptions even when names differ; for the gaming dataset the model inferred 9 of the 13 original themes at Phase 3, with one more found at Phase 4 and two present only as codes; "psychological perspective" and "violence/aggression" were never inferred as themes.
- Method follows Braun and Clarke's (2006) six TA phases ("(1) familiarising... (2) generating initial codes; (3) searching for themes; (4) reviewing themes; (5) defining and naming themes; (6) producing the report"); only Phases 1–5 (analysis-relevant: 2–5) were attempted, Phase 6 excluded due to debate over LLM scientific writing.
- The temperature parameter (range 0–2) was used to operationalise Phase 4: T=0 reproduces output deterministically; the author ran Phase 4 at T=1 (gaming) and T=1 then T=0.5 (teaching) across three tests to check theme consistency/validity.

## Critical notes from the literature
- The author explicitly frames the work as an "initial experiment" and a "provocation," not a comprehensive reproduction of inductive TA, and does not seek to establish formal procedures.
- Prompting was difficult and inconsistent: even slight wording changes or changing the requested number of themes yielded different results, due to the probabilistic nature of LLM outputs; results are only valid for the specific prompts and chunks used.
- Hallucination occurred (e.g., during Phase 3 code reduction the model generated new code names; the code "Gender and Diversity in eSports" was misassigned to the "Education" theme in Table 3); passing a dataframe index in the prompt mitigated some hallucination, but the author deliberately left some errors uncorrected to foster discussion.
- The model could not perform Phase 1 (familiarisation) or genuine interpretation of latent meaning; De Paoli notes LLMs work on "structural and probabilistic elements of language" rather than meaning (citing Floridi 2023, Hao et al. 2023), and Phases 4–5 in particular rely heavily on human interpretation and the author's own judgement.
- Ethics is flagged as a grey area: interviews must be fully anonymised before being sent to a cloud model, and using LLMs on newly generated interviews would require informing respondents and obtaining consent; De Paoli critiques prior LLM-coding work (Gao et al. 2023; Xiao et al. 2023) for prioritising tool-building over methodological reflection (echoing Baden et al. 2022).

## Key topics covered
Inductive thematic analysis; Braun and Clarke six-phase TA; GPT-3.5-Turbo; OpenAI API; qualitative coding with LLMs; codebook reduction; prompt engineering; temperature parameter; token limits and chunking; LLM hallucination; Human-AI collaboration; human-in-the-loop; deductive vs inductive coding; validity in qualitative analysis; reproducibility; research ethics for LLM data processing; semi-structured interviews; social science computational methods.
