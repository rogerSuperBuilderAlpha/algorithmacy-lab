# What the v4 rebuild is assuming

Four facts about the venue are unknown, and the rebuild proceeds without them on the
author's instruction. Everything the chapter does that depends on a guess is listed here,
with what changes if the guess is wrong. When the editor replies, this file is the
worklist.

Opened 2026-08-10, at the start of the rebuild.

---

## A1 — The word ceiling is 5,000 words of body text

**Status: assumed.** The call for the collection says 3,000–5,000 words. Nobody has
confirmed whether 5,000 is firm, whether it counts notes, or whether the collection has
ever run longer chapters. v3 sits at 5,092, which is 92 words over a ceiling that has
never been tested.

**What depends on it.** The whole v4 outline is budgeted to 5,000 and drafted at that
figure rather than drafted long and compressed. That choice is deliberate: the last
compression "took words out of the film and left the sociology whole," so v4 has no
compression phase to lose the film in. But it also means the section budgets are
load-bearing. A ceiling of 4,000 would not be a trim; it would be a different chapter,
and the outline would have to be rebuilt before drafting.

**If it is wrong.** 5,500 or above: the ranked restoration list in
`chapter/v3_cut_ledger.md` still applies, and the first thing to buy back is Benjamin's
assembly-line passage — the largest single loss in the v3 compression and the one place
the argument conceded that a platform power has a cinematic ancestor. 4,000 or below:
return to Phase 2 and rebudget.

## A2 — Chicago notes-bibliography is the citation style

**Status: assumed.** Film studies defaults to Chicago or MLA, and the project's lab style
(APA) is certainly wrong here. v3 carries 78 notes and an 80-entry bibliography in Chicago
notes-bibliography.

**What depends on it.** The apparatus, and `check_apparatus.py`, which reconciles notes
against bibliography in both directions. Conversion to author-date is mechanical and the
script would need a matching rewrite, but it is a day's work done twice if the answer
arrives late.

## A3 — No shot-level claim, because nobody has watched the disc

**Status: a hard rule, not a guess.** In five drafts across this project, the chapter has
never described a shot. The August editor named this the finding he cared about most: "In
5,400 words it never says what the camera looks like doing it… A 1990 newspaper critic did
the looking, and the 2026 chapter quotes him doing it."

**What v4 does about it.** `v4/disc_worksheet.md` lists every question one afternoon with
the Criterion disc would settle, each with both answers pre-written, so viewing notes drop
into the draft without a redraft. Until that afternoon happens, the draft carries
`[DISC:row-id]` markers wherever a claim would need it, and `v4/tools/run_gate.py` counts
them. **Nothing in this category may be guessed, inferred from subtitles, or written
around with a hedge.** The transcript is subtitle-derived and the project rule is that it
is a pointer to the disc, not a source.

**What is blocked until then.** The count and classification of the film's handoffs;
whether the moon-landing captive answers; whether the pap-smear pitch is cold or follows
an introduction; the on-screen wording of the oblique-strategies card; the format of the
finale camera; whether the opening relay is cut or continuous; and the audio wording of
every quotation the chapter draws from dialogue.

## A4 — The collection's title, editor of record, and deadline are unknown

**Status: unknown, and nothing in the pipeline can find out.** `editor_query.md` has been
drafted since 2 August and unsent. Its numbers are stale — it says 5,180 words and 77
notes against v3's actual 5,092 and 78 — and its item 4 describes a terminology change
that Phase 1 may supersede.

**What depends on it.** Nothing in the argument. Everything in the scheduling.

## A5 — The abstract's terminology may not survive

**Status: open by design.** The accepted abstract distinguishes a **hosting** third from an
**engineering** third. v3 renamed these **setting** and **selector**, and the rebuild has
re-opened even that, so v4 may land on a third vocabulary. Whatever Phase 1 chooses, the
editor should hear it from the author rather than discover it.

**The constraint.** The abstract's *commitments* are contractual even where its words are
not: Simmel's third, the Austin/camera contrast, the Uber parallel, the training claim, and
the closing questions about what makes a coordinating third contestable. A new frame may
rename them. It may not quietly drop one.

---

## Sources whose status cannot be raised by any agent

These sit in provenance class D. They are not defects in the rebuild; they are the residue
that needs a person, and they were already known before it started.

- **Rivera, Soderstrom & Uzzi (2010), read end to end.** The one live source debt. The v3
  novelty claim was printed against it unread, a panel opened it, and the claim was false as
  printed. It is now scoped rather than universal, and reading the body either upgrades the
  scoping or confirms it.
- **Moretti, p. 3** — confirm the two retained phrases. The note already hedges.
- **Two Criterion access dates** (the Pierson and Rosenbaum reprints). Criterion returns 403
  to scripted fetches; thirty seconds in a browser settles both.
- **The Criterion disc**, per A3.
