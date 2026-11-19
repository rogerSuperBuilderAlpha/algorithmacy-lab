---
key: burtnyk1976interactive
apa: "Burtnyk, N., & Wein, M. (1976). Interactive skeleton techniques for enhancing motion dynamics in key frame animation. *Communications of the ACM, 19*(10), 564–569. https://doi.org/10.1145/360349.360357"
authors: "Burtnyk, N.; Wein, M."
year: 1976
title: "Interactive Skeleton Techniques for Enhancing Motion Dynamics in Key Frame Animation"
venue: "Communications of the ACM"
volume: "19"
issue: "10"
pages: "564–569"
doi: "10.1145/360349.360357"
url: ""
type: article
facets: [F4]
claims: [c6, c1]
role: support
load: load-bearing
read_depth: abstract
object_read: "Crossref record with abstract (crossref.json), at ~/iit-playground/pt_ai_animation_local/pdfs/burtnyk1976interactive/; original https://doi.org/10.1145/360349.360357; read 2026-11-08; sha256 32dbcc7fc0b1224dc424617874946367ef730ab3bcc48a2c4e004c74b7cc1880 (shasum -a 256). No full text: the ACM DL returned 403 (BROWSER_LIST.md); inbox checked, no copy."
verified: verified
verified_against: "crossref.json (abstract), sha256 recomputed; BROWSER_LIST.md; DECISIONS.md and F1-F4 triage"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Burtnyk & Wein (1976), Interactive skeleton techniques

## What it argues

Abstract card. The full text was not read. This is what the Crossref abstract says. Skeleton control, the
authors write, gives a "significant increase in the capability for controlling motion dynamics in key frame
animation". An animator builds a complex motion by animating a stick-figure version of an image, and that
control sequence then drives an image sequence through the same movement. The stick figure is simple, so
the design stage stays highly interactive. The method fits ordinary key-frame animation, so the animator can
apply it to only the parts of a composite image that need it.

## What the paper uses it for

- **c6** (animation is the craft of composing a living character from inert parts). Support, at abstract
  level. The abstract describes a layered way of making a figure move: one thing (the stick figure) is
  animated and another (the image) is driven by it. That is the rig in the sketch's table, "character model
  and rig". Whether the full text bears on "living" or only on motion is not shown. The SKETCH's reading of
  the rig is the paper's, since the abstract says nothing about character, life or personality.
- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies). Support, weak. The abstract's point
  that skeleton control applies "selectively" to the components of a composite image that need it matches the
  paper's picture of a system of layers around a core. The mapping "rig = model weights" is the paper's and
  comes from the SKETCH's §3 table. The abstract gives no support for it and may cut against it, since the
  skeleton drives the image and the weights are not a simpler stand-in for the system.

## Loci

None.

## Caution

- **Browser list.** No text was available. The work is on BROWSER_LIST.md (ACM DL refused the automated
  fetch with 403). The card should be raised to full text when a copy lands in `inbox/`.
- **Record.** Crossref gives authors with initials only (N. Burtnyk, M. Wein, National Research Council of
  Canada), October 1976, volume 19, issue 10, pages 564–569. No OpenAlex record is in the folder.
- **Earlier work.** The authors have an earlier paper (1971, key-frame animation), listed in reserve in the
  F4 triage. This card does not stand in for it.
- **What the paper may not claim from it:** any quotation, any page-level claim, or that the authors treat
  a skeleton as a character.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W2 group 4
- verdict: verified. An honest abstract card: frontmatter matches Crossref, the summary keeps to the Crossref abstract, Loci None, and the c6 and c1 uses are flagged as at abstract level and weak.
- checked: crossref.json (Burtnyk, N.; Wein, M.; NRC Canada affiliation; CACM 19(10), 564–569, Oct 1976; journal-article; DOI; abstract text); sha256 of crossref.json matches the card; BROWSER_LIST.md row (ACM DL 403); no PDF in the folder; inbox has no copy; burtnyk1971computer in reserve per F1-F4 triage; SKETCH §3 table row 'Character model and rig | Model weights' confirmed.
- changed: nothing

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 0/0 (abstract card, Loci None); summary checked against the Crossref JATS abstract; frontmatter vs crossref.json (N. Burtnyk, M. Wein; CACM 19(10), 564–569, Oct 1976; DOI); sha256 recomputed, matches; inbox empty.
- Changed: nothing
- For the author: the 'rig = weights' mapping is the sketch's, not the abstract's, as the card says; status 'cited' though SOURCE.md and SKETCH.md do not name Burtnyk & Wein, while catmull1978problems on the same footing is 'candidate' (status note in part1.md).
