# Combine report — Paper 1 full draft

`DRAFT.md` is the combined full draft, assembled by `combine.py` from the eight per-section drafts in
`drafts/`. Re-runnable: edit a section draft and re-run `python3 combine.py`.

## What the combine did

- Concatenated the eight section bodies in spine order (Abstract → §1…§8), dropping each section's per-section
  working reference list.
- Merged all per-section reference lists into **one consolidated, de-duplicated, alphabetical bibliography**
  (in-text citations only in the body).
- Cleaned Google-Docs export cruft (escaped `\.`, `\[`, `r \= 0.17`, etc.) and normalized header levels
  (## sections, ### subsections).
- De-duplicated references by a year+title key (stable across author-name formatting variants); dropped
  placeholder stubs.

## Result

- **~22,180 body words** (a full dissertation-chapter length; the *Annals* submission is the 5-page proposal
  derived from this chapter to the four mandated headings — see `STRUCTURE.md`).
- **229 unique references** (337 raw entries across sections → 229 after dedup).
- 8 sections, abstract, consolidated bibliography.

## Resolved during the combine (citation integrity)

- **Gagrčin et al.** — the existing draft cited "Naab & Grub, 2026"; verified via Consensus + the DOI
  (10.1177/14614448241291137, which encodes 2024) that the correct year is **2024** and the work is the same
  *New Media & Society* integrative review. Standardized all in-text cites to "(Gagrčin et al., 2024)" and
  consolidated to one entry. **Still open:** the full author list (the two draft variants disagree — flagged
  in the entry).
- **EU AI Act (2024a)** — two title variants merged to the fuller form.
- **Parent-Rocheleau et al. (2024)** — a "[detail to confirm]" placeholder in §7 replaced with the real
  entry (HRM 63(1), 25–44).

## Citation-integrity pass — COMPLETE

Every `[new]`/`[verify]` entry was checked against authoritative sources (Consensus + publisher pages /
indexes). The pass caught **eight incorrect entries in the deepening additions** (six fabricated/incorrect
author lists, one mischaracterized paper, one wrong title) and corrected them; the corresponding in-text
cites were updated to match.

| Entry | Was | Corrected to | Source |
|---|---|---|---|
| Bankins | "Hu & Yuan, 2023" | **Ocampo, Marrone, Restubog, Woo (2024)**, JOB, job.2735 | Wiley/MQ |
| Kadolkar | "Mariappanadar & Kramar" | **Kepes & Subramony (2024)**, JOB 46(7) 1057–1080, job.2831 | Wiley/onwork |
| Leander | "Boldt" | **Burriss (2020)**, BJET 51(4), bjet.12924 | Wiley/ERIC |
| Uzunca | "Sharapov & Tee" | **Kas (2022)**, Industry & Innovation 30(6) 664–693 | T&F/SemanticScholar |
| Pidoux | "Cardon & Acker" | **Kypraiou & Dehaye (2025)**, Socio 20, 41–64 | OpenEdition |
| Jiang | "Perceived Algorithmic Management Questionnaire" | **research-agenda paper; Jiang, Hu & Li (2025)** — §4.5 sentence reframed | Wiley |
| Gagrčin | my "Porten-Cheé et al., 2024" | **Naab & Grub (2026)** (original draft was right) | NMS/sagepub |
| Heiland | "Neither timeless nor placeless…" | **"The social construction of algorithms…" (2023)**, ntwe.12282 | Wiley |

Verified correct as written: Keegan & Meijerink (2025, AROP 12:395–422), Dedema & Rosenbaum (2024, JASIST
75(3):344–374), Battiston et al. (2025, NHB 9(12):2441–2457), Bergh et al. (2019, JOM 45(1):122–158), Felin
& Zenger (2011), Lawson & Robins (2021), Siltaloppi & Vargo (2017), Bokányi & Hannák (2020), Schor et al.
(2020), Cram et al. (2022).

## Full-bibliography sweep — COMPLETE (all 229 entries)

Seven parallel verification agents checked every entry against authoritative sources (publisher pages,
Crossref, DOI resolvers). **224 verified clean; 5 discrepancies found in the inherited base references**, all
now corrected:

| Entry | Error | Corrected |
|---|---|---|
| Cram et al. (2022) | 4th author "Maedche" | **Benlian** (JMIS 39(2):426–453) |
| DeVito (2021) | DOI 10.1145/3479596 | **10.1145/3476080** |
| Goh et al. (2014) | pages 590–614 | **471–505** (Small Group Research 45(5)) |
| Liang et al. | "2024, ISR 35(1):319–342, isre.2023.1228" (resolved to a different paper) | **Liang, Peng, Hong & Gu (2023), ISR 34(1):297–318, 10.1287/isre.2022.1130** |
| Soda et al. (2018) | DOI 10.5465/amj.2015.0123 (404) | **10.5465/amj.2016.0123** |

The three earlier `[verify]` details were also confirmed and finalized: Bankins pages (159–182), Leander page
range (1262–1276), OECD DOI (10.1787/66d0702e-en). **No `[verify]`/`[new]`/`[shared]` flags remain in the
bibliography.**

## The one remaining placeholder (deliberately not fabricated)

- **§2 `[N]` corpus count** — left as "[N — to be finalized from the screening log]". This is a factual
  claim about the author's screening yield, not something to manufacture; the author sets it from the actual
  log.

## Seam notes (cross-section consistency, for a human read-through)

- **Triadic irreducibility appears in both §3.1 (Battiston 2025, brief) and §5.2 (Battiston 2020/2021 +
  Aumann/Myerson/Burch, the full formal treatment).** Intentional: §3 fixes the object briefly; §5.2 is the
  full warrant. Confirm §3.1 reads as forward-pointing, not a competing full version.
- **The variance puzzle** recurs by design (§1 opener → §6.1 → §7.1 → §8) — this is the spine echo, not
  redundancy.
- **EU AI Act / Platform Work Directive** appear in §1.3 and §7.5; confirm the two passages read
  consistently and don't repeat verbatim.

## Artifacts

- `DRAFT.md` — the combined full draft (regenerate with `combine.py`).
- `drafts/sN_*.md` — the eight per-section drafts (each with its own working reference list).
- `research/sN_*.md` — per-section deep-research finds (connectors + the §1 web harness).
- `combine.py` — the deterministic assembler.
