# What only the author can close

State of `chapter_v3.md` on 9 August 2026, after auditing every panel-3 finding against the current
text rather than against the task ledger.

**The headline: panel 3's accepted list is already applied.** The commits after 2 August — `57aba94`,
`21c1502` and their neighbours — closed it, and the README ledger was never updated to say so. Every
item in §3A–E and the ban residue was checked individually against the file. See
[`PANEL3_STATUS.md`](PANEL3_STATUS.md) for the item-by-item audit.

What remains is five things, and four of them need you.

---

## 1. The Criterion disc — T1

The largest single unblock, and unchanged since panel 2. One afternoon with the disc and a notepad.

| what to settle | what it unblocks |
|---|---|
| Classify the handoffs, roughly 36 of them | "about three dozen times" in §1; "almost none meet another twice" |
| The moon-landing walk: does the captive answer? | B2. The subtitle file shows "Mm-mmm," "Yeah," "Yeah, that's my birthday," and an exit attempt, so "unbroken monologue" was already removed — the disc confirms or reopens it |
| The pap-smear recognition beat | whether the woman is recognised or only heard out |
| The on-screen oblique-strategies card | the §1 Rosenbaum reading |
| Shot-level handoff confirmation | any claim in §4 about how a handoff is cut |

Panel 3's standing instruction while this is open: **do not invent shot claims.** Nothing in the
current text does.

## 2. Rivera, Soderstrom and Uzzi (2010), end to end — T2

The one live source debt. §2 currently says:

> Rivera, Soderstrom, and Uzzi already put proximity and brokerage on one map, but they ask why ties
> form. This chapter asks what the third knows and chooses. Three field-defining reviews never cite
> the other tradition.[^20a]

That is already scoped to the three documents in note 20a, so the universal negative panel 3 objected
to is gone. Reading the Rivera body either upgrades the claim or confirms the scoping is right. It is
not blocking submission.

**Feld 1981 p. 1016 is closed** — note 18 now quotes the definition from the page directly. Drop it
from any older list you are working from.

## 3. Moretti p. 3 — T4

Confirm the two retained phrases. Note 44 already hedges, so this raises confidence rather than
unblocking anything.

## 4. Send `editor_query.md` — T6

Drafted and unsent. Agents do not contact editors here, so this one is yours and it gates the rest:

- **The ceiling.** Body is **5,092 words** against a stated 5,000. The overage is 92 words, under two
  per cent. Ask whether that stands or whether you cut.
- Exact collection title, editor, deadline.
- Citation style — the chapter is Chicago notes-bibliography, 78 notes, three-part bibliography.
- Terminology: whether "attentional selector" and "transactional selector" survive house edit.

## 5. Two Criterion access dates to confirm

I added `Accessed August 2, 2026` to the Pierson and Rosenbaum reprints, matching the sibling
Criterion entry from the same research pass. **I could not verify either** — Criterion returns 403 to
scripted and agent fetches alike. Thirty seconds in a browser confirms or corrects them.

The other two URLs I did verify myself, resolving HTTP 200 on 9 August: Althouse and the *Austin
Chronicle*.

---

## What I closed this round

- **Apparatus reconciled both directions, mechanically.** 78 note keys used, 78 defined, no gaps, no
  duplicates, no orphan bibliography entries, no surviving placeholders. `check_apparatus.py` runs
  this in a second and has a negative control proving it fires.
- **Four live URLs given access dates** — the last of panel 3's D2.
- **A harness bug the chapter exposed.** The prose tool counted footnote definitions as body and read
  7,993 words where the true body is 5,092 — a 57% overcount on any Chicago notes chapter.

## What I could not do

**The `slacker` register is still uncalibrated.** DOAB holds metadata only; OAPEN has plenty of
open-access film PDFs but they are industry economics, historiography and festival studies, not
single-film critical essays. Building a floor from those would produce confident nonsense, which is
the failure mode the harness exists to prevent. The attempt and the queries tried are recorded in
`~/.claude/skills/draft/registers/slacker/manifest.json` so the next attempt starts somewhere new.

Until then the prose tool reports locators and raw rates for this chapter and issues no verdict. On
the raw rates it is clean: five lexical rules match at all across 5,092 words, and reading the hits,
two of those five are quoted dialogue and a case citation number.
