# Cadence rewrite against the model band — 24 August 2026

Full pass over all eleven sections plus the abstract, rewriting to Aytac's sentence-length distribution while holding the argument, citations, figures, and quotations fixed.

## Model benchmark

Computed from `sentence_pass/_sources/aytac2024.txt`, body prose only (front and back matter excluded), word counts excluding parenthetical citations. A defect in the first measurement was found and fixed during this pass: abbreviations in the splitter matched inside words, so "wired." and "gap." were read as "ed." and "p." and destroyed sentence boundaries. All figures below use the corrected splitter.

Model: n = 373, mean 23.89, sd 9.86, min 6, **P10 = 12**, median 23, **P90 = 36**, max 70. The band [12, 36] is the model's central 80 percent. MODEL.md's own recorded figures were not used, since they are rounded to multiples of two and contain a zero entry.

## Result

| | before | after | model |
|---|---|---|---|
| sentences | 560 | 467 | 373 |
| mean | 18.74 | **22.73** | 23.89 |
| sd | 11.02 | **9.74** | 9.86 |
| below 12 words | 30.4% | **13.7%** | 10% |
| above 36 words | 8.2% | **8.4%** | 10% |

Per section, after the rewrite: §1 7.9/10.5, §2 17.1/2.9, §3 11.1/3.2, §4 16.7/11.9, §5 19.5/10.4, §6 27.6/6.9, §7 13.8/10.3, §8 5.0/5.0, §9 8.3/10.4, §10 16.7/5.6, §11 7.1/14.3 (short percent / long percent).

## What was wrong and what was done

The diagnosis was over-splitting, not verbosity. Of 158 short sentences in the previous draft, 82 sat in runs of two or more consecutive fragments, and the dominant pattern was "X. It does not Y." The sentence pass had applied the house ban on X-not-Y constructions by splitting every contrast into two sentences, where the model carries contrast inside one sentence through subordination. The remedy was recombination with conjunctions and subordinate clauses, not padding.

Short sentences were kept wherever they do the work the model gives them: verdicts ("The object of sovereignty is the shape"), enumeration announcements ("The normative grounds are four"), question hinges ("Who bears the standing, a person or a firm?"), and imperative case-introductions ("Run the bypass on each function"). Aytac's own floor is 6 words and his shortest are load-bearing. Sections still above 10 percent short, notably §5 and §6, carry that excess entirely in announcements and verdicts, and §6's count includes one splitter artifact on a pinpoint citation rather than prose.

Long sentences were split where they were merely combined clauses and kept where they are announced enumerations, which the model also writes up to 70 words. The canonical §2 definition is exempt by STYLE_SPEC and was left at 50 words.

## Verification

Mechanical gate G1 through G16: zero flags. No em-dash, no first person, no authorial hedge, no metadiscourse, no banned string.

Citation parity: 190 in-text instances before and after. Two changes, both house-conforming and to the same sources, moving author-led citations to terminal position under G7: "Nanni et al. (2024)" and "Repetto (2025)". Reference list, Legislation, Cases, Additional Reading, and Key Terms are byte-identical to the previous version.

Content parity: all 61 numeric tokens present, all fifteen legal instruments and cases present, and all five verbatim quotations intact, including the Selznick passage, the Habermas locator, the Cohen page pins, the Curchod abstract phrase, and the ancillary-restraints quotation from Case C-264/23.

Body words 11,565 to 11,686. Abstract unchanged at 143 words, since its one long sentence is an announced enumeration and its wording is the locked recast claim.

## Still owed

The second QA pass, a sentence read by a reviewer who did not draft, and the author's read-aloud of §2 and §5. Housekeeping closed 24 Aug: `chapter_v3.md` promoted to `chapter.md`, exports regenerated, process files moved under `process/`, pre-rebuild draft archived as `archive/drafts/chapter_2026-08-18_pre_sentence_pass.md`.
