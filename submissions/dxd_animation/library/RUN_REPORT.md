# RUN_REPORT — library run `dxda-lib-2026-11` (S10)

> [Built by Claude, 2026-11-05.] What ran, the counts, and what waits on Roger at Checkpoint D.

## What ran

| Stage | Model | Output | Result |
|---|---|---|---|
| S0 setup | Haiku + main | `tools/`, `CITED_WORKS.md` | 44 cited works de-duplicated against 14 lab libraries (4,525 registry rows, outside the repo) |
| S1 facets | Fable | `FACETS.md` | F1–F10 + G; Checkpoint A approved |
| S2 search | Haiku + main | `search/`, `SEARCH_LOG.md` | 3,125 hits; 6 Consensus searches |
| S3 triage | Opus; Fable for decisions | `triage/` | 60 new + 17 upgrades approved; Checkpoint B rulings recorded |
| S4 fetch | Haiku + main | `FETCH_LOG.tsv`, `BROWSER_LIST.md`, `HELD_COPIES.tsv` | 26 PDFs held plus text-only copies; 55 rows for Roger's browser |
| S5–S6 cards | Workflow: Sonnet/Opus writers, Opus verifiers | `cards/` | 77 cards, 24/24 agents, writer ≠ verifier on every card; 40 verified, 37 corrected, 0 pending |
| S7 hand-check | Fable ×5 | `HAND_CHECK.md` | 78/78 (incl. wu2026ainimation, added 2026-11-06): 75 index, 3 index after fix, 0 hold |
| S8 index | scripts + Haiku | `INDEX.md`, `TRACKER.tsv`, `references.bib`, `REFERENCES_APA.md`, `DOI_CHECK.md`, `QUOTE_CHECK.md` (+ `_NOTES`), `POINTERS.md` | schema 0 malformed; DOIs 68/68 ok; quotations 0 unsupported after hand trace; 107 pointers, 0 missing paths, 30 pointer-weak |
| S9 critic + gap | Opus | `CRITIC.md`, `GAP_CHECK.md` | c9 open but narrowed; 5 new candidate works |

Plan checks: `build_index.py --check` exits 0; DOI title mismatches 0; quote misses all traced
(`QUOTE_CHECK_NOTES.md`); hand-check rows = live cards (77); 0 `pending`; every POINTERS path
exists; `SOURCE.md` unchanged; no PDF, text layer or registry in the tree.

## Read depth

| read_depth | cards |
|---|---|
| full_text | 24 |
| partial | 6 |
| abstract | 25 |
| metadata | 23 |

**26 load-bearing cards have no full or partial text.** Those that matter most to the argument:
`silvio2019puppets`, `silvio2010animation` (Silvio reached only through Stark);
`thomas1981illusion`, `lasseter1987principles` (the animator's methods, §5);
`wertheimer1912experimentelle`, `anderson1993myth`, `hoerl2015seeing`, `steinman2000phi` (the §4.2
perception claim and its contest); `ananny2018seeing` (§3.2); `norman1986cognitive`,
`bettman1998constructive` (§2); `chiou2023trusting` (ruling 4). The full list is in `CRITIC.md`;
the browser routes are in `BROWSER_LIST.md`, with S9's top-10 ranking in `CRITIC.md`.

`hoerl2015seeing`: the Warwick accepted version is now held locally; the card needs a re-write,
verify and hand-check to move to full text. No browser needed.

## For Roger (Checkpoint D)

1. **c1 has no source for a *moving* goal.** Every full or partial c1 card keeps the goal fixed
   (Saracay, Wadi, Subramonyam, Weinmann, Jachimowicz); Chen 2026 is abstract only. Decide whether
   the moving goal is your contribution, stated as such, or needs a source.
2. **c9: open but narrowed.** Stark 2024, Maeda & L. Stark 2025 and Jones 2026 already read LLM
   interfaces as animation. None turns that into a design method for the user's decision. Wu & Masson
   2026, "AInimation" (arXiv, 10.48550/arxiv.2607.18507), comes nearest. **[Updated 2026-11-06]:**
   now carded from the full text (`wu2026ainimation`). It animates prompt-to-response transitions as
   UI technique (n = 16; review tasks). It has no "decision", no animation theory and no character
   reading. It also gives the lab's only datum that a crafted, slower display beats an instant one,
   which bears on c8. Draft §6 wording, marked as Claude's, is in `GAP_CHECK.md`.
3. **Ruling 4 (HF triads):** Stanton 2006 has task-role agents and no interested third party.
   Cameron 2024's Deployer has interests, but they are not modelled, and the model is proposed and
   untested. Chiou 2023 is unread beyond the abstract, which names no third party. O'Neill 2022 is a
   pointer. The §3.2 wording is yours.
4. **Where the cards cut against the outline** (quoted in `CRITIC.md`):
   - Stark's animators are many, not one.
   - Stark's opacity is hidden labour, not missing frames.
   - His answer is regulation, not craft.
   - Shi treats authorship as diffuse.
   - Tan reads deliberate pacing as possible deception.
5. **Course coverage:** Action (§4.3) is the thinnest heading, followed by Cognition (§3.1). Nothing
   supports "biological" or "emotional".
6. **Your text, flagged and not changed** (`CHECK.md`, S10 section):
   - Stark's "structuring trope" is on p. 1664.
   - The ELIZA effect is defined at p. 1665.
   - Silvio: 2010 or 2019 for the definition?
   - "proves" → "shows".
   - "58 datasets from 55 studies".
   - Chevalier does not carry the animator's methods.
   - Gnewuch 2022 is cited by its file name.
7. **Untagged fits the hand-check offered:**
   - `abercrombie2023mirages` c6
   - `natale2019if` c3/c5
   - `ruddell2008from` c6
   
   **c1 scope rulings** for `saracay2026beyond` and `subramonyam2024bridging`.
8. **Records the title page must settle:**
   - Allison Alexy: editor or second author of Silvio 2019?
   - Ngai and Sheridan: author names are in no record.
   - Wertheimer 2012: translator credit.
   - Thomas & Johnston: edition and year.
   - Schwan: umlaut.
   - Clark & Fischer: 2022 or 2023?
9. **New candidates, not carded:** Kurian 2025 (10.1016/j.ijcci.2025.100788);
   Chen & He 2025 (10.1080/10447318.2025.2527847); Clark & Fischer (BBS). Maeda & Buening 2026 does
   not pre-empt c9.
10. **Pointer overlap:** POINTERS lists six works that also have cards here (Thomas & Johnston,
    Wertheimer 1912, Anderson & Anderson, Johnson 2012, Jachimowicz 2019, Ananny & Crawford). These
    are the approved upgrades, outside the ceiling (Checkpoint A).
11. **Open from S1:** Albantakis is the IIT 4.0 paper; the Huq 2026 title does not match its record.
12. **Pull request:** draft PR #878, branch `research/dxd-animation-library`, into `contrib`. Your
    approval is needed before it leaves draft.
