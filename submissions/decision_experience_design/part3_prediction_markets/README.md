# Part 3: Decision markets as decision experience design (opened 2026-10-03)

**Status:** research stage complete at full-text level for the load-bearing sources; outline revised; argument map drafted; no draft. Claude did all of the work for the author to revise. None of the prose is the author's.

**Thesis (author ruling, 2026-10-03).** Kalshi and Polymarket present as prediction and decision markets and are sports betting in that dress; the dress is the design failure. Prediction markets compute a probability, but their interfaces ask the user to trade. That gap is a decision experience design failure by the criteria in Parts 1 and 2. See `OUTLINE.md`.

**What the deep-research run did (2026-10-03, local session).** The first pass ran in a cloud session whose network policy blocked every scholarly, platform, regulator and court host, so it stopped at abstracts. The second pass ran locally with eight agents (model: Fable), one per facet:

- Facets A, B and C moved from abstract level to verified metadata and full text where a copy was reachable (A: 40 of 53 original entries in full text; B: 31 of 55; C: 37 of 65).
- Facet D now holds platform facts from primary sources, including the sports share of volume with its denominator.
- New facets: H (Robin Hanson; all ten required papers read in full), M (Tarek Mansour and Kalshi, reconstructed from court filings, CFTC self-certifications and interviews), L (event-contract law), X (the counter-case).

**Gate (author's condition: the run fails unless it captures Hanson's and Mansour's arguments).**
- Hanson: passes. Ten of ten required items in full text; seven are author preprints, so journal page numbers need a library copy.
- Mansour: passes, on a different footing. He has no academic work on markets (his 2019 MIT thesis is on deep learning), so the argument is reconstructed from the primary record. Not obtained: Kalshi's 2024 and 2026 CFTC comment letters, the Massachusetts order. No testimony or signed op-ed by Mansour was found.

**Second run (2026-10-03, same day).** The author stated the argument: prediction markets present a win-or-lose bet as coordination through a third party, a dark pattern of the well-meant kind. Four more agents (model: Fable) tested it: F (hedgers and speculators in currency and commodity markets), K (whether a dark pattern requires intent; the Like-button and advertising histories), T (the lab's triad criterion applied to six cases), R (Hanson's and Mansour's replies). `ARGUMENT.md` gives the verdict premise by premise: five hold, two hold in a narrower form, and the Forex premise fails as worded.

**Files.**

| File | Use |
| --- | --- |
| `OUTLINE.md` | Thesis, section plan with per-claim status flags, jargon table, open questions |
| `ARGUMENT.md` | The author's argument P1–P8 and C, each premise with support, replies, status, and the two forms the conclusion can take |
| `ARGUMENT_MAP.md` | Hanson's and Mansour's arguments and the counter-case, each row tied to a facet claim and marked for its bearing on the thesis |
| `literature/facets/A_market_theory_use.*` | Market theory and decision use (62 entries) |
| `literature/facets/B_betting_interfaces_harms.*` | Betting interfaces and harms (66 entries) |
| `literature/facets/C_probability_display_numeracy.*` | Probability display and numeracy (79 entries) |
| `literature/facets/D_platform_facts.*` | Platform facts from primary sources (101 entries) |
| `literature/facets/F_hedging_speculation.*` | Hedgers and speculators: BIS, CFTC, Keynes, Hicks, Working, Stout (31 entries) |
| `literature/facets/K_dark_patterns_intent.*` | Dark-pattern definitions and intent; Like button and advertising histories (58 entries) |
| `literature/facets/T_triad_test.md` | The triad criterion applied to six cases; strains and concessions |
| `literature/facets/R_replies.md` | Replies Hanson and Mansour would make to each premise |
| `literature/facets/H_hanson_arguments.*` | Hanson: 38 numbered claims with locators (37 entries) |
| `literature/facets/L_event_contracts_law.*` | Statute, CFTC record, circuit rulings, scholarship (63 entries) |
| `literature/facets/M_mansour_arguments.*` | Mansour and Kalshi: premises A1–C5 with sources (72 entries) |
| `literature/facets/X_counter_case.*` | Seven lines against the thesis, rated (38 entries) |
| `literature/references.bib` | Built file: first-wins merge of the ten facet bibs (550 entries) |
| `literature/cited_keys.txt` | The 51 keys `ARGUMENT.md` and `ARGUMENT_MAP.md` cite; replace with the draft's keys once a draft exists |
| `literature/audit/AUDIT_00.md`, `AUDIT_01.md` | What I checked myself: 32 records and 11 claims (first run); 9 claims (second run) |
| `literature/audit/BIB_CHANGES.md` | Merge decisions and proposed bib changes, not applied to the facet files |
| `literature/build_references.py` | Copied from Part 2; resolves all 51 keys and stops only because `DRAFT.md` does not exist |

**Not yet made.** `DRAFT.md`. A citation audit of the entries outside the load-bearing set.

**Open for the author.**
- The seven questions in `OUTLINE.md` section (f), starting with which form the conclusion takes (`ARGUMENT.md`, section C).
- Hosts that refused access in the local session: SSRN, CourtListener's site (its RECAP file store worked), Wiley, Sage, INFORMS, Springer, Elsevier, comments.cftc.gov, kalshi.com (rate-limited). The entries still at abstract level sit behind these; library access would close most of them.
- Facet D's volume computations ran from scripts kept outside the repo, and two of three Kalshi passes hit a page cap. Only the 24-hour snapshot is complete.
- The style authority `dissertation/current/paper1/exemplars/annals_20_2/FLOW_AND_COHESION.md` governs any drafting.
- This arm is a detour from Paper 1. Scope: full treatment, chosen by the author on 2026-10-03.
