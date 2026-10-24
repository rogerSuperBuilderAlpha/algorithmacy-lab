---
citekey: mitchell2019model
title: Model Cards for Model Reporting
authors: Mitchell, Margaret and Wu, Simone and Zaldivar, Andrew and Barnes, Parker and Vasserman, Lucy and Hutchinson, Ben and Spitzer, Elena and Raji, Inioluwa Deborah and Gebru, Timnit
year: 2019
type: article
doi: 10.1145/3287560.3287596
venue: "Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19), Atlanta, 29–31 January 2019, pp. 220–229. ACM"
source_basis: full-text
pages_read: "arXiv:1810.03993v2 (14 Jan 2019), PDF pp. 1–4 (abstract, §§1–4.2 with Figure 1) and p. 9 (conclusion); §§4.3–5 and the example cards (Figures 2–3) skimmed, not read"
source_url: https://arxiv.org/abs/1810.03993
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/N5_prior_work_gap/mitchell2019model.txt
sha256: c4ffb7b51cd7c7d1a2b11cedd91e5004d157fa3cdf8d5ad2ca50bf0743d1a91a
manuscript_lines: [213]
ledger_rows: [P6-N05]
verified: true
written: 2026-10-14
---

Basis note: the arXiv v2 copy is the authors' version; its pagination is the arXiv PDF's, not the proceedings' pp. 220–229. Figure 1 locates the same content in any version. I set `source_basis: full-text` for the sections the manuscript uses (abstract to §4.2 and the conclusion); the rest was not read closely.

## Summary

Mitchell and colleagues propose model cards: short documents released with a trained machine-learning model that report its performance, disaggregated across cultural, demographic, phenotypic and intersectional groups, and that disclose "the context in which models are intended to be used" (abstract, p. 1). They argue that no standard documentation exists for model performance, that bias has come to light only after deployment, and that the remedy is standard disclosure modelled on hardware datasheets and the FDA's disaggregated trial reporting (§§1–2). They list the stakeholders a card serves, from practitioners and developers to policymakers and "impacted individuals," who can use a card "to pursue remedies" (§3, p. 3). Figure 1 sets out the sections: model details, intended use (primary uses, primary users, out-of-scope use cases), factors, metrics, evaluation and training data, quantitative analyses, ethical considerations, and caveats. Out-of-scope uses are framed as warnings "inspired by warning labels on food and toys" (§4.2, p. 4). The conclusion concedes that a card's usefulness and accuracy rest on "the integrity of the creator(s)" and that standardisation sufficient to prevent misleading representations is unlikely in the near term (p. 9).

## Key facts it relies on

- Abstract (p. 1): model cards "provide benchmarked evaluation in a variety of conditions" and "also disclose the context in which models are intended to be used, details of the performance evaluation procedures, and other relevant information."
- §1 (p. 1): the authors propose "short (one to two page) records we call model cards."
- §3 (p. 3): "Impacted individuals who may experience effects from a model can better understand how it works or use information in the card to pursue remedies."
- Figure 1 (p. 3), "Summary of model card sections and suggested prompts for each": under "Intended Use", the prompts "Primary intended uses", "Primary intended users", "Out-of-scope use cases".
- §4 (p. 3): the sections "are not intended to be complete or exhaustive, and may be tailored depending on the model, context, and stakeholders."
- §4.2 (p. 4): "Out-of-scope uses: Here, the model card should highlight technology that the model might easily be confused with, or related contexts that users could try to apply the model to … This section is inspired by warning labels on food and toys, and similar disclaimers presented in electronic datasheets."
- Conclusion (p. 9): "the usefulness and accuracy of a model card relies on the integrity of the creator(s) of the card itself. It seems unlikely, at least in the near term, that model cards could be standardized or formalized to a degree needed to prevent misleading representations of model results."
- Conclusion (p. 9): model cards are "one transparency tool among many," alongside "algorithmic auditing by third-parties".

## Critical notes from the literature

- Facet N5 (`literature/facets/N5_prior_work_gap.md`, l. 147–148) calls the model card "the closest existing artifact to an envelope" and names three differences: it is voluntary, it describes method and measured performance, and it "binds no one to a limit on what the system may do to a person." The authors' own conclusion supports the "binds no one" reading: the card depends on its creator's integrity (p. 9).
- The "out-of-scope" heading addresses would-be users of the model (developers who might misapply it), not the people the model acts on. A card's out-of-scope list is a warning to deployers, not a limit owed to the affected person.
- Facet N5 (l. 150) pairs it with Gebru et al. (2021), whose datasheets describe "operating characteristics": the nearest phrase in the literature to "operating envelope", and descriptive, not binding.
- Facet N5 (l. 186) records a documented gap search: "I found no work that proposes advance, binding limits on outcomes, declared to the affected person, as distinct from documentation of method or performance, in the sources above."
- `review/v3/CLOSED_LEDGER.md` (l. 593) and `MANUSCRIPT_v3_CHANGES.md` (l. 255, 418): an audit moved the citation from "does not describe how the system works" to the binding sentence and added the Figure 1 locator.

## Key topics covered

model cards, ML documentation, disaggregated evaluation, intersectional analysis, intended use, out-of-scope uses, transparency, fairness evaluation, stakeholder reporting, datasheets, voluntary disclosure

## Where the manuscript uses it

- **Line 213**, "(a model card declares 'out-of-scope use cases' but binds no one; Mitchell et al., 2019, Figure 1)". Takes the model card as the nearest existing declaration of scope and the contrast with a binding envelope. Figure 1 (p. 3) and §4.2 (p. 4) for the declaration; conclusion (p. 9) for its dependence on the creator's integrity. **holds**: a card declares out-of-scope uses, and nothing in the paper makes the declaration binding. "binds no one" is the manuscript's inference, and the conclusion supports it.
- **Line 213**, quotation "out-of-scope use cases". Exact-string check: **found with a case change**. Figure 1 prints "Out-of-scope use cases" with a capital O; the manuscript lowers the initial capital to fit the sentence (recorded in `MANUSCRIPT_v3_CHANGES.md` l. 255). The body text of §4.2 uses "Out-of-scope uses". **holds**.

## Verifier notes

- 2026-10-14. sha256 of the local arXiv v2 text matches.
- Crossref (10.1145/3287560.3287596): title, nine authors in order, FAT* proceedings, pp. 220–229, 2019 all match the card, MANUSCRIPT_v3.md reference list (l. 401) and `references.bib`. No disagreements.
- Checked all eight key-fact bullets against arXiv pp. 1, 3, 4 and 9; every quotation is verbatim (including Figure 1's "Out-of-scope use cases" and the conclusion's "integrity of the creator(s)" and "standardized or formalized").
- Line 213 use (line unchanged in v3): holds; the quotation matches Figure 1 apart from the lowered initial capital. "binds no one" is the manuscript's inference, supported by the conclusion.
- Basis: pages cited are all within the pages the card says it read; no overreach.
