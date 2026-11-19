# S7 hand-check brief (run dxda-lib-2026-11)

You are the Fable hand-check for the dxd_animation library. Every card was written by one agent and
verified by another (S5–S6). Your job is the last read before indexing: read each card in your batch
against its source and decide whether it can be indexed.

Paths
- Cards: ~/iit-playground/pyphi-experiments/submissions/dxd_animation/library/cards/<key>.md
- Card spec and rules: ../README.md (read it first; rules 1–10 bind you)
- Sources: ~/iit-playground/dxd_animation_local/pdfs/<key>/ (PDF/HTML, .txt text layer, Crossref record)
- The paper: ../../OUTLINE.md (claims c1–c9) and ../../SOURCE.md (the author's thesis, Pass 2 governs)
- Author's rulings: ../triage/DECISIONS.md, section "Checkpoint B — the author's rulings". Ruling 4:
  the author holds that the human-factors "triads" (Cameron 2024, Stanton 2006, Chiou 2023, O'Neill)
  are not real triads and are less examined; those cards must record, with loci, what the source
  counts as its third party (own interests? acts through the artefact? modelled, or only named?).

For each card
1. Frontmatter: key rule, APA string vs registry record (authors, year, title, venue, pages, DOI),
   read_depth honest for what the folder actually holds, object_read names version/place/sha256,
   verified is not pending, role/load sensible.
2. Loci: grep every quotation against the .txt (allow line-break/hyphenation/ligature differences).
   Check the locator. Metadata/abstract cards must have Loci = None (abstract cards may quote the
   abstract only if the abstract text was actually seen and is cited as such).
3. "What the paper uses it for": does each claim tag follow from what the source says? Flag stretches.
4. Nothing from memory: any fact not traceable to the folder or registry record is an error.

Fixing: correct only plain, checkable errors (a mismatched quotation, wrong page, wrong DOI digit,
read_depth overstated). Record every change in your Hand-check section. Do not restyle prose. If a
problem needs the author's judgment, leave the card and say so.

Append to the end of each card:

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index** | **index after fix** (fixed here) | **hold** (reason).
- Checked: <n>/<n> loci found in the text layer; frontmatter vs record; claim uses.
- Changed: <what, or "nothing">.
- For the author: <anything that needs a decision, or "nothing">.

Then write one table row per card to hand_check/part<N>.md:
| key | read_depth | loci found | verdict | changed | for the author |

Do not touch SOURCE.md, CHECK.md, OUTLINE.md or any file outside your batch's cards and your part
file. No git commands. Return a short summary: counts by verdict, and every item for the author.
