# Phase 5 — verification against sources

209 assertions enumerated from `chapter/chapter_v4.md`, then checked. The regime was built
to break the failure this project already suffered: a research verdict recorded in the v3
outline travelled through four review panels unread, because every pass read the project's
own summary of a source rather than the source. So verifiers were given the chapter's
sentence and its citation and nothing else — no outline, no dossier, no gloss, no earlier
draft. Interpretive rows carried a stricter protocol still: state the source's own thesis
from retrieved text first, then compare.

Run 2026-08-10.

## What was checked

| type | rows |
|---|---|
| quotation | 73 |
| film | 58 |
| number | 37 |
| existence | 21 |
| interpretive | 20 |

Retrievability split 64 `agent`, 115 `author`, 29 `internal`. The `internal` rows — the
chapter's claims about its own census — were checked against the census files, which are
the only authority for them.

## Result

**Zero contradicted sources. Zero reversed theses. Zero fabricated quotations.** The
failure mode the whole regime was designed to catch did not occur in this draft.

Eleven corrections were applied. Each was minimal — a fact, a locator, or a hedge — and
the full gate re-ran after every one, because the review record shows fixes installing new
faults.

### The one that mattered most was not a citation error

Note 13 claimed the "Fired by an App" report's host pages "had gone dark by the time of
writing" and that a mirrored copy was read. A verifier retrieved the full 44-page PDF from
the publisher's own CDN and ran Wayback history on all three official URLs: 200
continuously, with only a 301 redirect chain following a 2024 organizational rebrand.
Nothing had gone dark. A referee who clicked the link would have found the claim false in
a second, and it was a claim about scholarly diligence rather than about the world.

### The rest

| finding | disposition |
|---|---|
| the chapter said the census records no deliberate handoff near the club door | it records one, at 29→30, which the chapter itself lists among its six — corrected, and the fix is sharper: the deliberate act there is a stranger's, not the doorman's |
| flat silence asserted across the last four transitions | the census refuses that claim about 34→35 ("Coding NONE here would report an observation I have not made") — now "none the transcript can show" |
| "Five equivocal seams" as a point estimate | the band is 4–5; the five listed are the union of the two codings, and the sentence now says so |
| Schegloff quoted from a 1972 reprint whose pages nobody could confirm | recited to the 1968 original, where both quotations sit verbatim at 1083 and 1086 |
| Meyer et al. coexistence finding attributed to the abstract | it is at 1733; the bibliography's contradicting "abstract consulted only" fixed with it |
| Amazon note claiming to quote a sentence "in full" | it stopped one sentence short — and the "engagement standards" phrase is verbatim on the page, so the removal capacity stands |
| "recently connected to the electrical grid" applied to all forty participants | the source says it of the twenty naive viewers only |
| schooling gap implied as established as the age gap | the age difference is significant (F(57,2) = 3.7, p = .03); the schooling difference is not (χ²(4) = 4.48, p = .3) |
| 30 percent given no reason | denominator is deactivated drivers, not all 810 surveyed |
| a missing "percent" on a falsifier statistic; an access date disagreeing with its own note | both fixed |

### The two foundations both hold

- **Schegloff.** Both quotations verbatim. And the load-bearing move — that the summons
  rule extends to co-present strangers — is *his own*, not the chapter's: he counts
  "'Pardon me,' when approaching a stranger" and a tap on the shoulder among summonses
  (1080), and the footnote to the "commits himself" sentence is about Joseph K. turning to
  face a priest who calls his name.
- **Simmel.** Wolff's translation is lending-locked everywhere, so the passage was checked
  against the 1908 German. He does set the third aside mid-thought and does promise a
  return: *"ist indes in späterem Zusammenhang zu behandeln"* — still to be treated, not
  dismissed.

## What could not be verified, and is now the author's

**A17 — Amazon's "invitation only" sentence.** This is the dated half of the closure pair
in §7, and the chapter prints it as a quotation from a page retrieved 1 August 2026. Three
independent attempts on 10 August could not re-retrieve it: two verifier agents (eight
direct fetches between them) and one pass here that followed the redirect onto the current
host. The live public pages carry no such wording, and the help topic appears to sit behind
a content-provider sign-in.

Nothing here shows the sentence is wrong. It shows nobody can currently check it. The
chapter now carries `[VERIFY:A17]` at that note, and the quotation needs a signed-in browser
session and a dated screenshot before publication. If it cannot be produced, §7's closure
claim rests on one half of its pair and should be reworded rather than printed.

**Tzioumakis's own hedge on the market-share figures.** Two verifiers independently hit an
Anubis anti-bot wall on the *Media Industries* journal across thirteen retrieval methods
between them. The trap is known and documented: the apparent collapse in market share is
substantially the author's own reclassification of firms between tiers, and he hedges it in
his text. Needs library access to confirm the hedge language.

**115 rows marked `author`.** Mostly film content, which the Criterion disc settles, plus a
few paywalled bodies. `v4/disc_worksheet.md` covers the film side.

## What the numbers survived

Every figure a referee would recompute from the published coder tables was rebuilt
independently from row-level codes rather than trusted from the merged file: both agreement
percentages (82, 91), both kappas (0.75, 0.84), the audible-link band, the equivocal band,
the six deliberate acts, the segment and transition counts, and the five substantiated
unfollowed plans. **All ten reproduce exactly.**
