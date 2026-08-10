# Internal verification — census claims against the census files

Checks every `claim_map.md` row marked `Retrievable? = internal` (29 rows) against
`v4/factbase/handoff_census.md` (the merged table) and the two independent codings,
`handoff_census_coder1.md` and `handoff_census_coder2.md`. Percentages and both kappa
values were recomputed from scratch from the two coders' own transition-by-transition
codes, not taken on the merged file's word. Then audits the five A3a conditions from
`v4/ASSUMPTIONS.md`, then recomputes the specific figures the task named.

---

## 1. Verdict table

| ID | Sentence (short) | Verdict | Basis |
|---|---|---|---|
| V-016 | "What follows the answerer runs about a hundred and thirty lines" | **confirmed** | Segment 5 runs from the overheard-friend line (line 152, coder 1: "bridge 146–152") to the 5→6 seam (line 280/281, both coders). 281−152 = 129, 280−151 = 129. "About a hundred and thirty" matches within rounding. |
| V-035 | "Of its first fifteen transitions, four or five carry an audible link." | **confirmed** | Recomputing transitions 1→2…15→16 from both coder files: both agree audible (SPOKEN-BRIDGE/ECHO) at 1→2, 4→5, 6→7, 7→8 (4); coder 1 alone adds 2→3 (ECHO), coder 2 codes it NONE. Band = 4–5, exactly as stated. |
| V-036 | "Of the middle fifteen — 16→17 through 30→31 — ten or eleven do." | **confirmed** | Both coders individually total 11 audible transitions across 16→17–30→31 (they just disagree on *which* 11: coder 1 has 22→23 equivocal/25→26 ECHO, coder 2 the reverse). Transitions both coders agree are audible = 10 (20→21, 24→25, 26→27 are the confirmed-NONE trio). Band = 10 (agreed floor) to 11 (either coder's own total) — confirmed, though the two numbers in the band are derived by different methods (intersection vs. either coder's total), worth noting if a referee asks how the band was built. |
| V-037 | "Of the last four, none [carry an audible link]." | **confirmed, narrow reading** | 31→32, 32→33, 33→34 are NONE/NONE in both codings — no dispute. 34→35 is EQUIVOCAL/EQUIVOCAL in both codings, not NONE. "None carry a link" is literally true (zero SPOKEN-BRIDGE/ECHO codes among the four), but this phrasing is defensible only because it stops short of asserting silence — see V-041/V-068 below, which do not stop there. |
| V-038 | Early bridges at 4→5 (missing-friend question) and 6→7 (Paul vanished, closed with invitation) | **confirmed** | 4→5 SPOKEN-BRIDGE/SPOKEN-BRIDGE both coders; 6→7 SPOKEN-BRIDGE/SPOKEN-BRIDGE both coders, agency DELIBERATE both. Matches merged table exactly. |
| V-040 | Middle stack: lift 18→19, address 23→24, guest list/van 27→28, stamp 29→30, camera 30→31 | **confirmed** (core); one descriptive detail outside census scope | All five transitions are SPOKEN-BRIDGE (or split-but-audible for 30→31) + DELIBERATE in both codings — matches. "A camera handed to a stranger" — the recipient's status as a "stranger" is not something the audio-only census can establish (coder 1: "Nothing below is inferred from the image"); not contradicted, just outside what this instrument can confirm. |
| V-041 | "from 31→32 to the end, nothing audible crossing a seam at all" | **overreach** | Same four transitions as V-037, but this phrasing asserts confirmed silence, not merely "no confirmed link." Both coders explicitly refuse to make that claim about 34→35: coder 2 writes "Coding NONE here would report an observation I have not made"; coder 1: "it cannot show either an audible link... or the absence of one." The census records an *unknown*, not a *silence*, at 34→35. |
| V-042 | "The film runs thirty-five segments, thirty-four of them with dialogue, and thirty-four transitions between them." | **confirmed** | Both coder files code all 34 transitions; both explicitly state segment 35 has no dialogue ("segment 35 has no dialogue; the transcript ends here" / "segment 35 is wordless and the transcript ends"). This is in fact more precise than the merged file's own header phrase ("35 dialogue segments" — see V-190). |
| V-043 | Method: two coders, same transcript, blind to each other, two questions (audible crossing / act producing next encounter) | **confirmed** | Matches `handoff_census.md` §1–2 and both coder files' opening method statements almost verbatim. |
| V-044 | "The codings agree on 82 percent of the first question (κ = 0.75) and 91 percent of the second (κ = 0.84)." | **confirmed, independently recomputed** | Row-by-row comparison of the two coder files: link dimension mismatches at 2→3, 19→20, 22→23, 25→26, 28→29, 30→31 = 6 of 34 → 28/34 = 82.4%. Agency mismatches at 22→23, 24→25, 28→29 = 3 of 34 → 31/34 = 91.2%. Cohen's κ computed from each coder's own marginal totals (link: SB 10/9, ECHO 6/6, NONE 13/15, EQUIVOCAL 5/4 → Pe=0.295, κ=0.7496; agency: DELIB 6/6, INCID 6/7, NONE 21/20, EQUIV 1/1 → Pe=0.4317, κ=0.8448) reproduces 0.75 and 0.84 exactly. |
| V-045 | "Fifteen or sixteen transitions carry an audible link; four or five are equivocal." | **confirmed** | Coder 1 total audible = 16 (5 first-third + 11 middle-third + 0 last-four); coder 2 total = 15 (4+11+0). Equivocal: both agree on 5→6, 12→13, 13→14, 34→35 (4); coder 1 alone adds 22→23 (5). |
| V-046 | Instrument = subtitle transcript, no speaker names, subtitles compress/paraphrase, disc may move the numbers | **confirmed** | Matches both coder files' opening statements and `handoff_census.md` §1 verbatim in substance. |
| V-047 | "Six transitions, identical in both codings, are deliberate — five of them in the film's middle third." | **confirmed** | Both coder summary tables list the identical set: DELIBERATE at 6→7, 18→19, 23→24, 27→28, 29→30, 30→31 (6, no disagreement). Under the partition the chapter itself already uses elsewhere (first fifteen / middle fifteen [16→17–30→31] / last four — see V-035–037), five of the six (18→19, 23→24, 27→28, 29→30, 30→31) fall in the middle-fifteen group and one (6→7) in the first. Confirmed under that reading; if "middle third" instead meant an equal three-way split of the 35 segments, only one (18→19) would land in the middle band, so the claim depends on the chapter's own established partition rather than a literal thirds split — worth a sentence of cross-reference if a referee reads "middle third" literally. |
| V-048 | Definition of DELIBERATE, incl. self-direction exclusion | **confirmed** | Near-verbatim match to both coder files' method notes, including the identical 16→17 example ("I'm gonna go look at some books"). |
| V-049 | The six, in order, with descriptions | **confirmed** (core); two descriptive details not checkable | Order and identity of the six transitions match exactly. "Offered to two women who accept" — gender is not recoverable from a dialogue-only transcript (both coder files state no visual/character-identity information is used); not contradicted, just outside the census's evidentiary reach, and arguably brushes against ASSUMPTIONS A3's ban on any claim about what is visible. "A driver who wants no part of the trip" — the quoted evidence (1041: "This whole neighborhood and you couldn't get a fuckin' TV?") is consistent with reluctance but no coder characterizes the driver as unwilling; a fair gloss, not a quoted finding. |
| V-054 | "No transition in either coding pairs a silent seam with a deliberate act" | **confirmed** | `handoff_census.md` §7, verbatim: "No transition in either coding is NONE + DELIBERATE... there is no silent handoff in the dialogue record." |
| V-055 | "Among the seams the codings leave bare, five hold a checkable offer, invitation, or destination the film declines to follow" | **confirmed** | `handoff_census.md` §7: "five contain a quoted, checkable offer, invitation, or stated destination that the film declines to follow — not nine... The exact number substantiated here is five, not nine." |
| V-065 | Drafting correction: "I first drafted that list of five with nine seams on it, and rechecking... left five" | **split — see note below** | The "five" half is fully confirmed (§7, as above). The "nine" half is not checkable against the census files at all in the sense the sentence implies. |
| V-068 | "the four transitions that carry them carry nothing audible at all: the cut has the film back" | **overreach** | Same problem as V-041: if "the four transitions" is 31→32–34→35 (consistent with V-066/V-067's segments 33–34 and the established last-four grouping), one of the four (34→35) is EQUIVOCAL, not confirmed silent, and both coders explicitly decline to assert absence there. |
| V-069 | "Five equivocal seams stay equivocal, each one the disc could settle." | **confirmed**, phrasing nuance flagged | The five named DISC-flagged rows (5→6, 12→13, 13→14, 22→23, 34→35) are exactly the five equivocal transitions across the two "Every EQUIVOCAL" lists (coder 1 lists all five; coder 2 lists four and reports 22→23 as ECHO, not equivocal, which is precisely the swing case). This is defensible as "listing five candidate rows," but stated as a bare number it reads as a point estimate rather than the "four or five" band used at V-044/045 for the same underlying count — see A3a §1 below. |
| V-075 | "Three pairs of segments also share overlapping line ranges, and several boundaries fall inside continuous exchanges" | **confirmed** | Coder 2's method note, verbatim: "Overlapping ranges. Three pairs overlap by design: 6/7 at 308–318, 17/18 at 809–815, 18/19 at 848–851." The "several boundaries... inside continuous exchanges" matches the additional four rows both coders separately flag (7→8, 12→13, 21→22, 28→29, plus 25→26). |
| V-087 | Restates the per-third audible-link figures | **confirmed**, same caveat as V-037 | Identical numbers, identical narrow-reading caveat about "none in the last four" glossing over 34→35's EQUIVOCAL status. |
| V-088 | "The invitation and the van in segment 27 produce segment 28's ride — one of the six deliberate handoffs" | **confirmed** | 27→28: SPOKEN-BRIDGE/SPOKEN-BRIDGE, DELIBERATE/DELIBERATE, both coders. Merged table: "Invitation, guest list, and a named vehicle, all before the cut. Segment 28 is the ride." |
| V-114 | "the census records no deliberate handoff anywhere near it [the club door]" | **contradicted** | The census records exactly one DELIBERATE act at this door, agreed by both coders: transition 29→30, the stamp offered, demonstrated, and redeemed at the very next door — the same act the chapter itself lists as one of the six deliberate handoffs at V-049 ("the stamp offered at one door, demonstrated, and claimed again at the very next one"). That handoff sits inside the same door sequence V-109–113 describes (pricing at 29/30, name-check at 28/29, eviction at 31/32). If V-114 means specifically "the doorman/door-as-institution never itself performs a deliberate act," that reading is supportable (28→29 and 31→32 are both non-DELIBERATE in both codings), but as worded — "no deliberate handoff anywhere near it" — the sentence is contradicted by the chapter's own other claim about the stamp. This is the single clearest internal inconsistency found in this pass. |
| V-147 | "twenty-nine lines into the next segment, a bystander... works out that the driver ran over his own mother" | **confirmed** | Segment 2 opens at line 86 ("Don't touch her. Need to call the police."); the payoff line is 115 ("Looks like some guy, uh, ran over his mother."). 115−86 = 29. |
| V-148 | "Both codings record the echo, and both record its agency as none" | **confirmed** | 1→2: ECHO/ECHO, NONE/NONE in both files. Coder 2's own row commentary: "The only ECHO with agency NONE... The film's connective work here is entirely the film's." |
| V-189 | "six candidate lines... disputed... are withheld from quotation" | **confirmed** | `ASSUMPTIONS.md` A3b: "Six of the seventeen candidate quotations are already flagged in disc_worksheet.md as disputed in placement or wording; those may not be printed as speech before an afternoon with the disc." Matches in count and characterization. |
| V-190 | "Segment numbers follow my division of the film into thirty-five dialogue segments." | **confirmed** | Matches the merged census's own header phrase verbatim: "the 35 dialogue segments of *Slacker*." (Segment 35's actual lack of dialogue is a separate, more precise fact the chapter states correctly elsewhere — V-042 — without contradicting this labeling convention.) |
| V-195 | "the two coders' full tables, with every disagreement preserved unresolved rather than reconciled by fiat, are available from the author" | **confirmed** | Both `handoff_census_coder1.md` and `handoff_census_coder2.md` exist as described, coded independently ("without seeing each other's work"), and the merged file's §4 states explicitly: "None is resolved here." Every one of the nine link/agency disagreements is presented as a live disagreement, not adjudicated. |

**Verdict counts:** confirmed 25 (one of those, V-047, confirmed under a specific reading worth cross-referencing; several others carry minor unconfirmable descriptive details noted inline but not counted against the verdict) · overreach 2 (V-041, V-068) · contradicted 1 (V-114) · split/not-checkable 1 (V-065, half confirmed / half not-checkable) · unsupported 0 · not-checkable (pure) 0.

---

## 2. The V-065 special case: the "nine to five" correction

> "I first drafted that list of five with nine seams on it, and rechecking every row against both coders' files left five, which is the number that prints."

The census **can** confirm the destination: `handoff_census.md` §7 independently verifies, by checking each of coder 2's fifteen NONE-on-both rows against both coder files and the transcript, that exactly five contain "a quoted, checkable offer, invitation, or stated destination that the film declines to follow — not nine." That work is reproduced in the file, row by row, and matches the "five" the chapter prints.

What the census **cannot** confirm is the first half of the sentence — that an earlier draft of *this chapter* listed nine. The census files contain no draft history of the chapter. They do contain a documented source for a "nine" figure, but it is not the chapter's own earlier draft: coder 2's file states, in its own commentary, "nine of the fifteen NONE-on-both rows contain a deliberate act... that the film declines to follow" — an uncorrected claim in coder 2's own working notes, which the merged census then checks and revises down to five. It is entirely plausible that an earlier chapter draft simply inherited coder 2's uncorrected "nine" before the recheck happened — the merged file's own narrative is consistent with that history — but the census files record the *coder's* nine, not the *chapter's* nine, and nothing here can settle whether the chapter's drafting history matches that account. As worded, "I first drafted that list of five with nine seams on it" claims something about the chapter's own manuscript history that only surviving drafts (not the census) could settle, so it is not fully checkable against the files this task specifies. The chapter should either soften the drafting-history claim to what the census can support (the number was checked and corrected from nine to five, full stop, without asserting whose nine it originally was) or produce the earlier draft as a second source.

---

## 3. A3a compliance audit

`ASSUMPTIONS.md` permits an asserted count of audible joins only if all five conditions hold.

**1. Published as a band, not a point estimate.**
Mostly satisfied. The chapter's central numbers are explicit bands: V-044/045 "fifteen or sixteen... four or five," V-035 "four or five," V-036 "ten or eleven," matching the census's own two-coder disagreement exactly (verified above by independent recomputation). The one soft spot: **V-069**, "Five equivocal seams stay equivocal," states the equivocal count as a bare five rather than repeating the "four or five" band used elsewhere for the identical underlying figure. This is partially rescued by the neighboring author-flagged row V-073, which says of the swing case (22→23) explicitly: "this single case is what makes the figure a band instead of a number" — so the chapter does, somewhere, name the band-not-point reasoning, but V-069 itself reads as a point estimate in isolation. Recommend tightening V-069 to "four or five" or adding an inline pointer to the swing case at the same sentence.

**2. Every equivocal case listed by segment pair.**
Satisfied. The five equivocal transitions the census records (5→6, 12→13, 13→14, 22→23, 34→35) are each given their own `[DISC:...]`-flagged row (V-070–V-074), by segment pair, matching both coder files' own "Every EQUIVOCAL" lists exactly.

**3. The coding method stated in the chapter.**
Satisfied. V-043 states the two-dimension scheme and the blind-coding setup; V-048 states the DELIBERATE definition and its self-direction exclusion, matching both coder files' method notes almost verbatim.

**4. Marked subtitle-derived throughout.**
Likely satisfied but not fully verifiable from the claim map alone. V-046 states the instrument is a subtitle transcript, compressing and paraphrasing, in the same cluster of sentences as the core counts (V-035, V-036, V-044, V-045). Whether that marking is repeated at every later reuse of the figures (V-069, V-087, V-114, etc.) or stated once and relied on, as Note 1 does for dialogue quotation generally, cannot be settled from the claim map's row-by-row excerpts — this needs a check against the full chapter text, which is outside this task's scope.

**5. Stated as revisable by the disc.**
Satisfied. V-046 ("an afternoon with the disc may move these numbers"), V-069 ("each one the disc could settle"), and the `[DISC:...]` markers on every equivocal row all state revisability explicitly and repeatedly.

**Overall: four of five conditions cleanly met; the fifth (band-not-point) has one weak instance (V-069) that a referee could reasonably flag, and the fourth (marked throughout) cannot be fully audited from the claim map excerpts alone.**

---

## 4. Recomputed figures

| Figure | Chapter's claim | Recomputed from census files | Match? |
|---|---|---|---|
| Agreement, audible-link question | 82% | 28/34 = 82.4% | Yes |
| Agreement, agency question | 91% | 31/34 = 91.2% | Yes |
| κ, audible-link | 0.75 | Computed from coders' own marginals: Pe = 0.295, κ = (0.8235−0.295)/(1−0.295) = 0.7496 | Yes |
| κ, agency | 0.84 | Pe = 0.4317, κ = (0.9118−0.4317)/(1−0.4317) = 0.8448 | Yes |
| Audible-link band | 15–16 of 34 | Coder 1 total 16, coder 2 total 15 | Yes |
| Equivocal band | 4–5 of 34 | Agreed-equivocal 4 (5→6, 12→13, 13→14, 34→35); coder 1 adds 22→23 for 5 | Yes |
| Count of deliberate acts | 6 of 34 | Both coder summaries list identical DELIBERATE sets: 6→7, 18→19, 23→24, 27→28, 29→30, 30→31 | Yes |
| Number of segments | 35 | Both coder files code against the 35-segment ledger; segment 35 explicitly noted as dialogue-free by both | Yes |
| Number of transitions | 34 | Both tables run 1→2 through 34→35 | Yes |
| Count of spoken-but-unfollowed plans | 5 (chapter corrects an earlier 9) | `handoff_census.md` §7: checked against all 15 NONE-on-both rows, "the exact number substantiated here is five, not nine" | Yes (see §2 above for the caveat on the "nine" half of V-065) |

**No figure in this list fails to match.** The two flagged problems in this pass are not numeric errors — every count, percentage, and kappa the chapter prints reproduces exactly from the underlying coder files — but two overreaching characterizations (V-041, V-068, both claiming confirmed silence where the census records "equivocal," i.e., unknown) and one direct contradiction (V-114, claiming no deliberate handoff near the club door when the census records one, which the chapter's own V-049 already names).

---

**Files checked:**
- `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/slacker_thirds/v4/verification/claim_map.md`
- `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/slacker_thirds/v4/factbase/handoff_census.md`
- `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/slacker_thirds/v4/factbase/handoff_census_coder1.md`
- `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/slacker_thirds/v4/factbase/handoff_census_coder2.md`
- `/Users/ludwitt/iit-playground/pyphi-experiments/org_frontier/slacker_thirds/v4/ASSUMPTIONS.md`
