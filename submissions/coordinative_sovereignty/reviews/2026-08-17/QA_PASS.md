# Pre-submission QA pass — 2026-08-17

**Manuscript:** `chapter/chapter.md` · **Venue:** IGI Global, *Organizational Implications of Digital
Sovereignty in the Age of AI* (ed. Samuel Fosso Wamba) · **Due:** 2026-08-30, thirteen days out.

Scope of this pass: establish which file is canonical, verify it mechanically end to end, verify the files
generated from it, and list what remains. Prose and argument were not revised.

**This pass complements the five-seat panel in this directory; it does not overlap it.** The panel read
`chapter.md` as a text — content, argument, cohesion, citation accuracy, style — under a review-only brief
that put the exports and the manuscript file itself out of scope. This pass read it as a build input, and
everything it found lives in that gap: a render defect invisible in any file a reader would open, two
generated exports that had silently drifted three edits behind their source, and no script to keep them
from drifting again. Seat 04 and this pass overlap on the citation graph and agree exactly — 109 entries,
zero orphans, zero ghosts, alphabetization and Anderson initials intact. Where they diverge, seat 04 wins:
it read sources, and found three defects a matcher cannot see.

---

## 1. Which file is canonical

**`chapter.md`.** It is the file NOW.md, both READMEs, and the 2026-08-17 review brief name, and nothing
found in this pass argues against it.

The three-file spread had made currency ambiguous, so it was settled by hash rather than by mtime:

| File | Last content change | Relation to `chapter.md` |
|---|---|---|
| `chapter.md` | 2026-08-14 (`ea4b917`) | canonical |
| `chapter_v2.md` | 2026-08-14 (`ea4b917`) | cut *from* the post-fix `chapter.md`; carries all six §0d fixes |
| `chapter_grammarly.md` | regenerated today | derived, was stale |
| `Full Paper - Alg & Sov.docx` | regenerated today | derived, was stale |

The 17 August timestamps on every file in this directory record the `chore/nav-reorg` move from
`org_frontier/` into `submissions/`, not an edit. All three markdown files are byte-identical to their
`ea4b917` versions, so the move changed nothing.

**Neither draft is stale relative to the other.** `chapter_v2.md` is not an older draft and not a
divergent one. Parity was checked on the load-bearing surface and is exact: 67 parenthetical citations,
11 statistics and monetary figures, 17 quotations, 27 headings, all identical between the two files. The
whole difference is 123 insertions and 117 deletions of prose — roughly fifty sentence merges that raise
length variation toward four published model essays.

So the choice between them is a prose-voice decision with no currency or content dimension, and it stays
with the author. Two things bear on it. `chapter_v2.md` sits closer to the model essays on sentence
length variation (sd 13.5 against `chapter.md`'s 12.3, against a 14.5 floor in the models). Against that,
its ~50 merges are a machine pass over prose, which is the failure mode the author has already named
once on this project's chapter work.

---

## 2. Defect found and fixed: the References heading did not render

`chapter.md` line 920 ended the conclusion and line 921 opened `## References` with no blank line between
them. Pandoc's `blank_before_header` is on by default, so a heading in that position is not a heading.

A render of `chapter.md` as it stood produced a conclusion ending in the literal string:

> …and on the diffusion of the competence that standing requires. Neither reading alone nor control alone
> secures it. ## References

— and no References heading anywhere in the document. The reference list ran on as body text.

The shipped `.docx` did not show the fault, because it was built before the 14 August hand edits
introduced it. That is the dangerous shape: the bug was invisible in the artifact anyone would have
opened, and would have appeared the moment the outstanding "regenerate the exports" task was done.

Fixed. A fresh render now produces 27 headings matching the 27 in the markdown, the table intact, and no
literal markdown in the output.

---

## 3. The generated exports were stale, and now are not

`HANDOFF.md` §0d listed regenerating `chapter_grammarly.md` and `Full Paper - Alg & Sov.docx` as owed
before submission. It was still owed. Both files predated all five substantive 14 August edits and still
carried:

1. The aphorism the author's own AI-slop verdict named — "a competence distributed like capital
   distributes standing like capital" (§4) — deleted from `chapter.md` on 14 August.
2. The half-cited clause "and to the politics of platform dependence more broadly" (§5.3), cut because
   no source in the bibliography carried it.
3. The pre-consolidation §5.5 hedge stack, four hedges in five sentences on the chapter's best empirical
   passage.
4. Neither carried the §7 sentence separating the instruments' bearers ("The instruments do not all reach
   the same bearer…"), which closes a gap between §7, §6, and §3.2.

Both are regenerated and verified: the deleted passages are gone, the added ones present, References is a
Heading2, no author name or affiliation appears, "Author, 2026" survives, and smart quotes applied.

**Root cause, and the fix for it.** Regeneration was a manual step nobody had scripted, so it drifted
silently while three documents asserted it had been done. `chapter/regen_exports.py` now performs it:

```
python3 regen_exports.py           # rewrite both exports from chapter.md
python3 regen_exports.py --check   # exit 1 if either has drifted, or if chapter.md has a structural fault
```

The `--check` mode also lints `chapter.md` for the two faults that break a render — a heading with no
blank line before it, a table with no blank line before it — and for the four required IGI sections. Run
it before packaging the submission.

---

## 4. Mechanical verification of `chapter.md`

Everything below was checked against the current file and passes.

**Citations.** 109 reference entries; every one is cited in the body. Every in-text citation resolves to
an entry. The thirteen that a naive matcher flags are all forms it cannot parse, and each was checked by
hand: reprint years (B. Anderson 1983/2006, Habermas 1962/1989, Simmel 1908/1950 — all three reference
entries carry the required "Original work published" note), group authors (European Commission 2025a,
2025b, 2026; European Competition Network 2017; European Parliament & Council 2024), a possessive
("DeVito's (2021)"), a second-author narrative cite (Stark & Vanden Broeck), and the masked
"Author. (2026)". Reference list is in APA alphabetical order. No non-APA DOI forms.

**Anonymization.** No occurrence of any author surname, either institution, the repository name, or any
local path, in `chapter.md` or in either export. "Author, 2026" appears in §5.1, §9, and the reference
list, as intended.

**Cross-references.** All ten internal section references resolve to sections that exist, and each points
the direction its sentence claims — §2.3→§4, §3.2→§7, §4→§2.3, §4→§3.3, §5.2→§5.1, §6→§3, §6→§9, §7→§8,
§7→§6, §8→§5.5.

**IGI template conformance.** Title · Abstract (149 words, under the 150 limit, no citations) · Keywords ·
numbered §1–§10 · References · Cases · Additional Reading (9 entries) · Key Terms and Definitions (14
terms). 15,057 words total against a 10,000 minimum.

**House style.** Zero banned emphasis-marker openers. Zero sentence-initial agentless passives; one
"has been described" in the whole body. Zero first person. Zero slop lexicon. "This chapter" twice in the
body. Sentence mean 21.6 words, sd 12.3, 22.5% under twelve words, 8.2% over forty. Em-dashes 2.0/1k,
semicolons 2.2/1k.

---

## 5. What is outstanding

### 5a. The five-seat panel is complete — and now applied

All five seats ran and `SYNTHESIS.md` is written. **Zero major, three minor, two accept-with-nits.**

**Applied to `chapter.md` on 2026-08-17 after this pass; see `HANDOFF.md` §0g for the full record.** Both
consensus-spine items, all six single-seat items, seat 04's three citation repairs, and seat 01's two
unsourced claims are closed. The list below records what each seat asked for.

| Seat | Verdict | Single most important fix |
|---|---|---|
| 01 content | minor | Split §8's platform-work package: the employment presumption may *exit* the triad, so it should not count as "coordinative sovereignty written into law." Keep Chapter III and Art. 25. |
| 02 argument | minor | §6 defines the construct on *irreducibility* and *cannot leave*, two predicates §5.2 has just distinguished from *necessity*. Rewrite the definition and the Key Terms entry as proper to necessary mediation. |
| 03 flow | minor | §1 closes on the Bodin–Repetto defense and §2 opens on a different Habermas. Rewrite so the competence §2 names is the tail §1 hands it. |
| 04 citations | accept-with-nits | Rewrite the COM(2026) 178 demand clause. |
| 05 style | accept-with-nits | The §5.5 caution pile (ll. 581–588); two `this chapter`s back in the glossary. |

`SYNTHESIS.md` carries what this QA pass cannot substitute for: a consensus spine under a two-seat rule
(S1 abstract-vs-body, S2 the COM(2026) 178 gloss), six single-seat items ranked for a later fix pass, an
eight-step suggested order, and — most useful for whoever edits next — an explicit **do-not-touch list**
of settled prose, so a fix pass does not reopen the OTA dating anchor, the capability wording, the DeVito
concession, or the Hirschman mapping.

### 5b. Fourteen VERIFY items across two seats

**Seat 04 confirmed the citation graph against fetched primaries and found three defects this pass's
mechanical checks structurally could not:**

- **A regression against `HANDOFF.md` §0c.** §7 lines 692–694 hang "mixed evidence of demand" on
  COM(2026) 178. The fetched report says mixed evidence *overall*, greater technical complexity, and
  **limited** demand. §0c claimed this gloss "confirmed verbatim"; the two load-bearing clauses hold, the
  causal tag does not.
- **Curchod et al. (2020), §4 lines 342–343.** "implicit coalition between buyers and the platform owner"
  is a direct quotation with no locator — the only unlocated quotation in the body, and it carries the §4
  triad. The phrase is verbatim in the abstract, so `(Abstract)` matches how Repetto and Sekar & Siddiq
  were closed.
- **European Commission (2025a) title truncated** past the repealing clause that names Regulations
  2018/1807, 2019/1150, 2022/868 and Directive 2019/1024 — the four identifiers licensing both the §7 DGA
  move and the §8 P2B repeal.

Plus two nits: Anderson C. K. carries `11[8]` for 2011 but no volume/issue for 2009 (make them alike),
and Ananny and Crawford lose their year on second mention at line 258.

**Seat 01's nine, two of which are unsourced claims rather than confirmations:**

- §8 line 777, "further gatekeeper decisions have followed against other platforms" — unsourced. Name
  them or cut the clause.
- §9 lines 888–890, "expertise the platform funds" — Art. 13(3) entitles representatives to an expert of
  their choice, with the platform bearing proportionate expenses only where it has more than 250 workers
  in the member state. The chapter states a general funded-expertise duty the article does not create.
- Fratini et al. (2024) at §3.2 lines 259–261, cited for "none addresses the coordination through which
  platforms enroll and bind," which the seat reports their four models do not support.

Six are live legal facts to re-confirm in the submission week: Directive 2024/2831 transposition (holds
as of mid-August, Italy's draft in parliament), Apple's T-438/25 appeal still pending, COM(2025) 837 still
a proposal and not an enacted repeal — the present-tense "requires" in §3.2 and the "would remove" in §8
both depend on that — plus the WeChat/Bernot sentence and the Schegg and ECN PDFs, which seat 04 checked
against the research ledgers rather than re-fetching.

### 5c. Carried forward from `HANDOFF.md`, unchanged

- **Three citation items no fetch route has resolved.** Anderson (2017) pp. 57–58 and 141–142 remain
  unconfirmed, which is safe as long as no quotation is added. C. K. Anderson (2009, 2011) volume and
  issue, and the measured billboard lift — the figures are out of the chapter rather than asserted. BGH
  KVR 54/20 docket, optional, nothing depends on it.
- **Title.** The editor note declining condition #4 is drafted in `HANDOFF.md` §0c and ready to send.
  Sending it is what makes the retained title read as a decision.
- **Hunt et al. (2025), "Digital Battlegrounds," *AMA* 19, 265–297.** The current Annals synthesis of
  platform power, omitted under the no-self-citation instruction because of a surname collision with an
  unrelated author. The one gap a referee might notice.
- **The author's read-aloud.** Not substitutable. §5.2 and §6 carry the most new argument and the densest
  citation load; §5.5 is where the style seat says a prose referee will trip.

### 5d. Not in the repository

The IGI chapter template and the editor's submission instructions are not stored anywhere in this arm.
The chapter's structure matches IGI's standard, and conformance has been asserted from that structure
rather than checked against the actual template file. Get the template before submission week so the
reflow is a formatting job and not a discovery.

---

## 6. Changes made in this pass

The QA pass itself changed no prose. The fix pass that followed it applied the panel — `HANDOFF.md` §0g is
the record, and `chapter.md` is now 15,277 words with a 148-word abstract. Every statistic and every
quotation in the manuscript is byte-identical to the pre-pass text, so nothing on `SYNTHESIS.md`'s
do-not-touch list moved.

- `chapter/chapter.md` — one blank line inserted before `## References` (the render fix), then the panel's
  findings applied: 154 insertions, 138 deletions.
- `chapter/chapter_grammarly.md` — regenerated; now carries all five 14 August edits.
- `chapter/Full Paper - Alg & Sov.docx` — regenerated; verified for headings, table, anonymization, and
  smart quotes.
- `chapter/regen_exports.py` — new; regenerates both exports and lints the source.
- `chapter/README.md`, `submissions/coordinative_sovereignty/README.md` — corrected the export
  descriptions. The arm README had called the `.docx` "stale and superseded," which was true when written
  and is not now.
