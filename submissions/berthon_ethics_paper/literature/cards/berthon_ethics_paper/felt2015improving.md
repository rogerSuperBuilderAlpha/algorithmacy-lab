---
citekey: felt2015improving
title: "Improving SSL Warnings: Comprehension and Adherence"
authors: Felt, Adrienne Porter; Ainslie, Alex; Reeder, Robert W.; Consolvo, Sunny; Thyagaraja, Somas; Bettes, Alan; Harris, Helen; Grimes, Jeff
year: 2015
type: article
doi: 10.1145/2702123.2702442
venue: CHI '15 (Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems), pp. 2893-2902
source_basis: partial-text
pages_read: "p. 2893 (abstract, introduction), p. 2895 (field data on adherence), p. 2900 (field experiment results, Table 5)"
source_url: https://research.google.com/pubs/archive/43265.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/R5/felt2015/felt2015.pdf
sha256: 1bb91af19c84f15506d89863179c461a053cd9cbbc6ac5531f0029d4ccb0c65f
manuscript_lines: [530, 531, 532, 541, 542]
ledger_rows: [D07, D06]
premises: [B1, CB]
facet: R5
supersedes: null
anthropic_authored: false
verified: pending
written: 2026-10-24
---

## Summary
Google's redesign of the Chrome SSL warning, tested by surveys and a field experiment on 17,787 users and then shipped
in Chrome 37. The team set out to make the warning understood and failed; it then changed the medium instead of the
text ("opinionated design": a visual layout that makes the safe choice the obvious one) and raised adherence from 30.9
to 58.3 percent. It is the cleanest implementation in the literature of D07's claim that a safeguard at the point of
use can work without the person understanding the process, and of D06's premise that comprehension cannot be assumed.
Printed page = PDF page + 2892, confirmed by Crossref pagination (2893-2902).

## Key facts it relies on
- Abstract (p. 2893): "We ultimately failed at our goal of a well-understood warning. However, nearly 30% more total
  users chose to remain safe after seeing our warning. We attribute this success to opinionated design, which promotes
  safety with visual cues."
- p. 2893: "Comprehension is our preferred goal, but adherence is an alternative if and when we cannot achieve
  comprehension."
- p. 2895: "Unfortunately, users adhered to only 30% of Google Chrome SSL warnings [1]."
- p. 2900, Table 5: original text and design 30.9% adherence (N = 4,551); proposed text with proposed grey design
  58.3% (N = 4,633). "Opinionated design substantially improved adherence."

## Critical notes from the literature
- Browser warnings protect the user of the browser; the designer and the protected party share an interest. D07 asks an
  operator to mark its own agent's denials for a person whose interest it may not share, which the SSL case does not
  test. Buçinca et al. (`dxf/bucinca2021trust`) show forcing functions are disliked; Vasconcelos et al.
  (`vasconcelos2023explanations`) show explanations reduce overreliance when the task is hard.

## Where the argument uses it
- **D07 (draft lines 530-532) and D06.** A working precedent for "change the medium" that does not depend on a
  measured health effect (unlike the grade card after `ho2019new`). It also supplies the premise D06 states: the
  designers tested comprehension, found it could not be secured, and carried the consequence by redesign. Verdict:
  D07 **holds**, with its precedent moved from the grade card to a case where the marker's author and the person
  protected are not adverse; the adverse case remains to be shown.

## Verifier notes
