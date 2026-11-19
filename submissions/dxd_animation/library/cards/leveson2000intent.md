---
key: leveson2000intent
apa: "Leveson, N. G. (2000). Intent specifications: An approach to building human-centered specifications. *IEEE Transactions on Software Engineering*, *26*(1), 15–35. https://doi.org/10.1109/32.825764"
authors: "Leveson, N. G."
year: 2000
title: "Intent specifications: an approach to building human-centered specifications"
venue: "IEEE Transactions on Software Engineering"
volume: "26"
issue: "1"
pages: "15–35"
doi: "10.1109/32.825764"
url: ""
type: article
facets: [G2]
claims: [m7]
role: contrast
load: exists
read_depth: abstract
object_read: "Crossref record (crossref.json; no abstract) and OpenAlex record with abstract inverted index (openalex.json), fetched 2026-11-11; ~/iit-playground/dxd_animation_local/pdfs/leveson2000intent/; sha256 of both in sha256.txt. The abstract quoted below was rebuilt by the lead from OpenAlex's inverted index (word order by position); it has not been checked against the article."
verified: corrected
verified_against: "crossref.json (no abstract) and openalex.json (abstract rebuilt from the inverted index by the verifier: 58 positions, none missing); GAP_CHECK_2.md; registry.tsv; sha256 of both records recomputed"
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Abstract card; the article was not read. Per the OpenAlex abstract, N. G. Leveson "examines and proposes an approach to writing software specifications, based on research in systems theory, cognitive psychology and human-machine interaction", whose goal "is to provide specifications that support human problem solving and the tasks that humans must perform in software development and evolution". She calls the resulting type of specification "intent specifications".

## What the paper uses it for

- **m7 (label contrast).** "Intent specification" already names a kind of engineering document in software engineering. The paper's "intent specification" names a person's competency in an algorithmically mediated coordination. The paper should say so in one sentence where it defines the competency. The abstract says nothing about what Leveson's specifications contain beyond supporting human problem solving; any claim that they record design rationale or "why" would need the article.

## Loci

None (abstract card).

## Caution

- The abstract is reconstructed from OpenAlex's inverted index, not read on the publisher's page.
- Crossref gives pp. 15–35; the gap check (`../GAP_CHECK_2.md`) cites the work without pages.
- Found by the run-2 gap check (label check).

## Verification

2026-11-11 · S6 verifier, batch C (Opus 5.5; not the writer) · verdict: corrected · checked: 0/0 loci (None, correct for an abstract card); frontmatter vs crossref.json (author "N.G. Leveson", 2000, title, IEEE Transactions on Software Engineering 26(1), pp. 15–35, IEEE, DOI); Crossref carries no abstract, as the card says; I rebuilt the abstract from OpenAlex's inverted index (58 word positions, none missing; OpenAlex W2105572062, 2000, same DOI and title), and all three quotations in What it argues match it word for word ("examines and proposes …", "is to provide specifications …", "intent specifications"); sha256 of crossref.json (dcd1c3…) and openalex.json (941ac6…) recomputed, both match sha256.txt; read_depth abstract honest; the Caution on GAP_CHECK_2 citing the work without pages confirmed (line 81) · changed: (1) What it argues, "Nancy Leveson" → "N. G. Leveson": Crossref gives only the initials, openalex.json carries no authorships, and no registry row or run file pairs "Nancy" with Leveson, so the given name was not seen this run (rule 1); (2) m7 bullet, "in software and safety engineering" → "in software engineering": the abstract and the venue support software specification, and no record held mentions safety engineering · for the lead: if the paper wants Leveson's full given name or the safety-engineering sense of intent specifications, it needs a record that shows it or the article itself; GAP_CHECK_2 row W8 names dblp and MIT OCW pages, but neither is held locally.

## Hand-check

- 2026-11-11, Claude (Opus 5.5, lead; S7). Verdict: **index**. Writer: the lead; check: S6 verifier, batch C (corrected: initials only; 'software engineering', not 'safety engineering'). Checked: the corrections against crossref.json and the rebuilt abstract. Changed: nothing further. For the author: the contrast sentence in the paper says 'a kind of software specification' and no more.
