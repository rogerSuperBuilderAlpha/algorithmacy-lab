# The foundation paper for Decision Experience Design

**Status (2026-10-13):** researched in three rounds, audited, carded and outlined. The author ruled on the
ten decisions on 2026-10-13 and then asked Claude for an abstract, an introduction and a section outline:
Claude drafted one, the author replaced it with a Gemini-written version in a Google Doc, and
[`DRAFT.md`](DRAFT.md) is a snapshot of that doc with Claude's edits and citation bullets marked. The
author then supplied a full draft; [`REVIEW_v2_2026-10-13.md`](REVIEW_v2_2026-10-13.md) reviews it and
[`DRAFT_v2.md`](DRAFT_v2.md) is the repaired version, with a rebuilt reference list and a table of every
change. [`DRAFT_v3.md`](DRAFT_v3.md) (2026-10-14) applies the claim check in `literature/audit/claims/`
and reties the essay to one argument in three moves. Version 2 is left in place so those line numbers still match. The target journal is *Human–Computer Interaction* ([`venue/`](venue/)). Claude wrote every file in this arm, and
none of the wording is the author's unless quoted.

**Where the research stands.** [`literature/facets/T_adjudication.md`](literature/facets/T_adjudication.md)
§9 and §10 are the current statement, and [`ARGUMENT_MAP.md`](ARGUMENT_MAP.md) follows it. In brief: readers used
to spaces lose a third to a half of their speed without them, and that dependence is the robust fact;
no source credits word separation with spreading literacy, and the nearest support for a shortened
training is one sentence of Saenger's (1997, p. 85). Word separation re-represented the page without
disclosing anything, which is what the paper needs from it. The author's rulings oppose *disclosure* as
a literacy-based intervention and move the engagement layer from reading and rewriting to deciding. The
evidence on disclosure is mixed in direction; no convention has been tested in a triad; and in courts,
dealer foreign exchange and platforms the third party yielded a convention only under outside force.
Nadella's insider post offers a person a record to read and a brake, and is silent on the people the
model acts upon.

A paper for PHD1750-3 / HF700-1, Foundations in Human Factors (Bentley, Fall 2026). It replaces the DIAL
response ([`../dial_response_algorithmacy/`](../dial_response_algorithmacy/)) as the course paper and is
meant to found the Decision Experience Design series
([`../decision_experience_design/`](../decision_experience_design/)).

**The argument under test.** Scribes moved from *scriptio continua* to spaces between words and so took
the work of finding words off the reader. Algorithmacy needs a move of the same kind. Satya Nadella's
post of 10 October 2026, "Models as Insider Risks in the Super Intelligence Era", proposes the opposite:
observation and containment by the organisation. See [`CLAIM.md`](CLAIM.md).

## Files

| File | Use |
| --- | --- |
| [`SOURCE.md`](SOURCE.md) | The author's instruction, answers and ten rulings, the course facts, the Nadella post record, the author's own sentences the paper keeps |
| [`CLAIM.md`](CLAIM.md) | The provisional claim, the two hypotheses on the history, and what not to claim |
| [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) | Terms, standing rulings, the four problems, the ten facets, the facet file format and rules |
| [`literature/REUSE.md`](literature/REUSE.md) | What the lab's other arms already hold, with recorded read depths |
| `literature/facets/` | Ten research facets (A–H, X, Z), three from the second round (I, J, K) and five from the third (L–P), one `.md` and one `.bib` each, then [`T_adjudication.md`](literature/facets/T_adjudication.md) |
| `literature/references.bib` | Built by `python3 literature/merge_bibs.py` from the facet bibs (first facet wins) |
| `literature/audit/` | `AUDIT_01`–`11.md` (every quotation and number in the facet syntheses, re-checked by independent agents), `CARD_FACET_CHECKS.md` (where a full reading disagreed with a facet), `DOI_CHECK.md` (written by `check_dois.py`), `BIB_CHANGES.md` |
| [`literature/library/`](literature/library/INDEX.md) | The contextual bibliography: 251 cards, one per source read from full text, each re-checked by a second agent. [`INDEX.md`](literature/library/INDEX.md) lists them by facet; [`README.md`](literature/library/README.md) gives the card format |
| [`ARGUMENT_MAP.md`](ARGUMENT_MAP.md) | Twelve premises to the conclusion, each with its source, depth mark and weakest point |
| [`OUTLINE.md`](OUTLINE.md) | Decisions, terms, section plan, course crosswalk, flags on existing texts, sources to fetch |

**How it was made.** Ten Sonnet agents ran one facet each on 2026-10-12; three more audited the
syntheses and three applied the audits' factual fixes. On 2026-10-13, after the author's rulings, three
agents ran facets I–K and three audited them. An open-access chain then fetched 134 full texts, agents
found 117 more by hand from legitimate open copies, and one agent read and carded each source; a second
agent re-opened every source and corrected 151 of the 251 cards. Claude (Opus) led, adjudicated and wrote
the argument map and outline. No paywall, bot wall or captcha was bypassed, and no full text is in this
repo. Monographs were read as snippets or not at all.

## Open for the author

- The points his rulings left open: last column of [`OUTLINE.md`](OUTLINE.md) (a), and
  `T_adjudication.md` §9.3 (a 1995 printed use of "algorithmacy"; a seventh flag on Part 1).
- The course paper's due date, length and rubric, and whether the change of topic from the approved
  DIAL proposal needs the instructor's agreement.
- The library list in [`OUTLINE.md`](OUTLINE.md) (f): Saenger and Parkes first. About 40 further
  sources have open copies behind bot walls that a person can open in a browser
  (`T_adjudication.md` §9.5).

This arm borrows lab constructs. It does not re-run Φ.
