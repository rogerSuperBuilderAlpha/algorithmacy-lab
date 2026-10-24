---
citekey: crawford2014big
title: "Big Data and Due Process: Toward a Framework to Redress Predictive Privacy Harms"
authors: Crawford, Kate and Schultz, Jason
year: 2014
type: article
doi: null
venue: Boston College Law Review 55(1), 93-128
source_basis: full-text
pages_read: "pp. 93, 120-121, 125-128"
source_url: https://lira.bc.edu/works/publication-article/24a3h-ggy63
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/N2_platform_law/scholarship/crawford2014.pdf
sha256: 475ebc4db305cd8cabdded2e858ec17db3b1b33511d54f5efb1d1e82dcfd087e
manuscript_lines: [175, 225, 303]
ledger_rows: [P5-N06, P6-N08]
verified: true
written: 2026-10-14
---

Source note: the Boston College LIRA copy carries the journal pagination (running heads "[Vol. 55:93]" to
"128"); PDF page n = journal page 92+n. No DOI (the `references.bib` note records that Crossref has none). I
re-extracted the PDF with `pdftotext -layout` this session. I read the abstract and pp. 120-121 and 125-128
in full; pp. 94-119 and 122-124 were not read.

## Summary
Crawford and Schultz argue that private "Big Data" analytics create "predictive privacy harms": by
inferring detailed profiles from existing data, they widen what counts as personally identifiable
information, slip past existing privacy regimes, and can produce inaccurate profiles that "nonetheless
impact an individual's life and livelihood" (p. 93, abstract). Existing regimes offer only "limited nominal
due process-like mechanisms" (p. 93), so the authors propose a right to "procedural data due process",
modelled on due process in Anglo-American law and on Citron's work on public administrative systems. On
p. 120 they treat due process as a separation of powers: it keeps those who write rules apart from those
who enforce and judge them, whereas in Big Data there is "little or no regulation of the interactions
among the algorithm's designer (the lawmaker), the person who oversees the queries (the executive), and the
adjudicator (the computational output)". Their framework (pp. 125-128) has three parts: notice of the
predictions made and the data used (pp. 125-126), an opportunity for a hearing, possibly before "a trusted
third party who would act as a neutral data arbiter", such as the FTC (p. 127), and an impartial
adjudicator with an audit trail (pp. 127-128).

## Key facts it relies on
- Abstract: individuals affected by Big Data "should have similar rights to those in the legal system with respect to how their personal data is used in such adjudications" (p. 93).
- Due process separates those "who write the legal code from adjudicators who use it" (p. 120, citing Chapman & McConnell 2012).
- Big Data has "little or no regulation of the interactions among the algorithm's designer (the lawmaker), the person who oversees the queries (the executive), and the adjudicator (the computational output)", hence "no system of checks and balances" (p. 120).
- For-profit providers "have direct financial interests in some of the outputs they produce" (p. 120).
- Notice: those who "adjudicate" others must disclose the predictions attempted and the general sources of data, with "a mechanism to access the audit trail or record" (pp. 125-126).
- Hearing: the role "could be given to a trusted third party who would act as a neutral data arbiter to routinely examine Big Data providers"; the FTC is the example, and the arbiter would let the public "be heard, to examine the evidence used ... and to challenge it" (p. 127).
- The arbiter "could examine the relationship between those who designed the analytics and those who run the individual processes to make sure that their roles are appropriate and distinct", which "would require some form of audit trail" (pp. 127-128).

## Critical notes from the literature
- Facet N2 (`literature/facets/N2_platform_law.md:289`) notes that the paper's §4.4 and §5.4 restate proposals already made here (the "neutral data arbiter", the separation of designer, executive and adjudicator) and by Kaminski and Urban (2021) and Wachter, Mittelstadt and Floridi (2017). The paper's novelty has to lie elsewhere (the triad).
- FIX_CHECK_B (P5-N06, `review/v3/FIX_CHECK_B.md`) found that Crawford and Schultz's three roles (designer, query overseer, computational output) are not the manuscript's roles (third party, counterparty, drafter, record-keeper). The v3 wording ("a like separation") was the fix it proposed.
- From my reading: the arbiter on p. 127 investigates and hears complaints. The text does not give it power to bind the provider, and it frames the FTC's role as investigation.
- From my reading: the p. 120 passage diagnoses the absence of separation. The request that roles be kept "appropriate and distinct" comes on p. 127.

## Key topics covered
big data, predictive privacy harms, procedural due process, separation of powers, notice, hearing, neutral data arbiter, FTC, audit trail, personally identifiable information

## Where the manuscript uses it
- l. 175: "The historical safeguards assumed that these were different people; Crawford and Schultz (2014, p. 120) ask for a like separation of roles in big-data systems." Takes: a call for separating roles in big-data systems. Source: p. 120 (designer, executive, adjudicator; "little or no regulation" of their interactions); the request itself is on p. 127 ("appropriate and distinct"). **narrower**: p. 120 diagnoses the missing separation rather than asking for it, and the roles separated are lawmaker, executive and adjudicator, not the drafter, counterparty and record-keeper of the manuscript's paragraph. "Like" carries the analogy. p. 127 would be the better pin for "ask for".
- l. 225: "Crawford and Schultz (2014, p. 127) for a 'neutral data arbiter' in big data." Takes: the proposal of an independent arbiter for big-data disputes. Source: p. 127. **holds**: the proposal is on p. 127, and the manuscript does not attribute binding power to it.
  - Quotation "neutral data arbiter": exact-string check **exact** (p. 127, "act as a neutral data arbiter"; also "The presence of a neutral data arbiter" and "A neutral data arbiter could field complaints").
- l. 303 (reference entry): BCLR 55(1), 93-128. Volume and page range match the running heads. The issue number was not checked against the PDF, which prints only "[Vol. 55:93]".

## Verifier notes
- 2026-10-14. sha256 of the PDF recomputed: matches. I re-extracted it with `pdftotext -layout` and confirmed the offset from the running heads (PDF p. 28 = "120 ... [Vol. 55:93]", PDF p. 35 = "127").
- Exact-string checks by journal page: abstract phrases (p. 93); "who write the legal code from adjudicators who use it", the designer/executive/adjudicator sentence, "no system of checks and balances", "direct financial interests" (p. 120); "a mechanism to access the audit trail or record" (p. 126); "neutral data arbiter", "be heard, to examine the evidence used", "appropriate and distinct", "would require some form of audit trail" (p. 127). All present on the pages the card gives.
- Bib: authors, title, BCLR 55, 93-128 match v3 l. 303 and `references.bib`; no DOI in Crossref per the bib note. Issue "(1)" stays unconfirmed from the PDF, as the card says.
- Uses: l. 175 **narrower** confirmed (p. 120 diagnoses; the request for "appropriate and distinct" roles is on p. 127); l. 225 **holds** confirmed, quotation "neutral data arbiter" EXACT on p. 127.
