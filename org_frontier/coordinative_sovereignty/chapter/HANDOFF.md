# Handoff — what the author must do before submitting

Rebuild completed 2026-08-01. Chapter due **2026-08-30**. This file lists everything the rewrite could not
close, ranked by how much damage it would do if it reached a referee unfixed.

Artifacts: `REVIEW.md` (section-by-section critique) · `OUTLINE.md` (architecture + contextual
bibliographies) · `research/section_*.md` (six deep-research files, ~480KB, each with a citation ledger) ·
`chapter_prerewrite_c247e56.md` (the pre-rewrite text, for diffing).

---

## 1. Citation verification — second pass, 2026-08-01

A second verification pass ran after the fetch budget reset. **Sixteen of the eighteen outstanding entries
are now verified**, several with corrections. Two could not be resolved by any available route.

### Verified this pass

| Entry | Result |
|---|---|
| **Schegg (2024)** | **VERBATIM from the HOTREC PDF.** "the share of direct bookings decreased by nearly 7 percentage points from 57.6% in 2013 to 50.9%" and "rising from 19.7% in 2013 to 29.6% in 2023." Author, title, institution, and date (Sierre, June 2024) all confirmed. **The evidence answering Reviewer 2 holds.** |
| **European Competition Network (2017)** | **VERBATIM,** §4.4, p. 17: "The basic commission rates of the three major OTAs range from ten percent to above twenty percent." Published 6 April 2017. Full title confirmed. Prompted one wording fix: OTAs are "paid solely on the basis of a share of each booking," so §5.5 now says "of each booking" rather than "of the room rate." |
| **Gagričin et al. (2026)** | Verified **with three corrections.** The surname is **Gagričin**, not Gagrčin. The subtitle is "An integrative **literature** review." Pages are 423–447 with DOI 10.1177/14614448241291137, so it is not issue 1. All three now applied. |
| **Cotter & Reisdorf (2020)** | Verified on the IJoC article page: *International Journal of Communication* **14** (2020), and the title really is "A new **Horizon**." **Restored to §4**, where the abstract supports the claim directly — "algorithmic knowledge varies according to socioeconomic advantage." |
| **Baldwin (2008)** | DOI 10.1093/icc/dtm036 confirmed and added. |
| **Bernot (2025)** · **Stadnik (2021)** · **Gehl & Zulli (2023)** · **Fortuny-Sicart et al. (2024)** · **Tortorici (2026)** | All five DOIs resolved. Titles, authors, venues, volumes, and pages exact as cited. |
| **Paglayan (2024)** · **Bishop (2020)** · **MacDonald (2023)** | All three resolved. Bishop's abstract confirms the §9 claim directly: the experts "encourage compliance with YouTube's business models rather than systemic change." |
| **Schlager & Ostrom (1992)** · **Cicerchia (2022)** | Both resolved as cited. |
| **Pettit (2016)** | **Partial.** DOI, title, author, journal, volume, and issue confirmed. Crossref carries **no page numbers** and a corrupted date field. The reported range 47–68 is unconfirmed, so it has been **removed** from the bib rather than asserted. |

### Still unresolved — two entries

| Entry | Routes tried | What to do |
|---|---|---|
| **Klonick (2020)**, *Yale Law Journal* 129(8), 2418–2499 | Crossref (no record), yalelawjournal.org (403), OpenAlex (429), Semantic Scholar (429), St. John's repository (JS-only search) | **Check a library copy.** It is the sole source for §7's oversight-board paragraph. Volume and pages are the fields at risk. |
| **Anderson (2017)** page cites | Book metadata verified (DOI 10.1515/9781400887781); De Gruyter (405), Google Books (429) | The text was never accessible. The reported passages at pp. 57–58 ("political hemiagnosia") and pp. 141–142 ("harvest the entire producer's surplus") are **unconfirmed**. The chapter cites her argument without page numbers, which is safe as it stands. Confirm before adding any quotation. |

### Not re-checked this pass

**Klawitter & Hargittai (2018)** — absent from both Crossref and the IJoC search index, and the venue in the
research file was truncated. **Left out of the chapter.** §4's distributional paragraph now rests on Cotter &
Reisdorf plus Petre et al., which is sufficient.

**Anderson, C. K. (2009)** billboard report (Cornell 403) · **BGH KVR 54/20** docket · **Parmigiani (2007)** ·
**COM(2025) 837** · the **Google €890m** decision of 23 July 2026. The Anderson report and the German docket
matter most of these, since §5.5 leans on both.

### A bug this pass caught in the existing bibliography

`literature/references.bib` carried **two** problems predating the rebuild, now fixed:

1. The kickoff-layer `markell2008` entry still had DOI `10.1177/0090591707310220`, which does not resolve.
   `verification_pass_2.md` established the correct DOI over a month ago and applied it to the chapter, but
   it was never propagated to the bib.
2. `anderson2017private` was a **duplicate bibtex key** — the entry already existed in the kickoff layer, and
   the rebuild added a second one. Duplicate keys break bibtex silently. Merged into the original.

## 3. Claims that changed, and what a co-author should know

These are not wording changes. Anyone reading the old draft will find the argument different here.

1. **Algorithmacy's novelty narrowed.** The old draft said "Algorithmacy adds no new part. It adds their
   integration." DeVito (2021) — cited in the chapter as an ally — already defines an integrated, adaptive
   competence, so that sentence was refutable by one citation. The draft now concedes integration by name and
   claims the **triadic setting** plus the competence→standing link.
2. **The pairing thesis was conceded to Habermas.** "This chapter adds a different axis" was false; Habermas
   already pairs a competence with a medium. §2 now claims the **unevenness within an era** instead, and
   dropped from 1,186 to ~800 words.
3. **Repetto was cited backwards.** The old draft had him charging the field with concept-stretching. He
   argues the opposite and is now cited in support.
4. **Selznick was cited backwards.** The old draft said his co-optation "granted the co-opted a real seat,"
   making the platform case "near its antonym." That holds only for *informal* co-optation. Platform
   enrollment is *formal* co-optation with the forms of participation removed — a narrowing along Selznick's
   own axis.
5. **The competitive-bottleneck mechanism was inverted** in two places. Armstrong's multi-homing side is the
   extracted one. Corrected, and it now fits the App Store example better.
6. **Hirschman's lazy monopoly was reversed.** His lazy monopolist is *relieved* by exit (Ch. 5, "How
   Monopoly Can Be Comforted by Competition"). §5.3 now states his actual point and uses it.
7. **"Computable" is gone from the conclusion**, per the panel's spine fix #7, which had never been applied.
8. **The OTA case was factually wrong in three of four particulars** and is now a live test of the
   diagnostic rather than an illustration. See §5.5.

## 4. Open panel findings — status

| Finding | Status |
|---|---|
| Answer Reviewer 2 in §5 (vs Burt / Williamson / essential facilities) | **Closed.** §5.2 now runs the node-versus-edge argument, demonstrates disagreement on the dealer case, and names the ancillary-restraints doctrine as the closest relative. |
| One case worked fully through the diagnostic | **Closed.** New §5.5. |
| Bearer: person or firm | **Closed.** §6, via Pettit (2016) on corporate bearers of non-domination. |
| Diffusion mechanism | **Closed.** §9, and the honest answer (compulsion, and a market that teaches compliance) is better than the hopeful one. |
| Instrument → mediator-type crosswalk | **Closed.** Table in §7. |
| Normative core (independence leaves an actor less sovereign) | **Closed.** §1, via Berlin and Anderson. |
| Decision rule for a `partial` verdict | **Closed.** §5.4. |
| What the oracy/literacy frame buys | **Closed.** §2 now answers it explicitly. |
| Title revision (volume editor's condition #4) | **Declined by author decision.** The deck, poster, and accepted abstract all carry the current title. Worth a line to the editor so it reads as a choice. |
| Borderline case where Φ and the plain counterfactual diverge | **Not closable here.** The chapter carries no Φ. It belongs to the companion paper. The chapter no longer overclaims in its place. |

## 5. Things I deliberately did not do

- **No first person.** Your global `~/.claude/writing-style.md` requires it; the repo's `CLAUDE.md` bans it;
  the chapter is external IGI academic APA and had none. The venue won. Say if you want it changed.
- **No citation to any work by you, Berthon, or Whitmer**, per your instruction, beyond the masked
  "Author (2026)". That excluded **Hunt et al. (2025), "Digital Battlegrounds," *AMA* 19, 265–297** — the
  current Annals synthesis of platform power, by Richard A. Hunt of Virginia Tech, no relation. Its absence
  is the one gap a referee might notice. Reconsider if you are comfortable with the surname collision.
- **Som Mobilitat dropped** from §8 — no peer-reviewed anchor exists. CoopCycle replaced it.
- **Braun & Hummel (2025), Krasner (1999), Smith & Burrows (2021), Armstrong & Wright (2007)** all dropped
  from the citation list. Krasner moved to Additional Reading. Smith & Burrows was being used for a claim
  about exit from digital infrastructures; their actual subject is neoreactionary exit via Urbit.

## 6. Style audit, before and after

| Marker | Before | After | Target |
|---|---|---|---|
| Antithesis machine | 11 (1.0/1k) | 33 (2.9/1k) | under 5/1k |
| Agentless passive | 0 | 0 | 0 |
| Self-reference ("this chapter") | 9 (0.8/1k) | 2 (0.2/1k) | ≤2 |
| Em-dashes | 15 (1.3/1k) | 11 (1.0/1k) | ≤1 per paragraph |
| Filler transitions | 0 | 0 | 0 |
| Banned openers | 0 | 0 | 0 |
| Body words | 11,203 | 11,313 | ≥10,000 total |
| Abstract | 148 | 148 | ≤150 |
| Total | 13,463 | 14,315 | ≥10,000 |

The antithesis count rose and stays well inside the bar. Twenty of the thirty-three are "rather than"; five
decorative ones were cut and the rest carry contrasts a reader would otherwise reach for wrongly. Over-thinning
this construction is its own tell, and five reviewers on the previous panel confirmed the machine was already
near-absent.

**No automated checker certifies prose.** The read-aloud is yours, and §5.2 and §6 are the passages I would
read aloud first — they carry the most new argument and the densest citation load.
