---
key: lasseter1987principles
apa: "Lasseter, J. (1987). Principles of traditional animation applied to 3D computer animation. In *Proceedings of the 14th Annual Conference on Computer Graphics and Interactive Techniques* (pp. 35–44). ACM. https://doi.org/10.1145/37401.37407"
authors: "Lasseter, John"
year: 1987
title: "Principles of Traditional Animation Applied to 3D Computer Animation"
venue: "SIGGRAPH '87"
volume: ""
issue: ""
pages: "35–44"
doi: "10.1145/37401.37407"
url: ""
type: proceedings
facets: [F4]
claims: [c6]
role: anchor
load: load-bearing
read_depth: abstract
object_read: "OpenAlex record W2121378366 with abstract (openalex.json) and Crossref record without abstract (crossref.json), at ~/iit-playground/pt_ai_animation_local/pdfs/lasseter1987principles/ (copied from dxd_animation_local per provenance.txt); original https://doi.org/10.1145/37401.37407; read 2026-11-08; sha256 openalex.json cee58df7217bc65f7964f70202055d8966dd85616bb8110b4be3d9d6b45c0b9d, crossref.json d8e00182ecf4856d546afe46df5d84c19aa8101fb1e800ff39167c240ca8f58d (shasum -a 256; both match the dxda card). No full text; inbox checked, no copy."
verified: verified
verified_against: "crossref.json 10.1145/37401.37407 and openalex.json W2121378366 (abstract), sha256 recomputed; provenance.txt; dxda card frontmatter; BROWSER_LIST.md; DECISIONS.md row; SKETCH.md §3"
prior_cards: [lasseter1987principles (dxda, abstract), lasseter1987principles (dxdanimator, said to be partial by the F1-F4 triage; not opened)]
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Lasseter (1987), Principles of traditional animation applied to 3D computer animation

## What it argues

Abstract card. The full text was not read. The OpenAlex abstract says John Lasseter's paper "describes the
basic principles of traditional 2D hand drawn animation and their application to 3D computer animation". It
first describes how these principles evolved, then details each one, "addressing their meanings in 2D hand
drawn animation and their application to 3D computer animation". Its stated aim is to show the importance of
the principles to quality 3D computer animation. The abstract names no individual principle. Crossref
places Lasseter at Pixar, San Rafael.

## What the paper uses it for

- **c6** (animation is the craft of composing a living character from inert parts). Anchor, at abstract
  level. The SKETCH §3 anchors the production-craft section in Thomas and Johnston (1981) and Lasseter
  (1987). The abstract shows what Lasseter does: he carries a body of hand-drawn craft principles into a
  computing medium. That fits a claim that the craft survives a change of medium. The abstract does not say
  which principles, nor that they compose a "living" character from "inert" parts, so the claim that the
  principles are about life rather than motion polish is not shown here. Lasseter writes about animating 3D
  characters, not about AI or software systems, so the carry-over to AI development is the paper's own.

## Loci

None.

## Caution

- **Browser list.** No text was available. The work is on BROWSER_LIST.md (the ACM DL refuses automated
  fetches). The F1-F4 triage had expected full text from the open bronze ACM PDF; the fetch did not obtain
  it. A copy in `inbox/` would raise the card to full text and allow Loci.
- **Upgrade, not a new card.** This is the planned upgrade of the dxda abstract card (not edited). The dxda
  card used the same DOI and the same abstract, with the claim c8 for the DXD paper. This card changes the
  use to c6 for a different paper. The dxdanimator card is described by the triage as partial and uses the
  other DOI. I did not open it, so I take nothing from it.
- **Two DOIs.** The Crossref record read here (10.1145/37401.37407) is the SIGGRAPH '87 proceedings record,
  with the OpenAlex id W2121378366 (reported open, bronze). The triage file says a second record,
  10.1145/37402.37407 (*Computer Graphics* 21(4), W2999276620, closed), covers the same pages and that the
  dxdanimator card uses it. I did not open that record. The reference list should pick one DOI; this card
  follows the proceedings one, and the proceedings volume has no volume or issue number in Crossref.
- **Abstract source.** The abstract came from OpenAlex, not Crossref (which has none).
- **What the paper may not claim from it:** any quotation, any named principle (squash and stretch and the
  rest), or page-level claim, until the text is read.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W2 group 4
- verdict: verified. An honest abstract card: frontmatter matches the proceedings record, the summary keeps to the OpenAlex abstract, Loci None, and the c6 use is flagged as abstract-level.
- checked: crossref.json (Lasseter, John; Pixar, San Rafael affiliation; title; Proceedings of the 14th annual conference on Computer graphics and interactive techniques; SIGGRAPH '87 event; pp. 35–44; Aug 1987; proceedings-article; ACM; no abstract); openalex.json (conference-paper, bronze OA URL at dl.acm.org, abstract read in full); both sha256 match the card and the dxda card's object_read; dxda card uses the same DOI and claims [c8]; provenance.txt; BROWSER_LIST.md row; DECISIONS.md row naming both DOIs; SKETCH §3 anchors Thomas & Johnston (1981) and Lasseter (1987). The second DOI 10.1145/37402.37407 was not opened by me either.
- changed: nothing

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: Loci = None (abstract card); the three phrases quoted in 'What it argues' match the OpenAlex abstract; 'Pixar, San Rafael' is in crossref.json; frontmatter against crossref.json (John Lasseter; Proceedings of the 14th annual conference on Computer graphics and interactive techniques, SIGGRAPH '87; pp. 35–44; 1987-08; ACM; DOI 10.1145/37401.37407); both sha256 values recomputed, match; provenance.txt names the dxd_animation_local copy; status cited: SKETCH §3 names Lasseter (1987). The c6 bullet names its stretch (abstract names no principle; nothing about life or AI).
- Changed: nothing.
- For the author: the ACM DL copy is bronze open access per OpenAlex; opening it in a browser would raise this anchor to full text.
