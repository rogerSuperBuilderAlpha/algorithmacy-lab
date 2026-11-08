---
key: schaeffer2023are
apa: "Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? In *Advances in Neural Information Processing Systems 36* (pp. 55565–55581). Neural Information Processing Systems Foundation. https://doi.org/10.52202/075280-2425"
authors: "Schaeffer, Rylan; Miranda, Brando; Koyejo, Sanmi"
year: 2023
title: "Are Emergent Abilities of Large Language Models a Mirage?"
venue: "NeurIPS 36"
volume: ""
issue: ""
pages: "55565–55581"
doi: "10.52202/075280-2425"
url: ""
type: proceedings
facets: [F8]
claims: [c2]
role: contrast
load: exists
read_depth: partial
object_read: "arXiv v2 (arXiv:2304.15004v2 [cs.AI], 22 May 2023; first page: 'Preprint. Under review.'; 14 pp.), an author preprint, NOT the NeurIPS proceedings text; and its text layer schaeffer2023are.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/schaeffer2023are/; fetched from https://arxiv.org/pdf/2304.15004 (FETCH_LOG.tsv, route arxiv_preprint); no copy in inbox/; read 2026-11-08; sha256 e3ecd65d314d8383d6e696abc9fa7a3fd58f79bf4e54e5f5bb0e46dd15faefc5 (PDF, from sha256.txt). Parts read in full: PDF pp. 1–6 (abstract, §1–§3, start of §4), 8–9 (§6 related work, §7 discussion). Parts skimmed: pp. 6–8 (the BIG-Bench meta-analysis tables and the vision experiments of §5). Parts not read: the reference list and Appendix A (derivations of metric behaviour), pp. 10–14."
verified: verified
verified_against: "crossref.json; sha256 re-hashed; per-page pdftotext of the arXiv v2 PDF, 8 quotations traced (all verbatim, page and section locators correct)"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# R. Schaeffer, B. Miranda and S. Koyejo (2023), Are emergent abilities of large language models a mirage?

## What it argues

Schaeffer, Miranda and Koyejo challenge the claim that large language models show "emergent abilities",
meaning abilities that appear sharply and unpredictably once a model passes some scale. They propose that
the sharpness comes from the researcher's metric. Suppose a model's per-token error falls smoothly with
scale. A metric that demands every token of an answer be right (exact string match) or that scores each
answer in steps (multiple-choice grade) then turns that smooth curve into a jump. A linear or continuous
metric on the same outputs (token edit distance, Brier score) shows smooth, predictable gains (§2).

They test the account three ways. First, on InstructGPT/GPT-3 arithmetic tasks, they hold the model outputs
fixed, change the metric, and watch the apparent emergence vanish; they also add test data and find that
small models score above chance (§3). Second, they meta-analyse BIG-Bench and find that more than 92 percent
of claimed emergent abilities appear under just two metrics, multiple choice grade and exact string match,
and that switching metric on LaMDA outputs removes the effect (§4). Third, they induce "emergent" abilities in
autoencoders and Omniglot classifiers by choosing discontinuous metrics (§5). The authors stop short of
denying emergence in general: nothing in the paper should be read as claiming that LLMs cannot show
emergent abilities, only that the previously claimed ones may be metric artefacts (§7). They also press
for model outputs to be made public.

## What the paper uses it for

- **c2** (model-centrism misplaces where the intelligence sits): the use is indirect, and the card is a
  contrast source for two reasons. (1) The paper may cite Schaeffer et al. for a narrow point that supports
  c2: whether a capability appears "in" a model at some scale depends on the measuring apparatus the
  researcher chooses, so even the model-centric story about where an ability sits is partly an artefact
  of the evaluation harness. That is a harness-shaped finding, close to c1's point that the surrounding
  apparatus counts. (2) Schaeffer et al. would object if the paper used their result as an argument against
  the model's capabilities, or used "emergence" as an explanation of the composed system. Their unit of
  analysis is a single model family's outputs against scale ("when analyzing fixed model outputs", p. 1);
  they say nothing about harnesses, tools or memory, and their own frame stays inside the model. They
  treat the capabilities as real and graded, they decline to say emergence cannot occur, and they would
  reject any move that reads "emergence" as an explanation not backed by a metric-controlled test. If the
  paper needs "intelligence emerges from the system", this source is a caution against the word, not a
  support.
  Stretch: the source reaches c2 only through its own critique of Wei et al., which the library does not
  hold. The distance from c2 is two steps (DECISIONS).

## Loci

Matched against schaeffer2023are.txt (arXiv v2 PDF text layer). Page numbers are the arXiv PDF's (14 pages),
not the NeurIPS pagination 55565–55581. Inner quotation marks are single quotes.

- p. 1, Abstract: "emergent abilities appear due the researcher’s choice of metric rather than due to fundamental changes in model behavior with scale."
- p. 2, §1: "In this paper, we call into question the claim that LLMs possess emergent abilities, by which we specifically mean sharp and unpredictable changes in model outputs as a function of model scale on specific tasks."
- p. 2, §1: "Our doubt stems from the observation that emergent abilities seem to appear only under metrics that nonlinearly or discontinuously scale any model’s per-token error rate."
- p. 3, §2: "the researcher’s choice of a nonlinear or discontinuous metric can distort the model family’s performance to appear sharp and unpredictable."
- p. 4, fn. 1: "While the independence assumption is not true, the approximation yields results qualitatively matching the observed emergence claims."
- p. 9, §7: "emergent abilities may be creations of the researcher’s choices, not a fundamental property of the model family on the specific task."
- p. 9, §7: "nothing in this paper should be interpreted as claiming that large language models cannot display emergent abilities"
- p. 9, §7: "scientific progress can be hampered when models and their outputs are not made public for independent scientific investigation."

## Caution

- **Version.** The copy is an arXiv v2 preprint stamped "Preprint. Under review." The record gives the
  NeurIPS 36 proceedings, pp. 55565–55581, with DOI prefix 10.52202; the publisher in Crossref is "Neural
  Information Processing Systems Foundation, Inc. (NeurIPS)". The page range comes from Crossref only. A
  verifier should check that the proceedings text matches the preprint wording.
- **Status.** DECISIONS marks this card for reserve if the Sculley slot is taken (a ceiling of 75 cards).
  No copy is in inbox/, so Sculley is not promoted at this writing. The card is written because the
  assignment lists the key, and it carries claim c2, so `status` is `cited`. S8 should recheck.
- **Date.** Volume year 2023, no `registered_year`; Crossref has 2023 only.
- **Scope.** Schaeffer et al. test one claim about scale and metrics. Their experiments concern GPT-family
  arithmetic, BIG-Bench and small vision models. They do not study dialogue systems, harnesses or any
  composed system.
- **Skimmed and not read.** §5 and the BIG-Bench tables (skimmed); Appendix A and the reference list (not read). The
  "more than 92 percent" figure is in §1 (p. 2) and §4 (p. 6); I did not check it against the BIG-Bench data.
- **What the paper may not claim from it:** that LLMs lack emergent abilities; that capabilities
  belong to the system rather than the model; any claim about harnesses.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 4
- verdict: verified
- checked: frontmatter against crossref.json (Rylan Schaeffer, Brando Miranda, Sanmi Koyejo; title;
  *Advances in Neural Information Processing Systems 36*, pp. 55565–55581, issued 2023; DOI
  10.52202/075280-2425; proceedings-article; publisher as the Caution gives it). No openalex.json in the
  folder, so Crossref is the only record, as the card says. sha256 of the PDF matches sha256.txt; all 8
  quotations found verbatim on the stated pages, and the section locators match the printed headings (§1
  p. 1, §2 p. 3, §4 p. 6, §6 p. 8, §7 p. 9). Body claims traced: InstructGPT/GPT-3 arithmetic and the
  above-chance result with more test data (p. 5), "92%" (pp. 2, 6–7), LaMDA (pp. 6–7), token edit
  distance and Brier score, autoencoders and Omniglot (pp. 7–8), "fixed model outputs" (p. 1).
  read_depth partial lists the parts read. No Sculley copy in inbox/, so the status note holds. The c2
  stretch (two steps, via Wei et al.) is named.
- changed: nothing

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index after fix** (fixed here).
- Checked: 8/8 loci found in schaeffer2023are.txt, each on the stated PDF page (1, 2, 2, 3, 4, 9, 9, 9); frontmatter against crossref.json (Schaeffer, Miranda, Koyejo; *Advances in Neural Information Processing Systems 36*, pp. 55565–55581; 2023; DOI 10.52202/075280-2425; the only record in the folder); PDF sha256 recomputed, matches sha256.txt; 14 pages; the p. 1 stamp reads 'arXiv:2304.15004v2 [cs.AI] 22 May 2023'. read_depth partial lists what was read, skimmed and not read. The c2 bullet names the two-step stretch via Wei et al.
- Changed: status cited → candidate [Corrected by Fable, S7]. The card set 'cited' because it carries claim c2; README defines cited as a work SOURCE.md or SKETCH.md uses, and neither names Schaeffer et al. Checkpoint B ruling 5 names the key only as the card Sculley would displace. Role, load and claims unchanged.
- For the author: the Sculley-vs-Schaeffer slot (ceiling 75) is still open; Sculley is not in inbox/.
