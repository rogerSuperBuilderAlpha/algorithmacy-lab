# S7 hand-check brief (run pta-lib-2026-11)

> [Written by Claude, 2026-11-08, adapted from the dxd_animation brief.]

You are the Fable hand-check for the pt_ai_as_animation library. Every card was written by one agent
and verified by another (S5–S6). Your job is the last read before indexing: read each card in your
batch against its source and decide whether it can be indexed.

Paths
- Cards: ~/iit-playground/wt-pt-animation/submissions/pt_ai_as_animation/library/cards/<key>.md
- Card spec and rules: ../README.md, section "Card schema" (read it first; its rules bind you)
- Sources: ~/iit-playground/pt_ai_animation_local/pdfs/<key>/ (PDF/HTML, .txt text layer, records:
  crossref.json, openalex.json, csl.json, openlibrary*.json; provenance.txt where a copy came from
  elsewhere). Ignore sha256.txt when looking for the text layer. Also check
  ~/iit-playground/pt_ai_animation_local/inbox/ for any copy the author has added.
- The paper: ../../SKETCH.md (claims) and ../../SOURCE.md (the author's words; never edited)
- Rulings: ../FACETS.md "Checkpoint A — rulings" and ../triage/DECISIONS.md "Checkpoint B — rulings".
  Ruling B2 (c9 narrowed): the triad cards (clark2023social, schumann2022machines and any card tagged
  c9) must record what the source counts as its third party (own interests? binding determination?
  keeps the parties apart? modelled, or only named?). Ruling B1 (c12): the gap cards (govind2026illusion,
  masumori2026openlife, hayesroth2006puppetry, sun2026between, rolla2026embodiment) must say what
  separates them from "AI development as a craft of animation, argued as a claim about what AI is".

For each card
1. Frontmatter: key rule; APA string vs record (authors, year, title, venue, pages, DOI);
   read_depth honest for what the folder actually holds; object_read names version, place, sha256
   (recompute with `shasum -a 256` for at least the text object); verified is not pending;
   role/load/status sensible (status "cited" only if SOURCE.md or SKETCH.md names it or a ruling does).
2. Loci: grep every quotation against the text layer (allow line-break, hyphenation and ligature
   differences; re-extract with pdftotext -layout or by column if the layer interleaves columns).
   Check the page locator. Metadata cards must have Loci = None; abstract cards quote only the
   abstract text actually seen in a record, cited as such.
3. "What the paper uses it for": does each claim tag follow from what the source says? Flag stretches
   the card does not already name.
4. Nothing from memory: any fact not traceable to the folder, the registry or another card's
   checked source is an error.

Fixing: correct only plain, checkable errors (a mismatched quotation, wrong page, wrong DOI digit,
read_depth overstated). Mark each change in the card "[Corrected by Fable, S7]" and record it in your
Hand-check section. Do not restyle prose. If a problem needs the author's judgment, leave the card and
say so.

Append to the end of each card:

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index** | **index after fix** (fixed here) | **hold** (reason).
- Checked: <n>/<n> loci found in the text layer; frontmatter vs record; claim uses.
- Changed: <what, or "nothing">.
- For the author: <anything that needs a decision, or "nothing">.

Then write a short header and one table row per card to hand_check/part<N>.md:
| key | read_depth | loci found | verdict | changed | for the author |

Do not touch SOURCE.md, SKETCH.md, DECISIONS.md, FACETS.md or any file outside your batch's cards and
your part file. No git commands. Return a short summary: counts by verdict, and every item for the
author.
