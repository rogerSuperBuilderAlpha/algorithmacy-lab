<!-- DRAFTED BY CLAUDE (Fable 5.2), 11 Nov 2026. Brief for the claim audit of DRAFT_v6 in run rr-2026-11-k. Read RUN_BRIEF_K.md first; its guards apply here. -->

# Claim audit: brief

**The job.** Decide, for every proposition in your batch of `manuscript/DRAFT_v6.md`, whether the source it rests on licenses it. An earlier verification checked that quotations matched their sources word for word and missed everything else: paraphrases that changed the population or the setting, scenarios of the paper's own credited to a source, hedges dropped, cases described beyond what they held. Your audit exists to catch those.

Root: `/Users/ludwitt/iit-playground/wt-hs-rr/submissions/hospitality_phygital/`.

## Inputs

- `manuscript/DRAFT_v6.md`: the text under audit. Use it as it stands today.
- `manuscript/rewrite_2026-11/sbs/LEDGER.md`: the sentence ids (S-001 to S-278, with S-150a and S-150b; A-1 to A-6 for the abstract). Where an entry has an 'As written' line, the last one is the current sentence. **Do not trust its 'Truth' lines**; many cite an earlier draft, not a source.
- Sources, in order of preference: the saved full texts under `manuscript/revision_2026-11/research/sources/<citekey>/` and `manuscript/rewrite_2026-11/journal/corpus/<key>/`; an open copy you fetch yourself (no logins, no bot checks); the abstract. `library/cards/<citekey>.md` tells you which text was read and where it is saved. **A card is a finding aid, never evidence**: cards have been wrong.
- `manuscript/keystone_2026-11/CLAIMS_FIXED.md`: K1–K9, for classifying the paper's own inferences.

## Unit: the proposition

Split each sentence into the separate things it asserts. A sentence about a case may hold four (who was sued, what was held, on what doctrine, with what qualification). Number them S-108.1, S-108.2 and so on. The six questions of the test and every cell of Tables 1 and 2 are propositions too (ids such as S-186.q3, T1.r2.c4).

## Type, and what to check for each

| Type | Check |
|---|---|
| **Quotation** | The exact words at the locator; who says them (the author, or someone the author reports); what the surrounding sentences do to their meaning. |
| **Paraphrase** | Paste the passage that licenses it. Then test each mismatch class below. |
| **Case description** (a study or a judgment described) | As paraphrase, plus: is every detail in the source, or is some of it the paper's own scenario? |
| **Legal proposition** | From the primary text only: court and jurisdiction; holding, dictum or dissent; conditions in the same section or paragraph; whether later treatment was checked (say 'not checked' if not). |
| **Empirical generalization** | The study's design, sample and setting; whether the sentence generalizes beyond them; any contrary evidence you know of in the library. |
| **Own inference** | Write it as numbered premises and a conclusion. Tag each premise: a sourced row, an earlier inference, a stipulation, or an assumption. Then see 'Testing inferences'. |
| **Definition or stipulation** | Is the term then used in that sense everywhere in your batch? List each use in another sense. |
| **Gap claim** ('no study…', 'the literature does not…') | Search the library first, including cards marked held or rejected (`grep` the cards). Then run at least two database queries that try to refute it, and log them. |
| **Signpost** | No check; record it and move on. |

**Mismatch classes** (the ones found on 11 Nov). For every paraphrase and case description, answer each:

1. **Population**: are the people the same (guests, respondents in a vignette, workers, students)?
2. **Setting**: same industry, country, period, kind of establishment?
3. **Strength**: has a hedge been dropped ('may', 'likely', 'could') or a quantifier widened?
4. **Speaker**: is it the author's finding, the view of people the author studied, or someone the author cites?
5. **Scope**: does the source's statement cover what the sentence applies it to?
6. **Design**: is a forecast, a vignette, a lab study, an editorial or a single case presented as an observed general fact?
7. **Application**: is the paper's own application or scenario presented as the source's?
8. **Version**: is the locator a page of the version in the reference list?

## The rule that decides a verdict

**No passage, no 'supported'.** A row is 'supported' only if you have pasted, from the source's own text, the passage that licenses the proposition (at most about 60 words, with locator), and every mismatch class is clean. If you could reach only an abstract, the best verdict is 'supported (abstract only)', and only for what the abstract itself says.

**Verdicts.** `supported` · `supported (abstract only)` · `partial` (say which class fails) · `contradicted` · `unverifiable` (closed text; say what would settle it) · for inferences: `valid` · `valid with added premise` (state it) · `equivocal` (a term changes sense) · `overgenerates` · `undergenerates` · `invalid`.

## Testing inferences

For each own inference, after writing its premises:

- **Counter-model.** Can the premises be true and the conclusion false? Describe the case.
- **Terms.** Track the sense of *authority*, *answer / answerable*, *standing*, *accountability*, *duty / obligation*, *holding out*, *reach / reachable* across the premises.
- **Quantifiers.** 'Rarely', 'often', 'every', 'no': does the conclusion's quantifier follow?
- **Overgeneration.** Would the same argument prove the same duty of a bank, an airline or a hospital? If yes, say whether the paper concedes it.
- **Undergeneration.** Does it fail for a restaurant, a guest placed by a third party who pays, or a short-term rental?
- **K claim.** Which of K1–K9 the inference instantiates, or 'none'.

## Depth by section

- **Introduction, 'Assembled hosts at the touchpoint' (all four subsections), Conclusion, abstract and tables:** the full audit above, row by row. Most of these sentences will survive into the next draft.
- **'The host's power and the host's obligation' and 'Delegation and standing':** these sections will be rewritten. Audit every source use fully (so that the sources can be reused or dropped with confidence) and every inference fully, but do not spend effort on wording.

## Output

Write `manuscript/keystone_2026-11/claims/CLAIM_REGISTER_<batch>.md` and nothing else. Do not edit any other file; do not commit.

For each sentence:

```
### S-108 · Delegation and standing ¶3
> the sentence as it stands

| Row | Proposition | Type | Source, version, locator | Passage (from the source) | Classes failed | Verdict | K | Action |
|---|---|---|---|---|---|---|---|---|
```

For an inference, put the premises, the tests and the verdict in a short list under the table.

End the file with:

1. counts by verdict;
2. the fifteen rows that most endanger the paper, ranked, one line each;
3. every source you could not read in full, with the rows that wait on it;
4. every gap claim, with the queries you ran;
5. sources in your batch that should be dropped, and sources you found that should replace them (as leads: record and where found).

**Report back** in at most 250 words: counts by verdict, the five most damaging rows, and anything a second reader should check hardest.
