---
citekey: strachan2024testing
title: Testing Theory of Mind in Large Language Models and Humans
authors: Strachan, James W. A. and Albergo, Dalila and Borghini, Giulia and Pansardi, Oriana and Scaliti, Eugenio and Gupta, Saurabh and Saxena, Krati and Rufo, Alessandro and Panzeri, Stefano and Manzi, Guido and Graziano, Michael S. A. and Becchio, Cristina
year: 2024
doi: 10.1038/s41562-024-01882-z
arxiv: null
journal: Nature Human Behaviour
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41562-024-01882-z.pdf
sha256: 1c8cf5e026069f85ebe571c06e9170fb045b33112ae08c182aa9ff5c9163bc3e
pdf_path: literature/pdfs/strachan2024testing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether large language models exhibit behaviour indistinguishable from humans on theory-of-mind (ToM) tasks, and uses an experimental "machine psychology" approach to find out. The authors administered a battery of well-established ToM tests (false belief, irony, hinting/indirect requests, faux pas, strange stories) repeatedly to two LLM families (GPT-4, GPT-3.5, and LLaMA2-70B-Chat) and compared their performance against a large human sample (total N = 1,907). GPT-4 matched or exceeded human performance on identifying indirect requests, false beliefs, irony, strange stories and misdirection, but failed on the faux pas test; LLaMA2-70B was generally the worst model yet was the only one to beat humans on faux pas. Follow-up manipulations showed that LLaMA2's faux pas "superiority" was illusory (a bias toward attributing ignorance), while GPT's faux pas failure reflected hyperconservatism — a refusal to commit to the most likely explanation — rather than a genuine failure of inference. The authors conclude that LLMs produce outputs consistent with mentalistic inference but respond differently from humans under social uncertainty, and stress the need for systematic, repeated testing against validated human benchmarks.

## Key facts it relies on
- Total human sample was N = 1,907 participants, recruited via Prolific (native English speakers, ages 18-70, no psychiatric/dyslexia history); 13 participants were excluded for LLM-generated or non-answering responses.
- The ToM battery used five test types: hinting task, false belief task, faux pas recognition, strange stories, and an irony test; the theory-of-mind battery stage compared LLMs against 250 human participants, with each test delivered to GPT-4, GPT-3.5 and LLaMA2-70B across 15 independent chats/sessions.
- For each published test, the authors generated novel items matching the original logic but with different semantic content, to control for training-set replication.
- On the original battery: GPT-4 significantly outperformed humans on irony (P = 0.040, r = 0.32), hinting (P = 0.040, r = 0.32), and strange stories (P = 1.04 x 10^-5, r = 0.60); both humans and all LLMs performed at ceiling on false belief.
- On faux pas, GPT-4 scored below humans (P = 5.42 x 10^-5, r = 0.55) and GPT-3.5 was near floor (P = 5.95 x 10^-8, r = 0.72), while LLaMA2-70B outperformed humans (P = 0.002, r = 0.44), achieving 100% accuracy in all but one run.
- The overwhelming majority of GPT faux pas errors said there was "not enough information" to be sure; only two responses out of 349 reported that the character did know.
- In the faux pas likelihood test (asking whether it was "more likely" the speaker knew or did not know), GPT-4 reached perfect performance and GPT-3.5 improved (requiring prompting on ~3% of items, failing to recognize the faux pas on ~9%), supporting the hyperconservatism hypothesis over the "failure of inference" and "Buridan's ass" alternatives.
- In the belief likelihood test (faux pas / neutral / knowledge-implied variants, total N = 900 humans), GPT-4 discriminated all three variants like humans, but LLaMA2-70B showed no differentiation between neutral and knowledge-implied (chi^2(1) = 1.80, P = 0.180), and both GPT-3.5 and LLaMA2-70B never reported uncertainty, exposing LLaMA2's faux pas success as an ignorance-attribution bias.
- LLaMA2-Chat models used temperature 0.7, max 512 new tokens, repetition penalty 1.1, Top P 0.9, with the system prompt "You are a helpful AI assistant"; only the 70B model is reported in the main text because 7B/13B produced too many non-codable responses.

## Critical notes from the literature
- The authors note that LLM success on false belief may have "lower-level explanations than belief tracking"; in a control with perturbation variants they replicated GPT's poor performance, but also found that human participants (N = 757) failed on half of these perturbations, complicating the human-machine comparison.
- The paper frames its central finding as a dissociation between competence and performance: GPT models may be "competent" to compute mentalistic-like inferences but do not spontaneously compute them to reduce uncertainty, attributing this partly to mitigation/inhibition measures (anti-hallucination training) in GPT architecture rather than to ToM ability per se.
- The authors caution that matching human output does not imply human-like underlying cognition; they explicitly point to Supplementary Information section 7 showing GPT's improved faux pas performance "may not necessarily reflect perfect or human-like reasoning."
- GPT models are described as closed, evolving systems; the authors flag reproducibility concerns and note GPT-4's 25-message-per-3-hours limit at the time, motivating inclusion of open-weight LLaMA2.
- Findings are tied to specific model versions tested in 2023 (GPT-4, GPT-3.5, LLaMA2); the authors emphasize the LLM landscape is fast-moving and that conclusions depend on systematic testing and validation against human samples.

## Key topics covered
Theory of mind; machine psychology; false belief task; faux pas recognition; hinting/indirect requests; irony comprehension; strange stories; GPT-4; GPT-3.5; LLaMA2-70B-Chat; hyperconservatism hypothesis; Buridan's ass hypothesis; failure-of-inference hypothesis; ignorance-attribution bias; competence vs performance dissociation; social uncertainty; species-fair comparison; novel-item controls; LLM evaluation.
