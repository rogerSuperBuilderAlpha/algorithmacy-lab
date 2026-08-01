# Handoff — what the author must do before submitting

Rebuild completed 2026-08-01. Chapter due **2026-08-30**. This file lists everything the rewrite could not
close, ranked by how much damage it would do if it reached a referee unfixed.

Artifacts: `REVIEW.md` (section-by-section critique) · `OUTLINE.md` (architecture + contextual
bibliographies) · `research/section_*.md` (six deep-research files, ~480KB, each with a citation ledger) ·
`chapter_prerewrite_c247e56.md` (the pre-rewrite text, for diffing).

---

## 1. Citations that must be verified before submission

Every citation below entered the draft on a research agent's verification, not mine. The session's WebFetch
budget ran out before I could resolve them independently. **This project has a documented history of agents
fabricating author lists and DOIs, so treat every unverified entry as suspect until a DOI resolves.**

Verify by resolving `https://api.crossref.org/works/<DOI>` or the publisher's page, and check the author list
character by character.

| Entry | What to check | Risk |
|---|---|---|
| **Klonick (2020)**, *Yale Law Journal* 129(8), 2418–2499 | **No Crossref record exists.** YLJ returned 403 on every route tried. Confirm volume, issue, and pages against a physical or library copy. | High — it is the only source for §7's oversight-board paragraph |
| **Gagrčin, Naab & Grub (2026)**, *New Media & Society* 28(1) | The subtitle "An integrative review" is reconstructed, not read off a record. Confirm the exact title and add page or article numbers. | High — a wrong title is an obvious tell |
| **Baldwin (2008)**, *Industrial and Corporate Change* 17(1), 155–195 | DOI omitted deliberately (unverified). Add it once confirmed. | Medium |
| **Berlin (1969)**, "Two concepts of liberty" | No page range given, because the "cutting off my legs" passage was paraphrased rather than quoted. If you want the quotation, get the page. | Medium |
| **Anderson (2017)**, *Private Government* | Book metadata verified (DOI 10.1515/9781400887781). The text was **not** accessible. The research reports the supporting passages at pp. 57–58 ("political hemiagnosia") and pp. 141–142 (exit rights let the employer "harvest the entire producer's surplus"). **Confirm both before adding any page cite or quotation.** | Medium |
| **European Competition Network (2017)** | §4.4, p. 17 of the hotel monitoring report — confirm the "ten percent to above twenty percent" figure and the section number. | High — it replaced a wrong number in the draft |
| **Schegg (2024)**, HOTREC distribution study | Confirm 19.7%→29.6% OTA share and 57.6%→50.9% direct, for 2013 and 2023. | **Highest — this is the evidence answering Reviewer 2** |
| **Anderson, C. K. (2009)**, *Cornell Hospitality Report* 9(16) | Confirm the 7.5–26% range and that independent hotels sit at the upper end. | High |
| **German ruling, 2021** | The draft says "the German Federal Court of Justice held the agencies' narrow parity clauses unlawful in 2021" without a docket. Research reports **BGH KVR 54/20**. Confirm and add if you want the citation. | Medium |
| **Bernot (2025)**, **Stadnik (2021)**, **Gehl & Zulli (2023)**, **Fortuny-Sicart et al. (2024)**, **Tortorici (2026)** | All five case citations came from research agents. Resolve each DOI. | Medium |
| **Paglayan (2024)**, **Bishop (2020)**, **MacDonald (2023)** | The diffusion argument in §9 rests on these three. | Medium |
| **Pettit (2016)**, **Schlager & Ostrom (1992)**, **Cicerchia (2022)**, **Parmigiani (2007)** | Recorded with DOIs in the research files; resolve them. | Low–medium |

**Verified by me directly this session** (safe): Armstrong (2006) · Bannerman (2024) pages · Curchod et al.
(2020) · Gu & Zhu (2021) · Jarrahi & Sutherland (2019) · Muldoon & Raekstad (2023) year · O'Reilly et al.
(2024) · Petre et al. (2019) · Repetto (2025) and its abstract · Robinson et al. (2026) author list · Ryall &
Sorenson (2007) · Sekar & Siddiq (2026) · Sutherland et al. (2020) · Beritelli & Schegg (2016) · Case
C-264/23 · Directive 2024/2831 Arts. 25 and 29(1) · COM(2026) 178 · Regulation (EU) 2026/1744.

## 2. Two sources cut for lack of verification — add them back if you can confirm

Both are almost certainly real and both would strengthen §4's distributional paragraph, which currently rests
on Petre et al. alone. Neither is in Crossref because *International Journal of Communication* does not
deposit DOIs.

- **Cotter, K., & Reisdorf, B. C. (2020). Algorithmic knowledge gaps: A new horizon of (digital)
  inequality.** Note the title trap: the version of record reads "A new **horizon**," where many indexes
  report "A new dimension."
- **Klawitter, E., & Hargittai, E. (2018). "It's like learning a whole other language": The role of
  algorithmic skill…**

The sentence to restore them to is in §4, immediately before "Petre et al. (2019) identify a mechanism…".

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
