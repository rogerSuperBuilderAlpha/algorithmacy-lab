---
citekey: cma2023ai
title: "AI Foundation Models: Initial Report"
authors: Competition and Markets Authority
year: 2023
type: report
doi: null
venue: Competition and Markets Authority (UK), London, 18 September 2023
source_basis: partial-text
pages_read: "cover and contents; paras 2.18-2.19 (pp. 13-14); paras 3.23-3.32 (pp. 34-36); paras 3.69-3.74 (p. 44); the cloud-inference bullet (p. 66)"
source_url: https://www.gov.uk/government/publications/ai-foundation-models-initial-report
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C3_scholarly/cma2023_foundation_models_full.pdf
sha256: 8346bc7836ce27f76feb9424da43870b82a62f7f03971725e138e20edf8ef7af
manuscript_lines: [138]
ledger_rows: [P4-058]
verified: true
written: 2026-10-14
---

Key note: the key `cma2023ai` comes from `review/v3/resolutions/C3_scholarly.bib`; `references.bib` has no entry for this report. I read the text extraction `cma2023.txt` (sha256 a486bbc5…) beside the 129-page PDF; page numbers are the report's printed folios.

## Summary
The UK Competition and Markets Authority's initial review of markets for AI foundation models (FMs), published 18 September 2023 under the Open Government Licence. It describes how FMs are built and deployed, examines competition and barriers to entry in their development, considers the impact of FMs on competition in other markets, consumer protection and the role of law, and ends with principles to guide FM markets (contents, chs. 2–7). In the sections I read, the CMA finds compute a key input. Training cost rises steeply with model size, and inference also needs heavy compute (paras 2.18, 3.24). "A handful of large technology companies" hold substantial compute; developers without data centres turn to cloud service providers (CSPs), where "only a few firms" secure partnerships, mostly with AWS, Microsoft Azure and Google Cloud (paras 3.25–3.28). Stakeholders worry that larger firms get "first in line" (para. 3.30). If models keep growing, development "may be restricted to firms that already have access to the required computational infrastructure", and this "arms race scenario could result in a concentrated market" (para. 3.71). The CMA treats this as a possible outcome, not a finding, and notes that fine-tuning may stay diverse (para. 3.72). Downstream, "most firms also need cloud computing to run the FM service for inference" (p. 66).

## Key facts it relies on
- Cover: "AI Foundation Models: Initial Report 18 September 2023"; Open Government Licence (cover, verso).
- "We have heard from stakeholders that compute required for inference can be particularly intensive at scale" (para. 2.18, p. 14).
- "A handful of large technology companies possess substantial compute resources" (para. 3.25, p. 34).
- Developers without data centres "will generally turn to cloud service providers ('CSPs') for compute", by on-demand purchase, reserved agreements or a commercial partnership, the last including "making the FM available on its cloud services for inference" (para. 3.27, pp. 34–35).
- "only a few firms have been able to secure a partnership with a CSP"; "The three main CSPs with acceleration capabilities are: Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). Typically partnerships are achieved through one of these three, although some FM developers maintain relationships with smaller providers" (para. 3.28, p. 35).
- Concern that "larger companies are more likely to get 'first in line'" for compute (para. 3.30, p. 36).
- "This arms race scenario could result in a concentrated market, with the inputs of compute and data creating high barriers to entry and/or expansion" (para. 3.71, p. 44).
- "most firms also need cloud computing to run the FM service for inference"; "Google, AWS and Microsoft (the cloud service providers or 'CSPs') supply cloud compute" (p. 66).

## Critical notes from the literature
- Resolution C3_scholarly.md (P4-058, narrower): the CMA documents concentration among cloud-compute suppliers and treats concentration in model development as possible, not established. The v3 table keeps the cell "Not established here; see Section 6", which matches.
- FIX_CHECK_B.md (P4-058, pass): para. 3.28 supports "supplied by a few cloud firms"; para. 3.27(c) covers serving (inference). FIX_CHECK_C.md: title and date match; the gov.uk URL was live.
- An initial report: much of the compute evidence is stakeholder testimony ("We have heard", "We understand", paras 2.18, 3.26, 3.28). Its UK focus shows in para. 3.31 (UK clusters lag on accelerators).
- The copyright line on the verso reads "© Crown copyright 2022" on a report dated 2023; the date on the cover and the gov.uk page is 2023.

## Key topics covered
foundation models, competition, compute, cloud service providers, AWS, Microsoft Azure, Google Cloud, barriers to entry, inference, market concentration, UK competition policy

## Where the manuscript uses it
- l. 138 (Table, "The means", today): "Compute for training and serving models supplied by a few cloud firms (Competition and Markets Authority, 2023)". Takes the claim that a few CSPs supply compute for training and for inference. Source para. 3.28, p. 35 (three main CSPs; partnerships typically through them), para. 3.27(c), pp. 34–35, and p. 66 (inference). **holds**: the CMA names three main providers and allows for smaller ones, which "a few" covers; the table's last cell leaves concentration of model development unestablished, as the CMA does.

## Verifier notes
- 2026-10-14. sha256 of the PDF recomputed: matches. Cover date "18 September 2023" and the verso "© Crown copyright 2022" are both in the text, as the card says.
- Exact-string checks on `cma2023.txt`, with folios read from the page footers: para. 2.18 (p. 14), 3.25 (p. 34), 3.27 (CSPs; inference partnership), 3.28 (p. 35), 3.30 "first in line" (p. 36), 3.71 arms race (p. 44), and the inference sentence (p. 66). All confirmed. The para. 3.28 quotation has a footnote marker (120) inside it in the source and continues "...smaller providers or a combination of providers"; the card's truncation does not change the sense.
- Bib: title, issuer, date and URL match v3 l. 301. `references.bib` now holds a `cma2023ai` entry (the card's key note says it had none); that entry agrees with the source.
- Use l. 138 (v3 table unchanged): **holds** confirmed.
