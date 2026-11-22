# ivarsson2026

- **Reference.** Ivarsson, F., & Islind, A. S. (2026). A taxonomy of the invisible work involved in the production of personal data. *ICIS 2026 Proceedings* (Data Management and Analytics track, paper ICIS2026-2260, completed paper). https://aisel.aisnet.org/icis2026/datamgmt/datamgmt/9 . No DOI. OpenAlex W7222988983.
- **Batch / triage.** P2. TRIAGE_T2, justesen2024, possible_answer, candidate 6.
- **Read depth.** abstract. The AISeL PDF (`oa_pdf_url`) returned a Cloudflare bot-check page to curl and HTTP 403 to WebFetch; no PDF saved. The AISeL landing page loaded (authors, track, paper number). The abstract quoted below is the OpenAlex abstract, reconstructed from `citing/justesen2024_openalex.json`.
- **Citation line found.** Not seen. OpenAlex's `referenced_works` for W7222988983 (67 references) includes Justesen and Plesner (2024) (W4392883145). Citation is confirmed by index metadata only.
- **Citing passages.** Not seen.

## Candidates touched

**6. Invisible work and opacity — takes_up, possible answer (abstract only).** [S10f: restores the reader's takes_up, which S10e had raised to "answers (on the abstract)" to match akhil2026. Both cards now carry what an abstract can carry. See Fable check.] [S10e: was takes_up. The abstract develops a typology of invisible work, which is what OQ-justesen2024-16 invites, and the card's own Caution already said the work "answers" the call; akhil2026, on equal abstract evidence, is classed answers.]
> "we develop a taxonomy of five forms of invisible work involved in producing personal data: strategizing, resourcing, maintenance, interpretative, and care work." (abstract)

> "we advance an understanding of personal data as situated and shaped through human data work" (abstract)

## What the work says

Ivarsson and Islind analyse 47 interviews with people who used wearables and an app for three months to improve their sleep, and sort the work of producing personal data into five forms of invisible work, including "interpretative" work. They argue that organizations sourcing such data depend on this distributed, unrecognized human data work.

## Caution

Abstract only. The setting is individuals producing data about themselves for organizations, not members working with colleagues through a system, so the work answers Justesen and Plesner's call for the typology of invisible work, not the person-to-person case algorithmacy addresses. What "interpretative work" covers (reading one's own data? reading the app's feedback?) cannot be told from the abstract. Read the full text before using the taxonomy.

## Verification

- **Verifier.** Claude Opus 5.5, S10e (independent check; did not write the card).
- **Date.** 22 November 2026.
- **Bibliographic line.** No DOI. The AISeL landing page (fetched 22 Nov 2026) gives title, authors Ivarsson, Frida and Islind, Anna Sigríður, and paper ICIS2026-2260, matching the card.
- **Citation of the OT article.** OpenAlex W7222988983 lists W4392883145 among its 67 referenced works. Index metadata only, as stated.
- **Quotes checked / corrected.** 2 / 0. Both match the reconstructed OpenAlex abstract.
- **Classification changes.** Candidate 6: takes_up → answers (on the abstract). The card's Caution already said the work answers the call; the class now agrees, and matches akhil2026 on the same evidence. PICKUP_P2.md lists it under "Take it up".
- **Read depth.** abstract, stated correctly.
- **Verdict.** verified_with_corrections

## Fable check

[Written by Fable (claude-fable-5-2), S10f, 2026-11-22]

- **Date.** 22 November 2026. Counting follows the plan's rule that "a citing work counts only if its reference list holds the OT article": for each candidate I say whether the work cites an asker of that candidate, and for what.
- **Read against.** The OpenAlex abstract for W7222988983, rebuilt from the inverted index in `citing/justesen2024_openalex.json`. The local store holds no text for this key.
- **Quotations.** 2 of 2 match the abstract word for word.
- **Classes.** Candidate 6: I restore `takes_up` and add "possible answer (abstract only)". The reader classed the work `takes_up`; S10e raised it to `answers` for consistency with akhil2026. I restore the consistency in the other direction, for the reason given on that card: triage T2 already judged this work `possible_answer:6` from the same title and abstract, and nothing was read after that. A second reason applies here. The abstract's workers are people "producing data about themselves" with sensor technologies "incorporated into people’s everyday lives" (abstract), while the invitation concerns "the invisible in the digitalized organization" (OQ-justesen2024-16, p. 21). Whether the taxonomy reaches work done inside an organization cannot be told from the abstract.
- **Counting.** Candidate 6: the citation of justesen2024 rests on OpenAlex's `referenced_works` (67 entries; W4392883145 is among them); no one has seen the reference line.
- **Use.** Abstract-level evidence that the invisible-work lens is travelling to personal data. The "interpretative" form is unread and should not be set beside algorithmacy's first part until the full text is.
- **Verdict.** used_with_corrections
