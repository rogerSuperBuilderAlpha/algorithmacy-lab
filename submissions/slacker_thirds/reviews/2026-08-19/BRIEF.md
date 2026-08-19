# Panel brief — *Slacker* chapter v17 — 2026-08-19

Eight-seat panel on the **live** manuscript. v17 has never been read by a panel: round 10
(`old/archive/reviews/2026-08-18-v16/`) judged v15, and round 11 was a single sentence audit that turned
v16 into v17. You are the first readers of this text.

**Manuscript:** `/Users/ludwitt/iit-playground/pyphi-experiments/submissions/slacker_thirds/chapter.md`
Pinned at commit `db5468d643d4985d87a26da901f8155353ab5c6f`, mtime Aug 18 20:02:21 2026.
Body **4,470 words** through the `## Notes` heading; 39 endnotes; 52 bibliography entries.
Title: "'You seen Gary around?': The Deferred Third of *Slacker*."

**Judge the current file.** Do not review anything under `old/`. Read the archive only to check whether a
prior finding was closed.

**Venue.** Bloomsbury collection *Slacker: Answering the True Call — Essays on Linklater's Cult Classic*,
eds. Sara Bizarro (UNO) and Melissa Remark (Nicholls State). Final draft due **2026-11-01**; optional
feedback draft 2026-10-01. Length **3,000–5,000 words**, stated as a firm range with no overage. Chicago,
notes as **endnotes**, US English (Merriam-Webster's Collegiate 11th). Terms: `../../COLLECTION_TERMS.md`.

**What governs.** `../../CLAIM.md` is the locked question and thesis. You may attack the argument; you may
**not** propose a different thesis. `../../outline.md` is v15 and **stale on the platform section** — it
specifies Amazon, which v16 rebuilt onto Uber. Where outline and CLAIM disagree, CLAIM wins, and a finding
grounded only in the stale outline will be declined.

**The accepted abstract** (`../../abstract.md`) promised hosting/engineering thirds, Lofland, Möhlmann, and
a century-of-viewer-training claim. None of that survives in v17; the vocabulary went hosting/engineering →
setting/selector → the deferred third. That divergence is real, unmanaged, and seat 04's central question.

---

## Register and bar (every seat)

**Register:** a first-person film-studies collection chapter in the Hansen/Bordwell manner. "I" steers;
scenes before theses; contractions; pointed concessions. **That register is deliberate.** The
dissertation's no-first-person rule and the *Annals* "I marks labor only" rule **do not apply here**.

**Off-limits as prose defects** — reporting any of these as slop is a failure of the seat:

- first person; contractions; scenes stated before theses; pointed concessions
- quoted dialogue and quoted scholarship (including trims marked with an ellipsis)
- the title line and the closing line, "whether anyone has seen Gary around"
- the two licensed refrains, each of which occurs exactly once and is *meant* to:
  "sharing a city is not sharing a past" and "somebody is always standing there to be asked"
- any accepted-abstract verbatim line that survives

Three separate slop-hunters in this project's history have flagged the author's own prose — including
lines lifted verbatim from his accepted abstract — as machine parallelism. No detector distinguishes a
distinctive human voice from a machine one. If you find yourself flagging the liveliest sentences in the
chapter, re-read this block before you write the finding.

**The cardinal rule.** Make the chapter better at being itself. Every proposed rewrite must be in the
author's diction, shorter than or equal to what it replaces, and more concrete. If your rewrite comes out
more nominalized, more hedged, more passive, or more journal-generic than the original, delete it.

**House invariants that do bind** (`~/.claude/writing-style.md`): named agents and active voice; claim-first;
every abstraction touches a case; verified citations; deliberate rhythm variation; no self-narrating rigor;
no antithesis machine run as a tic. Note that the same file holds em-dashes to be **load-bearing and not an
AI tell**, and says not to ration them below roughly 3 per 1,000 words.

**Verification rule.** Before proposing any factual or citation correction, tag it:

- `VERIFIED` — you retrieved the source in this session. Say how, and give the URL or edition.
- `UNVERIFIED — do not adopt` — suspicious but unretrieved. State it as a question in your VERIFY section.
- `AUTHOR-ONLY` — needs the disc or a library copy.

An untagged correction, or one tagged `UNVERIFIED`, **cannot enter the synthesis**. Reviewers hallucinate
corrections; this rule is mechanical, not a matter of judgment. Do not invent a page number or a locator.

**Fetch chain** when you need a source: WebFetch first; on 403 fall back to `curl -sL` with a browser
user-agent; then a Wayback snapshot via curl. Record which tier produced each verification. WebFetch is
blocked outright from `web.archive.org`; curl is not.

**Do not edit the chapter, and do not edit anything under `old/`.** Write only to your own file.

---

## Mechanical pack (locators — evidence, never verdicts)

Full output in `mechanical/`. The headline numbers, so no seat spends a finding rediscovering them:

- `check_bans.py`: **no verbatim bans**, no rate tell over budget. Landing lines 5/28 paragraphs (18%,
  threshold 25%). Two unglossed jargon terms flagged: *divide et impera*, *tertius gaudens*.
- `check_quotes.py`: 98 quoted spans. All 20 dialogue quotations resolve against `../../sources/transcript.md`.
  The 23 body quotations that do not resolve are all scholarly, legal, or web sources — correct. **No
  unsourceable line of dialogue.**
- `check_film.py`: PASS. 17 of 66 lexicon scene terms present. Longest filmless run **214 words**, starting
  "The definition is permissive at every point where one might expect strictness."
- `apparatus_v17.txt`: 39 note markers, 39 notes, no duplicates, no orphans either direction, first-use
  order sequential, 5 three-em dash continuations. **Apparatus is mechanically clean.**
- `report.py` five-tier, register `slacker`:
  - tail-head linkage 43.2%; **88.9% of paragraph joins share no entity**; 0 citation-final sentences
  - sentence-length CV 0.796 (z = +1.89); sentences under 10 words 14.1% (z = +1.17); four-plus-clause
    20.1% (z = +1.24); one-clause 30.2% (z = −1.09) — the report calls this shape a **barbell**
  - **em-dash 0.00/1k — a Tier 3 DEFICIT**, below every one of the 42 exemplars (band 0.35–10.88)
  - **semicolon 7.01/1k against a corpus mean of 2.39 (z = +2.85)**, flagged `high` by `check_bans` too
  - Tier 4 (corpus-mined discovery) is **skipped** — there is no `slop.json` for this register. You cannot
    lean on discovery; argue every flag from the text.

**Two calibration warnings.**

1. The `slacker` register's `profile.md` still says "declared, UNCALIBRATED." That text is stale:
   `floors.json` and `targets.json` were built from 42 documents and Tier 3 does gate.
2. That corpus is 42 open-access film-studies chapters (Epstein, Farocki, *Camera Obscura*, *Film
   Architecture*) — **genre-adjacent, not single-film chapters, and carrying no headings at all**. A
   z-score is a genre difference, not a fail. A prior panel formally resolved the short-sentence z as
   genre, not defect, and ruled that lengthening those sentences would damage the chapter. Any finding
   whose only evidence is a z-score will be downgraded to a locator unless you argue it from the text.

**One artifact of the sentence splitter** (`v17_sentences.txt`): a single quoted line can break across
indices — "Take my card. / Give me a call. … / I mean it," is one line of dialogue, not three fragments.
Do not report splitter artifacts as prose defects.

---

## Output format (every seat)

Write to your assigned absolute path. Structure:

0. **Word-budget impact.** Every change you propose, classed: *word-negative* / *word-neutral* /
   *adds N words*. Give a total for your seat. The body is 4,470 against a 5,000 ceiling — roughly **530
   words of headroom for the whole panel**, and eight seats each proposing three additions will blow it.
1. **Title block** — seat, manuscript, venue, your standpoint.
2. **Step 0 — register and bar.** Confirm the register in two lines; state what you will judge hard.
3. **Part 1 — findings, ranked by damage**, section-aware. For each: the claim, a quote with enough
   context to locate it, why it damages *your* lens, and what would fix it. If a section is clean for your
   lens, say so in one sentence and move on.
4. **Part 2 — seat-specific audit** (see your seat block).
5. **Part 3 — paste-ready revisions.** Highest-value only, in the author's voice, ready to drop in.
6. **Verdict** — accept as-is / minor revisions / major revisions / reject. Then: the single most important
   fix, the biggest genuine strength, and the one thing only the author can supply.
7. **VERIFY** — claims needing sourcing before press, with tags.
8. **Closed-item re-check** — every item in the list below, one line each: **Holds** / **Regresses** /
   **Not this seat**.
9. **What this seat is not judging.**

Prefer fewer, sharper findings to a laundry list. Quote the manuscript. Do not soft-pedal, and do not
invent problems to fill the form. Each review is a complete critical commentary from its lens, not a
capped bullet list. Do not compress yourself to bullets.

---

## Closed items — re-check, do not re-open

Claimed closed by the v16 rewrite and the gap-fill pass. Confirm each still holds in v17. A closed fix
reported as a fresh finding is the failure mode this list exists to prevent.

1. Steve is put on a **venue-kept** list, not one he owns; the door scenes happen **at night**; his lines
   are quoted as spoken.
2. The Gary framing: the asker is a returning acquaintance, and the stranger claim rests on the sidewalk
   pairing with the talker, not on the café exchange.
3. The dream line is about dreams ("there is always someone getting run over"), not about the street.
4. The Paul hand-off does not conflate two speakers.
5. Verification TODOs are gone from notes 3 and 9.
6. Bizarro is split from Marlovits, and the Strawsonian position is offered a **complement**, not a
   refutation.
7. The relay answer (Macor via Małecka) and Tröhler's mosaic both appear in the body with concede-then-gap
   exits.
8. The platform section runs on **Uber**, not Amazon; addressability is severed from accountability; the
   survey is hedged in the body.
9. The co-optation analogy is not inverted: the city holds without co-opting, and co-optation is what
   platforms added.
10. The stipulation paragraph on "third" is present at the end of the Simmel section, and "third" does not
    slide between entity and condition after it.
11. "Two jobs and a third act" admits the door's third act.
12. "Baton-passing" is attributed as **Macor quoted in Małecka**, not as Małecka's coinage.
13. The Stone "movement of these films" phrasing is **not** quoted as Stone's prose.
14. Note 16 says Simmel's two examples recur at p. 321 in **altered** form, not verbatim.
15. The two hitchhikers stay split: the funeral lift is not the man awaiting the true call at Les Amis.
16. Note 26 keeps the disclaimer that the door's four acts are the chapter's reading, not Reich's scheme.
17. Steve is refused **on the stated ground that he is not on the list**, not "without a reason."
18. US English in the author's voice: *favorable*, *characterizes*, *organized*.
19. Note keys unique and sequential; no shared keys.
20. The camera, not "the cut," is the selector, and hand-offs inside single takes are not described as cuts.

---

## Load-bearing claims this panel should press (questions, not findings)

1. Simmel postponed a third that unifies from a distance, and the conflict-chapter return at p. 321 never
   restores the third *as a third*. Is that reading of *Soziologie* 103/321 defensible, and does
   Austin-holds-without-unifying still follow?
2. Royce's three conditions are cumulative, and a day of unclaimed strangers fails the acceptance
   condition. Is Gary a fair test case, or is the chapter testing a scene against a definition built for
   something else?
3. The club door instantiates Reich's grant, while the chapter concedes the four acts are its own reading.
   Does the scene still carry the diagnosis?
4. Reach (the city) and selection (the camera) are a division the film never lets the two swap. Does the
   film actually keep that split — including the middle stretch, the talker who singles out his listener,
   and the doorman?
5. "I argue that this refusal and the platform's withheld reason are the same gesture seen at forty years'
   distance" is the chapter's most attackable sentence. Does it survive?
6. Can the editors recognize the accepted abstract in this chapter?

## Standing author-only tasks — flag, never invent a fix, spend no effort

- Berg's daisy-chain definition, *Film Criticism* 31, pp. 24–26 (the chapter hedges via "standard digests").
- Whether *Slacker* appears in Bordwell's chapter filmography, pp. 245–250.
- The Criterion disc: whether the passenger witnesses the hit-and-run, and the final dialogue against the
  subtitle track. Note 2's subtitle disclosure covers the chapter until then.
- An optional page reference for the *Uberland* deactivation passage.
- The reply to the editors and the Bloomsbury AI-use policy.

The chapter's existing hedges are **correct and are not findings**: note 2 (subtitle debt), note 3
(witnessing awaits the disc), note 10 (Berg paraphrased from digests), note 26 (four acts are the
chapter's reading).
