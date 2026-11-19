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

---

# RUN_REPORT — run 2 (`dxda-lib-2026-11b`, 2026-11-11)

> [Written by Claude (Opus 5.5, lead), 2026-11-11.] The model-paper pass (`../SOURCE.md`, Pass 3;
> rulings in `triage/DECISIONS.md`, "Run 2").

## What ran

| Stage | Who | Output | Result |
|---|---|---|---|
| S0–S1 | lead | facets F11–F13, G2; claims m1–m7 (`tools/build_index.py`, `README.md`) | — |
| S4 fetch | lead, through the author's Chrome session and arXiv/SciTePress | `~/iit-playground/dxd_animation_local/pdfs/` | 7 ACM papers, 2 arXiv papers, 1 SciTePress paper held; the three craft books need a loan (not obtained) |
| S5 cards | lead (Lasseter, Chang & Ungar, Thomas & Calder, Pinhanez, Zhang & Davis, Leveson, Vaithilingam); three writer subagents (Ribeiro & Paiva, Takayama, Schulz, Gonzalez, Kurian, Lewis, Hoerl, May) | `cards/` | 15 cards new or rewritten |
| S6 verify | three verifier subagents, batches A–C, none a writer | Verification sections | 6 verified, 9 corrected |
| S7 hand-check | lead | Hand-check sections | 15/15 index |
| S8 index | tools | `INDEX.md`, `TRACKER.tsv`, `references.bib`, `REFERENCES_APA.md` | 88 cards, 0 malformed, 0 stale; DOIs 14/14 ok; quotations 0 unsupported (`QUOTE_CHECK_NOTES.md`) |
| S9 gap | subagent | `GAP_CHECK_2.md` | gap holds only narrowed (Pinhanez 2017; Zhang & Davis 2026; Kurian 2025); three search legs failed |

Every agent ran on Opus 5.5 after the author's switch from Fable 5.2 (DECISIONS, "Run 2").

## Read depth of the run-2 cards

Full text: Lasseter 1987, Chang & Ungar 1993, Thomas & Calder 2001, Gonzalez 1996, Ribeiro & Paiva 2012,
Takayama et al. 2011, Schulz et al. 2019, Kurian 2025 (arXiv submitted version), Lewis et al. 2026,
Hoerl 2015 (Early View version of record), May et al. 2003, Pinhanez 2017. Partial: Zhang & Davis 2026.
Abstract: Leveson 2000, Vaithilingam et al. 2025.

## What changed the model

1. **Takayama et al. 2011**: a robot's forethought raised viewers' sureness and the robot's appeal but
   not correct readings. Row 3's cue must announce the rule, not show the character deliberating; P5
   has its strongest datum.
2. **Lasseter 1987**: eleven principles, not twelve; the timing chart as an instruction to the
   in-betweener; the overshooting machine in-betweener and the keys that lock it; "The change must come
   before, or after, the move" (p. 42).
3. **Pinhanez 2017** and **Zhang & Davis 2026** already do parts of rows 2 and 3 (anticipation before a
   binding charge; keyframes with LLM in-betweens). The novelty claim is narrowed to the selection by
   decision competencies in a triadic setting.
4. **Thomas & Calder 2001** do not show liking dissociated from performance (verifier); cited for "no
   measured performance gain" only.
5. **"Intent specification"** is used by Leveson 2000 and Vaithilingam et al. 2025; the paper contrasts
   them.

## For Roger

- Decisions D-a to D-m (`../MODEL.md`, §8).
- The three craft books (Thomas & Johnston; Williams; Whitaker & Halas) need an Internet Archive loan
  or a library copy; until then Thomas & Johnston is cited only as quoted.
- Rerun the failed gap-check legs (Scholar Gateway, OpenAlex, Semantic Scholar) before submission.
- Uncarded leads: Dragan, Lee & Srinivasa 2013 and Szafir, Mutlu & Fong 2014 (legible robot motion,
  via Schulz); So et al. 2026; Hau 2026; Govind Reddy 2026 (sibling library, abstract).

## Run 2, second day (2026-11-12)

[Written by Claude (Opus 5.5, lead).]

- **Gap check rerun** (`GAP_CHECK_2.md`, rerun section): OpenAlex ran (eight searches; citation snowballs
  on L. Stark 2024, Pinhanez 2017, Lasseter 1987, Takayama 2011); no new close hit; verdict unchanged.
  Scholar Gateway (access denied) and Semantic Scholar (HTTP 429) failed again.
- **Four cards**: `szafir2014communication` (full), `dragan2014analysis` (full), `dragan2013legibility`
  (abstract; full text paywalled on the ACM page), `zhang2026narrative` (upgraded to full). Writer:
  subagent; S6 verifier batch D: 4 corrected; S7 hand-check by the lead: 4 index. Index rebuilt (91 cards,
  0 malformed, 0 stale); DOIs 3/3 ok; quotations 41 found, 1 found-nospace.
- **What changed the model:** no read study shows an anticipatory cue raising prediction accuracy
  (Szafir 2014; Takayama 2011), so row 3's cue takes anticipation's function, not its form, and P4 has
  no support yet. Dragan 2014's "confidently wrong" is a property of their model, not a measured result.
  Zhang & Davis claim keyframing as new only within AI-assisted writing, and their generated material
  can rewrite the writer's keys.
- **Draft checks closed:** Hoerl p. 690, Dragicevic p. 2017, Takayama p. 74, Pinhanez pp. 31 and 34
  (inferred from Crossref ranges and PDF page counts); Burrell and D. Stark references completed.
  **Still open:** Kurian's version-of-record pages (ScienceDirect showed a CAPTCHA to the automated
  browser); the TIES reference-style name (its link names none); the two failed search legs.
