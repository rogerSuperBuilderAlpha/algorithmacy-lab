---
key: hooks2023acting
apa: "Hooks, E. (2023). *Acting for animators* (5th ed.). Routledge. https://doi.org/10.4324/9781003289753"
authors: "Hooks, Ed"
year: 2023
title: "Acting for Animators"
venue: "Routledge (London)"
volume: ""
issue: ""
pages: ""
doi: "10.4324/9781003289753"
url: ""
type: book
facets: [F4]
claims: [c6, c1]
role: support
load: exists
read_depth: abstract
object_read: "No copy of the book. Records only: Crossref work record for 10.4324/9781003289753 at ~/iit-playground/pt_ai_animation_local/pdfs/hooks2023acting/crossref.json (no abstract; sha256 8b5e50fba0f9cf00daddc8601985ed23a5c55833d7b46460f118760d61e00072); and, fetched 2026-11-08 into the session scratchpad, the OpenAlex record W594927527, which carries the abstract (sha256 f4aed1c762e4c733c3ded34a8f5fa34af9d5b0345519e81c4ea994fde4a1fc24), and the Crossref chapter record 10.4324/9781003289753-4 (sha256 31e861c54eab8a4d29fae99e7d49ebb284af8d64be9d4539c4f94361d920c36f); read 2026-11-08"
verified: verified
verified_against: "crossref.json (local); OpenAlex W594927527 abstract; Crossref chapter 10.4324/9781003289753-4; all three sha256 matching; Loci None"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# Hooks (2023), Acting for animators (5th ed.)

## What it argues

This is an abstract card; I read no text of the book. The abstract is the one on the OpenAlex record, and it
reads as the publisher's description of the fifth edition. Crossref gives Ed Hooks as author, Routledge, London,
edition number 5, published online 2023-05-24.

According to the abstract, Ed Hooks writes an acting guide for animation professionals rather than for stage
and film actors. He applies classical acting theory, from Aristotle to Stanislavsky, to animation. He covers
scene structure, character development and the links between thinking, emotion and physical action. He holds
that the theory applies to any character animation, whatever the technique (stop-motion, 2D, 3D or a blend),
because the audience is the same. The fifth edition adds scene-by-scene acting analyses of four animated
features (*Flee*, *Soul*, *Porco Rosso*, *The Triplets of Belleville*), and a revised "Classroom Notes"
section. That section covers experimental animation, a short history of actor training, and guidance on motion
and performance capture.

The Crossref chapter record adds one fact. The book has a chapter titled "Acting and the CG pipeline", pp.
19–20 (10.4324/9781003289753-4). I did not see its text.

## What the paper uses it for

- **c6** (animation is the craft of composing a living character from inert parts): Hooks supports the claim
  that the animator *performs* the character. On his account, the animator brings it to life by acting through
  it. That is a narrower sense of craft than c6's composition from parts. Hooks's frame is the actor's, so
  using him for composition stretches the abstract. The abstract does support c6's claim that the craft is
  the same across techniques.
- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the only link is the two-page chapter
  title "Acting and the CG pipeline". It puts performance and production pipeline in one place, which is why
  triage chose the book. What Hooks says there is unread. Citing him for c1 now would rest on a chapter
  title, and that is a stretch. The abstract's mention of motion and performance capture also bears on c10
  (§5). The card does not tag c10, because DECISIONS assigns only c6 and c1.

## Loci

None

## Caution

- **Record correction applied (DECISIONS, "Record corrections S5 must apply").** The work is the 2023 fifth
  edition, 10.4324/9781003289753, not the 2017 DOI that FACETS gives (10.4324/9781315618272, per triage
  F1-F4.md). I did not see the 2017 record this run.
- **OpenAlex dates the same DOI 2013.** W594927527 gives publication_year 2013 (2013-03-01), but its abstract
  describes the fifth edition, and Crossref gives 2023-05-24. The OpenAlex record looks as if it merges an
  earlier edition with this one. I kept 2023 from Crossref, the DOI registrant, and set no `registered_year`.
  S8 should check this before building the reference list.
- **Chapter pages.** The chapter's pp. 19–20 come from the Crossref chapter record. Whether those are print pages
  or e-book pages, the record does not say.
- **The abstract is the publisher's description, not Hooks's own words.** Anything quoted from it should be
  attributed to the abstract, not to Hooks.
- **Not read.** The book is on `BROWSER_LIST.md` (row for `hooks2023acting`; the pipeline chapter first). The
  OpenAlex and chapter records sit only in the session scratchpad. S4 should save them in the key folder.
- **Status.** The sketch does not name Hooks, so the status is candidate.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W2 group 3
- verdict: verified, no changes
- checked: frontmatter (Hooks, Ed; 2023; Routledge, London; ed. 5; monograph; DOI) against crossref.json; chapter title and pp. 19-20 against the chapter record; OpenAlex year 2013 vs Crossref 2023 (registered_year correctly unset, since the registrant record gives 2023); every sentence of "What it argues" against the reconstructed OpenAlex abstract; FACETS DOI 10.4324/9781315618272 and the DECISIONS correction; sha256 of all three records
- changed: nothing
