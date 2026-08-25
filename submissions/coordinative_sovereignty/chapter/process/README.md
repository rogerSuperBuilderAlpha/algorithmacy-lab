# Chapter writing process — archive

Completed passes for the IGI chapter. **Do not edit these to change the manuscript.**

| Path | What it is |
| --- | --- |
| [`sentence_pass/`](sentence_pass/) | Sentence-by-sentence rebuild against Aytac (argument) and Cutolo (applied): briefs, model transcription, outline, ledger, cadence notes. |
| [`cadence_rewrite.md`](cadence_rewrite.md) | Cadence pass (Aug 2026): recombined over-split sentences to the model length band. |
| [`author_voice_pass.md`](author_voice_pass.md) | Author-voice pass, dead-sentence sweep, and 25 Aug 2026 review adjudication (accepted/rejected with reasons). |
| [`gate_report.md`](gate_report.md) | Mechanical STYLE_SPEC gate on the draft before the sentence pass. |
| [`outline_v2.md`](outline_v2.md) | Section outline used during the Aug rebuild. |
| [`sentence_bank.md`](sentence_bank.md) | Candidate sentences held during drafting. |
| [`style_candidates/`](style_candidates/) | Register specimens. |
| [`drafting_ledgers/`](drafting_ledgers/) | Claim-defense notes from drafting. |

The submittable text is [`../chapter.md`](../chapter.md). Regenerate exports from there:

```bash
cd .. && python3 regen_exports.py
```

Superseded full drafts live in [`../../archive/drafts/`](../../archive/drafts/). The 25 August review-adjudication draft is [`../../archive/drafts/chapter_2026-08-25.md`](../../archive/drafts/chapter_2026-08-25.md). The midday author-voice draft (*Algorithmacy and Standing*) is [`../../archive/drafts/chapter_2026-08-25_standing.md`](../../archive/drafts/chapter_2026-08-25_standing.md).
