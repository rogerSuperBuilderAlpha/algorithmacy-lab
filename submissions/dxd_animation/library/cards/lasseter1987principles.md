---
key: lasseter1987principles
apa: "Lasseter, J. (1987). Principles of traditional animation applied to 3D computer animation. In *Proceedings of the 14th Annual Conference on Computer Graphics and Interactive Techniques* (pp. 35–44). ACM. https://doi.org/10.1145/37401.37407"
authors: "Lasseter, John"
year: 1987
title: "Principles of traditional animation applied to 3D computer animation"
venue: "SIGGRAPH '87"
volume: ""
issue: ""
pages: "35–44"
doi: "10.1145/37401.37407"
url: ""
type: proceedings
facets: [F1, F9]
claims: [c8]
role: method
load: load-bearing
read_depth: abstract
object_read: "Crossref record (crossref.json, sha256 d8e00182ecf4856d546afe46df5d84c19aa8101fb1e800ff39167c240ca8f58d, no abstract) and OpenAlex W2121378366 record with abstract (openalex.json, sha256 cee58df7217bc65f7964f70202055d8966dd85616bb8110b4be3d9d6b45c0b9d); local folder ~/iit-playground/dxd_animation_local/pdfs/lasseter1987principles/; original URL https://doi.org/10.1145/37401.37407; 2026-11-05. No full text: FETCH_LOG.tsv records HTTP 403."
verified: verified
verified_against: "crossref.json + openalex.json W2121378366 (sha256 recomputed); prior dxd_animator card; triage DECISIONS and F1-F2 row 75"
prior_cards: [lasseter1987principles (dxd_animator)]
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues
Abstract card. The full text was not read.

The OpenAlex abstract says the paper "describes the basic principles of traditional 2D hand drawn animation and their application to 3D computer animation". After describing how these principles evolved, it details each one, "addressing their meanings in 2D hand drawn animation and their application to 3D computer animation". It aims to "demonstrate the importance of these principles to quality 3D computer animation". The abstract names no individual principle.

## What the paper uses it for
- c8 (method). The paper says DXD should apply the animator's methods. Lasseter is the bridge from hand-drawn craft to a computing medium, the best-placed source for a toolkit of animator's principles. Which principles, and whether any carry over from a drawn character to an interface, is not shown by the abstract. Lasseter writes about animating 3D characters, not interface design, so the move to DXD is the paper's.

## Loci
None.

## Caution
- Upgrade of the dxd_animator abstract-only card (not edited). That card gave the DOI 10.1145/37402.37407, the *ACM SIGGRAPH Computer Graphics* 21(4) record, and cited it as 21(4), 35-44. This card uses 10.1145/37401.37407, the SIGGRAPH '87 proceedings record, which is the one in the records read (Crossref and OpenAlex W2121378366). The triage file says 37402.37407 is a second Crossref record of the same paper, OpenAlex W2999276620, closed; that was not opened here. Both are said to give pp. 35–44, which both the records read here do for 37401.
- The prior card also listed individual principles (squash and stretch, timing, anticipation, staging, follow-through, overlapping action, slow in and out, arcs, exaggeration, secondary action, appeal) and two "key claims", plus a Crossref citation count of 272. None of that appears in the records read this session, so it is not carried over; it stays unchecked until the text is read.
- The Crossref record gives the container title "Proceedings of the 14th annual conference on Computer graphics and interactive techniques", issued 1987-08, publisher ACM.
- Neither SOURCE.md nor OUTLINE.md cites the work, so status is candidate.

## Verification
2026-11-05 · S6 verifier, batch b11 (opus; not the writer) · verdict: verified · checked: loci 0/0; author, 1987, title, proceedings container, pp. 35–44, DOI 37401.37407 match both records; abstract quotations match OpenAlex; prior card's 37402 DOI, 21(4), principle list and count 272 confirmed as described; depth abstract honest · changed: nothing
