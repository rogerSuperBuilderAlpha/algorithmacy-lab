---
key: creel2020transparency
apa: "Creel, K. A. (2020). Transparency in complex computational systems. *Philosophy of Science*, *87*(4), 568–589. https://doi.org/10.1086/709729"
authors: "Creel, Kathleen A."
year: 2020
title: "Transparency in Complex Computational Systems"
venue: "Philosophy of Science"
volume: "87"
issue: "4"
pages: "568–589"
doi: "10.1086/709729"
url: ""
type: article
facets: [F7]
claims: [c7]
role: contrast
load: load-bearing
read_depth: abstract
object_read: "No full text. Abstract and metadata from the Crossref record (crossref.json, sha256 3058bf4e3322973f9dae0a1e31e60a94248b718fb9c6253323dc174f34ae3e44) and OpenAlex W2991187744 (openalex.json, sha256 3287688d05d58555af67c94d5425c5e6b682170b9a7b83d720c5ddc8abe38656) at ~/iit-playground/pt_ai_animation_local/pdfs/creel2020transparency/, read 2026-11-08; the two records carry the same abstract text; no copy in pt_ai_animation_local/inbox/; no PDF, no sha256.txt (S4: FETCH_LOG.tsv records only the PhilPapers route, '200 non-pdf (892496 bytes); HTTP Error 403: Forbidden'; the Cambridge Core 403 is recorded in BROWSER_LIST.md, not FETCH_LOG.tsv)"
verified: corrected
verified_against: "crossref.json and openalex.json (sha256s recomputed); abstract text in both; FETCH_LOG.tsv; abstract card"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Creel (2020), Transparency in complex computational systems

## What it argues

Abstract card: everything below comes from the abstract in the Crossref and OpenAlex records, not
from the article. Kathleen A. Creel starts from the observation that scientists depend on complex
computational systems that are "often ineliminably opaque", which harms their ability to give
explanations and to detect artifacts. She rejects the answer some philosophers give, treating such
systems instrumentally, and sides with computer scientists who find that unsatisfying. In its place she
analyses transparency as having three forms: transparency of the algorithm, of its realization in code,
and of the way the code runs on particular hardware and data. Her aim is the transparency most useful
for a given task. Where full transparency is impossible, she offers partial transparency at one of the
three levels and so avoids instrumentalism.

## What the paper uses it for

- **c7** (necessary opacity: no frame holds the motion, no component the intelligence): contrast. Creel
  grants part of c7: she calls the systems "often ineliminably opaque". She would object to the paper's
  thesis in three precise ways, as far as the abstract shows.
  1. *Opacity is not one thing.* The paper treats opacity as a single, in-principle property of the AI.
     Creel splits transparency into algorithm, code and execution on hardware and data. On her account the
     question is always transparency *of what*, and an answer of "opaque" at one level does not settle the
     others.
  2. *Partial transparency is available.* c7 says no component holds the intelligence, and it leans on
     Roger's "in principle black box". Creel's conclusion is that partial transparency can be had "when
     full transparency is impossible", so in-principle opacity of the whole does not license giving up on
     understanding the parts.
  3. *Her third level is the paper's own territory.* The paper locates the AI in the LLM plus harnesses,
     VMs and efficiencies. Those are exactly the code and the "particular hardware and data" of Creel's
     second and third forms. If she is right, the system around the model is where transparency can be
     gained, which cuts against reading that system as the seat of necessary opacity. If the paper's
     life frame means treating the system as something to tend rather than to explain, she would also
     call that a form of the instrumentalism she rejects. That last point is my extrapolation from the
     abstract, not her claim.
  The paper can still use her against model-centrism: on her three-level account, transparency of the
  algorithm alone is not transparency of the working system. That use, too, rests only on the abstract.

## Loci

None. Only the abstract was read; abstract cards carry no loci. (The phrases quoted under "What it
argues" and "What the paper uses it for" come from the abstract in `crossref.json`, which carries JATS
markup; I matched them against the text inside the `<jats:p>` element.)

## Caution

- **Abstract only; on `BROWSER_LIST.md`** (row for `creel2020transparency`: https://doi.org/10.1086/709729,
  "blocked: Cambridge Core PDF returns 403 (bot block)"). DECISIONS expected full_text by the open
  Cambridge Core PDF. The run does not bypass bot blocks (README rule 8).
- **An open accepted version may exist.** OpenAlex lists a PhilSci-Archive copy marked "acceptedVersion"
  (https://philsci-archive.pitt.edu/16669/1/Creel_TransparencyInComplexComputationalSystems.pdf) and a
  PhilPapers copy marked "submittedVersion". FETCH_LOG shows S4 tried PhilPapers (403) but not
  PhilSci-Archive. I did not fetch it, because S5 writes from what S4 holds. If S4 or Roger retrieves the
  PhilSci-Archive copy, the card should be rewritten at full_text, with a Caution that an accepted
  manuscript's pages differ from *Philosophy of Science* pp. 568–589.
- **Dates.** Crossref gives issue date October 2020 and a published-online date of 2022-01-01, which
  postdates the issue; I cannot tell from the record why. OpenAlex gives 2020-04-30. The volume year is
  2020; DECISIONS lists no `registered_year`, and the card sets none. S8's DOI check may want to note the
  2022 online date.
- **Publisher.** Crossref names "Cambridge University Press (CUP)" as the publisher. The APA line gives
  no publisher, as APA does for journal articles.
- **What the paper may not claim from it:** any argument, example or page from the body, or that Creel
  discusses machine learning or LLMs specifically. The abstract speaks of "complex computational systems"
  used by scientists.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 1
- verdict: corrected
- checked: frontmatter against crossref.json and openalex.json (Creel, Kathleen A.; 2020; title; Philosophy of Science 87(4) 568-589; DOI; journal-article); sha256s recomputed and match; the phrases quoted in the body ("often ineliminably opaque", "when full transparency is impossible", "particular hardware and data", "complex computational systems") are in the abstract of both records; the Crossref online date 2022-01-01 against the October 2020 issue and OpenAlex's 2020-04-30 confirmed; OpenAlex PhilSci-Archive acceptedVersion and PhilPapers submittedVersion locations confirmed; Roger's "in principle black box" is in SOURCE.md; the c7 extrapolation is marked as the writer's own.
- changed: object_read credited both 403s to FETCH_LOG.tsv, but FETCH_LOG.tsv records only the PhilPapers route ("200 non-pdf (892496 bytes); HTTP Error 403: Forbidden"); the Cambridge Core 403 is recorded in BROWSER_LIST.md. The provenance now says so.

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (abstract card); the four phrases quoted from the abstract are verbatim in both crossref.json and openalex.json; frontmatter vs both records (Creel, Kathleen A.; Phil. Sci. 87(4) 568–589; DOI; 2020); both sha256s recomputed, match; Roger's "in principle black box" is SOURCE.md line 23; the c7 extrapolation is marked as the writer's.
- Changed: nothing.
- For the author: status is `cited` although SOURCE.md and SKETCH.md do not name Creel. The PhilSci-Archive accepted version OpenAlex lists would raise the card to full_text if you fetch it.
