---
key: maier2022no
apa: "Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *Proceedings of the National Academy of Sciences*, *119*(31), Article e2200300119. https://doi.org/10.1073/pnas.2200300119"
authors: "Maier, Maximilian; Bartoš, František; Stanley, T. D.; Shanks, David R.; Harris, Adam J. L.; Wagenmakers, Eric-Jan"
year: 2022
title: "No evidence for nudging after adjusting for publication bias"
venue: "Proceedings of the National Academy of Sciences"
volume: "119"
issue: "31"
pages: "e2200300119"
doi: "10.1073/pnas.2200300119"
url: ""
type: article
facets: [F6]
claims: [c1]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "Final published version (PNAS Letter, 2 pages), UvA-DARE copy under CC BY with a 1-page repository cover sheet; local folder ~/iit-playground/dxd_animation_local/pdfs/maier2022no/ (maier2022no.pdf, maier2022no.txt); original URL https://pure.uva.nl/ws/files/100872641/pnas.2200300119.pdf (FETCH_LOG.tsv); read 2026-11-05; sha256 b8fd3d69d7f387853843a3b72ef09a6c7c5859a6390667a57ccd5bdf2912ac29"
verified: verified
verified_against: "maier2022no.txt (UvA-DARE PDF text layer, all 3 pages incl. cover sheet); crossref.json; openalex.json; sha256 of maier2022no.pdf recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Maier and five co-authors reanalyse the data of a large meta-analysis of nudging by Mertens et al. (their ref. 3). They start from Mertens et al.'s headline finding that choice architecture is an effective behaviour-change tool, and they argue that Mertens et al.'s own finding of "moderate publication bias" is the real headline. They point out that the Egger coefficient Mertens et al. report (b = 2.10) is "severe" by the standard they cite, and that Mertens et al. went on mostly without correcting for it. The authors apply robust Bayesian meta-analysis (RoBMA), which combines selection models with models of the link between effect size and standard error, and they report the results in Table 1 and Fig. 1.

Their result: once the bias is corrected, the overall effect is about zero (combined d = 0.04, 95% credible interval 0.00 to 0.14, BF01 = 0.95, which is indecisive rather than strong evidence for zero). There is evidence against an effect for "information" and "assistance" interventions, and the evidence is undecided for "structure" interventions. They find strong evidence of publication bias across subdomains. They also note that almost every category and domain shows heterogeneity, "which implies that some nudges might be effective." They conclude that the nudge literature in the Mertens data is "characterized by severe publication bias" and that after correction no evidence remains that nudges work as behaviour-change tools. The text read is a two-page Letter. It reports no new experiments.

## What the paper uses it for

- **c1 (contrast).** The paper says a moving goal breaks conversion-era design. If nudging barely works once publication bias is removed, conversion-era design may be weaker than c1 implies, and the paper should say it argues past this. The use is a stretch in three ways. First, Maier et al. study behaviour-change nudges in health, food, environment, finance and pro-social domains, not conversion funnels or retail interfaces. Second, they say nothing about LLM interfaces or about users whose goals shift mid-task. Third, their own text does not say nudges never work: it records heterogeneity and says some nudges might be effective. The source cuts against any sentence of the paper that treats nudging as settled evidence for conversion-era design. It does not cut against the paper's argument that such design assumes a fixed goal. Pairs with the pointer `mertens2022effectiveness` (see DECISIONS); the paper should cite Mertens et al. through its 2022 correction.

## Loci

Quotation marks inside quotations are single; none occur in these quotations as printed except where noted. "p. 1 of 2" and "p. 2 of 2" are the PNAS article's own page footers ("1 of 2", "2 of 2"). Each quotation was matched against the .txt text layer of the UvA-DARE PDF. The letter is set in two columns and the text layer interleaves them, so I rebuilt each quoted sentence from its own column.

- "when this publication bias is appropriately corrected for, no evidence for the effectiveness of nudges remains" — p. 1 of 2, opening paragraph; matched against maier2022no.txt.
- "there is an absence of evidence for an overall effect and evidence against an effect in the ‘information’ and ‘assistance’ intervention categories, whereas the evidence is undecided for ‘structure’ interventions" — p. 1 of 2, paragraph after Table 1 is introduced (the source prints these category names in double quotes; converted to single); matched against maier2022no.txt.
- "all intervention categories and domains apart from ‘finance’ show evidence for heterogeneity, which implies that some nudges might be effective" — p. 1 of 2 (the sentence runs on to "even when there is evidence against the mean effect", which ends on p. 2 of 2); source quotes "finance" in double quotes, converted to single; matched against maier2022no.txt.
- "We conclude that the ‘nudge’ literature analyzed in ref. 3 is characterized by severe publication bias." — p. 2 of 2, closing paragraph (source quotes "nudge" in double quotes, converted); matched against maier2022no.txt.
- "after correcting for this bias, no evidence remains that nudges are effective as tools for behaviour change" — p. 2 of 2, closing paragraph; matched against maier2022no.txt.

## Caution

- This is a Letter that reanalyses Mertens et al.'s data, not a new meta-analysis. The headline numbers I saw are in Table 1 (p. 2 of 2): combined random-effects estimate 0.43 [0.38, 0.48] against RoBMA 0.04 [0.00, 0.14], BF01 = 0.95. A BF01 near 1 is indecisive, not support for a zero effect. The authors themselves write "absence of evidence" for the overall effect and "evidence against" only for specific categories.
- The authors say the combined-sample results differ slightly from Mertens et al.'s moderator analysis because they analysed each subfield separately (Table 1 note). The table also carries a second RoBMA column that uses only the most precise estimate from each study; its combined value is 0.11 [0.00, 0.24], BF01 = 0.31, which the text calls "weak evidence for the overall effect."
- A footnote marked * says the analysis rests on "the corrected dataset in ref. 12", but in the printed reference list ref. 11 is the corrected Mertens data file and ref. 12 is the authors' own code and data deposit. I report this as printed and make no ruling.
- The triage note (F5-F6.md row 5, and the F2 facet entry) says Maier et al. still find heterogeneity "which implies that some nudges might be effective" (p. 1). I re-read it from this copy: it is there, p. 1 of 2.
- The UvA-DARE copy adds a repository cover page and a "Downloaded from pnas.org" stamp dated 13 December 2022; neither is part of the article. The PNAS article number is e2200300119; its volume and issue (119, 31) come from the printed footer and the cover citation.
- Maier et al. quote Mertens et al. ("an effective and widely applicable behavior change tool", p. 8 of Mertens). I did not read Mertens et al. here. Do not cite that phrase from this card.

## Verification

2026-11-05 · S6 verifier, batch b05 (opus; not the writer) · verdict: verified · checked: loci 5/5 found in maier2022no.txt (column-interleaved layout; each sentence rebuilt from its column), locators p. 1 of 2 / p. 2 of 2 confirmed; authors, year 2022, title, venue, 119(31), article number e2200300119 and DOI agree with crossref.json, openalex.json and the printed footer; Table 1 figures (0.43 [0.38, 0.48]; 0.04 [0.00, 0.14], BF01 = 0.95; 0.11 [0.00, 0.24], BF01 = 0.31) and the ref. 11 / ref. 12 footnote mismatch confirmed as printed; full_text depth honest (2-page Letter read whole); sha256 b8fd3d69… recomputed and matches · changed: nothing
