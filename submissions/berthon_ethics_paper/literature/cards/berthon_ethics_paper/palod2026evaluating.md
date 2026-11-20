---
citekey: palod2026evaluating
title: Evaluating the False Trust Engendered by LLM Explanations
authors: Palod, Vardhan; Biswas, Upasana; Kambhampati, Subbarao
year: 2026
type: article
doi: null
venue: arXiv preprint arXiv:2605.10930v2 [cs.HC], 15 May 2026
source_basis: partial-text
pages_read: "pp. 1-9 (all main text: abstract, introduction, related work, protocol, results, discussion, limitations, conclusion); appendices pp. 10-29 not read"
source_url: https://arxiv.org/pdf/2605.10930v2
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/arx_palod2026/page.pdf
sha256: afc04ce6801fbbdd8498a56c69620649e71d1e1fbc0361b714933b145b049f2c
manuscript_lines: []
ledger_rows: [H24, H22, E15]
premises: [A4, A8]
facet: N1
anthropic_authored: false
verified: corrected
written: 2026-10-24
---

## Summary
A between-subjects study (25 Prolific participants per condition, five conditions) of whether explanations help lay
users tell correct from incorrect AI answers on hard JEE-Bench problems they cannot solve. Conditions: answer only;
the full DeepSeek R1 reasoning trace; a summary of that trace (the form frontier vendors show); a post-hoc explanation
for the answer; and a "dual" explanation giving arguments for and against. Pro-answer explanations raised acceptance
of both correct and incorrect answers; raw traces raised acceptance of correct answers (75.0 vs 60.4) but not of
incorrect ones (54.0 vs 54.2); only the dual explanation lowered acceptance of wrong
answers below baseline. Users rated the raw traces the least helpful of the explanations.

## Key facts it relies on
- Vendors "do not show the actual reasoning traces which the models produced rather expose the users to what seems like
  a summarized version of the reasoning traces" (p. 2; the sentence names OpenAI, Google and Anthropic).
- Design: "Participants were randomly assigned to one condition, with 25 participants per condition" (p. 5); each saw
  8 problems, 4 answered correctly by the AI and 4 incorrectly (p. 4).
- Table 3 (p. 6): misjudgment (accepting an incorrect answer) was 54.2% for answer only, 54.0% for the reasoning trace,
  51.0% for the reasoning summary, 58.0% for the pro-answer explanation, and 46.9% for the dual explanation.
- "reasoning traces and post-hoc explanations are persuasive but not informative: they increase user acceptance of LLM
  predictions regardless of their correctness" (abstract, p. 1).
- "Reasoning traces, supposedly the provenance explanations, were rated as least helpful with only 56.5% of responses
  being rated as helpful" (p. 8).

## Critical notes from the literature
- Preprint; small cells (n = 25), no significance tests reported in the main text for the condition differences.
- The abstract's "persuasive but not informative" outruns Table 3 for the raw trace: its misjudgment rate (54.0%)
  equals the baseline's (54.2%); the trace raised acceptance of correct answers (75.0% against 60.4%), not of wrong
  ones. Table 1 likewise shows the highest false-trust rate for answer only (47.3%), which footnote 3 explains away.
- Lay participants on exam problems; not deployment, not agent actions.

## Where the argument uses it
- M3 / P9 (who reads chain of thought, and with what effect): supports a narrow claim. Lay readers shown reasoning
  traces or their summaries did no better than baseline at rejecting wrong answers; a design that presents arguments
  against the answer did. Holds as stated; does not hold for "traces mislead" in general.
- A8: the reader P9 would need is not shown to exist among lay users; the study tests no expert reader.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
